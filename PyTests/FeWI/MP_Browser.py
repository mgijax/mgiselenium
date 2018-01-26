'''
Created on Dec 7, 2017

@author: jeffc
'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from util import iterate
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../',)
)
import config

class TestMPBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() 

    def test_parent_data(self):
        """
        @status: Tests that the parent terms are correctly identified
        In this case parent term should be is-a
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/mp_ontology/MP:0005375")
        time.sleep(1)
        #identifies the table tags that  contain  parent terms
        parent = driver.find_element(By.ID, 'termPaneDetails').find_elements(By.TAG_NAME, 'td')
        print [x.text for x in parent]
        
        # verifies that the returned part terms are correct
        self.assertEqual(parent[2].text, "is-a mammalian phenotype")
        
        
    def test_default_sort_treeview(self):
        """
        @status: Tests that the terms are correctly sorted
        The default sort for the tree view is smart alpha
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/mp_ontology/MP:0011614")
        time.sleep(2)
        termList = driver.find_elements(By.CLASS_NAME, 'jstree-anchor')
        terms = iterate.getTextAsList(termList)
        print [x.text for x in termList]
        
        # slow aging should not be before the 18th item in the list
        self.assertGreater(terms.index('slow aging'), 18)
        
    def test_tissue_link_multi(self):
        """
        @status: Tests that searching by an MP ID that is associated with multiple expressions return the correct results/link
        @note: MP-ID-Search-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/mp_ontology/MP:0002633")
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, 'tissues').click()
        time.sleep(2)
        searchList = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchList)
        print [x.text for x in searchList]
        
        # These 2 terms should be returned in the anatomy search results
        self.assertIn('aorta TS23-28\npulmonary artery TS17-28', terms, 'these terms are not listed!')
        
 
    def test_tissue_link_single(self):
        """
        @status: Tests that searching by an MP ID that is associated with a single expression returns the correct results/link
        @note: MP-ID-Search-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/mp_ontology/MP:0014185")
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, 'tissues').click()
        searchList = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchList)
        print [x.text for x in searchList]
        time.sleep(2)
        # This 1 term should be returned in the anatomy search results
        self.assertIn('cerebellum TS21-28', terms, 'this term is not listed!')
        
    def test_tissue_link_nophenotype(self):
        """
        @status: Tests that searching by an MP term that is associated to an expression but has no phenotype annotations
        @note: MP-ID_Seach-4
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/mp_ontology/MP:0030355")
        driver.find_element(By.LINK_TEXT, 'tissues').click()
        time.sleep(2)
        searchList = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchList)
        print [x.text for x in searchList]
        
        # This term should be returned in the anatomy search results
        self.assertIn('lambdoidal suture TS25-28', terms, 'this term is not listed!')
        
    def test_tissue_link_results_sort(self):
        """
        @status: Tests that searching by an MP ID that is associated with multiple expressions return the correct results in alphanumeric sort order
        @note: MP-ID-Search-5
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/mp_ontology/MP:0012260")
        driver.find_element(By.LINK_TEXT, 'tissues').click()
        time.sleep(2)
        searchList = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchList)
        print [x.text for x in searchList]
        
        # These 2 terms should be returned in the anatomy search results
        self.assertIn('brain TS17-28\ncranium TS20-28\ntissue TS11-28', terms, 'these terms are not listed!')        
        
    def tearDown(self):
        pass
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMPBrowser))
    return suite
        
if __name__ == "__main__":
    unittest.main() 
    