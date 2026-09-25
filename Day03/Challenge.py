def count_strings(text):

    total = 0
    text = text.lower()

    total += text.count("cat")
    total += text.count("garden")
    total += text.count("mic")

    total += text.count("tac")
    total += text.count("nedrag")
    total += text.count("cim")

    return total




input_string = input("Enter a string: ")
print("The answer is", count_strings(input_string))