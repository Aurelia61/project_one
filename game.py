# coding: utf-8

# import modules

# additional modules
import variables
import initialization
import utilities


def get_avatar_action():
    """
        Ask for avatar action
    """

    while variables.game_in_progress :
        print()
        variables.chosen_action = input("Appuies sur (Q) pour quitter ou sur (C) pour continuer :").upper() 

        # wait for a valid action
        while variables.chosen_action not in variables.possibles_actions :
            variables.chosen_action = input(f"\nTu dois choisir entre les lettres suivantes : {variables.possibles_actions}").upper()

        if utilities.clear_console:
            utilities.clear_console()

        # execute action
        execute_avatar_action()
        return


def execute_avatar_action() :
    """
    executes chosen action
    """

    while variables.game_in_progress :
        if variables.chosen_action == "Q":
            print(variables.actions["Q"]["message"])
            variables.game_in_progress = variables.actions["Q"]["game_in_progress"]
            return
        elif variables.chosen_action == "C":
            print(variables.actions["C"]["message"])
            variables.game_in_progress = variables.actions["C"]["game_in_progress"]
            return



def draw_map() :
    """
    Draw map on console
    """
    pass

    for Y in range(len(variables.map1)) :
        for X in range(len(variables.map1[Y])) :
            if (Y == variables.avatar_position[1] 
                and X == variables.avatar_position[0]) :
                # if above is true, avatar is in this place, so draw it
                print(variables.avatar_symbol, end="")
            else :
                # if not, draw the item of the map
                print(variables.map_elements[variables.map1[Y][X]]["image"], end="")
        print()


def echec(player_name) :
    """
    echec of the player
    """
    
    pass

