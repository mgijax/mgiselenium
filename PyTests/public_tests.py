"""
Run all public WI related test suites
"""
import sys,os.path

# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../',)
)
import config

import unittest
import tracemalloc
from jd_HTMLTestRunner import HTMLTestRunner
# import all sub test suites
from .FeWI import all_tests as fewi_tests

import test_mrk_detail_links
import test_private_data
import test_snp_build_numbers

# add the test suites
def master_suite():
    suites = []
    # run all EmapA test suites
    suites.append(fewi_tests.master_suite())
    
    suites.append(test_mrk_detail_links.suite())
    suites.append(test_private_data.suite())
    suites.append(test_snp_build_numbers.suite())

    master_suite = unittest.TestSuite(suites)
    return master_suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))

    ret = not runner.run(test_suite).wasSuccessful()
    sys.exit(ret)
