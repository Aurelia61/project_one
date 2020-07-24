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
        initialization.show_map_initial()
        initialization.show_rules()
        game.show_dashboard()


        # pour éviter que le programme retourne au début
        variables.game_in_progress = False
    
    print(f"\nA bientôt {variables.player_name_capitalize} !\n")

    return            # A vérifier si toujours utile, car normalement la boucle while doit s'arrêter !!


# main entry point
if __name__ == "__main__" :
    start()