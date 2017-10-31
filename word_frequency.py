histogram = []
counter = 0

with open("fish.txt", "r") as f:
    f_contents = f.read()
    f_contents = f_contents.strip("\n")
    f_contents = f_contents.split(" ")

    for word in f_contents:
        first_word = f_contents[f_contents.index(word)]
        count = f_contents.count(word)
        histogram.append([first_word,count])

    for content_list in histogram:
        count = histogram.count(content_list)
        if count != 1:
            histogram.remove(content_list)
    print(histogram)

    # print(f_contents)
    # print(histogram)
