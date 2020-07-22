# coding: utf-8

# import modules
import random

# additional modules
import variables
import utilities
import game


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
    print(get_coded_texte(variables.letter_code_random))
    print(variables.letter_code_random)
    print()
    print("Tu peux essayer de changer ce message en appuyant sur une des lettres figurant sur les colonnes de l'arche.")
    
    
    print()
    letter_code_player = (input("--> Tape une lettre pour essayer de faire apparaître le message en clair : ")).upper()
    print("\nLe message sur l'arche se modifie...")
    print("...")
    print(f"En appuyant sur la lettre {letter_code_player}, tu as fait apparaître le message suivant :")
    while letter_code_player != variables.letter_code_random :
        print(get_coded_texte(letter_code_player))
        print("\nCa ne veut toujours rien dire !\n")
        test_other_letter = (input("Veux-tu essayer avec une autre lettre ? (O)ui ou (N)on : ")).upper()
        if test_other_letter == "O":
            print()
            letter_code_player = (input("--> Tape une lettre pour essayer de faire apparaître le message en clair : ")).upper()
            print()
            print("Le message sur l'arche se modifie...")
            print("...")
            print(f"En appuyant sur la lettre {letter_code_player}, tu as fait apparaître le message suivant :")
            get_coded_texte(letter_code_player)
            decrypt_texte(letter_code_player, get_coded_texte(letter_code_player))
            if letter_code_player == variables.letter_code_random :
                print()
                print(f"Bravo ! Tu sais maintenant que la clé du code César est la lettre {variables.letter_code_random}.\n Il faut décaler chaque lettre de {variables.number_code} lettres dans l'alphabet.")
                print()
                test_name = (input("Veux-tu tenter maintenant d'écrire ton prénom en suivant le code césar ? (O)ui ou (N)on : ")).upper()
                if test_name == "O" :
                    test_coded_name()
                else :
                    return

        elif test_other_letter == "N" :
            test_name = (input("Veux-tu tenter maintenant d'écrire ton prénom en suivant le code césar ? (O)ui ou (N)on : ")).upper()
            if test_name == "O" :
                test_coded_name()
                
            else :
                return
    
    print(decrypt_texte(letter_code_player, get_coded_texte(letter_code_player)))
    print(f"Bravo ! Tu sais maintenant que la clé du code César est la lettre {variables.letter_code_random}.\n Il faut reculer chaque lettre de {variables.number_code} lettres dans l'alphabet.")
    print()
    test_name = (input("Veux-tu tenter maintenant d'écrire ton prénom en suivant le code césar ? (O)ui ou (N)on : ")).upper()
    if test_name == "O" :
        test_coded_name()
    else :
        return


def test_coded_name():
    """
        tests the name coded by the player
    """

    print()

    coded_name_try = (input('--> Tape ton nom de joueur codé : ')).upper()
    decrypted_name = decrypt_texte(variables.letter_code_random, coded_name_try)
    variables.nb_round_caesar += 1
    if decrypted_name != variables.player_name and variables.nb_round_caesar != 5  :
        while variables.nb_round_caesar < 5  :
            print(decrypted_name)
            print("Ce n'est pas le bon cryptage...\n Essais à nouveau.\n")
            coded_name_try = (input('--> Tape ton nom de joueur crypté : ')).upper()
            decrypted_name = decrypt_texte(variables.letter_code_random, coded_name_try)
            variables.nb_round_caesar += 1
        variables.nb_round_caesar = 5
        print("Tu as utilisé tes 5 essais.\nRetente ta chance plus tard.")
        return
    elif decrypted_name == variables.player_name and variables.nb_round_caesar <= 5 :
        print(decrypted_name)
        print("Bravo ! Tu as réussi à crypter ton nom !\n")
        print("\u001b[2mTu peux prendre la clé d'argent !\u001b[0m\n")
        
        print()
    return



# and variables.coded_player_name != variables.coded_name_try 

# variables.coded_player_name = get_coded_texte(letter_code_player)


def get_coded_texte(letter_code, texte = variables.original_message):
    for index, element in enumerate(variables.alphabet):
        variables.number_code = (variables.alphabet).index(letter_code)
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
    coded_message = " ".join(coded_message)
    return coded_message


def decrypt_texte(letter_code, texte) :
    for index, element in enumerate(variables.alphabet):
        variables.number_code = (variables.alphabet).index(letter_code)
    coded_message = []
    variables.original_message_list = (texte).split()
    for word in variables.original_message_list:
        liste_word = [""]
        for letter in word:
            if letter == ".":
                liste_word.append(".")
            else :
                current_index = (variables.alphabet).index(letter)
                new_index = current_index - variables.number_code
                if new_index > 25:
                    new_index -= 26
                liste_word.append(variables.alphabet[new_index])
        (coded_message).append("".join(liste_word))
    coded_message = " ".join(coded_message)
    return coded_message


if __name__ == "__main__" :
    caesar_code()
    # get_coded_texte("F")