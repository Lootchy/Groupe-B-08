import random

def user_choice() -> str:
    return input("Rock, paper, scissors? ").lower()

def jeu_shifumi() -> tuple[str, str, str]:
    shifumi: list[str] = ["rock", "paper", "scissors"]
    choix_ordi: str = random.choice(shifumi)
    choix_joueur: str = user_choice()

    print("The computer chose:", choix_ordi)

    results = {
        (choix_ordi, choix_joueur): "It's a tie",
        ("rock", "scissors"): "You lost",
        ("scissors", "paper"): "You lost",
        ("paper", "rock"): "You lost",
        ("rock", "paper"): "You won",
        ("scissors", "rock"): "You won",
        ("paper", "scissors"): "You won",
    }

    result_message = results.get((choix_ordi, choix_joueur), "Logic error")
    print(result_message)

    return choix_ordi, choix_joueur, result_message

def launch_game() -> None:
    score_mapping = {
        "You won": lambda s: (s[0], s[1] + 1),
        "You lost": lambda s: (s[0] + 1, s[1]),
        "It's a tie": lambda s: s
    }

    score_ordi, score_joueur = 0, 0

    while score_ordi < 3 and score_joueur < 3:
        choix_ordi, choix_joueur, result_message = jeu_shifumi()
        score_ordi, score_joueur = score_mapping[result_message]((score_ordi, score_joueur))

        print(f"Score: Computer {score_ordi}, Player {score_joueur}")

    relancer = input("Do you want to play again? (Yes/No): ").lower()
    if relancer == "yes":
        launch_game()



launch_game()
