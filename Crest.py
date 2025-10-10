def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---------")
    print("\n")

def check_winner(board, player):
    # Проверка строк и столбцов
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("🎮 Добро пожаловать в Крестики-Нолики!")
    print("Игрок 1 — X, Игрок 2 — O")
    print("Введите номер строки и столбца (например: 1 2)")

    while True:
        print_board(board)
        try:
            row, col = map(int, input(f"Ход игрока {current_player}: ").split())
            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("❗ Введите числа от 1 до 3.")
                continue
            if board[row - 1][col - 1] != " ":
                print("❗ Эта клетка уже занята!")
                continue
        except ValueError:
            print("❗ Введите два числа через пробел.")
            continue

        board[row - 1][col - 1] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Игрок {current_player} победил!")
            break

        if is_board_full(board):
            print_board(board)
            print("🤝 Ничья!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()