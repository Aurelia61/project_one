import variables
import random

answers_without_good = ["Fizz", "Buzz", "FizzBuzz", "5"]
good_answer = "Fizz"

answers = []
# print(f" liste des mauvaises réponses : {answers}")
# print(f" liste de TOUTES les réponses : {answers_without_good}")
print()
all_answers = answers_without_good[:]
print(f" liste de all_answers : {all_answers}")
print(f" liste des réponses : {answers_without_good}")
print()
answers_without_good.remove(good_answer)
print(f" bonne réponse : {good_answer}")
print(f" liste de all_answers : {all_answers}")
print(f" liste des réponses fausses : {answers_without_good}")
print()
answers = all_answers
print(f" bonne réponse : {good_answer}")
print(f" liste des mauvaises réponses : {answers_without_good}")
print(f" liste de TOUTES les réponses : {all_answers}")


current_player = "monkey_1"

value_percentage = variables.players_fizzbuzz[current_player]["chance"]

answer_for_percentages = [good_answer, "faux"]
percentages = [value_percentage/100, 1-(value_percentage/100)]

good_or_bad = random.choices(answer_for_percentages, percentages)

if good_answer in good_or_bad :
    print(good_answer)
else:
    bad_answer = "".join(random.choices(answers_without_good))
    print(bad_answer)


