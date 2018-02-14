import random

class Board(list):
    def __init__(self, width, height):
        self = []
        #self.width = width
        for x in range(0, height):
            self.append(["O"] * width)

    def print(self):
        for row in self:
            print(" ".join(row))

boardWidth = 5
boardHeight = 5

board = Board(5, 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
board.print()

def random_row(board):
    return random.randint(0,len(board)-1)

def random_col(board):
    return random.randint(0,len(board[0])-1)

def inputInt(what):
    return int(input("Guess " + what + ": ").split()[0])

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

for turn in range(5):
    print("Turn ", turn + 1)
    guess_row, guess_col = inputInt("Row"), inputInt("Col")

    win = (guess_row == ship_row and guess_col == ship_col)
    if(win):        
        break
    else:
        if (guess_row < 0 or guess_row >= len(board)) or (guess_col < 0 or guess_col >= len(board[0])):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        elif(board[guess_row][guess_col] == "."):
            print("You missed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "."
    board.print()

print("Congratulations! You sunk my battleship!" if win else "Game Over")