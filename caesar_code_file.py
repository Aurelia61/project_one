# coding: utf-8

# import modules
import random

# additional modules
import variables
import utilities
import game


def caesar_code_play (clear_console = True) :
    """
        plays the code caesar
    """

    if clear_console:
        utilities.clear_console()
    
    
    print("   Défi 2 :")
    print(" Le code César")
    print(" - - - - - - - ")
    print()

    # the player can't play if he has already the sliver key
    if "s" in variables.backpack.keys() :
        print("Tu as déjà cette clé.")
        time.sleep(variables.message_speed)
        return

    # codes the sentence 
    # and shows it
    print("Voici le message incompréhensible figurant sur l'arche : ")
    print(get_coded_texte(variables.letter_code_random, variables.original_message))
    print(variables.letter_code_random)
    print()
    print("Tu peux essayer de changer ce message en appuyant sur une des lettres figurant sur les colonnes de l'arche.")
    
    
    print()
    letter_code_player = (input("--> Tape une lettre pour essayer de faire apparaître le message en clair : ")).upper()
    print("\nLe message sur l'arche se modifie...")
    print("...")
    print(f"En appuyant sur la lettre {letter_code_player}, tu as fait apparaître le message suivant :")
    while letter_code_player != variables.letter_code_random :
        print(get_coded_texte(letter_code_player, variables.original_message))
        print("\nCa ne veut toujours rien dire !\n")
        test_other_letter = (input("Veux-tu essayer avec une autre lettre ? (O)ui ou (N)on : ")).upper()
        if test_other_letter == "O":
            print()
            letter_code_player = (input("--> Tape une lettre pour essayer de faire apparaître le message en clair : ")).upper()
            print()
            print("Le message sur l'arche se modifie...")
            print("...")
            print(f"En appuyant sur la lettre {letter_code_player}, tu as fait apparaître le message suivant :")
            if letter_code_player == variables.letter_code_random :
                print(decrypt_texte(letter_code_player, get_coded_texte(letter_code_player, variables.original_message)))
                print()
                count_letter = variables.number_code + 1
                print(f"Bravo ! Tu sais maintenant que la clé du code César est la lettre {variables.letter_code_random}.\n Il faut décaler chaque lettre de {count_letter} lettres dans l'alphabet.")
                print()
                test_name = (input("Veux-tu tenter maintenant d'écrire ton prénom en suivant le code césar ? (O)ui ou (N)on : ")).upper()
                if test_name == "O" :
                    test_coded_name()
                else :
                    utilities.continue_or_exit()
                    game.show_dashboard()
                    return
            elif letter_code_player != variables.letter_code_random :
                get_coded_texte(letter_code_player, variables.original_message)
                print()
        elif test_other_letter == "N" :
            test_name = (input("Veux-tu tenter maintenant d'écrire ton prénom en suivant le code césar ? (O)ui ou (N)on : ")).upper()
            if test_name == "O" :
                test_coded_name()
            else :
                utilities.continue_or_exit()
                game.show_dashboard()
                return

    print(decrypt_texte(letter_code_player, get_coded_texte(letter_code_player, variables.original_message)))
    print()
    count_letter = variables.number_code + 1
    print(f"Bravo ! Tu sais maintenant que la clé du code César est la lettre {variables.letter_code_random}.\n Il faut décaler chaque lettre de {count_letter} lettres dans l'alphabet.")
    print()
    test_name = (input("Veux-tu tenter maintenant d'écrire ton prénom en suivant le code césar ? (O)ui ou (N)on : ")).upper()
    if test_name == "O" :
        test_coded_name()
    else :
        utilities.continue_or_exit()
        game.show_dashboard()
        return
    utilities.continue_or_exit()
    game.show_dashboard()
    print()
    return


def test_coded_name():
    """
        tests the name coded by the player
    """

    message = get_coded_texte(variables.letter_code_random, variables.player_name.upper())
    print(message)
    print()
    coded_name_try = (input('--> Tape ton nom de joueur codé : ')).upper()
    decrypted_name = decrypt_texte(variables.letter_code_random, coded_name_try)
    variables.nb_round_caesar += 1
    if decrypted_name != variables.player_name.upper() and variables.nb_round_caesar != 5  :
        while variables.nb_round_caesar < 5  :
            print(f'{decrypted_name}, est-ce ton prénom ?')
            print("Non... Ce n'est pas le bon cryptage...\n Essais à nouveau.\n")
            coded_name_try = (input('--> Tape ton nom de joueur crypté : ')).upper()
            decrypted_name = decrypt_texte(variables.letter_code_random, coded_name_try)
            variables.nb_round_caesar += 1
        if variables.nb_round_caesar == 5 :
            print(f'{decrypted_name}, est-ce ton prénom ?')
            print("Non... Ce n'est toujours pas le bon cryptage...\n")
            print("Tu as utilisé tes 5 essais.\nRetente ta chance plus tard.\n")
            return
    elif decrypted_name == variables.player_name.upper() and variables.nb_round_caesar <= 5 :
        print(f'{decrypted_name}, est-ce ton prénom ?')
        print("Oui ! Bravo ! Tu as réussi à crypter ton nom !\n")
        print("\u001b[1mTu obtiens la clé d'argent !\u001b[0m\n")
        # put the key in the backpack
        variables.backpack["s"] = (variables.game_keys["s"])
        print()
    return


def get_coded_texte(letter_code, texte): # texte = variables.original_message
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
    variables.player_name = "FREDO"
    caesar_code_play()
    # get_coded_texte("F")