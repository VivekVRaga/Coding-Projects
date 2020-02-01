# A simple game of 0 and Xs

theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'bot-l': ' ', 'bot-m': ' ', 'bot-r': ' ', }


def printboard(board):

    print(board['top-l'] + '|' + board['top-m']+'|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['bot-l'] + '|' + board['bot-m'] + '|' + board['bot-r'])


def checkwin(board):
    if ((board['top-l'] == 'O') and (board['top-m'] == 'O') and (board['top-m'] == 'O'))\
        or ((board['mid-l'] == 'O') and (board['mid-m'] == 'O') and (board['mid-m'] == 'O'))\
        or ((board['bot-l'] == 'O') and (board['bot-m'] == 'O') and (board['bot-m'] == 'O'))\
        or ((board['top-l'] == 'O') and (board['mid-l'] == 'O') and (board['bot-l'] == 'O'))\
        or ((board['top-m'] == 'O') and (board['mid-m'] == 'O') and (board['bot-m'] == 'O'))\
        or ((board['top-r'] == 'O') and (board['mid-r'] == 'O') and (board['bot-r'] == 'O'))\
        or ((board['top-l'] == 'O') and (board['mid-m'] == 'O') and (board['bot-r'] == 'O'))\
        or ((board['top-r'] == 'O') and (board['mid-m'] == 'O') and (board['bot-l'] == 'O')):
        return 'O wins'
    elif ((board['top-l'] == 'X') and (board['top-m'] == 'X') and (board['top-m'] == 'X'))\
        or ((board['mid-l'] == 'X') and (board['mid-m'] == 'X') and (board['mid-m'] == 'X'))\
        or ((board['bot-l'] == 'X') and (board['bot-m'] == 'X') and (board['bot-m'] == 'X'))\
        or ((board['top-l'] == 'X') and (board['mid-l'] == 'X') and (board['bot-l'] == 'X'))\
        or ((board['top-m'] == 'X') and (board['mid-m'] == 'X') and (board['bot-m'] == 'X'))\
        or ((board['top-r'] == 'X') and (board['mid-r'] == 'X') and (board['bot-r'] == 'X'))\
        or ((board['top-l'] == 'X') and (board['mid-m'] == 'X') and (board['bot-r'] == 'X'))\
        or ((board['top-r'] == 'X') and (board['mid-m'] == 'X') and (board['bot-l'] == 'X')):
        return 'X wins'
    else:
        return 0
GameEndState = False

for i in range(1, 10, 1):
    if (i % 2) == 0:
        print('Xs Turn')
    else:
        print('O\'s Turn')
    move = input()
    while move not in ['top-r', 'mid-m', 'bot-l', 'top-l', 'top-m', 'mid-l', 'mid-r','bot-r', 'bot-m']:
        print('Not a valid placement name')
        move = input()
    while theBoard[move] != ' ':
        print('error space is occupied')
        move = input()
    if (i % 2) == 0:
        theBoard[move] = 'X'
    else:
        theBoard[move] = 'O'
    printboard(theBoard)

    if checkwin(theBoard) != 0:
        print(checkwin(theBoard))
        break

if checkwin(theBoard) == 0:
    print('Draw')
