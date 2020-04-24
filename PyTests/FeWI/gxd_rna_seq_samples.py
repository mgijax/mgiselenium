'''
Created on Sep 30, 2019
Tests for the RNA-Seq Samples page
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

class TestGxdRnaSeqSamples(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/gxd/htexp_index")
        self.driver.implicitly_wait(10)

    def test_rnaseq_samples_array_express_link(self):
        '''
        @status this test verifies the array express link on the RNA-Seq samples page is correct.
        @see GXD-RNASeq-samples-1
        '''
        print ("BEGIN test_rnaseq_samples_array_express_link")
        
        self.driver.find_element(By.ID, 'strainNameAC').send_keys('C57BL/6J')#finds the age list and select the E4.0 option
        #find the Search button and click it
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        #find the View button of the second result and click it
        self.driver.find_element_by_id('row1button').click()
        #print result_set[2].text
        time.sleep(2)
        #switch focus the the popup samples window
        #switch focus to the next tab
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #find the Ext url IDs
        id_links = self.driver.find_elements_by_id('ids')
        id_links[0].click()
        time.sleep(5)
        #switch focus to the next tab
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #get the URL of the page
        page_url = self.driver.current_url
        print(page_url)
        #Assert the URL is correct
        self.assertEqual(page_url, "https://www.ebi.ac.uk/arrayexpress/experiments/E-ERAD-433/")
     
    def test_rnaseq_samples_exp_atlas_link(self):
        '''
        @status this test verifies the expression atlas link on the RNA-Seq samples page is correct.
        @see GXD-RNASeq-samples-2
        '''
        print ("BEGIN test_rnaseq_samples_exp_atlas_link")
        
        self.driver.find_element(By.ID, 'strainNameAC').send_keys('C57BL/6J')#finds the age list and select the E4.0 option
        #find the Search button and click it
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        #find the View button of the first result and click it
        self.driver.find_element_by_id('row0button').click()
        #print result_set[2].text
        time.sleep(2)
        #switch focus the the popup samples window
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #find the Ext url IDs for ID E-ERAD-169, we want to click the first one
        id_links = self.driver.find_elements_by_link_text('E-ERAD-169')
        id_links[1].click()
        time.sleep(2)
        #switch focus to the next tab(expression atlas page)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #get the URL of the page
        page_url = self.driver.current_url
        print(page_url)
        #Assert the URL is correct
        self.assertEqual(page_url, "https://www.ebi.ac.uk/gxa/experiments/E-ERAD-169/Results")

    def test_rnaseq_samples_geo_link(self):
        '''
        @status this test verifies the geo link on the RNA-Seq samples page is correct.
        @see GXD-RNASeq-samples-3
        '''
        print ("BEGIN test_rnaseq_samples_geo_link")
        
        self.driver.find_element(By.ID, 'strainNameAC').send_keys('C57BL/6J')#finds the age list and select the E4.0 option
        #find the Search button and click it
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        #find the View button of the third result and click it
        self.driver.find_element_by_id('row2button').click()
        time.sleep(2)
        #switch focus the the popup samples window
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #find the Ext url ID for ID GSE21860, we want to click it
        self.driver.find_element_by_link_text('GSE868').click()
        time.sleep(2)
        #switch focus to the next tab(geo page)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #get the URL of the page
        page_url = self.driver.current_url
        print(page_url)
        #Assert the URL is correct
        self.assertEqual(page_url, "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE868")
                    
    def test_rnaseq_samples_mutant_note(self):
        '''
        @status this test verifies a conditional mutant note on the RNA-Seq samples page for samples that require it.
        @see GXD-RNASeq-samples-4
        '''
        print ("BEGIN test_rnaseq_samples_mutant_note")
        #find the ArrayExpress or GEO ID filed and enter the text
        self.driver.find_element(By.ID, 'arrayExpressID').send_keys('E-GEOD-37646')#finds the age list and select the E4.0 option
        #find the Search button and click it
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        #find the View button of the first result and click it
        self.driver.find_element_by_id('row0button').click()
        time.sleep(2)
        #switch focus the the popup samples window
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #Find the sample table and locate the Note column
        sample_tbl = self.driver.find_element_by_id('sampleTable')
        table = Table(sample_tbl)
        #Iterate and print the Note column data
        muts = table.get_column_cells('Note')
        notes = iterate.getTextAsList(muts)
        print(notes)
        #Assert the first note field is correct
        self.assertEqual(notes[1], "Conditional mutant. day 6 of pregnancy")
    
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxdRnaSeqSamples))
    return suite 
       
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))