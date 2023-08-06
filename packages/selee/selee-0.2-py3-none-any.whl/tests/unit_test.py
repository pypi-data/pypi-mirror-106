import unittest 
from selee import selee_module

class TestCases(unittest.TestCase):
    
    # Test case for non-integer input
    def test_float(self):
        self.assertEqual(selee_module.fizz_buzz(1.2),1.2)
    
    # Test case for negative integer input
    def test_negative(self):
        self.assertEqual(selee_module.fizz_buzz(-1),-1)

    # Test case for integer divisible by 3
    def test_divisibleBy3(self):
        self.assertEqual(selee_module.fizz_buzz(3),'Fizz')
    
    # Test case for integer divisible by 5
    def test_divisibleBy5(self):
        self.assertEqual(selee_module.fizz_buzz(5),'Buzz')

    # Test case for integer divisible by 3 and 5
    def test_divisibleByAll(self):
        self.assertEqual(selee_module.fizz_buzz(15),'FizzBuzz')
    
    # Test case for integer not divisible by 3 and 5 
    def test_integer(self):
        self.assertEqual(selee_module.fizz_buzz(4),4)
    
    # Test case for 0
    def test_integer(self):
        self.assertEqual(selee_module.fizz_buzz(0),0)
        

# run unittest
if __name__ == '__main__':
    unittest.main()