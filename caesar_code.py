import random
import variables
import utilities

coded_name_try = ""
coded_player_name = ""

letter_code = ""
number_code = ""

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
original_message = "BEAUTIFUL IS BETTER THAN UGLY. EXPLICIT IS BETTER THAN IMPLICIT. SIMPLE IS BETTER THAN COMPLEX."
coded_message = ""

def caesar_code (caesar_code_number = random.randint(1, 26), round_left = 5, clear_console = True) :

    if clear_console:
        utilities.clear_console()

    # show coded message depend on letter input
    letter_code = (input("Tape une lettre pour essayer de faire apparaître le message en clair : ")).upper()
    for index, element in enumerate(alphabet):
        number_code = alphabet.index(letter_code) + 1
            
    original_message = "BEAUTIFUL IS BETTER THAN UGLY. EXPLICIT IS BETTER THAN IMPLICIT. SIMPLE IS BETTER THAN COMPLEX."
    coded_message = []
    original_message = original_message.split()
    for word in original_message:
        liste_word = []
        for letter in word:
            if letter == ".":
                liste_word.append(".")
            else :
                i = alphabet.index(letter)
                if i + number_code > 25:
                    i -= 26
                liste_word.append(alphabet[i+number_code])
        coded_message.append("".join(liste_word))
    print(" ".join(coded_message))



    # variables.coded_message = list(variables.original_message)

    # while round_left != 0 and coded_player_name != coded_name_try :
    #     letter_test = input("Tape une lettre pour essayer de faire apparaître le message en clair : ")







        # coded_name_try = input('Tape ton nom de joueur codé : ')




caesar_code()


