'''
Created on Feb 14, 2017
Test to try and get post feature to work with selenium-requests
@author: jeffc
'''
import unittest
import time
import requests
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
#Tests
tracemalloc.start()
class TestDoPostTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)
        
    def test_post_request(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by multiple Gene symbols (Foxm1, Lep, Ins2). There are 2 issues with this test, first selenium seems unable to locate the last 4 diseases in the grid so
        they have been commented out. The order of genes on the genes tab has Human symbols first, should be Mouse symbol first.
        @warning: This is not a complete test, just shows how to use a POST right now.
        '''
        #my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        #for option in my_select.find_elements(By.TAG_NAME, "option"):
            #if option.text == 'Gene Symbol(s) or ID(s)':
                #option.click()
                #break
            
        ##self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys('Foxm1, Lep, Ins2')#identifies the input field and enters gata1
        #wait.forAngular(self.driver)
        #self.driver.find_element(By.ID, "searchButton").click()
        #wait.forAngular(self.driver)
        #r = requests.post
        #identify the Genes tab and verify the tab's text
        #grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        #self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (9 x 32)", "Grid tab is not visible!")
        #grid_tab.click()
        #driver.get("http://www.google.com")
        #field = ()
        #condition = ()
        #parameters = ()
        #input = ()
        payload = {"operator":"AND","queries":[{"field":"mnS","condition":{"parameters":[],"input":"gata1"}}]}
        diseaseresult = requests.post('http://www.informatics.jax.org/diseasePortal/gridQuery', json=payload)
        #print(diseaseresult.json())
        data = diseaseresult.json()
        print(data['gridDiseaseHeaders'])
        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDoPostTest))
    return suite
       
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))