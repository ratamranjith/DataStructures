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
