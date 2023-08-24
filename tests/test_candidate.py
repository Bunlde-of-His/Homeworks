import unittest
from my_oop import Candidate

class TestCandidate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.candidates = Candidate.generate_candidates("https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv")

    def test_generate_candidates(self):
        self.assertEqual(len(self.candidates), 3)
        self.assertEqual(self.candidates[0].full_name, "Ivan Chechov")
        self.assertEqual(self.candidates[0].email, "ichech@example.com")
        self.assertEqual(self.candidates[0].tech_stack, "Python|Django|Angular")





    if __name__ == '__main__':
        unittest.main()