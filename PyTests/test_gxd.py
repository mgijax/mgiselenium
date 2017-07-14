'''
Created on Jan 4, 2016

@author: jeffc
'''
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config

'''
@Attention: This file does not have tests yet. Need to add them
'''

class GxdTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_gxd_Name(self):
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        self.assertIn("Mouse Gene Expression", driver.title, "page not found")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
