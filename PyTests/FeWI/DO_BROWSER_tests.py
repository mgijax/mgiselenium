'''
Created on Jan 30, 2017

@author: jeffc
'''
import unittest
from do_browser_general import TestDoBrowserGeneral
from do_browser_term import TestDoBrowserTermTab
from do_browser_gene import TestDoBrowserGeneTab
from do_browser_model import TestDoBrowserModelTab
from do_browser_models_popup import TestDoBrowserModelsPopup
import os
import HTMLTestRunner
from FeWI import do_browser_general, do_browser_term, do_browser_gene, do_browser_model, do_browser_models_popup


def main():
    do_browser_general_test = unittest.TestLoader().loadTestsFromTestCase(TestDoBrowserGeneral)
    do_browser_term_tab_test = unittest.TestLoader().loadTestsFromTestCase(TestDoBrowserTermTab)
    do_browser_gene_tab_test = unittest.TestLoader().loadTestsFromTestCase(TestDoBrowserGeneTab)
    do_browser_model_tab_test = unittest.TestLoader().loadTestsFromTestCase(TestDoBrowserModelTab)
    do_browser_models_popup_test = unittest.TestLoader().loadTestsFromTestCase(TestDoBrowserModelsPopup)
#Put them in an Array
    do_browser_tests = unittest.TestSuite([do_browser_general_test, do_browser_term_tab_test, do_browser_gene_tab_test, do_browser_model_tab_test, do_browser_models_popup_test])
#file
    dir = os.getcwd()
    outfile = open(r"C:\WebdriverTests\DOBROWSERtestreport.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream = outfile,title = 'Test Report',description = 'DO Browser Test Report')
    runner.run(do_browser_tests)

if __name__=="__main__":
    main()