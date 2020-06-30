'''
Created on Jun 8, 2018

@author: jeffc
'''
import unittest
import HtmlTestRunner
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from strain_qf import TestStrainQF
from strain_detail import TestStrainDetail
from strain_summary import TestStrainSummary
from ref_by_strain import TestRefByStrain
from reference_summary_bystrain import TestReferenceSummaryStrain

print('Begin Strain testing')
strain_qf_test = TestLoader().loadTestsFromTestCase(TestStrainQF)
strain_detail_test = TestLoader().loadTestsFromTestCase(TestStrainDetail)
strain_summary_test = TestLoader().loadTestsFromTestCase(TestStrainSummary)
ref_by_strain_test = TestLoader().loadTestsFromTestCase(TestRefByStrain)
refeference_summary_bystrain_test = TestLoader().loadTestsFromTestCase(TestReferenceSummaryStrain)
#Put them in an Array
strain_test_suite = TestSuite([strain_qf_test, strain_detail_test, strain_summary_test, ref_by_strain_test, refeference_summary_bystrain_test])
print('End Strain testing')
#file
runner = HTMLTestRunner(output='C://WebdriverTests/strain_test_suite')
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyStrainReport", add_timestamp=False).run(strain_test_suite)
#runner.run(strain_test_suite)

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
#reports generated Users/jeffc/git/mgiselenium/PyTests/PWI/reports  