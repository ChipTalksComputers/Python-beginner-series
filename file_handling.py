#File handling

#Open a file to read it

file = open('{file_path}', mode = 'r')

print(file.read())

print(file.read(3))

file.close()


#Open a file to write to it

file = open('{file_path}', mode = 'w') #Overwrite

file = open('{file_path}', mode = 'a') #Append

file.write('{your_message}')

file.close()


#Creating a file

file = open('{file_path}', mode = 'x')  #Just create

file = open('{file_path}', mode = 'w')  #Create and overwrite

file = open('{file_path}', mode = 'a')  #Create and append


#Deleting a file

import os

os.remove('{file_path}')  #Permanently delete the file




