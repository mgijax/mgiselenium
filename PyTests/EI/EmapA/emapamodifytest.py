'''
Created on Jan 28, 2016

@author: jeffc
'''
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..')
)
import config
from util import iterate, wait
from base_class import EmapaBaseClass

class TestModifyEmapa(unittest.TestCase, EmapaBaseClass):


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
    suite.addTest(unittest.makeSuite(TestModifyEmapa))
    return suite


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()