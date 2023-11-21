import random

def askint(minimum: int, maximum: int) -> int:
    while True:
        a = input(f"Donnez un nombre entre {minimum} et {maximum} : ")
        if a.isdigit():
            a = int(a)
            if minimum <= a <= maximum:
                return a
            else:
                print(f"Vous devez choisir un nombre entre {minimum} et {maximum} inclusivement.")
        else:
            print("Vous devez entrer un nombre entier !!!")

def play_game():
    found = False
    tentative = 0
    tentativemax = 5
    print(f"Vous avez {tentativemax} essais pour trouver le bon nombre")

    mingame = int(input("Entrer la valeur min : "))
    maxgame = int(input("Entrer la valeur max : "))
    
    num = random.randint(mingame, maxgame)

    while not found and tentative != tentativemax:
        a = askint(mingame, maxgame)

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

def game():
    rejouer = True
    while rejouer:
        play_game()
        relancer = input("Voulez-vous relancer une partie ? (Oui/Non) : ").lower()
        rejouer = relancer == "oui"


game()
