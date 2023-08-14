class Employee:
    def __init__(self, name, salary_per_day):
        self.name = name
        self.salary_per_day = salary_per_day

    def work(self):
        self.notification = "I come to the office."
        return self.notification
    
    def __str__(self):
       return f'My Position is {self.name}!'


class Recruiter(Employee):
    def work(self):
        return 'I come to the office and start to hiring.'

class Developer(Employee):
    def work(self):
        return 'I come to the office and start to coding.'


def salary_comparing(first_salary, second_salary):
    if first_salary > second_salary:
        return 'Recruiter earn more money!'
    elif first_salary < second_salary:
        return 'Developer earn more money!'
    else:
        return 'Both salaries are equal!'


recruiter_1 = Recruiter('Recruiter', 15)
developer_1 = Developer('Developer', 20)

print(recruiter_1.work())
print(recruiter_1.__str__())
print(developer_1.work())
print(developer_1.__str__())

print(salary_comparing(recruiter_1.salary_per_day, developer_1.salary_per_day))
