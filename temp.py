import variables
import game


variables.action_choosen = input()


if variables.action_choosen == "Q":
    print(variables.actions["Q"]["message"])
    game_in_progress = variables.actions["Q"]["game_in_progress"]
    game.echec("Aurélia")