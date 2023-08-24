import unittest
from datetime import datetime, timedelta
from unittest.mock import patch
from my_oop import Employee


class TestEmployee(unittest.TestCase):

    @patch("my_oop.datetime")
    def test_work(self, mock_datetime):
        mock_datetime.today.return_value = datetime(2023, 6, 15)

        emp = Employee("John", 100, "john@example.com")
        self.assertEqual(emp.work(), "I come to the office.")

    def test_save_email(self):
        emp = Employee("Alice", 120, "alice@example.com")
        emp.save_email()

        emails = emp.get_emails()
        self.assertTrue("alice@example.com" in emails)


        with open("emails.csv", "w"):
            pass
        with open("logs.txt", "w"):
            pass

    def test_gt(self):
        emp1 = Employee("Employee 1", 200, "emp1@example.com")
        emp2 = Employee("Employee 2", 150, "emp2@example.com")
        self.assertTrue(emp1 > emp2)

    def test_lt(self):
        emp1 = Employee("Employee 1", 200, "emp1@example.com")
        emp2 = Employee("Employee 2", 250, "emp2@example.com")
        self.assertTrue(emp1 < emp2)

    def test_eq(self):
        emp1 = Employee("Employee 1", 200, "emp1@example.com")
        emp2 = Employee("Employee 2", 200, "emp2@example.com")
        self.assertTrue(emp1 == emp2)


if __name__ == '__main__':
    unittest.main()


