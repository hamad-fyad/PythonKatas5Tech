import unittest
from katas.time_me import measure_execution_time, sample_function, quick_function
import math 

class Test_time_me(unittest.TestCase):
    def test_time_me(self):

        self.assertEqual(math.isclose(measure_execution_time(sample_function),500,rel_tol=10),True)
      
        self.assertEqual(math.isclose(measure_execution_time(quick_function),0,rel_tol=2), True)
      
        
