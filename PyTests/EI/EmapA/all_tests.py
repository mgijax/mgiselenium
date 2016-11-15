"""
Run all PWI EMAPA test suites
"""
import sys,os.path

# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../../config',)
)
import config

import unittest

# import all sub test suites
import emapaclipboardtest
import emapadetailtest
import emapatreeviewtest
from EI.EmapA import emapamodifytest
from EI.EmapA import emapasearchtest

# add the test suites
def master_suite():
        suites = []
        suites.append(emapaclipboardtest.suite())
        suites.append(emapadetailtest.suite())
        suites.append(emapatreeviewtest.suite())
        suites.append(emapamodifytest.suite())
        suites.append(emapasearchtest.suite())
        
        master_suite = unittest.TestSuite(suites)
        return master_suite

if __name__ == '__main__':
        test_suite = master_suite()
        runner = unittest.TextTestRunner()
        
        ret = not runner.run(test_suite).wasSuccessful()
        sys.exit(ret)
