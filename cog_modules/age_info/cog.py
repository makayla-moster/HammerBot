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

@tasks.loop(seconds=90)
async def get_1v1_player_json():
    """
    Helper function for pulling the top 10,000 AoE2 players' info.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get('https://aoe2.net/api/leaderboard?game=aoe2de&leaderboard_id=3&start=1&count=10000') as r:
            r = await r.json(content_type=None)
            await sesson.close()
            return r

class AgeCommands(commands.Cog):
    """Commands for age of empires calls by players."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # @commands.command(name='!rank', help='Returns player 1v1 ranking')
    # async def rank1v1(self, ctx: commands.Context, arg1=None):
    #     """
    #     Command: !rank [player name (optional)]
    #     Returns: 1v1 rank of player
    #     """
    #
    #     response = await get_1v1_player_json()
    #
    #     # rankings_1v1 = response['leaderboard']
    #     #
    #     # if arg1 == None:
    #     #     print(rankings_1v1['name'])
    #
    #     await ctx.send("Finished")


    @commands.command(name='!civ', help='Returns AoE2 civ tech tree information.')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def civInfo(self, ctx: commands.Context, arg):
        """
        Command: !civ [civname]
        Returns: The aoe2 tech tree link for that civ.
        """

        if arg.lower() in age_civs:
            response = "https://aoe2techtree.net/#" + str(arg.lower())
            await ctx.send(response)
        else:
            message = discord.Embed(title='Invalid Input', description="There was a problem with your input. Please check your input and try again.", color = discord.Color.red())
            await ctx.send(embed=message)


    @commands.command(name='!teamciv', help="Returns a team of civs.")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def teamRandomCiv(self, ctx: commands.Context, arg1=None):
        """
        Command: !teamciv
        Returns: !teamciv                       Returns 2 balanced civs
                 !teamciv [(optional) number]   Returns [number] balanced civs for a team.
        """

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

        if arg1.isnumeric() == True:
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

            if (user_arg == None) or user_arg == 2:
                response = f"{random_civ_position(0, 1, 5, 2)[0]}, {random_civ_position(1, 1, 5, 2)[0]}"
            elif user_arg == 3:
                response = f"Flanks: {', '.join(random_civ_position(0, 2, 5, 2))}\nPocket: {random_civ_position(1, 1, 5, 2)[0]}"
            else:
                response = f"Flanks: {', '.join(random_civ_position(0, 2, 5, 2))}\nPockets: {', '.join(random_civ_position(1, 2, 5, 2))}"
            await ctx.send(response)
        else:
            message = discord.Embed(title='Invalid Input', description="There was a problem with your input. Please check your input and try again.", color = discord.Color.red())
            await ctx.send(embed=message)



    @commands.command(name='!randomciv', help='Returns a random AoE2 civ.')
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def randomCiv(self, ctx: commands.Context, arg1=None, arg2=None):
        """
        Command: !randomciv [optional (number)]
        Returns: !randomciv                     returns one random civ out of the 39
                 !randomciv [number]            returns [number] of civs
                 If command caller is Luke, will only return Incas unless overridden with !randomciv [r].
        """
        error = False
        reponse = ''
        # age_civs = ['Britons', 'Byzantines', 'Celts', 'Chinese', 'Franks', 'Goths', 'Japanese', 'Mongols', 'Persians', 'Saracens', 'Teutons', 'Turks', 'Vikings', 'Aztecs', 'Huns', 'Koreans', 'Mayans', 'Spanish', 'Incas', 'Indians', 'Italians', 'Magyars', 'Slavs', 'Berbers', 'Ethiopians', 'Malians', 'Portuguese', 'Burmese', 'Khmer', 'Malay', 'Vietnamese', 'Bulgarians', 'Cumans', 'Lithuanians', 'Tatars', 'Burgundians', 'Sicilians', 'Bohemians', 'Poles']
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
                            response = random.choice(age_civs).title()
                        else:
                            response += "\n" + random.choice(age_civs).title()
            elif arg2 != None and arg2.isnumeric():
                for i in range(int(arg2)):
                    if i == 0:
                        response = "Incas"
                    else:
                        response += "\n" + "Incas"
            else:
                response = "Incas"
        elif (arg1 == None):
            response = random.choice(age_civs).title()
        elif arg1 == 'Lucas' or arg1 == "Luke" or arg1 == "divas" or arg1 == "Divas":
            response = "Incas"
        elif arg1.isnumeric():
            for i in range(int(arg1)):
                if i == 0:
                    response = random.choice(age_civs).title()
                else:
                    response += "\n" + random.choice(age_civs).title()
        else:
            error = True
            message = discord.Embed(title='Invalid Input', description="There was a problem with your input. Please check your input and try again.", color = discord.Color.red())

        if error == True:
            await ctx.send(embed=message)
        else:
            await ctx.send(response)


    @commands.command(name='!whichciv', help = 'Returns which civ has the stated technology(ies).')
    async def civTech(self, ctx: commands.Context, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
        """
        Command: !whichciv [technology1 (+technology)] [(optional)technology2] [(optional)technology3] [(optional)technology4] [(optional)technology5]
        Returns: A list of civs that have that technology.
                 !whichciv [tech1+tech2]            returns all civs that have those techs (allows to search for multiple techs)
                 !whichciv [tech1]                  returns all civs that have that tech
                 !whichciv [techpart1] [techpart2]  returns all civs with that tech (accounts for spaces in tech name)
        """
        error = False
        if arg5 is not None:
            arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title() + " " + arg4.title() + " " + arg5.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = discord.Embed(title='Invalid Input', description="There was a problem with your input. Please check your input and try again.", color = discord.Color.red())

        elif arg4 is not None:
            arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title() + " " + arg4.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = discord.Embed(title='Invalid Input', description="There was a problem with your input. Please check your input and try again.", color = discord.Color.red())

        elif arg3 is not None:
            arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = discord.Embed(title='Invalid Input', description="There was a problem with your input. Please check your input and try again.", color = discord.Color.red())

        elif arg2 is not None:
            arg1 = arg1.title() + " " + arg2.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = discord.Embed(title='Invalid Input', description="There was a problem with your input. Please check your input and try again.", color = discord.Color.red())

        elif '+' in arg1:
            arg1 = arg1.split("+")
            try:
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
            except:
                error = True
                message = discord.Embed(title='Invalid Input', description="There was a problem with your input. Please check your input and try again.", color = discord.Color.red())
        else:
            try:
                response = techTreeDict[arg1.title()]
            except:
                error = True
                message = discord.Embed(title='Invalid Input', description="There was a problem with your input. Please check your input and try again.", color = discord.Color.red())

        if error == True:
            await ctx.send(embed=message)
        else:
            response.sort()
            await ctx.send(", ".join(response))

    @commands.command(name='!does', help='Returns if a civ(s) has a technology.')
    async def techTree(self, ctx: commands.Context, arg1, arg2, arg3=None, arg4=None, arg5=None):
        """
        Command: !does [civName] [techName]
        Returns: !does [civ] [tech]                     returns whether the civ has the tech
                 !does [civ1+civ2] [tech]               returns whether the civs have the tech
                 !does [civ] [techpart1] [techpart2]    returns whether the civ has the tech
        """
        error = False
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
        elif '+' in arg1:
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
                error = True
                message = discord.Embed(title='Invalid Input', description="There was a problem with your input. Please check your input and try again.", color = discord.Color.red())
        else:
            error = True
            message = discord.Embed(title='Invalid Input', description="There was a problem with your input. Please check your input and try again.", color = discord.Color.red())

        if error == True:
            await ctx.send(embed=message)
        else:
            await ctx.send(response)

    @commands.command(name='!match', help="Returns BSHammer's current match information")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def match(self, ctx: commands.Context, arg1=None):
        """
        Command: !match
        Returns: Both teams, each player has a color, civ, and ELOs, also returns map, game type, and server.
        """
        if arg1 == None:
            resp = await get_json_info()
            lastmatch = resp['last_match']
            players = []
            team1 = []
            team2 = []
            hammerTeam1 = False
            hammerTeam2 = False
            team1players = ''
            team2players = ''
            response = None
            server = lastmatch['server']

            players = await getPlayerIDs(resp)

            for player in players:
                await player.info()
                if player.team == 1:
                    team1.append(player)
                elif player.team == 2:
                    team2.append(player)

            count = len(players)
            i = 0
            if (player.game == "1v1 Empire Wars") or (player.game == "Team Empire Wars"):
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
        else:
            response = discord.Embed(title="Invalid Input", description="There was a problem with your input. Please check your input and try again.", color = discord.Color.red())
            await ctx.send(embed=response)
get_json_info.start()
def setup(bot: commands.Bot):
    bot.add_cog(AgeCommands(bot))
