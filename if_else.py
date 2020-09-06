#Taking a number input
#Important: The indentation space I've used here is 2. You'll need to make the changes, if any on your compiler!

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
  
  
