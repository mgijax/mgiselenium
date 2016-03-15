"""
Run all PWI/EI test suites
"""
import sys,os.path

# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config

import unittest

# import all sub test suites
from EmapA import all_tests as emapa_tests
import Logintest

# add the test suites
def master_suite():
    suites = []
    # run all EmapA test suites
    suites.append(emapa_tests.master_suite())
    
    suites.append(Logintest.suite())
	
    master_suite = unittest.TestSuite(suites)
    return master_suite

if __name__ == '__main__':
	test_suite = master_suite()
	runner = unittest.TextTestRunner()
	
	ret = not runner.run(test_suite).wasSuccessful()
	sys.exit(ret)
