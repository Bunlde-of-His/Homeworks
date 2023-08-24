import unittest
from my_module import Developer  # Import your classes here


class TestDeveloper(unittest.TestCase):
    def setUp(self):
        self.developer = Developer("Bob", 200, ["Python"], "bob@example.com")

    def test_work(self):
        self.assertEqual(self.developer.work(), "I come to the office. and start to coding.")

    def test_add_developer(self):
        other_developer = Developer("Charlie", 150, ["Django", "Python"], "charlie@example.com")
        combined_developer = self.developer + other_developer
        self.assertEqual(combined_developer.tech_stack, ['Python', 'Django'])

    # Add more test methods for other Developer methods and behaviors

