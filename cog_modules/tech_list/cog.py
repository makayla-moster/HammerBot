import os

import disnake
from disnake.ext import commands, tasks
from dotenv import load_dotenv

class TechListCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

def setup(bot: commands.Bot):
    bot.add_cog(TechListCommand(bot))
