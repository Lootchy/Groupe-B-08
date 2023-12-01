import random

# Charger les mots depuis le fichier output.txt
with open('output.txt', 'r') as fin:
    words: list[str] = [word.strip() for word in fin.readlines()]

def choose_random_word(words: list[str]) -> str:
    # Choisir un mot au hasard parmi la liste de mots
    return random.choice(words)

def print_grid(grid: list[list[str]]) -> None:
    # Afficher la grille
    for row in grid:
        print(" ".join(row))

def get_valid_choice() -> str:
    while True:
        # Demander à l'utilisateur de deviner un mot
        choice: str = input("\nEnter your guess: ").lower()

        # Vérifier si l'entrée contient des chiffres ou n'a pas une longueur de 5 caractères
        if any(char.isdigit() for char in choice) or len(choice) != 5:
            if any(char.isdigit() for char in choice):
                print("Please enter a string without digits.")
            elif len(choice) != 5:
                print("Please enter a string of 5 characters.")
        # Vérifier si le mot deviné n'est pas dans la liste de mots
        elif choice not in words:
            print("Please enter a valid word.")
        else:
            return choice

def play_game(word: str, max_tries: int = 6) -> bool:
    found: bool = False
    nb_try: int = 0

    # Définir la taille de la grille
    rows, cols = 6, 5
    grid: list[list[str]] = [[' ' for _ in range(cols)] for _ in range(rows)]

    while not found and nb_try < max_tries:
        guess: str = get_valid_choice()

        nb_try += 1
        good_letter_count: int = 0
        letters_discovered: list[str] = ['_'] * len(word)
        letter_indices = {}
        for i in range(len(word)):
            if word[i] == guess[i]:
                letters_discovered[i] = '\033[32m' + guess[i] + '\033[0m'  # Green
                good_letter_count += 1
            elif guess[i] in word:
                if guess[i] not in letter_indices:
                    letter_indices[guess[i]] = i
                    letters_discovered[i] = '\033[33m' + guess[i] + '\033[0m'  # Yellow
                else:
                    if i == letter_indices[guess[i]]:
                        letters_discovered[i] = '\033[33m' + guess[i] + '\033[0m'  # Orange
                    else:
                        letters_discovered[i] = '\033[31m' + guess[i] + '\033[0m'  # Red

        # Mettre à jour la grille avec le résultat de l'essai
        grid[nb_try - 1] = letters_discovered

        # Afficher la grille
        print_grid(grid)

        if good_letter_count == len(word):
            found = True
            print(f"\nYou won with {nb_try} tries!")

    if nb_try == max_tries and not found:
        print(f"\nYou ran out of tries. The correct word was: {word}")

    return found

def replay() -> bool:
    # Demander à l'utilisateur s'il veut rejouer
    replay_choice: str = input("\nDo you want to play again? (Yes/No): ").lower()
    return replay_choice == "yes"


replay_game: bool = True

while replay_game:
    selected_word: str = choose_random_word(words)
    game_result: bool = play_game(selected_word)

    if not game_result:
        print("Game over. Thanks for playing!")
        break

    replay_game = replay()

print("Goodbye!")
