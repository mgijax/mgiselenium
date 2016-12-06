"""
Run all PWI GxdIndex test suites
"""
import sys,os.path

# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../../config',)
)
import config

import unittest

# import all sub test suites
import gxdindex_add_delete_test
import gxdindex_clear_test
import gxdindex_modify_test
import gxdindex_search_test

# add the test suites
def master_suite():
        suites = []
        suites.append(gxdindex_add_delete_test.suite())
        suites.append(gxdindex_clear_test.suite())
        suites.append(gxdindex_modify_test.suite())
        suites.append(gxdindex_search_test.suite())
        
        master_suite = unittest.TestSuite(suites)
        return master_suite

if __name__ == '__main__':
        test_suite = master_suite()
        runner = unittest.TextTestRunner()
        
        ret = not runner.run(test_suite).wasSuccessful()
        sys.exit(ret)
