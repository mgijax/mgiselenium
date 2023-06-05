'''
Created on Apr 28, 2020

@author: jeffc
'''
import unittest
from HTMLTestRunner import HTMLTestRunner
from unittest import TestLoader, TestSuite
from pwi_allele_detail import TestPwiAlleleDetail
from pwi_gxd_antibody_summary import TestPwiGxdAntibodySummaryPage
from pwi_gxd_assay_summary import TestPwiGxdAssaySummaryPage
from pwi_gxd_image_pane_summary import TestPwiGxdImagePanePage
from pwi_gxd_lit_index_by_mrk import TestPwiGxdLitIndexByMrk
from pwi_gxd_spec_summary_by_ref import TestPwiGxdSpecSumByRef
from pwi_mrk_detail import TestPwiMrkDetail

print('Begin PWI testing')
pwi_allele_detail = TestLoader().loadTestsFromTestCase(TestPwiAlleleDetail)
pwi_gxd_antibody_summary = TestLoader().loadTestsFromTestCase(TestPwiGxdAntibodySummaryPage)
pwi_gxd_assay_summary = TestLoader().loadTestsFromTestCase(TestPwiGxdAssaySummaryPage)
pwi_gxd_image_pane_summary = TestLoader().loadTestsFromTestCase(TestPwiGxdImagePanePage)
pwi_gxd_lit_index_by_mrk = TestLoader().loadTestsFromTestCase(TestPwiGxdLitIndexByMrk)
pwi_gxd_spec_summary_by_ref = TestLoader().loadTestsFromTestCase(TestPwiGxdSpecSumByRef)
pwi_mrk_detail = TestLoader().loadTestsFromTestCase(TestPwiMrkDetail)
#Put them in an Array
#pwi_test_suite = TestSuite([pwi_do_allele_test, pwi_gxd_antibody_test, pwi_gxd_assay_test, pwi_gxd_image_test, pwi_gxd_litindex_mrk_test, pwi_gxd_spec_byref_test, pwi_mrk_test])

def test_suite():
  test1 = unittest.TestLoader().loadTestsFromTestCase(TestPwiAlleleDetail)
  test2 = unittest.TestLoader().loadTestsFromTestCase(TestPwiGxdAntibodySummaryPage)
  test3 = unittest.TestLoader().loadTestsFromTestCase(TestPwiGxdAssaySummaryPage)
  test4 = unittest.TestLoader().loadTestsFromTestCase(TestPwiGxdImagePanePage)
  test5 = unittest.TestLoader().loadTestsFromTestCase(TestPwiGxdLitIndexByMrk)
  test6 = unittest.TestLoader().loadTestsFromTestCase(TestPwiGxdSpecSumByRef)
  test7 = unittest.TestLoader().loadTestsFromTestCase(TestPwiMrkDetail)
  suite = unittest.TestSuite([test1, test2, test3, test4, test5, test6, test7])
  runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='PWI Test report', report_name='pwireport',
                          open_in_browser=True, description="HTMLTestReport")
  runner.run(suite)
print('End PWI testing')
if __name__=="__main__":
    unittest.main(testRunner=HTMLTestRunner())
#reports generated Users/jeffc/git/mgiselenium/PyTests/PWI/reports  