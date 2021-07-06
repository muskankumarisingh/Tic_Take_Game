def dict1():
    global board
    board={'1':' ','2':' ','3':' ',
           '4':' ','5':' ','6':' ',
           '7':' ','8':' ','9':' '}

def check():
    if board['1']=='X' and board['2']=='X' and board['3']=='X':
        print("player one win!!")
        return 1
    elif board['4']=='X' and board['5']=='X' and board['6']=='X':
        print("player one win!!")
        return 1
    elif board['7']=='X' and board['8']=='X' and board['9']=='X':
        print("player one win")
        return 1
    elif board['1']=='X' and board['4']=='X' and board['7']=='X':
        print("player one win!!")
        return 1
    elif board['2']=='X' and board['5']=='X' and board['8']=='X':
        print("player one win!!")
        return 1
    elif board['3']=='X' and board['6']=='X' and board['9']=='X':
        print("player one win!!")
        return 1
    elif board['1']=='X' and board['5']=='X' and board['9']=='X':
        print("player one win")
        return 1
    elif board['3']=='X' and board['5']=='X' and board['7']=='X':
        print("player one win!!")
        return 1

    # Second player:
    if board['1']=='O' and board['2']=='O' and board['3']=='O':
        print("player two win")
        return 2
    elif board['4']=='O' and board['5']=='O' and board['6']=='O':
        print("player two win")
        return 2
    elif board['7']=='O' and board['8']=='O' and board['9']=='O':
        print("print two win")
        return 2
    elif board['1']=='O' and board['4']=='O' and board['7']=='O':
        print("player two win")
        return 2
    elif board['2']=='O' and board['5']=='O' and board['8']=='O':
        print("player two win!!")
        return 2
    elif board['3']=='O' and board['6']=='O' and board['9']=='O':
        print("player two win!!")
        return 2
    elif board['1']=='O' and board['5']=='O' and board['9']=='O':
        print("player two win !")
        return 2
    elif board['3']=='O' and board['5']=='O' and board['7']=='O':
        print("player two win !!")
        return 2
    else:
        return 0

def play_game():
    dict1()
    total_moves=0
    player=1

    print("1"," |","2 |","3")
    print("---+---+---")
    print("4"," |","5 |","6")
    print("---+---+---")
    print("7"," |","8 |","9\n")
    print("\U0001F600\ WELCOME TO GAME 'TIC TAC TOE'\U0001F600\n ")

    while True:
        print(board['1']+'   |'+board['2']+'   |'+board['3'])
        print("----+----+----")
        print(board['4']+'   |'+board['5']+'   |'+board['6'])
        print("----+----+----")
        print(board['7']+'   |'+board['8']+'   |'+board['9'])


        end_check=check()
        if end_check==1:
            print("congrates player one you are winner!!!\U0001F600\U0001F600")
            break
        elif end_check==2:
            print("congrates player two you are winner!!!\U0001F600\U0001F600")
            break
        if total_moves==9:
            print("GAME DRAW!!")
            break
        while True:
            if player==1:
                p1_input=input("player one X :")
                if p1_input in board and board[p1_input]==' ':
                    board[p1_input]='X'
                    player=2
                    break
                else:
                    print('invalid input,please try again...')
                    continue
            else:
                p2_input=input("player two O : ")
                if p2_input in board and board[p2_input]==' ':
                    board[p2_input]='O'
                    player=1
                    break
                else:
                    print('invalid input, please try again..')
                    continue
        total_moves+=1
        print()
play_game()

def again_play():
    user=input("do you want to play again\n y or n :")
    if user=="y":
        play_game()
        again_play()
    elif user=="n":
        print("EXIT\U0001F917")
again_play()