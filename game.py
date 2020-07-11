# coding: utf-8

# import modules

# additional modules
import variables


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
                    # add character to map
                    columns.append(map_symbol)
                    # place character at map entry
                    if map_symbol == "X":
                        variables.avatar_position["X"] = X
                        variables.avatar_position["Y"] = Y
                    X += 1
                # add line to map
                variables.map1.append(columns)
                Y += 1

    except FileNotFoundError:
        variables.game_in_progress = False     ######################### !!!!!!!!
        print("\nCette carte n'existe pas.\n")


def draw_map() :
    """
    Draw map on console
    """

    for Y in range(len(variables.map1)) :
        for X in range(len(variables.map1[Y])) :
            if (Y == variables.avatar_position["Y"] 
                and X == variables.avatar_position["X"]) :
                # if above is true, avatar is in this place, so draw it
                print(variables.avatar_symbol, end="")
            else :
                # if not, draw the item of the map
                print(variables.map_elements[variables.map1[Y][X]]["image"], end="")
        print()




