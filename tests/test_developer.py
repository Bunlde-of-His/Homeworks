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

    if __name__ == '__main__':
        unittest.main()


    # Add more test methods for other Developer methods and behaviors

