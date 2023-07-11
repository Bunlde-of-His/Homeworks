user_number = int(input("Enter your number "))

print("Dividers of your number", user_number, ":")
for i in range(1, user_number + 1):
    if user_number % i == 0:
        print(i)