'''
Created on Jan 28, 2016

@author: jeffc
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class modifyemapaTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get()

    def testName(self):
        pass

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()