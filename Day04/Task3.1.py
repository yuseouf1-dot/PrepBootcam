input_key = int(input("Enter an integer: "))
input_string = input("Enter a string: ")
result = "" 
alphabet = "abcdefghijklmnopqrstuvwxyz"

for char in input_string:
    if char in alphabet:
        current_index = alphabet.find(char)
        new_index = (current_index + input_key) % 26
        result += alphabet[new_index]
    else:
        result += char
        
print(result)