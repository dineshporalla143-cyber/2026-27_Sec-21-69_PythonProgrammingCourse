# Unit-2C_Task-9_Centered_Pyramid_Stars.py
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    print(" " * (rows - i - 1) + "* " * (i + 1))