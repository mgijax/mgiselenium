'''
Created on Apr 23, 2018

@author: jeffc
'''
import unittest
import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner
from unittest import TestLoader, TestSuite
from allele_detail import TestAlleleDetail
from allele_summary import TestAlleleSummary
from allele_qf import TestAlleleQueryForm
from private_allele import TestPrivateAllele

print('Begin allele testing')
allele_detail_test = TestLoader().loadTestsFromTestCase(TestAlleleDetail)
allele_summary_test = TestLoader().loadTestsFromTestCase(TestAlleleSummary)
allele_qf_test = TestLoader().loadTestsFromTestCase(TestAlleleQueryForm)
private_allele_test = TestLoader().loadTestsFromTestCase(TestPrivateAllele)
#Put them in an Array
allele_tests_suite = TestSuite([allele_detail_test, allele_summary_test, allele_qf_test, private_allele_test])
print('End allele testing')
#file
runner = HTMLTestRunner(output='C://WebdriverTests/allele_tests_suite')
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyAlleleReport", add_timestamp=False).run(allele_tests_suite)
#runner.run(allele_tests_suite)

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
#reports generated Users/jeffc/git/mgiselenium/PyTests/PWI/reports   