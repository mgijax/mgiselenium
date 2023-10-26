'''
Created on May 6, 2019
Tests the GXD RNASeq summary page
@author: jeffc
Verify the array express link on the RNA-Seq summary results page is correct
Verify the expression atlas link on the RNA-Seq summary results page is correct
Verify the geo link on the RNA-Seq summary results page is correct
Verify the filtering by a single variable on the RNA-Seq summary results page
Verify the filtering by multiple variables on the RNA-Seq summary  results page
Verify the filtering by a single study type on the RNA-Seq summary results page
Verify the sort order on the RNA-Seq summary results page for the View Experiment at column is correct
Verify the gxd link on the RNA-Seq summary results page is correct
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
class TestGxdRnaSeqSummary(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
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
        self.driver.find_element(By.ID, 'submit1').click()
        #identify the View experiment at cell of the first row of results returned
        result_set = self.driver.find_element(By.ID, "injectedResults").find_elements(By.CLASS_NAME, 'extUrl')
        print(result_set[3].text)
        result_set[3].click()
        time.sleep(2)
        #switch focus to the next tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #get the URL of the page
        page_url = self.driver.current_url
        print(page_url)
        #Assert the URL is correct
        self.assertEqual(page_url, "https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-GEOD-868")
     
    def test_rnaseq_summary_exp_atlas_link(self):
        '''
        @status this test verifies the expression atlas link on the RNA-Seq summary results page is correct.
        @see GXD-RNASeq-summary-6
        '''
        print ("BEGIN test_rnaseq_summary_exp_atlas_link")
        #finds the strain field and enters text
        self.driver.find_element(By.ID, 'strainNameAC').send_keys('C57BL/6J')
        #find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        #identify the View experiment at cell of the first row of results returned
        self.driver.find_element(By.CSS_SELECTOR, "#viewData0 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)").click()
        time.sleep(2)
        #switch focus to the next tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #get the URL of the page
        page_url = self.driver.current_url
        print(page_url)
        #Assert the URL is correct
        self.assertEqual(page_url, 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE30')
        
    def test_rnaseq_summary_geo_link(self):
        '''
        @status this test verifies the geo link on the RNA-Seq summary results page is correct.
        @see GXD-RNASeq-summary-7
        '''
        print ("BEGIN test_rnaseq_summary_geo_link")
        #finds the strain field and enters text
        self.driver.find_element(By.ID, 'strainNameAC').send_keys('C57BL/6J')
        #find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        #identify the View experiment at cell of the third row of results returned
        self.driver.find_element(By.CSS_SELECTOR, "#viewData1 > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > a:nth-child(1)").click()
        time.sleep(2)
        #switch focus to the next tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #get the URL of the page
        page_url = self.driver.current_url
        print(page_url)
        #Assert the URL is correct
        self.assertEqual(page_url, "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE868")
                    
    def test_rnaseq_summary_single_var_filter(self):
        '''
        @status this test verifies the filtering by a single variable on the RNA-Seq summary results page.
        @see GXD-RNASeq-summary-8
        '''
        print ("BEGIN test_rnaseq_summary_single_var_filter")
        Select(self.driver.find_element(By.ID, 'age')).deselect_by_value('ANY')#deselect the default option
        Select(self.driver.find_element(By.ID, 'age')).select_by_value('4')#finds the age list and select the E4.0 option
        #find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        #Find the Variable filter button and click it
        self.driver.find_element(By.ID, "variableFilter").click()
        #Find the Variable filter list of options. then select the option "genotype"
        self.driver.find_elements(By.NAME, 'variableFilter')[2].click()
        #find the Filter button and click it
        self.driver.find_element(By.ID, 'yui-gen0-button').click()
        #identify the Experimental variable row of the results returned
        result_set = self.driver.find_element(By.ID, "injectedResults").find_elements(By.CLASS_NAME, 'variables')
        print(result_set[0].text)
        #Assert the lone result has an Experimental variable of 'genotype'
        self.assertEqual(result_set[0].text, "developmental stage\ngenotype")
        
    def test_rnaseq_summary_multi_var_filter(self):
        '''
        @status this test verifies the filtering by multiple variables on the RNA-Seq summary  results page.
        @see GXD-RNASeq-summary-9 
        '''
        print ("BEGIN test_rnaseq_summary_multi_var_filter")
        Select(self.driver.find_element(By.ID, 'age')).deselect_by_value('ANY')#deselect the default option
        Select(self.driver.find_element(By.ID, 'age')).select_by_value('4.5')#finds the age list and select the E4.5 option
        #find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        #Find the Variable filer button and click it
        self.driver.find_element(By.ID, "variableFilter").click()
        #Find the Variable filter list of options. then select the options "genotype and single cell variation"
        self.driver.find_elements(By.NAME, 'variableFilter')[3].click()
        self.driver.find_elements(By.NAME, 'variableFilter')[4].click()
        #find the Filter button and click it
        self.driver.find_element(By.ID, 'yui-gen0-button').click()
        #identify the Experimental variables cell of row2 of the results returned
        result_set1 = self.driver.find_element(By.ID, "variableData1").find_element(By.CLASS_NAME, 'variables')
        print(result_set1.text)
        #Assert the result has an Experimental variables of 'developmental stage and genotype'
        self.assertEqual(result_set1.text, "developmental stage\ngenotype")        
        #identify the Experimental variable cell of row9 of the results returned
        result_set8 = self.driver.find_element(By.ID, "variableData8").find_element(By.CLASS_NAME, 'variables')
        print(result_set8.text)
        #Assert the result has an Experimental variable of 'anatomical structure, developmental stage, genotype, single cell variation'
        self.assertEqual(result_set8.text, "cell type\ndevelopmental stage\ngenotype\nsingle cell variation")
        
    def test_rnaseq_summary_study_filter(self):
        '''
        @status this test verifies the filtering by a single study type on the RNA-Seq summary results page.
        @see GXD-RNASeq-summary-10 
        '''
        print ("BEGIN test_rnaseq_summary_study_filter")
        Select(self.driver.find_element(By.ID, 'age')).deselect_by_value('ANY')#deselect the default option
        Select(self.driver.find_element(By.ID, 'age')).select_by_value('4')#finds the age list and select the E4.0 option
        #find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        #Find the Variable filter button and click it
        self.driver.find_element(By.ID, "studyTypeFilter").click()
        #Find the Study type filter list of options. then select the option "WT vs. Mutant"
        self.driver.find_elements(By.NAME, 'studyTypeFilter')[1].click()
        #find the Filter button and click it
        self.driver.find_element(By.ID, 'yui-gen0-button').click()
        #identify the Experimental variable column of the results returned
        result_set = self.driver.find_element(By.ID, "studyTypeData0")
        print(result_set.text)
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
        self.driver.find_element(By.ID, 'submit1').click()
        #identify the View experiment at cell of the third row of results returned
        result_set = self.driver.find_element(By.ID, "injectedResults").find_element(By.ID, 'viewData0')
        print(result_set.text)
        #Assert the sort order is correct
        self.assertEqual(result_set.text, "GEO: GSE30")

    def test_rnaseq_summary_gxd_link(self):
        '''
        @status this test verifies the gxd link on the RNA-Seq summary results page is correct.
        @see GXD-RNASeq-summary-14 
        '''
        print ("BEGIN test_rnaseq_summary_gxd_link")
        #finds the strain field and enters text
        self.driver.find_element(By.ID, 'strainNameAC').send_keys('C57BL/6J')
        #find the ArrayExpress or GEO ID field and enters text
        self.driver.find_element(By.ID, 'arrayExpressID').send_keys('E-ERAD-169')
        #find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        #Find the first E-ERAD--169 found in the first row of the View Experiment at column and click it.
        vea_links = self.driver.find_elements(By.LINK_TEXT, 'E-ERAD-169')
        print(vea_links[0].text)
        vea_links[0].click()
        #switch focus to the next tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #get the URL of the page
        page_url = self.driver.current_url
        print(page_url)
        #Assert the URL is correct
        self.assertEqual(page_url, "http://scrum.informatics.jax.org/gxd/experiment/E-ERAD-169")

  
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxdRnaSeqSummary))
    return suite 
       
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))