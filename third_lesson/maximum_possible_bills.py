def issues_of_the_bills(amount):
    denominations = [1000, 500, 200, 100, 50, 20, 10]
    notes = {}

    for el in denominations:
        if amount >= el:
            count = amount // el
            amount %= el
            notes[el] = count

    return notes

withdraw_amount = int(input("Enter the amount to withdraw: "))
result = issues_of_the_bills(withdraw_amount)
print("Bill distribution: ")
for el, count in result.items():
    print(f"{el} UAH: {count} counts.")