import random


def drawBoard(board):

    print()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' -----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' -----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print()


def inputPlayerLetter():

    print("avaiable variables are x and o x=player 1 & o=player 2 ")
    return ['X', 'O']


def whoGoesFirst():
    print("0=Heads and heads is allocated to Player 1")
    print()
    print("1=Tails and Tails is allocated to Player 2")
    print()
    result = random.randint(0, 1)

    if result == 0:
        return "Heads Player 1 will play first"
    else:
        return "Tails Player two will play first."


result = whoGoesFirst()


def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def isWinner(bo, le, player_turn):
    if player_turn == 1:
        return (
               (bo[7] == le and bo[8] == le and bo[9] == le) or
               (bo[4] == le and bo[5] == le and bo[6] == le) or
               (bo[1] == le and bo[2] == le and bo[3] == le) or
               (bo[7] == le and bo[4] == le and bo[1] == le) or
               (bo[8] == le and bo[5] == le and bo[2] == le) or
               (bo[9] == le and bo[6] == le and bo[3] == le) or
               (bo[7] == le and bo[5] == le and bo[3] == le) or
               (bo[9] == le and bo[5] == le and bo[1] == le) or
               (bo[7] == le and bo[4] == le and bo[1] == le)
        )
    elif player_turn == 2:
        return (
            (bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le)
        )
    else:
        return 'false'


def isBoardFull(board):
    return ' ' not in board[1:]


def makeMove(board, player_letter, player_name):
    while True:
        move = input(f"Player {player_name}, enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move)] == ' ':
            board[int(move)] = player_letter
            break
        else:
            print("Invalid move. Please choose an empty position from 1 to 9.")


board = [' '] * 10
player_turn = whoGoesFirst()
player_letters = inputPlayerLetter()

player1_name = "Player 1"
player2_name = "Player 2"

while True:
    drawBoard(board)

    # Player's move
    if player_turn == 1:
        makeMove(board, player_letters[0], player1_name)
        player_turn = 2  # Switch to player 2

    else:
        makeMove(board, player_letters[1], player2_name)
        player_turn = 1  # Switch to player 1
    # Display the updated board
    drawBoard(board)
    # Check for a win or a tie
    if isWinner(board, player_letters[player_turn - 1], player_turn):
        print(f" {player1_name} wins!"
              if player_turn == 1
              else f"{player2_name} wins!")
        break
    elif isBoardFull(board):
        print("The game is a tie!")
