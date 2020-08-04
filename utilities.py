# coding: utf-8

# import modules
import os
import sys
import variables


# additional modules

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


def load_map_from_file(file_name):
    """
        Load a map from specified file name
    """
    choose_placement_challenge()

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
                    # place avatar on the map
                    if (Y == variables.avatar_position["y"] 
                        and X == variables.avatar_position["x"]) :
                        # if above is true, avatar is in this place, so draw it
                        columns.append(variables.letter_avatar_symbol)
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
                #print(columns)     # à supprimer car pour test impression symbol avatar

    except FileNotFoundError:
        variables.game_in_progress = False     ######################### !!!!!!!!
        print("\nCette carte n'existe pas.\n")


def choose_placement_challenge() :
    """
    chooses the placement of the 4 mysterious places   
    """
                                                # randomly ???????
    variables.key_place_1 = "1"
    variables.key_place_2 = "2"
    variables.key_place_3 = "3"
    variables.key_gate = "4"


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


def show_instructions() :
    """
        shows the instructions that the player can play
    """

    print("Que veux-tu faire ? ")
    print("  - déplacer l'avatar vers le \u001b[1m(H)\u001b[0maut de n cases (par exemple H2)")
    print("  - déplacer l'avatar vers le \u001b[1m(B)\u001b[0mas de n cases (par exemple B6)")
    print("  - déplacer l'avatar vers la \u001b[1m(D)\u001b[0mroite de n cases (par exemple D5)")
    print("  - déplacer l'avatar vers la \u001b[1m(G)\u001b[0mauche de n cases (par exemple G1)") 
    print("  - \u001b[1m(P)\u001b[0mrendre un objet et le mettre dans le sac à dos")
    print("  - \u001b[1m(U)\u001b[0mtiliser un object")
    print("  - \u001b[1m(A)\u001b[0mbandonner un object au sol")
    print("  - s'h\u001b[1m(Y)\u001b[0mdrater pour augmenter ses points d'hydratation")
    print("  - \u001b[1m(M)\u001b[0manger pour augmenter ses points de satiété")
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

def try_again_or_not():
    pass





if __name__ == "__main__" :
    # show_new_map()
    # show_instructions()
    # load_map_from_file("map1")
    show_counter()
    # pass

# 