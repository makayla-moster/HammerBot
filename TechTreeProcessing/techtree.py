# Tech Tree
# !/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import json

# import requests
import sys

# Note to self (2023/10/21). This file's job is to
# create the "lookup" table for units/buildings/techs
# for which civs get each of.


# This JSON is found here (maybe 2023/10/21)
# https://github.com/SiegeEngineers/aoe2techtree/blob/master/data/data.json
with open("techtree.json") as fp:
    techtree = json.load(fp)

# This JSON is found here
# https://github.com/SiegeEngineers/halfon/blob/master/data/units_buildings_techs.de.json
with open("directory.json") as fp:
    directory = json.load(fp)

civs = list(techtree["civ_names"].keys())
master_dict = {}

unit_dict = {}
building_dict = {}
tech_dict = {}
unique_dict = {}

for c in civs:
    for x in techtree["techtrees"][c]["units"]:
        name = directory["units_buildings"][str(x)]["localised_name"]
        unit_dict[name] = x

for c in civs:
    for x in techtree["techtrees"][c]["buildings"]:
        name = directory["units_buildings"][str(x)]["localised_name"]
        building_dict[name] = x

for c in civs:
    for x in techtree["techtrees"][c]["techs"]:
        name = directory["techs"][str(x)]["localised_name"]
        tech_dict[name] = x

for c in civs:
    x = techtree["techtrees"][c]["unique"]["castleAgeUniqueUnit"]
    name = directory["units_buildings"][str(x)]["localised_name"]
    master_dict[name] = [c]
    x = techtree["techtrees"][c]["unique"]["imperialAgeUniqueUnit"]
    name = directory["units_buildings"][str(x)]["localised_name"]
    master_dict[name] = [c]
    x = techtree["techtrees"][c]["unique"]["castleAgeUniqueTech"]
    name = directory["techs"][str(x)]["localised_name"]
    master_dict[name] = [c]
    x = techtree["techtrees"][c]["unique"]["imperialAgeUniqueTech"]
    name = directory["techs"][str(x)]["localised_name"]
    master_dict[name] = [c]

for item in unit_dict.keys():
    master_dict[item] = []
for item in building_dict.keys():
    master_dict[item] = []
for item in tech_dict.keys():
    master_dict[item] = []

for key in unit_dict:
    pay = unit_dict[key]
    for c in civs:
        if pay in techtree["techtrees"][c]["units"]:
            master_dict[key].append(c)

for key in building_dict:
    pay = building_dict[key]
    for c in civs:
        if pay in techtree["techtrees"][c]["buildings"]:
            master_dict[key].append(c)

for key in tech_dict:
    pay = tech_dict[key]
    for c in civs:
        if pay in techtree["techtrees"][c]["techs"]:
            master_dict[key].append(c)

print(master_dict)
