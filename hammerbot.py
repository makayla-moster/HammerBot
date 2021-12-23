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

@bot.command(name='13', help='Returns AoE2 taunt #13.')
@commands.cooldown(1, 30, commands.BucketType.user)
async def isp(ctx):
    response = "Sure, blame it on your ISP."
    await ctx.send(response)
@isp.error
async def  clearError(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Return because we don't want to show an error for every command not found
    elif isinstance(error, commands.CommandOnCooldown):
        message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
    await ctx.send(message)

@bot.command(name='age?', help='Returns AoE2 taunt #30.')
@commands.cooldown(1, 30, commands.BucketType.user)
async def questionableAge(ctx):
    response = "Well, duh."
    await ctx.send(response)
@questionableAge.error
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


@bot.command(name='!randomciv', help='Returns a random AoE2 civ. [arg1] = flank or pocket or number, [arg2] = number')
@commands.cooldown(1, 10, commands.BucketType.user)
async def randomCiv(ctx, arg1=None, arg2=None):
    reponse = ''
    age_civs = ['Britons', 'Byzantines', 'Celts', 'Chinese', 'Franks', 'Goths', 'Japanese', 'Mongols', 'Persians', 'Saracens', 'Teutons', 'Turks', 'Vikings', 'Aztecs', 'Huns', 'Koreans', 'Mayans', 'Spanish', 'Incas', 'Indians', 'Italians', 'Magyars', 'Slavs', 'Berbers', 'Ethiopians', 'Malians', 'Portuguese', 'Burmese', 'Khmer', 'Malay', 'Vietnamese', 'Bulgarians', 'Cumans', 'Lithuanians', 'Tatars', 'Burgundians', 'Sicilians', 'Bohemians', 'Poles']
    pocket_civs = []
    flank_civs =[]
    if (arg1 == None) and (arg2 == None):
        response = random.choice(age_civs)
    elif arg1.isnumeric():
        for i in range(int(arg1)):
            if i == 0:
                response = random.choice(age_civs)
            else:
                response += "\n" + random.choice(age_civs)
    elif (arg1.lower() == 'flank'):
        if arg2 != None:
            if arg2.isnumeric():
                for i in range(int(arg2)):
                    if i == 0:
                        response = random.choice(age_civs)
                    else:
                        response += "\n" + random.choice(age_civs)
            else:
                response = "Not in correct format. !randomciv [optional (flank/pocket/number)] [optional (number)]"
        else:
            response = random.choice(age_civs)
    elif (arg1.lower() == 'pocket'):
        if arg2 != None:
            if arg2.isnumeric():
                for i in range(int(arg2)):
                    if i == 0:
                        response = random.choice(age_civs)
                    else:
                        response += "\n" + random.choice(age_civs)
            else:
                response = "Not in correct format. !randomciv [optional (flank/pocket/number)] [optional (number)]"
        else:
            response = random.choice(age_civs)
    else:
        response = "Not in correct format. !randomciv [optional (flank/pocket/number)] [optional (number)]"
    await ctx.send(response)
@randomCiv.error
async def  clearError(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Return because we don't want to show an error for every command not found
    elif isinstance(error, commands.CommandOnCooldown):
        message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
    await ctx.send(message)



@bot.event
async def on_ready():
    # feedChannel = int(os.getenv('BOT_FEED_LOG'))
    # await bot.get_channel(feedChannel).send("HammerBot is online!")
    game = discord.Game("with Aoe2 data")
    await bot.change_presence(activity=game)

bot.run(TOKEN)
