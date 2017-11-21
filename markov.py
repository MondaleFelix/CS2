from word_frequency import *
import random

comparison_array = []


def create_array(text_file):
    for word in text_file:
        if len(comparison_array) > 1:
            comparison_array.pop(0)
            comparison_array.append(word)
        else:
            comparison_array.append(word)
        print(comparison_array)

# def markovChain(lst):
#     for word in lst:
#         dictogram = dictionary(lst)
#         if word in dictogram:
#             word =+ 1
#         else:
#             dictogram[word] = Dictogram[word + 1]
#     print(dictogram)


def open_file(file_name):
    with open(file_name, "r") as f:
        f_contents = f.read().rstrip().split()
    return f_contents

words_list = open_file("fish.txt")

markovChain(words_list)
