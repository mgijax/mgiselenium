"""
Run all PWI EMAPA test suites
"""
import sys, os.path

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../../config', )
)

import unittest
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from unittest import TestLoader, TestSuite
from emapa_clipboard_tests import TestEiEmapaClipboard
from emapa_detail_tests import TestEiEmapaDetail
from emapa_search_tests import TestEiEmapaSearch
from emapa_treeview_tests import TestEiEmapaTreeView

def test_suite():
  test1 = unittest.TestLoader().loadTestsFromTestCase(TestEiEmapaClipboard)
  test2 = unittest.TestLoader().loadTestsFromTestCase(TestEiEmapaDetail)
  test3 = unittest.TestLoader().loadTestsFromTestCase(TestEiEmapaSearch)
  test4 = unittest.TestLoader().loadTestsFromTestCase(TestEiEmapaTreeView)
  suite = unittest.TestSuite([test1, test2, test3, test4])
  runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='EmapA Test report', report_name='emapareport',
                          open_in_browser=True, description="HTMLTestReport")
  runner.run(suite)

if __name__=="__main__":
    unittest.main(testRunner=HTMLTestRunner())
