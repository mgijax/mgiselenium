'''
Created on Jan 4, 2016

@author: jeffc
'''
import unittest
import tracemalloc
from jd_HTMLTestRunner import HTMLTestRunner
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

#Tests
tracemalloc.start()
class TestGxd(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_gxd_Name(self):
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        self.assertIn("Mouse Gene Expression", driver.title, "page not found")

    def tearDown(self):
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxd))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
