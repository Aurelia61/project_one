# coding: utf-8

# avatar
avatar_position = {"X" : 19, "Y" : 56}
avatar_symbol = "\u001b[38;5;196m☻\u001b[0m"    ################### mettre la couleur ???
# map

map1 = []

map_elements = {
    " " : {
        "name" : "terre",
        "image" : " ",
        "can_walk" : True
        },
    "^" : {
        "name" : "montain",
        "image" : "^",
        "can_walk" : False
        },
    "µ" : {
        "name" : "river",
        "image" : "µ",
        "can_walk" : False
        },
    "~" : {
        "name" : "sea",
        "image" : "~",
        "can_walk" : False
        },
    "&" : {
        "name" : "jungle",
        "image" : "&",
        "can_walk" : False
        },
    "§" : {
        "name" : "steppe",
        "image" : "§",
        "can_walk" : False
        },
    "°" : {
        "name" : "sand",
        "image" : "°",
        "can_walk" : False
        },
    "¤" : {
        "name" : "mysterious gate",
        "image" : "\u001b[38;5;164m¤\u001b[0m",
        "can_walk" : True
        },
    "*" : {
        "name" : "challenge",
        "image" : "\u001b[38;5;208m*\u001b[0m",
        "can_walk" : True
        },
    }
