"""
Run all PWI/EI test suites
@Note: this test suite does not work currently
"""
import sys,os.path

# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config

import unittest
import tracemalloc
# import all sub test suites
import private_allele
import Emapa_Browser
import QTL_allele_detail
import gxd_image_summary
import test_emboss_data
from HTMLTestRunner import HTMLTestRunner
# add the test suites
def master_suite():
    suites = []
    
    suites.append(Emapa_Browser.suite())
    suites.append(private_allele.suite())
    suites.append(QTL_allele_detail.suite())
    suites.append(gxd_image_summary.suite())
    suites.append(test_emboss_data.suite())

    master_suite = unittest.TestSuite(suites)
    return master_suite

if __name__ == '__main__':
    test_suite = master_suite()
    runner = unittest.TextTestRunner()

    ret = not runner.run(test_suite).wasSuccessful()
    sys.exit(ret)
