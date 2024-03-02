import unittest
from util import swapNumbers

class TestSwapVariables(unittest.TestCase):
    def test_swap_variables(self):
        arr = [5, 10]
        swapNumbers.swap_variables(arr)
        self.assertEqual(arr, [10, 5])

if __name__ == '__main__':
    unittest.main()
