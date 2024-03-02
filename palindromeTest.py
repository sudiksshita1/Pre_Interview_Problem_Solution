import unittest
from util.palindrome import Integer

class TestIntegerClass(unittest.TestCase):
    def test_is_palindrome(self):
        n1 = Integer(121)
        self.assertTrue(n1.is_palindrome())
        n2 = Integer(123)
        self.assertFalse(n2.is_palindrome())

if __name__ == '__main__':
    unittest.main()