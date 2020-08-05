


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

                    # # place item on the map
                    # elif (Y == variables.items_available["coconut"]["ln_y"]
                    #     and X == variables.items_available["coconut"]["col_x"]):
                    #     # if above is true, there is a coconut here, so show it with the symbol
                    #     columns.append(variables.items_available["coconut"]["symbol_items"])
                    # elif (Y == variables.items_available["spring_water"]["ln_y"]
                    #     and X == variables.items_available["spring_water"]["col_x"]):
                    #     # if above is true, there is a spring water here, so show it with the symbol
                    #     columns.append(variables.items_available["spring_water"]["symbol_items"])
                    # elif (Y == variables.items_available["worm"]["ln_y"]
                    #     and X == variables.items_available["worm"]["col_x"]):
                    #     # if above is true, there are some worms here, so show it with the symbol
                    #     columns.append(variables.items_available["worm"]["symbol_items"])
                    # elif (Y == variables.items_available["banana"]["ln_y"]
                    #     and X == variables.items_available["banana"]["col_x"]):
                    #     # if above is true, there is a banana here, so show it with the symbol
                    #     columns.append(variables.items_available["banana"]["symbol_items"])
                    # elif (Y == variables.items_available["red_berry"]["ln_y"]
                    #     and X == variables.items_available["red_berry"]["col_x"]):
                    #     # if above is true, there is an item here, so show it with the symbol
                    #     columns.append(variables.items_available["red_berry"]["symbol_items"])
                    # elif (Y == variables.items_available["berry"]["ln_y"]
                    #     and X == variables.items_available["berry"]["col_x"]):
                    #     # if above is true, there is an item here, so show it with the symbol
                    #     columns.append(variables.items_available["berry"]["symbol_items"])

                    else : 
                        # add character to map
                        columns.append(map_symbol)
                    X += 1
                Y += 1