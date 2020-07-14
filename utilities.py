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
                    if (Y == variables.avatar_position[1] 
                        and X == variables.avatar_position[0]) :
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
    chooses the placement of the 3 challenges    
    """
                                                # randomly ???????
    variables.key_place_1 = "1"
    variables.key_place_2 = "2"
    variables.key_place_3 = "3"
    variables.key_gate = "4"

    



if __name__ == "__main__" :
    load_map_from_file("map1")
    # pass

