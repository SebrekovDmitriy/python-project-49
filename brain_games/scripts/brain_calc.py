#!/usr/bin/env python3
from ..scripts.round_games import round_games
from ..scripts.get_random import get_random


def calc():
    result_calc = ['What is the result of the expression?']
    for i in range(3):
        base_operator = ['+', '-', '*']
        num_one_calc = get_random(1, 30)
        num_two_calc = get_random(1, 30)
        num_oper_index_calc = get_random(0, 2)
        num_operator_calc = base_operator[num_oper_index_calc]

        if num_oper_index_calc == 0:
            answer_correct = str(num_one_calc + num_two_calc)
            question_calc = f"{num_one_calc} {num_operator_calc} {num_two_calc}"
        elif num_oper_index_calc == 1:
            answer_correct = str(num_one_calc - num_two_calc)
            question_calc = f"{num_one_calc} {num_operator_calc} {num_two_calc}"
        else:
            answer_correct = str(num_one_calc * num_two_calc)
            question_calc = f"{num_one_calc} {num_operator_calc} {num_two_calc}"

        result_calc.append([question_calc, answer_correct])

    return result_calc


def main():
    round_games(calc())


if __name__ == '__main__':
    main()
