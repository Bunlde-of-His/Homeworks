import unittest
from unittest.mock import patch
from my_oop import Candidate

class TestCandidate(unittest.TestCase):

    @classmethod
    @patch("my_oop.requests.get")
    def setUpClass(cls, mock_get):
        mock_get.return_value.text = (
            "Full Name,Email,Technologies,Main Skill,Main Skill Grade\n"
            "Ivan Chechov,ichech@example.com,Python|Django|Angular,Python,Senior\n"
            "Max Payne,mpayne@example.com,PHP|Laravel|MySQL,PHP,Middle\n"
            "Tom Hanks,thanks@example.com,Python|CSS,Python,Junior\n"
        )
        cls.candidates = Candidate.generate_candidates("https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv")

    def test_generate_candidates(self):
        self.assertEqual(len(self.candidates), 3)
        self.assertEqual(self.candidates[0].full_name, "Ivan Chechov")
        self.assertEqual(self.candidates[0].email, "ichech@example.com")
        self.assertEqual(self.candidates[0].tech_stack, "Python|Django|Angular")  


if __name__ == '__main__':
    unittest.main()
