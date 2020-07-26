#Lambda functions

a = lambda x:x+2

print(a(10))

b = list(filter(lambda x:x>0, (100, 200, -5, -1)))

print(b)

c = list(map(lambda x:x>0, (100, 200, -5, -1)))

print(c)

#Bonus example for map

d = list(map(lambda x:x**2, (1, -2, 3, -4)))

print(d)
