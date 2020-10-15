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
import HtmlTestRunner
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

class TestGxdRnaSeqSummary(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1080,800)
        self.driver.get(config.TEST_URL + "/gxd/htexp_index")
        self.driver.implicitly_wait(10)

    def test_rnaseq_summary_array_express_link(self):
        '''
        @status this test verifies the array express link on the RNA-Seq summary results page is correct.
        @see GXD-RNASeq-summary-5
        '''
        print ("BEGIN test_rnaseq_summary_array_express_link")
        #finds the strain field and enters text
        self.driver.find_element(By.ID, 'strainNameAC').send_keys('C57BL/6J')
        #find the Search button and click it
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        #identify the View experiment at cell of the first row of results returned
        result_set = self.driver.find_element_by_id("injectedResults").find_elements_by_class_name('extUrl')
        print(result_set[2].text)
        time.sleep(2)
        result_set[2].click()
        time.sleep(2)
        #switch focus to the next tab
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #get the URL of the page
        page_url = self.driver.current_url
        print(page_url)
        #Assert the URL is correct
        self.assertEqual(page_url, "https://www.ebi.ac.uk/arrayexpress/experiments/E-ERAD-433/")
     
    def test_rnaseq_summary_exp_atlas_link(self):
        '''
        @status this test verifies the expression atlas link on the RNA-Seq summary results page is correct.
        @see GXD-RNASeq-summary-6
        '''
        print ("BEGIN test_rnaseq_summary_exp_atlas_link")
        #finds the strain field and enters text
        self.driver.find_element(By.ID, 'strainNameAC').send_keys('C57BL/6J')
        #find the Search button and click it
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        #identify the View experiment at cell of the first row of results returned
        result_set = self.driver.find_element_by_id("injectedResults").find_elements_by_class_name('extUrl')
        print(result_set[0].text)
        time.sleep(2)
        result_set[0].click()
        time.sleep(2)
        #switch focus to the next tab
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #get the URL of the page
        page_url = self.driver.current_url
        print(page_url)
        #Assert the URL is correct
        self.assertEqual(page_url, "https://www.ebi.ac.uk/gxa/experiments/E-ERAD-169/Results")

    def test_rnaseq_summary_geo_link(self):
        '''
        @status this test verifies the geo link on the RNA-Seq summary results page is correct.
        @see GXD-RNASeq-summary-7
        '''
        print ("BEGIN test_rnaseq_summary_geo_link")
        #finds the strain field and enters text
        self.driver.find_element(By.ID, 'strainNameAC').send_keys('C57BL/6J')
        #find the Search button and click it
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        #identify the View experiment at cell of the third row of results returned
        result_set = self.driver.find_element_by_id("injectedResults").find_elements_by_class_name('extUrl')
        print(result_set[4].text)
        time.sleep(2)
        result_set[4].click()
        time.sleep(2)
        #switch focus to the next tab
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #get the URL of the page
        page_url = self.driver.current_url
        print(page_url)
        #Assert the URL is correct
        self.assertEqual(page_url, "https://www.ebi.ac.uk/arrayexpress/experiments/E-GEOD-868/")
                    
    def test_rnaseq_summary_single_var_filter(self):
        '''
        @status this test verifies the filtering by a single variable on the RNA-Seq summary results page.
        @see GXD-RNASeq-summary-8 !!!broken, will not click variable filter!!!
        '''
        print ("BEGIN test_rnaseq_summary_single_var_filter")
        Select(self.driver.find_element(By.ID, 'age')).deselect_by_value('ANY')#deselect the default option
        Select(self.driver.find_element(By.ID, 'age')).select_by_value('4')#finds the age list and select the E4.0 option
        #find the Search button and click it
        self.driver.find_element_by_id('submit1').click()
        #time.sleep(2)
        #Find the Variable filter button and click it
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
        print(result_set[0].text)
        time.sleep(2)
        #Assert the lone result has an Experimental variable of 'genotype'
        self.assertEqual(result_set[0].text, "developmental stage\ngenotype")
        
    def test_rnaseq_summary_multi_var_filter(self):
        '''
        @status this test verifies the filtering by multiple variables on the RNA-Seq summary  results page.
        @see GXD-RNASeq-summary-9 !!!broken, will not click variable filter!!!
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
        print(result_set0.text)
        #print result_set[1].text
        time.sleep(2)
        #Assert the lone result has an Experimental variable of 'genotype'
        self.assertEqual(result_set0.text, "developmental stage\ngenotype")        
        #identify the Experimental variable cell of row2 of the results returned
        result_set1 = self.driver.find_element_by_id("variableData2").find_element_by_class_name('variables')
        print(result_set1.text)
        #print result_set[1].text
        time.sleep(2)
        #Assert the lone result has an Experimental variable of 'genotype'
        self.assertEqual(result_set1.text, "anatomical structure\ndevelopmental stage\ngenotype\nsingle cell variation")        
        
    def test_rnaseq_summary_study_filter(self):
        '''
        @status this test verifies the filtering by a single study type on the RNA-Seq summary results page.
        @see GXD-RNASeq-summary-10 !!!broken, will not click study filter!!!
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
        print(result_set.text)
        time.sleep(2)
        #Assert the lone result has a study type of 'WT vs. Mutant'
        self.assertEqual(result_set.text, "WT vs. Mutant")        

    def test_rnaseq_summary_vea_sort_order(self):
        '''
        @status this test verifies the sort order on the RNA-Seq summary results page for the View Experiment at column is correct.
        @see GXD-RNASeq-summary-13 
        '''
        print ("BEGIN test_rnaseq_summary_vea_sort_order")
        #finds the strain field and enters text
        self.driver.find_element(By.ID, 'strainNameAC').send_keys('C57BL/6J')
        #find the Search button and click it
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        #identify the View experiment at cell of the third row of results returned
        result_set = self.driver.find_element_by_id("injectedResults").find_element_by_id('viewData0')
        print(result_set.text)
        time.sleep(2)
        #Assert the sort order is correct
        self.assertEqual(result_set.text, "GXD: E-ERAD-169\nExpression Atlas: E-ERAD-169\nArrayExpress: E-ERAD-169")

    def test_rnaseq_summary_gxd_link(self):
        '''
        @status this test verifies the gxd link on the RNA-Seq summary results page is correct.
        @see GXD-RNASeq-summary-14 
        @note: this test will fail unless ran against Test due to assert asked for.
        '''
        print ("BEGIN test_rnaseq_summary_gxd_link")
        #finds the strain field and enters text
        self.driver.find_element(By.ID, 'strainNameAC').send_keys('C57BL/6J')
        #find the Search button and click it
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        #Find the first E-ERAD--169 found in the first row of the View Experiment at column and click it.
        vea_links = self.driver.find_elements_by_link_text('E-ERAD-169')
        print(vea_links[0])
        vea_links[0].click()
        time.sleep(2)
        #switch focus to the next tab
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #get the URL of the page
        page_url = self.driver.current_url
        print(page_url)
        #Assert the URL is correct
        self.assertEqual(page_url, "http://test.informatics.jax.org/gxd/experiment/E-ERAD-169")

  
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxdRnaSeqSummary))
    return suite 
       
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))