#Sets and set methods

numbers = [1,2,3,4]

numbers = set(numbers)

print(numbers)

numbers.add(5)

print(numbers)

numbers.remove(4)

print(numbers)

numbers1 = {5,6,7,2}

print(numbers.union(numbers1))

print(numbers.intersection(numbers1))

print(numbers.issubset(numbers1))

print(numbers.issuperset(numbers1))

print(numbers.isdisjoint(numbers1))

print(numbers.difference(numbers1))

numbers.clear()

print(numbers)

