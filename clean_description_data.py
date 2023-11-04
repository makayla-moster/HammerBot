# import json
# import re
#
# with open("descriptions.json") as fp:
#     description = json.load(fp)
#
# for item in description:
#     x = description[item].split(" ", 1)
#     if x[0] == "Create" or x[0] == "Build":
#         if "Upgrades" not in x[1]:
#             print(x[1])
#         # x = x[1].split("\n", 1)[1]
#         # x = x.split("<i>", 1)[0]
#         description[item] = x

# for item in description:
#     if int(item) > 26000 and int(item) < 42106:
#         print(description[item])


###########

import json

def remove_keys(text, re_subs):
    import re

    pattern = re.compile("|".join(re_subs))
    return pattern.sub(lambda m: '', text)

with open('descriptions.json','r') as f:
    data = json.load(f)

# Hardcode fix to Elite Berserk
# add <br>\n right before (‹cost›) in key "26576"
data["26576"] = data["26576"].replace("(‹cost›)", "<br>\n(‹cost›)")


filtered = {k: [a.strip() for a in remove_keys(v, {'<[^>]+>', '[(]?‹[^›]+›[)]?'}).split('\n') if len(a.strip())] for k,v in data.items()}

with open('directory.json','r') as f:
    directory = json.load(f)

final_description_directory = {}

for k in filtered:
    # print(type(k), k)
    for unit_building in directory['units_buildings']:
        description_look_up_key = directory['units_buildings'][unit_building]["help_converter"]
        unit_building_name = directory['units_buildings'][unit_building]["localised_name"]
        if description_look_up_key == int(k):
            final_description_directory[unit_building_name] = filtered[k][1]

for k in filtered:
    for tech in directory['techs']:
        description_look_up_key = directory['techs'][tech]["help_converter"]
        tech_name = directory['techs'][tech]["localised_name"]
        if description_look_up_key == int(k):
            final_description_directory[tech_name] = filtered[k][1]


with open('descriptions_cleaned.json', 'w') as json_file:
    json.dump(final_description_directory, json_file)
