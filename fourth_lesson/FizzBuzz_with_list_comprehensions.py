fizz = int(input("Enter your Fizz number: "))
buzz = int(input("Enter your Buzz number: "))
length = int(input("Enter Length of your number list: "))

output = ["FB" if not i % fizz and not i % buzz else "F" if not i % fizz else "B" if not i % buzz else i for i in range(1, length + 1)]


print(output)