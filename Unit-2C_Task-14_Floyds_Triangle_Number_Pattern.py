# Unit-2C_Task-14_Floyds_Triangle_Number_Pattern.py
rows = int(input("Enter the number of rows: "))
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()