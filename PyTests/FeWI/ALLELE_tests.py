'''
Created on Apr 23, 2018

@author: jeffc
'''
import unittest
from HTMLTestRunner import HTMLTestRunner
from unittest import TestLoader, TestSuite
from allele_detail import TestAlleleDetail
from allele_summary import TestAlleleSummary
from allele_qf import TestAlleleQueryForm
from private_allele import TestPrivateAllele

print('Begin allele testing')
test1 = TestLoader().loadTestsFromTestCase(TestAlleleDetail)
test2 = TestLoader().loadTestsFromTestCase(TestAlleleSummary)
test3 = TestLoader().loadTestsFromTestCase(TestAlleleQueryForm)
test4 = TestLoader().loadTestsFromTestCase(TestPrivateAllele)
suite = unittest.TestSuite([test1, test2, test3, test4])
runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='fewi Allele Test report', report_name='fewiallelereport',
                          open_in_browser=True, description="HTMLTestReport")
runner.run(suite)

if __name__=="__main__":
    unittest.main(testRunner=HTMLTestRunner())
