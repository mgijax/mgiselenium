
'''
Created on Jan 28, 2016
This test verifies searching within the EmapA module, Both a term search and a stage search
@author: jeffc
'''
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait


# Constants
BROWSER_URL = config.PWI_URL + "/edit/emapBrowser"

# Tests

class SearchTest(unittest.TestCase):
    """
    Test EMAPA browser search
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(BROWSER_URL)
        self.driver.implicitly_wait(10)

    def testBasicSearch(self):
        """
        tests that a basic term search works
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("brain")
        searchbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        term_result = self.driver.find_element_by_id("termResultList")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)
        
        self.assertIn('brain TS17-28', searchTextItems)
        
    def testSynonymSearch(self):
        """
        tests that a synonym term search works
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("myocardium")
        searchbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        term_result = self.driver.find_element_by_id("emapTermArea")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)
        
        self.assertIn('cardiac muscle tissue TS12-28', searchTextItems)        

    def testWildcardSearch(self):
        """
        tests that a wildcard term search works
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("%tectum")
        searchbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        term_result = self.driver.find_element_by_id("termResultList")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)
        
        self.assertIn('pretectum TS22-28', searchTextItems)
        self.assertIn('tectum TS22-28', searchTextItems)
        
    def testStageSearch(self):
        """
        tests that a stage search works, test under construction
        """
        searchbox = self.driver.find_element_by_id("stageSearch")
        searchbox.send_keys("10")
        searchbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        term_result = self.driver.find_element_by_id("emapTermArea")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)
        
        self.assertIn('??????', searchTextItems)
        
    def testMultipleStageSearch(self):
        """
        tests that a multiple stages search works, test under construction
        """
        searchbox = self.driver.find_element_by_id("stageSearch")
        searchbox.send_keys("10,11,12")
        searchbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        term_result = self.driver.find_element_by_id("emapTermArea")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)
        
        self.assertIn('??????', searchTextItems)
        
            
    def tearDown(self):
        self.driver.close()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SearchTest))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
