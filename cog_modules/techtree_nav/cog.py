import asyncio
import csv
import json
import logging
import os
import random
import re
import sys
import time
from itertools import combinations

import aiohttp
import disnake
import numpy as np
from disnake.ext import commands, tasks
from dotenv import load_dotenv

from age_player import *
from cog_modules.error_handler import error_helping
from techTreeInfo import *

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
LUKE = os.getenv("LUKE_ID")


class TechTree_Nav(commands.Cog):
    """Commands for age of empires calls by players."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="!civ", help="Returns AoE2 civ tech tree information.")
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
            message = disnake.Embed(
                title="Invalid Input",
                description="There was a problem with your input. Please check your input and try again.",
                color=disnake.Color.red(),
            )
            await ctx.send(embed=message)

    @commands.command(
        name="!does",
        aliases=["!do", "!doeshave"],
        help="Returns if a civ(s) has a technology. !does [civs] have [techs]"
    )
    async def doesCiv(self, ctx: commands.Context, *args):
        age_civs = [
            "Britons",
            "Byzantines",
            "Celts",
            "Chinese",
            "Franks",
            "Goths",
            "Japanese",
            "Mongols",
            "Persians",
            "Saracens",
            "Teutons",
            "Turks",
            "Vikings",
            "Aztecs",
            "Huns",
            "Koreans",
            "Mayans",
            "Spanish",
            "Incas",
            "Hindustanis",
            "Italians",
            "Magyars",
            "Slavs",
            "Berbers",
            "Ethiopians",
            "Malians",
            "Portuguese",
            "Burmese",
            "Khmer",
            "Malay",
            "Vietnamese",
            "Bulgarians",
            "Cumans",
            "Lithuanians",
            "Tatars",
            "Burgundians",
            "Sicilians",
            "Bohemians",
            "Poles",
            "Dravidians",
            "Bengalis",
            "Gurjaras",
        ]
        response = ''
        TITLE = "Invalid Input"
        DESCRIPTION = "There was a problem with your input. Please check your input and try again."
        message = (
            disnake.Embed(
                title=TITLE,
                description=DESCRIPTION,
                color=disnake.Color.red(),
            )
            if not args
            else None
        )
        error = False if not message else True
        if error:
            await ctx.send(embed=message)
        if len(args) >= error_helping.MAX_USER_INPUT_WORD_LENGTH:
            message = disnake.Embed(
                title=f"Input is longer than accepted",
                description=f"acceptable amount = {error_helping.MAX_USER_INPUT_WORD_LENGTH}",
                color=disnake.Color.red(),
            )
            await ctx.send(embed=message)
        else:
            i = 0
            for i in range(len(args)):
                if args[i] == 'have':
                    splitNum = i 
                else:
                    i += 1 
            civs = args[:splitNum]
            techs = args[splitNum + 1:]
            time = 0
            for j in range(len(civs)):
                if civs[j].title() in age_civs:
                    for k in range(len(techs)):
                        if techs[k].title() in techTreeDict:
                            bool = civs[j].title() in techTreeDict[techs[k].title()]
                            if bool:
                                if time == 0:
                                    response = civs[j].title() + " have " + techs[k].title()
                                else: 
                                    response += "\n" + civs[j].title() + " have " + techs[k].title()
                            elif not bool:
                                if time == 0:
                                    response = civs[j].title() + " do not have " + techs[k].title()
                                else: 
                                    response += "\n" + civs[j].title() + " do not have " + techs[k].title()
                            time += 1
                        else:
                            if time == 0:
                                response += techs[k].title() + "was not found, check spelling."
                                time += 1
                            else:
                                response += "\n" + techs[k].title() + " was not found, check spelling."
                            
            await ctx.send(response)

    @commands.command(
        name="!whichciv",
        aliases=["!which", "!wc"],
        help="Returns which civ has the stated technology(ies)."
        "Encapsulate technology inside double-quotes if you aren't getting what you're looking for.",
    )
    async def civTech(self, ctx: commands.Context, *args):
        """
        Command: !whichciv [technology1 (+technology)] [(optional)technology2] [(optional)technology3] [(optional)technology4] [(optional)technology5]
        Returns: A list of civs that have that technology.
                 !whichciv [tech1+tech2]            returns all civs that have those techs (allows to search for multiple techs)
                 !whichciv [tech1]                  returns all civs that have that tech
                 !whichciv [techpart1] [techpart2]  returns all civs with that tech (accounts for spaces in tech name)
        """
        age_civs = [
            "Britons",
            "Byzantines",
            "Celts",
            "Chinese",
            "Franks",
            "Goths",
            "Japanese",
            "Mongols",
            "Persians",
            "Saracens",
            "Teutons",
            "Turks",
            "Vikings",
            "Aztecs",
            "Huns",
            "Koreans",
            "Mayans",
            "Spanish",
            "Incas",
            "Hindustanis",
            "Italians",
            "Magyars",
            "Slavs",
            "Berbers",
            "Ethiopians",
            "Malians",
            "Portuguese",
            "Burmese",
            "Khmer",
            "Malay",
            "Vietnamese",
            "Bulgarians",
            "Cumans",
            "Lithuanians",
            "Tatars",
            "Burgundians",
            "Sicilians",
            "Bohemians",
            "Poles",
            "Dravidians",
            "Bengalis",
            "Gurjaras",
        ]
        TITLE = "Invalid Input"
        DESCRIPTION = "There was a problem with your input. Please check your input and try again."
        message = (
            disnake.Embed(
                title=TITLE,
                description=DESCRIPTION,
                color=disnake.Color.red(),
            )
            if not args
            else None
        )
        error = False if not message else True
        if error:
            await ctx.send(embed=message)
        if len(args) >= error_helping.MAX_USER_INPUT_WORD_LENGTH:
            message = disnake.Embed(
                title=f"Input is longer than accepted",
                description=f"acceptable amount = {error_helping.MAX_USER_INPUT_WORD_LENGTH}",
                color=disnake.Color.red(),
            )
            await ctx.send(embed=message)
        else:
            responses = {}
            technologies = [re.sub(r"[^\w]", " ", tech).strip().title() for tech in args]
            if " ".join(technologies) not in techTreeDict.keys():
                for r in range(1, len(technologies) + 1):
                    for permutation in combinations(technologies, r):
                        tech = " ".join(permutation).strip()
                        try:
                            responses[tech] = techTreeDict[tech]
                        except:
                            continue
            else:
                tech = " ".join(technologies)
                responses[tech] = techTreeDict[tech]
            techs = ", ".join(responses.keys())
            civs = list(set.intersection(*map(set, list(responses.values()))))
            print(list(set(age_civs) - set(civs)))
            civs.sort()
            civs = ", ".join(civs)
            if len(civs) < 1:
                civs = f"Sorry there are no civs with: {techs}"
            message = disnake.Embed(
                title=f"{techs} are found in the following civ(s)", description=f"{civs}", color=disnake.Color.green()
            )
            await ctx.send(embed=message)

    # Lazy implementaion of complement of whichciv
    @commands.command(
        name="!whichcivnot",
        aliases=["!whichnot", "!wcn"],
        help="Returns which civ do not have the stated technology(ies)."
        "Encapsulate technology inside double-quotes if you aren't getting what you're looking for.",
    )
    async def civTechNot(self, ctx: commands.Context, *args):
        """
        Command: !whichcivnot [technology1 (+technology)] [(optional)technology2] [(optional)technology3] [(optional)technology4] [(optional)technology5]
        Returns: A list of civs that have that technology.
                 !whichcivnot [tech1+tech2]            returns all civs that have those techs (allows to search for multiple techs)
                 !whichcivnot [tech1]                  returns all civs that have that tech
                 !whichcivnot [techpart1] [techpart2]  returns all civs with that tech (accounts for spaces in tech name)
        """
        age_civs = [
            "Britons",
            "Byzantines",
            "Celts",
            "Chinese",
            "Franks",
            "Goths",
            "Japanese",
            "Mongols",
            "Persians",
            "Saracens",
            "Teutons",
            "Turks",
            "Vikings",
            "Aztecs",
            "Huns",
            "Koreans",
            "Mayans",
            "Spanish",
            "Incas",
            "Hindustanis",
            "Italians",
            "Magyars",
            "Slavs",
            "Berbers",
            "Ethiopians",
            "Malians",
            "Portuguese",
            "Burmese",
            "Khmer",
            "Malay",
            "Vietnamese",
            "Bulgarians",
            "Cumans",
            "Lithuanians",
            "Tatars",
            "Burgundians",
            "Sicilians",
            "Bohemians",
            "Poles",
            "Dravidians",
            "Bengalis",
            "Gurjaras",
        ]
        TITLE = "Invalid Input"
        DESCRIPTION = "There was a problem with your input. Please check your input and try again."
        message = (
            disnake.Embed(
                title=TITLE,
                description=DESCRIPTION,
                color=disnake.Color.red(),
            )
            if not args
            else None
        )
        error = False if not message else True
        if error:
            await ctx.send(embed=message)
        if len(args) >= error_helping.MAX_USER_INPUT_WORD_LENGTH:
            message = disnake.Embed(
                title=f"Input is longer than accepted",
                description=f"acceptable amount = {error_helping.MAX_USER_INPUT_WORD_LENGTH}",
                color=disnake.Color.red(),
            )
            await ctx.send(embed=message)
        else:
            responses = {}
            technologies = [re.sub(r"[^\w]", " ", tech).strip().title() for tech in args]
            if " ".join(technologies) not in techTreeDict.keys():
                for r in range(1, len(technologies) + 1):
                    for permutation in combinations(technologies, r):
                        tech = " ".join(permutation).strip()
                        try:
                            responses[tech] = techTreeDict[tech]
                        except:
                            continue
            else:
                tech = " ".join(technologies)
                responses[tech] = techTreeDict[tech]
            techs = ", ".join(responses.keys())
            civs = list(set.intersection(*map(set, list(responses.values()))))
            civs_not = list(set(age_civs) - set(civs))
            civs_not.sort()
            civs_not = ", ".join(civs_not)
            if len(civs_not) < 1:
                civs_not = f"Every civ has: {techs}"
            message = disnake.Embed(
                title=f"{techs} is missing from the following civ(s)", description=f"{civs_not}", color=disnake.Color.green()
            )
            await ctx.send(embed=message)


def setup(bot: commands.Bot):
    bot.add_cog(TechTree_Nav(bot))
