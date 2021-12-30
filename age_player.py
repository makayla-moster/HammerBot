import csv
import requests
import sys

# while True:
url = f"https://aoe2.net/api/player/lastmatch?game=aoe2de&profile_id=313591" #313591 5001328
resp = requests.get(url).json()
lastmatch = resp['last_match']
playerName = resp['name']

url2 = f"https://aoe2.net/api/strings?game=aoe2de&language=en"
resps = requests.get(url2).json()
mapType = resps['map_type']
civTypes = resps['civ']

name_by_id = dict([(str(p['id']), p['string']) for p in mapType])
civ_by_id = dict([(str(p['id']), p['string']) for p in civTypes])

# print(playerName)
players = []
team1 = []
team2 = []
hammerTeam1 = False
hammerTeam2 = False

class Player:
    def __init__(self, id, team, color, name, civ, map):
        self.id = id
        self.team = team
        self.color = color
        self.name = name
        self.country = '--'
        self.tg_rating = 0
        self.rating = 0
        self.civ = civ
        self.map = map

    def info(self):
        player_url = f"https://aoe2.net/api/leaderboard?game=aoe2de&profile_id={self.id}&leaderboard_id=4"
        player_url_1v1 = f"https://aoe2.net/api/leaderboard?game=aoe2de&profile_id={self.id}&leaderboard_id=3"
        player_tg = requests.get(player_url).json()
        player_1v1 = requests.get(player_url_1v1).json()
        player_tg_rating_url = f"https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=4&profile_id={self.id}&count=1"
        player_tg_rate = requests.get(player_tg_rating_url).json()
        player_1v1_rating_url =f"https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=3&profile_id={self.id}&count=1"
        player_1v1_rate = requests.get(player_1v1_rating_url).json()

        if len(player_tg["leaderboard"]) > 0:
            playerLeaderboard = player_tg["leaderboard"][0]
            # self.name = playerLeaderboard["name"]
            self.country = playerLeaderboard["country"]
        if len(player_1v1["leaderboard"]) > 0:
            playerLeaderboard = player_1v1["leaderboard"][0]
            # self.name = playerLeaderboard["name"]
            self.country = playerLeaderboard["country"]
        if len(player_1v1_rate) > 0:
            self.rating = player_1v1_rate[0]['rating']
        if len(player_tg_rate) > 0:
            self.tg_rating = player_tg_rate[0]['rating']

    @property
    def print_info(self):
        return ("Name: " + str(self.name) + "\n\tCountry: " + str(self.country) + "\tTG ELO:" + str(self.tg_rating) + "\tELO: " + str(self.rating) + '\tTEAM: ' + str(self.team) + '\n')


def getPlayerIDs():
    players = []
    for player in lastmatch['players']:
        # profileIDs.append(player['profile_id'])
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
        players.append(Player(player['profile_id'], player['team'], color, player['name'], civ_by_id[str(civNum)], name_by_id[str(mapNum)]))
    return players
