import os

import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv


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
        response = f'Sent to "{message.author}": 1000 Food'
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
