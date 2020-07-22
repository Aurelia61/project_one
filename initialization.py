# coding: utf-8

# import modules

# additional modules
import game
import utilities
import variables



def show_title_and_story(clear_console = True) :
    """
        shows the title and the story at the beginning.
    """

    if clear_console:
        utilities.clear_console()

    print("       Bienvenue à")
    print(" Python Mysterious Island !")
    print(" - - - - - - - - - - - - - \n")
    print("Arriveras-tu à survivre pour découvrir le grand mystère caché au centre de l'ïle ?")
    print()
    print("Une seule manière de le savoir : L'ACTION !")
    print()
    print("Tu devras te déplacer pour rejoindre l'emplacement des 3 défis. ")             ##### Mettre les symbols
    print("Pour chaque défi relevé, tu gagneras une clé.")                         ##### Mettre les symbols
    print("À l'aide de ces 3 clés, tu pourras ouvrir la porte secrète cachée dans la montagne.")           ##### Mettre le symbol
    print()
    print("Mais attention...")
    print("Sur l'île, il fait chaud... ")
    print("Tu auras faim... ")
    print("Et l'épuisement ne sera jamais très loin...")
    print("Donc, prends soin de tes 3 signes vitaux !")                 ##### Mettre les symbols
    print()
    print("Dans cette aventure, tu as une malette avec un ordinateur et un système de recharge photovoltaïque.")
    print("Surprenant d'avoir ce type de matériel et du réseau ici, non ?")
    print("Tu découvriras bien assez tôt à quoi il te servira.")
    print()
    print("Heureusement, tu n'as pas que cette malette.")
    print()
    print("Tu as aussi un sac à dos.")                                ##### Mettre dessin ascii
    print("À l'intérieur, un petit couteau multifonctions de bonne facture.")
    print("Indispensable, pour l'aventurier.e que tu es.")
    print()
    print("Et une bouteille vide en verre.")                              ##### Mettre le symbol
    print("Tu réfléchis déjà où tu vas pouvoir aller la remplir ?")
    print("Je te donne mon premier conseil :")
    print("...attention à l'eau salée qui te rendra malade.")
    print()
    print("C'est bien léger pour survivre sur cette île inconnue...")
    print("À toi de remplir ton sac à dos avec ce que tu trouveras sur ton chemin.")
    print()
    print("Seulement, ce n'est pas le sac de Mary Poppins.")
    print("Et tu ne pourras y mettre que 5 objets.")
    print("Mon deuxième conseil sera le suivant :")
    print("Méfies-toi de ce que tu mettras dans ton sac à dos...")
    print()
    print("Il est encore temps de quitter le jeu si tu as trop peur...")
        
    game.continue_or_exit()


def get_name_and_symbol(clear_console = True):
    """ 
        gets the name of the player 
        asks which symbol she/he wants for her/his avatar
    """

    while variables.game_in_progress :
        print("Mais avant de commencer, tu dois répondre aux 2 questions suivantes :")
        variables.player_name = input("Quel est ton nom ? ").capitalize()
        print()
        print(f"Bienvenue {variables.player_name} !")
        print()
        print("Quel symbole souhaites-tu pour ton avatar ?")         ##### !!! que le choix entre 1 ou 2... et si le joueur veut rajouter son propre symbole ???
        print(f'     - (L)ady: {variables.avatar_symbol["L"]["color_start"]}{variables.avatar_symbol["L"]["symbol"]}{variables.avatar_symbol["L"]["color_end"]} ')
        print(f'     - (K)night : {variables.avatar_symbol["K"]["color_start"]}{variables.avatar_symbol["K"]["symbol"]}{variables.avatar_symbol["K"]["color_end"]} ')
        print(f'     - (N)o One : {variables.avatar_symbol["N"]["color_start"]}{variables.avatar_symbol["N"]["symbol"]}{variables.avatar_symbol["N"]["color_end"]} ')
        variables.letter_avatar_symbol = input(f"Choisis maintenant entre {variables.possibles_avatar_symbol} : ").upper()                
        print()
        
        if clear_console:
            utilities.clear_console()

        print()
        if variables.letter_avatar_symbol == "L":    
            variables.avatar_symbol_current = variables.avatar_symbol["L"]["color_start"]+variables.avatar_symbol["L"]["symbol"]+variables.avatar_symbol["L"]["color_end"]                                             #### trouver la solution ###############
            print(variables.avatar_symbol["L"]["message"])
        elif variables.letter_avatar_symbol == "K":
            variables.avatar_symbol_current = variables.avatar_symbol["K"]["color_start"]+variables.avatar_symbol["K"]["symbol"]+variables.avatar_symbol["K"]["color_end"]
            print(variables.avatar_symbol["K"]["message"])
        elif variables.letter_avatar_symbol != "L" and variables.letter_avatar_symbol != "K":
            variables.letter_avatar_symbol = "N"
            variables.avatar_symbol_current = variables.avatar_symbol["N"]["color_start"]+variables.avatar_symbol["N"]["symbol"]+variables.avatar_symbol["N"]["color_end"]
            print(variables.avatar_symbol["N"]["message"])
        return
    return variables.avatar_symbol_current


def show_map_initial(clear_console = True) :
    """
    shows the map.
    """
    while variables.game_in_progress :
        
        utilities.get_text_place_symbol()

        print()
        print("Oh ! Mais, j'oublie le principal...")
        print("Dans la malette, tu as aussi une carte de l'île : ")
        print()
        print(f'Vois-tu où est ton avatar ? \n --> {variables.avatar_symbol[variables.letter_avatar_symbol]["color_start"]}{variables.avatar_symbol[variables.letter_avatar_symbol]["symbol"]}{variables.avatar_symbol[variables.letter_avatar_symbol]["color_end"]}')     
        print(f'Prends note également où se trouvent les 3 défis et la porte mystérieuse : \n --> {variables.text_place_symbol}')
        print()

        utilities.load_map_from_file("map1")

        for Y in range(len(variables.map1)) :
            for X in range(len(variables.map1[Y])) :
                if variables.map1[Y][X] in variables.avatar_symbol.keys() :
                    # if above is true, avatar is in this place, so draw it
                    print(f'{variables.avatar_symbol[variables.letter_avatar_symbol]["color_start"]}{variables.avatar_symbol[variables.letter_avatar_symbol]["symbol"]}{variables.avatar_symbol[variables.letter_avatar_symbol]["color_end"]}', end="")  
                elif variables.map1[Y][X] in variables.place.keys() :
                    print(f'{variables.place[variables.map1[Y][X]]["color_start"]}{variables.place[variables.map1[Y][X]]["image"]}{variables.place[variables.map1[Y][X]]["color_end"]}', end="")
                else :
                    # if not, draw the item of the map
                    print(f'{variables.map_elements[variables.map1[Y][X]]["color_start"]}{variables.map_elements[variables.map1[Y][X]]["image"]}{variables.map_elements[variables.map1[Y][X]]["color_end"]}', end="" )
            print()

        print()
        print(f'Sauras-tu te déplacer en évitant les dangers de la jungle {variables.map_elements["J"]["color_start"]}{variables.map_elements["J"]["image"]}{variables.map_elements["J"]["color_end"]}, des sables mouvants {variables.map_elements["v"]["color_start"]}{variables.map_elements["v"]["image"]}{variables.map_elements["v"]["color_end"]} et de la rivière {variables.map_elements["u"]["color_start"]}{variables.map_elements["u"]["image"]}{variables.map_elements["u"]["color_end"]}  ?')    ##### Mettre les symbols
        print()
        print("Découvres maintenant comment jouer !")

        game.continue_or_exit()

        return              # A vérifier si toujours utile, car normalement la boucle while doit s'arrêter !!



def show_rules(clear_console = True) :
    """
    shows the rules.
    """
    while variables.game_in_progress :
        if clear_console:
            utilities.clear_console()
    
        print("   Les règles du jeu de")
        print(" Python Mysterious Island !")
        print(" - - - - - - - - - - - - - ")
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
        print("Instructions comprises par l'avatar :")
        print("    - le déplacer en choisissant sa direction :")
        print("          - vers le (H)aut")                                        #  de n cases (par exemple H2)
        print("          - vers le (B)as")                                         #  de n cases (par exemple B6)
        print("          - vers la (D)roite")                                      #  de n cases (par exemple D5)
        print("          - vers la (G)auche")                                      #  de n cases (par exemple G1)
        print("    - (P)rendre un objet et le mettre dans le sac à dos")
        print("    - (U)tiliser un object")
        print("    - (A)bandonner un object au sol")
        print("    - s'h(Y)drater pour augmenter ses points d'hydratation")
        print("    - (M)anger pour augmenter ses points de satiété")
        print("    - se (R)eposer pour récupérer des points de vie")
        print("    - (S)auvegarder la partie")
        print("    - (T)élécharger la partie")
        print("    - (Q)uitter le jeu (et échouer)")
        print()
        
        game.continue_or_exit()
        
        return                 # A vérifier si toujours utile, car normalement la boucle while doit s'arrêter !!
    



