import json

# TODO: Make these JSONS connected directly to the source. 2023/10/21

# This JSON is found here (maybe 2023/10/21)
# https://github.com/SiegeEngineers/aoe2techtree/blob/master/data/data.json
with open("full_tech_tree.json") as fp:
    techtree = json.load(fp)

# This JSON is found here
# https://github.com/SiegeEngineers/halfon/blob/master/data/units_buildings_techs.de.json
with open("directory.json") as fp:
    directory = json.load(fp)


EntityId = int


def create_localised_name_lookup(category_key):
    localised_name_lookup = {}

    for key, value in directory[category_key].items():
        if value["localised_name"] in localised_name_lookup:
            localised_name_lookup[value["localised_name"]] = str(
                min(int(key), int(localised_name_lookup[value["localised_name"]]))
            )
        else:
            localised_name_lookup[value["localised_name"]] = key

    return localised_name_lookup


localised_unit_building_name_lookup = create_localised_name_lookup("units_buildings")

# for item in localised_unit_building_name_lookup:
#     print(item, localised_unit_building_name_lookup[item])


localised_tech_name_lookup = create_localised_name_lookup("techs")


# Hardcode a fix for Huskarl because it appears again at "759",
# but "759" does not exist in the other json
localised_unit_building_name_lookup["Huskarl"] = "41"
localised_unit_building_name_lookup["Elite Huskarl"] = "555"
localised_unit_building_name_lookup["Stable"] = "101"
localised_unit_building_name_lookup["Archery Range"] = "87"
localised_unit_building_name_lookup["Blacksmith"] = "103"
localised_unit_building_name_lookup["Monastery"] = "104"
localised_unit_building_name_lookup["Condottiero"] = "882"
localised_unit_building_name_lookup["Villager"] = "83"


# This list comes from this java script file.
# https://github.com/SiegeEngineers/aoe2techtree/blob/master/js/techtree.js
unitClasses = {
    0: "Unused",
    1: "Infantry",
    2: "Turtle Ships",
    3: "Base Pierce",
    4: "Base Melee",
    5: "War Elephants",
    6: "Unused",
    7: "Unused",
    8: "Cavalry",
    9: "Unused",
    10: "Unused",
    11: "All Buildings",
    12: "Unused",
    13: "Stone Defense",
    14: "FE Predator Animals",
    15: "Archers",
    16: "Ships & Camels & Saboteurs",
    17: "Rams",
    18: "Trees",
    19: "Unique Units",
    20: "Siege Weapons",
    21: "Standard Buildings",
    22: "Walls & Gates",
    23: "FE Gunpowder Units",
    24: "Boars",
    25: "Monks",
    26: "Castle",
    27: "Spearmen",
    28: "Cavalry Archers",
    29: "Eagle Warriors",
    30: "HD Camels",
    31: "Anti-Leitis",
    32: "Condottieros",
    33: "Organ Gun Damage",
    34: "Fishing Ships",
    35: "Mamelukes",
    36: "Heroes and Kings",
    37: "Hussite Wagons",
    38: "Skirmishers",
    39: "Cavalry Resistance",
}


def get_cost(unit, type):
    if type == "techs":
        return techtree["data"][type][localised_tech_name_lookup[unit]]["Cost"]
    else:
        return techtree["data"][type][localised_unit_building_name_lookup[unit]]["Cost"]


def get_attacks(unit, type):
    attackDict = {}
    attacks = techtree["data"][type][localised_unit_building_name_lookup[unit]]["Attacks"]
    for attackItem in attacks:
        attackDict[unitClasses[attackItem["Class"]]] = attackItem["Amount"]
    return attackDict


def get_armours(unit, type):
    armourDict = {}
    armours = techtree["data"][type][localised_unit_building_name_lookup[unit]]["Armours"]
    for attackItem in armours:
        armourDict[unitClasses[attackItem["Class"]]] = attackItem["Amount"]
    return armourDict


def get_range(unit, type):
    rangeDict = {}
    minRange = techtree["data"][type][localised_unit_building_name_lookup[unit]]["MinRange"]
    range = techtree["data"][type][localised_unit_building_name_lookup[unit]]["Range"]
    rangeDict["Minimum Range"] = minRange
    rangeDict["Range"] = range
    return rangeDict


def get_trainTime(unit, type):
    return techtree["data"][type][localised_unit_building_name_lookup[unit]]["TrainTime"]


def get_HP(unit, type):
    return techtree["data"][type][localised_unit_building_name_lookup[unit]]["HP"]


def get_accuracy(unit, type):
    return techtree["data"][type][localised_unit_building_name_lookup[unit]]["AccuracyPercent"]


def get_attackDelay(unit, type):
    return techtree["data"][type][localised_unit_building_name_lookup[unit]]["AttackDelaySeconds"]


def get_frameDelay(unit, type):
    return techtree["data"][type][localised_unit_building_name_lookup[unit]]["FrameDelay"]


def get_garrisonCapacity(unit, type):
    return techtree["data"][type][localised_unit_building_name_lookup[unit]]["GarrisonCapacity"]


def get_LineOfSight(unit, type):
    return techtree["data"][type][localised_unit_building_name_lookup[unit]]["LineOfSight"]


def get_reloadTime(unit, type):
    return techtree["data"][type][localised_unit_building_name_lookup[unit]]["ReloadTime"]


def get_speed(unit, type):
    if type == "units":
        return techtree["data"][type][localised_unit_building_name_lookup[unit]]["Speed"]
    else:
        return 0


def get_upgrade_cost(unitNum):
    return techtree["data"]["unit_upgrades"][unitNum]["Cost"]


def get_upgrade_researchTime(unitNum):
    return techtree["data"]["unit_upgrades"][unitNum]["ResearchTime"]


def get_tech_researchTime(techNum):
    return techtree["data"]["techs"][techNum]["ResearchTime"]
