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
import private_allele
import QTL_variant_notes
import test_emboss_data

# add the test suites
def master_suite():
    suites = []
    
    suites.append(private_allele.suite())
    suites.append(QTL_variant_notes.suite())
    suites.append(test_emboss_data.suite())
	
    master_suite = unittest.TestSuite(suites)
    return master_suite

if __name__ == '__main__':
	test_suite = master_suite()
	runner = unittest.TextTestRunner()
	
	ret = not runner.run(test_suite).wasSuccessful()
	sys.exit(ret)
