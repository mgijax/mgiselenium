'''
Created on Dec 22, 2015

@author: jeffc
'''
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
import config
from util import wait
import time



class TestPrivateData(unittest.TestCase): 

    def setUp(self):
        self.driver = webdriver.Firefox() 

    def test_hide_private_allele(self):
        """
        @status: Test is under construction
        """
        driver = self.driver
        driver.get(config.PUBLIC_URL)
        self.assertIn("Informatics", driver.title)
        querytext = driver.find_element_by_name('query')
        querytext.send_keys("Brca1")  # put your marker symbol
        querytext.send_keys(Keys.RETURN)  # click the submit button
        brcalink = driver.find_element_by_link_text("Brca1")  # Find the Brca1 link and click it
        brcalink.click()  # Find the all alleles and mutations link and click it
        allallelelink = driver.find_element_by_link_text("89")
        allallelelink.click()
        time.sleep(.5)
        wait.forAjax(driver)
        #allalleles = driver.find_elements_by_id("dynamicdata")
        # assert that there is no link for Brca1<test1>#testallele = driver.find_element_by_link_text('Brca1<sup>test1</sup>')
        self.assertNotIn("test1", self.driver.page_source,"Test1 allele is displaying!")

    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPrivateData))
    return suite
        
if __name__ == "__main__":
    unittest.main() 
    
