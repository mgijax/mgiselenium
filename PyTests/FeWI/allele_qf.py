'''
Created on Oct 19, 2016
This set of tests verifies items found on the allele query form page
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

    def test_ribbon_locations(self):
        '''
        @status This test verifies the ribbons are being displayed in the correct order on the page.
        '''
        self.driver.find_element_by_name("alleleQueryForm")
        phenotypesdisease = self.driver.find_element_by_css_selector("tr.stripe1 > td.cat1")
        print phenotypesdisease.text
        self.assertEquals(phenotypesdisease.text, 'Mouse phenotypes &\nmouse models of\nhuman disease', "heading is incorrect")
        nomengenomelocation = self.driver.find_element_by_css_selector("tr.stripe2 > td.cat2")
        print nomengenomelocation.text
        self.assertEquals(nomengenomelocation.text, 'Nomenclature\n& genome location', "heading is incorrect")
        categories = self.driver.find_element_by_css_selector("tr:nth-child(4).stripe1 > td.cat1")
        print categories.text
        self.assertEquals(categories.text, 'Categories', "heading is incorrect")
     
        
        
        
        
        
        
        
        
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()                
