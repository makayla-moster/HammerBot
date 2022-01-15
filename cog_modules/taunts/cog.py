import os
from dotenv import load_dotenv
from discord.ext import tasks, commands

class Taunts(commands.Cog):
    """Replies with taunts from AoE2"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="30")
    async def monk_30(self, ctx: commands.Context):
        """
        Command: 30
        Returns: The age taunt #30. (Wololo!)
        """
        response = "Wololo!"
        await ctx.send(response)

    @commands.command(name='14', help='Returns AoE2 taunt #14.')
    # @commands.cooldown(1, 30, commands.BucketType.user)
    async def startTheGame(self, ctx: commands.Context):
        """
        Command: 14
        Returns: The age2 taunt #14. (Start the game already!)
        """
        response = "Start the game already!"
        await ctx.send(response)

    @commands.command(name='13', help='Returns AoE2 taunt #13.')
    # @commands.cooldown(1, 30, commands.BucketType.user)
    async def isp(self, ctx:commands.Context):
        """
        Command: 13
        Returns: The age2 taunt #13. (Sure, blame it on your ISP.)
        """
        response = "Sure, blame it on your ISP."
        await ctx.send(response)

    @commands.command(name='age?', help='Returns AoE2 taunt #30.')
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

def setup(bot: commands.Bot):
    bot.add_cog(Taunts(bot))
