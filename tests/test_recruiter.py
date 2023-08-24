import unittest
from my_oop import Recruiter


class TestRecruiter(unittest.TestCase):
    def setUp(self):
        self.recruiter = Recruiter("Alice", 150, "alice@example.com")

    def test_work(self):
        self.assertEqual(self.recruiter.work(), "I come to the office. and start to hiring.")

    def test_salary_comparison(self):
        other_recruiter = Recruiter("Bob", 200, "bob@example.com")
        self.assertTrue(self.recruiter < other_recruiter)

    def test_salary_equality(self):
        other_recruiter = Recruiter("Charlie", 150, "charlie@example.com")
        self.assertTrue(self.recruiter == other_recruiter)

    if __name__ == '__main__':
        unittest.main()