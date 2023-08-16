class Employee:
    def __init__(self, name, salary_per_day):
        self.name = name
        self.salary_per_day = salary_per_day

    def work(self):
        self.notification = "I come to the office."
        return self.notification
    
    def __str__(self):
        return f'My Position is {self.name}!'
    
    def __gt__(self, other):
        return self.salary_per_day > other.salary_per_day
    
    def __lt__(self, other):
        return self.salary_per_day < other.salary_per_day
    
    def __eq__(self, other):
        return self.salary_per_day == other.salary_per_day


class Recruiter(Employee):
    def work(self):
        return 'I come to the office and start to hiring.'


class Developer(Employee):
    def work(self):
        return 'I come to the office and start to coding.'


recruiter_1 = Recruiter('Recruiter', 15)
developer_1 = Developer('Developer', 20)

print(recruiter_1.work())
print(str(recruiter_1))
print(developer_1.work())
print(str(developer_1))

if recruiter_1 > developer_1:
    print('Recruiter earn more money!')
elif recruiter_1 < developer_1:
    print('Developer earn more money!')
else:
    print('Both salaries are equal!')

