user_number = int(input("Enter your number: "))

dividers = [i for i in range(1, user_number + 1) if not user_number % i]

print("Dividers of your number", user_number, ":")
print(dividers)