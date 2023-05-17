data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

numbers.remove(6.13)
a = numbers.pop(0)
letters.append(a)
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[1] = 'G'
letters[-2] = 'c'
numbers = [i**2 for i in numbers]
letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)
