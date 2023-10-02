import pickle
from collections import Counter

try:
    with open("serverResources", "rb") as f:
        serverResources = pickle.load(f)
except FileNotFoundError:
    serverResources = {
        "quela": {"Food": "-1068", "Wood": "449", "Gold": "-826", "Stone": "12"},
        "bshammer": {"Food": "-1250", "Wood": "-1173", "Gold": "-850", "Stone": "1942"},
        "probablybutter": {"Food": "295", "Wood": "-2024", "Gold": "-1006", "Stone": "-2044"},
        "olaf_the_shrew": {"Food": "323", "Wood": "0", "Gold": "0", "Stone": "0"},
        ".harristotle": {"Food": "-2241", "Wood": "560", "Gold": "-986", "Stone": "-706"},
    }

try:
    with open("gizmoResources", "rb") as f:
        gizmoResources = pickle.load(f)
except FileNotFoundError:
    gizmoResources = Counter()

try:
    with open("taoResources", "rb") as f:
        taoResources = pickle.load(f)
except FileNotFoundError:
    taoResources = Counter()
