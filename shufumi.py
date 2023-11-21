import random

def user_choice():
    while True:
        player : str = input("pierre, papier, ciseaux ? ").lower()
        if player in ["pierre", "papier", "ciseaux"]:
            return player
        else:
            print("Choix invalide. Veuillez choisir parmi : pierre, papier, ciseaux")

def jeu_shifumi():
    shifumi = ["pierre", "papier", "ciseaux"]
    choix_ordi : str = random.choice(shifumi)
    choix_joueur = user_choice()

    print("L'ordinateur a choisi :", choix_ordi)

    if choix_ordi == choix_joueur:
        print("Égalité")
    elif (choix_ordi == "pierre" and choix_joueur == "ciseaux") or \
         (choix_ordi == "ciseaux" and choix_joueur == "papier") or \
         (choix_ordi == "papier" and choix_joueur == "pierre"):
        print("Vous avez perdu")
    else:
        print("Vous avez gagné")

def launch_game():
    rejouer = True
    while rejouer:
        jeu_shifumi()
        relancer = input("Voulez-vous relancer une partie ? (Oui/Non) : ").lower()
        rejouer = relancer == "oui"

launch_game()
