

def get_board(cells):
    rows, cols = [], []
    for i in range(0,9,3):
        rows.append([cells[i], cells[i+1], cells[i+2]])
    for i in range(3):
        cols.append([cells[i], cells[i+3], cells[i+6]])

    diag1, diag2 = [],[]
    for i in range(3):
        diag1.append(rows[i][i])
        diag2.append(rows[(i)][-(i+1)])
    return rows, cols, diag1, diag2

def print_board():
    print('---------')
    for i in range(3):
        print('| ', end='')
        for j in range(3):
            print(rows[i][j] + ' ', end='')
        print('|')
    print('---------')

def user_turn(user):
    global rows
    while True:
        user_input = input('Enter the coordinates: ').split()
        redo = False
        for i in range(2):
            if not user_input[i].isdigit():
                print('You should enter numbers!')
                redo = True
            elif not (1 <= int(user_input[i]) <= 3):
                print('Coordinates should be from 1 to 3!')
                redo = True
        if redo == True:
            continue
        user_col = int(user_input[0])-1
        user_row = (-int(user_input[1])+3)
        if rows[user_row][user_col] != '_':
            print('This cell is occupied! Choose another one!')
            continue
        break
    rows[user_row][user_col] = user
    if user == 'X':
        user = 'O'
    else:
        user = 'X'
    cells = ''
    for row in rows:
        for col in row:
            cells += col
    return user, cells

def check_winner():
    x_win = ['X', 'X', 'X']
    o_win = ['O', 'O', 'O']
    winnerx, winnero = False, False
    x_count, o_count, unders = 0, 0, 0

    for row in rows:
        x_count += row.count('X')
        o_count += row.count('O')
        unders += row.count('_')

    if diag1 == x_win or diag2 == x_win or x_win in rows or x_win in cols:
        winnerx = True
    if diag1 == o_win or diag2 == o_win or o_win in rows or o_win in cols:
        winnero = True

    #if abs(x_count - o_count) >= 2:
     #   print('Impossible')
    #elif winnero and winnerx:
     #   print('Impossible')
    if winnero == False and winnerx == False:
        if unders == 0:
            return 'Draw'
    elif winnero:
        return 'O'
    elif winnerx:
        return 'X'
    else:
        return None

cells = '_'*9
user = 'X'
winner = None
rows, cols, diag1, diag2 = get_board(cells)
while winner == None:
    print_board()
    user, cells = user_turn(user)
    rows, cols, diag1, diag2 = get_board(cells)
    winner = check_winner()

print_board()
if winner == 'X':
    print('X wins')
elif winner == 'O':
    print('O wins')
else:
    print('Draw')
