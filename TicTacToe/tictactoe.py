import random
import time

def print_board(board: list[list[str]]) -> None:
    for row in board:
        print("|".join(row))
        print("-" * (2 * len(row) - 1))

def check_victory(board: list[list[str]], symbol: str, row: int, col: int, win_length: int) -> bool:
    # Verifie les colonnes et les lignes
    if all(board[row][j] == symbol for j in range(len(board))) or all(board[i][col] == symbol for i in range(len(board))):
        return True

    # Verifie les diagonales
    if row == col or row + col == len(board) - 1:
        if all(board[i][i] == symbol for i in range(len(board))) or all(board[i][len(board) - 1 - i] == symbol for i in range(len(board))):
            return True

    return False


###Aide chatGPT###
def winning_move(board: list[list[str]], symbol: str, row: int, col: int, win_length: int) -> tuple[int, int]:
    # Verifie les lignes
    for i in range(len(board)):
        if sum(board[row][j] == symbol for j in range(len(board))) == win_length - 1 and ' ' in board[row]:
            return row, board[row].index(' ')
    
    # Verifie les colonnes
    for i in range(len(board)):
        if sum(board[i][col] == symbol for i in range(len(board))) == win_length - 1 and ' ' in [board[i][col] for i in range(len(board))]:
            return [i for i in range(len(board)) if board[i][col] == ' '][0], col

    # Verifie les diagonales
    if row == col:
        if sum(board[i][i] == symbol for i in range(len(board))) == win_length - 1 and ' ' in [board[i][i] for i in range(len(board))]:
            return [i for i in range(len(board)) if board[i][i] == ' '][0], [i for i in range(len(board)) if board[i][i] == ' '][0]
    
    if row + col == len(board) - 1:
        if sum(board[i][len(board) - 1 - i] == symbol for i in range(len(board))) == win_length - 1 and ' ' in [board[i][len(board) - 1 - i] for i in range(len(board))]:
            return [i for i in range(len(board)) if board[i][len(board) - 1 - i] == ' '][0], [i for i in range(len(board)) if board[i][len(board) - 1 - i] == ' '][0]

    return None, None

###Fin ide chatGPT###
def blocking_move(board: list[list[str]], player_symbol: str, row: int, col: int, win_length: int) -> tuple[int, int]:
    return winning_move(board, 'X' if player_symbol == 'O' else 'O', row, col, win_length)

def play_turn(board: list[list[str]], symbol: str, player: str, win_length: int) -> bool:
    print(f"{player}'s turn ({symbol})")
    print_board(board)
    
    if player == 'AI':
        print("IA PLAYING...")
        start = time.time()
        move = winning_move(board, symbol, 0, 0, win_length)
        if move == (None, None):
            move = blocking_move(board, symbol, 0, 0, win_length)
            if move == (None, None):
                available_moves = [(i, j) for i in range(len(board)) for j in range(len(board)) if board[i][j] == ' ']
                move = random.choice(available_moves)
        end = time.time()
        print("DONE in:" + str(end - start))
    else:
        while True:
            try:
                row = int(input(f"Choose the row (0-{len(board)-1}): "))
                col = int(input(f"Choose the column (0-{len(board)-1}): "))
                if 0 <= row < len(board) and 0 <= col < len(board) and board[row][col] == ' ':
                    move = (row, col)
                    break
                else:
                    print("The cell is already occupied or the coordinates are invalid. Choose another.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    board[move[0]][move[1]] = symbol
    return check_victory(board, symbol, move[0], move[1], win_length)

def play_tic_tac_toe() -> None:
    board_size: int = int(input("Choose the board size (minimum 3): "))
    win_length: int = int(input("Choose the number of symbols in a row to win: "))
    board: list[list[str]] = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    turn: int = 0

    while True:
        if turn % 2 == 0:
            symbol: str = 'X'
            player: str = 'Player'
        else:
            symbol: str = 'O'
            player: str = 'AI'

        if play_turn(board, symbol, player, win_length):
            print(f"{player} ({symbol}) wins!")
            break

        turn += 1
        if turn == board_size * board_size:
            print("It's a draw!")
            break

def launch_game() -> None:
    replay: bool = True
    while replay:
        play_tic_tac_toe()
        restart: str = input("Do you want to play again? (Yes/No): ").lower()
        replay = restart == "yes"

launch_game()
