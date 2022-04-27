import discord
import os
import requests
import json
import random
from dotenv import load_dotenv

# load dotenv
env_path = '.env'
load_dotenv(dotenv_path=env_path)

client = discord.Client()

sad_words = ['sad', 'depression', 'unhappy', 'angry', 'miserable']

starter_encouragements = [
    'Be happy!',
    'Hang in there!',
    'You are a great person!',
    "Don't worry!",
]

def get_quote_from_api():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$inspire"):

        quote = get_quote_from_api()

        await message.channel.send(quote)

    else:
        for sad in sad_words:
            if sad in message.content.lower:
                await message.channel.send(starter_encouragements)

client.run(os.getenv('TOKEN'))
