'''
Created on Oct 19, 2016
This set of tests verifies items found on the Gene Expression query form page
@author: jeffc
'''
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
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
        self.driver.get(config.TEST_URL + "/gxd/")
        self.driver.implicitly_wait(10)

    def test_ribbon_locations(self):
        '''
        @status This test verifies the ribbons are being displayed in the correct order on the page.
        '''
        self.driver.find_element(By.ID, 'gxdQueryForm')
        genesribbon = self.driver.find_element(By.CSS_SELECTOR, 'tr.stripe1 > td.cat1Gxd')
        print genesribbon.text
        self.assertEquals(genesribbon.text, 'Genes', "heading is incorrect")
        genomelocation = self.driver.find_element(By.CSS_SELECTOR, 'tr.stripe2 > td.cat2Gxd')
        print genomelocation.text
        self.assertEquals(genomelocation.text, 'Genome location', "heading is incorrect")
        structurestage = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(4).stripe1 > td.cat1Gxd')
        print structurestage.text
        self.assertEquals(structurestage.text, 'Anatomical structure or stage', "heading is incorrect")
        mutantwt = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(5).stripe2 > td.cat2Gxd')
        print mutantwt.text
        self.assertEquals(mutantwt.text, 'Mutant / wild type', "heading is incorrect")
        assaytype = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(6).stripe1 > td.cat1Gxd')
        print assaytype.text
        self.assertEquals(assaytype.text, 'Assay types', "heading is incorrect")
        
        
        
        
        
        
        
    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()                