'''
Created on Sep 1, 2016
This page is linked to from the Marker detail page
@author: jeffc
Verify the table headers are correct
Verify the context column data
Verify the sorting of the Aspect column
'''
import unittest
import time
import tracemalloc
import config
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import wait, iterate
from config.config import TEST_URL
from config import TEST_URL

#Tests
tracemalloc.start()
class TestGoAnnotationsPage(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        
    def test_table_headers(self):
        """
        @status: Tests that the Gene Ontology Classifications page in Tabular view, table headers are correct
        Headers are: Aspect, Category, Classification Term, Context, Proteoform, Evidence, Inferred From, Reference(s)
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker")
        genebox = driver.find_element(By.NAME, 'nomen')
        # put your marker symbol in the Nomenclature box
        genebox.send_keys("Ccr3")
        genebox.send_keys(Keys.RETURN)
        time.sleep(2)
        #finds the correct marker link and clicks it
        driver.find_element(By.LINK_TEXT, 'Ccr3').click()
        #Finds the All GO Annotations link and clicks it
        driver.find_element(By.CLASS_NAME, 'goRibbon').find_element(By.ID, 'goAnnotLink').click()
        wait.forAjax(driver)
        #Locates the marker header table and finds the table headings
        tabularheaderlist = driver.find_element(By.ID, 'dynamicdata')
        items = tabularheaderlist.find_elements(By.TAG_NAME, 'th')
        searchTextItems = iterate.getTextAsList(items)
        wait.forAjax(driver)
        print(searchTextItems)
        #verifies all the table headings are correct and in order
        self.assertEqual(searchTextItems, ['Aspect','Category','Classification Term', 'Context', 'Proteoform', 'Evidence', 'Inferred From', 'Reference(s)'])

    def test_context_display(self):
        """
        @status: Tests that the correct items are displayed in the Context column, also that items that should not display are hidden(like noctua-model-id, orchid id, ECO id)
        @attention: This test is still under construction!!! Need to figure out how to capture/assert  items in Context  fields
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker")
        genebox = driver.find_element(By.NAME, 'nomen')
        # put your marker symbol
        genebox.send_keys("cxcl17")
        genebox.send_keys(Keys.RETURN)
        time.sleep(2)
        #finds the correct marker link and clicks it
        driver.find_element(By.LINK_TEXT, 'Cxcl17').click()
        wait.forAjax(driver)
        #Finds the All GO Annotations link and clicks it
        driver.find_element(By.CLASS_NAME, 'goRibbon').find_element(By.ID, 'goAnnotLink').click()
        wait.forAjax(driver)
        #finds the Type column and then iterates through all items
        context = driver.find_elements(By.CLASS_NAME, 'goProperties')
        print(context)
        #searchTextItems = iterate.getTextAsList(webElement)
        #wait.forAjax(driver)
        #print searchTextItems
        time.sleep(5)
        #element = driver.find_element(By.CLASS_NAME, 'goProperties')
        #elementText = element.text
        #print(elementText)
        #asserts that the rows of Context data are in correct order and displayed correctly
        #self.assertEqual(searchTextItems, [u'', u'', u'', u'', u'', u'', u'', u'', u'happens in lung\nhappens in larynx mucous membrane\nresults in the movement of macrophage', u'', u'', u'', u'', u'', u'', u''])
        #self.assertIn(elementText, ['happens in lung\nhappens in larynx mucous membrane\nresults in the movement of macrophage'])
        #self.assertIn(elementText, ['happens in larynx mucous membrane'])
        #self.assertIn(elementText, ['results in the movement of macrophage'])
        #self.assertNotin(elementText, ['noctua-model-id'])
        
    def test_aspect_sort(self):
        """
        @status: Tests that the sorting of Aspect column is by smart alpha/reverse smart alpha
        Note: annotations with Proteoform data always display at top of table
        Note: this test is not perfect but it does test the basic sorting of aspect!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker")
        genebox = driver.find_element(By.NAME, 'nomen')
        # put your marker symbol in the Nomenclature box
        genebox.send_keys("Ednrb")
        genebox.send_keys(Keys.RETURN)
        time.sleep(2)
        #finds the correct marker link and clicks it
        driver.find_element(By.LINK_TEXT, 'Ednrb').click()
        wait.forAjax(driver)
        #Finds the All GO Annotations link and clicks it
        driver.find_element(By.CLASS_NAME, 'goRibbon').find_element(By.ID, 'goAnnotLink').click()
        wait.forAjax(driver)
        #Locates  the table by row
        tabularheaderlist = driver.find_element(By.ID, 'dynamicdata')
        items = tabularheaderlist.find_elements(By.TAG_NAME, 'div')
        searchTextItems = iterate.getTextAsList(items)
        asp1 = driver.find_element(By.CSS_SELECTOR, '#yui-rec0')
        asp11 = driver.find_element(By.CSS_SELECTOR, '#yui-rec10')
        asp16 = driver.find_element(By.CSS_SELECTOR, '#yui-rec15')
        print(asp1.text)
        print(asp11.text)
        print(asp16.text)
        wait.forAjax(driver)
        self.assertEqual(asp1.text, 'Molecular Function\nsignaling receptor activity\nendothelin receptor activity\nIBA\nPTN002517505\nJ:265628 [PMID:21873635]', 'the aspect is wrong')
        self.assertEqual(asp11.text, 'Cellular Component\nmembrane\nIEA\nIPR000276 | IPR000499 | IPR001112 | IPR017452\nJ:72247', 'the aspect is wrong')
        self.assertEqual(asp16.text, 'Biological Process\nlipid metabolic process\naldosterone metabolic process\nIMP\nMGI:3693642\nJ:116002 [PMID:16868309]', 'the aspect is wrong')
    
    
        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGoAnnotationsPage))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))