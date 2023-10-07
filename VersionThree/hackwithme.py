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


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print("in here")
        translated = translate_message("hello", "DE")
        await message.channel.send(translated)

    if message.content.startswith('$translate'):
        print('in translate')
        translated = translate_message(message.content[10:], "DE")
        await message.channel.send(translated)


@client.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji
    await translate_emoji_flag(emoji, reaction)


async def translate_emoji_flag(emoji, reaction):
    if emoji is not None:
        translated_message = None
        match emoji:
            case "🇧🇬":
                translated_message = translate_message(reaction.message, "BG")
            case "🇨🇿":
                translated_message = translate_message(reaction.message, "CS")
            case "🇩🇰":
                translated_message = translate_message(reaction.message, "DA")
            case "🇩🇪":
                translated_message = translate_message(reaction.message, "DE")
            case "🇬🇷":
                translated_message = translate_message(reaction.message, "EL")
            case "🇬🇧":
                translated_message = translate_message(reaction.message, "EN")
            case "🇺🇸":
                translated_message = translate_message(reaction.message, "EN-US")
            case "🇪🇸":
                translated_message = translate_message(reaction.message, "ES")
            case "🇪🇪":
                translated_message = translate_message(reaction.message, "ET")
            case "🇫🇮":
                translated_message = translate_message(reaction.message, "FI")
            case "🇫🇷":
                translated_message = translate_message(reaction.message, "FR")
            case "🇭🇺":
                translated_message = translate_message(reaction.message, "HU")
            case "🇮🇩":
                translated_message = translate_message(reaction.message, "ID")
            case "🇮🇹":
                translated_message = translate_message(reaction.message, "IT")
            case "🇯🇵":
                translated_message = translate_message(reaction.message, "JP")
            case "🇰🇷":
                translated_message = translate_message(reaction.message, "KO")
            case "🇱🇹":
                translated_message = translate_message(reaction.message, "LT")
            case "🇱🇻":
                translated_message = translate_message(reaction.message, "LV")
            case "🇳🇴":
                translated_message = translate_message(reaction.message, "NB")
            case "🇳🇱":
                translated_message = translate_message(reaction.message, "NL")
            case "🇵🇱":
                translated_message = translate_message(reaction.message, "PL")
            case "🇵🇹":
                translated_message = translate_message(reaction.message, "PT")
            case "🇧🇷":
                translated_message = translate_message(reaction.message, "PT-BR")
            case "🇷🇴":
                translated_message = translate_message(reaction.message, "RO")
            case "🇷🇺":
                translated_message = translate_message(reaction.message, "RU")
            case "🇸🇰":
                translated_message = translate_message(reaction.message, "SK")
            case "🇸🇮":
                translated_message = translate_message(reaction.message, "SL")
            case "🇸🇪":
                translated_message = translate_message(reaction.message, "SV")
            case "🇹🇷":
                translated_message = translate_message(reaction.message, "TR")
            case "🇺🇦":
                translated_message = translate_message(reaction.message, "UK")
            case "🇨🇳":
                translated_message = translate_message(reaction.message, "ZH")
            case _:
                return

        if translated_message is not None:
            translation_thread_to_message = await reaction.message.create_thread(name='Translated via reaction', auto_archive_duration=60, slowmode_delay=None, reason='Translation trigger by reaction')
            await translation_thread_to_message.send(content=translated_message)


# translate a message


def translate_message(message, target_language):
    return translator.translate_text(message.content, target_lang=target_language)


# assign a logger handler and then run our discord bot client
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

client.run(token=BOT_TOKEN, log_handler=handler, log_level=logging.DEBUG)
