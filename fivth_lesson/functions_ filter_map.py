def is_simple(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == False:
            return False
    return True

prime_list = list(filter(is_simple, range(51)))
print(prime_list)

def my_square(num):
    return num ** 2

squared_numbers = list(map(my_square, prime_list))
print(squared_numbers)



















