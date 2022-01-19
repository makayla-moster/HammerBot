# bot.py
import os, discord, random, logging
import aiohttp, asyncio
from dotenv import load_dotenv
from discord.ext import tasks, commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')
# LUKE = os.getenv('LUKE_ID')

bot = commands.Bot(command_prefix='')

for folder in os.listdir("cog_modules"):
    if os.path.exists(os.path.join("cog_modules", folder, "cog.py")):
        bot.load_extension(f"cog_modules.{folder}.cog")


@bot.event
async def on_ready():
    game = discord.Game("with AoE2 data")
    await bot.change_presence(activity=game)

bot.run(TOKEN)
