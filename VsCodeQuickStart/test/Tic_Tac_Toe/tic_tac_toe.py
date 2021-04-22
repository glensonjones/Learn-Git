# Tic Tac Toe game in Python
"""
X’s always go first, letting the user make the first move. 
We will get input from the console with a number 1-9. 
Where each number represents a different number in the grid 
(top left is 1, bottom right is 9). 
Once the user moves the computer will automatically decide 
on it’s move and make it. I am going to be using one main 
game loop that calls a few different functions. 
"""
board = [' ' for x in range(10)]
# board is now: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']



def insertLetter(letter, position):
    # insert X or O in specified position
    board[position] = letter

def spaceIsFree(position):
    # will return True or False according to whether no letter has yet been assigned 
    # or the reverse
    return board[position] == ' '

def isWinner(board, letter):
    # Given a board and a player’s letter, this function returns True if that player has won.
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
    (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
    (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
    (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
    (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
    (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
    (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal
    
def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    insertLetter('X', move)
                    run = False
                else:
                    print('Sorry, that space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

def selectRandom(a_list):
    import random
    a_list_length = len(a_list)
    r = random.randrange(0, a_list_length)
    return a_list[r]

def compMove():
    # Make a List of possible moves
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0


    for choise in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = choise
            if isWinner(boardCopy, choise):
                move = i
                return move

    cornersOpen = []
    for tryOne in possibleMoves:
        if tryOne in [1,3,7,9]:
            cornersOpen.append(tryOne)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for tryOne in possibleMoves:
        if tryOne in [2,4,6,8]:
            edgesOpen.append(tryOne)

        if len(edgesOpen) > 0:
            move = selectRandom(edgesOpen)

        return move


def isBoardFull(board):
    if board.count(' ') > 0:
        return False
    else:
        return True

def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def clearBoard():
    board = [' ' for x in range(10)]
    # board is now: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    return board

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')

# clearBoard()

# main()

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break