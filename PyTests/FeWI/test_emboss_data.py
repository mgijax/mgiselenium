'''
Created on Feb 22, 2016

@author: jeffc
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ddt import ddt, data, unpack, file_data
from pkgutil import get_data

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
    @ddt
    def hide_private_allele(self):
        driver = self.driver
        driver.get("http://www.informatics.jax.org/sequence/")
        self.assertIn("Sequence Detail", driver.title)
        @file_data("embossdata.txt")
        def test_file_embossdata(self, "value"):
        
        def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()