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
from .EI import all_tests as ei_tests
from .FeWI import all_tests as fewi_tests
from .PWI import all_tests as pwi_tests

from . import test_mrk_detail_links
from . import test_private_data
from . import test_snp_build_numbers

# add the test suites
def master_suite():
    suites = []
    # run all EmapA test suites
    suites.append(ei_tests.master_suite())
    suites.append(fewi_tests.master_suite())
    suites.append(pwi_tests.master_suite())
    
    suites.append(test_mrk_detail_links.suite())
    suites.append(test_private_data.suite())
    suites.append(test_snp_build_numbers.suite())

    master_suite = unittest.TestSuite(suites)
    return master_suite

if __name__ == '__main__':
    test_suite = master_suite()
    runner = unittest.TextTestRunner()

    ret = not runner.run(test_suite).wasSuccessful()
    sys.exit(ret)
