# coding: utf-8

# import modules
import random

# additional modules
import variables
import utilities



def mysterious_number (number_test_left = 20, round_left = 3, clear_console = True) :
    
    if clear_console:
        utilities.clear_console()
    
    # number_test_left = 20
    # round_left = 3
    
    print("       Défi 1 :")
    print(" Le nombre mystérieux")
    print("   - - - - - - - - -  ")
    print()
    print("Trouve les 3 nombres mystérieux du Sphinx pour gagner la clé de bronze.")

    while number_test_left != 0 :
        if round_left != 0 and number_test_left != 0 or variables.player_number != variables.sphinx_number :
            variables.sphinx_number = random.randint(1,100)
            variables.player_number = int(input("\n--> Tape un nombre entre 1 et 100 :  ")) 
            # print(sphinx_number)
            while variables.player_number != variables.sphinx_number and number_test_left != 0 and round_left != 0:

                if variables.player_number < variables.sphinx_number :
                    print("\n'Le nombre que j'ai en tête est plus \u001b[1mgrand\u001b[0m.'")
                    number_test_left -= 1
                    if number_test_left != 0 :
                        print(f'Il te reste encore {number_test_left} essais pour trouver le(s) {round_left} nombre(s) mystérieu(x) restant(s).\n')
                        variables.player_number = int(input("\n--> Tape un nombre entre 1 et 100 :  "))  
                    else :
                        print(f'\nTu as utilisé tes 20 essais sans succès.\n Retentes ta chance. ')

                elif variables.player_number > variables.sphinx_number : 
                    print("\nLe nombre que j'ai en tête est plus \u001b[1mpetit\u001b[0m.")
                    number_test_left -= 1
                    if number_test_left != 0 :
                        print(f'Il te reste encore {number_test_left} essais pour trouver le(s) {round_left} nombre(s) mystérieu(x) restant(s).\n')
                        variables.player_number = int(input("\n--> Tape un nombre entre 1 et 100 :  ")) 
                    else :
                        print(f'\nTu as utilisé tes 20 essais sans succès.\n Retentes ta chance. ')
            if variables.player_number == variables.sphinx_number :
                print()
                print("\u001b[1m Bien joué ! \u001b[0m" + f"Le nombre mystérieux est : {variables.sphinx_number}.")
                print()
                number_test_left -= 1
                round_left -= 1
                if round_left != 0 :
                    print(f'\nTu as encore {round_left} nombre(s) mystérieu(x) à trouver.\n' )
                    print(f'Il te reste encore {number_test_left} essais pour trouver le(s) {round_left} nombre(s) mystérieu(x) restant(s).\n')
                elif round_left == 0 :
                    print(f'!! Bravo !! \nTu as trouvé les 3 nombres mystérieux en {20-number_test_left} essais !\n')
                    print("\u001b[1mTu peux prendre la clé de bronze !\u001b[0m\n")
                    number_test_left = 0
    print()




# !!!!! Mettre la clé dans le sac à dos !!!!


if __name__ == "__main__" :
    mysterious_number () 
