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
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait

from base_class import EmapaBaseClass

# Tests

class TreeViewTest(unittest.TestCase, EmapaBaseClass):
    """
    Test EMAPA browser treeview
    """

    def setUp(self):
        self.init()

    def testBasicSort(self):
        """
        tests that a basic term sort works by displaying the top terms and verifying the sort of them.
        @status: test works
        @todo: add comments
        """
        self.performSearch(term="mouse")
        
        treesort = self.driver.find_element_by_id("emapTree").find_element_by_class_name("mgitreeview")
        items = treesort.find_elements_by_css_selector(".node")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        
        self.assertEqual(["mouse", "body fluid or substance", "body region", "cavity or lining", "conceptus", "early embryo", "embryo", "extraembryonic component", "germ layer", "organ", "organ system", "tissue", "umbilical or vitelline vessel"], searchTreeItems)

    def testSpecificStageTree(self):
        """
        tests that tree view changes to show just tree of term selected.
        @status: test works
        @todo: add comments
        """
        self.performSearch(term="embryo")
        
        # select specific stage
        stage20 = self.driver.find_element_by_id("stageList").find_element_by_link_text("20")
        stage20.click()
        wait.forAjax(self.driver)
        
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "embryo")
        self.assertEqual(items[1].text, "Theiler Stage 20")
        self.assertEqual(items[2].text, "EMAPS:1603920")
        
        
    def testDetailParent(self):
        """
        tests that term detail updates including valid parents.
        @status:  test works
        @todo: needs comments
        """
        self.performSearch(term="cortical renal tubule")
        
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "cortical renal tubule")
        self.assertEqual(items[1].text, "Theiler Stages 22-28")
        self.assertEqual(items[2].text, "EMAPA:18976")
        self.assertEqual(items[3].text, "kidney cortex tubule, renal cortex tubule")
        self.assertEqual(items[4].text.split("\n"), ["part-of developing capillary loop stage nephron group","part-of early nephron","part-of late tubule","part-of mature nephron","part-of maturing nephron","part-of renal cortex","part-of stage IV immature nephron"])
        
        stage24 = self.driver.find_element_by_id("stageList").find_element_by_link_text("24")
        stage24.click()
        wait.forAjax(self.driver)
        
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "cortical renal tubule")
        self.assertEqual(items[1].text, "Theiler Stage 24")
        self.assertEqual(items[2].text, "EMAPS:1897624")
        self.assertEqual(items[3].text, "kidney cortex tubule, renal cortex tubule")
        self.assertEqual(items[4].text.split("\n"), ["part-of developing capillary loop stage nephron group","part-of early nephron","part-of late tubule","part-of maturing nephron","part-of renal cortex"])
        
        stage22 = self.driver.find_element_by_id("stageList").find_element_by_link_text("22")
        stage22.click()
        wait.forAjax(self.driver)
        
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "cortical renal tubule")
        self.assertEqual(items[1].text, "Theiler Stage 22")
        self.assertEqual(items[2].text, "EMAPS:1897622")
        self.assertEqual(items[3].text, "kidney cortex tubule, renal cortex tubule")
        self.assertEqual(items[4].text.split("\n"), ["part-of developing capillary loop stage nephron group","part-of early nephron","part-of late tubule","part-of maturing nephron","part-of renal cortex","part-of stage IV immature nephron"])
        
        
    def testParentStage(self):
        """
        tests that if parent link is clicked remain in the current stage.
        @status: works fine
        @todo: add comments
        """
        self.performSearch(term="3rd ventricle%")
        
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "3rd ventricle")
        self.assertEqual(items[1].text, "Theiler Stages 14-28")
        self.assertEqual(items[2].text, "EMAPA:16900")
        self.assertEqual(items[3].text, "diencephalic vesicle, third ventricle")
        self.assertEqual(items[4].text.split("\n"), ["is-a brain ventricle","part-of diencephalon","part-of future diencephalon"])
        
        stage15 = self.driver.find_element_by_id("stageList").find_element_by_link_text("15")
        stage15.click()
        wait.forAjax(self.driver)
        
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "3rd ventricle")
        self.assertEqual(items[1].text, "Theiler Stage 15")
        self.assertEqual(items[2].text, "EMAPS:1690015")
        self.assertEqual(items[3].text, "diencephalic vesicle, third ventricle")
        self.assertEqual(items[4].text.split("\n"), ["is-a brain ventricle","part-of diencephalon"])
        
        parent = self.driver.find_element_by_id("termDetailContent").find_element_by_class_name("detailPageListData")
        parent.find_element_by_link_text("diencephalon").click()
        wait.forAjax(self.driver)
        
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "diencephalon")
        self.assertEqual(items[1].text, "Theiler Stage 15")
        self.assertEqual(items[2].text, "EMAPS:1689615")
        self.assertEqual(items[3].text.split("\n"), ["part-of future forebrain"])
        
        activestage = self.driver.find_element_by_css_selector(".stageselector.active")
        self.assertEqual(activestage.text,"15")
        
        
    def testClickingNode(self):
        """
        tests that if a term is clicked, the detail updates,
            and also that node expands
        """
        self.performSearch(term="mouse")
        
        # click tissue node in tree
        tree = self.driver.find_element_by_id("emapTree")
        tissueNode = tree.find_element_by_link_text("tissue")
        tissueNode.click()
        wait.forAjax(self.driver)
        
        # verify term detail changed
        detail = self.driver.find_element_by_id("termDetailContent")
        ddItems = detail.find_elements_by_tag_name("dd")
        # verify EMAPA ID for 'tissue' is displayed
        self.assertEqual(ddItems[2].text, "EMAPA:35868")
        
        # verify tree has expanded to include children of tissue
        tree = self.driver.find_element_by_id("emapTree")
        self.assertTrue("epithelium" in tree.text, "epithelium should be in tree view")
        self.assertTrue("muscle tissue" in tree.text, "muscle tissue should be in tree view")
             
    def tearDown(self):
        self.closeAllWindows()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TreeViewTest))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
