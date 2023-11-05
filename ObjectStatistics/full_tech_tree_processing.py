import json

with open("full_tech_tree.json") as fp:
    techtree = json.load(fp)

with open("directory.json") as fp:
    directory = json.load(fp)


EntityId = int


def create_localised_name_lookup(category_key: str) -> dict[EntityId, str]:
    localised_name_lookup = {}

    for key, value in directory[category_key].items():
        localised_name_lookup[value["localised_name"]] = key

    return localised_name_lookup


localised_unit_building_name_lookup = create_localised_name_lookup("units_buildings")

print(localised_unit_building_name_lookup)

# Hardcode a fix for Huskarl because it appears again at "759",
# but "759" does not exist in the other json
localised_unit_building_name_lookup["Huskarl"] = "41"
localised_unit_building_name_lookup["Elite Huskarl"] = "555"

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
    11: '<abbr title="(except Port)">All Buildings</abbr>',
    12: "Unused",
    13: "Stone Defense",
    14: "FE Predator Animals",
    15: "Archers",
    16: "Ships & Camels & Saboteurs",
    17: "Rams",
    18: "Trees",
    19: '<abbr title="(except Turtle Ship)">Unique Units</abbr>',
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
}


def get_cost(unit):
    return techtree["data"]["units"][localised_unit_building_name_lookup[unit]]["Cost"]


def get_attacks(unit):
    attackDict = {}
    attacks = techtree["data"]["units"][localised_unit_building_name_lookup[unit]]["Attacks"]
    for attackItem in attacks:
        attackDict[unitClasses[attackItem["Class"]]] = attackItem["Amount"]
    return attackDict


def get_armours(unit):
    armourDict = {}
    armours = techtree["data"]["units"][localised_unit_building_name_lookup[unit]]["Armours"]
    for attackItem in armours:
        armourDict[unitClasses[attackItem["Class"]]] = attackItem["Amount"]
    return armourDict


def get_range(unit):
    rangeDict = {}
    minRange = techtree["data"]["units"][localised_unit_building_name_lookup[unit]]["MinRange"]
    range = techtree["data"]["units"][localised_unit_building_name_lookup[unit]]["Range"]
    rangeDict["Minimum Range"] = minRange
    rangeDict["Range"] = range
    return rangeDict


def get_trainTime(unit):
    return techtree["data"]["units"][localised_unit_building_name_lookup[unit]]["TrainTime"]


def get_HP(unit):
    return techtree["data"]["units"][localised_unit_building_name_lookup[unit]]["HP"]


def get_accuracy(unit):
    return techtree["data"]["units"][localised_unit_building_name_lookup[unit]]["AccuracyPercent"]


def get_attackDelay(unit):
    return techtree["data"]["units"][localised_unit_building_name_lookup[unit]]["AttackDelaySeconds"]


def get_frameDelay(unit):
    return techtree["data"]["units"][localised_unit_building_name_lookup[unit]]["FrameDelay"]


def get_garrisonCapacity(unit):
    return techtree["data"]["units"][localised_unit_building_name_lookup[unit]]["GarrisonCapacity"]


def get_LineOfSight(unit):
    return techtree["data"]["units"][localised_unit_building_name_lookup[unit]]["LineOfSight"]


def get_reloadTime(unit):
    return techtree["data"]["units"][localised_unit_building_name_lookup[unit]]["ReloadTime"]


def get_speed(unit):
    return techtree["data"]["units"][localised_unit_building_name_lookup[unit]]["Speed"]


# print(techtree["data"]["units"][localised_unit_building_name_lookup["Elite Huskarl"]])
