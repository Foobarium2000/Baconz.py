import discord
from discord.ext import commands

TOKEN = 'NjkwMTE4NDkwNzUyOTQyMDgw.XnmFAw.GXudfyL2dNEG9QpJRKnAxEff3WE'

description = '''idfk'''
bot = commands.Bot(command_prefix='baconz ', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def ping(ctx):
    """later(tm)"""
    await ctx.send("brug moment")
    
bot.run(TOKEN)