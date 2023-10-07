# DiscordDeepLBot Hack-with-me v2

Version 2 does a little more in the ways of translating by using the $translate command. Still doesn't allow language selection

```python
import deepl

import discord

# importing os and dotenv to load up the deepl auth key I have stored in my .env file
import os
from dotenv import load_dotenv

# import logging
import logging

# use the load_dotenv function to load the .env file
load_dotenv()

# populate AUTH_KEY and BOT_TOKEN with the values from our .env file
AUTH_KEY = os.getenv("AUTH_KEY")
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# create a translator instance
translator = deepl.Translator(AUTH_KEY)
# event for when the bot is ready

# This example requires the 'message_content' intent.
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


# on_ready event override
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# on_message event override
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print("in here")
        translated = translate_message("hello", "DE")
        await message.channel.send(translated)

    # substring from the end of $translate and translate that
    if message.content.startswith('$translate'):
        print('in translate')
        translated = translate_message(message.content[10:], "DE")
        await message.channel.send(translated)


# translate a message
def translate_message(message, target_language):
    return translator.translate_text(message, target_lang=target_language)


# assign a logger handler and then run our discord bot client
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

client.run(token=BOT_TOKEN, log_handler=handler, log_level=logging.DEBUG)

```