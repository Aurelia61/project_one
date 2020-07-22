# coding: utf-8

# import modules

# additional modules
import variables
import initialization
import utilities


def continue_or_exit(clear_console = True):
    """
        Asks if the player wants to continue or to exit
    """

    chosen_action = ""
    while variables.game_in_progress :
        print()
        chosen_action = input("Appuies sur (Q) pour quitter ou sur (C) pour continuer : ").upper() 

        # until the action given by the player is not valid
        # still asks
        while chosen_action != "Q" and chosen_action != "C" and chosen_action != "":
            chosen_action = input(f"\nTu dois choisir entre les lettres suivantes : {variables.possibles_actions} : ").upper()
        if chosen_action == "Q":
            print(variables.actions["Q"]["message"])
            variables.game_in_progress = variables.actions["Q"]["game_in_progress"]
            return
        elif chosen_action == "C":
            if utilities.clear_console:
                utilities.clear_console()
                print(variables.actions["C"]["message"])
            variables.game_in_progress = variables.actions["C"]["game_in_progress"]
            return
        elif chosen_action == "":
            print(variables.actions[""]["message"])
            variables.game_in_progress = variables.actions[""]["game_in_progress"]
            return

        if utilities.clear_console:
            utilities.clear_console()

        # if valid action
        # executes the action
        execute_avatar_action(chosen_action)
        return                     # A vérifier si toujours utile, car normalement la boucle while doit s'arrêter !!


def get_avatar_action ():
    """
        gets what the avatar has to do
    """

    chosen_action = ""
    # until the action given by the player is not valid
    # still asks
    while chosen_action not in variables.possibles_actions :
        chosen_action = input("Que dois faire ton avatar ? ").upper()

    # if valid action
    # executes the action
    execute_avatar_action(chosen_action)



def execute_avatar_action(action) :
    """
    executes chosen action
    """
    new_avatar_x = variables.avatar_position["x"]
    new_avatar_y = variables.avatar_position["y"]

    # prepares action
    while variables.game_in_progress :
        if action == "H":
            new_avatar_y -= 1
            print(variables.actions["H"]["message"])
            variables.game_in_progress = variables.actions["H"]["game_in_progress"]
            # executes action
            variables.avatar_position["x"] = new_avatar_x
            variables.avatar_position["y"] = new_avatar_y
            show_dashboard()

        elif action == "B":
            new_avatar_y += 1
            print(variables.actions["B"]["message"])
            variables.game_in_progress = variables.actions["B"]["game_in_progress"]
            # executes action
            variables.avatar_position["x"] = new_avatar_x
            variables.avatar_position["y"] = new_avatar_y
            show_dashboard()
            
        elif action == "D":
            new_avatar_x += 1
            print(variables.actions["D"]["message"])
            variables.game_in_progress = variables.actions["D"]["game_in_progress"]
            # executes action
            variables.avatar_position["x"] = new_avatar_x
            variables.avatar_position["y"] = new_avatar_y
            show_dashboard()

        elif action == "G":
            new_avatar_x -= 1
            print(variables.actions["G"]["message"])
            variables.game_in_progress = variables.actions["G"]["game_in_progress"]
            # executes action
            variables.avatar_position["x"] = new_avatar_x
            variables.avatar_position["y"] = new_avatar_y
            show_dashboard()

        elif action == "R":
            print(variables.actions["R"]["message"])
            variables.game_in_progress = variables.actions["R"]["game_in_progress"]
            return
            
        elif action == "P":
            print(variables.actions["P"]["message"])
            variables.game_in_progress = variables.actions["P"]["game_in_progress"]
            return
        elif action == "U":
            print(variables.actions["U"]["message"])
            variables.game_in_progress = variables.actions["U"]["game_in_progress"]  
            return      
        elif action == "A":
            print(variables.actions["A"]["message"])
            variables.game_in_progress = variables.actions["A"]["game_in_progress"]
            return
        elif action == "Y":
            print(variables.actions["Y"]["message"])
            variables.game_in_progress = variables.actions["Y"]["game_in_progress"]
            return
        elif action == "M":
            print(variables.actions["M"]["message"])
            variables.game_in_progress = variables.actions["M"]["game_in_progress"]  
            return      

        elif action == "Q":
            print(variables.actions["Q"]["message"])
            variables.game_in_progress = variables.actions["Q"]["game_in_progress"]
            return
        elif action == "C":
            print(variables.actions["C"]["message"])
            variables.game_in_progress = variables.actions["C"]["game_in_progress"]  
        elif action == "S":
            print(variables.actions["S"]["message"])
            variables.game_in_progress = variables.actions["S"]["game_in_progress"]
            return
        elif action == "T":
            print(variables.actions["T"]["message"])
            variables.game_in_progress = variables.actions["T"]["game_in_progress"]
            return

            

    show_dashboard()

    print("Game_in_progress = False !!!!!!")
    return          # A vérifier si toujours utile, car normalement la boucle while doit s'arrêter !!



def show_dashboard(clear_console = True) :
    """
    draws dashbord with map, instructions and live counter
    """
    while variables.game_in_progress :

        if clear_console:
            utilities.clear_console()

        show_new_map ()

        # shows intructions of the avatar's action
        utilities.show_instructions()

        # shows the counters : eat, drink, live, items in the bag, ...
        # utilities.show_counter()

        # asks player which action she/he wants to play
        chosen_action = ""
        print()
        chosen_action = input("Tapes ici tes instructions : ").upper() 

        # wait for a valid action
        while chosen_action not in variables.possibles_actions :
            chosen_action = input(f"\nTu dois choisir entre les lettres suivantes : {variables.possibles_actions} : ").upper()

        if utilities.clear_console:
            utilities.clear_console()

        # execute action
        execute_avatar_action(chosen_action)
        return        # A vérifier si toujours utile, car normalement la boucle while doit s'arrêter !!


def show_new_map (clear_console = True):
    """
        draws the map with the current placements of everything
    """

    if clear_console:
        utilities.clear_console()

    while variables.game_in_progress :
        utilities.load_map_from_file("map1")

        for Y in range(len(variables.map1)) :
            for X in range(len(variables.map1[Y])) :
                if variables.map1[Y][X] in variables.possibles_avatar_symbol and variables.map1[Y][X] != " ":
                    # if above is true, avatar is in this place, so draw it
                    print(f'{variables.avatar_symbol_current}', end="" )
                elif variables.map1[Y][X] in variables.place.keys() :
                    print(f'{variables.place[variables.map1[Y][X]]["color_start"]}{variables.place[variables.map1[Y][X]]["image"]}{variables.place[variables.map1[Y][X]]["color_end"]}', end="")
                    if variables.map1[Y][X] == "1" and variables.map1[Y][X] in variables.possibles_avatar_symbol :
                        mysterious_number()
                else :
                    # if not, draw the item of the map
                    print(f'{variables.map_elements[variables.map1[Y][X]]["color_start"]}{variables.map_elements[variables.map1[Y][X]]["image"]}{variables.map_elements[variables.map1[Y][X]]["color_end"]}', end="" )
            print()
        return


def echec(player_name) :
    """
    echec of the player
    """
    
    while not variables.game_in_progress :
        pass




if __name__ == "__main__" :
    pass