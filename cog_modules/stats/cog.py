import json
import os

import disnake
from disnake.ext import commands, tasks
from dotenv import load_dotenv

from full_tech_tree_processing import *
from techtree_descriptions import *
from techTreeInfo import *


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

        if arg5 is not None:
            arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title() + " " + arg4.title() + " " + arg5.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = disnake.Embed(
                    title="Invalid Input",
                    description="There was a problem with your input. Please check your input and try again.",
                    color=disnake.Color.red(),
                )

        elif arg4 is not None:
            arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title() + " " + arg4.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = disnake.Embed(
                    title="Invalid Input",
                    description="There was a problem with your input. Please check your input and try again.",
                    color=disnake.Color.red(),
                )

        elif arg3 is not None:
            arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = disnake.Embed(
                    title="Invalid Input",
                    description="There was a problem with your input. Please check your input and try again.",
                    color=disnake.Color.red(),
                )

        elif arg2 is not None:
            arg1 = arg1.title() + " " + arg2.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = disnake.Embed(
                    title="Invalid Input",
                    description="There was a problem with your input. Please check your input and try again.",
                    color=disnake.Color.red(),
                )

        if arg1.title() in localised_tech_name_lookup:
            unitBuildNum = localised_tech_name_lookup[arg1.title()]
            entity = "techs"
            entityDirectory = "Techs"
        if arg1.title() in localised_unit_building_name_lookup:
            unitBuildNum = localised_unit_building_name_lookup[arg1.title()]
            if unitBuildNum in techtree["data"]["units"]:
                entity = "units"
                entityDirectory = "Units"
            if unitBuildNum in techtree["data"]["buildings"]:
                entity = "buildings"
                entityDirectory = "Buildings"



        print(entity)


        cost = get_cost(arg1.title(), entity)
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

        if entity != "techs" and arg1.title()[-1] != "s":
            embed = disnake.Embed(
                title=f"{arg1.title()} Stats", description=f"Information about {arg1.title()}s.", color=0xD5D341
            )
        else:
            embed = disnake.Embed(
                title=f"{arg1.title()} Stats", description=f"Information about {arg1.title()}.", color=0xD5D341
            )
        embed.set_thumbnail(
            url=f"https://raw.githubusercontent.com/SiegeEngineers/aoe2techtree/master/img/{entityDirectory}/{unitBuildNum}.png"
        )
        embed.add_field(name="Cost", value=costString2, inline=True)

        if entity == "techs":
            embed.add_field(name="Description", value=f"{descriptions[arg1.title()]}", inline=False)

        else:
            embed.add_field(name="Hit Points", value=f"{get_HP(arg1.title(), entity)}", inline=True)
            if "Base Melee" in get_attacks(arg1.title(), entity):
                embed.add_field(
                    name="Base Melee Damage", value=f"{get_attacks(arg1.title(), entity)['Base Melee']}", inline=True
                )
            if "Base Pierce" in get_attacks(arg1.title(), entity):
                embed.add_field(
                    name="Base Pierce Damage", value=f"{get_attacks(arg1.title(), entity)['Base Pierce']}", inline=True
                )
            embed.add_field(name="Melee Armor", value=f"{get_armours(arg1.title(), entity)['Base Melee']}", inline=True)
            embed.add_field(name="Pierce Armor", value=f"{get_armours(arg1.title(), entity)['Base Pierce']}", inline=True)
            if get_range(arg1.title(), entity)["Range"] != 0:
                embed.add_field(name="Range", value=f"{get_range(arg1.title(), entity)['Range']} tiles", inline=True)
            if get_speed(arg1.title(), entity) != 0:
                embed.add_field(name="Speed", value=f"{get_speed(arg1.title(), entity)} tiles/sec", inline=True)
        embed.set_footer(
            text=f"{ctx.author.name}\nFor more information run !advstats {arg1.title()}",
            icon_url=ctx.author.display_avatar.url,
        )
        await ctx.send(embed=embed)

    @commands.command(name="!advstats", aliases=["!advstat"])
    async def advstatInfo(self, ctx: commands.Context, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
        """
        Command: !advstat
        Returns: Redirects user to the !does command due to renaming.
        """

        if arg5 is not None:
            arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title() + " " + arg4.title() + " " + arg5.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = disnake.Embed(
                    title="Invalid Input",
                    description="There was a problem with your input. Please check your input and try again.",
                    color=disnake.Color.red(),
                )

        elif arg4 is not None:
            arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title() + " " + arg4.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = disnake.Embed(
                    title="Invalid Input",
                    description="There was a problem with your input. Please check your input and try again.",
                    color=disnake.Color.red(),
                )

        elif arg3 is not None:
            arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = disnake.Embed(
                    title="Invalid Input",
                    description="There was a problem with your input. Please check your input and try again.",
                    color=disnake.Color.red(),
                )

        elif arg2 is not None:
            arg1 = arg1.title() + " " + arg2.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = disnake.Embed(
                    title="Invalid Input",
                    description="There was a problem with your input. Please check your input and try again.",
                    color=disnake.Color.red(),
                )

        if arg1.title() in localised_tech_name_lookup:
            unitBuildNum = localised_tech_name_lookup[arg1.title()]
            entity = "techs"
            entityDirectory = "Techs"
        if arg1.title() in localised_unit_building_name_lookup:
            unitBuildNum = localised_unit_building_name_lookup[arg1.title()]
            if unitBuildNum in techtree["data"]["units"]:
                entity = "units"
                entityDirectory = "Units"
            if unitBuildNum in techtree["data"]["buildings"]:
                entity = "buildings"
                entityDirectory = "Buildings"

        cost = get_cost(arg1.title(), entity)

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

        if entity != "techs" and arg1.title()[-1] != "s":
            embed = disnake.Embed(
                title=f"{arg1.title()} Stats", description=f"Information about {arg1.title()}s.", color=0xD5D341
            )
        else:
            embed = disnake.Embed(
                title=f"{arg1.title()} Stats", description=f"Information about {arg1.title()}.", color=0xD5D341
            )

        embed.set_thumbnail(
            url=f"https://raw.githubusercontent.com/SiegeEngineers/aoe2techtree/master/img/{entityDirectory}/{unitBuildNum}.png"
        )
        embed.add_field(name="Cost", value=costString2, inline=True)

        if entity == "techs":
            embed.add_field(name="Description", value=f"{descriptions[arg1.title()]}", inline=False)
        else:
            embed.add_field(name="Hit Points", value=f"{get_HP(arg1.title(), entity)}", inline=True)
            if "Base Melee" in get_attacks(arg1.title(), entity):
                embed.add_field(
                    name="Base Melee Damage", value=f"{get_attacks(arg1.title(), entity)['Base Melee']}", inline=True
                )
            if "Base Pierce" in get_attacks(arg1.title(), entity):
                embed.add_field(
                    name="Base Pierce Damage", value=f"{get_attacks(arg1.title(), entity)['Base Pierce']}", inline=True
                )

            if "Base Melee" in get_armours(arg1.title(), entity):
                embed.add_field(
                    name="Base Melee Armor", value=f"{get_armours(arg1.title(), entity)['Base Melee']}", inline=True
                )
            if "Base Pierce" in get_armours(arg1.title(), entity):
                embed.add_field(
                    name="Base Pierce Armor", value=f"{get_armours(arg1.title(), entity)['Base Pierce']}", inline=True
                )

            if get_range(arg1.title(), entity)["Range"] != 0:
                embed.add_field(name="Range", value=f"{get_range(arg1.title(), entity)['Range']} tiles", inline=True)
            if get_range(arg1.title(), entity)["Minimum Range"] != 0:
                embed.add_field(
                    name="Minimum Range", value=f"{get_range(arg1.title(), entity)['Minimum Range']} tiles", inline=True
                )
            for key in get_attacks(arg1.title(), entity):
                if key != ("Base Melee") and key != ("Base Pierce"):
                    embed.add_field(name=f"{key} Damage", value=f"{get_attacks(arg1.title(), entity)[key]}", inline=True)
            for key in get_armours(arg1.title(), entity):
                if key != ("Anti-Leitis") and key != ("Base Melee") and key != ("Base Pierce"):
                    embed.add_field(name=f"{key} Armor", value=f"{get_armours(arg1.title(), entity)[key]}", inline=True)
            if get_attacks(arg1.title(), entity):
                embed.add_field(name="Accuracy", value=f"{get_accuracy(arg1.title(), entity)}%", inline=True)
                if entity == "units":
                    embed.add_field(
                        name="Attack Delay", value=f"{round(float(get_attackDelay(arg1.title(), entity)), 2)} sec", inline=True
                    )
                if entity == "units":
                    embed.add_field(name="Frame Delay", value=f"{get_frameDelay(arg1.title(), entity)}", inline=True)
                embed.add_field(name="Reload Time", value=f"{get_reloadTime(arg1.title(), entity)} sec", inline=True)
            embed.add_field(name="Line of Sight", value=f"{get_LineOfSight(arg1.title(), entity)} tiles", inline=True)
            if get_speed(arg1.title(), entity) != 0:
                embed.add_field(name="Speed", value=f"{get_speed(arg1.title(), entity)} tiles/sec", inline=True)
            if entity == "buildings":
                embed.add_field(name="Build Time", value=f"{get_trainTime(arg1.title(), entity)} sec", inline=True)
            if entity == "units":
                embed.add_field(name="Train Time", value=f"{get_trainTime(arg1.title(), entity)} sec", inline=True)

        embed.set_footer(
            text=f"{ctx.author.name}\nFor less information run !stats {arg1.title()}", icon_url=ctx.author.display_avatar.url
        )
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(StatCommands(bot))
