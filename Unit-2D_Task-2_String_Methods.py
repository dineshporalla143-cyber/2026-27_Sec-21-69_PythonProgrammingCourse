# Unit-2D_Task-2_String_Methods.py
text = "   Hello, Python World!   "

print("Original:", repr(text))
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Strip:", repr(text.strip()))
print("Split:", text.strip().split(", "))

words = ["Python", "is", "awesome"]
print("Join:", " ".join(words))

print("Replace World with Universe:", text.replace("World", "Universe"))
print("Find 'Python':", text.find("Python"))