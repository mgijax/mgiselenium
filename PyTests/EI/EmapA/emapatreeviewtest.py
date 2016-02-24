'''
Created on Jan 28, 2016
This test verifies searching within the EmapA module
@author: jeffc
'''
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../../config',)
)
import config


# Constants
BROWSER_URL = config.PWI_URL + "/edit/emapBrowser"

# Tests

class TreeViewTest(unittest.TestCase):
    """
    Test EMAPA browser treeview
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(BROWSER_URL)
        self.driver.implicitly_wait(10)

    def testBasicSort(self):
        """
        tests that a basic term sort works by displaying the top terms and verifying the sort of them
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("mouse")
        searchbox.send_keys(Keys.RETURN)
        treesort = self.driver.find_element_by_id("emapTree").find_element_by_class_name("mgitreeview")
        items = treesort.find_elements_by_css_selector(".node")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(items)
        
        self.assertEqual(["mouse", "body fluid or substance", "body region", "cavity or lining", "conceptus", "early embryo", "embryo", "extraembryonic component", "germ layer", "organ", "organ system", "tissue", "umbilical or vitelline vessel"], searchTreeItems)

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
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
