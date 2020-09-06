#Functions
#Important: The indentation space I've used here is 2. You'll need to make the changes, if any on your compiler!

def print_message():
  print("Chip is a good squirrel")

print_message()

def print_message1(adjective = "good"):
  print("Chip is a "+adjective+" squirrel")
  
print_message1("cute")
print_message1()

def print_message2(*adjective):
  print("Chip is a "+adjective[2]+" squirrel")
  
print_message2("cute", "clever", "naughty")

def print_message3(**adjective):
  print("Chip is a "+adjective[adj2]+" squirrel")
  
print_message3(adj1 = "cute", adj2 = "clever", adj3 = "squirrel")

