# Unit-2C_Task-11_Hollow_Diamond_Stars.py
rows = int(input("Enter the number of rows (half-height): "))

# Upper hollow pyramid
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower inverted hollow pyramid
for i in range(rows - 2, -1, -1):
    print(" " * (rows - i - 1), end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")
    print()