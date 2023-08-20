import unittest

from main import quadriero


class TestQuadriero(unittest.TestCase):
    
    def test_2_squared_equals_4(self):
        # Arrange
        
        # Act
        result = quadriero(2)
        
        # Assert
        self.assertEqual(result, 4)
        
    def test_0_squared_equals_0(self):
        # Arrange
        
        # Act
        result = quadriero(0)
        
        # Assert
        self.assertEqual(result, 0)
        
    def test_negative_number_squared_equals_positive_number(self):
        # Arrange
        
        # Act
        result = quadriero(-6)
        
        # Assert
        self.assertEqual(result, 36)
        
if __name__ == "__main__":
    unittest.main()