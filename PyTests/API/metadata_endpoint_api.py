'''
Created on Feb 12, 2018
These tests are to confirm results you get back from swagger/java api using various result requirements for meta data
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


    def test_get_metadata(self):
        '''
        @note under construction
        '''
        self.driver.get(config.TEST_API_URL + "/metadata")
        
        jsonData = iterate.getJsonData(self.driver)

        db_name=jsonData["database_name"]
        
        print jsonData
        
        self.assertEqual(db_name,"scrumdog")