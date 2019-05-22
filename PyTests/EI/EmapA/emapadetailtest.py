'''
Created on Feb 15, 2016
Add'l 4 tests added Aug 2016; jlewis

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
from util import iterate, wait
from base_class import EmapaBaseClass

class TestEmapaDetail(unittest.TestCase, EmapaBaseClass):


    def setUp(self):
        self.init()

    def testDefaultDetail(self):
        """
        This test verifies that the initial detail is of the main term
        @status: test works
        """
        self.performSearch(term="%cort%")
        
        # verify first term in search results
        term_result = self.driver.find_element_by_id("termResultList")
        items = term_result.find_elements_by_tag_name("li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems[0], "adrenal cortex TS22-28")
        
        # verify this term is loaded into term detail section
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
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
        self.performSearch(term="mouse")
        
        detailArea = self.driver.find_element_by_id("termDetailContent")
        
        stageItems = detailArea.find_elements_by_class_name("stageSelector")
        # add all li text to a list for "assertIn" test
        stages = iterate.getTextAsList(stageItems)
        
        self.assertEqual(stages, ["All","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"])

        # click stage 10
        stage10 = detailArea.find_element_by_link_text("10").click()
        wait.forAngular(self.driver)  
        
        #verify EMAPS term is loaded for mouse
        detailItems = self.driver.find_elements_by_css_selector("#termDetailContent dd")
        self.assertEqual(detailItems[2].text, "EMAPS:2576510")
        
        # verify stage is active
        activeStage = self.driver.find_element_by_css_selector(".stageSelector.active")
        self.assertEqual(activeStage.text, "10")


    def testAnnotationResults(self):
        """
        tests that when you click a term from the tree the annotation results changes  to just that node results
        @status: test works
        @todo: add comments
        """
        
        self.performSearch(term="brain")
        
        # select specific stage
        activetree = self.driver.find_element_by_css_selector(".mgitreeview .active")
        self.assertEqual(activetree.text,"brain")
        
        # verify count of results for the EMAPA term
        term1CountTag = self.driver.find_element_by_css_selector(".resultsLink a")
        term1Count = int(term1CountTag.text)
        # assert positive count
        self.assertGreater(term1Count,0)
        
        # navigate to a term from the tree
        self.driver.find_element_by_css_selector(".mgitreeview").find_element_by_link_text("brain blood vessel").click()
        wait.forAngular(self.driver)  
        
        # verify count of results for the stage specific term2 term
        term2CountTag = self.driver.find_element_by_css_selector(".resultsLink a")
        term2Count = int(term2CountTag.text)
        # assert positive count
        self.assertGreater(term2Count,0)
        
        # verify the count is different from the first term
        self.assertNotEqual(term1Count, term2Count)
        
    def testAnnotationDetailLink(self):
        """
        tests that when you click on the annotations link in the detail section it  goes to the correct assay results
        """
        self.performSearch(term="brain blood vessel")
        
        # select specific stage
        activetree = self.driver.find_element_by_css_selector(".mgitreeview .active")
        self.assertEqual(activetree.text,"brain blood vessel")
        wait.forAngular(self.driver)        
        
        
        # verify annotation count exists
        annotCountTag = self.driver.find_element_by_css_selector(".resultsLink a")
        annotCount = int(annotCountTag.text)
        self.assertTrue(annotCount > 0, "annotation count not greater than zero")
        
        # click link to go to results page
        annotCountTag.click()
        
        wait.forNewWindow(self.driver)
        
        searchFor = self.driver.find_element_by_css_selector(".youSearchedFor")
        
        self.assertEqual(self.driver.title, "Result Summary")
        self.assertTrue("brain blood vessel" in searchFor.text, "You searched for does not contain structure name")
        
        body = self.driver.find_element_by_tag_name("body")
        self.assertTrue( ("of %d" % annotCount) in body.text, "same annotation count not found on results summary")
        
        
    def testStageSpecificDetail(self):
        """
        This test verifies the stage-specific view of the Term Detail section; jlewis
        @status: test works
        """
        self.performSearch(term="renal artery", stage="22")
        
        # verify first term in search results
        term_result = self.driver.find_element_by_id("termResultList")
        items = term_result.find_elements_by_tag_name("li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems[0], "renal artery TS21-28")
        
        # verify this term is loaded into term detail section
        term_det = self.driver.find_element_by_id("termDetailContent")
        items = term_det.find_elements_by_tag_name("dd")
        self.assertEqual(items[0].text, "renal artery")
        self.assertEqual(items[1].text, "Theiler Stage 22 (13.5-15.0 dpc)")
        self.assertEqual(items[2].text, "EMAPS:2837322")
        self.assertEqual(items[3].text.split("\n"), ["is-a artery","part-of renal arterial system","part-of renal large blood vessel","part-of renal vasculature", "part-of urinary system"])
       
        
    def testMinimalStageLinks(self):
        """
        tests that all stage links exist in the term detail section and clicking them function correctly; this is for a case with only a few stages; jlewis
        """
        self.performSearch(term="second polar body")
        
        detailArea = self.driver.find_element_by_id("termDetailContent")
        
        stageItems = detailArea.find_elements_by_class_name("stageSelector")
        # add all link text to a list for "assertIn" test
        stages = iterate.getTextAsList(stageItems)
        
        self.assertEqual(stages, ["All", "1", "2", "3", "4"])

        # click stage 1
        stage1 = detailArea.find_element_by_link_text("1").click()
        wait.forAjax(self.driver)
        
        #verify EMAPS term is loaded for second polar body
        detailItems = self.driver.find_elements_by_css_selector("#termDetailContent dd")
        self.assertEqual(detailItems[2].text,"EMAPA:16034")
        
        
        # verify stage is active
        activeStage = self.driver.find_element_by_css_selector(".stageSelector.active")
        self.assertEqual(activeStage.text,"1")


    def testAnnotationStageResults(self):
        """
        tests that when you click a term for a specific stage from the tree the annotation results changes  to just that node results; jlewis
        @status: test works
        """
        
        self.performSearch(term="bowman's capsule%", stage=26)
        
        # verify tree is highlighting correct term
        activetree = self.driver.find_element_by_css_selector(".mgitreeview .active")
        self.assertEqual(activetree.text,"Bowman's capsule of mature renal corpuscle")
        
        # verify there is a count of results for the EMAPS term
        term1CountTag = self.driver.find_element_by_css_selector(".resultsLink a")
        term1Count = int(term1CountTag.text)
        # assert positive count
        self.assertGreater(term1Count,0)
        
        # navigate to a child term from the tree
        self.driver.find_element_by_css_selector(".mgitreeview").find_element_by_link_text("urinary space of mature renal corpuscle").click()
        wait.forAngular(self.driver)
        
        # verify count of results for the stage specific term2 term
        term2CountTag = self.driver.find_element_by_css_selector(".resultsLink a")
        term2Count = int(term2CountTag.text)
        # assert zero count (as-of data on 8/18/2016)
        self.assertEqual(term2Count,0)
        
        # verify the count is different from the first term
        self.assertNotEqual(term1Count, term2Count)
        
    def testAnnotationStageDetailLink(self):
        """
        tests that when you click on the annotations link in the detail section it  goes to the correct assay results; jlewis
        """
        self.performSearch(term="thymus/parathyroid primordium", stage="19")
        
        # select specific stage
        activetree = self.driver.find_element_by_css_selector(".mgitreeview .active")
        self.assertEqual(activetree.text,"thymus/parathyroid primordium")
        wait.forAjax(self.driver)        
        
        
        # verify annotation count exists
        annotCountTag = self.driver.find_element_by_css_selector(".resultsLink a")
        annotCount = int(annotCountTag.text)
        self.assertTrue(annotCount > 0, "annotation count not greater than zero")
        
        # click link to go to results page
        annotCountTag.click()
        
        wait.forNewWindow(self.driver)
        
        searchFor = self.driver.find_element_by_css_selector(".youSearchedFor")
        
        self.assertEqual(self.driver.title, "Result Summary")
        self.assertTrue("thymus/parathyroid primordium" in searchFor.text, "You searched for does not contain structure name")
        
        body = self.driver.find_element_by_tag_name("body")
        self.assertTrue( ("of %d" % annotCount) in body.text, "same annotation count not found on results summary")                 

        

    def tearDown(self):
        self.closeAllWindows()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEmapaDetail))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
