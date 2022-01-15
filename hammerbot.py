# bot.py
import os, discord, random, logging
import csv, sys, aiohttp, asyncio
from dotenv import load_dotenv
from age_player import *
from discord.ext import tasks, commands
from techTreeInfo import *
import numpy as np

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

for folder in os.listdir("cog_modules"):
    if os.path.exists(os.path.join("cog_modules", folder, "cog.py")):
        bot.load_extension(f"cog_modules.{folder}.cog")

@bot.command(name='!civ', help='Returns AoE2 civ tech tree information.')
@commands.cooldown(1, 10, commands.BucketType.user)
async def civInfo(ctx, arg):
    """
    Command: !civ [civname]
    Returns: The aoe2 tech tree link for that civ.
    """
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

@bot.command(name='!teamciv', help="Returns a team of civs.")
@commands.cooldown(1, 10, commands.BucketType.user)
async def teamRandomCiv(ctx, arg1=None):
    """
    Command: !teamciv
    Returns: !teamciv                       Returns 2 balanced civs
             !teamciv [(optional) number]   Returns [number] balanced civs for a team.
    """
    if arg1 != None:
        user_arg = int(arg1)
    else:
        user_arg = 2
    flanksum = 0
    pocketsum = 0
    for item in civ_score_dict:
        flanksum += civ_score_dict[item][0]
        pocketsum += civ_score_dict[item][1]
    flankavg = flanksum/39
    pocketavg = pocketsum/39


    def random_civ_position(position, amount, uniform_size, b1):
        # position: flank = 0, pocket = 1
        b0_values = [flankavg, pocketavg]
        result = []
        for i in range(amount):
            random_civs = []
            for i in range(uniform_size):
                random_civs.append(age_civs[random.randint(0, 38)].title())

            total_score = 0
            for item in random_civs:
                total_score += civ_score_dict[item][position]

            weights = []
            b0 = (-b0_values[position]+0)*b1

            for item in random_civs:
                p = 1/ (1 + np.exp( -(b0 + b1*civ_score_dict[item][position]) ))
                weights.append(p)
            result.append(random.choices(random_civs, weights, k = 1)[0])

        return result

    if (user_arg == None) or user_arg == 2:
        response = f"{random_civ_position(0, 1, 5, 2)[0]}, {random_civ_position(1, 1, 5, 2)[0]}"
    elif user_arg == 3:
        response = f"Flanks: {', '.join(random_civ_position(0, 2, 5, 2))}\nPocket: {random_civ_position(1, 1, 5, 2)[0]}"
    else:
        response = f"Flanks: {', '.join(random_civ_position(0, 2, 5, 2))}\nPockets: {', '.join(random_civ_position(1, 2, 5, 2))}"

    await ctx.send(response)

@bot.command(name='!randomciv', help='Returns a random AoE2 civ.')
@commands.cooldown(1, 10, commands.BucketType.user)
async def randomCiv(ctx, arg1=None, arg2=None):
    """
    Command: !randomciv [optional (number)]
    Returns: !randomciv                     returns one random civ out of the 39
             !randomciv [number]            returns [number] of civs
             If command caller is Luke, will only return Incas unless overridden with !randomciv [r].
    """
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
        elif arg2 != None and arg2.isnumeric():
            for i in range(int(arg2)):
                if i == 0:
                    response = "Incas"
                else:
                    response += "\n" + "Incas"
        else:
            response = "Incas"
    elif (arg1 == None):
        response = random.choice(age_civs)
    elif arg1 == 'Lucas' or arg1 == "Luke" or arg1 == "divas" or arg1 == "Divas":
        response = "Incas"
    elif arg1.isnumeric():
        for i in range(int(arg1)):
            if i == 0:
                response = random.choice(age_civs)
            else:
                response += "\n" + random.choice(age_civs)
    else:
        response = "Not in correct format. !randomciv [(optional) number]"
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
    """
    Command: !whichciv [technology1 (+technology)] [(optional)technology2] [(optional)technology3] [(optional)technology4] [(optional)technology5]
    Returns: A list of civs that have that technology.
             !whichciv [tech1+tech2]            returns all civs that have those techs (allows to search for multiple techs)
             !whichciv [tech1]                  returns all civs that have that tech
             !whichciv [techpart1] [techpart2]  returns all civs with that tech (accounts for spaces in tech name)
    """

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

# @bot.command(name='!contributors', help = 'Returns a list of HammerBot contributors.')
# async def contribute(ctx):
#     """
#     Command: !contributors
#     Returns: An embed of the list of contributors to HammerBot.
#     """
#     embed=discord.Embed(title="HammerBot Contributors", description="List of HammerBot Contributors", color=0xd5d341)
#     embed.add_field(name="BSHammer", value="\u200b", inline=True)
#     embed.add_field(name="quela", value="\u200b", inline=True)
#     embed.add_field(name="harristotle", value="\u200b", inline=True)
#     embed.add_field(name="Rangebro", value="\u200b", inline=True)
#     await ctx.send(embed=embed)

@bot.command(name='!does', help='Returns if a civ(s) has a technology.')
async def techTree(ctx, arg1, arg2, arg3=None, arg4=None, arg5=None):
    """
    Command: !does [civName] [techName]
    Returns: !does [civ] [tech]                     returns whether the civ has the tech
             !does [civ1+civ2] [tech]               returns whether the civs have the tech
             !does [civ] [techpart1] [techpart2]    returns whether the civ has the tech
    """

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





# @bot.command(name='!is', help='Redirects to !does.')
# @commands.cooldown(1, 10, commands.BucketType.user)
# async def techTreeRedirect(ctx):
#     """
#     Command: !is
#     Returns: Redirects user to the !does command due to renaming.
#     """
#     response = "Please use !does instead."
#     await ctx.send(response)

@tasks.loop(seconds=75)
async def get_json_info():
    """
    Helper function for pulling the last AoE2 match played by BSHammer. Is looped every 75 seconds to have up-to-date json info.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get('https://aoe2.net/api/player/lastmatch?game=aoe2de&profile_id=313591') as r:
            r = await r.json(content_type=None)
            await session.close()
            return r

@bot.command(name='!match', help="Returns BSHammer's current match information")
@commands.cooldown(1, 10, commands.BucketType.user)
async def match(ctx):
    """
    Command: !match
    Returns: Both teams, each player has a color, civ, and ELOs, also returns map, game type, and server.
    """
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
