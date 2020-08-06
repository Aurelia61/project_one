# coding: utf-8

#import modules
import random
import string   # for choosing randomly a letter

# additional modules
import utilities

#player
player_name = ""


# game
game_in_progress = True
message_speed = 2

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
        "value_min" : 0,
        "value" : 100,
        "dormir" : 6,
        "movement" : -3,
        "message_mort" : "Ton avatar est mort de fatigue"
    },
    "hydration" : {
        "name" : "Points d'hydratation",
        "symbol_full" : "☼",
        "symbol_empty" : ".",
        "value_max" : 100,
        "value_min" : 0,
        "value" : 100,
        "dormir" : -2,
        "movement" : -2,
        "message_mort" : "Ton avatar est mort de soif"
    },
    "satiety" : {
        "name" : "Points de satiété",
        "symbol_full" : "♦",
        "symbol_empty" : ".",
        "value_max" : 100,
        "value_min" : 0,
        "value" : 100,
        "dormir" : -1,
        "movement" : -2,
        "message_mort" : "Ton avatar est mort de faim"
    }
}


# items
    ## what is in the backpack
backpack = {
    "knife" : {
        "name" : "Couteau",
        "symbol_items" : "f",
        "message" : "Attention à ne pas te couper !",
        "number" : 1,
        "col_x" : [],
        "ln_y" : [],
        "value_hydration" : 0,
        "value_satiety" : 0,
        "drink" : False,
        "eat" : False
    },
    "bottle" : {
        "name" : "Bouteille d'eau",
        "symbol_items" : "o",
        "message" : "Reste-t-il encore de l'au dedans...",
        "number" : 1,
        "col_x" : [],
        "ln_y" : [],
        "value_hydration" : 0,
        "value_satiety" : 0,
        "drink" : False,
        "eat" : False
    },
    "computer" : {
        "name" : "Ordinateur portable",
        "symbol_items" : "p",
        "message" : "Ce n'est pas le moment de jouer !",
        "number" : 1,
        "col_x" : [],
        "ln_y" : [],
        "value_hydration" : 0,
        "value_satiety" : 0,
        "drink" : False,
        "eat" : False
    },
}

    ## items that the player could find
items_available = {
    "c" : {
        "name" : "a coconut",
        "symbol_items" : "c",
        "message" : "Mmmm, ça va être bon ...",
        "number" : 10,
        "col_x" : [],
        "ln_y" : [],
        "value_hydration" : 15,
        "value_satiety" : 25,
        "blind" : False,
        "drink" : True,
        "eat" : True
    },
    "g" : {
        "name" : "spring_water",
        "symbol_items" : "g",
        "message" : "Mmmm, ça va être rafraichissant ...",
        "number" : 3,
        "col_x" : [],
        "ln_y" : [],
        "value_hydration" : 100,
        "value_satiety" : 5,
        "blind" : False,
        "drink" : True,
        "eat" : False
    },
    "w" : {
        "name" : "some worms",
        "symbol_items" : "w",
        "message" : "Des vers dans un sac à dos ?!?! A tes risques et périls ...",
        "number" : 20,
        "col_x" : [],
        "ln_y" : [],
        "value_hydration" : 2,
        "value_satiety" : 10,
        "blind" : False,
        "drink" : False,
        "eat" : True
    },
    "f" : {
        "name" : "fresh_water",
        "symbol_items" : "f",
        "message" : "Mmmm, ça va être rafraichissant ...",
        "number" : 5,
        "col_x" : [],
        "ln_y" : [],
        "value_hydration" : 100,
        "value_satiety" : 0,
        "blind" : False,
        "drink" : True,
        "eat" : False
    },
    "a" : {
        "name" : "sea_water",
        "symbol_items" : "s",
        "message" : "Beurk ! C'est beaucoup trop salé ...",
        "number" : 3,
        "col_x" : [],
        "ln_y" : [],
        "value_hydration" : -15,
        "value_satiety" : 0,
        "blind" : False,
        "drink" : True,
        "eat" : False
    },
    "b" : {
        "name" : "a banana",
        "symbol_items" : "b",
        "message" : "Mmmm, ça va être bon ...",
        "number" : 25,
        "col_x" : [],
        "ln_y" : [],
        "value_hydration" : 2,
        "value_satiety" : 50,
        "blind" : False,
        "drink" : False,
        "eat" : True
    },
    "r" : {
        "name" : "a red berry",
        "symbol_items" : "r",
        "message" : "Mmmm, ça va être bon ...",
        "number" : 3,
        "col_x" : [57],
        "ln_y" : [17],
        "value_hydration" : 0,
        "value_satiety" : 0,
        "blind" : True,
        "drink" : False,
        "eat" : True
    },
    "y" : {
        "name" : "some berries",
        "symbol_items" : "y",
        "message" : "Mmmm, ça va être bon ...",
        "number" : 10,
        "col_x" : [],
        "ln_y" : [],
        "value_hydration" : 2,
        "value_satiety" : 10,
        "blind" : False,
        "drink" : False,
        "eat" : True
    }
}

symbol_items = "."

current_item_found = ""
possibles_item_symbol =  ", ".join(items_available.keys())


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
        "message" : "\nL'avatar se déplace vers le haut.",
        "game_in_progress" : True,
        "movement" : True,
        "impossible" : "\nImpossible d'aller plus haut."
    },
    "B" : {
        "name" : "Bas",
        # "character" : "S",
        "message" : "\nL'avatar se déplace vers le bas.\n",
        "game_in_progress" : True,
        "movement" : True,
        "impossible" : "\nImpossible d'aller plus bas."
    },
    "D" : {
        "name" : "Droite",
        # "character" : "D",
        "message" : "\nL'avatar se déplace vers la droite.\n",
        "game_in_progress" : True,
        "movement" : True,
        "impossible" : "\nImpossible d'aller plus à droite."
    },
    "G" : {
        "name" : "Gauche",
        # "character" : "G",
        "message" : "\nL'avatar se déplace vers la gauche.\n",
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
        "message" : "\nL'avatar se repose.\n",
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
    "O" : {
        "name" : "ouvrir",
        # "character" : "",
        "message" : "\nLe sac à dos s'ouvre.\n",
        "game_in_progress" : True,
        "movement" : False,
        "impossible" : "\nImpossible."
    }
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
map_blind_print = []

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
    # pass
    print(symbol_items, end="")
    print(symbol_items, end="")
    print(symbol_items, end="")