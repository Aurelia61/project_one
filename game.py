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

        # if one of the counter is 0, game is over
        if variables.counters["life"]["value"] < variables.counters["life"]["value_min"]:
            if clear_console:
                utilities.clear_console()
            print(variables.counters["life"]["message_mort"])
            utilities.show_image("skull")
            return
        if variables.counters["hydration"]["value"] < variables.counters["hydration"]["value_min"] :
            if clear_console:
                utilities.clear_console()
            print(variables.counters["hydration"]["message_mort"])
            utilities.show_image("skull")
            return
        if variables.counters["satiety"]["value"] < variables.counters["satiety"]["value_min"] :
            if clear_console:
                utilities.clear_console()
            print(variables.counters["hydration"]["message_mort"])
            utilities.show_image("skull")
            return

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

        # if avatar on the gate and if he has the 3 keys, the player win
        if variables.avatar_position["y"] == variables.place["4"]["ln_y"] :
            if variables.avatar_position["x"] == variables.place["4"]["col_x"] :
                if "g" in variables.backpack.keys() and "s" in variables.backpack.keys() and "b" in variables.backpack.keys() :
                    if clear_console:
                        utilities.clear_console()
                    print(f'{variables.player_name} a gagné !')
                    utilities.show_image("fist")
                    time.sleep(20)
            else :
                print("Tu as cru quoi ???")
                time.sleep(20)
        
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
        actions_instruction = input("\nQue doit faire ton avatar ? ").strip().upper()

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
            if clear_console:
                utilities.clear_console()
            # get the number of hour the avatar havs to sleep
            print()
            print("Tu as décidé de dormir.")
            print(f'Ton avatar gagne {variables.counters["life"]["dormir"]} point de vie par heure dormie.')
            nb_hour_sleep = int(input("Combien d'heure(s) ? "))
            # modify the counter of "life", "hydratation" and "satiety"
            variables.counters["life"]["value"] += nb_hour_sleep * variables.counters["life"]["dormir"]
            variables.counters["hydration"]["value"] += nb_hour_sleep * variables.counters["hydration"]["dormir"]
            variables.counters["satiety"]["value"] += nb_hour_sleep * variables.counters["satiety"]["dormir"]
            # check if the life value doesn't go over the max value, if yes, keep the max value no more
            if variables.counters["life"]["value"] > variables.counters["life"]["value_max"]:
                variables.counters["life"]["value"] = variables.counters["life"]["value_max"]
            # clear console
            if clear_console:
                utilities.clear_console()
            # print a little message
            print(variables.actions["R"]["message"])
            # for hour in range(nb_hour_sleep+1) :
            #     nb_hour_sleep_left = nb_hour_sleep - hour
            #     if hour == 0 :
            #         continue
            #     elif nb_hour_sleep == 1 and hour >= 1 :
            #         print(f"Ton avatar a dormi 1 heure.\nIl est temps de se réveiller !!")
            #         time.sleep(variables.message_speed)
            #     elif nb_hour_sleep_left == 1 and hour >= 1  :
            #         print(f"Ton avatar dort depuis {hour} heure.\nIl est temps de se réveiller !!")
            #         time.sleep(variables.message_speed)
            #     elif hour == nb_hour_sleep+1:
            #         print(f"Ton avatar a dormi {hour} heure(s).\nEncore {nb_hour_sleep_left}...")
            #     else:
            #         print(f"Ton avatar dort depuis {hour} heures.\nEncore {nb_hour_sleep_left}...")
            #         time.sleep(variables.message_speed)  
            time.sleep(variables.message_speed * nb_hour_sleep)  
            # game still in progress
            variables.game_in_progress = variables.actions["R"]["game_in_progress"]
            # update counters
            variables.counters["number_actions"]["value"] += 1
            return
        
        elif current_action == "O":
            # clear console
            if clear_console:
                utilities.clear_console()
            # print a little message
            print(variables.actions["O"]["message"])
            time.sleep(variables.message_speed)
            # open the backpack
            open_backpack()
            # game still in progress
            variables.game_in_progress = variables.actions["O"]["game_in_progress"]
            # update counters
            variables.counters["number_actions"]["value"] += 1
            return


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
            return

        elif current_action == "L" :
            if clear_console:
                utilities.clear_console()
            print ("*** Ladies Mode ***")
            print("Les 3 clés apparaissent dans ton sac.")
            print("Te voilà téléportée au pied de la mystérieuse porte...")
            variables.backpack["s"] = (variables.game_keys["s"])
            variables.backpack["g"] = (variables.game_keys["g"])
            variables.backpack["b"] = (variables.game_keys["b"])
            variables.avatar_position["x"] = 32
            variables.avatar_position["y"] = 6
            utilities.continue_or_exit()
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
        # put the item in the backpack
        variables.backpack[item] = (variables.items_available[item])
        # modify counter
        variables.counters["number_actions"]["value"] += 1
        # clear console
        if clear_console :
            utilities.clear_console()
        # print a little message
        print(f'\nVoilà {variables.items_available[item]["name"]} dans ton sac à dos !\n{variables.items_available[item]["message"]}\nRetour à la carte...')
        time.sleep(variables.message_speed)

    elif action_item == "U" :
        if clear_console :
            utilities.clear_console()
        # print a little message
        print("\nBonne idée !\n")
        # put item in the back pack to use it (not good, has to be modified)
        variables.backpack[item] = (variables.items_available[item])
        # use item
        use_item (item)
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
        print(f'- \u001b[4m{variables.backpack[item]["name"]}\u001b[0m qui te redonne \u001b[4m{variables.backpack[item]["value_hydration"]}\u001b[0m point(s) d hydratation et \u001b[4m{variables.backpack[item]["value_satiety"]}\u001b[0m point(s)de satiété.Tape \u001b[1m({variables.backpack[item]["symbol_items"]})\u001b[0m pour le sélectionner.')
    item_backpack_chosen = input(f"Quel objet veux-tu prendre ? ").lower()
    use_item (item_backpack_chosen)
    return 


def use_item (item, clear_console = True):
    if not variables.backpack[item]["drink"] and not variables.backpack[item]["eat"] and not variables.backpack[item]["blind"]:
        print(f'\n{variables.backpack[item]["message"]}')
        utilities.continue_or_exit()
    elif variables.backpack[item]["drink"] and not variables.backpack[item]["eat"] and not variables.backpack[item]["blind"] :
        print(f'\nTon avatar gagne {variables.backpack[item]["value_hydration"]} point(s) d hydratation.')
        if variables.backpack[item]["value_hydration"] != 0 :
            print("\nLa chance ! ")
            print(f'Avec {variables.backpack[item]["name"]}, tu gagnes aussi {variables.backpack[item]["value_satiety"]} point(s) de satiété.')
        utilities.continue_or_exit()
    elif not variables.backpack[item]["drink"] and variables.backpack[item]["eat"] and not variables.backpack[item]["blind"] :
        print(f'\nTon avatar gagne {variables.backpack[item]["value_satiety"]} point(s) de satiété.')
        if variables.backpack[item]["value_satiety"] != 0 :
            print("\nLa chance ! ")
            print(f'Avec {variables.backpack[item]["name"]}, tu gagnes aussi {variables.backpack[item]["value_hydration"]} point(s) d hydratation.')
        utilities.continue_or_exit()
    elif variables.backpack[item]["drink"] and variables.backpack[item]["eat"] and not variables.backpack[item]["blind"] :
        print("Il y a à boire et à manger avec ça !")
        print(f'\nTon avatar gagne {variables.backpack[item]["value_hydration"]} point(s) d hydratation et {variables.backpack[item]["value_satiety"]} point(s) de satiété.')
        utilities.continue_or_exit()
    elif variables.backpack[item]["blind"] :
        if clear_console :
            utilities.clear_console()
            print("\nQue se passe-t-il ????\n Tout s'assombrit... \nOMG ! Tu deviens aveugle...")
            utilities.show_image("eyes")
            time.sleep(10)
    # update counters, but not over the max value
    variables.counters["hydration"]["value"] += variables.backpack[item]["value_hydration"]
    if variables.counters["hydration"]["value"] > variables.counters["hydration"]["value_max"] :
        variables.counters["hydration"]["value"] = variables.counters["hydration"]["value_max"]
    variables.counters["satiety"]["value"] += variables.backpack[item]["value_satiety"]
    if variables.counters["satiety"]["value"] > variables.counters["satiety"]["value_max"]:
        variables.counters["satiety"]["value"] = variables.counters["satiety"]["value_max"]
    if variables.backpack[item]["drop_on_floor"]:
        # update backpack
        del variables.backpack[item]


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