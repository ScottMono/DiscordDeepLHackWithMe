# importing discord things
import discord
from discord.ext import commands, tasks

# importing os and dotenv to load up the deepl auth key I have stored in my .env file
import os
from dotenv import load_dotenv

# import logging
import logging

# use the load_dotenv function to load the .env file
load_dotenv()

# populate BOT_TOKEN with the values from our .env file
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")


class DeeplyBot(commands.Bot):
    def __init__(self):
        # setup intents to read message content
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        intents.reactions = True
        super().__init__(command_prefix='$', intents=intents)

    async def setup_hook(self):
        self.background_task.start()
        # loading all cogs
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')

    async def close(self):
        await super().close()

    @tasks.loop(minutes=10)
    async def background_task(self):
        print('Running background task...')

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


# assign a logger handler and then run our discord bot client
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')


x = DeeplyBot()
x.run(token=BOT_TOKEN, log_handler=handler, log_level=logging.DEBUG)
