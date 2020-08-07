# coding: utf-8

# import modules
import os
import sys


# additional modules
import variables
import initialization


def continue_or_exit(clear_console_ok = True):
    """
        Asks if the player wants to continue or to exit
    """

    chosen_action = ""
    while variables.game_in_progress :
        print()
        chosen_action = input("Appuies sur (Q) pour quitter ou sur (C) pour continuer : ").upper() 

        # until the action given by the player is not valid
        # still asks
        while chosen_action != "Q" and chosen_action != "C" and chosen_action != "":
            chosen_action = input(f'\nTu dois choisir entre les lettres suivantes : "C" ou "Q" : ').upper()
        if chosen_action == "Q":
            if clear_console_ok :
                clear_console()
            print(variables.actions["Q"]["message"])
            variables.game_in_progress = variables.actions["Q"]["game_in_progress"]
            show_image("quitter")
            return
        elif chosen_action == "C":
            if clear_console_ok :
                clear_console()
                print(variables.actions["C"]["message"])
            variables.game_in_progress = variables.actions["C"]["game_in_progress"]
            return
        elif chosen_action == "":
            print(variables.actions[""]["message"])
            variables.game_in_progress = variables.actions[""]["game_in_progress"]
            return

        if clear_console_ok:
            clear_console()

        return                     # A vérifier si toujours utile, car normalement la boucle while doit s'arrêter !!


def clear_console() :
    """
    clears the console depending on OS.
    """

    if "win" in sys.platform.lower():
        # for windows
        os.system("cls")
    elif "linux" in sys.platform.lower():
        # for linux
        os.system("clear")


def load_map_from_file(file_name = "map1"):
    """
        Load a map from specified file name
    """

    # choose the placement of the 4 mysterious places
    initialization.choose_placement_challenge()

    # get the place of all the items
    initialization.get_place_items()

    try:
        with open(file_name, "r", encoding="utf-8") as my_file:
            Y = 0
            for line in my_file:
                columns = []
                X = 0
                for map_symbol in line:
                    # ignore line ends
                    if map_symbol == "\n":
                        continue
                    # place items on map
                    if map_symbol == " " :
                        for keys in variables.items_available :
                            for number in range(variables.items_available[keys]["number"]) :
                                if (Y == variables.items_available[keys]["ln_y"][number]
                                    and X == variables.items_available[keys]["col_x"][number]) :
                                    # if above is true, there is an item here, so draw it
                                    columns.append(variables.items_available[keys]["symbol_items"])
                    # place avatar on the map
                    if (Y == variables.avatar_position["y"] 
                        and X == variables.avatar_position["x"]) :
                        # if above is true, avatar is in this place, so draw it
                        columns.append(variables.letter_avatar_symbol)
                    # place challenges and gate on the map
                    elif (Y == variables.place["1"]["ln_y"]
                        and X == variables.place["1"]["col_x"]):
                        # if above is true, there is the challenge 1 here, so draw the number
                        columns.append(variables.place["1"]["print"])
                    elif (Y == variables.place["2"]["ln_y"]
                        and X == variables.place["2"]["col_x"]):
                        # if above is true, there is the challenge 2 here, so draw the number
                        columns.append(variables.place["2"]["print"])
                    elif (Y == variables.place["3"]["ln_y"]
                        and X == variables.place["3"]["col_x"]):
                        # if above is true, there is the challenge 3 here, so draw the number
                        columns.append(variables.place["3"]["print"])
                    elif (Y == variables.place["4"]["ln_y"]
                        and X == variables.place["4"]["col_x"]):
                        # if above is true, there is the gate here, so draw the number
                        columns.append(variables.place["4"]["print"])
                    else : 
                        # add character to map
                        columns.append(map_symbol)
                    X += 1
                # add line to map
                variables.map1.append(columns)
                Y += 1
        return

    except FileNotFoundError:
        variables.game_in_progress = False     ######################### !!!!!!!!
        print("\nCette carte n'existe pas.\n")


def show_instructions() :
    """
        shows the instructions that the player can play
    """

    print("Que veux-tu faire ? ")
    print("  - déplacer l'avatar vers le \u001b[1m(H)\u001b[0maut de n cases (par exemple H2)")
    print("  - déplacer l'avatar vers le \u001b[1m(B)\u001b[0mas de n cases (par exemple B6)")
    print("  - déplacer l'avatar vers la \u001b[1m(D)\u001b[0mroite de n cases (par exemple D5)")
    print("  - déplacer l'avatar vers la \u001b[1m(G)\u001b[0mauche de n cases (par exemple G1)") 
    print("  - \u001b[1m(O)\u001b[0muvrir le sac à dos")
    print("  - se\u001b[1m (R)\u001b[0meposer pour récupérer des points de vie")
    print("  - \u001b[1m(S)\u001b[0mauvegarder la partie")
    print("  - \u001b[1m(T)\u001b[0mélécharger la partie")
    print("  - \u001b[1m(Q)\u001b[0muitter le jeu (et échouer)")


def show_counter ():
    """
        shows all the counters
    """
    print()
    print(f'Tu as fait \u001b[1m{variables.counters["number_movements"]["color_start"]}{variables.counters["number_movements"]["value"]}{variables.counters["number_movements"]["color_end"]}\u001b[0m déplacements et \u001b[1m{variables.counters["number_actions"]["color_start"]}{variables.counters["number_actions"]["value"]}{variables.counters["number_actions"]["color_end"]}\u001b[0m actions.\n')

    print(f'{variables.counters["life"]["name"]} ::\n' + f'{variables.counters["life"]["symbol_full"]}' * variables.counters["life"]["value"] + f'{variables.counters["life"]["symbol_empty"]}' * (variables.counters["life"]["value_max"] - variables.counters["life"]["value"]))
    print(f'{variables.counters["hydration"]["name"]} ::\n' + f'{variables.counters["hydration"]["symbol_full"]}' * variables.counters["hydration"]["value"] + f'{variables.counters["hydration"]["symbol_empty"]}' * (variables.counters["hydration"]["value_max"] - variables.counters["hydration"]["value"]))
    print(f'{variables.counters["satiety"]["name"]} ::\n' + f'{variables.counters["satiety"]["symbol_full"]}' * variables.counters["satiety"]["value"] + f'{variables.counters["satiety"]["symbol_empty"]}' * (variables.counters["satiety"]["value_max"] - variables.counters["satiety"]["value"]))
    print()


def get_text_place_symbol () : 
    """
        gets a string with the symbol of the 4 mysterious places
    """

    for k in (variables.place).keys() :
        (variables.list_place_symbol).append((variables.place[k]).get("color_start"))
        (variables.list_place_symbol).append((variables.place[k]).get("image"))
        (variables.list_place_symbol).append((variables.place[k]).get("color_end"))
        (variables.list_place_symbol).append(", ")
        variables.text_place_symbol = "".join(variables.list_place_symbol)
    return


def load_image_from_file(file_name):
    """
        Load a image from specified file name
    """

    # create a list in a dico
    variables.drawn_image[file_name] = []

    try:
        with open(file_name, "r", encoding="utf-8") as my_file:
            Y = 0
            for line in my_file:
                columns = []
                X = 0
                for image_symbol in line:
                    # ignore line ends
                    if image_symbol == "\n":
                        continue
                    # draw each symbol
                    columns.append(image_symbol)
                    X += 1
                # add line to map
                variables.drawn_image[file_name].append(columns)
                Y += 1
        return

    except FileNotFoundError:
        variables.game_in_progress = False     ######################### !!!!!!!!
        print("\nCette image n'existe pas.\n")


def show_image(image):
    load_image_from_file(image)

    for Y in range(len(variables.drawn_image[image])) :
        for X in range(len(variables.drawn_image[image][Y])) :
            if variables.drawn_image[image][Y][X] == " " :
                print(" ", end="" )
            elif variables.drawn_image[image][Y][X] == "i" :
                print("▓", end="" )
            elif variables.drawn_image[image][Y][X] == "y" :
                print("•", end="" )

        print()



def try_again_or_not():
    pass





if __name__ == "__main__" :
    # show_new_map()
    # show_instructions()
    # load_map_from_file("map1")
    # show_counter()
    # show_image("eyes")
    pass

# 