from json import load, dump
from pathlib import Path


keyboard = load(Path("./info.json").open())
lys = keyboard["layouts"]
for ly in lys.values():
    for key in ly["layout"]:
        key["col"] = key["matrix"][0]
        key["row"] = key["matrix"][1]


dump(keyboard, Path("./piantor.json").open("w"))
