'''
Created on Jul 27, 2017
These tests are to confirm results you get back using various result requirements
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
from util.form import ModuleForm
from util.table import Table

class TestTermEndpointAPI(unittest.TestCase):


    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        #self.driver.get('http://scrumdogdev.informatics.jax.org/allele')
        self.driver.implicitly_wait(10)


    def test_get_term(self):
        
        self.driver.get(config.TEST_API_URL + "/term/847165")
        
        jsonData = iterate.getJsonData(self.driver)

        term_key=jsonData["_term_key"]
        
        print jsonData
        
        self.assertEqual(term_key,847165)