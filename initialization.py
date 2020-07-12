# coding: utf-8

# import modules

# additional modules
import game
import utilities


def show_title_and_story(clear_console = True ) :
    """
    Show the title and the story at the beginning.
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


#### demander au joueur s'il veut continuer !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    print("J'oubliais le principal...")
    print("La carte de l'île : ")
    print()
    game.load_map_from_file("map1")
    game.draw_map()
    print()
    print("Sauras-tu te déplacer en évitant les dangers de la jungle, des sables mouvants et des eaux profondes ?")
    print("A toi de jouer !")
    print()