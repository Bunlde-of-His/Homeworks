output_file = "output.txt"

with open("numbers.txt", "r") as file:
    with open(output_file, "w") as output:
        for line in file:
            nums = list(map(int, line.strip().split()))
            fizz = nums[0]
            buzz = nums[1]
            length = nums[2]

            for i in range(1, length + 1):
                if i % fizz == 0 and i % buzz == 0:
                    output.write("FB\n")
                elif i % fizz == 0:
                    output.write("F\n")
                elif i % buzz == 0:
                    output.write("B\n")
                else:
                    output.write(str(i) + "\n")
