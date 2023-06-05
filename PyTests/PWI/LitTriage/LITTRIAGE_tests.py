'''
Created on Jan 27, 2017

@author: jeffc
'''
import unittest
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from litriage_search_test import TestEiLitTriageSearch
from littriage_detail_test import TestEiLitTriageDetail
from littriage_short_search_test import TestEiLitTriageShortSearch
from littriage_summary_test import TestEiLitTriageSummarySearch

import os
def test_suite():
  test1 = unittest.TestLoader().loadTestsFromTestCase(TestEiLitTriageSearch)
  test2 = unittest.TestLoader().loadTestsFromTestCase(TestEiLitTriageDetail)
  test3 = unittest.TestLoader().loadTestsFromTestCase(TestEiLitTriageShortSearch)
  test4 = unittest.TestLoader().loadTestsFromTestCase(TestEiLitTriageSummarySearch)
  suite = unittest.TestSuite([test1, test2, test3, test4])
  runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Lit Triage Test report', report_name='littriagereport',
                          open_in_browser=True, description="HTMLTestReport")
  runner.run(suite)

if __name__=="__main__":
    unittest.main(testRunner=HTMLTestRunner())