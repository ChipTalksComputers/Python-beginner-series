#While loop 

i = 0
while i!=8:
  print(i)
  i += 1

#break
while i!=8:
  print(i)
  break
  i+=1

#continue  
while i!=8:
  if i == 4:
    i += 1
    continue
  else:
    print(i)
    continue
    
#pass
while i!=8:
  if i == 4:
    pass
  else:
    print(i)
  i+=1
  
#while-else
while i!= 8:
  print(i)
  i+=1
else:
  print("While loop completed successfully")
