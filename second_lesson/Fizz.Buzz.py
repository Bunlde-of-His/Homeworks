fizz = int(input("Enter your Fizz number: "))
buzz = int(input("Enter your Buzz number: "))
length = int(input("Enter Length of your number list: "))

for i in range(1, length + 1):
    if i % fizz == 0 and i % buzz == 0:
        print("FB")
    elif i % fizz == 0:
        print("F")
    elif i % buzz == 0:
        print("B")
    else:
        print(i)



