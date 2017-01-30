'''
Created on Oct 21, 2016
These tests were created to verify details on the Genotype detail pages(genoview)
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table



# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/allele/")
        self.driver.implicitly_wait(10)
        
    def test_genotype_header(self):
        '''
        @status this test verifies ????.
        @bug: under construction
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Pax6")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text("Sey-Dey").click()
        self.driver.find_element_by_link_text('ht3').click()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.window(self.driver.window_handles[1])
        mgiid = self.driver.find_element_by_class_name("genoID")
        self.assertEquals(mgiid.text, "MGI:2680573", "This is not the correct MGI ID")        
        self.driver.find_element_by_class_name("results")
        headers = self.driver.find_elements_by_tag_name("td")
        
        
        
    
    def tearDown(self):
        self.driver.close()
       
'''
These tests should NEVER!!!! be run against a production system!!
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAdd))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main() 