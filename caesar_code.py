import random
import variables

coded_name_try = ""
coded_player_name = ""

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def caesar_code (caesar_code_number = random.randint(1, 26), round_left = 5) :

    variables.coded_message = list(variables.original_message)

    while round_left != 0 and coded_player_name != coded_name_try :
        letter_test = input("Tape une lettre pour essayer de faire apparaître le message en clair : ")

        if not letter_test :
            print (variables.original_message)

        elif letter_test :






        coded_name_try = input('Tape ton nom de joueur codé : ')


    for index, element in enumerate(alphabet):
            print()
        

        print(index, element)
        print()

caesar_code()


