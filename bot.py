import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='A bot that does stuff.', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')