import csv
import requests
import sys
import aiohttp
import asyncio
import discord
from discord.ext import tasks, commands

async def get_json_info2():
    """
    Helper function for pulling the last AoE2 match played by BSHammer. Is looped every 75 seconds to have up-to-date json info.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get('https://aoe2.net/api/strings?game=aoe2de&language=en') as r:
            r = await r.json(content_type=None)
            await session.close()
            return r

async def getPlayerURLInfo(self):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://aoe2.net/api/leaderboard?game=aoe2de&profile_id={self.id}&leaderboard_id=4') as r:
            r = await r.json(content_type=None)
            await session.close()
            return r

async def getPlayer1v1Info(self):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://aoe2.net/api/leaderboard?game=aoe2de&profile_id={self.id}&leaderboard_id=3') as r:
            r = await r.json(content_type=None)
            await session.close()
            return r

async def getPlayerEW1v1Info(self):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://aoe2.net/api/leaderboard?game=aoe2de&profile_id={self.id}&leaderboard_id=13') as r:
            r = await r.json(content_type=None)
            await session.close()
            return r

async def getPlayerEWInfo(self):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://aoe2.net/api/leaderboard?game=aoe2de&profile_id={self.id}&leaderboard_id=14') as r:
            r = await r.json(content_type=None)
            await session.close()
            return r

async def getPlayerTGRate(self):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=4&profile_id={self.id}&count=1') as r:
            r = await r.json(content_type=None)
            await session.close()
            return r

async def getPlayer1v1Rate(self):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=3&profile_id={self.id}&count=1') as r:
            r = await r.json(content_type=None)
            await session.close()
            return r

async def getPlayerTGEWRate(self):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=14&profile_id={self.id}&count=1') as r:
            r = await r.json(content_type=None)
            await session.close()
            return r

async def getPlayer1v1EWRate(self):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=13&profile_id={self.id}&count=1') as r:
            r = await r.json(content_type=None)
            await session.close()
            return r

class Player:
    def __init__(self, id, team, color, name, civ, game, map):
        self.id = id
        self.team = team
        self.color = color
        self.name = name
        self.country = '--'
        self.tg_rating = 0
        self.rating = 0
        self.ew_tg_rating = 0
        self.ew_rating = 0
        self.civ = civ
        self.map = map
        self.game = game

    async def info(self):
        player_tg = await getPlayerURLInfo(self)
        player_1v1 = await getPlayer1v1Info(self)
        player_tg_rate = await getPlayerTGRate(self)
        player_1v1_rate = await getPlayer1v1Rate(self)
        player_tg_ew_rate = await getPlayerTGEWRate(self)
        player_1v1_ew_rate = await getPlayer1v1EWRate(self)

        if len(player_tg["leaderboard"]) > 0:
            playerLeaderboard = player_tg["leaderboard"][0]
            self.country = playerLeaderboard["country"]

        if len(player_1v1["leaderboard"]) > 0:
            playerLeaderboard = player_1v1["leaderboard"][0]
            self.country = playerLeaderboard["country"]

        if len(player_1v1_rate) > 0:
            self.rating = player_1v1_rate[0]['rating']

        if len(player_tg_rate) > 0:
            self.tg_rating = player_tg_rate[0]['rating']

        if len(player_1v1_ew_rate) > 0:
            self.ew_rating = player_1v1_ew_rate[0]['rating']

        if len(player_tg_ew_rate) > 0:
            self.ew_tg_rating = player_tg_ew_rate[0]['rating']

async def getInfo():
    # this function only needs to be called once... all info never changes
    resps = await get_json_info2()
    mapType = resps['map_type']
    civTypes = resps['civ']
    gameTypes = resps['game_type']

    name_by_id = dict([(str(p['id']), p['string']) for p in mapType])
    civ_by_id = dict([(str(p['id']), p['string']) for p in civTypes])
    game_by_id = dict([(str(p['id']), p['string']) for p in gameTypes])
    return name_by_id, civ_by_id, game_by_id

async def getPlayerIDs(resp):
    name_by_id, civ_by_id, game_by_id = await getInfo()

    lastmatch = resp['last_match']
    playerName = resp['name']
    players = []

    for player in lastmatch['players']:
        if player['color'] == 1:
            color = ':blue_circle:'
        elif player['color'] == 2:
            color = ':red_circle:'
        elif player['color'] == 3:
            color = ':green_circle:'
        elif player['color'] == 4:
            color = ':yellow_circle:'
        elif player['color'] == 5:
            color = ':globe_with_meridians:'
        elif player['color'] == 6:
            color = ':purple_circle:'
        elif player['color'] == 7:
            color = ':white_circle:'
        else:
            color = ':orange_circle:'
        mapNum = lastmatch['map_type']
        civNum = player['civ']
        game = lastmatch['game_type']
        players.append(Player(player['profile_id'], player['team'], color, player['name'], civ_by_id[str(civNum)], game_by_id[str(game)], name_by_id[str(mapNum)]))
    return players
