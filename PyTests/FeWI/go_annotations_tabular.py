'''
Created on Sep 1, 2016
This page is linked to from the Marker detail page
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        genebox = driver.find_element_by_name('nomen')
        # put your marker symbol
        genebox.send_keys("Ccr3")
        genebox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the correct marker link and clicks it
        driver.find_element_by_link_text("Ccr3").click()
        time.sleep(3)
        #Finds the All sequences link and clicks it
        driver.find_element_by_class_name("goRibbon").find_element_by_link_text("27").click()
        wait.forAjax(driver)
        #Locates the marker header table and finds the table headings
        tabularheaderlist = driver.find_element_by_id("dynamicdata")
        items = tabularheaderlist.find_elements_by_tag_name("th")
        searchTextItems = iterate.getTextAsList(items)
        wait.forAjax(driver)
        print searchTextItems
        #verifies all the table headings are correct and in order
        self.assertEqual(searchTextItems, ['Aspect','Category','Classification Term', 'Context', 'Proteoform', 'Evidence', 'Inferred From', 'Reference(s)'])

    def test_context_display(self):
        """
        @status: Tests that the correct items are displayed in the Context column, also that items that should not display are hidden(like noctua-model-id, orchid id, ECO id)
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker")
        genebox = driver.find_element_by_name('nomen')
        # put your marker symbol
        genebox.send_keys("Cxcl17")
        genebox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the correct marker link and clicks it
        driver.find_element_by_link_text("Cxcl17").click()
        wait.forAjax(driver)
        #Finds the All sequences link and clicks it
        driver.find_element_by_class_name("goRibbon").find_element_by_link_text("16").click()
        wait.forAjax(driver)
        #finds the Type column and then iterates through all items
        contextlist = driver.find_elements_by_css_selector("td.yui-dt-col-annotationExtensions .yui-dt-liner")
        searchTextItems = iterate.getTextAsList(contextlist)
        wait.forAjax(driver)
        print searchTextItems
        time.sleep(5)
        #asserts that the rows of Context data are in correct order and displayed correctly
        self.assertEqual(searchTextItems, [u'', u'', u'', u'', u'', u'', u'', u'', u'happens in lung\nhappens in larynx mucous membrane\nresults in the movement of macrophage', u'', u'', u'', u'', u'', u'', u''])
        
        
    def tearDown(self):
        self.driver.close()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGoAnnotationsPage))
    return suite

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSpecSumByRef']
    unittest.main()