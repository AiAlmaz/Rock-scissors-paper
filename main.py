import random

choice = ['r', 's', 'p']

def check_answer(t):
    if t == 'r':
        print("Rock")
    elif t == 's':
        print('Scissors')
    elif t == 'p':
        print('Paper')

def check_win(turn, c_turn):
    count = [0, 0]
    if turn == 'r' and c_turn == 's' or turn == 'p' and c_turn == 's' or turn == 's' and c_turn == 'p':
        print('You won')
        count[0] += 1
    elif c_turn == 'r' and turn == 's' or c_turn == 'p' and turn == 's' or c_turn == 's' and turn == 'p':
        print('Comp won')
        count[1] += 1
    elif turn == c_turn:
        print("It is tie: ")
    print('the score is: ', count[0], ':', count[1])

def main():
    round = 0
    while round < 5:
        turn = input("please enter choose ('r', 's', 'p'): ").lower()
        if turn == 'exit':
            break
        else:
            check_answer(turn)
        c_turn = random.choice(choice)
        check_answer(c_turn)
        check_win(turn, c_turn)
        if turn not in choice:
            print("you chose incorrectly: ")
            continue
        round += 1
        if round == 5:
            return False
            break
    if count[0] > count[1]:
        print('Congrats you won the game')
    else:
        print('Computer won the game')

main()
