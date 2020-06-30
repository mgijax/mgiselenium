'''
Created on Jan 30, 2017

@author: jeffc
'''
import unittest
import HtmlTestRunner
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from do_browser_general import TestDoBrowserGeneral
from do_browser_term import TestDoBrowserTermTab
from do_browser_gene import TestDoBrowserGeneTab
from do_browser_model import TestDoBrowserModelTab
from do_browser_models_popup import TestDoBrowserModelsPopup

print('Begin DO browser testing')
do_browser_general_test = TestLoader().loadTestsFromTestCase(TestDoBrowserGeneral)
do_browser_term_tab_test = TestLoader().loadTestsFromTestCase(TestDoBrowserTermTab)
do_browser_gene_tab_test = TestLoader().loadTestsFromTestCase(TestDoBrowserGeneTab)
do_browser_model_tab_test = TestLoader().loadTestsFromTestCase(TestDoBrowserModelTab)
do_browser_models_popup_test = TestLoader().loadTestsFromTestCase(TestDoBrowserModelsPopup)
#Put them in an Array
do_browser_suite = TestSuite([do_browser_general_test, do_browser_term_tab_test, do_browser_gene_tab_test, do_browser_model_tab_test, do_browser_models_popup_test])
print('End DO browser testing')
#file
runner = HTMLTestRunner(output='C://WebdriverTests/do_browser_suite')
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyDoBrowserReport", add_timestamp=False).run(do_browser_suite)
#runner.run(do_browser_suite)

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
#reports generated Users/jeffc/git/mgiselenium/PyTests/PWI/reports  