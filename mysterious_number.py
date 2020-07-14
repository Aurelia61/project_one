import random


player_number = ""
sphinx_number = ""

number_test_left = 20
round_left = 3

while number_test_left != 0 :
    if round_left != 0 and number_test_left != 0 or player_number != sphinx_number :
        sphinx_number = random.randint(1,100)
        player_number = int(input("\nTapes un nombre entre 1 et 100 :  ")) 
        print(sphinx_number)
        while player_number != sphinx_number :

            if player_number < sphinx_number :
                print("\nLe nombre que j'ai en tête est plus \u001b[1mgrand\u001b[0m.\n")
                number_test_left -= 1
                print(f'Il te reste encore {number_test_left} essais pour trouver le(s) {round_left} nombre(s) mystérieu(x) restant(s).\n')
                
                player_number = int(input("\nTapes un nombre entre 1 et 100 :  "))  

            elif player_number > sphinx_number : 
                print("\nLe nombre que j'ai en tête est plus \u001b[1mpetit\u001b[0m.\n")
                print(f'Il te reste encore {number_test_left} essais pour trouver le(s) {round_left} nombre(s) mystérieu(x) restant(s).\n')
                number_test_left -= 1
                player_number = int(input("\nTapes un nombre entre 1 et 100 :  ")) 
                
            
        print(f'\nBien joué ! Le nombre mystérieux est : {sphinx_number}.\n')
        number_test_left -= 1
        round_left -= 1
        if round_left != 0 :
            print(f'\nTu as encore {round_left} nombre(s) mystérieu(x) à trouver.\n' )
            print(f'Il te reste encore {number_test_left} essais pour trouver le(s) {round_left} nombre(s) mystérieu(x) restant(s).\n')
        else:
            print(f'Bravo tu as trouvé les 3 nombres mystérieux en {20-number_test_left} essais !')
    print(f'Tu as utilisé tes {number_test_left} essais sans succès.\n Retentes ta chance. ')




# try_again_or_not()




print("tu as le droit à encore {3} essais")