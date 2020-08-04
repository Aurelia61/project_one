# coding: utf-8

#import modules
import random
import string   # for choosing randomly a letter


#player
player_name = ""


# game
game_in_progress = True
message_speed = 1

# avatar
avatar_position = { "x" : 57, "y" : 20}      # X , Y  à mettre aléatoirement !!!!

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

avatar_previous_position = {"x" : None, "y" : None }
symbol_under_avatar = ""

avatar_speed = 0.3

# all the counters are here

counters = {
    "number_movements" : {
        "name" : "Compteur de déplacement",
        "value" : 0,
        "color_start" : "\u001b[38;5;99m",
        "color_end" : "\u001b[0m"
    },
    "number_actions" : {
        "name" : "Compteur d'actions",
        "value" : 0,
        "color_start" : "\u001b[38;5;99m",
        "color_end" : "\u001b[0m"
    },
    "life" : {
        "name" : "Points de vie",
        "symbol_full" : "♥",
        "symbol_empty" : ".",
        "color_start_danger" : "\u001b[38;5;196m",
        "color_start_ok" : "\u001b[38;5;196m",
        "color_end" : "\u001b[0m",
        "value_max" : 100,
        "value" : 100,
        "dormir" : 6,
        "movement" : 3
    },
    "hydration" : {
        "name" : "Points d'hydratation",
        "symbol_full" : "☼",
        "symbol_empty" : ".",
        "value_max" : 100,
        "value" : 100,
        "dormir" : 2,
        "movement" : 2
    },
    "satiety" : {
        "name" : "Points de satiété",
        "symbol_full" : "♦",
        "symbol_empty" : ".",
        "value_max" : 100,
        "value" : 100,
        "dormir" : 1,
        "movement" : 2
    }
}


# items
    ## what is in the backpack
backpack = {
    "knife" : {
        "name" : "Couteau"
    },
    "bottle" : {
        "name" : "Bouteille d'eau"
    },
    "computer" : {
        "name" : "Ordinateur portable"
    },
}

    ## items that the player could find
items_available = {
    "coconut" : {
        "name" : "Noix de coco",
        "symbol_items" : "?",
        "number" : 10,
        "col_x" : 0,
        "ln_y" : 0,
        "value_hydration" : 15,
        "value_satiety" : 25
    },
    "spring_water" : {
        "name" : "Eau de source",
        "symbol_items" : "?",
        "number" : 3,
        "col_x" : 0,
        "ln_y" : 0,
        "value_hydration" : 100,
        "value_satiety" : 5
    },
    "worm" : {
        "name" : "Vers de terre",
        "symbol_items" : "?",
        "number" : 20,
        "col_x" : 0,
        "ln_y" : 0,
        "value_hydration" : 2,
        "value_satiety" : 10
    },
    "fresh_water" : {
        "name" : "Eau douce ",
        "symbol_items" : "?",
        "number" : 5,
        "col_x" : 0,
        "ln_y" : 0,
        "value_hydration" : 100,
        "value_satiety" : 2
    },
    "sea_water" : {
        "name" : "Eau de mer",
        "symbol_items" : "?",
        "number" : 3,
        "col_x" : 0,
        "ln_y" : 0,
        "value_hydration" : 20,
        "value_satiety" : 3
    },
    "banana" : {
        "name" : "banane",
        "symbol_items" : "?",
        "number" : 25,
        "col_x" : 0,
        "ln_y" : 0,
        "value_hydration" : 2,
        "value_satiety" : 50
    },
    "red_berry" : {
        "name" : "Baie rouge",
        "symbol_items" : "?",
        "number" : 3,
        "col_x" : 0,
        "ln_y" : 0,
        "value_hydration" : 0,
        "value_satiety" : 0,
        "blind" : True
    },
    "berry" : {
        "name" : "Petits fruits",
        "symbol_items" : "?",
        "number" : 10,
        "col_x" : 0,
        "ln_y" : 0,
        "value_hydration" : 2,
        "value_satiety" : 10
    }
}


# actions

chosen_action = ""

actions = {
    "C" : {
        "name" : "Continuer",
        # "character" : "C",
        "message" : "\nBonne décision ! \n",
        "game_in_progress" : True,
        "movement" : False,
        "impossible" : "\nImpossible de continuer la partie."
    },
    "Q" : {
        "name" : "Quitter",
        # "character" : "Q",
        "message" : "\nC'est dommage...\n",
        "game_in_progress" : False,
        "movement" : False,
        "impossible" : "\nImpossible de quitter la partie."
    },
    "T" : {
        "name" : "Télécharger",
        # "character" : "T",
        "message" : "\nPartie téléchargée.\n",
        "game_in_progress" : True,
        "movement" : False,
        "impossible" : "\nImpossible de télécharger la partie."
    },
    "S" : {
        "name" : "Sauvegarder",
        # "character" : "S",
        "message" : "\nPartie sauvegardée.\n",
        "game_in_progress" : True,
        "movement" : False,
        "impossible" : "\nImpossible de sauvegarder la partie."
    },
    "H" : {
        "name" : "Haut",
        # "character" : "H",
        "message" : "\nL'avatar s'est déplacé vers le haut.",
        "game_in_progress" : True,
        "movement" : True,
        "impossible" : "\nImpossible d'aller plus haut."
    },
    "B" : {
        "name" : "Bas",
        # "character" : "S",
        "message" : "\nL'avatar s'est déplacé vers le bas.\n",
        "game_in_progress" : True,
        "movement" : True,
        "impossible" : "\nImpossible d'aller plus bas."
    },
    "D" : {
        "name" : "Droite",
        # "character" : "D",
        "message" : "\nL'avatar s'est déplacé vers la droite.\n",
        "game_in_progress" : True,
        "movement" : True,
        "impossible" : "\nImpossible d'aller plus à droite."
    },
    "G" : {
        "name" : "Gauche",
        # "character" : "G",
        "message" : "\nL'avatar s'est déplacé vers la gauche.\n",
        "game_in_progress" : True,
        "movement" : True,
        "impossible" : "\nImpossible d'aller plus à gauche."
    },
    "P" : {
        "name" : "Prendre",
        # "character" : "P",
        "message" : "\nL'avatar a pris l'objet.\n",
        "game_in_progress" : True,
        "movement" : False,
        "impossible" : "\nIl n'y a rien à prendre ici."
    },
    "U" : {
        "name" : "Utiliser",
        # "character" : "U",
        "message" : "\nL'avatar a utilisé l'objet.\n",
        "game_in_progress" : True,
        "movement" : False,
        "impossible" : "\nImpossible."
    },
    "A" : {
        "name" : "Abandonner",
        # "character" : "A",
        "message" : "\nL'avatar a abandonné l'objet parterre.\n",
        "game_in_progress" : True,
        "movement" : False,
        "impossible" : "\nImpossible."
    },
    "Y" : {
        "name" : "s'hYdrater",
        # "character" : "Y",
        "message" : "\nL'avatar s'est hydraté.\n",
        "game_in_progress" : True,
        "movement" : False,
        "impossible" : "\nImpossible de s'hydrater."
    },
    "M" : {
        "name" : "Manger",
        # "character" : "M",
        "message" : "\nL'avatar a mangé.\n",
        "game_in_progress" : True,
        "movement" : False,
        "impossible" : "\nImpossible de manger."
    },
    "R" : {
        "name" : "se Reposer",
        # "character" : "R",
        "message" : "\nL'avatar s'est reposé.\n",
        "game_in_progress" : True,
        "movement" : False,
        "impossible" : "\nImpossible de se reposer."
    },
    "" : {
        "name" : " ",
        # "character" : "",
        "message" : "\nLa partie continue.\n",
        "game_in_progress" : True,
        "movement" : False,
        "impossible" : "\nImpossible."
    },
}

possibles_actions =  ", ".join(actions.keys())


# places of challenges
    ## 4 places : 3 challenges and 1 gate

place = {
    "1" : {
        "name" : "Mysterious number",
        "col_x" : 57,
        "ln_y" : 18,
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


    ## challenge 1 :: mysterious number


player_number = ""
sphinx_number = ""

    ## challenge 2 :: caesar code
original_message = "BEAUTIFUL IS BETTER THAN UGLY. EXPLICIT IS BETTER THAN IMPLICIT. SIMPLE IS BETTER THAN COMPLEX."
coded_message = []
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

nb_round_caesar = 0

coded_name_try = ""
coded_player_name = ""

letter_code_random = (random.choice(string.ascii_uppercase))
number_code = 0

    ## challenge 3 :: multi FizzBuzz

players_fizzbuzz = {
    "monkey_1" : {
        "name_monkey" : "Chef Alain",
        "num_monkey" : 1,
        "chance" : random.randint(50,80)
    },
    "monkey_2" : {
        "name_monkey" : "Alex",
        "num_monkey" : 2,
        "chance" : random.randint(10,70)
            },
    "monkey_3" : {
        "name_monkey" : "Alexandre",
        "num_monkey" : 3,
        "chance" : random.randint(10,70)
    },
    "monkey_4" : {
        "name_monkey" : "Aurélia",
        "num_monkey" : 4,
        "chance" : random.randint(10,70)
    },
    "monkey_5" : {
        "name_monkey" : "Guillaume",
        "num_monkey" : 5,
        "chance" : random.randint(10,70)
    },
    "monkey_6" : {
        "name_monkey" : "Hadrien",
        "num_monkey" : 6,
        "chance" : random.randint(10,70)
    },
    "monkey_7" : {
        "name_monkey" : "Javier",
        "num_monkey" : 7,
        "chance" : random.randint(10,70)
    },
    "monkey_8" : {
        "name_monkey" : "Laura",
        "num_monkey" : 8,
        "chance" : random.randint(10,70)
    },
    "monkey_9" : {
        "name_monkey" : "Mélanie",
        "num_monkey" : 9,
        "chance" : random.randint(10,70)
    },
    "monkey_10" : {
        "name_monkey" : "Wilfried",
        "num_monkey" : 10,
        "chance" : random.randint(10,70)
    },
    "avatar" : {
        "name_monkey" : "",
        "num_monkey" : 11,
        "chance" : random.randint(80,90)
    }
}



# map
map1 = []
map_elements = {
    " " : {
        "name" : "terre",
        "image" : " ",
        "can_walk" : True,
        "message_walk" : "\nTu marches en regardant le magnifique paysage qui t'entoure.\n",
        "color_start" : "\u001b[38;5;15m",
        "color_end" : "\u001b[0m"
        },
    "^" : {
        "name" : "montain",
        "image" : "▲",
        "can_walk" : False,
        "message_walk" : "\nTu n'es pas équipé pour escalader la montagne.\n",
        "color_start" : "\u001b[38;5;136m",
        "color_end" : "\u001b[0m"
        },
    "u" : {
        "name" : "river",
        "image" : "≈",
        "can_walk" : False,
        "message_walk" : "\nIl y a trop de courant. Tu ne peux pas traverser.\nTrouves un endroit où la rivière est moins large et mets un tronc d'arbres en travers pour la traverser.",
        "color_start" : "\u001b[38;5;21m",
        "color_end" : "\u001b[0m"
        },
    "s" : {
        "name" : "sea",
        "image" : "▓",
        "can_walk" : False,
        "message_walk" : "\nLa mer est beaucoup trop agitée... Tu ne peux pas nager sans risquer de te noyer.\n",
        "color_start" : "\u001b[38;5;117m",
        "color_end" : "\u001b[0m"
        },
    "J" : {
        "name" : "jungle",
        "image" : "♣",
        "can_walk" : False,
        "message_walk" : "\nRegarde où tu marches !\n",
        "color_start" : "\u001b[38;5;65m",
        "color_end" : "\u001b[0m"
        },
    "v" : {
        "name" : "steppe",
        "image" : "∞",
        "can_walk" : False,
        "message_walk" : "\nAie ! Ces arbustes piquent. Impossible de passer.\n",
        "color_start" : "\u001b[38;5;34m",
        "color_end" : "\u001b[0m"
        },
    ":" : {
        "name" : "sand",
        "image" : "▒",
        "can_walk" : True,
        "message_walk" : "\nAttention! Le sable est très chaud...\n",
        "color_start" : "\u001b[38;5;226m",
        "color_end" : "\u001b[0m"
        },
    "-" : {
        "name" : "tree trunk",
        "image" : "▬",
        "can_walk" : True,
        "message_walk" : "\nBravo ! Tu peux traverser la rivière.\n",
        "color_start" : "\u001b[38;5;94m",
        "color_end" : "\u001b[0m"
    }
}

if __name__ == "__main__" :
    # get_list_place_symbol()
    pass
