#Dictionaries

my_dict = {1:'A', 2:'B', 3:'C'}

print(my_dict)

del my_dict

my_dict = dict([[1, 'A'], [2, 'B'], [3, 'C']])

print(my_dict)

my_dict.pop(1)

print(my_dict)

print(my_dict.popitem())

print(my_dict)

my_dict.update([(2, 'D')])

print(my_dict)

print(my_dict.items())

print(my_dict.values())

print('A' in my_dict.values())

print((1, 'A') in my_dict.items())

clear(my_dict)
