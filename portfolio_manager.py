import requests
import json

url = "https://investspiel.de/z/portfolio_assets?portfolio_id=583456&lang=de"

async def get_portfolio_updates():

    response = requests.request("GET", url)

    assets = response.json()["Assets"][1:]

    request_companies = []
    for asset in assets:
        request_companies.append(asset['Name'])


    # Load the companies from the JSON file
    with open('companies.json', 'r') as f:
        companies_from_file = json.load(f)



    bought_stocks = [company for company in request_companies if company not in companies_from_file['companies']]
    sold_stocks = [company for company in companies_from_file['companies'] if company not in request_companies]



    with open('companies.json', 'w') as f:
        json.dump({"companies": request_companies}, f)

    return bought_stocks,sold_stocks