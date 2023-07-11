with open("numbers.txt", "r") as file:
    for line in file:
        nums = list(map(int, line.strip().split()))
        fizz = nums[0]
        buzz = nums[1]
        length = nums[2]

        for i in range(1, length + 1):
            if i % fizz == 0 and i % buzz == 0:
                print("FB")
            elif i % fizz == 0:
                print("F")
            elif i % buzz == 0:
                print("B")
            else:
                print(i)













