#!/usr/bin/env python3
from ..scripts.round_games import round_games
from ..scripts.get_random import get_random


def even_number():
    result_even = [
        'Answer "yes" if the number is even, otherwise answer "no".'
    ]
    for i in range(3):
        question_even = get_random(1, 100)
        if question_even % 2 == 0:
            answer_correct = 'yes'
        else:
            answer_correct = 'no'
        result_even.append([question_even, answer_correct])
    return result_even


def main():
    round_games(even_number())


if __name__ == '__main__':
    main()
