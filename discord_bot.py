import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print("bot is ready")

@bot.command()
async def hello(ctx):
    await ctx.send('Hi Zanan')



bot.run('Nzg3NDI4ODQyOTgwNzY5ODQz.X9U0QQ.IRB0mK_cUfVvrxVhBo_pTZzSbos')