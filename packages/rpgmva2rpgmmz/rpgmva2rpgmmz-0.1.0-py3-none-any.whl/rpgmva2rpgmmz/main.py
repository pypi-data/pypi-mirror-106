from rubymarshal.reader import load

try:
    from rpgmva2rpgmmz.classes import tileset
except:
    from classes import tileset
    
import json
import argparse
import sys


def main():

    parser = argparse.ArgumentParser(description="Convert and extract tilesets from RPG Maker VX/Ace to RPG Maker MZ")
    parser.add_argument("rvdata", help="Tilesets.rvdata2 from RPG Maker VX/Ace")
    parser.add_argument("-t", "--tileset", type=int, help="Tileset index you want to get")
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument("-o", "--output", type=str, help="File where the JSON will be printed")
    output_group.add_argument("-a", "--append", type=str, help="Append the tileset to a tilesets.json file")

    commands = parser.parse_args()

    jsonObj = []

    content = ""
    with open(commands.rvdata, "rb") as fd:
        content = load(fd)

    if commands.tileset != None:
        if commands.tileset > len(content) or commands.tileset <= 0:
            print("Error : Tileset index out of range")
            return

        jsonObj.append(None)
        jsonObj.append(content[commands.tileset].tojson())

    else:
        for i in content:
            if i is not None:
                jsonObj.append(i.tojson())
            else:
                jsonObj.append(i)


    if commands.output:
        with open(commands.output, "w") as fd:
            json.dump(jsonObj, fd)
    
    if commands.append:
        jsonIn = {}

        with open(commands.append, "r") as fd:
            jsonIn = json.load(fd)

        maxId = maxId = max(node["id"] for node in jsonIn[1:])
        maxId += 1

        for tileset in jsonObj[1:]:
            tileset["id"] = maxId
            maxId += 1

        for tileset in jsonObj[1:]:
            jsonIn.append(tileset)

        with open(commands.append, "w") as fd:
            json.dump(jsonIn, fd)

    if commands.output is None and commands.append is None:
        print(json.dumps(jsonObj))

    return

if __name__ == "__main__":
    main()