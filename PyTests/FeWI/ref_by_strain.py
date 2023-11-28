'''
Created on Apr 30, 2018
This set of tests verifies the Reference by strain page results
@author: jeffc
Verify that the Reference by strain page has the correct header items
Verify that the Reference by strain page has the sort of descending year, secondary sort of assending J number
'''
import unittest
import time
import tracemalloc
import config
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from util import wait, iterate
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from genericpath import exists
from util import wait, iterate
from config import TEST_URL

#Tests
tracemalloc.start()
class TestRefByStrain(unittest.TestCase):


    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
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
        strainsearchbox.send_keys(Keys.RETURN)
        #locates the reference link in row 1 and clicks it
        driver.find_element(By.CLASS_NAME, 'referenceLink').click()
        #switch focus to the new tab for strain detail page
        driver.switch_to.window(self.driver.window_handles[-1])
        #verify the strain name is correct for this page
        strname = driver.find_element(By.CLASS_NAME, 'symbolLink')
        print(strname.text)
        self.assertEqual(strname.text, 'C57BL/6J')   
        #verify the MGI ID is correct for this page
        mginum = driver.find_element(By.CSS_SELECTOR, "#templateBodyInsert > table.summaryHeader > tbody > tr > td.summaryHeaderData1 > span")
        print(mginum.text)
        self.assertEqual(mginum.text, 'MGI:3028467')       

    def test_ref_by_strain_sort(self):
        """
        @status: Tests that the Reference by strain page has the sort of descending year, secondary sort of assending J number
        @note: ref-strain-2. 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("C57BL/6J")
        strainsearchbox.send_keys(Keys.RETURN)
        #locate the link for C57BL/6J and click it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        #switch focus to the new tab for strain detail page
        driver.switch_to.window(self.driver.window_handles[-1])
        #locates the All reference link and clicks it
        driver.find_element(By.ID, 'allRefs').click()
        #rows of data for this page and verify sort by asserting correct results
        row1 = driver.find_element(By.XPATH, "//*[@id='dynamicdata']/table/tbody/tr[1]/td[6]/div")
        print(row1.text)
        row2a = driver.find_element(By.XPATH, "//*[@id='dynamicdata']/table/tbody/tr[2]/td[1]/div")
        print(row2a.text)
        row3a = driver.find_element(By.XPATH, "//*[@id='dynamicdata']/table/tbody/tr[3]/td[1]/div")
        print(row3a.text)
        row4a = driver.find_element(By.XPATH, "//*[@id='dynamicdata']/table/tbody/tr[4]/td[1]/div")
        print(row4a.text)
        row2 = driver.find_element(By.XPATH, "//*[@id='dynamicdata']/table/tbody/tr[2]/td[6]/div")
        print(row2.text)
        row3 = driver.find_element(By.XPATH, "//*[@id='dynamicdata']/table/tbody/tr[3]/td[6]/div")
        print(row3.text)
        row4 = driver.find_element(By.XPATH, "//*[@id='dynamicdata']/table/tbody/tr[4]/td[6]/div")
        print(row4.text)
        row5 = driver.find_element(By.XPATH, "//*[@id='dynamicdata']/table/tbody/tr[5]/td[6]/div")
        print(row5.text)
        row6 = driver.find_element(By.XPATH, "//*[@id='dynamicdata']/table/tbody/tr[6]/td[6]/div")
        print(row6.text)
        row7 = driver.find_element(By.XPATH, "//*[@id='dynamicdata']/table/tbody/tr[7]/td[6]/div")
        print(row7.text)
        self.assertEqual(row1.text, '2023')
        self.assertEqual(row2a.text, '36766792\nJ:336276\nJournal Link')
        self.assertEqual(row3a.text, '37468468\nJ:338209\nJournal Link')
        self.assertEqual(row4a.text, '37279768\nJ:339445\nJournal Link')
        self.assertEqual(row2.text, '2023')
        self.assertEqual(row3.text, '2023')
        self.assertEqual(row4.text, '2023')
        self.assertEqual(row5.text, '2023')
        self.assertEqual(row6.text, '2023')
        self.assertEqual(row7.text, '2023')
        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRefByStrain))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))