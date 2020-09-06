#Error handling in Python
#Important: The indentation space I've used here is 2. You'll need to make the changes, if any on your compiler!



try:
  a = int(input("Enter an integer"))
  if a < 0:
    raise ValueError
except ValueError:
  print("Bad input")
except KeyboardInterrupt:
  print("You pressed Ctrl+C")
else:
  print("No errors")
finally:
  print("Program finished successfully")
  
