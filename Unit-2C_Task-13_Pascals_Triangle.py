# Unit-2C_Task-13_Pascals_Triangle.py
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    print("  " * (rows - i - 1), end="")
    val = 1
    for j in range(i + 1):
        print(f"{val:3}", end=" ")
        val = val * (i - j) // (j + 1)
    print()