# Unit-2C_Task-12_Centered_Number_Pyramid.py
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    # Print leading spaces
    print("  " * (rows - i - 1), end="")
    # Print increasing numbers
    for j in range(1, i + 2):
        print(j, end=" ")
    # Print decreasing numbers
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()