#!/usr/bin/env python3
from ..scripts.round_games import round_games
from ..scripts.get_random import get_random


def progression():
    result_progression = ['What number is missing in the progression?']
    for i in range(3):
        question_progression = []
        number_one_p = get_random(1, 100)
        base_progression = number_one_p
        step_prog = get_random(1, 20)
        index_prog = get_random(0, 9)
        for _ in range(10):
            question_progression.append(base_progression)
            base_progression += step_prog
        answer_correct = str(question_progression[index_prog])
        question_progression[index_prog] = '..'
        result_progression.append([' '.join(map(str, question_progression)), answer_correct])
    return result_progression


def main():
    round_games(progression())


if __name__ == '__main__':
    main()
