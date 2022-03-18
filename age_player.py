import asyncio
import csv
import sys

import aiohttp
import disnake
import requests
from disnake.ext import commands, tasks


async def getPlayerInfo(self, client_sesh: aiohttp.ClientSession) -> dict:
    r = await client_sesh.get(f"https://aoe2.net/api/leaderboard?game=aoe2de&profile_id={self.id}&leaderboard_id=4")
    return await r.json(content_type=None)


async def getPlayer1v1Info(self, client_sesh: aiohttp.ClientSession) -> dict:
    r = await client_sesh.get(f"https://aoe2.net/api/leaderboard?game=aoe2de&profile_id={self.id}&leaderboard_id=3")
    return await r.json(content_type=None)


async def getPlayerTGRating(self, client_sesh: aiohttp.ClientSession) -> dict:
    r = await client_sesh.get(
        f"https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=4&profile_id={self.id}&count=1"
    )
    return await r.json(content_type=None)


async def getPlayer1v1Rating(self, client_sesh: aiohttp.ClientSession) -> dict:
    r = await client_sesh.get(
        f"https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=3&profile_id={self.id}&count=1"
    )
    return await r.json(content_type=None)


async def getPlayerEWTGRating(self, client_sesh: aiohttp.ClientSession) -> dict:
    r = await client_sesh.get(
        f"https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=14&profile_id={self.id}&count=1"
    )
    return await r.json(content_type=None)


async def getPlayerEW1v1Rating(self, client_sesh: aiohttp.ClientSession) -> dict:
    r = await client_sesh.get(
        f"https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=13&profile_id={self.id}&count=1"
    )
    return await r.json(content_type=None)


async def getAllOfTheInfo(self):
    async with aiohttp.ClientSession() as client_sesh:
        responses: List[dict] = await asyncio.gather(
            getPlayerInfo(self, client_sesh),
            getPlayer1v1Info(self, client_sesh),
            getPlayerTGRating(self, client_sesh),
            getPlayer1v1Rating(self, client_sesh),
            getPlayerEWTGRating(self, client_sesh),
            getPlayerEW1v1Rating(self, client_sesh),
        )
        return responses


async def get_json_info2():
    """
    Helper function for pulling the last AoE2 match played by BSHammer. Is looped every 75 seconds to have up-to-date json info.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get("https://aoe2.net/api/strings?game=aoe2de&language=en") as r:
            r = await r.json(content_type=None)
            await session.close()
            return r


class Player:
    def __init__(self, id, team, color, name, civ, game, map):
        self.id = id
        self.team = team
        self.color = color
        self.name = name
        self.country = "--"
        self.tg_rating = 0
        self.rating = 0
        self.ew_tg_rating = 0
        self.ew_rating = 0
        self.civ = civ
        self.map = map
        self.game = game

    async def info(self):
        responses = await getAllOfTheInfo(self)

        player_tg = responses[0]
        player_1v1 = responses[1]
        player_tg_rate = responses[2]
        player_1v1_rate = responses[3]
        player_tg_ew_rate = responses[4]
        player_1v1_ew_rate = responses[5]

        if len(player_tg["leaderboard"]) > 0:
            playerLeaderboard = player_tg["leaderboard"][0]
            self.country = playerLeaderboard["country"]

        if len(player_1v1["leaderboard"]) > 0:
            playerLeaderboard = player_1v1["leaderboard"][0]
            self.country = playerLeaderboard["country"]

        if len(player_1v1_rate) > 0:
            self.rating = player_1v1_rate[0]["rating"]

        if len(player_tg_rate) > 0:
            self.tg_rating = player_tg_rate[0]["rating"]

        if len(player_1v1_ew_rate) > 0:
            self.ew_rating = player_1v1_ew_rate[0]["rating"]

        if len(player_tg_ew_rate) > 0:
            self.ew_tg_rating = player_tg_ew_rate[0]["rating"]


async def getInfo():
    # this function only needs to be called once... all info never changes
    resps = await get_json_info2()
    mapType = resps["map_type"]
    civTypes = resps["civ"]
    gameTypes = resps["game_type"]

    name_by_id = dict([(str(p["id"]), p["string"]) for p in mapType])
    civ_by_id = dict([(str(p["id"]), p["string"]) for p in civTypes])
    game_by_id = dict([(str(p["id"]), p["string"]) for p in gameTypes])
    return name_by_id, civ_by_id, game_by_id


async def getPlayerIDs(resp):
    name_by_id, civ_by_id, game_by_id = await getInfo()

    lastmatch = resp["last_match"]
    playerName = resp["name"]
    players = []

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
        players.append(
            Player(
                player["profile_id"],
                player["team"],
                color,
                player["name"],
                civ_by_id[str(civNum)],
                game_by_id[str(game)],
                name_by_id[str(mapNum)],
            )
        )
    return players
