import csv
import requests

class CandidateManager:
    @classmethod
    def generate_candidates_from_web(cls, source):
        response = requests.get(source)
        lines = response.text.split('\n')
        return cls._generate_candidates(lines)
    
    @classmethod
    def generate_candidates_from_file(cls, source):
        with open(source, 'r') as file:
            lines = file.readlines()
        return cls._generate_candidates(lines)
    
    @classmethod
    def _generate_candidates(cls, lines):
        candidates = []
        reader = csv.DictReader(lines)
        for row in reader:
            candidate = Candidate(row['Full Name'], row['Email'],
                                  row['Technologies'], row['Main Skill'], row['Main Skill Grade'])
            candidates.append(candidate)
        return candidates

class Candidate:
    def __init__(self, full_name, email, tech_stack, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade
    
    @property
    def first_last_name(self):
        names = self.full_name.split()
        if len(names) >= 2:
            return names[0] + ' ' + names[-1]
        return self.full_name
    
    def __str__(self):
        return (
            f"Full Name: {self.full_name}\n"
            f"Email: {self.email}\n"
            f"Tech Stack: {self.tech_stack}\n"
            f"Main Skill: {self.main_skill}\n"
            f"Main Skill Grade: {self.main_skill_grade}"
        )

candidates = CandidateManager.generate_candidates_from_web("https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv")
for candidate in candidates:
    print(candidate)
    print()






