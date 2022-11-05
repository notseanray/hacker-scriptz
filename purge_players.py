import json
import os

WORLD_FILE = "HypnosSurvival"

wlist = open("whitelist.json")
jsonwlist = json.load(wlist)
uuids = []
for player in jsonwlist:
    uuids.append(player["uuid"])
for dir in os.listdir("./" + WORLD_FILE + "/playerdata/"):
    if "tmp" in dir:
        os.remove("./" + WORLD_FILE + "/playerdata/" + dir)
    if dir[:36] in uuids:
        continue
    os.remove("./" + WORLD_FILE + "/playerdata/" + dir)

