
import utilities


def show_map_blind(blind_map):
    utilities.load_map_from_file(blind_map, map_blind_print)

    for Y in range(len(variables.map_blind_print)) :
        for X in range(len(variables.map_blind_print[Y])) :
            print("▓", end="" )
        print()

show_map_blind("eyes")