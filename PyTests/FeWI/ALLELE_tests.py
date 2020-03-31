'''
Created on Apr 23, 2018

@author: jeffc
'''

import unittest
from .allele_detail import TestAlleleDetail
from .allele_summary import TestAlleleSummary
from .allele_qf import TestAlleleQueryForm
from .private_allele import TestPrivateAllele
import os
import HtmlTestRunner
from FeWI import allele_detail, allele_summary, allele_qf, private_allele

#from fewi allele import allele_detail, allele_summary, allele_qf, private_allele
def main():
    allele_detail_test = unittest.TestLoader().loadTestsFromTestCase(TestAlleleDetail)
    allele_summary_test = unittest.TestLoader().loadTestsFromTestCase(TestAlleleSummary)
    allele_qf_test = unittest.TestLoader().loadTestsFromTestCase(TestAlleleQueryForm)
    private_allele_test = unittest.TestLoader().loadTestsFromTestCase(TestPrivateAllele)

#Put them in an Array
    allele_tests = unittest.TestSuite([allele_detail_test, allele_summary_test, allele_qf_test, private_allele_test])
#file
    dir = os.getcwd()
    outfile = open(r"C:\WebdriverTests\Alleletestreport.html", "w")
    runner = HtmlTestRunner.HTMLTestRunner(stream = outfile,title = 'Test Report',description = 'Alleles Test Report')
    runner.run(allele_tests)

if __name__=="__main__":
    main()