# coding: utf-8

# import modules

# additional modules
import game


def start() :
    """
    Game start here
    """
    
    game.load_map_from_file("map1")
    game.draw_map()



# main entry point
if __name__ == "__main__" :
    start()