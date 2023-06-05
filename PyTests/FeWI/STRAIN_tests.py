'''
Created on Jun 8, 2018

@author: jeffc
'''
import unittest
from unittest import TestLoader, TestSuite
from HTMLTestRunner import HTMLTestRunner
from strain_qf import TestStrainQF
from strain_detail import TestStrainDetail
from strain_summary import TestStrainSummary
from ref_by_strain import TestRefByStrain
from reference_summary_bystrain import TestReferenceSummaryStrain

print('Begin Strain testing')
test1 = TestLoader().loadTestsFromTestCase(TestStrainQF)
test2 = TestLoader().loadTestsFromTestCase(TestStrainDetail)
test3 = TestLoader().loadTestsFromTestCase(TestStrainSummary)
test4 = TestLoader().loadTestsFromTestCase(TestRefByStrain)
test5 = TestLoader().loadTestsFromTestCase(TestReferenceSummaryStrain)
suite = unittest.TestSuite([test1, test2, test3, test4, test5])
runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='fewi Strain Test report', report_name='fewistrainreport',
                          open_in_browser=True, description="HTMLTestReport")
runner.run(suite)


if __name__=="__main__":
    unittest.main(testRunner=HTMLTestRunner())
#reports generated Users/jeffc/git/mgiselenium/PyTests/PWI/reports  