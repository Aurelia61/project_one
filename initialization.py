# coding: utf-8

# import modules

# additional modules
import game
import utilities
import variables


def show_map(clear_console = True) :
    """
    shows the map.
    """

    
    # if action_choosen == "C":
    #     if clear_console:
    #         utilities.clear_console()

    print(variables.actions["C"]["message"])
    
    print("Mais avant de commencer, tu dois répondre aux 2 questions suivantes :")
    variables.player_name= input("Quel est ton nom ? ")
    print()
    print("Quel symbole souhaites-tu pour ton avatar ?")         ##### !!! que le choix entre 1 ou 2... et si le joueur veut rajouter son propre symbole ???
    print("     - (F)ille : ♀ ")
    print("     - (G)arçon : ♂ ")
    letter_avatar_symbol = input("Choisis maintenant entre (F) ou (G) : ").upper()                
    print()

    if letter_avatar_symbol == "F":    
        variables.avatar_symbol_current = variables.avatar_symbol["F"]["symbol"]                                              #### trouver la solution ###############
        print(variables.avatar_symbol["F"]["message"])
    elif letter_avatar_symbol == "G":
        variables.avatar_symbol = variables.avatar_symbol["G"]["symbol"]
        print(variables.avatar_symbol["G"]["message"])
    else:
        variables.avatar_symbol = variables.avatar_symbol["N"]["symbol"]
        print(variables.avatar_symbol["N"]["message"])



    print("Alors ? C'est parti pour l'aventure ???")
    print()
    print("Oh ! Mais, j'oublie le principal...")
    print("...")
    print("La carte de l'île : ")
    print()
    print(f"--> Vois-tu où est ton avatar {variables.avatar_symbol_current} ?")
    print()

    game.load_map_from_file("map1")

    for Y in range(len(variables.map1)) :
        for X in range(len(variables.map1[Y])) :
            if (Y == variables.avatar_position["Y"] 
                and X == variables.avatar_position["X"]) :
                # if above is true, avatar is in this place, so draw it
                print(variables.avatar_symbol[letter_avatar_symbol]["symbol"], end="")
            else :
                # if not, draw the item of the map
                print(variables.map_elements[variables.map1[Y][X]]["image"], end="")
        print()

    print()
    print("Sauras-tu te déplacer en évitant les dangers de la jungle, des sables mouvants et des eaux profondes ?")    ##### Mettre les symbols
    print()

    print("Il est encore temps de quitter le jeu si tu as trop peur...")
    print()

    variables.action_choosen = input("Appuies sur (Q) pour quitter ou sur (C) pour continuer :").upper()          ##### même message    ↓↓↓↓  --> faire un dico ? 

    if variables.action_choosen == "Q":
        print(variables.actions["Q"]["message"])
        game_in_progress = variables.actions["Q"]["game_in_progress"]
        game.echec("Aurélia")

    elif variables.action_choosen != "C" or variables.action_choosen != "Q" :
        # if clear_console:
        #     utilities.clear_console()

        while variables.action_choosen != "C" and variables.action_choosen != "Q" :
            variables.action_choosen = "E"
            print(variables.actions["E"]["message"])
            action_choosen = input("Appuies sur (Q) pour quitter ou sur (C) pour continuer :").upper()   ##### même message    ↑↑↑↑  --> faire un dico ? 

    print("Découvres maintenant comment jouer !")



# def quit_game(clear_console = True) :
#     print("Il est encore temps de quitter le jeu si tu as trop peur...")
#     print()

#     action_choosen = input("Appuies sur (Q) pour quitter ou sur (C) pour continuer :").upper()          ##### même message    ↓↓↓↓  --> faire un dico ? 

#     if action_choosen != "C" or action_choosen != "Q" :
#         # if clear_console:
#         #     utilities.clear_console()

#         while action_choosen != "C" and action_choosen != "Q" :
#             action_choosen = "E"
#             print(variables.actions["E"]["message"])
#             action_choosen = input("Appuies sur (Q) pour quitter ou sur (C) pour continuer :").upper()   ##### même message    ↑↑↑↑  --> faire un dico ? 
    
#     elif action_choosen == "Q":
#         print(variables.actions["Q"]["message"])
#         game_in_progress = variables.actions["Q"]["game_in_progress"]
#         game.echec("Aurélia")

#     else:
#         game.draw_map()


def show_title_and_story(clear_console = True) :
    """
    shows the title and the story at the beginning.
    """

    if clear_console:
        utilities.clear_console()


    print("       Bienvenue à")
    print(" Python Mysterious Island !")
    print(" ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞ \n")
    print("Arriveras-tu à survivre pour découvrir le grand mystère caché au centre de l'ïle ?")
    print()
    print("Une seule manière de le savoir : L'ACTION !")
    print()
    print("Tu devras te déplacer pour rejoindre l'emplacement des 3 défis. ")             ##### Mettre les symbols
    print("Pour chaque défi relevé, tu gagneras une clé.")                         ##### Mettre les symbols
    print("A l'aide de ces 3 clés, tu pourras ouvrir la porte secrète cachée dans la montagne.")           ##### Mettre le symbol
    print()
    print("Mais attention...")
    print("Sur l'île, il fait chaud... ")
    print("Tu auras faim... ")
    print("Et l'épuisement ne sera jamais très loin...")
    print("Donc, prends soin de tes 3 signes vitaux !")                 ##### Mettre les symbols
    print()
    print("Dans cette aventure, tu as une sacoche avec un ordinateur et un système de recharge photovoltaïque.")
    print("Surprenant d'avoir ce type de matériel et du réseau ici, non ?")
    print("Tu découvriras bien assez tôt à quoi il te servira.")
    print()
    print("Heureusement, tu n'as pas que cette sacoche.")
    print()
    print("Tu as aussi un sac à dos.")                                ##### Mettre dessin ascii
    print("A l'intérieur, un petit couteau multifonctions de bonne facture.")
    print("Indispensable, pour l'aventurier que tu es.")
    print()
    print("Et une bouteille vide en verre.")                              ##### Mettre le symbol
    print("Tu réfléchis déjà où tu vas pouvoir aller la remplir ?")
    print("Je te donne mon premier conseil :")
    print("...attention à l'eau salée qui te rendra malade.")
    print()
    print("Je suis sûr que tu penses que ça ne fait pas beaucoup, alors que tu es sur une île inconnue...")
    print("A toi, de remplir ton sac à dos avec ce que tu trouveras sur ton chemin.")
    print()
    print("Seulement, ce n'est pas le sac de Mary Poppins.")
    print("Et tu ne pourras y mettre que 5 objets.")
    print("Mon deuxième conseil sera le suivant :")
    print("Méfies-toi de ce que tu mettras dans ton sac à dos...")
    print()
    
    print("Il est encore temps de quitter le jeu si tu as trop peur...")
    print()

    action_choosen = input("Appuies sur (Q) pour quitter ou sur (C) pour continuer :").upper()          ##### même message    ↓↓↓↓  --> faire un dico ? 

    if action_choosen != "C" or action_choosen != "Q" :
        # if clear_console:
        #     utilities.clear_console()

        while action_choosen != "C" and action_choosen != "Q" :
            action_choosen = "E"
            print(variables.actions["E"]["message"])
            action_choosen = input("Appuies sur (Q) pour quitter ou sur (C) pour continuer :").upper()   ##### même message    ↑↑↑↑  --> faire un dico ? 
    
    elif action_choosen == "Q":
        print(variables.actions["Q"]["message"])
        game_in_progress = variables.actions["Q"]["game_in_progress"]
        game.echec("Aurélia")



def show_rules(clear_console = True) :
    """
    shows the rules.
    """

    if clear_console:
        utilities.clear_console()

    if not variables.game_in_progress : 
        game.echec()
    
    print("   Les règles du jeu de")
    print(" Python Mysterious Island !")
    print(" ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞ ∞ \n")
    print()
    print("Objectifs ::")
    print("1- Récupérer les 3 clés situées dans les 3 lieux mystérieux.")
    print("2- Te rendre au 4e lieu mystérieux dans la montagne avec les 3 clés.")
    print()
    print("Règles particulières :")
    print("    - lorsque les objectifs ci-dessus sont remplis, la partie est gagnée")
    print("    - si ton avatar perd tous ses points de soif, la partie est perdue")
    print("    - si ton avatar perd tous ses points de faim, la partie est perdue")
    print("    - si ton avatar perd tous ses points de vie, la partie est perdue")
    print("    - les instructions doivent être séparées par un espace")
    print()
    print("Instructions comprises par l'avatar' :")
    print("    - le déplacer en choisissant sa direction :")
    print("          - vers le (H)aut de n cases (par exemple H2)")
    print("          - vers le (B)as de n cases (par exemple B6)")
    print("          - vers la (D)roite de n cases (par exemple D5)")
    print("          - vers la (G)auche de n cases (par exemple G1)")
    print("    - (P)rendre un objet et le mettre dans le sac à dos")
    print("    - (U)tiliser un object")
    print("    - (A)bandonner un object au sol")
    print("    - s'(H)ydrater pour augmenter ses points d'hydratation")
    print("    - (M)anger pour augmenter ses points de satiété")
    print("    - se (R)eposer pour récupérer des points de vie")
    print("    - (Q)uitter le jeu (et échouer)")
    



