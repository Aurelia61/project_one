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
                    else: 
                        # add character to map
                        columns.append(map_symbol)
                    X += 1
                # add line to map
                variables.map1.append(columns)
                Y += 1
                # print(columns)     à supprimer car pour test impression symbol avatar

    except FileNotFoundError:
        variables.game_in_progress = False     ######################### !!!!!!!!
        print("\nCette carte n'existe pas.\n")

if __name__ == "__main__" :
    load_map_from_file("map1")

