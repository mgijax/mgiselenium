'''
Created on Jan 27, 2017

@author: jeffc
'''
import unittest
from littriage_search_test import TestLitSearch
from littriage_summary_test import TestLitSummarySearch
import os
import HTMLTestRunner
#from LitTriage import littriage_search_test, littriage_summary_test


def main():
    littriage_search_test = unittest.TestLoader().loadTestsFromTestCase(TestLitSearch)
    littriage_summary_test = unittest.TestLoader().loadTestsFromTestCase(TestLitSummarySearch)

#Put them in an Array
    littriage_tests = unittest.TestSuite([littriage_search_test, littriage_summary_test])
#file
    dir = os.getcwd()
    outfile = open(r"C:\WebdriverTests\LitTriagetestreport.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream = outfile,title = 'Test Report',description = 'Literature Triage Test Report')
    runner.run(littriage_tests)

if __name__=="__main__":
    main()