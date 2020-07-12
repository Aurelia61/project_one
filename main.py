# coding: utf-8

# import modules

# additional modules
import game
import initialization


def start() :
    """
    Game start here
    """
    
    initialization.show_title_and_story()
    initialization.show_map()
    initialization.show_rules()


# main entry point
if __name__ == "__main__" :
    start()