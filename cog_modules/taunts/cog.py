import json
import os
import random

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

from resources import *


class Taunts(commands.Cog):
    """Replies with taunts from AoE2"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="1")
    async def yes_1(self, ctx: commands.Context):
        """
        Command: 1
        Returns: The age taunt #1. (Yes.)
        """
        response = "Yes."
        await ctx.send(response)

    @commands.command(name="2")
    async def no_2(self, ctx: commands.Context):
        """
        Command: 2
        Returns: The age taunt #2. (No.)
        """
        response = "No."
        await ctx.send(response)

    @commands.command(name="3")
    async def no_3(self, ctx: commands.Context):
        response = f'Sent to "{ctx.message.author.display_name}": 1000 Food'
        await ctx.send(response)

    @commands.command(name="4")
    async def no_4(self, ctx: commands.Context):
        response = f'Sent to "{ctx.message.author.display_name}": 1000 Wood'
        await ctx.send(response)

    @commands.command(name="5")
    async def no_5(self, ctx: commands.Context):
        response = f'Sent to "{ctx.message.author.display_name}": 1000 Gold'
        await ctx.send(response)

    @commands.command(name="6")
    async def no_6(self, ctx: commands.Context):
        response = f'Sent to "{ctx.message.author.display_name}": 1000 Stone'
        await ctx.send(response)

    @commands.command(name="28")
    async def otherguy_28(self, ctx: commands.Context):
        """
        Command: 28
        Returns: The age taunt #28. (Yeah, well, you should see the other guy.)
        """
        response = "Yeah, well, you should see the other guy."
        await ctx.send(response)

    @commands.command(name="30")
    async def monk_30(self, ctx: commands.Context):
        """
        Command: 30
        Returns: The age taunt #30. (Wololo!)
        """
        response = "Wololo!"
        await ctx.send(response)

    @commands.command(name="14", help="Returns AoE2 taunt #14.")
    # @commands.cooldown(1, 30, commands.BucketType.user)
    async def startTheGame(self, ctx: commands.Context):
        """
        Command: 14
        Returns: The age2 taunt #14. (Start the game already!)
        """
        response = "Start the game already!"
        await ctx.send(response)

    @commands.command(name="13", help="Returns AoE2 taunt #13.")
    # @commands.cooldown(1, 30, commands.BucketType.user)
    async def isp(self, ctx: commands.Context):
        """
        Command: 13
        Returns: The age2 taunt #13. (Sure, blame it on your ISP.)
        """
        response = "Sure, blame it on your ISP."
        await ctx.send(response)

    @commands.command(name="age?", help="Returns AoE2 taunt #30.")
    # @commands.cooldown(1, 30, commands.BucketType.user)
    async def questionableAge(self, ctx: commands.Context):
        """
        Command: age?
        Returns: The phrase "Well, duh."
        """
        response = "Well, duh."
        await ctx.send(response)

    @commands.command(name="!stockpile")
    async def stockpile(self, ctx: commands.Context):
        user = str(ctx.message.author.name)
        if user in serverResources:
            food = serverResources[user]["Food"]
            wood = serverResources[user]["Wood"]
            gold = serverResources[user]["Gold"]
            stone = serverResources[user]["Stone"]
            embed = discord.Embed(
                title=f"{ctx.message.author.display_name}'s Resource Stockpile",
                description=f"The amount of resources HammerBot has gifted you.",
                color=0xD5D341,
            )
            embed.add_field(name="Food", value=food + "<:food:978788983377121311>", inline=True)
            embed.add_field(name="Wood", value=wood + "<:woodAge:978788983435853834>", inline=True)
            embed.add_field(name="Gold", value=gold + "<:gold:978788983364546581>", inline=True)
            embed.add_field(name="Stone", value=stone + "<:stone:978788984547315792>", inline=True)
            embed.set_footer(
                text=f"{ctx.author.display_name}\nTo get more resources type `38` in chat.",
                icon_url=ctx.author.display_avatar.url,
            )
        else:
            serverResources[user] = {"Food": "0", "Wood": "0", "Gold": "0", "Stone": "0"}
            embed = discord.Embed(
                title=f"{ctx.message.author.display_name}'s Resource Stockpile",
                description=f"The amount of resources HammerBot has gifted you.",
                color=0xD5D341,
            )
            embed.add_field(name="Food", value="0" + "<:food:978788983377121311>", inline=True)
            embed.add_field(name="Wood", value="0" + "<:woodAge:978788983435853834>", inline=True)
            embed.add_field(name="Gold", value="0" + "<:gold:978788983364546581>", inline=True)
            embed.add_field(name="Stone", value="0" + "<:stone:978788984547315792>", inline=True)
            embed.set_footer(
                text=f"{ctx.author.display_name}\nTo get more resources type `38` in chat.",
                icon_url=ctx.author.display_avatar.url,
            )

        await ctx.send(embed=embed)

    @commands.command(name="!printdict")
    async def printdict(self, ctx: commands.Context):
        print(serverResources)
        # with open('serverResources.json', 'w') as f:
        #     json.dump(serverResources, f)

    @commands.command(name="38")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def no_38(self, ctx: commands.Context):
        user = str(ctx.message.author.name)
        res = random.choice(["Wood", "Food", "Gold", "Stone"])
        num = random.randint(-1000, 1000)
        response = f'Sent to "{ctx.message.author.display_name}": {num} {res}'
        if user in serverResources:
            currentRes = serverResources[user][res]
            serverResources[user][res] = str(int(currentRes) + int(num))
            response += f"\n You now have ||{serverResources[user][res}|| {res} "
        else:
            serverResources[user] = {"Food": "0", "Wood": "0", "Gold": "0", "Stone": "0"}
            serverResources[user][res] = str(num)
        await ctx.send(response)

    @no_38.error
    async def no_38_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"You can only get resources every 30 seconds. Try again in {round(error.retry_after, 2)} seconds.")

    @commands.command(name="58")
    async def no_58(self, ctx: commands.Context):
        response = f"Sent {ctx.message.author.display_name}'s lunch money to Gizmo. Rest in pieces, plants."
        await ctx.send(response)

    @commands.command(name="11")
    async def laugh(self, ctx: commands.Context):
        """
        Command: 11
        Returns: The age taunt #11. (*laughter*)
        """
        response = "🤣"
        await ctx.send(response)

    @commands.command(name="!gg")
    async def gg(self, ctx: commands.Context):
        """
        Command: :gg:
        Returns: The server GG emote.
        """
        response = "<:gg:861701719050551307>"
        await ctx.send(response)


async def setup(bot: commands.Bot):
    await bot.add_cog(Taunts(bot))
