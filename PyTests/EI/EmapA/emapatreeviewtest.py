'''
Created on Jan 28, 2016
This test verifies searching within the EmapA module
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests

class TestEiEmapaTreeView(unittest.TestCase):
    """
    Test EMAPA browser treeview
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/emapaBrowser")        
        # logging in for all tests
        username = self.driver.find_element_by_name('user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = self.driver.find_element_by_name('password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = self.driver.find_element_by_name("submit") #Find the Login button
        submit.click() #click the login button
        time.sleep(1)  

    def testBasicSort(self):
        """
        tests that a basic term sort works by displaying the top terms and verifying the sort of them.
        @status: test works
        @todo: add comments
        """
        wait.forAngular(self.driver)
        #find the "Term Search" box and enter the term mouse 
        self.driver.find_element_by_id("termSearch").send_keys('mouse')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element_by_css_selector('#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        treesort = self.driver.find_element_by_id("emapaTree").find_element_by_class_name("mgitreeview")
        items = treesort.find_elements_by_css_selector(".node")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        
        self.assertEqual(["mouse", "body fluid or substance", "body region", "cavity or lining", "conceptus", "early embryo", "embryo", "extracellular matrix", "extraembryonic component", "germ layer", "organ", "organ system", "tissue", "umbilical or vitelline vessel"], searchTreeItems)

    def testSpecificStageTree(self):
        """
        tests that tree view changes to show just tree of term selected.
        @status: test works
        @todo: add comments
        """
        wait.forAngular(self.driver)
        #find the "Term Search" box and enter the term embryo
        self.driver.find_element_by_id("termSearch").send_keys('embryo')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element_by_css_selector('#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        # select specific stage
        stage20 = self.driver.find_element_by_id("stageList").find_element_by_link_text("20")
        stage20.click()
        wait.forAngular(self.driver)
        
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "embryo")
        self.assertEqual(items[1].text, "Theiler Stage 20 (11.5-13.0 dpc)")
        self.assertEqual(items[2].text, "EMAPS:1603920")
        
        
    def testDetailParent(self):
        """
        tests that term detail updates including valid parents.
        @status:  test works
        @todo: needs comments
        """
        wait.forAngular(self.driver)
        #find the "Term Search" box and enter the term cortical renal tubule 
        self.driver.find_element_by_id("termSearch").send_keys('cortical renal tubule')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element_by_css_selector('#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "cortical renal tubule")
        self.assertEqual(items[1].text, "Theiler Stages 22-28")
        self.assertEqual(items[2].text, "EMAPA:18976")
        self.assertEqual(items[3].text, 'kidney cortex tubule, renal cortex tubule')
        self.assertEqual(items[4].text.split("\n"), ["part-of developing capillary loop stage nephron group","part-of early nephron","part-of late tubule","part-of mature nephron","part-of maturing nephron","part-of renal cortex","part-of stage IV immature nephron"])
        
        stage24 = self.driver.find_element_by_id("stageList").find_element_by_link_text("24")
        stage24.click()
        wait.forAngular(self.driver)
        
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "cortical renal tubule")
        self.assertEqual(items[1].text, "Theiler Stage 24 (16.0-16.99 dpc)")
        self.assertEqual(items[2].text, "EMAPS:1897624")
        self.assertEqual(items[3].text, "kidney cortex tubule, renal cortex tubule")
        self.assertEqual(items[4].text.split("\n"), ["part-of developing capillary loop stage nephron group","part-of early nephron","part-of late tubule","part-of maturing nephron","part-of renal cortex"])
        
        stage22 = self.driver.find_element_by_id("stageList").find_element_by_link_text("22")
        stage22.click()
        wait.forAngular(self.driver)
        
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "cortical renal tubule")
        self.assertEqual(items[1].text, "Theiler Stage 22 (13.5-15.0 dpc)")
        self.assertEqual(items[2].text, "EMAPS:1897622")
        self.assertEqual(items[3].text, "kidney cortex tubule, renal cortex tubule")
        self.assertEqual(items[4].text.split("\n"), ["part-of developing capillary loop stage nephron group","part-of early nephron","part-of late tubule","part-of maturing nephron","part-of renal cortex","part-of stage IV immature nephron"])
        
        
    def testParentStage(self):
        """
        tests that if parent link is clicked remain in the current stage.
        @status: works fine
        @todo: add comments
        """
        wait.forAngular(self.driver)
        #find the "Term Search" box and enter the term 3rd ventricle% 
        self.driver.find_element_by_id("termSearch").send_keys('3rd ventricle%')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element_by_css_selector('#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "3rd ventricle")
        self.assertEqual(items[1].text, "Theiler Stages 14-28")
        self.assertEqual(items[2].text, "EMAPA:16900")
        self.assertEqual(items[3].text, "diencephalic vesicle, third ventricle")
        self.assertEqual(items[4].text.split("\n"), ["is-a brain ventricle","part-of diencephalon","part-of future diencephalon"])
        
        stage15 = self.driver.find_element_by_id("stageList").find_element_by_link_text("15")
        stage15.click()
        wait.forAngular(self.driver)
        
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "3rd ventricle")
        self.assertEqual(items[1].text, "Theiler Stage 15 (9.0-10.25 dpc)")
        self.assertEqual(items[2].text, "EMAPS:1690015")
        self.assertEqual(items[3].text, "diencephalic vesicle, third ventricle")
        self.assertEqual(items[4].text.split("\n"), ["is-a brain ventricle","part-of diencephalon"])
        
        parent = self.driver.find_element_by_id("termDetailContent").find_element_by_class_name("detailPageListData")
        parent.find_element_by_link_text("diencephalon").click()
        wait.forAngular(self.driver)
        
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "diencephalon")
        self.assertEqual(items[1].text, "Theiler Stage 15 (9.0-10.25 dpc)")
        self.assertEqual(items[2].text, "EMAPS:1689615")
        self.assertEqual(items[3].text.split("\n"), ["part-of future forebrain"])
        
        activestage = self.driver.find_element_by_css_selector(".stageselector.active")
        self.assertEqual(activestage.text,"15")
        
        
    def testClickingNode(self):
        """
        tests that if a term is clicked, the detail updates,
            and also that node expands
        """
        wait.forAngular(self.driver)
        #find the "Term Search" box and enter the term mouse
        self.driver.find_element_by_id("termSearch").send_keys('mouse')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element_by_css_selector('#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        # click tissue node in tree
        tree = self.driver.find_element_by_id("emapaTree")
        time.sleep(1)
        tissueNode = tree.find_element_by_link_text("tissue")
        tissueNode.click()
        wait.forAngular(self.driver)
        
        # verify term detail changed
        detail = self.driver.find_element_by_id("termDetailContent")
        ddItems = detail.find_elements_by_tag_name("dd")
        # verify EMAPA ID for 'tissue' is displayed
        self.assertEqual(ddItems[2].text, "EMAPA:35868")
        
        # verify tree has expanded to include children of tissue
        tree = self.driver.find_element_by_id("emapaTree")
        self.assertTrue("epithelium" in tree.text, "epithelium should be in tree view")
        self.assertTrue("muscle tissue" in tree.text, "muscle tissue should be in tree view")
             
    def tearDown(self):
        self.driver.close()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiEmapaTreeView))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
