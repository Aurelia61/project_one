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
    ">" : {
        "name" : "montain",
        "image" : "\u001b[38;5;58m▲\u001b[0m",
        "can_walk" : False
        },
    # "<" : {
    #     "name" : "montain",
    #     "image" : "▲",
    #     "can_walk" : False
        # },
    "µ" : {
        "name" : "river",
        "image" : "≡",
        "can_walk" : False
        },
    "u" : {
        "name" : "river",
        "image" : "\u001b[38;5;6m≡\u001b[0m",
        "can_walk" : False
        },
    "i" : {
        "name" : "river",
        "image" : "\u001b[38;5;57mµ\u001b[0m",
        "can_walk" : False
        },
    "~" : {
        "name" : "sea",
        "image" : "~",
        "can_walk" : False
        },
    "s" : {
        "name" : "sea",
        "image" : "\u001b[38;5;39m≈\u001b[0m",
        "can_walk" : False
        },
    "t" : {
        "name" : "jungle",
        "image" : "♣",
        "can_walk" : False
        },
    "J" : {
        "name" : "jungle",
        "image" : "\u001b[38;5;76m♣\u001b[0m",
        "can_walk" : False
        },
    ":" : {
        "name" : "steppe",
        "image" : "∞",
        "can_walk" : False
        },
    "v" : {
        "name" : "steppe",
        "image" : "\u001b[38;5;76m∞\u001b[0m",
        "can_walk" : False
        },
    "°" : {
        "name" : "sand",
        "image" : ":",
        "can_walk" : False
        },
    "." : {
        "name" : "sand",
        "image" : "\u001b[38;5;223m:\u001b[0m",
        "can_walk" : False
        },
    "¤" : {
        "name" : "mysterious gate",
        "image" : "\u001b[48;5;164m¤\u001b[0m",
        "can_walk" : True
        },
    "*" : {
        "name" : "challenge",
        "image" : "\u001b[48;5;208m*\u001b[0m",
        "can_walk" : True
        },
    }
