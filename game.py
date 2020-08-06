# coding: utf-8

# import modules
import time

# additional modules
import variables
import initialization
import utilities
import mysterious_number_file
import caesar_code_file
import multi_fizzbuzz_file


def show_dashboard(clear_console = True) :
    """
    draws dashbord with map, instructions and live counter
    """
    while variables.game_in_progress :

        if clear_console:
            utilities.clear_console()

        # show the map
        show_new_map ()

        # shows the counters : eat, drink, live, items in the bag, ...
        utilities.show_counter()

        # shows intructions of the avatar's action
        utilities.show_instructions()

        # asks player which action she/he wants to play
        (letter_action, number_action) = get_avatar_action()

        # if valid action, execute action
        execute_avatar_action(letter_action, number_action)

        # if avatar on the game "1", play the game 1
        if variables.avatar_position["y"] == variables.place["1"]["ln_y"] and variables.avatar_position["x"] == variables.place["1"]["col_x"] :
            mysterious_number_file.mysterious_number_play()

        # if avatar on the game "2", play the game 2
        if variables.avatar_position["y"] == variables.place["2"]["ln_y"] and variables.avatar_position["x"] == variables.place["2"]["col_x"] :
            caesar_code_file.caesar_code_play()

        # if avatar on the game "3", play the game 3
        if variables.avatar_position["y"] == variables.place["3"]["ln_y"] and variables.avatar_position["x"] == variables.place["3"]["col_x"] :
            multi_fizzbuzz_file.multi_fizzbuzz_play()
        
        # check if there is an item where the avatar is
        for keys in variables.items_available :
            for number in range(variables.items_available[keys]["number"]) :
                if (variables.avatar_position["y"] == variables.items_available[keys]["ln_y"][number]
                    and variables.avatar_position["x"] == variables.items_available[keys]["col_x"][number]) :
                    # if above is true, there is an item here, ask to the player what to do
                    play_item(keys)
                    


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
                # if variables.actions[letter_action]["movement"] == True :                     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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


def execute_avatar_action(current_action, action_occurences=1, clear_console = True) :
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
                if new_avatar_y + movement > 0 :  
                    # move avatar
                    new_avatar_y -= 1
                    # update counters
                    variables.counters["number_movements"]["value"] += 1
                    variables.counters["life"]["value"] += variables.counters["life"]["movement"]
                    variables.counters["hydration"]["value"] += variables.counters["hydration"]["movement"]
                    variables.counters["satiety"]["value"] += variables.counters["satiety"]["movement"]
                    # game continues
                    variables.game_in_progress = variables.actions["H"]["game_in_progress"]
                else :
                    # if action go to high, print message
                    print(variables.actions["H"]["impossible"])
                    new_avatar_y = 0
            # change avatar position x and y
            variables.avatar_position["x"] = new_avatar_x
            variables.avatar_position["y"] = new_avatar_y
            # clear console
            if clear_console:
                utilities.clear_console()
            # show message
            print(variables.actions["H"]["message"])
            # keep the message visible for a while
            time.sleep(variables.message_speed)
            return

        # avatar moves down
        elif current_action == "B":
            for movement in range(action_occurences) :
                if new_avatar_y + movement < 30 :  
                    # move avatar
                    new_avatar_y += 1
                    # update counters
                    variables.counters["number_movements"]["value"] += 1
                    variables.counters["life"]["value"] += variables.counters["life"]["movement"]
                    variables.counters["hydration"]["value"] += variables.counters["hydration"]["movement"]
                    variables.counters["satiety"]["value"] += variables.counters["satiety"]["movement"]
                    # game continues
                    variables.game_in_progress = variables.actions["B"]["game_in_progress"]                   
                else :
                    # if action go to down, print message
                    print(variables.actions["B"]["impossible"])
                    new_avatar_y = 30
            # change avatar position x and y
            variables.avatar_position["x"] = new_avatar_x
            variables.avatar_position["y"] = new_avatar_y
            # clear console
            if clear_console:
                utilities.clear_console()
            # show message
            print(variables.actions["B"]["message"])
            # keep the message visible for a while
            time.sleep(variables.message_speed)
            return
            
        # avatar moves to the left
        elif current_action == "G":
            for movement in range(action_occurences) :
                if new_avatar_x + movement > 0 :
                    # move avatar
                    new_avatar_x -= 1
                    # update counters
                    variables.counters["number_movements"]["value"] += 1
                    variables.counters["life"]["value"] += variables.counters["life"]["movement"]
                    variables.counters["hydration"]["value"] += variables.counters["hydration"]["movement"]
                    variables.counters["satiety"]["value"] += variables.counters["satiety"]["movement"]
                    # game continues
                    variables.game_in_progress = variables.actions["G"]["game_in_progress"]
                elif new_avatar_x + movement < 0 :
                    # if action go to right, print message
                    print(variables.actions["G"]["impossible"])
                    new_avatar_x = 0
            # change avatar position x and y
            variables.avatar_position["x"] = new_avatar_x
            variables.avatar_position["y"] = new_avatar_y
            # clear console
            if clear_console:
                utilities.clear_console()
            # show message
            print(variables.actions["G"]["message"])
            # keep the message visible for a while
            time.sleep(variables.message_speed)
            return

        # avatar moves to the right
        elif current_action == "D":
            for movement in range(action_occurences) :
                if new_avatar_x + movement < 80 :  
                    # move avatar
                    new_avatar_x += 1
                    # update counters
                    variables.counters["number_movements"]["value"] += 1
                    variables.counters["life"]["value"] += variables.counters["life"]["movement"]
                    variables.counters["hydration"]["value"] += variables.counters["hydration"]["movement"]
                    variables.counters["satiety"]["value"] += variables.counters["satiety"]["movement"]
                    # game continues
                    variables.game_in_progress = variables.actions["D"]["game_in_progress"]
                elif new_avatar_x + movement > 80 :
                    # if action go to right, print message
                    print(variables.actions["D"]["impossible"])
                    new_avatar_x = 80                
            # change avatar position x and y
            variables.avatar_position["x"] = new_avatar_x
            variables.avatar_position["y"] = new_avatar_y
            # clear console
            if clear_console:
                utilities.clear_console()
            # show message
            print(variables.actions["D"]["message"])
            # keep the message visible for a while
            time.sleep(variables.message_speed)
            return
            
        elif current_action == "R":
            # get the number of hour the avatar havs to sleep
            print()
            print("Tu as décidé de dormir.")
            print(f'Ton avatar gagne {variables.counters["life"]["dormir"]} point de vie par heure dormie.')
            nb_hour_sleep = int(input("Combien d'heure(s) veux-tu que ton avatar dorme ? "))
            # modify the counter of "lif", "hydratation" and "satiety"
            variables.counters["life"]["value"] += nb_hour_sleep * variables.counters["life"]["dormir"]
            variables.counters["hydration"]["value"] += nb_hour_sleep * variables.counters["hydration"]["dormir"]
            variables.counters["satiety"]["value"] += nb_hour_sleep * variables.counters["satiety"]["dormir"]
            # check to don't go over the max value or min value (=death)
            if variables.counters["life"]["value"] > variables.counters["life"]["value_max"]:
                variables.counters["life"]["value"] = variables.counters["life"]["value_max"]
            if variables.counters["hydration"]["value"] < variables.counters["hydration"]["value_min"] :
                print(variables.counters["hydration"]["message_mort"])
            if variables.counters["satiety"]["value"] < variables.counters["satiety"]["value_min"] :
                print(variables.counters["hydration"]["message_mort"])
                # clear console
            if clear_console:
                utilities.clear_console()
            # print a little message
            print(variables.actions["R"]["message"])
            for hour in range(nb_hour_sleep+1) :
                nb_hour_sleep_left = nb_hour_sleep - hour
                if hour == 0 :
                    continue
                elif hour == 1 :
                    print(f"Ton avatar dort depuis {hour} heure.\nEncore {nb_hour_sleep_left}...")
                    time.sleep(variables.message_speed)
                elif hour == nb_hour_sleep+1:
                    print(f"Ton avatar a dormi {hour} heure(s).\nIl est temps de se réveiller !!")
                else:
                    print(f"Ton avatar dort depuis {hour} heures.\nEncore {nb_hour_sleep_left}...")
                    time.sleep(variables.message_speed)            
            # game still in progress
            variables.game_in_progress = variables.actions["R"]["game_in_progress"]
            # update counters
            variables.counters["number_actions"]["value"] += 1
            return
        
        elif current_action == "O":
            # clear console
            if clear_console:
                utilities.clear_console()
            print(variables.actions["O"]["message"])
            time.sleep(variables.message_speed)
            open_backpack()
            variables.game_in_progress = variables.actions["O"]["game_in_progress"]



            # update counters
            variables.counters["number_actions"]["value"] += 1


        elif current_action == "P":
            print(variables.actions["P"]["message"])
            variables.game_in_progress = variables.actions["P"]["game_in_progress"]
            # update counters
            variables.counters["number_actions"]["value"] += 1

            return
        elif current_action == "U":
            print(variables.actions["U"]["message"])
            variables.game_in_progress = variables.actions["U"]["game_in_progress"]
            # update counters
            variables.counters["number_actions"]["value"] += 1

            return      
        elif current_action == "A":
            print(variables.actions["A"]["message"])
            variables.game_in_progress = variables.actions["A"]["game_in_progress"]
            # update counters
            # variables.counters["number_actions"]["value"] += 1

            return
        elif current_action == "Y":
            print(variables.actions["Y"]["message"])
            variables.game_in_progress = variables.actions["Y"]["game_in_progress"]
            # update counters
            variables.counters["number_actions"]["value"] += 1

            return
        elif current_action == "M":
            print(variables.actions["M"]["message"])
            variables.game_in_progress = variables.actions["M"]["game_in_progress"]
            # update counters
            variables.counters["number_actions"]["value"] += 1

            return      

        elif current_action == "Q":
            print(variables.actions["Q"]["message"])
            variables.game_in_progress = variables.actions["Q"]["game_in_progress"]
            # update counters
            # variables.counters["number_actions"]["value"] += 1

            return
        elif current_action == "C":
            print(variables.actions["C"]["message"])
            variables.game_in_progress = variables.actions["C"]["game_in_progress"]
            # update counters
            # variables.counters["number_actions"]["value"] += 1

        elif current_action == "S":
            print(variables.actions["S"]["message"])
            variables.game_in_progress = variables.actions["S"]["game_in_progress"]
            # update counters
            # variables.counters["number_actions"]["value"] += 1

            return
        elif current_action == "T":
            print(variables.actions["T"]["message"])
            variables.game_in_progress = variables.actions["T"]["game_in_progress"]
            # update counters
            # variables.counters["number_actions"]["value"] += 1

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
                elif variables.map1[Y][X] in variables.possibles_item_symbol and variables.map1[Y][X] != " " and variables.map1[Y][X] != "r":
                    # if above is true, item is in this place, so draw it
                    print(variables.symbol_items, end="") 
                    current_item_found = variables.map1[Y][X]
                elif variables.map1[Y][X] in variables.possibles_item_symbol and variables.map1[Y][X] != " " and variables.map1[Y][X] == "r":
                    # if above is true, item is in this place, so draw it
                    print(variables.items_available["r"]["symbol_items"], end="") 
                    current_item_found = variables.map1[Y][X]
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


def play_item(item, clear_console = True) :
    """
        choose what to do with the item
    """
    
    if clear_console :
        utilities.clear_console()

    print(f'Tu viens de trouver {variables.items_available[item]["name"]}.\n Tu peux :')
    print("  - \u001b[1m(P)\u001b[0mrendre l'objet et le mettre dans ton sac à dos")
    print("  - \u001b[1m(U)\u001b[0mtiliser l'object aussitôt")
    print("  - \u001b[1m(A)\u001b[0mbandonner l'object au sol")
    action_item = input("\nQue veux-tu faire ? ").upper()

    if action_item == "P" :
        # mettre l'objet dans le sac à dos
        variables.backpack[item] = (variables.items_available[item])
        # modify counter
        variables.counters["number_actions"]["value"] += 1
        print(f'Voilà {variables.items_available[item]["name"]} dans ton sac à dos !\n{variables.items_available[item]["message"]}\nRetour à la carte...')
        time.sleep(variables.message_speed)

    elif action_item == "U" :
        # lancer la fonction pour utiliser l'objet

        # modify counter
        variables.counters["number_actions"]["value"] += 1
        pass

    elif action_item == "A" :
        # do nothing
        print("Tu as décidé de le laisser là.\nRetour à la carte...")
        time.sleep(variables.message_speed)


def open_backpack(clear_console = True) :
    print("Voici ce que tu as dans ton sac à dos :")
    for item in variables.backpack.keys() :
        print(f'- {variables.backpack[item]["name"]} qui te redonne {variables.backpack[item]["value_hydration"]} point(s) d hydratation et {variables.backpack[item]["value_satiety"]} point(s)de satiété.Tape {variables.backpack[item]["symbol_items"]} pour le sélectionner.')
    item_backpack_chosen = input(f"Quel objet veux-tu prendre ? ").lower()
    if variables.backpack[item_backpack_chosen]["drink"] and not variables.backpack[item_backpack_chosen]["eat"] and not variables.backpack[item_backpack_chosen]["blind"] :
        print(f'Ton avatar gagne {variables.backpack[item]["value_hydration"]} point(s) d hydratation.')
        if variables.backpack[item]["value_hydration"] != 0 :
            print("La chance ! ")
            print(f'Avec {variables.backpack[item_backpack_chosen]["name"]}, tu gagnes aussi {variables.backpack[item]["value_satiety"]} point(s) de satiété.')
        utilities.continue_or_exit()
    elif not variables.backpack[item_backpack_chosen]["drink"] and variables.backpack[item_backpack_chosen]["eat"] and not variables.backpack[item_backpack_chosen]["blind"] :
        print(f'Ton avatar gagne {variables.backpack[item]["value_satiety"]} point(s) de satiété.')
        if variables.backpack[item]["value_satiety"] != 0 :
            print("La chance ! ")
            print(f'Avec {variables.backpack[item_backpack_chosen]["name"]}, tu gagnes aussi {variables.backpack[item]["value_hydration"]} point(s) d hydratation.')
        utilities.continue_or_exit()
    elif variables.backpack[item_backpack_chosen]["drink"] and variables.backpack[item_backpack_chosen]["eat"] and not variables.backpack[item_backpack_chosen]["blind"] :
        print("Quelle bonne idée !")
        print(f'Ton avatar gagne {variables.backpack[item]["value_hydration"]} point(s) d hydratation et {variables.backpack[item]["value_satiety"]} point(s) de satiété.')
        utilities.continue_or_exit()
    elif variables.backpack[item_backpack_chosen]["blind"] :
        if clear_console :
            utilities.clear_console()
            print("Que se passe-t-il ????\n Tout s'assombrit... \nOMG ! Tu deviens aveugle...")
            show_map_blind("eyes")
            time.sleep(20)

def show_map_blind(blind_map):
    utilities.load_map_from_file(blind_map, map_blind_print)

    for Y in range(len(variables.map_blind_print)) :
        for X in range(len(variables.map_blind_print[Y])) :
            print("▓", end="" )
        print()




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


if __name__ == "__main__" :
    pass