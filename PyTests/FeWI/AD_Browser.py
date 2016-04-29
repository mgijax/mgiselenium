'''
Created on Apr 22, 2016

@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,os.path
from util import wait, iterate
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import PUBLIC_URL

class TestADBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox() 

    def test_parent_data(self):
        """
        @status: Tests that the parent terms are correctly identified
        In this case all 3 parent terms should be part-of
        """
        driver = self.driver
        driver.get(config.PUBLIC_URL + "/vocab/gxd/anatomy/EMAPA:16042")
        
        wait.forAjax(driver)
        time.sleep(1)
        #identifies the table tags that  contain  parent terms
        parent = driver.find_element_by_id("termPaneDetails").find_elements_by_tag_name("td")
        #print [x.text for x in parent]
        
        # verifies that the returned part terms are correct
        self.assertEqual(parent[4].text, "part-of conceptus\npart-of egg cylinder\npart-of mouse")
        
        
    def test_default_sort_treeview(self):
        """
        @status: Tests that the terms are correctly sorted
        The default sort for the tree view is smart alpha
        """
        driver = self.driver
        driver.get(config.PUBLIC_URL + "/vocab/gxd/anatomy/EMAPA:16042")
        
        wait.forAjax(driver)
        time.sleep(1)
        termList = driver.find_elements_by_class_name("ygtvlabel")
        terms = iterate.getTextAsList(termList)
        print [x.text for x in termList]
        
        # extra embryonic component should not be 2nd item in list
        self.assertGreater(terms.index('extraembryonic component'), 2)
        
        
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestADBrowser))
    return suite
        
if __name__ == "__main__":
    unittest.main() 
    
