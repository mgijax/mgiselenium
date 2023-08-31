'''
Created on Jun 6, 2016
Verify column headings
Verify DOIDs by allele
Verify DOIDs by marker
Note: uses highlight feature in these tests.
@author: jeffc
'''

import unittest
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys,os.path
from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
from util.table import Table
import time
import config
from config import TEST_URL

#Tests
tracemalloc.start()
class TestAlleleSummary(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/allele/")
        #self.driver.get("http://scrumdogdev.informatics.jax.org/allele/")
        self.driver.implicitly_wait(10)

# ...
    def highlight(self, element, duration=3):
        driver = self.driver

        # Store original style so it can be reset later
        original_style = element.get_attribute("style")

        # Style element with dashed red border
        driver.execute_script(
            "arguments[0].setAttribute(arguments[1], arguments[2])",
            element,
            "style",
            "border: 2px solid red; border-style: dashed;")

        # Keep element highlighted for a spell and then revert
        if (duration > 0):
            time.sleep(duration)
            driver.execute_script(
                "arguments[0].setAttribute(arguments[1], arguments[2])",
                element,
                "style",
                original_style)

       
    def test_column_headings(self):
        '''
        @status This test verifies the correct column headings are being displayed in the correct order on the page.
        '''
        self.driver.find_element(By.NAME, "nomen").clear()
        self.driver.find_element(By.NAME, "nomen").send_keys("Pkd1")
        self.driver.find_element(By.CLASS_NAME, "buttonLabel").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "tm2Jzh").click()
        assert "Pkd1<sup>tm2Jzh</sup>" in self.driver.page_source
        assert 'id="summaryHeader"' in self.driver.page_source
        assert 'id="originHeader"' in self.driver.page_source  
        self.highlight(self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle'))  
        
    def test_disease_doids_byallele(self):
        '''
        @status this test verifies In the Disease models section, that after each disease in the disease table is it's corresponding DO ID.
        '''
        self.driver.find_element(By.NAME, "nomen").clear()
        self.driver.find_element(By.NAME, "nomen").send_keys("Gata1")
        self.driver.find_element(By.CLASS_NAME, "buttonLabel").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm2Sho').click()
        disease_table = self.driver.find_element(By.ID, 'diseasetable_id')
        table = Table(disease_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))
        
        # print row 1
        cells = table.get_column_cells("Human Diseases")
        disease_cells = iterate.getTextAsList(cells)
        print(disease_cells)
        self.assertEqual(disease_cells[1], 'myelofibrosis\nIDs')
        
    def test_disease_doids_bymarker(self):
        '''
        @status this test verifies on the Phenotypes, Alleles & Disease Models Search summary page, that after each disease in the Human Disease Models column is it's corresponding DO ID.
        '''
        self.driver.find_element(By.NAME, "nomen").clear()
        self.driver.find_element(By.NAME, "nomen").send_keys("shh")
        self.driver.find_element(By.CLASS_NAME, "buttonLabel").click()
        data_table = self.driver.find_element(By.CSS_SELECTOR, "#dynamicdata").find_element(By.CSS_SELECTOR, "table > tbody.yui-dt-data")
        #this is finding all the cells in every row so you need to count cells to find the item you want
        cells = data_table.find_elements(By.TAG_NAME, "td")
        searchTextItems = iterate.getTextAsList(cells)
        print(searchTextItems)
        #this is the 167th cell which corresponds to the Human Disease model result for the seventh allele 
        self.assertEqual(searchTextItems[167], 'brachydactyly type A1 (IDs)')
        
        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAlleleSummary))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
