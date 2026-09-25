# cipher_text = input("Enter the Caesar-ciphered text: ")

# for test_key in range(1, 26):
#     decrypted_text = ""
    
#     for char in cipher_text:
#         if char.isalpha():
#             if char.islower():
#                 base = ord('a')
#             else:
#                 base = ord('A')

#             decrypted_char = chr((ord(char) - base - test_key) % 26 + base)
#             decrypted_text += decrypted_char
#         else:
#             decrypted_text += char
            
#     print(f"Key {test_key:2}: {decrypted_text}")




cipher_text = input("Enter the Caesar-ciphered text: ")
decrypted_text = "" 
