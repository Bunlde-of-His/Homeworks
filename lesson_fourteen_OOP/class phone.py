class Phone:
    def __init__(self, number):
        self.number = number
        self.incoming_calls = 0

    def get_number(self):
        return self.number

    def get_incoming_calls(self):
        return self.incoming_calls

    def accept_call(self):
        self.incoming_calls += 1

    def __str__(self):
        return f"Phone number: {self.number}, Incoming calls: {self.incoming_calls}"

def main():
    phones = [
        Phone("47445723222"),
        Phone("86443622226"),
        Phone("78678346675")
    ]

    for phone in phones:
        phone.accept_call()
        phone.accept_call()

    total_incoming_calls = sum([phone.get_incoming_calls() for phone in phones])
    print("Total incoming calls:", total_incoming_calls)

    with open("call_logs.txt", "w") as file:
        file.write("Phone Number, Incoming Calls\n")
        for phone in phones:
            file.write(f"{phone.get_number()},{phone.get_incoming_calls()}\n")

if __name__ == "__main__":
    main()
