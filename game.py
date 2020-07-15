# coding: utf-8

# import modules

# additional modules
import variables
import initialization
import utilities


def continue_or_exit():
    """
        Asks if the player wants to continue or to exit
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
        return                     # A vérifier si toujours utile, car normalement la boucle while doit s'arrêter !!


def execute_avatar_action() :
    """
    executes chosen action
    """

    while variables.game_in_progress :
        if variables.chosen_action == "H":
            print(variables.actions["H"]["message"])
            variables.game_in_progress = variables.actions["H"]["game_in_progress"]
            return
        elif variables.chosen_action == "B":
            print(variables.actions["B"]["message"])
            variables.game_in_progress = variables.actions["B"]["game_in_progress"]
            return
        elif variables.chosen_action == "D":
            print(variables.actions["D"]["message"])
            variables.game_in_progress = variables.actions["D"]["game_in_progress"]
            return
        elif variables.chosen_action == "G":
            print(variables.actions["G"]["message"])
            variables.game_in_progress = variables.actions["G"]["game_in_progress"]
            return
        elif variables.chosen_action == "P":
            print(variables.actions["P"]["message"])
            variables.game_in_progress = variables.actions["P"]["game_in_progress"]
            return
        elif variables.chosen_action == "U":
            print(variables.actions["U"]["message"])
            variables.game_in_progress = variables.actions["U"]["game_in_progress"]  
            return      
        elif variables.chosen_action == "A":
            print(variables.actions["A"]["message"])
            variables.game_in_progress = variables.actions["A"]["game_in_progress"]
            return
        elif variables.chosen_action == "Y":
            print(variables.actions["Y"]["message"])
            variables.game_in_progress = variables.actions["Y"]["game_in_progress"]
            return
        elif variables.chosen_action == "M":
            print(variables.actions["M"]["message"])
            variables.game_in_progress = variables.actions["M"]["game_in_progress"]  
            return      
        elif variables.chosen_action == "R":
            print(variables.actions["R"]["message"])
            variables.game_in_progress = variables.actions["R"]["game_in_progress"]
            return
        elif variables.chosen_action == "Q":
            print(variables.actions["Q"]["message"])
            variables.game_in_progress = variables.actions["Q"]["game_in_progress"]
            return
        elif variables.chosen_action == "C":
            print(variables.actions["C"]["message"])
            variables.game_in_progress = variables.actions["C"]["game_in_progress"]  
            return      
        elif variables.chosen_action == "S":
            print(variables.actions["S"]["message"])
            variables.game_in_progress = variables.actions["S"]["game_in_progress"]
            return
        elif variables.chosen_action == "T":
            print(variables.actions["T"]["message"])
            variables.game_in_progress = variables.actions["T"]["game_in_progress"]
            return
        # elif variables.chosen_action == "H":
        #     print(variables.actions["H"]["message"])
        #     variables.game_in_progress = variables.actions["H"]["game_in_progress"]

    print("Game_in_progress = False !!!!!!")
    return          # A vérifier si toujours utile, car normalement la boucle while doit s'arrêter !!



def show_dashboard(clear_console = True) :
    """
    draws dashbord with map, instructions and live counter
    """
    while variables.game_in_progress :

        if clear_console:
            utilities.clear_console()

        # draws the map with the current placements of everything
        # utilities.load_map_from_file("map1")

        for Y in range(len(variables.map1)) :
            for X in range(len(variables.map1[Y])) :
                if variables.map1[Y][X] in variables.avatar_symbol.keys() :
                    # if above is true, avatar is in this place, so draw it
                    print(f'{variables.avatar_symbol[variables.letter_avatar_symbol]["color_start"]}{variables.avatar_symbol[variables.letter_avatar_symbol]["symbol"]}{variables.avatar_symbol[variables.letter_avatar_symbol]["color_end"]}', end="")  
                elif variables.map1[Y][X] in variables.place.keys() :
                    print(f'{variables.place[variables.map1[Y][X]]["color_start"]}{variables.place[variables.map1[Y][X]]["image"]}{variables.place[variables.map1[Y][X]]["color_end"]}', end="")
                else :
                    # if not, draw the item of the map
                    print(f'{variables.map_elements[variables.map1[Y][X]]["color_start"]}{variables.map_elements[variables.map1[Y][X]]["image"]}{variables.map_elements[variables.map1[Y][X]]["color_end"]}', end="" )
            print()

        # shows intructions of the avatar's action
        utilities.show_instructions()

        # shows the counters : eat, drink, live, items in the bag, ...
        # utilities.show_counter()

        # asks player which action she/he wants to play
        print()
        variables.chosen_action = input("Tapes ici tes instructions : ").upper() 

        # wait for a valid action
        while variables.chosen_action not in variables.possibles_actions :
            variables.chosen_action = input(f"\nTu dois choisir entre les lettres suivantes : {variables.possibles_actions}").upper()

        if utilities.clear_console:
            utilities.clear_console()

        # execute action
        execute_avatar_action()
        return        # A vérifier si toujours utile, car normalement la boucle while doit s'arrêter !!



def echec(player_name) :
    """
    echec of the player
    """
    
    while not variables.game_in_progress :
        pass




if __name__ == "__main__" :
    pass