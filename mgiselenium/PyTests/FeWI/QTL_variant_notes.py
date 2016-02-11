'''
Created on Feb 10, 2016

@author: jeffc
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://firien.informatics.jax.org/allele/")
        self.driver.implicitly_wait(10)

    def testVariant_note(self):
        self.driver.find_element_by_id("phenotype").clear()
        self.driver.find_element_by_id("phenotype").send_keys("Adre")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_css_selector("#yui-rec0 > td.yui-dt0-col-nomen.yui-dt-col-nomen.yui-dt-sortable.yui-dt-first > div > a > sup").click()
        assert "B6.C-H21<sup>c</sup>/ByJ" in self.driver.page_source()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()