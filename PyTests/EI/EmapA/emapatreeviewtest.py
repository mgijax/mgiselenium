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
        time.sleep(1)
        # select specific stage
        stage20 = self.driver.find_element_by_id("stageList").find_element_by_link_text("20")
        stage20.click()
        time.sleep(3)
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "embryo")
        self.assertEqual(items[1].text, "Theiler Stage 20")
        self.assertEqual(items[2].text, "EMAPS:1603920")
        
        
    def testdetailparent(self):
        """
        tests that term detail updates including valid parents, test under construction
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("cortical renal tubule")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "cortical renal tubule")
        self.assertEqual(items[1].text, "Theiler Stages 22-28")
        self.assertEqual(items[2].text, "EMAPA:18976")
        self.assertEqual(items[3].text, "kidney cortex tubule, renal cortex tubule")
        self.assertEqual(items[4].text.split("\n"), ["part-of developing capillary loop stage nephron group","part-of early nephron","part-of late tubule","part-of mature nephron","part-of maturing nephron","part-of renal cortex","part-of stage IV immature nephron"])
        
        stage24 = self.driver.find_element_by_id("stageList").find_element_by_link_text("24")
        stage24.click()
        time.sleep(3)
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "cortical renal tubule")
        self.assertEqual(items[1].text, "Theiler Stage 24")
        self.assertEqual(items[2].text, "EMAPS:1897624")
        self.assertEqual(items[3].text, "kidney cortex tubule, renal cortex tubule")
        self.assertEqual(items[4].text.split("\n"), ["part-of developing capillary loop stage nephron group","part-of early nephron","part-of late tubule","part-of maturing nephron","part-of renal cortex"])
        
        stage22 = self.driver.find_element_by_id("stageList").find_element_by_link_text("22")
        stage22.click()
        time.sleep(3)
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "cortical renal tubule")
        self.assertEqual(items[1].text, "Theiler Stage 22")
        self.assertEqual(items[2].text, "EMAPS:1897622")
        self.assertEqual(items[3].text, "kidney cortex tubule, renal cortex tubule")
        self.assertEqual(items[4].text.split("\n"), ["part-of developing capillary loop stage nephron group","part-of early nephron","part-of late tubule","part-of maturing nephron","part-of renal cortex","part-of stage IV immature nephron"])
        
        
        
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
