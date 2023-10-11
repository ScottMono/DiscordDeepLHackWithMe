# DiscordDeepLBot Hack-with-me v5

Version 5 extends upon V4 by loading all cogs without needing to specify one each time

```python
    async def setup_hook(self):
        self.background_task.start()
        # loading all cogs
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
```