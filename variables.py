# coding: utf-8

#player
player_name =""

# game
game_in_progress = True


# avatar
avatar_position = [19, 56]      # X , Y

letter_avatar_symbol = ""

avatar_symbol = {                                                ################### rajouter le choix de la couleur ???
    "F" : {
        "name" : "Fille",
        "symbol" : "♀",
        "message" : "Quelle bonne idée d'avoir choisi ce symbole \u001b[38;5;201m♀\u001b[0m !\n Tu as débloqué le 'Ladies Mode' !",
        "color_start" : "\u001b[38;5;201m",
        "color_end" : "\u001b[0m"
    },
    "G" : {
        "name" : "Garçon",
        "symbol" : "♂",
        "message" : "Voici le symbole de ton avatar : \u001b[38;5;33m♂\u001b[0m !",
        "color_start" : "\u001b[38;5;33m",
        "color_end" : "\u001b[0m"
    },
    "N" : {
        "name" : "Neutre",
        "symbol" : "☻",
        "message" : "Voici le symbole de ton avatar : \u001b[38;5;10m☻\u001b[0m !",
        "color_start" : "\u001b[38;5;10m",
        "color_end" : "\u001b[0m"
    }
}

avatar_symbol_current = ""

possibles_avatar_symbol =  ", ".join(avatar_symbol.keys())


# map
map1 = []
map_elements = {
    " " : {
        "name" : "terre",
        "image" : " ",
        "can_walk" : True,
        "color_start" : "\u001b[38;5;15m",
        "color_end" : "\u001b[0m"
        },
    "^" : {
        "name" : "montain",
        "image" : "▲",
        "can_walk" : False,
        "color_start" : "\u001b[38;5;136m",
        "color_end" : "\u001b[0m"
        },
    "u" : {
        "name" : "river",
        "image" : "≈",
        "can_walk" : False,
        "color_start" : "\u001b[38;5;21m",
        "color_end" : "\u001b[0m"
        },
    "s" : {
        "name" : "sea",
        "image" : "▓",
        "can_walk" : False,
        "color_start" : "\u001b[38;5;117m",
        "color_end" : "\u001b[0m"
        },
    "T" : {
        "name" : "jungle",
        "image" : "♣",
        "can_walk" : False,
        "color_start" : "\u001b[38;5;65m",
        "color_end" : "\u001b[0m"
        },
    "v" : {
        "name" : "steppe",
        "image" : "∞",
        "can_walk" : False,
        "color_start" : "\u001b[38;5;34m",
        "color_end" : "\u001b[0m"
        },
    ":" : {
        "name" : "sand",
        "image" : "▒",
        "can_walk" : False,
        "color_start" : "\u001b[38;5;226m",
        "color_end" : "\u001b[0m"
        },
    "G" : {
        "name" : "mysterious gate",
        "image" : "∩",
        "can_walk" : True,
        "color_start" : "\u001b[48;5;223m",
        "color_end" : "\u001b[0m"
        },
    "*" : {
        "name" : "challenge",
        "image" : "*",
        "can_walk" : True,
        "color_start" : "\u001b[38;5;208m",
        "color_end" : "\u001b[0m"
        },
    }


# actions

chosen_action = ""

actions = {
    "C" : {
        "name" : "Continuer",
        # "character" : "C",
        "message" : "\nBonne décision ! \n",
        "game_in_progress" : True 
    },
    "Q" : {
        "name" : "Quitter",
        # "character" : "Q",
        "message" : "\nC'est dommage...\n",
        "game_in_progress" : False 
    },
    # "E" : {
    #     "name" : "Erreur de lettre",
    #     # "character" : "E",
    #     "message" : "\nOups !\nJe ne comprends pas ce que tu veux faire.\n",
    #     "game_in_progress" : True 
    # },
}

possibles_actions =  ", ".join(actions.keys())



# symbol challenge

# symbols : {
#     { }
# }


