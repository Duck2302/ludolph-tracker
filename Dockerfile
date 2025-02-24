FROM python:3.12.3-slim

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD ./app /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt --root-user-action=ignore


# Run app.py when the container launches
#future setup script: # Run setup shell script 
CMD [ "python", "./main.py"]