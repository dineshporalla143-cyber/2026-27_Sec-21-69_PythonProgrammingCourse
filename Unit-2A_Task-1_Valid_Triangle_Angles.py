a=int(input("Enter the 1st angle:"))
b=int(input("Enter the 2nd angle:"))
c=int(input("Enter the 3rd angle:"))
if a>0 and b>0 and c>0 and a+b+c==180:
    print("valid triangle")
else:
    print("not valid triangle")