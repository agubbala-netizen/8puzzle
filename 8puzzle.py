import random

def print_board(board):
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print([x if x != 0 else " " for x in row])
    print()

def find_blank(board):
    return board.index(0)

def move(board, direction):
    i = find_blank(board)
    row, col = divmod(i, 3)

    if direction == "w" and row > 0:  # up
        swap = i - 3
    elif direction == "s" and row < 2:  # down
        swap = i + 3
    elif direction == "a" and col > 0:  # left
        swap = i - 1
    elif direction == "d" and col < 2:  # right
        swap = i + 1
    else:
        return board

    board[i], board[swap] = board[swap], board[i]
    return board

def is_solved(board):
    return board == [1,2,3,4,5,6,7,8,0]

def main():
    board = [1,2,3,4,5,6,7,8,0]
    random.shuffle(board)

    while True:
        print_board(board)

        if is_solved(board):
            print("You solved it!")
            break

        move_input = input("Move (w=up, s=down, a=left, d=right): ")
        board = move(board, move_input)

if __name__ == "__main__":
    main()
