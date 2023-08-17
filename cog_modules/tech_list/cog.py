import os

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

from techTreeInfo import *


class TechListCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="!units", aliases=["!unitlist", "!unit"], help="Returns an alphabetical list of unit names.")
    async def listUnits(self, ctx: commands.Context, arg1=None, arg2=None, arg3=None, arg4=None):
        if arg1 != None:
            if arg1.lower() == "a":
                embed = discord.Embed(title="'A' Units", description="Units that start with A.", color=0xD5D341)
                embed.add_field(name="Arambai", value="Unique Unit", inline=True)
                embed.add_field(name="Arbalester", value="Archer Unit", inline=True)
                embed.add_field(name="Archer", value="Archer Unit", inline=True)
            elif arg1.lower() == "b":
                embed = discord.Embed(title="'B' Units", description="Units that start with B.", color=0xD5D341)
                embed.add_field(name="Ballista Elephant", value="Unique Unit", inline=True)
                embed.add_field(name="Battering Ram", value="Siege Unit", inline=True)
                embed.add_field(name="Battle Elephant", value="Cavalry Unit", inline=True)
                embed.add_field(name="Berserk", value="Unique Unit", inline=True)
                embed.add_field(name="Bombard Cannon", value="Siege Unit", inline=True)
                embed.add_field(name="Boyar", value="Unique Unit", inline=True)
            elif arg1.lower() == "c":
                embed = discord.Embed(title="'C' Units", description="Units that start with C.", color=0xD5D341)
                embed.add_field(name="Camel Archer", value="Unique Unit", inline=True)
                embed.add_field(name="Camel Rider", value="Calvary Unit", inline=True)
                embed.add_field(name="Cannon Galleon", value="Warship Unit", inline=True)
                embed.add_field(name="Capped Ram", value="Siege Unit", inline=True)
                embed.add_field(name="Caravel", value="Warship Unit", inline=True)
                embed.add_field(name="Cataphract", value="Unique Unit", inline=True)
                embed.add_field(name="Cavalier", value="Cavalry Unit", inline=True)
                embed.add_field(name="Cavalry Archer", value="Cavalry Archer Unit", inline=True)
                embed.add_field(name="Champion", value="Infantry Unit", inline=True)
                embed.add_field(name="Chu Ko Nu", value="Unique Unit", inline=True)
                embed.add_field(name="Condottiero", value="Unique Unit", inline=True)
                embed.add_field(name="Conquistador", value="Unique Unit", inline=True)
                embed.add_field(name="Coustillier", value="Unique Unit", inline=True)
                embed.add_field(name="Crossbowman", value="Archer Unit", inline=True)
            elif arg1.lower() == "d":
                embed = discord.Embed(title="'D' Units", description="Units that start with D.", color=0xD5D341)
                embed.add_field(name="Demolition Raft", value="Warship Unit", inline=True)
                embed.add_field(name="Demolition Ship", value="Warship Unit", inline=True)
            elif arg1.lower() == "e":
                embed = discord.Embed(
                    title="'E' Units",
                    description="Units that start with E. See !units e2 and !units e3 for more.",
                    color=0xD5D341,
                )
                embed.add_field(name="Eagle Scout", value="Infantry Unit", inline=True)
                embed.add_field(name="Eagle Warrior", value="Infantry Unit", inline=True)
                embed.add_field(name="Elephant Archer", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Arambai", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Ballista Elephant", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Battle Elephant", value="Cavalry Unit", inline=True)
                embed.add_field(name="Elite Berserk", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Boyar", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Camel Archer", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Cannon Galleon", value="Warship Unit", inline=True)
                embed.add_field(name="Elite Caravel", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Cataphract", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Chu Ko Nu", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Conquistador", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Coustillier", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Eagle Warrior", value="Infantry Unit", inline=True)
                embed.add_field(name="Elite Elephant Archer", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Gbeto", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Genitour", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Genoese Crossbowman", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Huskarl", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Hussite Wagon", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Jaguar Warrior", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Janissary", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Kamayuk", value="Unique Unit", inline=True)
                # breaks here, need pagination
            elif arg1.lower() == "e2":
                embed = discord.Embed(
                    title="'E' Units",
                    description="Units that start with E. See !units e and !units e3 for more.",
                    color=0xD5D341,
                )
                embed.add_field(name="Elite Karambit Warrior", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Keshik", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Kipchak", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Konnik", value="Unique Unit", inline=True)
                # embed.add_field(name="Elite Konnik (Dismounted)", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Leitis", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Longboat", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Longbowman", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Magyar Huszar", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Mameluke", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Mangudai", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Obuch", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Organ Gun", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Plumed Archer", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Karambit Warrior", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Rattan Archer", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Samurai", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Serjeant", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Shotel Warrior", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Skirmisher", value="Archer Unit", inline=True)
                embed.add_field(name="Elite Steppe Lancer", value="Calvary Unit", inline=True)
                embed.add_field(name="Elite Tarkan", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Teutonic Knight", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Throwing Axeman", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Turtle Ship", value="Unique Unit", inline=True)
            elif arg1.lower() == "e3":
                embed = discord.Embed(
                    title="'E' Units",
                    description="Units that start with E. See !units e and !units e2 for more.",
                    color=0xD5D341,
                )
                embed.add_field(name="Elite War Elephant", value="Unique Unit", inline=True)
                embed.add_field(name="Elite War Wagon", value="Unique Unit", inline=True)
                embed.add_field(name="Elite Woad Raider", value="Unique Unit", inline=True)
            elif arg1.lower() == "f":
                embed = discord.Embed(title="'F' Units", description="Units that start with F.", color=0xD5D341)
                embed.add_field(name="Fast Fire Ship", value="Warship Unit", inline=True)
                embed.add_field(name="Fire Galley", value="Warship Unit", inline=True)
                embed.add_field(name="Fire Ship", value="Warship Unit", inline=True)
                embed.add_field(name="Fishing Ship", value="Economic Unit", inline=True)
                embed.add_field(name="Flaming Camel", value="Unique Unit", inline=True)
                embed.add_field(name="Flemish Militia", value="Unique Unit", inline=True)
            elif arg1.lower() == "g":
                embed = discord.Embed(title="'G' Units", description="Units that start with G.", color=0xD5D341)
                embed.add_field(name="Galleon", value="Warship Unit", inline=True)
                embed.add_field(name="Galley", value="Warship Unit", inline=True)
                embed.add_field(name="Gbeto", value="Unique Unit", inline=True)
                embed.add_field(name="Genitour", value="Unique Unit", inline=True)
                embed.add_field(name="Genoese Crossbowman", value="Unique Unit", inline=True)
            elif arg1.lower() == "h":
                embed = discord.Embed(title="'H' Units", description="Units that start with H.", color=0xD5D341)
                embed.add_field(name="Halberdier", value="Infantry Unit", inline=True)
                embed.add_field(name="Hand Cannoneer", value="Archer Unit", inline=True)
                embed.add_field(name="Heavy Camel Rider", value="Cavalry Unit", inline=True)
                embed.add_field(name="Heavy Calvary Archer", value="Cavalry Archer Unit", inline=True)
                embed.add_field(name="Heavy Demolition Ship", value="Warship Unit", inline=True)
                embed.add_field(name="Heavy Scorpion", value="Siege Unit", inline=True)
                embed.add_field(name="Houfnice", value="Unique Unit", inline=True)
                embed.add_field(name="Huskarl", value="Unique Unit", inline=True)
                embed.add_field(name="Hussar", value="Cavalry Unit", inline=True)
            elif arg1.lower() == "i":
                embed = discord.Embed(title="'I' Units", description="Units that start with I.", color=0xD5D341)
                embed.add_field(name="Imperial Camel Rider", value="Unique Unit", inline=True)
                embed.add_field(name="Imperial Skirmisher", value="Unique Unit", inline=True)
            elif arg1.lower() == "j":
                embed = discord.Embed(title="'J' Units", description="Units that start with J.", color=0xD5D341)
                embed.add_field(name="Jaguar Warrior", value="Unique Unit", inline=True)
                embed.add_field(name="Janissary", value="Unique Unit", inline=True)
            elif arg1.lower() == "k":
                embed = discord.Embed(title="'K' Units", description="Units that start with K.", color=0xD5D341)
                embed.add_field(name="Kamayuk", value="Unique Unit", inline=True)
                embed.add_field(name="Karambit Warrior", value="Unique Unit", inline=True)
                embed.add_field(name="Keshik", value="Unique Unit", inline=True)
                embed.add_field(name="Kipchak", value="Unique Unit", inline=True)
                embed.add_field(name="Knight", value="Cavalry Unit", inline=True)
                embed.add_field(name="Konnik", value="Unique Unit", inline=True)
                # embed.add_field(name="Konnik (Dismounted)", value="Unique Unit", inline=True)
            elif arg1.lower() == "l":
                embed = discord.Embed(title="'L' Units", description="Units that start with L.", color=0xD5D341)
                embed.add_field(name="Leitis", value="Unique Unit", inline=True)
                embed.add_field(name="Light Cavalry", value="Cavalry Unit", inline=True)
                embed.add_field(name="Long Swordsman", value="Infantry Unit", inline=True)
                embed.add_field(name="Longboat", value="Unique Unit", inline=True)
                embed.add_field(name="Longbowman", value="Unique Unit", inline=True)
            elif arg1.lower() == "m":
                embed = discord.Embed(title="'M' Units", description="Units that start with M.", color=0xD5D341)
                embed.add_field(name="Magyar Huszar", value="Unique Unit", inline=True)
                embed.add_field(name="Mameluke", value="Unique Unit", inline=True)
                embed.add_field(name="Man-at-Arms", value="Infantry Unit", inline=True)
                embed.add_field(name="Mangonel", value="Siege Unit", inline=True)
                embed.add_field(name="Mangudai", value="Unique Unit", inline=True)
                embed.add_field(name="Militia", value="Infantry Unit", inline=True)
                embed.add_field(name="Missionary", value="Unique Unit", inline=True)
                embed.add_field(name="Monk", value="Monk Unit", inline=True)
            elif arg1.lower() == "o":
                embed = discord.Embed(title="'O' Units", description="Units that start with O.", color=0xD5D341)
                embed.add_field(name="Obuch", value="Unique Unit", inline=True)
                embed.add_field(name="Onager", value="Siege Unit", inline=True)
                embed.add_field(name="Organ Gun", value="Unique Unit", inline=True)
            elif arg1.lower() == "p":
                embed = discord.Embed(title="'P' Units", description="Units that start with P.", color=0xD5D341)
                embed.add_field(name="Paladin", value="Cavalry Unit", inline=True)
                embed.add_field(name="Petard", value="Petard Unit", inline=True)
                embed.add_field(name="Pikeman", value="Infantry Unit", inline=True)
                embed.add_field(name="Plumed Archer", value="Unique Unit", inline=True)
            elif arg1.lower() == "r":
                embed = discord.Embed(title="'R' Units", description="Units that start with R.", color=0xD5D341)
                embed.add_field(name="Rattan Archer", value="Unique Unit", inline=True)
            elif arg1.lower() == "s":
                embed = discord.Embed(title="'S' Units", description="Units that start with S.", color=0xD5D341)
                embed.add_field(name="Samurai", value="Unique Unit", inline=True)
                embed.add_field(name="Scorpion", value="Siege Unit", inline=True)
                embed.add_field(name="Scout Cavalry", value="Cavalry Unit", inline=True)
                embed.add_field(name="Serjeant", value="Unique Unit", inline=True)
                embed.add_field(name="Shotel Warrior", value="Unique Unit", inline=True)
                embed.add_field(name="Siege Onager", value="Siege Unit", inline=True)
                embed.add_field(name="Siege Ram", value="Siege Unit", inline=True)
                embed.add_field(name="Siege Tower", value="Siege Unit", inline=True)
                embed.add_field(name="Skirmisher", value="Archer Unit", inline=True)
                embed.add_field(name="Slinger", value="Unique Unit", inline=True)
                embed.add_field(name="Spearman", value="Infantry Unit", inline=True)
                embed.add_field(name="Steppe Lancer", value="Cavalry Unit", inline=True)
            elif arg1.lower() == "t":
                embed = discord.Embed(title="'T' Units", description="Units that start with T.", color=0xD5D341)
                embed.add_field(name="Tarkan", value="Unique Unit", inline=True)
                embed.add_field(name="Teutonic Knight", value="Unique Unit", inline=True)
                embed.add_field(name="Throwing Axeman", value="Unique Unit", inline=True)
                embed.add_field(name="Trade Cart", value="Trade Unit", inline=True)
                embed.add_field(name="Trade Cog", value="Trade Unit", inline=True)
                embed.add_field(name="Transport Ship", value="Transport Unit", inline=True)
                embed.add_field(name="Trebuchet", value="Siege Unit", inline=True)
                embed.add_field(name="Turtle Ship", value="Unique Unit", inline=True)
                embed.add_field(name="Two-Handed Swordsman", value="Infantry Unit", inline=True)
            elif arg1.lower() == "v":
                embed = discord.Embed(title="'V' Units", description="Units that start with V.", color=0xD5D341)
                embed.add_field(name="Villager", value="Economic Unit", inline=True)
            elif arg1.lower() == "w":
                embed = discord.Embed(title="'W' Units", description="Units that start with W.", color=0xD5D341)
                embed.add_field(name="War Elephant", value="Unique Unit", inline=True)
                embed.add_field(name="War Galley", value="Warship Unit", inline=True)
                embed.add_field(name="War Wagon", value="Unique Unit", inline=True)
                embed.add_field(name="Winged Hussar", value="Unique Unit", inline=True)
                embed.add_field(name="Woad Raider", value="Unique Unit", inline=True)
            elif arg1.lower() == "x":
                embed = discord.Embed(title="'X' Units", description="Units that start with X.", color=0xD5D341)
                embed.add_field(name="Xolotl Warrior", value="Cavalry Unit", inline=True)
            else:
                if arg4 != None:
                    arg1 = arg1.lower() + " " + arg2.lower() + " " + arg3.lower() + " " + arg4.lower()
                elif arg3 != None:
                    arg1 = arg1.lower() + " " + arg2.lower() + " " + arg3.lower()
                elif arg2 != None:
                    arg1 = arg1.lower() + " " + arg2.lower()

                embed = discord.Embed(
                    title=f"'{arg1.upper()}' Units", description=f"Units that start with {arg1.upper()}.", color=0xD5D341
                )
                tempDict = {}
                for key in unitList:
                    if key.lower().startswith(arg1.lower()):
                        tempDict[key] = unitList[key]
                if len(tempDict) == 0:
                    embed = discord.Embed(
                        title=f"There are no '{arg1.upper()}' Units",
                        description=f"No units that start with {arg1.upper()}.",
                        color=0xD5D341,
                    )
                elif len(tempDict) > 25:
                    embed = discord.Embed(
                        title=f"There are too many '{arg1.upper()}' Units",
                        description=f"Please refine your search.",
                        color=0xD5D341,
                    )
                else:
                    for key in tempDict:
                        embed.add_field(name=f"{key}", value=f"{unitList[key][0]}", inline=True)
        else:
            embed = discord.Embed(title="Unit Dictionary", description="Search for unit names alphabetically.", color=0xD5D341)
            embed.add_field(name="Search for a Unit with !unit <letter>", value="Example usage: !unit a", inline=True)

        await ctx.send(embed=embed)

    @commands.command(name="!techs", aliases=["!techlist", "!tech"], help="Returns an alphabetical list of tech names.")
    async def listTechs(self, ctx: commands.Context, arg1=None, arg2=None, arg3=None, arg4=None):
        if arg1 != None:
            if arg4 != None:
                arg1 = arg1.lower() + " " + arg2.lower() + " " + arg3.lower() + " " + arg4.lower()
            elif arg3 != None:
                arg1 = arg1.lower() + " " + arg2.lower() + " " + arg3.lower()
            elif arg2 != None:
                arg1 = arg1.lower() + " " + arg2.lower()

            embed = discord.Embed(
                title=f"'{arg1.upper()}' Techs",
                description=f"Researchable techs that start with {arg1.upper()}.",
                color=0xD5D341,
            )
            tempDict = {}
            for key in techList:
                if key.lower().startswith(arg1.lower()):
                    tempDict[key] = techList[key]
            if len(tempDict) == 0:
                embed = discord.Embed(
                    title=f"There are no '{arg1.upper()}' Techs",
                    description=f"No researchable techs that start with {arg1.upper()}.",
                    color=0xD5D341,
                )
            elif len(tempDict) > 25:
                embed = discord.Embed(
                    title=f"There are too many '{arg1.upper()}' Techs",
                    description=f"Please refine your search.",
                    color=0xD5D341,
                )
            else:
                for key in tempDict:
                    embed.add_field(name=f"{key}", value=f"{techList[key][0]}", inline=True)
        else:
            embed = discord.Embed(
                title="Tech Dictionary", description="Search for researchable technology names alphabetically.", color=0xD5D341
            )
            embed.add_field(name="Search for a Tech with !techs <letter>", value="Example usage: !techs a", inline=True)

        await ctx.send(embed=embed)

    @commands.command(
        name="!buildings",
        aliases=["!buildinglist", "!build", "!building"],
        help="Returns an alphabetical list of building names.",
    )
    async def listBuildings(self, ctx: commands.Context, arg1=None, arg2=None, arg3=None, arg4=None):
        if arg1 != None:
            if arg4 != None:
                arg1 = arg1.lower() + " " + arg2.lower() + " " + arg3.lower() + " " + arg4.lower()
            elif arg3 != None:
                arg1 = arg1.lower() + " " + arg2.lower() + " " + arg3.lower()
            elif arg2 != None:
                arg1 = arg1.lower() + " " + arg2.lower()

            embed = discord.Embed(
                title=f"'{arg1.upper()}' Buildings",
                description=f"Buildings that start with {arg1.upper()}.",
                color=0xD5D341,
            )
            tempDict = {}
            for key in buildingList:
                if key.lower().startswith(arg1.lower()):
                    tempDict[key] = buildingList[key]
            if len(tempDict) == 0:
                embed = discord.Embed(
                    title=f"There are no '{arg1.upper()}' Buildings",
                    description=f"No buildings that start with {arg1.upper()}.",
                    color=0xD5D341,
                )
            elif len(tempDict) > 25:
                embed = discord.Embed(
                    title=f"There are too many '{arg1.upper()}' Buildings",
                    description=f"Please refine your search.",
                    color=0xD5D341,
                )
            else:
                for key in tempDict:
                    embed.add_field(name=f"{key}", value=f"{buildingList[key][0]}", inline=True)
        else:
            embed = discord.Embed(
                title="Building Dictionary", description="Search for building names alphabetically.", color=0xD5D341
            )
            embed.add_field(
                name="Search for a Building with !buildings <letter>", value="Example usage: !buildings a", inline=True
            )

        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(TechListCommand(bot))
