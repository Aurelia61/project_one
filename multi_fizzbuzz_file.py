# coding: utf-8

# import modules
import random
import time

# additional modules
import variables
import utilities
import game


# à enregister dans variables si variable globale !!!



def get_possible_answers (index_def, good_answer_def) :
    """
        get all the possible answers
    """

    answers_without_good = ["Fizz", "Buzz", "FizzBuzz",]      # à mettre dans variables                      

    answers = []
    all_answers = answers_without_good[:]
    if type(good_answer_def) != int  :
        answers_without_good.remove(good_answer_def)
        answers = all_answers
        answers_without_good.append(index_def)
    return answers_without_good


def multi_fizzbuzz_play (clear_console = True) :
    """
        plays the multi_fizzbuzz
    """

    if clear_console:
        utilities.clear_console()
        
    # the player can't play if he has already the gold key
    if "g" in variables.backpack.keys() :
        print("Tu as déjà cette clé.")
        time.sleep(variables.message_speed)
        return
    
    print("      Défi 3 :")
    print(" Le multi FizzBuzz")
    print(" - - - - - - - - - ")
    print()

    keys_players = variables.players_fizzbuzz.keys()
    list_players = list(keys_players)
    nb_players = len(list_players)
    nb_players_left = nb_players
    index = 1


    while nb_players_left > 2:
        
        for player in list_players :
            print()
            good_answer = get_good_answer(index)
            answer_player = get_answer_player(player, good_answer, index)
            if answer_player != good_answer and player != "avatar" :
                print(f'{(variables.players_fizzbuzz[player]["name_monkey"]).capitalize()} a perdu !')
                list_players.remove(player)
                index = 1
                nb_players_left -= 1
                print(f'Il y a encore {len(list_players)} joueurs.')
                time.sleep(variables.fizz_speed)
            elif answer_player != good_answer and player == "avatar" :
                print("-->\u001b[1mTu as perdu !\u001b[0m\nRetente ta chance plus tard.")
                utilities.continue_or_exit()
                game.show_dashboard()
                print()
                return
            elif answer_player == good_answer and player == "avatar" :
                print("\u001b[1mBien joué !\u001b[0m")
                index += 1
                time.sleep(2)
            elif answer_player == good_answer and player != "avatar" :
                index += 1
                time.sleep(2)
    while nb_players_left == 2 :
        for player in list_players :
            print()
            good_answer = get_good_answer(index)
            answer_player = get_answer_player(player, good_answer, index)
            if answer_player != good_answer and player != "avatar":
                print(f'{(variables.players_fizzbuzz[player]["name_monkey"]).capitalize()} a perdu !')
                time.sleep(variables.fizz_speed)
                list_players.remove(player)
                nb_players_left -= 1
            elif answer_player != good_answer and player == "avatar" :
                print("-->\u001b[1mTu as perdu !\u001b[0m\nRetente ta chance. Tu as été jusqu'en finale !")
                utilities.continue_or_exit()
                game.show_dashboard()
                print()
                return
            elif answer_player == good_answer and player == "avatar" :
                print("\u001b[1mBien joué !\u001b[0m")
                index += 1
                time.sleep(2)
            elif answer_player == good_answer and player != "avatar" :
                index += 1
                time.sleep(2)
    if nb_players_left == 1 :
        for player in list_players :
            winner = player 
            print(f'\n{(variables.players_fizzbuzz[winner]["name_monkey"]).capitalize()}, tu as gagné !')
            print("-->\u001b[1mTu obtiens la clé d'or !\u001b[0m\n")
            # put the key in the backpack
            variables.backpack["g"] = (variables.game_keys["g"])
            # continue or exit
            utilities.continue_or_exit()
            game.show_dashboard()
            print()
            return


def get_good_answer(given_number):

    fizz = not given_number % 3
    buzz = not given_number % 5

    if fizz and buzz :
        good_answer = "FizzBuzz"
    elif fizz:
        good_answer = "Fizz"
    elif buzz:
        good_answer = "Buzz"
    else:
        good_answer = given_number
    return good_answer
    

def get_answer_player (current_player, good_answer_def, index_def) :
    """
        gets answer of the player
    """

    value_percentage = variables.players_fizzbuzz[current_player]["chance"]
    answer_for_percentages = [good_answer_def, "faux"]
    percentages = [value_percentage/100, 1-(value_percentage/100)]
    good_or_bad = random.choices(answer_for_percentages, percentages)
    if good_answer_def in good_or_bad :
        player_answer = good_answer_def
        print(f'{(variables.players_fizzbuzz[current_player]["name_monkey"]).capitalize()} dit "{player_answer}" !')
        time.sleep(2)
    else:
        answers_without_good = get_possible_answers(index_def, good_answer_def)
        player_answer = random.choice(answers_without_good)
        print(f'{(variables.players_fizzbuzz[current_player]["name_monkey"]).capitalize()} dit "{player_answer}" !')
        time.sleep(2)
    return player_answer




if __name__ == "__main__" :
    # get_good_answer(3)
    # print(good_answer)
    variables.players_fizzbuzz["avatar"]["name_monkey"] = "joueur"
    multi_fizzbuzz_play()