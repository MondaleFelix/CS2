histogram = []
counter = 0

with open("fish.txt", "r") as f:
    f_contents = f.read()
    f_contents = f_contents.strip("\n")
    f_contents = f_contents.split(" ")
    print(f_contents)

    # # for word in f_contents:
    #     word.replace('\n', '')


    # for word in f_contents:
    #     first_word = f_contents[f_contents.index(word)]
    #     count = f_contents.count(word)
    #     histogram.append([first_word,count])
    #     if count != 1:
    #         f_contents.remove(word)
    #     print(f_contents)


    # print(histogram)
