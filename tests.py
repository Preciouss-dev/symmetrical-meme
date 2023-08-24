import unittest
from unittest.mock import patch
from datetime import datetime

from main import removeExpense

# Assuming you have the functions and variables defined in your code here

class TestRemoveExpense(unittest.TestCase):

    def setUp(self):
        self.expenses = [{'amount': 50.0, 'category': 'Food', 'date': datetime.strptime("2023-08-24", '%Y-%m-%d').date()}]
    
    @patch('builtins.input', side_effect=['1'])
    def test_remove_valid_expense(self, mock_input):
        initial_salary = 1000.0
        salary = initial_salary
        
        with patch('builtins.print'):
            removeExpense(self.expenses)
        
        self.assertEqual(len(self.expenses), 0)
        self.assertEqual(salary, initial_salary)
    
    @patch('builtins.input', side_effect=['0', '2'])
    def test_remove_out_of_range_expense(self, mock_input):
        initial_salary = 1000.0
        salary = initial_salary
        
        with patch('builtins.print'):
            removeExpense(self.expenses)
        
        self.assertEqual(len(self.expenses), 1)
        self.assertEqual(salary, initial_salary)
    
    @patch('builtins.input', side_effect=['invalid', '1'])
    def test_remove_invalid_input(self, mock_input):
        initial_salary = 1000.0
        salary = initial_salary
        
        with patch('builtins.print'):
            removeExpense(self.expenses)
        
        self.assertEqual(len(self.expenses), 0)
        self.assertEqual(salary, initial_salary)
    

if __name__ == '__main__':
    unittest.main()
