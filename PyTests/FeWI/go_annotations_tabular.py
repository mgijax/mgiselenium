'''
Created on Sep 1, 2016
This page is linked to from the Marker detail page
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import sys,os.path
from util import wait, iterate
from config.config import TEST_URL
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import TEST_URL

class TestGoAnnotationsPage(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        
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
        time.sleep(3)
        #finds the correct marker link and clicks it
        driver.find_element(By.LINK_TEXT, 'Ccr3').click()
        time.sleep(3)
        #Finds the All GO Annotations link and clicks it
        driver.find_element(By.CLASS_NAME, 'goRibbon').find_element(By.ID, 'goAnnotLink').click()
        wait.forAjax(driver)
        #Locates the marker header table and finds the table headings
        tabularheaderlist = driver.find_element(By.ID, 'dynamicdata')
        items = tabularheaderlist.find_elements(By.TAG_NAME, 'th')
        searchTextItems = iterate.getTextAsList(items)
        wait.forAjax(driver)
        print searchTextItems
        #verifies all the table headings are correct and in order
        self.assertEqual(searchTextItems, ['Aspect','Category','Classification Term', 'Context', 'Proteoform', 'Evidence', 'Inferred From', 'Reference(s)'])

    def test_context_display(self):
        """
        @status: Tests that the correct items are displayed in the Context column, also that items that should not display are hidden(like noctua-model-id, orchid id, ECO id)
        @attention: This test is still under construction!!!
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
        #contextlist = driver.find_elements(By.CSS_SELECTOR, 'td.yui-dt-annotationExtensions div.goProperties.span.value')
        webElement = driver.find_elements_by_class_name('goProperties')
        print webElement
        #searchTextItems = iterate.getTextAsList(webElement)
        #wait.forAjax(driver)
        #print searchTextItems
        time.sleep(5)
        element = driver.find_element_by_class_name('goProperties')
        elementText = element.text
        print elementText
        #asserts that the rows of Context data are in correct order and displayed correctly
        #self.assertEqual(searchTextItems, [u'', u'', u'', u'', u'', u'', u'', u'', u'happens in lung\nhappens in larynx mucous membrane\nresults in the movement of macrophage', u'', u'', u'', u'', u'', u'', u''])
        self.assertIn(elementText, ['happens in lung\nhappens in larynx mucous membrane\nresults in the movement of macrophage'])
        #self.assertIn(elementText, ['happens in larynx mucous membrane'])
        #self.assertIn(elementText, ['results in the movement of macrophage'])
        #self.assertNotin(elementText, ['noctua-model-id'])
        
    def tearDown(self):
        self.driver.close()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGoAnnotationsPage))
    return suite

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSpecSumByRef']
    unittest.main()