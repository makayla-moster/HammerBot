import asyncio
import os
import disnake
import requests
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()
CATS = os.getenv("x-api-key")


class Random(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="!cat", aliases=["!cotd", "!cats"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def cat(self, ctx: commands.Context):
        url = f"https://api.thecatapi.com/v1/images/search?api_key={CATS}"
        response = requests.get(url, timeout=5)
        res = response.json()
        await ctx.send(res[0]["url"])


def setup(bot: commands.Bot):
    bot.add_cog(Random(bot))
