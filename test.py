import variables

variables.backpack["g"] = (variables.game_keys["g"])
variables.backpack["s"] = (variables.game_keys["s"])
# variables.backpack["b"] = (variables.game_keys["b"])

if "g" in variables.backpack.keys() and "s" in variables.backpack.keys() and "b" in variables.backpack.keys() :
    print("ok")
else:
    print("no")