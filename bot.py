import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from webserver import keep_alive
import threading

load_dotenv()

bot = commands.Bot(command_prefix='!', description='A bot that does stuff.', intents=discord.Intents.all())
token = os.getenv('DISCORD_TOKEN')

# Create a lock object
lock = threading.Lock()

@bot.event
async def on_ready():
    with lock:
        if not getattr(on_ready, "has_run", False):
            on_ready.has_run = True
            print(f'{bot.user.name} has connected to Discord!')
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    await bot.load_extension(f'cogs.{filename[:-3]}')
            await bot.load_extension('jishaku')

# Start the web server to keep the bot alive
keep_alive()

# Start the bot
bot.run(token)
