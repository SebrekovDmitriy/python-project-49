#!/usr/bin/env python3
import random


def get_random(minimum, maximum):
    min_number = int(minimum)
    max_number = int(maximum)
    return random.randint(min_number, max_number)
