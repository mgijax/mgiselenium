"""
This file runs all public WI related test suites as long as they are in this suite test.
"""
import sys,os.path

# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../',)
)
import config

import unittest
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
# import all sub test suites
from unittest import TestLoader, TestSuite
from test_mrk_detail_links import TestMarkerDetailLinks
from test_private_data import TestPrivateData
from test_snp_build_numbers import TestSnpBuildNumbers


def test_suite():
  test1 = unittest.TestLoader().loadTestsFromTestCase(TestMarkerDetailLinks)
  test2 = unittest.TestLoader().loadTestsFromTestCase(TestPrivateData)
  test3 = unittest.TestLoader().loadTestsFromTestCase(TestSnpBuildNumbers)
  suite = unittest.TestSuite([test1, test2, test3])
  runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                          open_in_browser=True, description="HTMLTestReport")
  runner.run(suite)


if __name__ == '__main__':
  test_suite()





