'''
Created on Nov 3, 2017 -- used HMDC_tests.py as the template

@author: jlewis
'''
import unittest
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from gxdindex_clear_test import TestEiGxdIndexClear
from gxdindex_notes_picklist_test import TestEiGxdIndexNotesPicklist
from gxdindex_search_test import TestEiGxdIndexSearch
from gxdindex_shortcuts_test import TestEiGxdIndexShortcuts

import os
def test_suite():
  test1 = unittest.TestLoader().loadTestsFromTestCase(TestEiGxdIndexClear)
  test2 = unittest.TestLoader().loadTestsFromTestCase(TestEiGxdIndexNotesPicklist)
  test3 = unittest.TestLoader().loadTestsFromTestCase(TestEiGxdIndexSearch)
  test4 = unittest.TestLoader().loadTestsFromTestCase(TestEiGxdIndexShortcuts)
  suite = unittest.TestSuite([test1, test2, test3, test4])
  runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='GXD Index Test report', report_name='gxdindexreport',
                          open_in_browser=True, description="HTMLTestReport")
  runner.run(suite)

if __name__=="__main__":
    unittest.main(testRunner=HTMLTestRunner())


