'''
Created on Jun 7, 2016

@author: jeffc
This set of tests verifies items found on the marker query form page.
'''
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
import config
from config import TEST_URL

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(config.TEST_URL + "/marker/")
        self.driver.implicitly_wait(10)

    def test_ribbon_locations(self):
        '''
        @status This test verifies the ribbons are being displayed in the correct order on the page.
        '''
        self.driver.find_element_by_name("markerQF")
        genemarker = self.driver.find_element_by_class_name("queryCat1")
        self.assertEquals(genemarker.text, 'Gene/Marker', "heading is incorrect")
        featuretype = self.driver.find_element_by_class_name("queryCat2")
        self.assertEquals(featuretype.text, 'Feature type', "heading is incorrect")
     
        
        
        
        
        
        
        
        
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()                
