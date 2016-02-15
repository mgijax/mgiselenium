'''
Created on Feb 15, 2016

@author: jeffc
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://scrumdog.informatics.jax.org/pwi/edit/emapBrowser")
        self.driver.implicitly_wait(1)

    def testDefaultDetail(self):
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("%cort%")
        searchbox.send_keys(Keys.RETURN)
        self.assertEqual(self.driver.find_element_by_id("termDetailContent").find_element_by_tag_name("li").text(), "adrenal cortex")
        term_result = self.driver.find_element_by_id("termResultList")
        items = term_result.find_elements_by_tag_name("li")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()