'''
Created on Jan 27, 2017

@author: jeffc
'''
import unittest
from littriage_search_test import TestEiLitTriageSearch
from littriage_summary_test import TestEiLitTriageSummarySearch
from littriage_detail_test import TestEiLitTriageDetail
import os
import HtmlTestRunner

#from LitTriage import littriage_search_test, littriage_summary_test
def main():
    littriage_search_test = unittest.TestLoader().loadTestsFromTestCase(TestEiLitTriageSearch)
    littriage_summary_test = unittest.TestLoader().loadTestsFromTestCase(TestEiLitTriageSummarySearch)
    littriage_detail_test = unittest.TestLoader().loadTestsFromTestCase(TestEiLitTriageDetail)

#Put them in an Array
    littriage_tests = unittest.TestSuite([littriage_search_test, littriage_summary_test, littriage_detail_test])
#file
    dir = os.getcwd()
    outfile = open(r"C:\WebdriverTests\LitTriagetestreport.html", "w")
    runner = HtmlTestRunner.HTMLTestRunner(stream = outfile,title = 'Test Report',description = 'Literature Triage Test Report')
    runner.run(littriage_tests)

if __name__=="__main__":
    main()