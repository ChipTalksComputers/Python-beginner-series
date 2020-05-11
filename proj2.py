greeting = 'Hello wassup'
name = 'Chip'

#OUTPUT FUNCTION PRINT()

#Usual output
print(greeting, 'my name is', name)

#Using sep parameter(separate by comma)
print(greeting, 'my name is', name, sep=',')

#Using end parameter(end with a space)
print(greeting, 'my name is', name, end=' ')
print('Hi')

#Formatted output
print(f'{greeting}, my name is {name}')

#format() function
print('{}, my name is {}'.format(greeting, name))


#INPUT FUNCTION INPUT()

#Input with prompt
greeting = input('Enter any greeting')
name = input("What's your name?")

print(greeting, name)

#eval() function
exp = '5+9'
print(eval(exp))

