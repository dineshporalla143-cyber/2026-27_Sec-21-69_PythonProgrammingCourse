# Unit-2C_Task-7_Right_Angled_Triangle_Pattern.py
rows = int(input("Enter the number of rows: "))
symbol = input("Enter the symbol to print (e.g. * or 0): ")
for i in range(1, rows + 1):
    for j in range(i):
        print(symbol, end=" ")
    print()