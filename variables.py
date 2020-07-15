# coding: utf-8

#player
player_name =""

# game
game_in_progress = True


# avatar
avatar_position = [57, 20]      # X , Y  à mettre aléatoirement !!!!  et sous format dico ?????

letter_avatar_symbol = ""

avatar_symbol = {                                                ################### rajouter le choix de la couleur ???
    "L" : {
        "name" : "Lady",
        "symbol" : "♀",
        "message" : "Quelle bonne idée d'avoir choisi ce symbole \u001b[38;5;201m♀\u001b[0m !\n Tu as débloqué le 'Ladies Mode' !",
        "color_start" : "\u001b[38;5;201m",
        "color_end" : "\u001b[0m"
    },
    "K" : {
        "name" : "Knight",
        "symbol" : "♂",
        "message" : "Voici le symbole de ton avatar : \u001b[38;5;33m♂\u001b[0m !",
        "color_start" : "\u001b[38;5;33m",
        "color_end" : "\u001b[0m"
    },
    "N" : {
        "name" : "No One",
        "symbol" : "☻",
        "message" : "Voici le symbole de ton avatar : \u001b[38;5;10m☻\u001b[0m !",
        "color_start" : "\u001b[38;5;10m",
        "color_end" : "\u001b[0m"
    }
}

avatar_symbol_current = ""

possibles_avatar_symbol =  ", ".join(avatar_symbol.keys())


# 4 places : 3 challenges and 1 gate

place = {
    "1" : {
        "name" : "Mysterious number",
        "col_x" : 73,
        "ln_y" : 8,
        "print" : "1",
        "image" : "1",
        "can_walk" : True,
        "color_start" : "\u001b[38;5;208m",
        "color_end" : "\u001b[0m"
        },
    "2" : {
        "name" : "Caesar Code",
        "col_x" : 45,
        "ln_y" : 23,
        "print" : "2",
        "image" : "2",
        "can_walk" : True,
        "color_start" : "\u001b[38;5;208m",
        "color_end" : "\u001b[0m"
            },
    "3" : {
        "name" : "Multi FizzBuzz",
        "col_x" : 21,
        "ln_y" : 21,
        "print" : "3",
        "image" : "3",
        "can_walk" : True,
        "color_start" : "\u001b[38;5;208m",
        "color_end" : "\u001b[0m"
            },
    "4" : {
        "name" : "Mysterious Gate",
        "col_x" : 31,
        "ln_y" : 5,
        "print" : "4",
        "image" : "∩",
        "can_walk" : True,
        "color_start" : "\u001b[48;5;223m",
        "color_end" : "\u001b[0m"
            }
}

key_place_1 = ""
key_place_2 = ""
key_place_3 = ""
key_gate = ""

list_place_symbol = []
text_place_symbol = ""

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
    "T" : {
        "name" : "Télécharger",
        # "character" : "T",
        "message" : "\nPartie téléchargée.\n",
        "game_in_progress" : True
    },
    "S" : {
        "name" : "Sauvegarder",
        # "character" : "S",
        "message" : "\nPartie sauvegardée.\n",
        "game_in_progress" : True
    },
    "H" : {
        "name" : "Haut",
        # "character" : "H",
        "message" : "\nL'avatar s'est déplacé vers le haut.",
        "game_in_progress" : True
    },
    "B" : {
        "name" : "Bas",
        # "character" : "S",
        "message" : "\nL'avatar s'est déplacé vers le bas.\n",
        "game_in_progress" : True
    },
    "D" : {
        "name" : "Droite",
        # "character" : "D",
        "message" : "\nL'avatar s'est déplacé vers la droite.\n",
        "game_in_progress" : True
    },
    "G" : {
        "name" : "Gauche",
        # "character" : "G",
        "message" : "\nL'avatar s'est déplacé vers la gauche.\n",
        "game_in_progress" : True
    },
    "P" : {
        "name" : "Prendre",
        # "character" : "P",
        "message" : "\nL'avatar a pris l'objet.\n",
        "game_in_progress" : True
    },
    "U" : {
        "name" : "Utiliser",
        # "character" : "U",
        "message" : "\nL'avatar a utilisé l'objet.\n",
        "game_in_progress" : True
    },
    "A" : {
        "name" : "Abandonner",
        # "character" : "A",
        "message" : "\nL'avatar a abandonné l'objet parterre.\n",
        "game_in_progress" : True
    },
    "Y" : {
        "name" : "s'hYdrater",
        # "character" : "Y",
        "message" : "\nL'avatar s'est hydraté.\n",
        "game_in_progress" : True
    },
    "M" : {
        "name" : "Manger",
        # "character" : "M",
        "message" : "\nL'avatar a mangé.\n",
        "game_in_progress" : True
    },
    "R" : {
        "name" : "se Reposer",
        # "character" : "R",
        "message" : "\nL'avatar s'est reposé.\n",
        "game_in_progress" : True
    }
    # "E" : {
    #     "name" : "Erreur de lettre",
    #     # "character" : "E",
    #     "message" : "\nOups !\nJe ne comprends pas ce que tu veux faire.\n",
    #     "game_in_progress" : True 
    # },
}

possibles_actions =  ", ".join(actions.keys())


# challenge

    # challenge 1 :: mysterious number
player_number = ""
sphinx_number = ""

original_message = "BEAUTIFUL IS BETTER THAN UGLY. EXPLICIT IS BETTER THAN IMPLICIT. SIMPLE IS BETTER THAN COMPLEX."
coded_message = ""


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
    "J" : {
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
        }
}

if __name__ == "__main__" :
    get_list_place_symbol()

