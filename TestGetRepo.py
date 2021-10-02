from typing import Type
from requests.api import get
from GetRepo import get_repos
import unittest

class TestGetRepo(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testValidRepoReturn(self):

        expected =  {'CS559_MachineLearning': 8,

   'Complexity': 46,

   'DesignPatternPractice': 1,

   'GEDCOM_database': 3,

    'GitHubAPI567': 4,

   'HW3_345': 3,

   'HW4-345': 5,

   'HW4_345': 1,

   'Is_It_Open': 2,

   'Machine_Learning_Study': 18,

   'NodeJS_app': 2,

   'SSW345-FinalBot': 13,

   'SSW345-HW5': 3,

   'SSW345-HW5-1': 2,

   'SSW533': 3,

   'SSW567': 8,

   'Triangle567': 7,

   'data_analysis': 2,

   'first': 2,

   'gemini_API': 1,

   'joncucci': 7,

   'random_java': 2,

   'random_python': 2,

   'test-HW4-345': 2,

   'workspace': 1}

        self.assertEqual(get_repos('joncucci'), expected, 'Wrong repo and commit combination.')

    def testInvalidUser(self):
        with self.assertRaises(TypeError): get_repos('oienaolzsdktrnaioernf')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()