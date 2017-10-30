import random, sys
sentence = []

with open('/usr/share/dict/words', 'r') as f:
    f_contents = f.readlines()

    def new_sentence(number):
        for i in range(number):
            random_index = random.randint(0,len(f_contents))
            sentence.append(f_contents[random_index])

        print(sentence)

        for word in sentence:
            new_word = word.replace("\n","")
            sentence.append(new_word)
            sentence.pop(0)

        egg = " ".join(sentence)
        print(egg)
        return sentence

number_argument = sys.argv[1]
new_sentence(int(number_argument))

