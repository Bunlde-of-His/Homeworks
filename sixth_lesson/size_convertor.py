
sizes = {
    'XXS': {'Ukraine': '38', 'Germany': '36', 'USA': '8', 'France': '38', 'Great Britain': '24'},
    'XS': {'Ukraine': '40', 'Germany': '38', 'USA': '10', 'France': '38', 'Great Britain': '26'},
    'S': {'Ukraine': '42', 'Germany': '40', 'USA': '12', 'France': '38', 'Great Britain': '28'},
    'M': {'Ukraine': '44', 'Germany': '42', 'USA': '14', 'France': '38', 'Great Britain': '30'},
    'L': {'Ukraine': '46', 'Germany': '44', 'USA': '16', 'France': '38', 'Great Britain': '32'},
    'XL': {'Ukraine': '48', 'Germany': '46', 'USA': '18', 'France': '38', 'Great Britain': '34'},
    'XXL': {'Ukraine': '50', 'Germany': '48', 'USA': '20', 'France': '38', 'Great Britain': '36'},
    'XXXL': {'Ukraine': '52', 'Germany': '50', 'USA': '22', 'France': '38', 'Great Britain': '38'}
}

def size_convertor(international_size, system):
    if international_size in sizes and system in sizes[international_size]:
        return sizes[international_size][system]
    return "Size is not found"

international_size = input("Enter your international size: ")

system = input("Enter name of your country: ")

result = size_convertor(international_size, system)
print(f'Your size is {result}')





















