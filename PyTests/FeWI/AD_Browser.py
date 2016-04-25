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
from config import DEV_URL

class TestADBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox() 


    def verify_default_sort_treeview(self):
        """
        @status: Tests that the terms are correctly sorted
        The default sort for the tree view is smart alpha
        """
        driver = self.driver
        driver.get(config.DEV_URL + "/vocab/gxd/anatomy/EMAPA:16042")
        
        wait.forAjax(driver)
        termlist = driver.find_element_by_class("ygtvtable")
        items = termlist[17].find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(items)
        print [x.text for x in items]
        #self.assertEqual(searchTextItems, ["Gsx2", "Nkx2-1", "Pax6"])
        
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main() 
    
