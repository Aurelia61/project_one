# coding: utf-8

# import modules

# additional modules
import game
import initialization
import variables


def start() :
    """
    Game start here
    """
    while variables.game_in_progress:
        initialization.show_title_and_story()
        initialization.get_name_and_symbol()
        initialization.show_map()
        initialization.show_rules()


        # pour éviter que le programme retourne au début
        variables.game_in_progress = False
    
    print(f"\nA bientôt {variables.player_name} !\n")

    return


# main entry point
if __name__ == "__main__" :
    start()