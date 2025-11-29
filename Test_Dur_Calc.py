# This file is a unit test for the duration calc 


import unittest 
import numpy as np
from DurationCalc import dur_calc
from unittest.mock import patch

class my_unit_tests(unittest.TestCase):
    
    @patch("fake.input", return_value="2025-10-01")
    def test_date_calc(self):
        '''
        Function checks that the difference between user input and todays date is correct 
        Using a mock user input

        '''

        today = np.datetime64("today")
        assumed_result = np.datetime64("20025-10-01") - today

        actual_result = dur_calc()
    
        self.assertEqual(assumed_result,assumed_result)

        

# run the tests
if __name__ == "__main__":
    unittest.main()