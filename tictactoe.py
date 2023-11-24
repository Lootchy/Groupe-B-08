def create_board() -> list[list[int]]:
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def display_board(board: list[list[int]]) -> None:
    for row in board:
        print(" | ".join(map(str, row)))
        print("-" * 9)

def check_for_winner(board: list[list[int]]) -> int | str | None:
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            return row[0]

    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]

    if all([all(row) for row in board]):
        return "tie"

    return None

def declare_winner(winner: int | str) -> None:
    if winner == "tie":
        print("Egalité !")
    else:
        print(f"Joueur {winner} a gagné!")

def play_tic_tac_toe() -> None:
    board = create_board()
    current_player = 1

    while True:
        display_board(board)

        row = int(input("Choisissez la ligne (0, 1, ou 2) : "))
        col = int(input("Choisissez la colonne (0, 1, ou 2) : "))

        if board[row][col] == 0:
            if current_player == 1:
                board[row][col] = "X"
                current_player = 2
            else:
                board[row][col] = "O"
                current_player = 1

            winner = check_for_winner(board)
            if winner:
                display_board(board)
                declare_winner(winner)
                break

        else:
            print("Case déjà occupée, veuillez choisir une autre.")

def launch_game():
    rejouer = True
    while rejouer:
        play_tic_tac_toe()
        relancer = input("Voulez-vous relancer une partie ? (Oui/Non) : ").lower()
        rejouer = relancer == "oui"

launch_game()
