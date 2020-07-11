# coding: utf-8

# import modules

# additional modules
import variables



def draw_map() :
    """
    Draw map on console
    """

    for Y in range(len(variables.map)) :
        for X in range(len(variables.map[Y])) :
            if (Y == variables.avatar_position["Y"] 
                and X == variables.avatar_position[X]) :
                # if above is true, avatar is in this place, so draw it
                print(variables.avatar_symbol, end="")
            else :
                # if not, draw the item of the map
                print(variables.map[variables.map[Y][X]]["image"], end="")
        print()




