# import word_frequency
import random

fishy = {"one": 1, "two" : 1, "red": 1, "blue" : 1, "fish": 4}

def get_random_word(dictionary):
    words = sum(dictionary.values())
    random_number = random.randint(1, words)
    for i in dictionary:
        if dictionary[i] < random_number:
            random_number -= dictionary[i]
        else:
            return i



print(get_random_word(fishy))
