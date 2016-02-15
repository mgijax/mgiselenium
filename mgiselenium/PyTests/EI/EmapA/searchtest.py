
'''
Created on Jan 28, 2016
This test verifies searching within the EmapA module
@author: jeffc
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants
BROWSER_URL = "http://scrumdog.informatics.jax.org/pwi/edit/emapBrowser"
# TODO(kstone): move browser urls to a config file
#BROWSER_URL = "http://mlg-balrog.jax.org:7000/pwi/edit/emapBrowser"

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
        tests that a basic term search work
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("brain")
        searchbox.send_keys(Keys.RETURN)
        term_result = self.driver.find_element_by_id("termResultList")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextItems = self.getSearchTextAsList(items)
        
        self.assertIn('brain TS17-28', searchTextItems)
        
    def testSynonymSearch(self):
        """
        tests that a synonym term search works
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("myocardium")
        searchbox.send_keys(Keys.RETURN)
        term_result = self.driver.find_element_by_id("emapTermArea")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextItems = self.getSearchTextAsList(items)
        
        self.assertIn('cardiac muscle tissue TS12-28', searchTextItems)        

    def testWildcardSearch(self):
        """
        tests that a wildcard term search works
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("%tectum")
        searchbox.send_keys(Keys.RETURN)
        term_result = self.driver.find_element_by_id("termResultList")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextItems = self.getSearchTextAsList(items)
        
        self.assertIn('pretectum TS22-28', searchTextItems)
        self.assertIn('tectum TS22-28', searchTextItems)
        
    def testTermWithCommaSearch(self):
        """
        tests that a term with a comma search works
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("female,%")
        searchbox.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_id("emapTermArea")
        assert False
        
        
    def getSearchTextAsList(self, liItems):
        """
        Take all found li tags in liItems
            and return a list of all the text values
            for each li tag
        """
        searchTextItems = []
        for item in liItems:
            text = item.text
            searchTextItems.append(item.text)
            
        print "li text = %s" % searchTextItems
        return searchTextItems
        
        
            
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()