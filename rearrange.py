import sys
import random


words_list = sys.argv[1:]

def mix_words():
    scrambled_words = []
    for i in words_list:
        scrambled_words.insert(random.randint(0,len(words_list)), i)

    print(scrambled_words)

mi_words()
