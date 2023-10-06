import asyncio
import datetime
import os
import pickle
import random

import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

from gizmopics import *
from resources import gizmoResources, taoResources

load_dotenv()
CATS = os.getenv("x-api-key")
botDMs = int(os.getenv("DMChannel"))
botID = int(os.getenv("BOTID"))


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

    @cat.error
    async def cat_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                f"You can only get 1 cat picture every 30 seconds. Try again in {round(error.retry_after, 2)} seconds."
            )

    @commands.command(name="!gizmo", aliases=["!gismo", "!gizmø"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def gizmo(self, ctx: commands.Context):
        num = random.randint(0, len(gizmoPics) - 1)
        info = f"Gizmo #{num + 1} of {len(gizmoPics)}."
        pic = gizmoPics[num]
        gizmoResources[pic] += 1
        with open("gizmoResources", "wb") as f:
            pickle.dump(gizmoResources, f)
        most_common = gizmoResources.most_common(2)
        if most_common[0][1] != most_common[1][1] and pic == most_common[0][0]:
            info += f" HammerBot's favorite Gizmo pic! Shown {most_common[0][1]} times."
        elif gizmoResources[pic] == 1:
            info += " First time shown! ^_^"
        else:
            info += f" Shown {gizmoResources[pic]} times."
        await ctx.send(info)
        await ctx.send(pic)

    @gizmo.error
    async def gizmo_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                f"Gizmo likes to hide, so you can only view him once every 30 seconds. Try again in {round(error.retry_after, 2)} seconds."
            )

    @commands.command(name="!tao", aliases=["!taø"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def tao(self, ctx: commands.Context):
        num = random.randint(0, len(taoPics) - 1)
        info = f"Tao #{num + 1} of {len(taoPics)}."
        pic = taoPics[num]
        taoResources[pic] += 1
        with open("taoResources", "wb") as f:
            pickle.dump(taoResources, f)
        most_common = taoResources.most_common(2)
        if most_common[0][1] != most_common[1][1] and pic == most_common[0][0]:
            info += f" HammerBot's favorite Tao pic! Shown {most_common[0][1]} times."
        elif gizmoResources[pic] == 1:
            info += " First time shown! ^_^"
        else:
            info += f" Shown {taoResources[pic]} times."
        await ctx.send(info)
        await ctx.send(pic)

    @tao.error
    async def tao_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(
                f"Tao is shy, so you can only view him once every 30 seconds. Try again in {round(error.retry_after, 2)} seconds."
            )

    @commands.command(name="Gizmo or Tao?")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def taoVgizmo(self, ctx: commands.Context):
        gizmo_count = gizmoResources.total()
        tao_count = taoResources.total()
        if gizmo_count > tao_count:
            info = f"Tao is more elusive, but I still like him."
        elif gizmo_count < tao_count:
            info = f"Gizmo is more elusive, but I still like him."
        else:
            info = f"I like Gizmo and Tao equally."
        await ctx.send(info)

    # Checks to see if someone DMs the bot
    # If so, it forwards the message to a specific channel and replies to the
    # person who sent the message
    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel):  # if the message is a DM
            channel = self.bot.get_channel(botDMs)  # get channel to forward message to
            if message.author.id != botID:  # make sure we're not forwarding/sending messages when the bot messages
                newMessage = discord.Embed(
                    title=f"New bot DM from `{message.author}`", description=f"{message.content}", timestamp=message.created_at
                )
                await channel.send(embed=newMessage)  # forwards message to channel
            await self.bot.process_commands(message)


async def setup(bot: commands.Bot):
    await bot.add_cog(Random(bot))
