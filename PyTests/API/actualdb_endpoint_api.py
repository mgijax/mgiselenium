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

class TestActualDBEndpointAPI(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        #self.driver.get('http://scrumdogdev.informatics.jax.org/allele')
        self.driver.implicitly_wait(10)
