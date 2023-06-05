'''
Created on May 26, 2023 -- tests all image tests

@author: jeffc
'''
import unittest
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from image_pane_tests import TestEiImagePaneSearch
from image_search_test import TestEiImageSearch

import os
def test_suite():
  test1 = unittest.TestLoader().loadTestsFromTestCase(TestEiImagePaneSearch)
  test2 = unittest.TestLoader().loadTestsFromTestCase(TestEiImageSearch)
  suite = unittest.TestSuite([test1, test2])
  runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Image Test report', report_name='imagereport',
                          open_in_browser=True, description="HTMLTestReport")
  runner.run(suite)

if __name__=="__main__":
    unittest.main(testRunner=HTMLTestRunner())
