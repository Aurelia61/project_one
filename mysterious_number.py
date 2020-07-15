import random


player_number = ""
sphinx_number = ""

number_test_left = 20
round_left = 3

while number_test_left != 0 :
    if round_left != 0 and number_test_left != 0 or player_number != sphinx_number :
        sphinx_number = random.randint(1,100)
        player_number = int(input("\n--> Tapes un nombre entre 1 et 100 :  ")) 
        print(sphinx_number)
        while player_number != sphinx_number and number_test_left != 0 and round_left != 0:

            if player_number < sphinx_number :
                print("\n'Le nombre que j'ai en tête est plus \u001b[1mgrand\u001b[0m.'")
                number_test_left -= 1
                if number_test_left != 0 :
                    print(f'Il te reste encore {number_test_left} essais pour trouver le(s) {round_left} nombre(s) mystérieu(x) restant(s).\n')
                    player_number = int(input("\n--> Tapes un nombre entre 1 et 100 :  "))  
                else :
                    print(f'\nTu as utilisé tes 20 essais sans succès.\n Retentes ta chance. ')

            elif player_number > sphinx_number : 
                print("\nLe nombre que j'ai en tête est plus \u001b[1mpetit\u001b[0m.")
                number_test_left -= 1
                if number_test_left != 0 :
                    print(f'Il te reste encore {number_test_left} essais pour trouver le(s) {round_left} nombre(s) mystérieu(x) restant(s).\n')
                    player_number = int(input("\n--> Tapes un nombre entre 1 et 100 :  ")) 
                else :
                    print(f'\nTu as utilisé tes 20 essais sans succès.\n Retentes ta chance. ')
        if player_number == sphinx_number :
            print(f'\nBien joué ! Le nombre mystérieux est : {sphinx_number}.\n')
            number_test_left -= 1
            round_left -= 1
            if round_left != 0 :
                print(f'\nTu as encore {round_left} nombre(s) mystérieu(x) à trouver.\n' )
                print(f'Il te reste encore {number_test_left} essais pour trouver le(s) {round_left} nombre(s) mystérieu(x) restant(s).\n')
            elif round_left == 0 :
                print(f'!! Bravo !! Tu as trouvé les 3 nombres mystérieux en {20-number_test_left} essais !\nTu peux prendre la clé de bronze !')
                number_test_left = 0

# !!!!! Mettre la clé dans le sac à dos !!!!



