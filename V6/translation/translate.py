import os

import deepl
from discord.ext import commands
from dotenv import load_dotenv


class Translate:
    def __init__(self, bot, auth_key):
        self.bot = bot
        self.translator = deepl.Translator(auth_key)

    # starting point/testing for role assignment based upon random shit. Will eventually swap to when a user joins

    async def reply_processing(self, ctx, *args):
        if len(args) > 0:
            if ctx.message.reference is not None:
                thread = None
                for translate_to in args:
                    translated = await self.translate_from_reply(ctx.message.reference.resolved, translate_to)
                    thread = await self.threads(translated, ctx.message.reference.resolved, thread)

    async def guild_test_processing(self, message):
        if message.content.startswith('!guild'):
            guild_roles = message.guild.roles
            for role in guild_roles:
                if role.name == 'test':
                    await message.author.add_roles(role, reason="Triggered by bot command", atomic=True)
                    break

            # await message.channel.send(guild_roles)

    async def threads(self, translated_message, message, thread):
        if thread is not None:
            await thread.send(content=translated_message)
            return thread
        if translated_message is not None:
            translation_thread_to_message = await message.create_thread(name='Translated via reply',
                                                                        auto_archive_duration=60, slowmode_delay=None,
                                                                        reason='Translation trigger by reaction')
            await translation_thread_to_message.send(content=translated_message)
            return translation_thread_to_message
        return

    async def translate_from_reply(self, message, target_lang):
        if message is not None:
            translated_message = None
            match target_lang:
                case "BG":
                    translated_message = self.translate_message(message.content, "BG")
                case "CZ":
                    translated_message = self.translate_message(message.content, "CS")
                case "DK":
                    translated_message = self.translate_message(message.content, "DA")
                case "DE":
                    translated_message = self.translate_message(message.content, "DE")
                case "GR":
                    translated_message = self.translate_message(message.content, "EL")
                case "EN":
                    translated_message = self.translate_message(message.content, "EN")
                case "US":
                    translated_message = self.translate_message(message.content, "EN-US")
                case "ES":
                    translated_message = self.translate_message(message.content, "ES")
                case "EE":
                    translated_message = self.translate_message(message.content, "ET")
                case "FI":
                    translated_message = self.translate_message(message.content, "FI")
                case "FR":
                    translated_message = self.translate_message(message.content, "FR")
                case "HU":
                    translated_message = self.translate_message(message.content, "HU")
                case "ID":
                    translated_message = self.translate_message(message.content, "ID")
                case "IT":
                    translated_message = self.translate_message(message.content, "IT")
                case "JP":
                    translated_message = self.translate_message(message.content, "JP")
                case "KR":
                    translated_message = self.translate_message(message.content, "KO")
                case "LT":
                    translated_message = self.translate_message(message.content, "LT")
                case "LV":
                    translated_message = self.translate_message(message.content, "LV")
                case "NO":
                    translated_message = self.translate_message(message.content, "NB")
                case "NL":
                    translated_message = self.translate_message(message.content, "NL")
                case "PL":
                    translated_message = self.translate_message(message.content, "PL")
                case "PT":
                    translated_message = self.translate_message(message.content, "PT-PT")
                case "BR":
                    translated_message = self.translate_message(message.content, "PT-BR")
                case "RO":
                    translated_message = self.translate_message(message.content, "RO")
                case "RU":
                    translated_message = self.translate_message(message.content, "RU")
                case "SK":
                    translated_message = self.translate_message(message.content, "SK")
                case "SI":
                    translated_message = self.translate_message(message.content, "SL")
                case "SE":
                    translated_message = self.translate_message(message.content, "SV")
                case "TR":
                    translated_message = self.translate_message(message.content, "TR")
                case "UA":
                    translated_message = self.translate_message(message.content, "UK")
                case "CN":
                    translated_message = self.translate_message(message.content, "ZH")
                case _:
                    return

            return translated_message

    # translate a message

    def translate_message(self, message, target_language):
        return self.translator.translate_text(message, target_lang=target_language)
