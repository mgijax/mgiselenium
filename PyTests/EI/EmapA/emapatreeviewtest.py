'''
Created on Jan 28, 2016
This test verifies searching within the EmapA module
@author: jeffc
'''
import unittest
import time
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

    def testSpecificStageTree(self):
        """
        tests that tree view changes to show just tree of term selected, test under construction
        """
        
        # perform term search
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("embryo")
        searchbox.send_keys(Keys.RETURN)
        
        # select specific stage
        stage20 = self.driver.find_element_by_id("stageList").find_element_by_link_text("20")
        stage20.click()
        
        time.sleep(1)
        
        # TODO: assert something
#         treesort = self.driver.find_element_by_id("emapTree").find_element_by_class_name("mgitreeview")
#         items = treesort.find_elements_by_css_selector("mark")
#         
#         # add all li text to a list for "assertIn" test
#         searchTreeItems = self.getSearchTextAsList(items)
#         activestage = self.driver.find_element_by_id("stageList").find_element_by_class_name("stageSelector")
#         
#         self.assertEqual(["embryo","embryo"], searchTreeItems)
#         self.assertEqual(activestage.find_element_by_link_text("All"), "All", "incorrect stage selected")

    def testdetailparent(self):
        """
        tests that term detail updates including valid parents, test under construction
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("mouse")
        searchbox.send_keys(Keys.RETURN)
        treesort = self.driver.find_element_by_id("emapTree").find_element_by_class_name("mgitreeview")
        items = treesort.find_elements_by_css_selector(".node")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(items)
        
        self.assertEqual(["mouse", "body fluid or substance", "body region", "cavity or lining", "conceptus", "early embryo", "embryo", "extraembryonic component", "germ layer", "organ", "organ system", "tissue", "umbilical or vitelline vessel"], searchTreeItems)

    def testparentstage(self):
        """
        tests that if parent link is clicked remain in the current stage, test under construction
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("mouse")
        searchbox.send_keys(Keys.RETURN)
        treesort = self.driver.find_element_by_id("emapTree").find_element_by_class_name("mgitreeview")
        items = treesort.find_elements_by_css_selector(".node")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(items)
        
        self.assertEqual(["mouse", "body fluid or substance", "body region", "cavity or lining", "conceptus", "early embryo", "embryo", "extraembryonic component", "germ layer", "organ", "organ system", "tissue", "umbilical or vitelline vessel"], searchTreeItems)

    def teststagelinks(self):
        """
        tests that all stage links exist in the term detail section and clicking them function correctly, test under construction
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("mouse")
        searchbox.send_keys(Keys.RETURN)
        treesort = self.driver.find_element_by_id("emapTree").find_element_by_class_name("mgitreeview")
        items = treesort.find_elements_by_css_selector(".node")
        time.sleep(5)
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(items)
        stagesort = self.driver.find_element_by_id(".stageList")
        stageitems = stagesort.find_elements_by_class_name("stageSelector")
        time.sleep(5)
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(stageitems)
        
        self.assertEqual([stageitems.text, "All", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], searchTreeItems)

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


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TreeViewTest))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
