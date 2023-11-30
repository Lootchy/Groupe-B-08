# Tools.py

import random

###Partie sur le plus ou moins###
def askint(minimum: int, maximum: int) -> int:
    while True:
        a: str = input(f"Donnez un nombre entre {minimum} et {maximum} : ")
        if a.isdigit():
            a = int(a)
            if minimum <= a <= maximum:
                return a
            else:
                print(f"Vous devez choisir un nombre entre {minimum} et {maximum} inclusivement.")
        else:
            print("Vous devez entrer un nombre entier !!!")

def get_valid_input() -> tuple[int, int]:
    while True:
        mingame: str = input("Entrer la valeur min : ")
        maxgame: str = input("Entrer la valeur max : ")
        
        if mingame.isdigit() and maxgame.isdigit():
            mingame = int(mingame)
            maxgame = int(maxgame)
            
            if mingame <= maxgame:
                return mingame, maxgame
            else:
                print("La valeur minimale ne peut pas être supérieure à la valeur maximale. Réessayez.")
        else:
            print("Vous devez entrer des nombres entiers. Réessayez.")

def play_game() -> None:
    found: bool = False
    tentative: int = 0
    tentativemax: int = 5
    
    mingame, maxgame = get_valid_input()
    
    print(f"Vous avez {tentativemax} essais pour trouver le bon nombre")
    
    num: int = random.randint(mingame, maxgame)

    while not found and tentative != tentativemax:
        a: int = askint(mingame, maxgame)

        if a > num:
            print("C'est moins !")
        elif a < num:
            print("C'est plus !")
        elif a == num:
            print("Tu as trouvé le bon nombre.")
            found = True
        tentative += 1

    if not found:
        print("Vous avez dépassé le nombre d'essais")
    print(f"Le nombre était : {num} et vous avez mis {tentative} essais")


###Partie shifumi###

def user_choice() -> str:
    while True:
        player: str = input("pierre, papier, ciseaux ? ").lower()
        if player in ["pierre", "papier", "ciseaux"]:
            return player
        else:
            print("Choix invalide. Veuillez choisir parmi : pierre, papier, ciseaux")

def jeu_shifumi(score_ordi: int, score_joueur: int) -> tuple[int, int]:
    shifumi: list[str] = ["pierre", "papier", "ciseaux"]
    choix_ordi: str = random.choice(shifumi)
    choix_joueur: str = user_choice()

    print("L'ordinateur a choisi :", choix_ordi)

    if choix_ordi == choix_joueur:
        print("Égalité, il y a", score_ordi,"pour l'ordi et", score_joueur, "pour le joueur")
    elif (choix_ordi == "pierre" and choix_joueur == "ciseaux") or \
         (choix_ordi == "ciseaux" and choix_joueur == "papier") or \
         (choix_ordi == "papier" and choix_joueur == "pierre"):
        score_ordi += 1
        print("Vous avez perdu, il y a", score_ordi,"pour l'ordi et", score_joueur, "pour le joueur")
    else:
        score_joueur += 1
        print("Vous avez gagner, il y a", score_ordi,"pour l'ordi et", score_joueur, "pour le joueur")

    return score_ordi, score_joueur




###Partie Wordle###
def get_valid_choice() -> str:
    while True:
        choice = input("\nEnter your guess: ").lower()

        # Verifie sur l'input est valide
        if any(char.isdigit() for char in choice) or len(choice) != 5:
            if any(char.isdigit() for char in choice):
                print("Please enter a string without digits.")
            elif len(choice) != 5:
                print("Please enter a string of 5 characters.")
        else:
            return choice