'''
Created on Jan 28, 2016
@attention: Needs tests added as time permits!!!!!!
@attention: Needs tests added as time permits!!!!!!
@attention: Needs tests added as time permits!!!!!!
@author: jeffc
'''
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..')
)
import config
from util import iterate, wait
from .base_class import EmapaBaseClass

class TestEiEmapaModify(unittest.TestCase, EmapaBaseClass):


    def setUp(self):
        self.init()

    def testName(self):
        # example term search
        #self.performSearch(term="mouse")
        pass

    def tearDown(self):
        self.closeAllWindows()
        
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiEmapaModify))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
