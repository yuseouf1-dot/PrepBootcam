cipher_text = input("Enter the cipher text: ")
key_length = int(input("Enter the length of the key: "))

alpha_only = ""
for char in cipher_text:
    if char.isalpha():
        alpha_only += char.lower()

groups = []
for i in range(key_length):
    group = alpha_only[i::key_length]
    groups.append(group)

found_key = ""
for group in groups:
    most_frequent_char = max(group, key=group.count)    
    shift_amount = (ord(most_frequent_char) - ord('e')) % 26
    key_char = chr(shift_amount + ord('a'))
    found_key += key_char

print(f"Key: {found_key}")

decrypted_text = ""
key_index = 0

for char in cipher_text:
    if char.isalpha():
        if char.islower():
            base = ord('a')
        else:
            base = ord('A')
            
        decrypted_char = chr((ord(char) - base - (ord(found_key[key_index % key_length]) - ord('a'))) % 26 + base)
        decrypted_text += decrypted_char
        key_index += 1
    else:
        decrypted_text += char

print(f"Decrypted text: {decrypted_text}")