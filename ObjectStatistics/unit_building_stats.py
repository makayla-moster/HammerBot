
import json


# json obtained from
# https://github.com/SiegeEngineers/halfon/blob/master/data/units_buildings_techs.de.json
with open("directory.json") as fp:
    directory = json.load(fp)


class unit_building:
    def __init__(self, info):
        self._info = info

        self.set_cost(self._info['cost'])
        self.set_stats(self._info)
        self.set_name(self._info)

    def set_name(self, info):
        self._name = info['localised_name']

    def get_name(self):
        return self._name

    def __str__(self):
        return self._name

    def set_cost(self, cost):
        self._food_cost = cost['food']
        self._wood_cost = cost['wood']
        self._gold_cost = cost['gold']
        self._stone_cost = cost['stone']

    def get_cost(self):
        return (self._food_cost, self._wood_cost, self._gold_cost, self._stone_cost, )

    def set_stats(self, info):
        self._attack = info['attack']
        self._melee_armor = info['melee_armor']
        self._pierce_armor = info['pierce_armor']
        self._hit_points = info['hit_points']
        self._los = info['line_of_sight']

    def get_attack(self):
        return self._attack

    def get_melee_armor(self):
        return self._melee_armor

    def get_pierce_armor(self):
        return self._pierce_armor

    def get_hit_points(self):
        return self._hit_points

    def get_los(self):
        return self._los

x = "4"

obj = unit_building(directory["units_buildings"][x])

print(obj.get_cost())

print(obj)

unit_building_dict = {}

for item in directory["units_buildings"]:
    unit_building_obj = unit_building(directory["units_buildings"][item])
    unit_building_dict[unit_building_obj.get_name()] = unit_building_obj


print(unit_building_dict["Man-at-Arms"].get_cost())
