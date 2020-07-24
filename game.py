# coding: utf-8

# import modules
import time

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

    actions_instruction = ""

    # until the action given by the player is not valid
    # still asks
    while actions_instruction not in variables.actions :
        actions_instruction = input("Que dois faire ton avatar ? ").strip().upper()

    # if no number after the letter action, the occurence of this action is 1 (by default)
    number_action  = 1

    # replaces the string given by the players in a list of actions (separated by space)
    avatar_actions_list = avatar_actions.split(" ")

    # for each action in list
    for action in avatar_actions_list :
        action_is_valid = False
        # checks if action exists in variables.actions
        for action_todo in variables.actions :
            # gets letter action only (not the number) with a list slice
            letter_action = action[:1]
            if letter_action == action_todo[0]:
                # action exists in variables.actions
                action_is_valid = True
                if action_todo[1] == True :
                    # check if there is a number for the action
                    if len(action) > 1 :
                        # if there is one, extrat it
                        number_action  = int(action[1:])
                        # if not, keeps 1 by default
                # stop browsing actions
                break
        # if valid action
        # # executes action
        game.execute_avatar_action(letter_action, number_action )

        # resets number of action at 1 (by default)
        number_action  = 1

        # if the action doesn't exist
        if not action_is_valid :
            print(f"{action} n'est pas une instruction connue.")
            print(f'Selectionne une action parmi les suivantes : {variables.possibles_actions}')


def place_avatar_on_map() :
    """
        places the avatar on the map and saves the symbol that was here before
    """

    if not variables.avatar_previous_position == None :
        # put the symbol that was at the previous avatar position
        variables.map1[variables.avatar_previous_position] =variables.symbol_under_avatar

    # save symbol map
    variables.symbol_under_avatar = variables.map1[variables.letter_avatar_symbol]
    # place avatar symbol
    variables.map1[variables.letter_avatar_symbol] = variables.avatar_symbol_current
    # save prevuois avatar position
    variables.avatar_previous_position = variables.letter_avatar_symbol



def execute_avatar_action(current_action, action_occurences) :
    """
    executes action
    """
    new_avatar_x = variables.avatar_position["x"]
    new_avatar_y = variables.avatar_position["y"]

    # prepare current_action
    while variables.game_in_progress :

        # avatar moves up
        if current_action == "H":
            for movement in range(action_occurences) :
                if new_avatar_y < 30 :  
                    # move avatar
                    new_avatar_y -= 1
                    # update counters

                    # places avatar on the map
                    place_avatar_on_map()
                    # show message
                    print(variables.actions["H"]["message"])
                    # game continues
                    variables.game_in_progress = variables.actions["H"]["game_in_progress"]
                else :
                    # if action go to high, print message
                    print(variables.actions["H"]["impossible"])
                # change avatar position x and y
                variables.avatar_position["x"] = new_avatar_x
                variables.avatar_position["y"] = new_avatar_y
                # shows the dashboard
                show_new_map()
                # slow down the movement of the avatar on the map
                time.sleep(variables.avatar_speed)
        
    
        # avatar moves down
        elif current_action == "B":
            new_avatar_y += 1
            print(variables.actions["B"]["message"])
            variables.game_in_progress = variables.actions["B"]["game_in_progress"]
            # executes current_action
            variables.avatar_position["x"] = new_avatar_x
            variables.avatar_position["y"] = new_avatar_y
            show_dashboard()
            
        # avatar moves to the right
        elif current_action == "D":
            new_avatar_x += 1
            print(variables.actions["D"]["message"])
            variables.game_in_progress = variables.actions["D"]["game_in_progress"]
            # executes current_action
            variables.avatar_position["x"] = new_avatar_x
            variables.avatar_position["y"] = new_avatar_y
            show_dashboard()

        # avatar moves to the left
        elif current_action == "G":
            new_avatar_x -= 1
            print(variables.actions["G"]["message"])
            variables.game_in_progress = variables.actions["G"]["game_in_progress"]
            # executes action
            variables.avatar_position["x"] = new_avatar_x
            variables.avatar_position["y"] = new_avatar_y
            show_dashboard()


        elif current_action == "R":
            print(variables.actions["R"]["message"])
            variables.game_in_progress = variables.actions["R"]["game_in_progress"]
            return
            
        elif current_action == "P":
            print(variables.actions["P"]["message"])
            variables.game_in_progress = variables.actions["P"]["game_in_progress"]
            return
        elif current_action == "U":
            print(variables.actions["U"]["message"])
            variables.game_in_progress = variables.actions["U"]["game_in_progress"]  
            return      
        elif current_action == "A":
            print(variables.actions["A"]["message"])
            variables.game_in_progress = variables.actions["A"]["game_in_progress"]
            return
        elif current_action == "Y":
            print(variables.actions["Y"]["message"])
            variables.game_in_progress = variables.actions["Y"]["game_in_progress"]
            return
        elif current_action == "M":
            print(variables.actions["M"]["message"])
            variables.game_in_progress = variables.actions["M"]["game_in_progress"]  
            return      

        elif current_action == "Q":
            print(variables.actions["Q"]["message"])
            variables.game_in_progress = variables.actions["Q"]["game_in_progress"]
            return
        elif current_action == "C":
            print(variables.actions["C"]["message"])
            variables.game_in_progress = variables.actions["C"]["game_in_progress"]  
        elif current_action == "S":
            print(variables.actions["S"]["message"])
            variables.game_in_progress = variables.actions["S"]["game_in_progress"]
            return
        elif current_action == "T":
            print(variables.actions["T"]["message"])
            variables.game_in_progress = variables.actions["T"]["game_in_progress"]
            return

            

    show_dashboard()

    
    # if game is already ended, go out of the loop
        # return


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
        chosen_action = input("Tape ici tes instructions : ").upper() 

        # wait for a valid action
        # while chosen_action not in variables.possibles_actions :
        #     chosen_action = input(f"\nTu dois choisir entre les lettres suivantes : {variables.possibles_actions} : ").upper()

        if utilities.clear_console:
            utilities.clear_console()

        # execute action
        # execute_avatar_action(chosen_action)
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


def echec(player_name_def) :
    """
    echec of the player
    """
    
    while not variables.game_in_progress :
        pass




if __name__ == "__main__" :
    pass