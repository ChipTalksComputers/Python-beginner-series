#Taking a number input

num = int(input("Enter a number"))

#The ladder

if num > 0:
    print(f"{num} is positive")
    if num % 2 == 0:
        print(f"{num} is an even positive number")
    else:
        print(f"{num} is an odd positive number}")
elif num == 0:
    print(f"{num} is 0")
    print(f"{num} is even")
else:
    print(f"{num} is a negative number")
  
  
