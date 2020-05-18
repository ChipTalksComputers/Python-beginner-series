# Logical operators

a = 5
b = 6


# and operator

print(a<b and a!=b) #Returns True if both the statements are True, else False

# or operator

print(a<b or a>b)   #Returns True if any one of the statements is True, else False

# not operator

print(not(a))       #Returns True if False and False if True



# Bitwise operators

#Bitwise &

print(a&b)        #Performs logical multiplication on individual bits

#Bitwise |

print(a|b)        #Performs logical addition on individual bits

#Bitwise ~

print(~a)         #Binary addition of 1 to the bit, with a - sign before the number

#Bitwise ^

print(a^b)        #XOR gives 0 if both bits are 0 else 1

#Bitwise <<

print(a<<b)       #Shifts out 'b' bits from the left and adds 'b' zeros to the right

#Bitwise >>

print(a>>b)       #Shifts out 'b' bits from the right and adds 'b' zeros to the left



#Miscellaneous operators

# is operator

print(a is b)     #Returns True if a is equal to b (same as ==)

# is not operator

print(a is not b) #Returns True if a is not equal to b (same as !=)

#ShortHand operator

a+=b         #Increment a by b and store in a
print(a)

a*=b
print(a)    #Multiply a by b and store in a 
