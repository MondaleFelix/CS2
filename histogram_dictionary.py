histogram = []
counter = 1

def open_file(file_name):
    with open(file_name, "r") as f:
        f_contents = f.read()
        f_contents = f_contents.split(" ")

    for word in f_contents:
        histogram.append({word: counter})
    print(histogram)

open_file("fish.txt")
