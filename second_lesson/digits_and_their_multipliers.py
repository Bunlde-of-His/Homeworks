user_number = input("Enter your number: ") 

result = ""  

for i, digit in enumerate(user_number):
    exponent = len(user_number) - i - 1
    result += f"{digit} * 10^{exponent} + " if exponent != 0 else f"{digit} * 10^{exponent}"
    
# В цій задачі я використував альтернативний запис if, який був частиной домашнього завдання 

print("Your result:", result)  



