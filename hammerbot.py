# bot.py
import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
import logging

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix='')
@bot.command(name='30', help='Returns AoE2 taunt #30.')
@commands.cooldown(1, 30, commands.BucketType.user)
async def monkNoise(ctx):
    response = "Wololo!"
    await ctx.send(response)
@monkNoise.error
async def  clearError(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Return because we don't want to show an error for every command not found
    elif isinstance(error, commands.CommandOnCooldown):
        message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
    await ctx.send(message)

@bot.command(name='14', help='Returns AoE2 taunt #14.')
@commands.cooldown(1, 30, commands.BucketType.user)
async def startTheGame(ctx):
    response = "Start the game already!"
    await ctx.send(response)
@startTheGame.error
async def  clearError(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Return because we don't want to show an error for every command not found
    elif isinstance(error, commands.CommandOnCooldown):
        message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
    await ctx.send(message)


@bot.command(name='!civ', help='Returns AoE2 civ tech tree information.')
@commands.cooldown(1, 10, commands.BucketType.user)
async def civInfo(ctx, arg):
    age_civs = ['britons', 'byzantines', 'celts', 'chinese', 'franks', 'goths', 'japanese', 'mongols', 'persians', 'saracens', 'teutons', 'turks', 'vikings', 'aztecs', 'huns', 'koreans', 'mayans', 'spanish', 'incas', 'indians', 'italians', 'magyars', 'slavs', 'berbers', 'ethiopians', 'malians', 'portuguese', 'burmese', 'khmer', 'malay', 'vietnamese', 'bulgarians', 'cumans', 'lithuanians', 'tatars', 'burgundians', 'sicilians', 'bohemians', 'poles']
    if arg.lower() in age_civs:
        response = "https://aoe2techtree.net/#" + str(arg.lower())
    else:
        response = arg + " is not a current AoE 2 civ."
    await ctx.send(response)
@civInfo.error
async def  clearError(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Return because we don't want to show an error for every command not found
    elif isinstance(error, commands.CommandOnCooldown):
        message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
    await ctx.send(message)


@bot.event
async def on_ready():
    feedChannel = int(os.getenv('BOT_FEED_LOG'))
    await bot.get_channel(feedChannel).send("HammerBot is online!")

bot.run(TOKEN)
