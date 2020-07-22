def show_new_map ():
    """
        draws the map with the current placements of everything
    """

    load_map_from_file("map1")

    for Y in range(len(variables.map1)) :
        for X in range(len(variables.map1[Y])) :
            if variables.map1[Y][X] == variables.avatar_position["x"] and variables.map1[Y] == variables.avatar_position["y"]:
                # if above is true, avatar is in this place, so draw it
                print(f'{variables.avatar_symbol_current}', end="" )
            elif variables.map1[Y][X] in variables.place.keys() :
                print(f'{variables.place[variables.map1[Y][X]]["color_start"]}{variables.place[variables.map1[Y][X]]["image"]}{variables.place[variables.map1[Y][X]]["color_end"]}', end="")
            else :
                # if not, draw the item of the map
                print(f'{variables.map_elements[variables.map1[Y][X]]["color_start"]}{variables.map_elements[variables.map1[Y][X]]["image"]}{variables.map_elements[variables.map1[Y][X]]["color_end"]}', end="" )
                # print(f'{variables.avatar_symbol[variables.letter_avatar_symbol]["color_start"]}{variables.avatar_symbol[variables.letter_avatar_symbol]["symbol"]}{variables.avatar_symbol[variables.letter_avatar_symbol]["color_end"]}', end="")
        print()