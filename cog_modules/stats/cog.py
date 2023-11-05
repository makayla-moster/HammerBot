import json
import os

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from fuzzywuzzy import fuzz

from full_tech_tree_processing import *
from techtree_descriptions import *

# Dictionary of all techs, units, and buildings
# as the keys with values equal to the civs
# that get the key.
from techTreeInfo import *

# Load the descriptions_cleaned.json file as descriptions
with open("descriptions_cleaned.json") as fp:
    descriptions = json.load(fp)

# <<<<<<< Updated upstream
# =======
# Load the unique_techs.json file as unique_techs
with open("unique_techs.json") as fp:
    unique_techs = json.load(fp)
# >>>>>>> Stashed changes


class StatCommands(commands.Cog):
    """Commands for stat commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="!stats", aliases=["!stat"])
    # @commands.cooldown(1, 10, commands.BucketType.user)
    async def statInfo(self, ctx: commands.Context, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
        """
        Command: !stat
        Returns: Redirects user to the !does command due to renaming.
        """

        input = [arg1, arg2, arg3, arg4, arg5]
        input = [x.title() for x in input if x is not None]
        input = " ".join(input)

        if input not in techTreeDict:
            # This is when we do fuzzy suggestion and stop.
            fuzzy_search_scores = {}
            for item in techTreeDict:
                fuzzy_search_scores[item] = fuzz.ratio(input, item)
            top3 = sorted(fuzzy_search_scores, key=fuzzy_search_scores.get, reverse=True)[:3]
            error = f"There was an error with your input. Did you mean {top3[0]}, {top3[1]}, or {top3[2]}?"
            embed = discord.Embed(
                title="Invalid Input",
                description=error,
                color=discord.Color.red(),
            )
            await ctx.send(embed=embed)
        else:
            if input in localised_tech_name_lookup:
                unitBuildNum = localised_tech_name_lookup[input]
                entity = "techs"
                entityDirectory = "Techs"
            if input in localised_unit_building_name_lookup:
                unitBuildNum = localised_unit_building_name_lookup[input]
                if unitBuildNum in techtree["data"]["units"]:
                    entity = "units"
                    entityDirectory = "Units"
                if unitBuildNum in techtree["data"]["buildings"]:
                    entity = "buildings"
                    entityDirectory = "Buildings"

            cost = get_cost(input, entity)
            costString = ""
            if "Food" in cost:
                costString += f"{cost['Food']} <:food:978788983377121311> "
            if "Wood" in cost:
                costString += f"{cost['Wood']} <:woodAge:978788983435853834> "
            if "Gold" in cost:
                costString += f"{cost['Gold']} <:gold:978788983364546581> "
            if "Stone" in cost:
                costString += f"{cost['Stone']} <:stone:978788984547315792>: "
            if costString != "":
                costString2 = costString
            else:
                costString2 = "No resources needed."

            if entity != "techs" and input[-1] != "s":
                embed = discord.Embed(title=f"{input} Stats", description=f"Information about {input}s.", color=0xD5D341)
            else:
                embed = discord.Embed(title=f"{input} Stats", description=f"Information about {input}.", color=0xD5D341)

            # Check to see if entity is a Castle Age Unique Tech
            if input in unique_techs["castle_age_unique_techs"]:
                embed.set_thumbnail(
                    url=f"https://raw.githubusercontent.com/SiegeEngineers/aoe2techtree/master/img/{entityDirectory}/unique_tech_1.png"
                )
            # Check to see if entity is a Castle Age Unique Tech
            elif input in unique_techs["imperial_age_unique_techs"]:
                embed.set_thumbnail(
                    url=f"https://raw.githubusercontent.com/SiegeEngineers/aoe2techtree/master/img/{entityDirectory}/unique_tech_2.png"
                )
            else:
                embed.set_thumbnail(
                    url=f"https://raw.githubusercontent.com/SiegeEngineers/aoe2techtree/master/img/{entityDirectory}/{unitBuildNum}.png"
                )
            embed.add_field(name="Cost", value=costString2, inline=True)

            if entity == "techs":
                embed.add_field(name="Research Time", value=get_tech_researchTime(unitBuildNum), inline=True)
                embed.add_field(name="Description", value=f"{descriptions[input]}", inline=False)

            else:
                embed.add_field(name="Hit Points", value=f"{get_HP(input, entity)}", inline=True)
                if "Base Melee" in get_attacks(input, entity):
                    embed.add_field(name="Base Melee Damage", value=f"{get_attacks(input, entity)['Base Melee']}", inline=True)
                if "Base Pierce" in get_attacks(input, entity):
                    embed.add_field(
                        name="Base Pierce Damage", value=f"{get_attacks(input, entity)['Base Pierce']}", inline=True
                    )
                embed.add_field(name="Melee Armor", value=f"{get_armours(input, entity)['Base Melee']}", inline=True)
                embed.add_field(name="Pierce Armor", value=f"{get_armours(input, entity)['Base Pierce']}", inline=True)
                if get_range(input, entity)["Range"] != 0:
                    embed.add_field(name="Range", value=f"{get_range(input, entity)['Range']} tiles", inline=True)
                if get_speed(input, entity) != 0:
                    embed.add_field(name="Speed", value=f"{get_speed(input, entity)} tiles/sec", inline=True)
            embed.set_footer(
                text=f"{ctx.author.name}\nFor more information run !advstats {input}",
                icon_url=ctx.author.display_avatar.url,
            )
            await ctx.send(embed=embed)

    @commands.command(name="!advstats", aliases=["!advstat"])
    async def advstatInfo(self, ctx: commands.Context, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
        """
        Command: !advstat
        Returns: Redirects user to the !does command due to renaming.
        """

        input = [arg1, arg2, arg3, arg4, arg5]
        input = [x.title() for x in input if x is not None]
        input = " ".join(input)

        if input not in techTreeDict:
            # This is when we do fuzzy suggestion and stop.
            fuzzy_search_scores = {}
            for item in techTreeDict:
                fuzzy_search_scores[item] = fuzz.ratio(input, item)
            top3 = sorted(fuzzy_search_scores, key=fuzzy_search_scores.get, reverse=True)[:3]
            error = f"There was an error with your input. Did you mean {top3[0]}, {top3[1]}, or {top3[2]}?"
            embed = discord.Embed(
                title="Invalid Input",
                description=error,
                color=discord.Color.red(),
            )
            await ctx.send(embed=embed)
        else:
            if input in localised_tech_name_lookup:
                unitBuildNum = localised_tech_name_lookup[input]
                entity = "techs"
                entityDirectory = "Techs"
            if input in localised_unit_building_name_lookup:
                unitBuildNum = localised_unit_building_name_lookup[input]
                if unitBuildNum in techtree["data"]["units"]:
                    entity = "units"
                    entityDirectory = "Units"
                if unitBuildNum in techtree["data"]["buildings"]:
                    entity = "buildings"
                    entityDirectory = "Buildings"

            cost = get_cost(input, entity)

            costString = ""
            if "Food" in cost:
                costString += f"{cost['Food']} <:food:978788983377121311> "
            if "Wood" in cost:
                costString += f"{cost['Wood']} <:woodAge:978788983435853834> "
            if "Gold" in cost:
                costString += f"{cost['Gold']} <:gold:978788983364546581> "
            if "Stone" in cost:
                costString += f"{cost['Stone']} <:stone:978788984547315792> "
            if costString != "":
                costString2 = costString
            else:
                costString2 = "No resources needed."

            if entity != "techs" and input[-1] != "s":
                embed = discord.Embed(title=f"{input} Stats", description=f"Information about {input}s.", color=0xD5D341)
            else:
                embed = discord.Embed(title=f"{input} Stats", description=f"Information about {input}.", color=0xD5D341)

            # Check to see if entity is a Castle Age Unique Tech
            if input in unique_techs["castle_age_unique_techs"]:
                embed.set_thumbnail(
                    url=f"https://raw.githubusercontent.com/SiegeEngineers/aoe2techtree/master/img/{entityDirectory}/unique_tech_1.png"
                )
            # Check to see if entity is a Castle Age Unique Tech
            elif input in unique_techs["imperial_age_unique_techs"]:
                embed.set_thumbnail(
                    url=f"https://raw.githubusercontent.com/SiegeEngineers/aoe2techtree/master/img/{entityDirectory}/unique_tech_2.png"
                )
            else:
                embed.set_thumbnail(
                    url=f"https://raw.githubusercontent.com/SiegeEngineers/aoe2techtree/master/img/{entityDirectory}/{unitBuildNum}.png"
                )
            embed.add_field(name="Cost", value=costString2, inline=True)

            if entity == "techs":
                embed.add_field(name="Research Time", value=get_tech_researchTime(unitBuildNum), inline=True)
                embed.add_field(name="Description", value=f"{descriptions[input]}", inline=False)
            else:
                embed.add_field(name="Hit Points", value=f"{get_HP(input, entity)}", inline=True)
                if "Base Melee" in get_attacks(input, entity):
                    embed.add_field(name="Base Melee Damage", value=f"{get_attacks(input, entity)['Base Melee']}", inline=True)
                if "Base Pierce" in get_attacks(input, entity):
                    embed.add_field(
                        name="Base Pierce Damage", value=f"{get_attacks(input, entity)['Base Pierce']}", inline=True
                    )

                if "Base Melee" in get_armours(input, entity):
                    embed.add_field(name="Base Melee Armor", value=f"{get_armours(input, entity)['Base Melee']}", inline=True)
                if "Base Pierce" in get_armours(input, entity):
                    embed.add_field(
                        name="Base Pierce Armor", value=f"{get_armours(input, entity)['Base Pierce']}", inline=True
                    )

                if get_range(input, entity)["Range"] != 0:
                    embed.add_field(name="Range", value=f"{get_range(input, entity)['Range']} tiles", inline=True)
                if get_range(input, entity)["Minimum Range"] != 0:
                    embed.add_field(
                        name="Minimum Range", value=f"{get_range(input, entity)['Minimum Range']} tiles", inline=True
                    )
                for key in get_attacks(input, entity):
                    if key != ("Base Melee") and key != ("Base Pierce"):
                        embed.add_field(name=f"{key} Damage", value=f"{get_attacks(input, entity)[key]}", inline=True)
                for key in get_armours(input, entity):
                    if key != ("Anti-Leitis") and key != ("Base Melee") and key != ("Base Pierce"):
                        embed.add_field(name=f"{key} Armor", value=f"{get_armours(input, entity)[key]}", inline=True)
                if get_attacks(input, entity):
                    embed.add_field(name="Accuracy", value=f"{get_accuracy(input, entity)}%", inline=True)
                    if entity == "units":
                        embed.add_field(
                            name="Attack Delay",
                            value=f"{round(float(get_attackDelay(input, entity)), 2)} sec",
                            inline=True,
                        )
                    if entity == "units":
                        embed.add_field(name="Frame Delay", value=f"{get_frameDelay(input, entity)}", inline=True)
                    embed.add_field(name="Reload Time", value=f"{get_reloadTime(input, entity)} sec", inline=True)
                embed.add_field(name="Line of Sight", value=f"{get_LineOfSight(input, entity)} tiles", inline=True)
                if get_speed(input, entity) != 0:
                    embed.add_field(name="Speed", value=f"{get_speed(input, entity)} tiles/sec", inline=True)
                if entity == "buildings":
                    embed.add_field(name="Build Time", value=f"{get_trainTime(input, entity)} sec", inline=True)
                if entity == "units":
                    embed.add_field(name="Train Time", value=f"{get_trainTime(input, entity)} sec", inline=True)
            if unitBuildNum in techtree["data"]["unit_upgrades"]:
                cost = get_upgrade_cost(unitBuildNum)
                costString = ""
                if "Food" in cost:
                    costString += f"{cost['Food']} <:food:978788983377121311> "
                if "Wood" in cost:
                    costString += f"{cost['Wood']} <:woodAge:978788983435853834> "
                if "Gold" in cost:
                    costString += f"{cost['Gold']} <:gold:978788983364546581> "
                if "Stone" in cost:
                    costString += f"{cost['Stone']} <:stone:978788984547315792> "
                if costString != "":
                    costString2 = costString
                else:
                    costString2 = "No resources needed."

                embed.add_field(name="Upgrade Cost", value=f"{costString2}", inline=True)
                embed.add_field(name="Upgrade Research Time", value=f"{get_upgrade_researchTime(unitBuildNum)}", inline=True)

            embed.set_footer(
                text=f"{ctx.author.name}\nFor less information run !stats {input}",
                icon_url=ctx.author.display_avatar.url,
            )
            await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(StatCommands(bot))
