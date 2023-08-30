import csv
import requests

class Candidate:
    def __init__(self, full_name, email, tech_stack, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade
    
    def __str__(self):
        return (
            f"Full Name: {self.full_name}\n"
            f"Email: {self.email}\n"
            f"Tech Stack: {self.tech_stack}\n"
            f"Main Skill: {self.main_skill}\n"
            f"Main Skill Grade: {self.main_skill_grade}"
        )

    
    @classmethod
    def generate_candidates(cls, source):
        candidates = []

        if source.startswith("http://") or source.startswith("https://"):
            response = requests.get(source)
            lines = response.text.split('\n')
        else:
            with open(source, 'r') as file:
                lines = file.readlines()
        
        reader = csv.DictReader(lines)
        for row in reader:
            candidate = cls(row['Full Name'], row['Email'],
                            row['Technologies'], row['Main Skill'], row['Main Skill Grade'])
            candidates.append(candidate)
        
        return candidates


candidates = Candidate.generate_candidates("https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv")
for candidate in candidates:
    print(candidate)
    print()






