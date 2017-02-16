'''
Created on Dec 2, 2016
This set of tests is for the disease auto complete list 
@author: jeffc
'''
import unittest
import time
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



# Tests

class TestHMDCAutocomplete(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)
        
    def test_index_tab_headers(self):
        '''
        @status this test verifies the auto complete list is displaying the terms associated to the text you entered.
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Phenotype or Disease Name':
                option.click()
                break
        
        self.driver.find_element_by_id("formly_3_autocomplete_input_0").send_keys("systemic lupus")#identifies the input field and enters systemic lupus
        wait.forAngular(self.driver)
        #identify the autocomplete dropdown list
        auto_list = self.driver.find_element_by_class_name("dropdown-menu")
        items = auto_list.find_elements_by_tag_name("li")
        for item in items:
            text = item.text
            print text
        self.assertEqual(items[0].text, "systemic lupus", "Term 0 is not visible!")
        self.assertEqual(items[1].text, "systemic lupus erythematosus", "Term 1 is not visible!")
        self.assertEqual(items[2].text, "Lupus Erythematosus, systemic", "Term 2 is not visible!")
        self.assertEqual(items[3].text, "SLE - Lupus Erythematosus, systemic", "Term 3 is not visible!")
        self.assertEqual(items[4].text, "decreased susceptibility to systemic lupus erythematosus", "Term 4 is not visible!")
        self.assertEqual(items[5].text, "increased resistance to systemic lupus erythematosus", "Term 5 is not visible!")
        self.assertEqual(items[6].text, "increased susceptibility to systemic lupus erythematosus", "Term 6 is not visible!")                                                                                                                                 
        self.assertEqual(items[7].text, "reduced susceptibility to systemic lupus erythematosus", "Term 7 is not visible!")
        self.assertEqual(items[8].text, "decreased resistance to systemic lupus erythematosus", "Term 8 is not visible!")
        
    def tearDown(self):
        self.driver.close()
       
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