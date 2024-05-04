#!/usr/bin/env python3
from ..scripts.round_games import round_games
from ..scripts.get_random import get_random


def nod(num1, num2):
    number1 = num1
    number2 = num2
    for i in range(2):
        while number1 and number2:
            if number1 > number2:
                number1 %= number2
            else:
                number2 %= number1
        number1 += number2
    return number1


def gcd():
    result_gcd = ['Find the greatest common divisor of given numbers.']
    for i in range(3):
        number_one_gcd = get_random(1, 100)
        number_two_gcd = get_random(1, 100)
        question_gcd = f"{number_one_gcd} {number_two_gcd}"
        answer_correct = str(nod(number_one_gcd, number_two_gcd))
        result_gcd.append([question_gcd, answer_correct])
    return result_gcd


def main():
    round_games(gcd())


if __name__ == '__main__':
    main()
