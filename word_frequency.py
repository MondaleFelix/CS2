def dictionary(f_contents):
    histogram = {}
    for word in f_contents:
        first_word = f_contents[f_contents.index(word)]
        count = f_contents.count(word)
        histogram[first_word] = count
    print(histogram)

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

def tuple(f_contents):
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
        f_contents = f.read()
        f_contents = f_contents.strip("\n")
        f_contents = f_contents.split(" ")
    return f_contents

words_list = open_file("fish.txt")
tuple(words_list)
nested_array(words_list)
dictionary(words_list)
