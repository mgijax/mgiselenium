'''
Created Aug 26, 2021
!!!!!!!!!!!!!!!UNDER CONSTRUCTION!!!!!!!!!!!!
This test verifies searching within the HT Index module.

@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import HtmlTestRunner
import json
import string
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

class TestEiHTindexSearch(unittest.TestCase):
    """
    @status Test GXD HT Index search 
    """

    def setUp(self):
        self.driver = webdriver.Firefox() 
        #self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/gxdHTEval")
    
        
    def testArrayExpSearch(self):
        """
        @Status tests that an Array Express ID search works
        @see pwi-htindex-search-1
        """
        #start the firefox browser and go to the PWI HT Index page
        #finds the ArrayExp field and enter the ID
        self.driver.find_element(By.ID, "arrayexpressid").send_keys("E-BAIR-1");
        #Find the Search button and click it
        self.driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the search results
        html_list = self.driver.find_element(By.CLASS_NAME, "scrollable-menu")
        items = html_list.find_elements(By.TAG_NAME, "li")
        for item in items:
            text = item.text
            print(text)
        #Assert the correct ID  is returned
        assert item("E-BAIR-1").exists()
        
        
        #find the search results table
        #results_table = self.driver.find_element(By.ID, "resultsTable")
        #table = Table(results_table)
        #Iterate and print the search results headers
        #cell1 = table.get_row_cells(0)
        #symbol1 = iterate.getTextAsList(cell1)
        #print(symbol1)
        #Assert the correct marker symbol and marker type is returned
        #self.assertEqual(symbol1, ['03.MMHAP34FRA.seq'])
        #since we search for a particular marker type verify the correct type is displayed
        #mrktype = driver.find_element(By.ID, 'markerType').get_attribute('value')
        #self.assertEqual(mrktype, 'string:2')#2 equals "DNA Segment"

    def testArrayExpwildSearch(self):
        """
        @Status tests that an Array Express ID wildcard search works
        @see pwi-htindex-search-1 *NOTE: currently broken
        """
        driver = self.driver
        #finds the ArrayExp field and enter the ID
        driver.find_element(By.ID, "arrayexpressid").send_keys("E-BAIR-%");
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results
        html_list = self.driver.find_element(By.CLASS_NAME, "scrollable-menu")
        items = html_list.find_elements(By.TAG_NAME, "li")
        for item in items:
            text = item.text
            print(text)
        #Assert the correct ID  is returned
        self.assertEqual(text, 'E-BAIR-1 *, E-BAIR-10, E-BAIR-11, E-BAIR-12, E-BAIR-13, E-BAIR-2 *, E-BAIR-3 *, E-BAIR-4 *, E-BAIR-5 *, E-BAIR-6 *, E-BAIR-7, E-BAIR-8, E-BAIR-9')

    def testGeoSearch(self):
        """
        @Status tests that a GEO ID search works
        @see pwi-htindex-search-2
        """
        driver = self.driver
        #finds the ArrayExp field and enter the ID
        driver.find_element(By.ID, "geoid").send_keys("GSE1008");
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the search results
        html_list = self.driver.find_element(By.CLASS_NAME, "scrollable-menu")
        items = html_list.find_elements(By.TAG_NAME, "li")
        for item in items:
            text = item.text
            print(text)
        #Assert the correct ID  is returned
        self.assertEqual(text, 'E-GEOD-1008 *')
        
        
        #find the search results table
        #results_table = self.driver.find_element(By.ID, "resultsTable")
        #table = Table(results_table)
        #Iterate and print the search results headers
        #cell1 = table.get_row_cells(0)
        #symbol1 = iterate.getTextAsList(cell1)
        #print(symbol1)
        #Assert the correct marker symbol and marker type is returned
        #self.assertEqual(symbol1, ['03.MMHAP34FRA.seq'])
        #since we search for a particular marker type verify the correct type is displayed
        #mrktype = driver.find_element(By.ID, 'markerType').get_attribute('value')
        #self.assertEqual(mrktype, 'string:2')#2 equals "DNA Segment"

    def testGeoPriSearch(self):
        """
        @Status tests that a GEO ID search that is primary works
        @see pwi-htindex-search-2
        """
        driver = self.driver
        #finds the ArrayExp field and enter the ID
        driver.find_element(By.ID, "geoid").send_keys("GSE10002");
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the search results
        html_list = self.driver.find_element(By.CLASS_NAME, "scrollable-menu")
        items = html_list.find_elements(By.TAG_NAME, "li")
        for item in items:
            text = item.text
            print(text)
        #Assert the correct ID  is returned
        self.assertEqual(text, 'GSE10002')
        
        
        #find the search results table
        #results_table = self.driver.find_element(By.ID, "resultsTable")
        #table = Table(results_table)
        #Iterate and print the search results headers
        #cell1 = table.get_row_cells(0)
        #symbol1 = iterate.getTextAsList(cell1)
        #print(symbol1)
        #Assert the correct marker symbol and marker type is returned
        #self.assertEqual(symbol1, ['03.MMHAP34FRA.seq'])
        #since we search for a particular marker type verify the correct type is displayed
        #mrktype = driver.find_element(By.ID, 'markerType').get_attribute('value')
        #self.assertEqual(mrktype, 'string:2')#2 equals "DNA Segment"


    def testGeowildSearch(self):
        """
        @Status tests that a GEO ID wildcard search works
        @see pwi-htindex-search-2 *NOTE: currently broken
        """
        driver = self.driver
        #finds the ArrayExp field and enter the ID
        driver.find_element(By.ID, "geoid").send_keys("GSE10005%");
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results
        html_list = self.driver.find_element(By.CLASS_NAME, "scrollable-menu")
        items = html_list.find_elements(By.TAG_NAME, "li")
        for item in items:
            text = item.text
            print(text)
        #Assert the correct ID  is returned
        self.assertEqual(text, [''])

    def testHTindexTitleSearch(self):
        """
        @Status tests that a Title field wildcard search works
        @see pwi-htindex-search-5
        """
        driver = self.driver
        #finds the ArrayExp field and enter the ID
        driver.find_element(By.ID, "name").send_keys("%microvasculature");
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results
        html_list = self.driver.find_element(By.CLASS_NAME, "scrollable-menu")
        items = html_list.find_elements(By.TAG_NAME, "li")
        for item in items:
            text = item.text
            print(text)
        #Assert the correct ID  is returned
        self.assertEqual(text, 'E-GEOD-10035 *')
        #find the Title field
        title = self.driver.find_element(By.ID, "name")
        self.assertEqual(title.text, 'mRNA expression profiling of mouse microvasculature')
        
    def testHTindexDescSearch(self):
        """
        @Status tests that a Description field wildcard search works
        @see pwi-htindex-search-6
        """
        driver = self.driver
        #finds the ArrayExp field and enter the ID
        driver.find_element(By.ID, "description").send_keys("%angiogenesis and osteogenesis%")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results
        html_list = self.driver.find_element(By.CLASS_NAME, "scrollable-menu")
        items = html_list.find_elements(By.TAG_NAME, "li")
        for item in items:
            text = item.text
            print(text)
        #Assert the correct ID  is returned
        self.assertEqual(text, 'GSE95196')
        #find the Description field text and assert it contains angiogenesis and osteogenesis
        fetch_text = self.driver.find_element(By.ID, "description").text
        if "angiogenesis and osteogenesis" in fetch_text:
            self.assertTrue(fetch_text, 'text exists in the description')

    def testHTindexEvalSearch(self):
        """
        @Status tests that an Evaluation search works
        @see pwi-htindex-search-7
        """
        driver = self.driver
        #finds the ArrayExp field and enter the ID
        driver.find_element(By.ID, "name").send_keys("%microvasculature");
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results
        html_list = self.driver.find_element(By.CLASS_NAME, "scrollable-menu")
        items = html_list.find_elements(By.TAG_NAME, "li")
        for item in items:
            text = item.text
            print(text)
        #Assert the correct ID  is returned
        self.assertEqual(text, 'E-GEOD-10035 *')
        #find the Title field
        title = self.driver.find_element(By.ID, "name")
        self.assertEqual(title.text, 'mRNA expression profiling of mouse microvasculature')
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiHTindexSearch))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))    
