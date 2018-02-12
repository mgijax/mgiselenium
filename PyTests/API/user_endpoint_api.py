'''
Created on Feb 12, 2018
These tests are to confirm results you get back from swagger/java api using various result requirements for user
@author: jeffc
'''
import unittest
import json
from selenium import webdriver
import sys,os.path
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)

import config
from util import iterate

class TestTermEndpointAPI(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)


    def test_get_user(self):
        '''
        @note under construction
        '''
        self.driver.get(config.TEST_API_URL + "/user/?????")
        
        jsonData = iterate.getJsonData(self.driver)

        term_key=jsonData["_term_key"]
        
        print jsonData
        
        self.assertEqual(term_key,847165)