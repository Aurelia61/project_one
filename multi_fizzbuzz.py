import random
import variables
import utilities
import game

# à enregister dans variables si variable globale !!!


def get_possible_answers (index_def, good_answer_def) :
    answers_without_good = ["Fizz", "Buzz", "FizzBuzz",]      # à mettre dans variables                      

    answers = []
    all_answers = answers_without_good[:]
    answers_without_good.remove(good_answer_def)
    answers = all_answers
    answers_without_good.append(index_def)
    return (all_answers, answers_without_good)





def multi_fizzbuzz (clear_console = True) :
    """
        plays the multi_fizzbuzz
    """

    if clear_console:
        utilities.clear_console()

    
    print("      Défi 3 :")
    print(" Le multi FizzBuzz")
    print(" - - - - - - - - - ")
    print()

    list_players = variables.players_fizzbuzz.keys()
    nb_players = len(list_players)
    nb_players_left = nb_players


    while nb_players_left > 1:

        for player in variables.players_fizzbuzz :
            index = 1
            good_answer = get_good_answer(index)
            answer_player = get_answer_player(player, good_answer, index)
            if answer_player != good_answer :
                print("Le joueur a perdu !")
                del list_players[player]
            else:
                continue
            index += 1
            










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
        print(f'{variables.players_fizzbuzz[current_player]["name_monkey"]} dit "{player_answer}" !')
    else:
        answers_without_good = get_possible_answers(index_def, good_answer_def)
        player_answer = "".join(random.choices(answers_without_good))
        print(f'{variables.players_fizzbuzz[current_player]["name_monkey"]} dit "{player_answer}" !')
    return player_answer




if __name__ == "__main__" :
    # get_good_answer(3)
    # print(good_answer)
    multi_fizzbuzz()