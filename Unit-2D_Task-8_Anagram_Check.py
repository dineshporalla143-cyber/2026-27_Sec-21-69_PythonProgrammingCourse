# Unit-2D_Task-8_Anagram_Check.py
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase
clean1 = "".join(str1.lower().split())
clean2 = "".join(str2.lower().split())

if sorted(clean1) == sorted(clean2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")