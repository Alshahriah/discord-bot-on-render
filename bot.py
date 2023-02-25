import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from webserver import keep_alive
load_dotenv()

bot = commands.Bot(command_prefix='!', description='A bot that does stuff.', intents=discord.Intents.all())
token = os.getenv('DISCORD_TOKEN')
has_run = bool

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
    await bot.load_extension('jishaku')

if has_run == False:
    keep_alive()
    bot.run(token)
has_run = True