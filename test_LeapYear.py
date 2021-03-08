import unittest
import LeapYear


class FizzBuzzTestCases(unittest.TestCase):

    def test1(self):
        self.assertEqual(LeapYear.LeapYear(2003),"Not a leap year")
    
    
if __name__ == "__main__":
    unittest.main()

