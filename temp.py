import variables
import utilities
import game

avatar_position = [3, 1]    # X, Y

map2 = []

avatar_symbol_current ="A"

def show_map(clear_console = True) :
    """
    shows the map.
    """

    load_map_from_file("map2")

    print("ok")

    for Y in range(len(map2)) :
        for X in range(len(map2[Y])) :
            if (Y == avatar_position[1]
                and X == avatar_position[0]) :
                # if above is true, avatar is in this place, so draw it
                print(avatar_symbol_current)
            else :
                # if not, draw the item of the map
                print(f'{variables.map_elements[map2[Y][X]]["color_start"]}{variables.map_elements[map2[Y][X]]["image"]}{variables.map_elements[map2[Y][X]]["color_end"]}', end="" )
        print("fini")

    print()
    print("Sauras-tu te déplacer en évitant les dangers de la jungle, des sables mouvants et des eaux profondes ?")    ##### Mettre les symbols
    print()
    print("Découvres maintenant comment jouer !")
    return

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
                map2.append(columns)
                Y += 1

    except FileNotFoundError:
        variables.game_in_progress = False     ######################### !!!!!!!!
        print("\nCette carte n'existe pas.\n")


show_map()
