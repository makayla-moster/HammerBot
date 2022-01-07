# bot.py
import os
import discord
import random
from dotenv import load_dotenv
import logging
from age_player import *
import csv
import requests
import sys
import aiohttp
import asyncio
from discord.ext import tasks, commands
from techTreeInfo import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
LUKE = os.getenv('LUKE_ID')

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


@bot.command(name='!randomciv', help='Returns a random AoE2 civ.')
@commands.cooldown(1, 10, commands.BucketType.user)
async def randomCiv(ctx, arg1=None, arg2=None, arg3=None):
    reponse = ''
    age_civs = ['Britons', 'Byzantines', 'Celts', 'Chinese', 'Franks', 'Goths', 'Japanese', 'Mongols', 'Persians', 'Saracens', 'Teutons', 'Turks', 'Vikings', 'Aztecs', 'Huns', 'Koreans', 'Mayans', 'Spanish', 'Incas', 'Indians', 'Italians', 'Magyars', 'Slavs', 'Berbers', 'Ethiopians', 'Malians', 'Portuguese', 'Burmese', 'Khmer', 'Malay', 'Vietnamese', 'Bulgarians', 'Cumans', 'Lithuanians', 'Tatars', 'Burgundians', 'Sicilians', 'Bohemians', 'Poles']
    pocket_civs = []
    flank_civs =[]
    username = ctx.message.author.id
    if str(username) == str(LUKE):
        if arg1 != None and arg1.isnumeric():
            for i in range(int(arg1)):
                if i == 0:
                    response = "Incas"
                else:
                    response += "\n" + "Incas"
        elif arg1 != None and arg1 == "r":
            if arg2 == None:
                response = random.choice(age_civs)
            elif arg2.isnumeric():
                for i in range(int(arg2)):
                    if i == 0:
                        response = random.choice(age_civs)
                    else:
                        response += "\n" + random.choice(age_civs)
            elif (arg2.lower() == 'flank'):
                if arg3 != None:
                    if arg3.isnumeric():
                        for i in range(int(arg3)):
                            if i == 0:
                                response = random.choice(age_civs)
                            else:
                                response += "\n" + random.choice(age_civs)
                    else:
                        response = "Not in correct format. !randomciv [optional (flank/pocket/number)] [optional (number)]"
                else:
                    response = random.choice(age_civs)
            elif (arg2.lower() == 'pocket'):
                if arg3 != None:
                    if arg3.isnumeric():
                        for i in range(int(arg3)):
                            if i == 0:
                                response = random.choice(age_civs)
                            else:
                                response += "\n" + random.choice(age_civs)
                    else:
                        response = "Not in correct format. !randomciv [optional (flank/pocket/number)] [optional (number)]"
                else:
                    response = random.choice(age_civs)
        elif arg2 != None and arg2.isnumeric():
            for i in range(int(arg2)):
                if i == 0:
                    response = "Incas"
                else:
                    response += "\n" + "Incas"
        else:
            response = "Incas"
    elif (arg1 == None) and (arg2 == None):
        response = random.choice(age_civs)
    elif arg1 == 'Lucas' or arg1 == "Luke" or arg1 == "divas" or arg1 == "Divas":
        response = "Incas"
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

@bot.command(name='!whichciv', help = 'Returns which civ has the stated technology(ies).')
async def civTech(ctx, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
    
    if arg5 is not None:
        arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title() + " " + arg4.title() + " " + arg5.title()
        response = techTreeDict[arg1]
    elif arg4 is not None:
        arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title() + " " + arg4.title()
        response = techTreeDict[arg1]
    elif arg3 is not None:
        arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title()
        response = techTreeDict[arg1]
    elif arg2 is not None:
        arg1 = arg1.title() + " " + arg2.title()
        response = techTreeDict[arg1]
    elif '+' in arg1:
        arg1 = arg1.split("+")
        # print(arg1)
        for i in range(len(arg1)-1):
            tech = arg1[int(i)]
            tech2 = arg1[int(i+1)]
            if i == 0:
                list1 = techTreeDict[tech.title()]
                list2 = techTreeDict[tech2.title()]
            else:
                list1 = list3
                list2 = techTreeDict[tech2.title()]
            list3 = set(list1).intersection(list2)
        response = list3
    else:
        response = techTreeDict[arg1.title()]

    await ctx.send(", ".join(response))



@bot.command(name='!does', help='Returns if a civ(s) has a technology.')
async def techTree(ctx, arg1, arg2, arg3=None, arg4=None, arg5=None):


    if arg1.lower() in age_civs:
        if arg5 is not None:
            arg2 = arg2.title() + " " + arg3.title() + " " + arg4.title() + " " + arg5.title()
        elif arg4 is not None:
            arg2 = arg2.title() + " " + arg3.title() + " " + arg4.title()
        elif arg3 is not None:
            arg2 = arg2.title() + " " + arg3.title()

        bool = arg1.title() in techTreeDict[arg2.title()]

        if bool:
            response = arg1.title() + " have " + arg2.title()
        elif not bool:
            response = arg1.title() + " do not have " + arg2.title()
        else:
            response = f"Error!"
    else:
        arg1 = arg1.split("+")

        if arg5 is not None:
            arg2 = arg2.title() + " " + arg3.title() + " " + arg4.title() + " " + arg5.title()
        elif arg4 is not None:
            arg2 = arg2.title() + " " + arg3.title() + " " + arg4.title()
        elif arg3 is not None:
            arg2 = arg2.title() + " " + arg3.title()


        if len(arg1) > 0:
            for i in range(len(arg1)):
                if arg1[i].lower() in age_civs:
                    bool = arg1[i].title() in techTreeDict[arg2.title()]
                    if bool:
                        if i == 0:
                            response = arg1[i].title() + " have " + arg2.title()
                        else:
                            response += "\n" + arg1[i].title() + " have " + arg2.title()
                    elif not bool:
                        if i == 0:
                            response = arg1[0].title() + " do not have " + arg2.title()
                        else:
                            response += "\n" + arg1[i].title() + " do not have " + arg2.title()
                    else:
                        response = f"Error!"
        else:
            response = f"Please ensure the civ name is spelled correctly with capitalization."
    await ctx.send(response)
@techTree.error
async def  clearError(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # Return because we don't want to show an error for every command not found
    elif isinstance(error, commands.CommandOnCooldown):
        message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
    await ctx.send(message)


@bot.command(name='!help', help='Returns commands, their syntax, and uses.')
@commands.cooldown(1, 10, commands.BucketType.user)
async def helpUser(ctx):
    embed=discord.Embed(title="Commands", description="Command Help", color=0xd5d341)
    embed.add_field(name="13", value="[`13`], Returns AoE2 taunt #13.", inline=True)
    embed.add_field(name="14", value="[`14`], Returns AoE2 taunt #14", inline=True)
    embed.add_field(name="30", value="[`30`], Returns AoE2 taunt #30.", inline=True)
    embed.add_field(name="age?", value="[`age?`], Returns 'Well, duh.'", inline=True)
    embed.add_field(name="!randomciv", value="[`!randomciv flank/pocket/number number`], Returns random Aoe2 civ(s).", inline=True)
    embed.add_field(name="!civ", value="[`!civ civName`], Returns AoE2 civ tech tree information.", inline=True)
    embed.add_field(name="!does", value="[`!does civName(+civNames) upgradeName`], Returns information about if a civ(s) has a technology.", inline=True)
    embed.add_field(name="!match", value="[`!match`], Returns information about BSHammer's current game.", inline=True)
    await ctx.send(embed=embed)


@bot.command(name='!is', help='Redirects to !does.')
@commands.cooldown(1, 10, commands.BucketType.user)
async def techTreeRedirect(ctx):
    response = "Please use !does instead."
    await ctx.send(response)

@tasks.loop(seconds=75)
async def get_json_info():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://aoe2.net/api/player/lastmatch?game=aoe2de&profile_id=313591') as r:
            r = await r.json(content_type=None)
            await session.close()
            return r

@bot.command(name='!match', help="Returns BSHammer's current match information")
@commands.cooldown(1, 10, commands.BucketType.user)
async def match(ctx):
    resp = await get_json_info()
    lastmatch = resp['last_match']
    playerName = resp['name']
    players = []
    team1 = []
    team2 = []
    hammerTeam1 = False
    hammerTeam2 = False
    team1players = ''
    team2players = ''
    response = None
    server = lastmatch['server']
    map = lastmatch['map_type']
    # print(players)

    players = getPlayerIDs(resp)
    for player in players:
        player.info()
        if player.team == 1:
            team1.append(player)
        elif player.team == 2:
            team2.append(player)
        if (player.name == playerName) and player.team == 1:
            hammerTeam1 = True
        elif (player.name == playerName) and player.team == 2:
            hammerTeam2 = True
    count = len(players)
    i = 0
    if (player.game == "1v1 Empire Wars") or (player.game == "Team Empire Wars"):
        if hammerTeam1 == True:
            for i in range(count // 2):
                player1 = team1[i]
                if i == 0:
                    team1players = f"{player1.color} {player1.name} [{player1.country} {player1.ew_tg_rating} {player1.ew_rating}] as {player1.civ} "
                else:
                    team1players += f"{player1.color} {player1.name} [{player1.country} {player1.ew_tg_rating} {player1.ew_rating}] as {player1.civ} "
                player2 = team2[i]
                if i == 0:
                    team2players = f"{player2.color} {player2.name} [{player2.country} {player2.ew_tg_rating} {player2.ew_rating}] as {player2.civ} "
                else:
                    team2players += f"{player2.color} {player2.name} [{player2.country} {player2.ew_tg_rating} {player2.ew_rating}] as {player2.civ} "
            response = f"{team1players}-- VS -- {team2players}playing {player1.game} on {player1.map}\nServer: {server}"
        elif hammerTeam2 == True:
            for i in range(count // 2):
                player1 = team2[i]
                if i == 0:
                    team1players = f"{player1.color} {player1.name} [{player1.country} {player1.ew_tg_rating} {player1.ew_rating}] as {player1.civ} "
                else:
                    team1players += f"{player1.color} {player1.name} [{player1.country} {player1.ew_tg_rating} {player1.ew_rating}] as {player1.civ} "
                player2 = team1[i]
                if i == 0:
                    team2players = f"{player2.color} {player2.name} [{player2.country} {player2.ew_tg_rating} {player2.ew_rating}] as {player2.civ} "
                else:
                    team2players += f"{player2.color} {player2.name} [{player2.country} {player2.ew_tg_rating} {player2.ew_rating}] as {player2.civ} "
            response = f"{team1players}-- VS -- {team2players}playing {player1.game} on {player1.map}\nServer: {server}"
        else:
            for i in range(count // 2):
                player1 = team1[i]
                if i == 0:
                    team1players = f"{player1.color} {player1.name} [{player1.country} {player1.ew_tg_rating} {player1.ew_rating}] as {player1.civ} "
                else:
                    team1players += f"{player1.color} {player1.name} [{player1.country} {player1.ew_tg_rating} {player1.ew_rating}] as {player1.civ} "
                player2 = team2[i]
                if i == 0:
                    team2players = f"{player2.color} {player2.name} [{player2.country} {player2.ew_tg_rating} {player2.ew_rating}] as {player2.civ} "
                else:
                    team2players += f"{player2.color} {player2.name} [{player2.country} {player2.ew_tg_rating} {player2.ew_rating}] as {player2.civ} "
            response = f"{team1players}-- VS -- {team2players}playing {player1.game} on {player1.map}\nServer: {server}"
    else:
                if hammerTeam1 == True:
                    for i in range(count // 2):
                        player1 = team1[i]
                        if i == 0:
                            team1players = f"{player1.color} {player1.name} [{player1.country} {player1.tg_rating} {player1.rating}] as {player1.civ} "
                        else:
                            team1players += f"{player1.color} {player1.name} [{player1.country} {player1.tg_rating} {player1.rating}] as {player1.civ} "
                        player2 = team2[i]
                        if i == 0:
                            team2players = f"{player2.color} {player2.name} [{player2.country} {player2.tg_rating} {player2.rating}] as {player2.civ} "
                        else:
                            team2players += f"{player2.color} {player2.name} [{player2.country} {player2.tg_rating} {player2.rating}] as {player2.civ} "
                    response = f"{team1players}-- VS -- {team2players}playing {player1.game} on {player1.map}\nServer: {server}"
                elif hammerTeam2 == True:
                    for i in range(count // 2):
                        player1 = team2[i]
                        if i == 0:
                            team1players = f"{player1.color} {player1.name} [{player1.country} {player1.tg_rating} {player1.rating}] as {player1.civ} "
                        else:
                            team1players += f"{player1.color} {player1.name} [{player1.country} {player1.tg_rating} {player1.rating}] as {player1.civ} "
                        player2 = team1[i]
                        if i == 0:
                            team2players = f"{player2.color} {player2.name} [{player2.country} {player2.tg_rating} {player2.rating}] as {player2.civ} "
                        else:
                            team2players += f"{player2.color} {player2.name} [{player2.country} {player2.tg_rating} {player2.rating}] as {player2.civ} "
                    response = f"{team1players}-- VS -- {team2players}playing {player1.game} on {player1.map}\nServer: {server}"
                else:
                    for i in range(count // 2):
                        player1 = team1[i]
                        if i == 0:
                            team1players = f"{player1.color} {player1.name} [{player1.country} {player1.tg_rating} {player1.rating}] as {player1.civ} "
                        else:
                            team1players += f"{player1.color} {player1.name} [{player1.country} {player1.tg_rating} {player1.rating}] as {player1.civ} "
                        player2 = team2[i]
                        if i == 0:
                            team2players = f"{player2.color} {player2.name} [{player2.country} {player2.tg_rating} {player2.rating}] as {player2.civ} "
                        else:
                            team2players += f"{player2.color} {player2.name} [{player2.country} {player2.tg_rating} {player2.rating}] as {player2.civ} "
                    response = f"{team1players}-- VS -- {team2players}playing {player1.game} on {player1.map}\nServer: {server}"
    await ctx.send(response)


@bot.event
async def on_ready():
    # feedChannel = int(os.getenv('BOT_FEED_LOG'))
    # await bot.get_channel(feedChannel).send("HammerBot is online!")
    game = discord.Game("with AoE2 data")
    await bot.change_presence(activity=game)

get_json_info.start()
bot.run(TOKEN)
