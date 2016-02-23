'''
Created on Jan 4, 2016

@author: jeffc
'''
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GxdTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_gxd_Name(self):
        driver = self.driver
        driver.get("http://www.informatics.jax.org/gxd")
        self.assertIn("Mouse Gene Expression", driver.title, "page not found")



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
