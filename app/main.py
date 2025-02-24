from portfolio_manager import get_portfolio_updates 

import discord
import asyncio
import logging
import os

_log = logging.getLogger('discord')

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
CHANNEL_ID = os.environ['CHANNEL_ID']

STANDARD_MESSAGE = "🚀🔥🚀🔥**Ludolph has made a trade:**🚀🔥🚀🔥\n\n"

intents = discord.Intents.default()
client = discord.Client(intents=intents)


async def send_portfolio_updates():
    """Fetch portfolio updates and send them as a message every 5 minutes."""
    await client.wait_until_ready()
    channel = client.get_channel(int(CHANNEL_ID))

    while not client.is_closed():
        bought_stocks, sold_stocks = await get_portfolio_updates()

        message = STANDARD_MESSAGE
        if bought_stocks:
            message += f"📈**Bought Stocks:** {', '.join(bought_stocks)}\n\n"
        if sold_stocks:
            message += f"📉**Sold Stocks:** {', '.join(sold_stocks)}\n"

        if message != STANDARD_MESSAGE: 
        # Send message
            if channel:
                await channel.send(message)
                _log.info(f"Sent portfolio updates.")
            else:
                _log.error("Invalid channel ID.")

        await asyncio.sleep(60)  # Wait for 1 minute

@client.event
async def on_ready():
    _log.info(f'Logged in as {client.user}')
    asyncio.create_task(send_portfolio_updates())  # Start initial background task

client.run(DISCORD_TOKEN)
