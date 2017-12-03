from architecture import Dictogram
import random


class Markov(object):

    def __init__(self, word_list):
        self.states = self.create_states(word_list)
        self.states_lists_of_counts = self.histogram_states()
    def joiner(word_list):
        """TODO: What it does, what input it takes, and what it returns (if anything)."""
        output = " ".join(word_list)
        output += "."
        return output

    def dict_Histogram(dictogram):
        """TODO: create list of counts type histogram, inputs list of words, returns histogram."""
        tokens = []
        types = []
        for word in dictogram:
            number = dictogram[word]
            if number not in tokens:
                tokens.append(number)
                number_list = (number, [word])
                types.append(number_list)
            else:
                for index in types:
                    if number == index[0]:
                        index[1].append(word)
        return sorted(types)

    def next_word_dict(self, word_list):
        '''take word list, check word after word and create dictionary {word: [words after word]} '''
        word_after_dict = {}
        for i in range(-1, len(word_list)):
            #
            if i == -1:
                word = "START"
                word_after = word_list[i+1]
            elif i == len(word_list)-1:
                word = word_list[i]
                word_after = "STOP"
            else:
                word = word_list[i]
                word_after = word_list[i+1]
            #
            if word not in word_after_dict:
                word_after_dict[word] = [word_after]
            else:
                word_after_dict[word].append(word_after)

        return word_after_dict

    def create_states(self, word_list):
        '''convert list of words after word to histogram of words after word {word: {word after word: tokens}}'''
        word_after_dict = self.next_word_dict(word_list)
        print(word_after_dict)
        states = {}
        for word in word_after_dict:
            states[word] = Dictogram(word_after_dict[word])
        print(states)
        return states

    def histogram_states(self):
        '''convert dictionary type of histogram to list of counts type of histogram {word: [(count, [words after word])]}'''
        states_lists_of_counts = {}
        for word in self.states:
            states_lists_of_counts[word] = self.dict_Histogram(self.states[word])
        print(states_lists_of_counts)
        return states_lists_of_counts

    def calculate_probabilities_dict(self):
        '''calculate probability of each word in each histogram'''
        probabilities_dict = {}
        for word in self.states_lists_of_counts:
            probabilities_dict[word] = sample.probability(self.states[word].tokens, self.states_lists_of_counts[word])
        return probabilities_dict

    def next_word_in(self, word):
        '''pick one word that is after input word based on probabilities'''
        probabilities_dict = self.dict_probability()
        if word in probabilities_dict:
            probabilities = probabilities_dict[word]
            random_number = random.random()
            for i in range(0, len(probabilities)):
                if random_number < probabilities[i]:
                    random_number = random.randint(0, len(self.states_lists_of_counts[word][i][1]) - 1)
                    picked_word = self.states_lists_of_counts[word][i][1][random_number]
                    return picked_word
                else:
                    pass

    def list_words(self, number_of_words):
        '''pick number_of_words words and return list of words, initial word is 'START' and stop picking words when picking 'STOP' '''
        picked_words = []
        word = "START"
        for _ in range(0, number_of_words):
            picked_word = self.next_word_in(word)
            if picked_word == "STOP":
                break
            else:
                picked_words.append(picked_word)
                word = picked_word
        return picked_words


def main():
    fish_text = 'one fish two fish red fish blue fish'
    word_list = fish_text.split()
    markov = Markov(word_list)
    picked_words = markov.list_words(10)
    made_output = output.joiner(picked_words)
    print(made_output)


if __name__ == "__main__":
    main()
