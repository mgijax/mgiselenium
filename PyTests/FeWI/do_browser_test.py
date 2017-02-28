'''
Created on Feb 14, 2017
Test to try and get post feature to work with selenium-requests
@author: jeffc
'''
import unittest
import time
#from seleniumrequests import Firefox
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import HTMLTestRunner
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    
class TestDoBrowserTest(unittest.TestCase):
    caps = DesiredCapabilities.FIREFOX
    caps["marionette"] = True
    driver = webdriver.Firefox(capabilities=caps, executable_path="/Users/jeffc/eclipse/geckodriver")
    driver.get("http://www.google.com")
    field = ()
    condition = ()
    parameters = ()
    input = ()
    #diseaseresult = webdriver.request('POST', 'http://www.informatics.jax.org/diseasePortal/gridQuery', data={"field": "miS", "condition": {"parameters": [], "input": "pax6"}})
    #print(diseaseresult)
    
    
    def tearDown(self):
        self.driver.quit()
       
        '''
        These tests should NEVER!!!! be run against a production system!!
        def suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(TestAdd))
        return suite
        '''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main() 