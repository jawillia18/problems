import super_algos
import unittest
from unittest.mock import patch
from io import StringIO
import sys

class  MyTestC(unittest.TestCase):
    
    def test_min(self):

        element = ["a",2,3,4]
        self.assertEqual(super_algos.find_min(element), -1)
        self.assertEqual(super_algos.find_min([]), -1)
        self.assertEqual(super_algos.find_min([3,4,7,2,6]),2)

    def test_sum(self):
        element2 = ["a",2,3,4]
        self.assertEqual(super_algos.sum_all(element2), -1)
        self.assertEqual(super_algos.sum_all([]), -1)
        self.assertEqual(super_algos.sum_all([1+2+3+4]),10)

