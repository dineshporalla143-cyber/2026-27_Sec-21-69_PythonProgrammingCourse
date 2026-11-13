year = int(input("Enter the year:"))

if year < 1 or year > 100: 
    print(f"{year} is not between 1 and 100")
elif year == 1:  
    print(f"{year} is not a prime number")
elif year in [2, 3, 5, 7]: 
    print(f"{year} is a prime number")
elif year % 2 == 0 or year % 3 == 0 or year % 5 == 0 or year % 7 == 0: 
    print(f"{year} is not a prime number")
else:
    print(f"{year} is a prime number")