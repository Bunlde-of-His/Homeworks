def my_zip(*args):
    min_length = min(len(element) for element in args)
    return list(tuple(element[i] for element in args) for i in range(min_length))

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = (10, 20, 30)


print(my_zip(a, b, c))
print(list(zip(a, b, c)))





















