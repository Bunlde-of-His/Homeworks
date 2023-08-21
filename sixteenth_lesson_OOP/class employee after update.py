from datetime import datetime, timedelta

class Employee:
    WORKING_DAYS_PER_MONTH = 20
    WORKING_DAYS_PER_WEEK = 5

    def __init__(self, name, salary_per_day):
        self.name = name
        self.salary_per_day = salary_per_day

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
    def __init__(self, name, salary_per_day, tech_stack, *args, **kwargs):
        super().__init__(name, salary_per_day, *args, **kwargs)
        self.tech_stack = tech_stack

    def work(self):
        return super().work() + ' and start to coding.'

    def __add__(self, other):
        new_name = f"{self.name} {other.name}"
        new_tech_stack = list(set(self.tech_stack + other.tech_stack))
        new_salary_per_day = max(self.salary_per_day, other.salary_per_day)
        return Developer(new_name, new_salary_per_day, new_tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)


# Create instances
recruiter_1 = Recruiter('Recruiter - Jane', 80)
dev1 = Developer("Developer - John", 100, ["Python", "JavaScript"])
dev2 = Developer("Developer - Alice", 120, ["Python", "Java", "Psql"])
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



