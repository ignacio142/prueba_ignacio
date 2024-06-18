import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    username = input("Por favor, ingresa tu nombre de usuario: ")

    while True:
        print("MENU:")
        print("1. Nueva Partida contra IA")
        print("2. Versus")
        print("3. Salir")
        choice = input("Elige una opción: ")

        if choice == '1':  # Nueva Partida contra IA
            play_game(0, username)
        elif choice == '2':  # Versus
            play_game(1, username)
        elif choice == '3':  # Salir
            print("¡Gracias por jugar! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige nuevamente.")

def play_game(mode, username):
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        if mode == 0 and turn == 1:  # Turno de la IA
            print(f"Turno de la IA ({players[turn]}).")
            row, col = ia_move(board)
        else:
            print(f"Turno del {username if turn == 0 else 'JUGADOR 2'} ({players[turn]}).")
            row = int(input("Ingresa fila (0, 1, o 2): "))
            col = int(input("Ingresa columna (0, 1, o 2): "))

        if row not in range(3) or col not in range(3):
            print("Fila o columna inválida. Por favor, ingresa nuevamente.")
            continue

        if board[row][col] != ' ':
            print("¡Esa celda ya está ocupada! Inténtalo de nuevo.")
            continue

        board[row][col] = players[turn]

        if check_winner(board, players[turn]):
            print_board(board)
            print(f"¡{username if turn == 0 else 'JUGADOR 2'} FELICIDADES, HAS GANADO!" if mode == 1 else f"¡{username if turn == 0 else 'IA'} FELICIDADES, HAS GANADO!")
            break
        elif is_board_full(board):
            print_board(board)
            print("¡Es un empate!")
            break

        turn = (turn + 1) % 2

def ia_move(board):
    # IA simple que elige una celda vacía al azar
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)

if __name__ == "__main__":
    main()
