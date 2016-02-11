'''
Created on Jan 28, 2016
This test verifies searching within the EmapA module
@author: jeffc
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class searchTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://scrumdog.informatics.jax.org/pwi/edit/emapBrowser")
        self.driver.implicitly_wait(10)

    def testSearch(self):#tests that a basic term search works
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("brain")
        searchbox.send_keys(Keys.RETURN)
        term_result = self.driver.find_element_by_id("emapTermArea")
        assert term_result.text() == 'brain TS17-28'
        
    def testSynonymSearch(self):#tests that a synonym term search works
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("myocardium")
        searchbox.send_keys(Keys.RETURN)
        #assert "cardiac muscle tissue TS12-28" in self.driver.find_element_by_id("emapTermArea").text()        

    def testWildcardSearch(self):#tests that a wildcard term search works
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("%tectum")
        searchbox.send_keys(Keys.RETURN)
        assert "pretectum TS22-28 tectum TS22-28" in self.driver.find_element_by_id("emapTermArea").text
        
    def testtermwithcommaSearch(self):#tests that a term with a comma search works
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("female,%")
        searchbox.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_id("emapTermArea")
        #assert result.text == 
            
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()