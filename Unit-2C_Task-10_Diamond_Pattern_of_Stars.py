# Unit-2C_Task-10_Diamond_Pattern_Stars.py
rows = int(input("Enter the number of rows (half-height of diamond): "))

# Upper pyramid
for i in range(rows):
    print(" " * (rows - i - 1) + "* " * (i + 1))

# Lower inverted pyramid
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)