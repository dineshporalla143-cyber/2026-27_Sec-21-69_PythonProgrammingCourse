# Unit-2C_Task-5_Star_Grid_User_Input.py
rows = int(input("Enter the grid size: "))
for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()