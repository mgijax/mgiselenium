'''
Created on Feb 15, 2016
Add'l 4 tests added Aug 2016; jlewis

@author: jeffc
'''
import unittest
import time
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys, os.path

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..')
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table


# from .base_class import EmapaBaseClass
#Tests
tracemalloc.start()
class TestEiEmapaDetail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/emapaBrowser")
        # logging in for all tests
        username = self.driver.find_element(By.NAME, 'user')  # finds the user login box
        username.send_keys(config.PWI_LOGIN)  # enters the username
        passwd = self.driver.find_element(By.NAME, 'password')  # finds the password box
        passwd.send_keys(config.PWI_PASSWORD)  # enters a valid password
        submit = self.driver.find_element(By.NAME, "submit")  # Find the Login button
        submit.click()  # click the login button
        time.sleep(1)

    def testDefaultDetail(self):
        """
        This test verifies that the initial detail is of the main term
        @status: test works
        """
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term %cort%
        self.driver.find_element(By.ID, "termSearch").send_keys('%cort%')
        time.sleep(2)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        # verify first term in search results
        term_result = self.driver.find_element(By.ID, "termResultList")
        items = term_result.find_elements(By.TAG_NAME, "li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems[0], "adrenal cortex TS22-28")

        # verify this term is loaded into term detail section
        term_det = self.driver.find_element(By.ID, "termDetailContent")
        items = term_det.find_elements(By.TAG_NAME, "dd")
        searchTermItems = iterate.getTextAsList(items)
        self.assertEqual(searchTermItems[0], "adrenal cortex")
        self.assertEqual(searchTermItems[1], "Theiler Stages 22-28")
        self.assertEqual(searchTermItems[2], "EMAPA:18427")
        self.assertEqual(searchTermItems[3], "adrenal gland cortex")
        self.assertEqual(searchTermItems[4], "part-of adrenal gland")

    def testStageLinks(self):
        """
        tests that all stage links exist in the term detail section and clicking them function correctly
        """
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term mouse
        self.driver.find_element(By.ID, "termSearch").send_keys('mouse')
        time.sleep(2)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        detailArea = self.driver.find_element(By.ID, "termDetailContent")

        stageItems = detailArea.find_elements(By.CLASS_NAME, "stageSelector")
        # add all li text to a list for "assertIn" test
        stages = iterate.getTextAsList(stageItems)

        self.assertEqual(stages,
                         ["All", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
                          "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"])

        # click stage 10
        stage10 = detailArea.find_element(By.LINK_TEXT, "10").click()
        wait.forAngular(self.driver)

        # verify EMAPS term is loaded for mouse
        detailItems = self.driver.find_elements(By.CSS_SELECTOR, "#termDetailContent dd")
        self.assertEqual(detailItems[2].text, "EMAPS:2576510")

        # verify stage is active
        activeStage = self.driver.find_element(By.CSS_SELECTOR, ".stageSelector.active")
        self.assertEqual(activeStage.text, "10")

    def testAnnotationResults(self):
        """
        tests that when you click a term from the tree the annotation results changes  to just that node results
        @status: test works
        @todo: add comments
        """
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term brain
        self.driver.find_element(By.ID, "termSearch").send_keys('brain')
        time.sleep(2)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        # select specific stage
        activetree = self.driver.find_element(By.CSS_SELECTOR, ".mgitreeview .active")
        self.assertEqual(activetree.text, "brain")

        # verify count of results for the EMAPA term
        term1CountTag = self.driver.find_element(By.CSS_SELECTOR, ".resultsLink a")
        term1Count = int(term1CountTag.text)
        # assert positive count
        self.assertGreater(term1Count, 0)

        # navigate to a term from the tree
        self.driver.find_element(By.CSS_SELECTOR, ".mgitreeview").find_element(By.LINK_TEXT,
                                                                               "brain blood vessel").click()
        wait.forAngular(self.driver)

        # verify count of results for the stage specific term2 term
        term2CountTag = self.driver.find_element(By.CSS_SELECTOR, ".resultsLink a")
        term2Count = int(term2CountTag.text)
        # assert positive count
        self.assertGreater(term2Count, 0)

        # verify the count is different from the first term
        self.assertNotEqual(term1Count, term2Count)

    def testAnnotationDetailLink(self):
        """
        tests that when you click on the annotations link in the detail section it  goes to the correct assay results
        """
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term brain blood vessel
        self.driver.find_element(By.ID, "termSearch").send_keys('brain blood vessel')
        time.sleep(2)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        time.sleep(2)
        # select specific stage
        activetree = self.driver.find_element(By.CSS_SELECTOR, ".mgitreeview .active")
        self.assertEqual(activetree.text, "brain blood vessel")
        wait.forAngular(self.driver)

        # verify annotation count exists
        annotCountTag = self.driver.find_element(By.CSS_SELECTOR, ".resultsLink > a:nth-child(1)")
        annotCount = int(annotCountTag.text)
        self.assertTrue(annotCount > 0, "annotation count not greater than zero")

        # click link to go to results page
        annotCountTag.click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        searchFor = self.driver.find_element(By.CSS_SELECTOR, ".youSearchedFor > dl:nth-child(2) > dd:nth-child(2)")

        self.assertEqual(self.driver.title, "Result Summary")
        self.assertTrue("EMAPA:35182" in searchFor.text, "You searched for does not contain structure ID")

    def testStageSpecificDetail(self):
        """
        This test verifies the stage-specific view of the Term Detail section; jlewis
        @status: test works
        """
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term renal artery
        self.driver.find_element(By.ID, "termSearch").send_keys('renal artery')
        # find the "Stage Search" box and enter the stage '22'
        self.driver.find_element(By.ID, "stageSearch").send_keys('22')
        time.sleep(2)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        time.sleep(2)
        # verify first term in search results
        term_result = self.driver.find_element(By.ID, "termResultList")
        items = term_result.find_elements(By.TAG_NAME, "li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems[0], "renal artery TS21-28")

        # verify this term is loaded into term detail section
        term_det = self.driver.find_element(By.ID, "termDetailContent")
        items = term_det.find_elements(By.TAG_NAME, "dd")
        self.assertEqual(items[0].text, "renal artery")
        self.assertEqual(items[1].text, "Theiler Stage 22 (13.5-15.0 dpc)")
        self.assertEqual(items[2].text, "EMAPS:2837322")
        self.assertEqual(items[3].text.split("\n"),
                         ["is-a artery", "part-of renal arterial system", "part-of renal large blood vessel",
                          "part-of renal vasculature", "part-of urinary system"])

    def testMinimalStageLinks(self):
        """
        tests that all stage links exist in the term detail section and clicking them function correctly; this is for a case with only a few stages; jlewis
        """
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term second polar body
        self.driver.find_element(By.ID, "termSearch").send_keys('second polar body')
        time.sleep(2)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        time.sleep(2)
        detailArea = self.driver.find_element(By.ID, "termDetailContent")

        stageItems = detailArea.find_elements(By.CLASS_NAME, "stageSelector")
        # add all link text to a list for "assertIn" test
        stages = iterate.getTextAsList(stageItems)

        self.assertEqual(stages, ["All", "1", "2", "3", "4"])

        # click stage 1
        stage1 = detailArea.find_element(By.LINK_TEXT, "1").click()
        # wait.forAjax(self.driver)
        time.sleep(2)
        # verify EMAPS term is loaded for second polar body
        detailItems = self.driver.find_elements(By.CSS_SELECTOR, "#termDetailContent dd")
        self.assertEqual(detailItems[2].text, "EMAPS:1603401")

        # verify stage is active
        activeStage = self.driver.find_element(By.CSS_SELECTOR, ".stageSelector.active")
        self.assertEqual(activeStage.text, "1")

    def testAnnotationStageResults(self):
        """
        tests that when you click a term for a specific stage from the tree the annotation results changes  to just that node results; jlewis
        @status: test works
        """
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term bowman's capsule%
        self.driver.find_element(By.ID, "termSearch").send_keys("bowman's capsule%")
        # find the "Stage Search" box and enter the stage '26'
        self.driver.find_element(By.ID, "stageSearch").send_keys('26')
        time.sleep(2)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        time.sleep(2)
        # verify tree is highlighting correct term
        activetree = self.driver.find_element(By.CSS_SELECTOR, ".mgitreeview .active")
        self.assertEqual(activetree.text, "Bowman's capsule of mature renal corpuscle")

        # verify there is a count of results for the EMAPS term
        term1CountTag = self.driver.find_element(By.CSS_SELECTOR, ".resultsLink a")
        term1Count = int(term1CountTag.text)
        # assert positive count
        self.assertGreater(term1Count, 0)

        # navigate to a child term from the tree
        self.driver.find_element(By.CSS_SELECTOR, ".mgitreeview").find_element(By.LINK_TEXT,
                                                                               "urinary space of mature renal corpuscle").click()
        wait.forAngular(self.driver)

        # verify count of results for the stage specific term2 term
        term2CountTag = self.driver.find_element(By.CSS_SELECTOR, ".resultsLink a")
        term2Count = int(term2CountTag.text)
        # assert zero count (as-of data on 8/18/2016)
        self.assertEqual(term2Count, 0)

        # verify the count is different from the first term
        self.assertNotEqual(term1Count, term2Count)

    def testAnnotationStageDetailLink(self):
        """
        tests that when you click on the annotations link in the detail section it  goes to the correct assay results; jlewis
        """
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term thymus/parathyroid primordium
        self.driver.find_element(By.ID, "termSearch").send_keys("thymus/parathyroid primordium")
        # find the "Stage Search" box and enter the stage '19'
        self.driver.find_element(By.ID, "stageSearch").send_keys('19')
        time.sleep(2)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        time.sleep(2)
        # select specific stage
        activetree = self.driver.find_element(By.CSS_SELECTOR, ".mgitreeview .active")
        self.assertEqual(activetree.text, "thymus/parathyroid primordium")
        wait.forAjax(self.driver)

        # verify annotation count exists
        annotCountTag = self.driver.find_element(By.CSS_SELECTOR, ".resultsLink a")
        annotCount = int(annotCountTag.text)
        self.assertTrue(annotCount > 0, "annotation count not greater than zero")

        # click link to go to results page
        annotCountTag.click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(10)

        searchFor = self.driver.find_element(By.CSS_SELECTOR, ".youSearchedFor > dl:nth-child(2) > dd:nth-child(2)")

        self.assertEqual(self.driver.title, "Result Summary")
        self.assertTrue("EMAPS:3586519" in searchFor.text,
                        "You searched for does not contain structure ID")

        body = self.driver.find_element(By.TAG_NAME, "body")
        self.assertTrue(("of %d" % annotCount) in body.text, "same annotation count not found on results summary")

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiEmapaDetail))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))