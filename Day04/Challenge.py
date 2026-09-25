user_input = input("Enter integer and string :")
a, b = user_input.split(" ")
a = int(a)

if a == 0 :
    quit()

has_vowel = False
for char in b:
    if char in "aeiou":
        has_vowel = True
        break  

if has_vowel or a >= 42:
    print(a)
else :
    print(b)


