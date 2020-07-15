import random
import variables
import utilities


def caesar_code (clear_console = True) :
    """
        plays the code caesar
    """

    if clear_console:
        utilities.clear_console()

    
    print("   Défi 2 :")
    print(" Le code César")
    print(" - - - - - - - ")
    print()

    # codes the sentence 
    # and shows it
    print("Voici le message incompréhensible figurant sur l'arche : ")
    get_coded_texte(variables.letter_code_random)
    print(variables.letter_code_random)

    print("Tu peux essayer de changer ce message en appuyant sur une des lettres figurant sur les colonnes de l'arche.")
    print()
    while variables.original_message != variables.coded_message :
        variables.letter_code_player = (input("Tape une lettre pour essayer de faire apparaître le message en clair : ")).upper()
        print("Le message sur l'arche se modifie.")
        print(f"En appuyant sur la lettre '{variables.letter_code_player}, tu as fait apparaître le message suivant :")
        print()
        get_coded_texte(variables.letter_code_player)
        if variables.original_message != variables.coded_message :
            
            print("Ca ne veut toujours rien dire !\n")
            test_other_letter = (input("Veux-tu essayer avec une autre lettre ? (O)ui ou (N)on : ")).upper()
            if test_other_letter == "O":
                variables.letter_code_player = (input("Tape une lettre pour essayer de faire apparaître le message en clair : ")).upper()
                print()
                print("Le message sur l'arche se modifie.")
                print(f"En appuyant sur la lettre '{variables.letter_code_player}, tu as fait apparaître le message suivant :")
                print()
                get_coded_texte(variables.letter_code_player)
            elif test_other_letter == "N" :
                test_name = (input("Veux-tu tenter maintenant d'écrire ton prénom en suivant le code césar ? (O)ui ou (N)on : ")).upper()
        print("fini ?")







    # while variables.nb_round_caesar != 5 :
    #     print()

    #     print()
    #     if len(letter_code_player) > 1 :
    #         get_coded_texte(letter_code_player)
    #     else :
    #         get_coded_texte(letter_code_player)




def get_coded_texte(letter_code, texte = variables.original_message):
    for index, element in enumerate(variables.alphabet):
        variables.number_code = (variables.alphabet).index(letter_code) + 1
    coded_message = []
    variables.original_message_list = (texte).split()
    for word in variables.original_message_list:
        liste_word = [""]
        for letter in word:
            if letter == ".":
                liste_word.append(".")
            else :
                current_index = (variables.alphabet).index(letter)
                new_index = current_index + variables.number_code
                if new_index > 25:
                    new_index -= 26
                liste_word.append(variables.alphabet[new_index])
        (coded_message).append("".join(liste_word))
    print(" ".join(coded_message))
    print()



# coded_name_try = input('Tape ton nom de joueur codé : ')

# and variables.coded_player_name != variables.coded_name_try 

# variables.coded_player_name = get_coded_texte(letter_code_player)


if __name__ == "__main__" :
    caesar_code()