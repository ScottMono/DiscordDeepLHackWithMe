import os

import deepl
from discord.ext import commands
from dotenv import load_dotenv


class Translation(commands.Cog):
    def __init__(self, bot, translator):
        self.bot = bot
        self.translator = translator

    @commands.command
    async def on_ready(self):
        print(f'Logged in as {self.bot.user} (ID: {self.bot.user.id})')
        print('------')

    # event for when a message is sent. Hook into the message and check values then react accordingly

    @commands.command
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        await self.guild_test_processing(message)

        await self.bot.process_commands(message)

    @commands.command(name='translate')
    async def reply_processing(self, ctx, *args):
        if len(args) > 0:
            if ctx.message.reference is not None:
                thread = None
                for translate_to in args:
                    translated = await self.translate_from_reply(ctx.message.reference.resolved, translate_to)
                    thread = await self.threads(translated, ctx.message.reference.resolved, thread)

    async def translation_reply(self, message):
        if message.content.startswith('!translate'):
            return

    @commands.command(name='help_translate')
    async def translation_help(self, message):
        await message.channel.send('Want to translate a message? Simply reply to a message with the command $translate '
                                   'and one or more of the following language codes BG, CS, DA, DE, EL, EN, US, ES, ET, '
                                   'FI, FR, HU, ID, IT, JP, KO, LT, LV, NB, NL, PL, PT, BR, RO, RU, SK, SL, SV, TR, UK, ZH')

    async def on_reaction_add(self, reaction, user):
        return

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
                    translated_message = self.translate_message(message, "BG")
                case "CZ":
                    translated_message = self.translate_message(message, "CS")
                case "DK":
                    translated_message = self.translate_message(message, "DA")
                case "DE":
                    translated_message = self.translate_message(message, "DE")
                case "GR":
                    translated_message = self.translate_message(message, "EL")
                case "EN":
                    translated_message = self.translate_message(message, "EN")
                case "US":
                    translated_message = self.translate_message(message, "EN-US")
                case "ES":
                    translated_message = self.translate_message(message, "ES")
                case "EE":
                    translated_message = self.translate_message(message, "ET")
                case "FI":
                    translated_message = self.translate_message(message, "FI")
                case "FR":
                    translated_message = self.translate_message(message, "FR")
                case "HU":
                    translated_message = self.translate_message(message, "HU")
                case "ID":
                    translated_message = self.translate_message(message, "ID")
                case "IT":
                    translated_message = self.translate_message(message, "IT")
                case "JP":
                    translated_message = self.translate_message(message, "JP")
                case "KR":
                    translated_message = self.translate_message(message, "KO")
                case "LT":
                    translated_message = self.translate_message(message, "LT")
                case "LV":
                    translated_message = self.translate_message(message, "LV")
                case "NO":
                    translated_message = self.translate_message(message, "NB")
                case "NL":
                    translated_message = self.translate_message(message, "NL")
                case "PL":
                    translated_message = self.translate_message(message, "PL")
                case "PT":
                    translated_message = self.translate_message(message, "PT-PT")
                case "BR":
                    translated_message = self.translate_message(message, "PT-BR")
                case "RO":
                    translated_message = self.translate_message(message, "RO")
                case "RU":
                    translated_message = self.translate_message(message, "RU")
                case "SK":
                    translated_message = self.translate_message(message, "SK")
                case "SI":
                    translated_message = self.translate_message(message, "SL")
                case "SE":
                    translated_message = self.translate_message(message, "SV")
                case "TR":
                    translated_message = self.translate_message(message, "TR")
                case "UA":
                    translated_message = self.translate_message(message, "UK")
                case "CN":
                    translated_message = self.translate_message(message, "ZH")
                case _:
                    return

            return translated_message

    # translate a message

    def translate_message(self, message, target_language):
        return self.translator.translate_text(message.content, target_lang=target_language)


async def setup(bot):
    load_dotenv()

    # populate AUTH_KEY with the values from our .env file
    AUTH_KEY = os.getenv("AUTH_KEY")
    # create a translator instance
    translator = deepl.Translator(AUTH_KEY)
    await bot.add_cog(Translation(bot, translator))