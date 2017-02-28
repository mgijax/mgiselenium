
'''
Created on Jan 28, 2016
This test verifies searching within the EmapA module, Both a term search and a stage search
Add'l 4 tests added August 2016; jlewis
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

class TestSearch(unittest.TestCase, EmapaBaseClass):
    """
    @status Test EMAPA browser search using terms, stages, synonymns
    """

    def setUp(self):
        self.init()

    def testBasicSearch(self):
        """
        tests that a basic term search works
        """
        self.performSearch(term="brain")
        
        term_result = self.driver.find_element_by_id("termResultList")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)
        
        self.assertIn('brain TS17-28', searchTextItems)
        
    def testSynonymSearch(self):
        """
        tests that a synonym term search works
        """
        self.performSearch(term="myocardium")
        
        term_result = self.driver.find_element_by_id("emapTermArea")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)
        
        self.assertIn('cardiac muscle tissue TS12-28 (myocardium)', searchTextItems)        
        

    def testWildcardSearch(self):
        """
        tests that a wildcard term search works
        """
        self.performSearch(term="%tectum")
        
        term_result = self.driver.find_element_by_id("termResultList")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextTerms = self.getOnlyTermNames(items)
        
        self.assertIn('pretectum', searchTextTerms)
        self.assertIn('tectum', searchTextTerms)
        
    def testStageSearch(self):
        """
        tests that a stage search works
        """
        self.performSearch(stage="10")
        
        term_result = self.driver.find_element_by_id("emapTermArea")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextTerms = self.getOnlyTermNames(items)
        
        # verify term that exists at 10 or beyond
        self.assertIn('allantois', searchTextTerms)
        
        # verify term that only exists at 10
        self.assertIn('amniotic fold ectoderm', searchTextTerms)
        
    def testMultipleStageSearch(self):
        """
        tests that a multiple stages search works.
        """
        self.performSearch(stage="10,11,12")
        
        term_result = self.driver.find_element_by_id("emapTermArea")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextTerms = self.getOnlyTermNames(items)
        
        # verify term that exists at one, but not all the three stages
        self.assertIn('1st branchial arch', searchTextTerms)
        
        # verify term that exists at all stages entered
        self.assertIn('amniotic cavity', searchTextTerms)

        
    def testTermShortcut(self):
        """
        tests that the shortcut ALT + c clears the term and stage fields
        """
        self.performSearch(term="brain", stage="20,21,22")
        
        term_result = self.driver.find_element_by_id("termResultList")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)
        
        self.assertIn('brain TS17-28', searchTextItems)
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.text
        self.assertIn("brain", searchbox.get_attribute("value"))
        searchbox.send_keys(Keys.ALT + "c")
        self.assertIn("", searchbox.get_attribute("value"))
        
    def testComboTermStageSearch(self):
        """
        tests that a combined search of term and stage works; also includes wild cards; jlewis
        """
        self.performSearch(term="%renal artery%", stage="27")
        
        term_result = self.driver.find_element_by_id("termResultList")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)
        
        self.assertIn('endothelium of renal artery TS21-28', searchTextItems)
        
    def testSpecialCharSearch(self):
        """
        tests that a term with a special character works; jlewis
        """
        self.performSearch(term="rathke's pouch")
        
        term_result = self.driver.find_element_by_id("emapTermArea")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)
        
        self.assertIn("Rathke's pouch TS14-19", searchTextItems)        
        

    def testMultipleTermSearch(self):
        """
        tests that a search with multiple terms works; semi-colon is the delimiter; jlewis
        """
        self.performSearch(term="liver; brain; heart")
        
        term_result = self.driver.find_element_by_id("termResultList")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextTerms = self.getOnlyTermNames(items)
        
        self.assertIn('brain', searchTextTerms)
        self.assertIn('heart', searchTextTerms)
        self.assertIn('liver', searchTextTerms)
        
    def testStageRangeSearch(self):
        """
        tests that a search for a range of stages works; jlewis
        """
        self.performSearch(stage="1-3")
        
        term_result = self.driver.find_element_by_id("emapTermArea")
        items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        searchTextTerms = self.getOnlyTermNames(items)
        
        # verify term that exists only at stage 1
        self.assertIn('first polar body', searchTextTerms)
        
        # verify term that only exists at stage 2
        self.assertIn('2-cell stage conceptus', searchTextTerms)
        
        # verify term that only exists at stage 3
        self.assertIn('8-cell stage embryo', searchTextTerms)
        
    
    def getOnlyTermNames(self, elements):
        """
        Returns text strings from each element,
            but only includes the term name, not the TS range or synonyms
        """
        
        terms = []
        for element in elements:
            # term is the first section before TS range
            term = element.text.split(" TS")[0]
            terms.append(term)
            
        return terms
        
        
            
    def tearDown(self):
        self.closeAllWindows()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSearch))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()