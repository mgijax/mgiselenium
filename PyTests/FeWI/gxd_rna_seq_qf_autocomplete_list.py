'''
Created on Apr 25, 2019
This set of tests is for the Anatomical structure autocomplete list of the RNA Seq and Microarray Experiments query form
@author: jeffc
Verify the auto complete list is displaying the correct anatomical structures associated to the text you entered
Verify
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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
class TestGxdRnaSeqAutocomplete(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/gxd/htexp_index")
        self.driver.implicitly_wait(10)
        
    def test_index_structureAC_headers(self):
        '''
        @status this test verifies the auto complete list is displaying the correct anatomical structures associated to the text you entered.
        @see GXD-RNASeq-search-1
        '''
        print ("BEGIN test_structureAC_headers")
        self.driver.find_element(By.ID, 'structureAC').send_keys('heart')#identifies the anatomical structure field and enters text
        #wait.forAngular(self.driver)
        #identify the autocomplete dropdown list
        auto_list = self.driver.find_element(By.ID, "ui-id-1")
        items = auto_list.find_elements(By.TAG_NAME, "li")
        for item in items:
            text = item.text
            print(text)
        self.assertEqual(items[0].text, "heart", "Term 0 is not visible!")
        self.assertEqual(items[1].text, "heart apex", "Term 1 is not visible!")
        self.assertEqual(items[2].text, "heart atrium", "Term 2 is not visible!")
        self.assertEqual(items[3].text, "heart endothelium", "Term 3 is not visible!")
        self.assertEqual(items[4].text, "heart mesenchyme", "Term 4 is not visible!")
        self.assertEqual(items[5].text, "heart mesentery", "Term 5 is not visible!")
        self.assertEqual(items[6].text, "heart septum", "Term 6 is not visible!") 
        self.assertEqual(items[7].text, "heart trabecula", "Term 7 is not visible!")                                                                                                                                
        self.assertEqual(items[8].text, "heart valve", "Term 8 is not visible!")
        self.assertEqual(items[9].text, "heart ventricle", "Term 9 is not visible!")
    
    def tearDown(self):
        self.driver.close()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxdRnaSeqAutocomplete))
    return suite 
       
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))