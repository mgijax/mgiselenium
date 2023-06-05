'''
Created on May 26, 2023 -- tests all image tests

@author: jeffc
'''
import unittest
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from marker_search_history_test import TestEiMrkSearchHistory
from marker_search_test import TestEiMrkSearch

import os
def test_suite():
  test1 = unittest.TestLoader().loadTestsFromTestCase(TestEiMrkSearchHistory)
  test2 = unittest.TestLoader().loadTestsFromTestCase(TestEiMrkSearch)
  suite = unittest.TestSuite([test1, test2])
  runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='PWI Marker Test report', report_name='markermodulereport',
                          open_in_browser=True, description="HTMLTestReport")
  runner.run(suite)

if __name__=="__main__":
    unittest.main(testRunner=HTMLTestRunner())