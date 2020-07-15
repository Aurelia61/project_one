import variables
# import random
# import string
# def getPassword(length):
#     """Générer une chaîne aléatoire de longueur fixe"""
#     str = string.ascii_lowercase
#     return ''.join(random.choice(str) for i in range(length))
    
# print ("La chaine aleatoire est :", getPassword(8) )

letter_code = "E"
variables.original_message = "BEAUTIFUL BGEE. "

for index, element in enumerate(variables.alphabet):
    variables.number_code = (variables.alphabet).index(letter_code) + 1

variables.original_message = (variables.original_message).split()
print(variables.original_message)
for word in variables.original_message:
    liste_word = []
    for letter in word:
        if letter == ".":
            liste_word.append(".")
        else :
            current_index = (variables.alphabet).index(letter)
            new_index = current_index + variables.number_code
            if new_index > 25:
                new_index -= 26
            liste_word.append(variables.alphabet[new_index])
    (variables.coded_message).append("".join(liste_word))
print(" ".join(variables.coded_message))

