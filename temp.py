import variables
import random
import multi_fizzbuzz

answers_without_good = ["Fizz", "Buzz", "FizzBuzz", "5"]
good_answer = "Fizz"

answers = []
all_answers = answers_without_good[:]
answers_without_good.remove(good_answer)
answers = all_answers
nb_players = len(variables.players_fizzbuzz)
nb_players_left = nb_players

# print(f" bonne réponse : {good_answer}")
# print(f" liste des mauvaises réponses : {answers_without_good}")
# print(f" liste de TOUTES les réponses : {all_answers}")




current_player = "monkey_1"









if __name__ == "__main__" :
    # for number in range (1,13):
    #     get_good_answer(number)

    get_answer_player ("monkey_1", multi_fizzbuzz.get_good_answer(3))
    