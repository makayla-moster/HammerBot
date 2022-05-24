import json
import pickle
from unit_building_class import unit_building

# json obtained from
# https://github.com/SiegeEngineers/halfon/blob/master/data/units_buildings_techs.de.json
with open("directory.json") as fp:
    directory = json.load(fp)



x = "4"

obj = unit_building(directory["units_buildings"][x])

# print(obj.get_cost())
#
# print(obj)

unit_building_dict = {}

for item in directory["units_buildings"]:
    unit_building_obj = unit_building(directory["units_buildings"][item])
    unit_building_dict[unit_building_obj.get_name()] = unit_building_obj


# save obj to file
a_file = open("unit_build_stats.pkl", "wb")
pickle.dump(unit_building_dict, a_file)
a_file.close()
