# Unit-2D_Task-5_Count_Vowels_Consonants_Digits_Spaces.py
text = input("Enter a string: ")
vowels = consonants = digits = spaces = 0

for char in text:
    if char.isspace():
        spaces += 1
    elif char.isdigit():
        digits += 1
    elif char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")