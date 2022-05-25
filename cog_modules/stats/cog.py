import json
import os

import disnake
from disnake.ext import commands, tasks
from dotenv import load_dotenv

from full_tech_tree_processing import *
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

        cost = get_cost(arg1.title())
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

        embed = disnake.Embed(title=f"{arg1.title()} Stats", description=f"Information about {arg1.title()}s.", color=0xD5D341)
        embed.add_field(name="Cost", value=costString2, inline=True)
        embed.add_field(name="Hit Points", value=f"{get_HP(arg1.title())}", inline=True)
        if "Base Melee" in get_attacks(arg1.title()):
            embed.add_field(name="Attack", value=f"{get_attacks(arg1.title())['Base Melee']}", inline=True)
        if "Base Pierce" in get_attacks(arg1.title()):
            embed.add_field(name="Attack", value=f"{get_attacks(arg1.title())['Base Pierce']}", inline=True)
        embed.add_field(name="Melee Armor", value=f"{get_armours(arg1.title())['Base Melee']}", inline=True)
        embed.add_field(name="Pierce Armor", value=f"{get_armours(arg1.title())['Base Pierce']}", inline=True)
        embed.add_field(name="Range", value=f"{get_range(arg1.title())['Range']}", inline=True)
        # embed.add_field(name="Line of Sight", value=f"{get_LineOfSight(arg1.title())}", inline=True)
        embed.add_field(name="Speed", value=f"{get_speed(arg1.title())}", inline=True)
        # embed.add_field(name="Train Time", value=f"{get_trainTime(arg1.title())}", inline=True)
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

        cost = get_cost(arg1.title())
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

        embed = disnake.Embed(title=f"{arg1.title()} Stats", description=f"Information about {arg1.title()}s.", color=0xD5D341)
        embed.add_field(name="Cost", value=costString2, inline=True)
        for key in get_attacks(arg1.title()):
            embed.add_field(name=f"{key} Damage", value=f"{get_attacks(arg1.title())[key]}", inline=True)
        for key in get_armours(arg1.title()):
            embed.add_field(name=f"{key} Armor", value=f"{get_armours(arg1.title())[key]}", inline=True)

        embed.add_field(name="Hit Points", value=f"{get_HP(arg1.title())}", inline=True)
        embed.add_field(name="Range", value=f"{get_range(arg1.title())['Range']}", inline=True)
        embed.add_field(name="Minimum Range", value=f"{get_range(arg1.title())['Minimum Range']}", inline=True)
        embed.add_field(name="Accuracy", value=f"{get_accuracy(arg1.title())}%", inline=True)
        embed.add_field(name="Attack Delay", value=f"{get_attackDelay(arg1.title())}s", inline=True)
        embed.add_field(name="Frame Delay", value=f"{get_frameDelay(arg1.title())}", inline=True)
        embed.add_field(name="Reload Time", value=f"{get_reloadTime(arg1.title())}s", inline=True)
        embed.add_field(name="Line of Sight", value=f"{get_LineOfSight(arg1.title())}", inline=True)
        embed.add_field(name="Speed", value=f"{get_speed(arg1.title())}", inline=True)
        embed.add_field(name="Train Time", value=f"{get_trainTime(arg1.title())}s", inline=True)
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(StatCommands(bot))
