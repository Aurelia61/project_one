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
    print("  - déplacer l'avatar vers le \u001b[1m(H)\u001b[0maut")                  #  de n cases (par exemple H2)
    print("  - déplacer l'avatar vers le \u001b[1m(B)\u001b[0mas")                  #  de n cases (par exemple B6)
    print("  - déplacer l'avatar vers la \u001b[1m(D)\u001b[0mroite")                #  de n cases (par exemple D5)
    print("  - déplacer l'avatar vers la \u001b[1m(G)\u001b[0mauche")                #  de n cases (par exemple G1)
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
    pass


def try_again_or_not():
    pass


def show_new_map ():
    """
        draws the map with the current placements of everything
    """

    # utilities.load_map_from_file("map1")

    for Y in range(len(variables.map1)) :
        for X in range(len(variables.map1[Y])) :
            if variables.map1[Y][X] == variables.avatar_position["x"] and variables.map1[Y] == variables.avatar_position["y"]:
                # if above is true, avatar is in this place, so draw it
                print(f'{variables.avatar_symbol_current}', end="" )
            elif variables.map1[Y][X] in variables.place.keys() :
                print(f'{variables.place[variables.map1[Y][X]]["color_start"]}{variables.place[variables.map1[Y][X]]["image"]}{variables.place[variables.map1[Y][X]]["color_end"]}', end="")
            else :
                # if not, draw the item of the map
                print(f'{variables.avatar_symbol[variables.letter_avatar_symbol]["color_start"]}{variables.avatar_symbol[variables.letter_avatar_symbol]["symbol"]}{variables.avatar_symbol[variables.letter_avatar_symbol]["color_end"]}', end="")
        print()


if __name__ == "__main__" :
    show_instructions()
    # load_map_from_file("map1")
    # pass

