'''
Created on Jan 30, 2017

@author: jeffc
'''
import unittest
from do_browser_general import TestDoBrowserGeneral
from do_browser_term import TestDoBrowserTermTab
import os
import HTMLTestRunner
from FeWI import do_browser_general, do_browser_term


def main():
    do_browser_general_test = unittest.TestLoader().loadTestsFromTestCase(TestDoBrowserGeneral)
    do_browser_term_tab_test = unittest.TestLoader().loadTestsFromTestCase(TestDoBrowserTermTab)
#Put them in an Array
    do_browser_tests = unittest.TestSuite([do_browser_general_test, do_browser_term_tab_test])
#file
    dir = os.getcwd()
    outfile = open(r"C:\WebdriverTests\DOBROWSERtestreport.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream = outfile,title = 'Test Report',description = 'DO Browser Test Report')
    runner.run(do_browser_tests)

if __name__=="__main__":
    main()