import json
import pickle

from unit_building_class import unit_building

# json obtained from
# https://github.com/SiegeEngineers/halfon/blob/master/data/units_buildings_techs.de.json
with open("directory.json") as fp:
    directory = json.load(fp)

unit_building_dict = {}

for item in directory["units_buildings"]:
    unit_building_obj = unit_building(directory["units_buildings"][item])
    unit_building_dict[unit_building_obj.get_name()] = unit_building_obj

json_dict = {}

for key, value in unit_building_dict.items():
    json_dict[value.get_name()] = {"cost": value.get_cost(),
    "attack" : value.get_attack(),
    "melee_armor": value.get_melee_armor(),
    "pierce_armor": value.get_pierce_armor(),
    "hit_points": value.get_hit_points(),
    "los": value.get_los()}

# Serializing json
json_object = json.dumps(json_dict, indent = 4)

# Writing to sample.json
with open("unit_building.json", "w") as outfile:
    outfile.write(json_object)




# # save obj to file
# a_file = open("unit_build_stats.pkl", "wb")
# pickle.dump(unit_building_dict, a_file)
# a_file.close()
