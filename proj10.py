#Loops in Python
#For loop

numbers = ['5', '3', '2']

for number in numbers:
    print(number)
    
for i in range(7):
    print(i)
    
for i in range(7):
    if i == 4:
        break
    print(i)
else:
    print('For loop completed successfully')   #This won't get printed!
for i in range(7):
    if i == 4:
        continue
for i in range(7):
    if i == 4:
        pass
    else:
        print(i)
        
   
