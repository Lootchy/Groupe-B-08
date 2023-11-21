import random

def user_choice():
    return input("pierre, papier, ciseaux ? ").lower()

def jeu_shifumi():
    shifumi = ["pierre", "papier", "ciseaux"]
    choix_ordi : str = random.choice(shifumi)
    choix_joueur = user_choice()

    print("L'ordinateur a choisi :", choix_ordi)

    results = {
        (choix_ordi, choix_joueur): "Égalité",
        ("pierre", "ciseaux"): "Vous avez perdu",
        ("ciseaux", "papier"): "Vous avez perdu",
        ("papier", "pierre"): "Vous avez perdu",
        ("pierre", "papier"): "Vous avez gagné",
        ("ciseaux", "pierre"): "Vous avez gagné",
        ("papier", "ciseaux"): "Vous avez gagné",
    }
    
    print(results.get((choix_ordi, choix_joueur), "Erreur de logique"))

def launch_game():
    rejouer : bool = True
    while rejouer:
        jeu_shifumi()
        relancer : str = input("Voulez-vous relancer une partie ? (Oui/Non) : ").lower()
        rejouer = relancer == "oui"

launch_game()
