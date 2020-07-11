# coding: utf-8

# avatar
avatar_position = {"X" : 19, "Y" : 56}
avatar_symbol = "\033[37m☻"
# map

map = []

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
        "image" : "§",
        "can_walk" : False
        },
    "¤" : {
        "name" : "mysterious gate",
        "image" : "¤",
        "can_walk" : True
        },
    "*" : {
        "name" : "challenge",
        "image" : "*",
        "can_walk" : True
        },
    }
