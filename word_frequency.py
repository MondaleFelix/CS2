import random

def dictionary(f_contents):
    histogram = {}
    for word in f_contents:
        first_word = f_contents[f_contents.index(word)]
        count = f_contents.count(word)
        histogram[first_word] = count
    return histogram



def nested_array(f_contents):
    histogram = []
    for word in f_contents:
        first_word = f_contents[f_contents.index(word)]
        count = f_contents.count(word)
        histogram.append([first_word, count])

    for content_list in histogram:
        count = histogram.count(content_list)
        if count != 1:
            histogram.remove(content_list)
    print(histogram)
    return histogram

# def stochastic_sampling(weighted_hist):
#     rand_float = random.uniform(0,1)
#     cum_weight = 0
#     for word in weighted_hist:
#         cum_weight += word[1]
#         print(cum_weight)

# def weight_array(f_contents):
#     weighted_hist = []
#     total = sum([word[1] for word in f_contents])
#     for word in f_contents:
#         weighted_hist.append([word[0],word[1]/total])
#     print(weighted_hist)
#     return weighted_hist



def tuple_list(f_contents):
    histogram = []
    for word in f_contents:
        first_word = f_contents[f_contents.index(word)]
        count = f_contents.count(word)
        histogram.append((first_word, count))

    for content_list in histogram:
        count = histogram.count(content_list)
        if count != 1:
            histogram.remove(content_list)
    print(histogram)

def open_file(file_name):
    with open(file_name, "r") as f:
        f_contents = f.read().rstrip().split()
    return f_contents

words_list = open_file("fish.txt")
# egg = weight_array(arr)
# stochastic_sampling(egg)
# tuple_list(words_list)
print(dictionary(words_list))
# nested_array(words_list)
