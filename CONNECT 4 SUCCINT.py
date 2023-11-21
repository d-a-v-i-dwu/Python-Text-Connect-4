"""
Author: David Wu
"""

from ast import Index

board = "-  -  -  -  -  -  -\n-  -  -  -  -  -  -\n-  -  -  -  -  -  -\n-  -  -  -  -  -  -\n-  -  -  -  -  -  -\n-  -  -  -  -  -  -\n-  -  -  -  -  -  -\n1  2  3  4  5  6  7"
print(board)
game_progress = True

def main(player):
    def player_move():
        if player == "O":
            move = input("Player 1, select a position: ")
        else:
            move = input("Player 2, select a position: ")
        return move
    move = player_move()

    def guess_check(move):
        try:
            int(move)
        except ValueError:
            print("A number from 1 to 7 please")
            return "retry"
        
        if int(move) > 7 or int(move) < 1:
            print("A number from 1 to 7 please")
            return "retry"
        else:
            return "no"
    check = guess_check(move)

    while check == "retry":
        move = player_move()
        check = guess_check(move)

    def move_input(move):
        global board
        move_position = (int(move) - 1) * 3
        move_positions = [(move_position + 120), (move_position + 100), (move_position + 80), (move_position + 60), (move_position + 40), (move_position + 20), move_position]
        for ele in move_positions:
            if board[ele] == "-":
                board = board[:ele] + player + board[ele + 1:]
                return
            elif ele == move_position:
                print("Slot is full, pick another")
                return "retry"
            else:
                continue
    check = move_input(move)
    
    while check == "retry":
        move = player_move()
        check = guess_check(move)
        if check == "retry":
            continue
        check = move_input(move)

    def vertical_check():
        for ele_position in range(len(board)):
            ele = board[ele_position]
            if ele == player and ele == board[ele_position + 20] and ele == board[ele_position + 40] and ele == board[ele_position + 60]:
                return False
            else:
                continue
        return
    game_progress = vertical_check()

    def horizontal_check(game_progress):
        if game_progress == False:
            return False
        else:
            for ele_position in range(len(board)):
                ele = board[ele_position]
                if ele == player and ele == board[ele_position + 3] and ele == board[ele_position + 6] and ele == board[ele_position + 9]:
                    return False
                else:
                    continue
        return
    game_progress = horizontal_check(game_progress)

    def downward_diagonal_check(game_progress):
        if game_progress == False:
            return game_progress
        else:
            for ele_position in range(len(board)):
                ele = board[ele_position]
                try:
                    if ele == player and ele == board[ele_position + 23] and ele == board[ele_position + 46] and ele == board[ele_position + 69]:
                        return False
                    else:
                        continue
                except IndexError:
                    continue
        return
    game_progress = downward_diagonal_check(game_progress)

    def upward_diagonal_check(game_progress):
        if game_progress == False:
            return game_progress
        else:
            for ele_position in range(len(board)):
                ele = board[ele_position]
                try:
                    if ele == player and ele == board[ele_position + 17] and ele == board[ele_position + 34] and ele == board[ele_position + 51]:
                        return False
                    else:
                        continue
                except IndexError:
                    continue
        return
    game_progress = upward_diagonal_check(game_progress)
    
    return game_progress

while game_progress != False:
    player = "O"
    game_progress = main(player)
    print(board)
    if game_progress == False:
        print("Game Over, Player 1 Wins!")
        break
    player = "X"
    game_progress = main(player)
    print(board)
else:
    print("Game Over, Player 2 Wins!")