mode = input("Enter 'e' to encrypt, or 'd' to decrypt: ")
input_key = input("Enter the key: ")
plain_text = input("Enter a string: ")
cipher_text = ""
i = 0

for char in plain_text:
    if char.isalpha():
        if mode == 'e':
            char = chr((ord(char) - ord('a') + ord(input_key[i % len(input_key)]) - ord('a')) % 26 + ord('a'))
        elif mode == 'd':
            char = chr((ord(char) - ord('a') - (ord(input_key[i % len(input_key)]) - ord('a'))) % 26 + ord('a'))
        cipher_text += char
        i += 1
    else:
        cipher_text += char

print(cipher_text)