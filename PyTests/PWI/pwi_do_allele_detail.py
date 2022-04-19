'''
Created on Nov 22, 2016
These tests start out using the Marker form THE MARKER FORM IS NOW GONE reevaluate these tests!
@author: jeffc
'''

import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import sys,os.path
from util import wait, iterate
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import TEST_PWI_URL

class TestPwiDoAlleleDetail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome() 

    def test_disease_annotations(self):
        """
        @status: Tests that the disease annotations section is correct, this section now has both OMIM and DO annotations.
        @note rewritten on 4/8/2022
        """
        driver = self.driver
        #opens the PWI
        driver.get(TEST_PWI_URL)
        time.sleep(5)
        #find the Acc ID(s) / Gene Symbol box and enter text
        accbox = driver.find_element(By.NAME, 'ids')
        # put your marker symbol in the box
        accbox.send_keys("MGI:97490")
        accbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Public Pax6 Page')))#waits until the Public Pax6 Page link is displayed on the page
        driver.find_element(By.LINK_TEXT, "Alleles").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Sey-Dey')))#waits until the allele link for Pax6<Sey-Dey> is displayed on the page
        driver.find_element(By.PARTIAL_LINK_TEXT, "Sey-Dey").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Public Allele Detail Page')))#waits until the link 'Public Allele Detail Page' is displayed on the page
        #Locates the summary table and finds the table headings
        #driver.find_element(By.CSS_SELECTOR, 'div.genotypeDetail:nth-child(3)')
        #driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData:nth-child(1)')
        #driver.find_elements(By.TAG_NAME, 'dd.detailPageListData')
        #data = driver.find_elements(By.TAG_NAME, 'a')
        #print (iterate.getTextAsList(data))#prints out almost all data found on this page, hopefully someday  I can figure out how to capture just the disease annotations section.
        time.sleep(5)
        element = driver.find_elements(By.XPATH, '/html/body/main/div/div[3]/dl[2]')
        # iterate through list and get text
        for i in element:
            print("Classes:"+ i.text)
                
        #asserts that all the disease annotations data is correct for MGI:2175204 Pax6Sey-Dey/Pax6+
        self.assertIn(i.text, "Term\naniridia\nDO ID\nDOID:12271\nReference\nJ:10820\nTerm\nWAGR syndrome (NOT)\nDO ID\nDOID:14515\nReference\nJ:10820")
        

    def tearDown(self):
        self.driver.close()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPwiDoAlleleDetail))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))    
        