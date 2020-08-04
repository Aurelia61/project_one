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
            chosen_action = input(f'\nTu dois choisir entre les lettres suivantes : "C" ou "Q" : ').upper()
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
        # execute_avatar_action(chosen_action)
        return                     # A vérifier si toujours utile, car normalement la boucle while doit s'arrêter !!


def show_dashboard(clear_console = True) :
    """
    draws dashbord with map, instructions and live counter
    """
    while variables.game_in_progress :

        if clear_console:
            utilities.clear_console()

        show_new_map ()

        # shows the counters : eat, drink, live, items in the bag, ...
        # utilities.show_counter()

        # shows intructions of the avatar's action
        utilities.show_instructions()

        # asks player which action she/he wants to play
        (letter_action, number_action) = get_avatar_action()

        # if valid action, execute action
        execute_avatar_action(letter_action, number_action)

        # return        # A vérifier si toujours utile, car normalement la boucle while doit s'arrêter !!


def get_avatar_action ():
    """
        gets what the avatar has to do
    """

    actions_instruction = ""

    # until the action given by the player is not valid
    # still asks
    while actions_instruction == "" :
        actions_instruction = input("\nQue dois faire ton avatar ? ").strip().upper()

    # replaces the string given by the players in a list of actions (separated by space)
    actions_instruction_list = actions_instruction.split(" ")

    # for each action in list
    for action in actions_instruction_list :
        action_is_valid = False
        # checks if action exists in variables.actions
        for action_todo in variables.actions.keys() :
            # gets letter action only (not the number) with a list slice
            letter_action = (action[:1]).upper()
            if letter_action == action_todo:
                # action exists in variables.actions
                action_is_valid = True
                if variables.actions[letter_action]["movement"] == True :
                    # check if there is a number for the action
                    if len(action) > 1 :
                        # if there is one, extrat it
                        number_action = int(action[1:])
                        # if valid action, return values
                        return letter_action, number_action
                        # if not, keeps 1 by default
                    else :
                        number_action = 1
                        # if valid action, return values
                        return letter_action, number_action
                # stop browsing actions
                break


        # if the action doesn't exist
        # if not action_is_valid :
        #     print(f"{action} n'est pas une instruction connue.")
        #     print()
                

# def place_avatar_on_map() :
#     """
#         places the avatar on the map and saves the symbol that was here before
#     """

#     if not variables.avatar_previous_position == None :
#         # put the symbol that was at the previous avatar position
#         variables.map1[variables.avatar_previous_position] =variables.symbol_under_avatar

#     # save symbol map
#     variables.symbol_under_avatar = variables.map1[variables.avatar_position]
#     # place avatar symbol
#     variables.map1[variables.avatar_position] = variables.avatar_symbol_current
#     # save prevuois avatar position
#     variables.avatar_previous_position = variables.avatar_position



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
            for movement in range(0, action_occurences) :
                if new_avatar_y > 0 :  
                    # move avatar
                    new_avatar_y -= 1
                    # update counters

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
                # slow down the movement of the avatar on the map
                time.sleep(variables.avatar_speed)
            return

        # avatar moves down
        elif current_action == "B":
            for movement in range(action_occurences) :
                if new_avatar_y < 30 :  
                    # move avatar
                    new_avatar_y += 1
                    # update counters

                    # show message
                    print(variables.actions["B"]["message"])
                    # game continues
                    variables.game_in_progress = variables.actions["B"]["game_in_progress"]
                else :
                    # if action go to high, print message
                    print(variables.actions["B"]["impossible"])
                # change avatar position x and y
                variables.avatar_position["x"] = new_avatar_x
                variables.avatar_position["y"] = new_avatar_y
                # slow down the movement of the avatar on the map
                time.sleep(variables.avatar_speed)
            return
            
        # avatar moves to the right
        elif current_action == "D":
            for movement in range(action_occurences) :
                if new_avatar_x < 80 :  
                    # move avatar
                    new_avatar_x += 1
                    # update counters

                    # show message
                    print(variables.actions["D"]["message"])
                    # game continues
                    variables.game_in_progress = variables.actions["D"]["game_in_progress"]
                else :
                    # if action go to high, print message
                    print(variables.actions["B"]["impossible"])
                # change avatar position x and y
                variables.avatar_position["x"] = new_avatar_x
                variables.avatar_position["y"] = new_avatar_y
                # slow down the movement of the avatar on the map
                time.sleep(variables.avatar_speed)
            return
            

        # avatar moves to the left
        elif current_action == "G":
            new_avatar_x -= 1
            print(variables.actions["G"]["message"])
            variables.game_in_progress = variables.actions["G"]["game_in_progress"]
            # executes action
            variables.avatar_position["x"] = new_avatar_x
            variables.avatar_position["y"] = new_avatar_y
            


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
    
    # if game is already ended, go out of the loop
        # return


    print("Game_in_progress = False !!!!!!")
    return          # A vérifier si toujours utile, car normalement la boucle while doit s'arrêter !!


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