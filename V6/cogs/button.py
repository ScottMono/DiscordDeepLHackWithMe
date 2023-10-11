import os

import deepl
import discord
from discord.ext import commands
from dotenv import load_dotenv

from translation.translate import Translate


class ButtonShitView(discord.ui.View, commands.Cog):
    def __init__(self, bot, message_content):
        self.replied_message_content = message_content
        super().__init__()
        self.bot = bot
    SELECT_OPTIONS = [
        discord.SelectOption(label='Bulgarian', value="BG", description='stuff', emoji="🇧🇬"),
        discord.SelectOption(label='Czech', value="CS", description='stuff also', emoji="🇨🇿"),
        discord.SelectOption(label='Danish', value="DA", description='stuff', emoji="🇩🇰"),
        discord.SelectOption(label='German', value="DE", description='stuff', emoji="🇩🇪"),
        discord.SelectOption(label='Greek', value="EL", description='stuff also', emoji="🇬🇷"),
        discord.SelectOption(label='English', value="EN", description='stuff', emoji="🇩🇪"),
        discord.SelectOption(label='Spanish', value="ES", description='stuff also', emoji="🇬🇧"),
        discord.SelectOption(label='Estonian', value="ET", description='stuff', emoji="🇪🇪"),
        discord.SelectOption(label='Finnish', value="FI", description='stuff also', emoji="🇫🇮"),
        discord.SelectOption(label='French', value="FR", description='stuff also', emoji="🇫🇷"),
        discord.SelectOption(label='Hungarian', value="HU", description='stuff', emoji="🇭🇺"),
        discord.SelectOption(label='Indonesian', value="ID", description='stuff also', emoji="🇮🇩"),
        discord.SelectOption(label='Italian', value="IT", description='stuff', emoji="🇮🇹"),
        discord.SelectOption(label='Japanese', value="JP", description='stuff also', emoji="🇯🇵"),
        discord.SelectOption(label='Korean', value="KO", description='stuff', emoji="🇰🇷"),
        discord.SelectOption(label='Lithuanian', value="LT", description='stuff also', emoji="🇱🇹"),
        discord.SelectOption(label='Latvian', value="LV", description='stuff', emoji="🇱🇻"),
        discord.SelectOption(label='Norwegian (Bokmål)', value="NB", description='stuff also', emoji="🇳🇴"),
        discord.SelectOption(label='Dutch', value="NL", description='stuff', emoji="🇳🇱"),
        # discord.SelectOption(label='Polish', value="PL", description='stuff also', emoji="🇵🇱"),
        # discord.SelectOption(label='Portuguese', value="PT-PT", description='stuff', emoji="🇵🇹"),
        # discord.SelectOption(label='Portuguese (Brazilian)', value="PT-BR", description='stuff also', emoji="🇧🇷"),
        # discord.SelectOption(label='Romanian', value="RO", description='stuff', emoji="🇷🇴"),
        # discord.SelectOption(label='Russian', value="RU", description='stuff also', emoji="🇷🇺"),
        # discord.SelectOption(label='Slovak', value="SK", description='stuff', emoji="🇸🇰"),
        # discord.SelectOption(label='Slovenian', value="SL", description='stuff also', emoji="🇸🇮"),
        # discord.SelectOption(label='Swedish', value="SV", description='stuff', emoji="🇸🇪"),
        # discord.SelectOption(label='Turkish', value="TR", description='stuff also', emoji="🇹🇷"),
        # discord.SelectOption(label='Ukrainian', value="UK", description='stuff', emoji="🇺🇦"),
        # discord.SelectOption(label='Chinese (simplified)', value="ZH", description='stuff also', emoji="🇨🇳"),
        discord.SelectOption(label='Go Back', value="4", description='Go Back!!!', emoji='↩️')
    ]

    @discord.ui.select(placeholder='Select one', options=SELECT_OPTIONS, max_values=1)
    async def select_option_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        x = interaction
        load_dotenv()

        # populate AUTH_KEY with the values from our .env file
        auth_key = os.getenv("AUTH_KEY")

        translator = Translate(auth_key=auth_key, bot=self.bot)
        if self.replied_message_content is not None:
            print(self.replied_message_content)
            translated = translator.translate_message(self.replied_message_content, select.values[0])
            await interaction.response.send_message(translated)
            return
        return

    @commands.command(name='button')
    async def button(self, ctx):
        if ctx.message.reference is not None:
            resolved = ctx.message.reference.resolved
            await resolved.reply(content="Pick a translation option", view=ButtonShitView(bot=self.bot, message_content=resolved.content))
            return

        await ctx.message.channel.send("Pick a translation option", view=ButtonShitView(bot=self.bot, message_content=None))


async def setup(bot):
    await bot.add_cog(ButtonShitView(bot=bot, message_content=None))