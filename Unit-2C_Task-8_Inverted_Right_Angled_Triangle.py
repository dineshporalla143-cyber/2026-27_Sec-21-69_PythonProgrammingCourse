# Unit-2C_Task-8_Inverted_Right_Angled_Triangle.py
rows = int(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()