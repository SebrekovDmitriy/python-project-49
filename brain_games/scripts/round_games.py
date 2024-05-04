#!/usr/bin/env python3
def round_games(basequestion):
    print('Welcome to the Brain Games!')
    user = input('May I have your name? ')  # Get name user
    print(f'Hello, {user}!')
    name_game = basequestion[0]
    print(name_game)
    for i in range(3):
        base_round = basequestion[i + 1]
        question_round = base_round[0]
        ans_round = base_round[1]
        print(f'Question: {question_round}')
        answer = input('Your answer: ')  # Get answer
        if answer == ans_round:
            if i == 2:
                print('Correct!')
                print(f'Congratulations, {user}!')
            else:
                print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{ans_round}'.\n"
                  f"Let's try again, {user}!")
            break
