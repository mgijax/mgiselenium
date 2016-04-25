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


    def verify_default_sort_treeview(self):
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
        
if __name__ == "__main__":
    unittest.main() 
    
