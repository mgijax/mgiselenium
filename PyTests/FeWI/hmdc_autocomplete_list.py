'''
Created on Dec 2, 2016
This set of tests is for the disease auto complete list 
@author: jeffc
Verify the auto complete list is displaying the terms associated to the text you entered
'''
import unittest
import time
import tracemalloc
import config
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from lib import *
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests
tracemalloc.start()
class TestHmdcAutocomplete(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)
        
    def test_index_tab_headers(self):
        '''
        @status this test verifies the auto complete list is displaying the terms associated to the text you entered.
        @see HMDC-DQ-?? passed 4-15-2020
        '''
        print ("BEGIN test_index_tab_headers")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element(By.ID, "formly_3_autocomplete_input_0").send_keys("systemic lupus")#identifies the input field and enters systemic lupus
        wait.forAngular(self.driver)
        #identify the autocomplete dropdown list
        auto_list = self.driver.find_element(By.CLASS_NAME, "dropdown-menu")
        items = auto_list.find_elements(By.TAG_NAME, "li")
        for item in items:
            text = item.text
            print(text)
        self.assertEqual(items[0].text, "systemic lupus", "Term 0 is not visible!")
        self.assertEqual(items[1].text, "systemic lupus erythematosus", "Term 1 is not visible!")
        self.assertEqual(items[2].text, "Lupus Erythematosus, systemic", "Term 2 is not visible!")
        self.assertEqual(items[3].text, "SLE - Lupus Erythematosus, systemic", "Term 3 is not visible!")
        self.assertEqual(items[4].text, "increased susceptibility to systemic lupus erythematosus", "Term 4 is not visible!")
        self.assertEqual(items[5].text, "decreased susceptibility to systemic lupus erythematosus", "Term 5 is not visible!")
        self.assertEqual(items[6].text, "decreased resistance to systemic lupus erythematosus", "Term 6 is not visible!")                        
        self.assertEqual(items[7].text, "reduced susceptibility to systemic lupus erythematosus", "Term 7 is not visible!")
        self.assertEqual(items[8].text, "increased resistance to systemic lupus erythematosus", "Term 8 is not visible!")
                                                                                                                 
        
        
        
        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()
       
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHmdcAutocomplete))
    return suite 

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))