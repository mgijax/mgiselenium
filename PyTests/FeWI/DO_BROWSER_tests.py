'''
Created on Jan 30, 2017

@author: jeffc
'''
import unittest
from HTMLTestRunner import HTMLTestRunner
from unittest import TestLoader, TestSuite
from do_browser_general import TestDoBrowserGeneral
from do_browser_term import TestDoBrowserTermTab
from do_browser_gene import TestDoBrowserGeneTab
from do_browser_model import TestDoBrowserModelTab
from do_browser_models_popup import TestDoBrowserModelsPopup

print('Begin DO browser testing')
test1 = TestLoader().loadTestsFromTestCase(TestDoBrowserGeneral)
test2 = TestLoader().loadTestsFromTestCase(TestDoBrowserTermTab)
test3 = TestLoader().loadTestsFromTestCase(TestDoBrowserGeneTab)
test4 = TestLoader().loadTestsFromTestCase(TestDoBrowserModelTab)
test5 = TestLoader().loadTestsFromTestCase(TestDoBrowserModelsPopup)

test1 = TestLoader().loadTestsFromTestCase(TestDoBrowserGeneral)
test2 = TestLoader().loadTestsFromTestCase(TestDoBrowserTermTab)
test3 = TestLoader().loadTestsFromTestCase(TestDoBrowserGeneTab)
test4 = TestLoader().loadTestsFromTestCase(TestDoBrowserModelTab)
test5 = TestLoader().loadTestsFromTestCase(TestDoBrowserModelsPopup)
suite = unittest.TestSuite([test1, test2, test3, test4, test5])
runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='fewi Do Browser Test report', report_name='fewidobrowserreport',
                          open_in_browser=True, description="HTMLTestReport")
runner.run(suite)

if __name__=="__main__":
    unittest.main(testRunner=HTMLTestRunner())