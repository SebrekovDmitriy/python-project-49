#!/usr/bin/env python3
from ..scripts.round_games import round_games
from ..scripts.get_random import get_random
import math


def prime():
    result_prime = ['Answer "yes" if given number is prime. Otherwise answer "no".']
    for i in range(3):
        answer_correct = 'yes'
        question_prime = ''
        number_prime = get_random(2, 101)  # setting the range of random number 1
        question_prime = number_prime
        for start_number in range(2, int(math.sqrt(number_prime)) + 1):
            if number_prime % start_number == 0:
                answer_correct = 'no'
                break
        result_prime.append([question_prime, answer_correct])
    return result_prime


def main():
    round_games(prime())


if __name__ == '__main__':
    main()
