# Unit-2D_Task-3_String_Palindrome.py
text = input("Enter a string: ")
# Remove spaces and convert to lowercase for accurate check
cleaned = "".join(text.lower().split())

if cleaned == cleaned[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")