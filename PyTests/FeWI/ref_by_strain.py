'''
Created on Apr 30, 2018
This set of tests verifies the Reference by strain page results
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from util import wait, iterate
import sys,os.path
from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
import config
from config import TEST_URL

class TestRefByStrain(unittest.TestCase):


    def setUp(self):
    
        self.driver = webdriver.Firefox()
        self.driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        self.driver.implicitly_wait(10)
        
    def test_ref_by_strain_header(self):
        """
        @status: Tests that the Reference by strain page has the correct header items
        @note: ref-strain-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("C57BL/6J")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locate the link for C57BL/6J and click it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #locates the earliest reference link and clicks it
        driver.find_element(By.LINK_TEXT, '54').click()
        time.sleep(2)
        #verify the strain name is correct for this page
        strname = driver.find_element_by_css_selector("#templateBodyInsert > table.summaryHeader > tbody > tr > td.summaryHeaderData1 > a.symbolLink")
        print strname.text
        self.assertEquals(strname.text, 'C57BL/6J')   
        #verify the MGI ID is correct for this page
        mginum = driver.find_element_by_css_selector("#templateBodyInsert > table.summaryHeader > tbody > tr > td.summaryHeaderData1 > span")
        print mginum.text
        self.assertEquals(mginum.text, 'MGI:3028467')       

    def test_ref_by_strain_sort(self):
        """
        @status: Tests that the Reference by strain page has the sort of descending year, secondary sort of assending J number
        @note: ref-strain-2. this test is not working, does not show text for column1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("C57BL/6J")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locate the link for C57BL/6J and click it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #locates the earliest reference link and clicks it
        driver.find_element(By.ID, 'allRefs').click()
        time.sleep(2)
        #rows of data for this page and verify sort by asserting correct results
        row1 = driver.find_element_by_xpath("//*[@id='dynamicdata']/table/tbody/tr[1]/td[6]/div")
        print row1.text
        row1a = driver.find_element_by_xpath("//*[@id='dynamicdata']/table/tbody/tr[1]/td[2]/div")
        print row1a.text
        row2 = driver.find_element_by_xpath("//*[@id='dynamicdata']/table/tbody/tr[2]/td[6]/div")
        print row2.text
        row3 = driver.find_element_by_xpath("//*[@id='dynamicdata']/table/tbody/tr[3]/td[6]/div")
        print row3.text
        row4 = driver.find_element_by_xpath("//*[@id='dynamicdata']/table/tbody/tr[4]/td[6]/div")
        print row4.text
        row5 = driver.find_element_by_xpath("//*[@id='dynamicdata']/table/tbody/tr[5]/td[6]/div")
        print row5.text
        row6 = driver.find_element_by_xpath("//*[@id='dynamicdata']/table/tbody/tr[6]/td[6]/div")
        print row6.text
        row7 = driver.find_element_by_xpath("//*[@id='dynamicdata']/table/tbody/tr[7]/td[6]/div")
        print row7.text
        self.assertEqual(row1.text, '2016')   
        self.assertEqual(row1a.text, '26768846,\nJ;227903,\nJournal Link')       
        self.assertEqual(row2.text, '2016')
        self.assertEqual(row3.text, '2016')
        self.assertEqual(row4.text, '2016')
        self.assertEqual(row5.text, '2016')
        self.assertEqual(row6.text, '2015') 
        self.assertEqual(row7.text, '2014')    
        
    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRefByStrain))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'TestRefByStrain.testName']
    unittest.main()      