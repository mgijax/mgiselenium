'''
Created on Feb 15, 2016

@author: jeffc
'''
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
from dircache import annotate
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..')
)
import config
from util import wait

import time 


# Constants
BROWSER_URL = config.PWI_URL + "/edit/emapBrowser"

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(BROWSER_URL)
        self.driver.implicitly_wait(1)

    def testDefaultDetail(self):
        """
        This test verifies that the initial detail is of the main term
        @status: test works
        @todo: needs more comments
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("%cort%")
        searchbox.send_keys(Keys.RETURN)
        
        wait.forAjax(self.driver)
        
        term_result = self.driver.find_element_by_id("termResultList")
        items = term_result.find_elements_by_tag_name("li")
        searchTextItems = self.getSearchTextAsList(items)
        self.assertEqual(searchTextItems[0], "adrenal cortex TS22-28")
        
        term_det = self.driver.find_element_by_id("termDetailContent")
        item = term_det.find_elements_by_tag_name("dd")
        searchTermItems = self.getTermDetailTextAsList(item)
        self.assertEqual(searchTermItems[0], "adrenal cortex")
        self.assertEqual(searchTermItems[1], "Theiler Stages 22-28")
        self.assertEqual(searchTermItems[2], "EMAPA:18427")
        self.assertEqual(searchTermItems[3], "adrenal gland cortex")
        self.assertEqual(searchTermItems[4], "part-of adrenal gland")
        
    def teststagelinks(self):
        """
        tests that all stage links exist in the term detail section and clicking them function correctly
        @status:  works fine
        @todo: Add comments and still need code for clicking a stage link
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("mouse")
        searchbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        stageitems = self.driver.find_elements_by_class_name("stageSelector")
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(stageitems)
        
        self.assertEqual(searchTreeItems, ["All","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"])

    def testannotationresults(self):
        """
        tests that when you click a term from the tree the annotation results changes  to just that node results
        @status: under construction
        @todo: add comments
        """
        
        # perform term search
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("brain")
        searchbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        # select specific stage
        activetree = self.driver.find_element_by_css_selector(".mgitreeview .active")
        self.assertEqual(activetree.text,"brain")
        wait.forAjax(self.driver)
        
        annotdata = self.driver.find_element_by_css_selector(".resultsLink")
        self.assertEqual(annotdata.text, "32262 direct annotations")
        wait.forAjax(self.driver)
        
        self.driver.find_element_by_css_selector(".mgitreeview").find_element_by_link_text("brain blood vessel").click()
        wait.forAjax(self.driver)
        annotdata = self.driver.find_element_by_css_selector(".resultsLink")
        self.assertEqual(annotdata.text, "62 direct annotations")
        
    def testannotationdetaillink(self):
        """
        tests that when you click on the annoations link in the detail section it  goes to the correct assay results
        @status: under construction
        @todo: add comments
        """
        
        # perform term search
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("brain blood vessel")
        searchbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        # select specific stage
        activetree = self.driver.find_element_by_css_selector(".mgitreeview .active")
        self.assertEqual(activetree.text,"brain blood vessel")
        wait.forAjax(self.driver)        
        
        
        #testing on new displayed page
        annotdata = self.driver.find_element_by_css_selector(".resultsLink")
        self.assertEqual(annotdata.text, "62 direct annotations")
        
        anchor = annotdata.find_element_by_css_selector("a")
        anchor.click()
        
        time.sleep(3)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        
        searchfor =self.driver.find_element_by_css_selector(".youSearchedFor")
        
        self.assertEqual(self.driver.title, "Result Summary")
        
        
        
    def getSearchTextAsList(self, liItems):
        """
        Take all found li tags in liItems
            and return a list of all the text values
            for each li tag (search result section)
        """
        searchTextItems = []
        for item in liItems:
            text = item.text
            searchTextItems.append(item.text)
            
        print "li text = %s" % searchTextItems
        return searchTextItems
    
    def getTermDetailTextAsList(self, ddItem):            
        """
        Take all found dd tags in ddItem 
            and return a list of all the text values 
            for each dd tag (term detail section)
        """
        searchTermItems = []
        for item in ddItem:
            text = item.text
            searchTermItems.append(item.text)
            
        print "dd text = %s" % searchTermItems
        return searchTermItems

    def tearDown(self):
        self.driver.close()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
