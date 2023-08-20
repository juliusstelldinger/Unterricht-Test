import unittest

from main import quadrizzle

class TestQuadrizzle(unittest.TestCase):
    
    def test_two_squared_is_four(self):
        # arrange
        
        # act
        result = quadrizzle(2)
        
        # assert
        self.assertEqual(result, 4)
        
if __name__ == "__main__":
    unittest.main()