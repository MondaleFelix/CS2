import sys
import random as r


words_list = sys.argv[1:]

def mix_words():
    scrambled_words = []
    for i in words_list:
        scrambled_words.insert(r.randint(0,len(words_list)), i)

    print(scrambled_words)

mix_words()
