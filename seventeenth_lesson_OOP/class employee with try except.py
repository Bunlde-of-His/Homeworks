from datetime import datetime, timedelta
import csv
import traceback

class EmailAlreadyExistsException(Exception):
    pass

class Employee:
    WORKING_DAYS_PER_MONTH = 20
    WORKING_DAYS_PER_WEEK = 5

    def __init__(self, name, salary_per_day, email):
        self.name = name
        self.salary_per_day = salary_per_day
        self.email = email
        self.save_email()
        self.validate()

    def work(self):
        self.notification = "I come to the office."
        return self.notification

    def check_salary(self):
        today = datetime.today()
        start_of_month = datetime(today.year, today.month, 1)

        days_worked = 0
        current_day = start_of_month
        while current_day <= today:
            if current_day.weekday() < self.WORKING_DAYS_PER_WEEK:  # 0-Monday, 4-Friday
                days_worked += 1
            current_day += timedelta(days=1)

        total_salary = days_worked * self.salary_per_day
        return f'My total salary is {total_salary}$'

    def __str__(self):
        return f"My Position is {self.name}!"

    def save_email(self):
        with open('emails.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.email])

    def validate(self):
        try:
            with open('emails.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if self.email in row:
                        raise EmailAlreadyExistsException("Email already exists")
        except EmailAlreadyExistsException:
            with open('logs.txt', mode='a') as log_file:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                trace = traceback.format_exc()
                log_file.write(f"{timestamp} | {trace}\n")

    def __gt__(self, other):
        return self.salary_per_day > other.salary_per_day
    
    def __lt__(self, other):
        return self.salary_per_day < other.salary_per_day
    
    def __eq__(self, other):
        return self.salary_per_day == other.salary_per_day

class Recruiter(Employee):
    def work(self):
        return super().work() + ' and start to hiring.'

class Developer(Employee):
    def __init__(self, name, salary_per_day, tech_stack, email, *args, **kwargs):
        super().__init__(name, salary_per_day, email, *args, **kwargs)
        self.tech_stack = tech_stack

    def work(self):
        return super().work() + ' and start to coding.'

    def __add__(self, other):
        new_name = f"{self.name} {other.name}"
        new_tech_stack = list(set(self.tech_stack + other.tech_stack))
        new_salary_per_day = max(self.salary_per_day, other.salary_per_day)
        return Developer(new_name, new_salary_per_day, new_tech_stack, self.email)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)


# Create instances
recruiter_1 = Recruiter('Recruiter - Jane', 80, 'jane@example.com')
dev1 = Developer("Developer - John", 100, ["Python", "JavaScript"], 'john@example.com')
dev2 = Developer("Developer - Alice", 120, ["Python", "Java", "Psql"], 'alice@example.com')
print(recruiter_1.work())
print(recruiter_1)
print(recruiter_1.check_salary())
print(dev1.work())
print(dev1)
print(dev1.check_salary())
print(dev2.work())
print(dev2)
print(dev2.check_salary())

# Combine developers
combined_dev = dev1 + dev2
print(f"Combined Developer: {combined_dev.name}")
print(f"Combined Tech Stack: {combined_dev.tech_stack}")
print(f"Combined Salary: {dev1.salary_per_day + dev2.salary_per_day}")

# Compare salaries
if recruiter_1 > dev1:
    print('Recruiter earn more money than Developer!')
elif recruiter_1 < dev1:
    print('Developer earn more money than Recruiter!')
else:
    print('Both salaries are equal!')

# Compare developers by the number of technologies
if dev1 > dev2:
    print(f"{dev1.name} knows more technologies than {dev2.name}")
elif dev1 < dev2:
    print(f"{dev2.name} knows more technologies than {dev1.name}")
else:
    print(f"{dev1.name} and {dev2.name} know the same number of technologies")


