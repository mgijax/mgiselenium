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
from util import wait

class ModifyEmapaTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get()

    def testName(self):
        pass

    def tearDown(self):
        self.driver.close()
        
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ModifyEmapaTest))
    return suite


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
