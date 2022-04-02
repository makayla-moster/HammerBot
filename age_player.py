import asyncio
import csv
import sys

import aiohttp
import disnake
import requests
from disnake.ext import commands, tasks

from PlayerClass import *


async def get_backup_info(client_sesh: aiohttp.ClientSession) -> dict:
    """
    Helper function for pulling the last AoE2 match played by BSHammer. Is looped every 75 seconds to have up-to-date json info.
    """
    r = await client_sesh.get("https://aoe2.net/api/player/matches?game=aoe2de&profile_id=313591&count=1")
    return await r.json(content_type=None)


async def get_json_info2(client_sesh: aiohttp.ClientSession) -> dict:
    """
    Helper function for pulling the last AoE2 match played by BSHammer. Is looped every 75 seconds to have up-to-date json info.
    """
    r = await client_sesh.get("https://aoe2.net/api/strings?game=aoe2de&language=en")
    return await r.json(content_type=None)


async def getMatchInfo():
    async with aiohttp.ClientSession() as client_sesh:
        responses: List[dict] = await asyncio.gather(
            get_backup_info(client_sesh),
            get_json_info2(client_sesh),
        )
        return responses


async def getInfo():
    # this function only needs to be called once... all info never changes
    responses = await getMatchInfo()
    resp = responses[0][0]
    resps = responses[1]
    mapType = resps["map_type"]
    civTypes = resps["civ"]
    gameTypes = resps["game_type"]
    playerInfo = resp["players"]

    name_by_id = dict([(str(p["id"]), p["string"]) for p in mapType])
    civ_by_id = dict([(str(p["id"]), p["string"]) for p in civTypes])
    game_by_id = dict([(str(p["id"]), p["string"]) for p in gameTypes])
    return name_by_id, civ_by_id, game_by_id, playerInfo


async def getPlayerIDs(resp):
    name_by_id, civ_by_id, game_by_id, playerInfo = await getInfo()

    lastmatch = resp["last_match"]
    playerName = resp["name"]
    playerId = resp["profile_id"]
    players = []

    count = 0
    for player in lastmatch["players"]:
        if player["color"] == 1:
            color = ":blue_circle:"
        elif player["color"] == 2:
            color = ":red_circle:"
        elif player["color"] == 3:
            color = ":green_circle:"
        elif player["color"] == 4:
            color = ":yellow_circle:"
        elif player["color"] == 5:
            color = ":globe_with_meridians:"
        elif player["color"] == 6:
            color = ":purple_circle:"
        elif player["color"] == 7:
            color = ":white_circle:"
        else:
            color = ":orange_circle:"
        mapNum = lastmatch["map_type"]
        civNum = player["civ"]
        game = lastmatch["game_type"]

        if player["name"] == None:
            name = playerInfo[count]["name"]
        else:
            name = player["name"]

        players.append(
            Player(
                player["profile_id"],
                player["team"],
                color,
                name,
                civ_by_id[str(civNum)],
                game_by_id[str(game)],
                name_by_id[str(mapNum)],
            )
        )
        count += 1
    return players
