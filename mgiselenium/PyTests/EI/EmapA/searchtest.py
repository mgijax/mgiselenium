'''
Created on Jan 28, 2016

@author: jeffc
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class searchTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://prodwww.informatics.jax.org/~kstone/selenium/emapa_dummy.html")

    def testSearch(self):
        searchbox = self.driver.find_element_by_id("emapaSearch")
        searchbox.send_keys("brain")
        searchbox.send_keys(Keys.RETURN)
        assert "No results found" not in self.driver.page_source
        

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()