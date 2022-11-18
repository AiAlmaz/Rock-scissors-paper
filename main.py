import random

choice = ['r', 's', 'p']
count = [0, 1]
def check_answer(t):
    if t == 'r':
        print("Rock")
    elif t == 's':
        print('Scissors')
    elif t == 'p':
        print('Paper')

def check_win(win, lose):
    if win == 'r' and lose == 'p':
        print(win)
    elif win == 'p' and lose == 'r':
        print()
    elif win == ''

def main():
    a = 0
    b = 0
    while True:
        turn = input("Please enter your turn: ('r', 's', 'p'): ").lower()
        if turn == 'exit':
            break
        else:
            check_answer(turn)
        c_turn = random.choice(choice)
        check_answer(c_turn)

        # if turn == 'r' and c_turn == 's':
        #     print('You win')
        # elif turn == 'p' and c_turn == 'r':
        #     print('You win')
        # elif turn == 's' and c_turn == 'p':
        #     print('You win')
        # elif c_turn == 'r' and turn == 's':
        #     print('comp win')
        # elif c_turn == 'p' and turn == 'r':
        #     print('You win')
        # elif c_turn == 's' and turn == 'p':
        #     print('You win')

        if turn == 'r' and c_turn == 's' or turn == 'p' and c_turn == 'r' or turn == 's' and c_turn == 'p':
            print('You win')
            count[0] += 1
        elif c_turn == 'r' and turn == 's' or c_turn == 'p' and turn == 'r' or c_turn == 's' and turn == 'p':
            print('Comp win')
            count[1] += 1
        print('current score:', count)
        if

main()
