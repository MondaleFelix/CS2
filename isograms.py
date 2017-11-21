def is_isogram(string):
    string_array = list(string)
    repeated_letters = []
    for letter in string_array:
        if string_array.count(letter) > 1:
            repeated_letters.append(letter)

    if len(repeated_letters) > 1:
        print(False)
    else:
        print(True)


is_isogram("Mondale")
