'''
Created on Apr 6, 2018

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

class TestHPOBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() 

    def test_parent_data(self):
        """
        @status: Tests that the parent terms are correctly identified
        In this case parent term should be is-a
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/hp_ontology/HP:0000118")
        time.sleep(1)
        #identifies the table tags that  contain  parent terms
        parent = driver.find_element(By.ID, 'termPaneDetails').find_elements(By.TAG_NAME, 'td')
        print [x.text for x in parent]
        
        # verifies that the returned part terms are correct
        #self.assertEqual(parent[3].text, "is-a All")
        
        
    def test_default_sort_treeview(self):
        """
        @status: Tests that the terms are correctly sorted
        The default sort for the tree view is smart alpha
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/hp_ontology/HP:0001425")
        time.sleep(2)
        termList = driver.find_elements(By.CLASS_NAME, 'jstree-anchor')
        terms = iterate.getTextAsList(termList)
        print [x.text for x in termList]
        
        # Heterogeneous should not be before the 10th item in the list
        self.assertGreater(terms.index('Heterogeneous'), 10)
 
    def test_term_w_ofthe(self):
        """
        @status: Tests that searching by an HP term that has 'of the' in the name correctly returns results
        @note: 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/hp_ontology/")
        searchbox = driver.find_element(By.ID, 'searchTerm')
        # put your HPO search term in the search box
        searchbox.send_keys("Abnormality of the ear")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        searchList = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchList)
        print [x.text for x in searchList]
        
        # This term should be returned in the HPO search results
        self.assertIn('Abnormality of the ear', terms)        
        
    def tearDown(self):
        pass
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHPOBrowser))
    return suite
        
if __name__ == "__main__":
    unittest.main() 
    