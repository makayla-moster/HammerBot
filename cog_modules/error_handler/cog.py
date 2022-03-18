import ast
import asyncio
import os
import traceback

import aiohttp
import disnake
from disnake.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
ERROR_CHANNEL_ID = int(os.getenv("ERROR_CHANNEL_ID"))


def format_exception(e: Exception) -> str:
    return "".join(traceback.format_exception(type(e), e, e.__traceback__, 4))


class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""

        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.CommandOnCooldown):
            message = disnake.Embed(
                title="Command on Cooldown",
                description=f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds.",
                color=disnake.Color.red(),
            )
        elif isinstance(error, commands.MissingPermissions):
            message = disnake.Embed(
                title="Missing Permissions",
                description="You are missing the required permissions to run this command.",
                color=disnake.Color.red(),
            )
        elif isinstance(error, commands.BadArgument):
            message = disnake.Embed(
                title="Bad Argument",
                description="You have input an invalid parameter for this command.",
                color=disnake.Color.red(),
            )
        elif isinstance(error, commands.ExpectedClosingQuoteError):
            message = disnake.Embed(
                title="Missing Quotes",
                description="Quotes are required for multi-word arguments for this command.",
                color=disnake.Color.red(),
            )
        elif isinstance(error, commands.ArgumentParsingError):
            message = disnake.Embed(
                title="Argument Error",
                description="Looks like that argument didn't work. Please try again with a different one.",
                color=disnake.Color.red(),
            )
        elif isinstance(error, commands.TooManyArguments):
            message = disnake.Embed(
                title="Too Many Arguments",
                description="You have too many arguments for the command. Please try again with less arguments.",
                color=disnake.Color.red(),
            )
        elif isinstance(error, commands.UserInputError):
            message = disnake.Embed(
                title="Input Error",
                description="There was a problem with your input. Please check your input and try again.",
                color=disnake.Color.red(),
            )
        elif isinstance(error, commands.CommandInvokeError):
            message = disnake.Embed(
                title="Command Error",
                description="There was a problem with the command. Check your input or aoe2.net.",
                color=disnake.Color.red(),
            )
        else:
            error_nice = format_exception(error)
            print(error_nice)
            message = disnake.Embed(
                title="Tell @quela about this",
                description="If you are seeing this, something has gone horribly wrong.",
                color=disnake.Color.red(),
            )

            # log error in error channel
            debug_info = (
                f"```\n{ctx.author} {ctx.author.id}: {ctx.message.content}"[:200]
                + "```"
                + f"```py\n{error_nice.replace('```', '｀｀｀')}"[: 2000 - 206]
                + "```"
            )

            error_channel = self.bot.get_channel(ERROR_CHANNEL_ID)

            if error_channel is not None:
                await error_channel.send(debug_info)

        await ctx.send(embed=message)


def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))
