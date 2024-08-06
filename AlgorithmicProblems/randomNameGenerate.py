"""
    Generate Random characters
"""

# Without Algorithm
import random
import string


def generate_random(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choices(characters, k=length))


print(generate_random(9))

# Applying Algorithm
"""
Linear congruential generator:
- A linear congruential generator (LCG) is an algorithm that yields a sequence of pseudo-randomized 
    numbers calculated with a discontinuous piecewise linear equation. 
- The method represents one of the oldest and best-known pseudorandom number generator algorithms. 
- The theory behind them is relatively easy to understand, and they are easily implemented and fast, 
    especially on computer hardware which can provide modular arithmetic by storage-bit truncation.
    x(n+1) = (a * x(n) + c) mod m
"""


def random_character(characterValue):

    a = 65879
    c = 56465431307098098
    m = 2**32
    characters = (a * characterValue + c) % m
    return characters


def generate_random_algo(length=9):
    characters = string.ascii_letters + string.digits + string.punctuation
    characterValue = 12568
    random_string = ""
    for _ in range(length):
        characterValue = random_character(characterValue)
        index = characterValue % len(characters)
        random_string += characters[index]
    return random_string


# print(random_character(12345))
print(generate_random_algo(78))
