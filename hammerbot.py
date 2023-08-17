# bot.py
import asyncio
import logging
import os
import random

import aiohttp
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix="")
logging.basicConfig(level=logging.INFO)


async def load_cogs():
    for folder in os.listdir("cog_modules"):
        if os.path.exists(os.path.join("cog_modules", folder, "cog.py")):
            await bot.load_extension(f"cog_modules.{folder}.cog")
            print(f"{folder} cog loaded")
        else:
            print(f"{folder} cog NOT loaded")


@bot.event
async def on_ready():
    game = discord.Game("with AoE2 data")
    await bot.change_presence(activity=game)
    await load_cogs()


bot.run(TOKEN)
