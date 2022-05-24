import pickle
# from unit_building_class import unit_building
# read obj from file
a_file = open("unit_build_stats.pkl", "rb")
obj = pickle.load(a_file)

print(obj["Archer"].get_cost())
