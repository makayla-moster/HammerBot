from discord.ext import tasks, commands
import aiohttp, asyncio, discord

class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error:commands.CommandError):
        """A global error handler cog."""

        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.CommandOnCooldown):
            message = discord.Embed(title="Command on Cooldown", description=f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds.", color=discord.Color.red())
        elif isinstance(error, commands.MissingPermissions):
            message = discord.Embed(title="Missing Permissions", description="You are missing the required permissions to run this command.", color = discord.Color.red())
        else:
            message = discord.Embed(title="Tell @quela about this", description="If you are seeing this, something has gone horribly wrong.", color = discord.Color.red())

        await ctx.send(embed=message)

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
