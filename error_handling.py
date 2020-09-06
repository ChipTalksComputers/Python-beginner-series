#Error handling in Python

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
  
