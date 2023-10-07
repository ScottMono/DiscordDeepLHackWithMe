import asyncio
import discord
from discord.ext import commands


class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='demo')
    async def command(self, ctx, argument):
        await self.bot.say("Stuff")

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)


async def setup(bot):
    await bot.add_cog(Example(bot))
