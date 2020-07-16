
# answers = ["Fizz", "Buzz", "FizzBuzz", "5"]
# good_answer = "Fizz"
# bad_answers = list(answers).remove(good_answer)
# print(bad_answers)
# print(answers)

# answers = ["Fizz", "Buzz", "FizzBuzz", "5"]
# good_answer = "Fizz"
# bad_answers = []
# answers_all = answers[:]
# answers.remove(good_answer)
# bad_answers = answers_all
# print(good_answer)
# print(bad_answers)
# print(answers)

answers_without_good = ["Fizz", "Buzz", "FizzBuzz", "5"]
good_answer = "Fizz"

answers = []
all_answers = answers_without_good[:]
answers_without_good.remove(good_answer)
answers = all_answers
print(f" bonne réponse : {good_answer}")
print(f" liste des mauvaises réponses : {answers_without_good}")
print(f" liste de TOUTES les réponses : {all_answers}")