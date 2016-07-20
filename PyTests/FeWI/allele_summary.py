'''
Created on Jun 6, 2016

@author: jeffc
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
from config import PWI_URL

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(config.FEWI_URL + "/allele/")
        self.driver.implicitly_wait(10)
        
    def test_column_headings(self):
        '''
        @status This test verifies the correct column headings are being displayed in the correct order on the page.
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Pkd1")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text("tm2Jzh").click()
        assert "Pkd1<sup>tm2Jzh</sup>" in self.driver.page_source
        assert 'id="nomenclatureHeader"' in self.driver.page_source
        assert 'id="originHeader"' in self.driver.page_source    
        
        
        
        
        
        
        
        
        
        
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()        
