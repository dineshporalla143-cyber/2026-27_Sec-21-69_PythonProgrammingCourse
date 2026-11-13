# Unit-2C_Task-6_Hollow_Star_Grid_User_Input.py
rows = int(input("Enter the grid size: "))
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end=" ")
        else:
            print("  ", end="")
    print()