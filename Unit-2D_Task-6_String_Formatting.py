# Unit-2D_Task-6_String_Formatting.py
name = "Alice"
age = 20
score = 95.5

# 1. % operator
print("1. % operator: Name: %s, Age: %d, Score: %.1f" % (name, age, score))

# 2. format() method
print("2. format() method: Name: {}, Age: {}, Score: {}".format(name, age, score))

# 3. f-strings
print(f"3. f-strings: Name: {name}, Age: {age}, Score: {score}")