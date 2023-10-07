# DiscordDeepLBot Hack-with-me v4

Version 4 moves to the newer implementation of discordpy. This means we have to move to using async for our main function. This also allows us to utilise cogs, and start being a little smarter with the commands. 

As of V4 code will be snippets, not entire file as we are using multiple files from this version

The largest change in this version is the translation cog allowing us to handle arguments passed with the command. This is done with the following snippet
```python
@commands.command(name='translate')
    async def reply_processing(self, ctx, *args):
        if len(args) > 0:
            if ctx.message.reference is not None:
                thread = None
                for translate_to in args:
                    translated = await self.translate_from_reply(ctx.message.reference.resolved, translate_to)
                    thread = await self.threads(translated, ctx.message.reference.resolved, thread)

```