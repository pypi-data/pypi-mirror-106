import random

def construct_random_letter(seed):
    letters = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(1,seed):
        string = random.choice(letters)
        return string


print(construct_random_letter(2))