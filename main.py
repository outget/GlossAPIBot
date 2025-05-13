import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

class GlossAPIBot(commands.Bot):
    def __init__(self):
        self.description = "GlossAPI Discord App"

        super().__init__(
            command_prefix={"."},
            intents=discord.Intents.all(),
            description=self.description,
            case_insensitive=True, 
        )

    async def on_ready(self):
        print(f'Logged on as {self.user}')

bot = GlossAPIBot()

async def is_channel(ctx):
    return ctx.channel.id == 1371865752654712842


@bot.command()
@commands.check(is_channel)
async def announce(ctx, *, arg):
    channel = bot.get_channel(1371779191623647314)
    await channel.send(arg) # type: ignore
    await ctx.message.delete()

@bot.command()
@commands.check(is_channel)
async def clear(ctx, amount: int = 0):
    if amount:
        await ctx.channel.purge(limit=amount + 1)
    else:
        await ctx.channel.purge()

@announce.error
async def announce_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        print('Invalid channel!')

load_dotenv()
token = os.getenv('TOKEN')

bot.run(token) # type: ignore
