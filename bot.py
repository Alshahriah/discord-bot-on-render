import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix='!', description='A bot that does stuff.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
    await bot.load_extension('jishaku')

bot.run(os.getenv('TOKEN2'))