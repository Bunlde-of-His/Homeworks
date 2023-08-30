import unittest
from my_oop import Developer


class TestDeveloper(unittest.TestCase):
    def setUp(self):
        self.developer = Developer("Bob", 200, ["Python"], "bob@example.com")

    def test_work(self):
        self.assertEqual(self.developer.work(), "I come to the office. and start to coding.")

    def test_tech_stack_comparison(self):
            other_developer = Developer("Alice", 180, ["Java"], "alice@example.com")
            self.assertFalse(self.developer > other_developer)

    def test_salary_comparison(self):
            other_developer = Developer("Eve", 250, ["JavaScript"], "eve@example.com")
            self.assertFalse(self.developer < other_developer)

    def test_salary_equality(self):
            other_developer = Developer("Mallory", 200, ["Python"], "mallory@example.com")
            self.assertTrue(self.developer == other_developer)

    def test_add_developers(self):
        other_developer = Developer("Charlie", 150, ["Python", "Django"], "charlie@example.com")
        combined_developer = self.developer + other_developer

        expected_name = "Bob Charlie"
        expected_tech_stack = set(["Python", "Django"])
        expected_salary = max(self.developer.salary_per_day, other_developer.salary_per_day)

        self.assertEqual(combined_developer.name, expected_name)
        self.assertEqual(set(combined_developer.tech_stack), expected_tech_stack)
        self.assertEqual(combined_developer.salary_per_day, expected_salary)


    if __name__ == '__main__':
        unittest.main()
