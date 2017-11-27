'''
Created on Oct 21, 2016
These tests were created to verify details on the Genotype detail pages(genoview)
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
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
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Sey-Dey').click()
        self.driver.find_element(By.LINK_TEXT, 'ht3').click()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.window(self.driver.window_handles[1])
        mgiid = self.driver.find_element(By.CLASS_NAME, 'genoID')
        self.assertEquals(mgiid.text, "MGI:2680573", "This is not the correct MGI ID")        
        self.driver.find_element(By.CLASS_NAME, 'results')
        headers = self.driver.find_elements(By.TAG_NAME, 'td')
        
        
        
    
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