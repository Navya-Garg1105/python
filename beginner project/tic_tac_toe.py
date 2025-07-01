def print_board(lst):
    st = '''
     {}|{}|{}
    -------
     {}|{}|{}
    -------
     {}|{}|{}'''.format(*lst)
    print(st)
choices = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
print("welcome")
print_board(choices)
turns = 'X'
while 1:
    mv = int(input(f"its your turn {turns},your move[0-9]"))
    if choices [mv] == ' ':
        choices[mv] = turns
        print_board(choices)
    elif choices[0] == choices[1] == choices[2] != ' ':
        print(f"you won {turns}")
        break
    elif choices[3] == choices[4] == choices[5] != ' ':
        print(f"you won {turns}")
        break
    elif choices[6] == choices[7] == choices[8] != ' ':
        print(f"you won {turns}")
        break
    elif choices[0] == choices[3] == choices[6] != ' ':
        print(f"you won {turns}")
        break
    elif choices[1] == choices[4] == choices[7] != ' ':
        print(f"you won {turns}")
        break
    elif choices[2] == choices[5] == choices[8] != ' ':
        print(f"you won {turns}")
        break
    elif choices[0] == choices[4] == choices[8] != ' ':
        print(f"you won {turns}")
        break
    elif choices[2] == choices[4] == choices[6] != ' ':
        print(f"you won {turns}")
        break
    turns = 'X' if turns == '0'else'0'
    print_board(choices)

