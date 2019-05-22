'''
Created on May 6, 2019

@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import HTMLTestRunner
# from lib import *
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

class TestRnaSeqSummary(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/gxd/htexp_index")
        self.driver.implicitly_wait(10)
        
    def test_rnaseq_summary_single_var_filter(self):
        '''
        @status this test verifies the filtering by a single variable on the RNA-Seq summary  results page.
        @see GXD-RNASeq-summary-7
        '''
        print ("BEGIN test_rnaseq_summary_single_var_filter")
        Select(self.driver.find_element(By.ID, 'age')).deselect_by_value('ANY')#deselect the default option
        Select(self.driver.find_element(By.ID, 'age')).select_by_value('4')#finds the age list and select the E4.0 option
        #find the Search button and click it
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        #Find the Variable filer button and click it
        self.driver.find_element_by_id("variableFilter").click()
        time.sleep(2)
        #Find the Variable filter list of options. then select the option "genotype"
        self.driver.find_elements_by_name('variableFilter')[2].click()
        time.sleep(2)
        #find the Filter button and click it
        self.driver.find_element_by_id('yui-gen0-button').click()
        time.sleep(2)
        #identify the Experimental variable row of the results returned
        result_set = self.driver.find_element_by_id("injectedResults").find_elements_by_class_name('variables')
        print result_set[0].text
        time.sleep(2)
        #Assert the lone result has an Experimental variable of 'genotype'
        self.assertEqual(result_set[0].text, "developmental stage\ngenotype")
        
    def test_rnaseq_summary_multi_var_filter(self):
        '''
        @status this test verifies the filtering by multiple variables on the RNA-Seq summary  results page.
        @see GXD-RNASeq-summary-8
        '''
        print ("BEGIN test_rnaseq_summary_multi_var_filter")
        Select(self.driver.find_element(By.ID, 'age')).deselect_by_value('ANY')#deselect the default option
        Select(self.driver.find_element(By.ID, 'age')).select_by_value('4.5')#finds the age list and select the E4.5 option
        #find the Search button and click it
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        #Find the Variable filer button and click it
        self.driver.find_element_by_id("variableFilter").click()
        time.sleep(2)
        #Find the Variable filter list of options. then select the options "genotype and single cell variation"
        self.driver.find_elements_by_name('variableFilter')[2].click()
        self.driver.find_elements_by_name('variableFilter')[3].click()
        time.sleep(2)
        #find the Filter button and click it
        self.driver.find_element_by_id('yui-gen0-button').click()
        time.sleep(2)
        #identify the Experimental variable cell of row1 of the results returned
        result_set0 = self.driver.find_element_by_id("variableData0").find_element_by_class_name('variables')
        print result_set0.text
        #print result_set[1].text
        time.sleep(2)
        #Assert the lone result has an Experimental variable of 'genotype'
        self.assertEqual(result_set0.text, "developmental stage\ngenotype")        
        #identify the Experimental variable cell of row2 of the results returned
        result_set1 = self.driver.find_element_by_id("variableData2").find_element_by_class_name('variables')
        print result_set1.text
        #print result_set[1].text
        time.sleep(2)
        #Assert the lone result has an Experimental variable of 'genotype'
        self.assertEqual(result_set1.text, "anatomical structure\ndevelopmental stage\ngenotype\nsingle cell variation")        
        
    def test_rnaseq_summary_study_filter(self):
        '''
        @status this test verifies the filtering by a single study type on the RNA-Seq summary results page.
        @see GXD-RNASeq-summary-9
        '''
        print ("BEGIN test_rnaseq_summary_study_filter")
        Select(self.driver.find_element(By.ID, 'age')).deselect_by_value('ANY')#deselect the default option
        Select(self.driver.find_element(By.ID, 'age')).select_by_value('4')#finds the age list and select the E4.0 option
        #find the Search button and click it
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        #Find the Variable filter button and click it
        self.driver.find_element_by_id("studyTypeFilter").click()
        time.sleep(2)
        #Find the Study type filter list of options. then select the option "WT vs. Mutant"
        self.driver.find_elements_by_name('studyTypeFilter')[1].click()
        time.sleep(2)
        #find the Filter button and click it
        self.driver.find_element_by_id('yui-gen0-button').click()
        time.sleep(2)
        #identify the Experimental variable column of the results returned
        result_set = self.driver.find_element_by_id("studyTypeData0")
        print result_set.text
        time.sleep(2)
        #Assert the lone result has a study type of 'WT vs. Mutant'
        self.assertEqual(result_set.text, "WT vs. Mutant")        
    
    
    def tearDown(self):
        self.driver.close()
       
        
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main() 