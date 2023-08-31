'''
Created on Sep 30, 2019
Tests for the RNA-Seq Samples page
@author: jeffc
Verify the array express link on the RNA-Seq samples page is correct
Verify the expression atlas link on the RNA-Seq samples page is correct
Verify the geo link on the RNA-Seq samples page is correct
Verify a conditional mutant note on the RNA-Seq samples page for samples that require it
'''
import unittest
import time
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
tracemalloc.start()
class TestGxdRnaSeqSamples(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/gxd/htexp_index")
        self.driver.implicitly_wait(10)

    def test_rnaseq_samples_array_express_link(self):
        '''
        @status this test verifies the array express link on the RNA-Seq samples page is correct.
        @see GXD-RNASeq-samples-1
        '''
        print ("BEGIN test_rnaseq_samples_array_express_link")
        #find the Strain field and enter the text
        self.driver.find_element(By.ID, 'strainNameAC').send_keys('C57BL/6J')
        #find the ArrayExpress or GEO ID field and enter the text
        self.driver.find_element(By.ID, 'arrayExpressID').send_keys('E-MEXP-5')
        #find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        #find the View button of the first result and click it
        self.driver.find_element(By.ID, 'row0button').click()
        #switch focus the the popup samples window
        #switch focus to the next tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #find the ArrayExpress ID E-MEXP-5 link and click it
        self.driver.find_element(By.LINK_TEXT, 'E-MEXP-5').click()
        time.sleep(2)
        #switch focus to the next tab
        self.driver.switch_to.window(self.driver.window_handles[-2])
        #get the URL of the page
        page_url = self.driver.current_url
        print(page_url)
        #Assert the URL is correct
        self.assertEqual(page_url, "https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MEXP-5")
     
    def test_rnaseq_samples_expression_atlas_link(self):
        '''
        @status this test verifies the expression atlas link on the RNA-Seq samples page is correct.
        @see GXD-RNASeq-samples-2 
        '''
        print ("BEGIN test_rnaseq_samples_exp_atlas_link")

        self.driver.find_element(By.ID, 'stagesTab').click()
        Select(self.driver.find_element(By.ID, 'theilerStage')).deselect_by_value('0')#deselect the default option
        Select(self.driver.find_element(By.ID, 'theilerStage')).select_by_value('27')#finds the theiler stage list and select the TS 27 option
        self.driver.find_element(By.ID, 'strainNameAC').send_keys('C57BL/6J')#finds the strain field and enter C57BL/6J
        #find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        #find the View button of the first result and click it
        self.driver.find_element(By.ID, 'row0button').click()
        #switch focus the the popup samples window
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #find the Expression Atlas ID E-GEOD-1294 link and click it
        Atlas_Link = self.driver.find_element(By.LINK_TEXT, 'E-GEOD-1294').click() 
        time.sleep(2)
        print(Atlas_Link)
        #switch focus to the next tab(expression atlas page)
        self.driver.switch_to.window(self.driver.window_handles[-2])
        #get the URL of the page
        page_url = self.driver.current_url
        print(page_url)
        #Assert the URL is correct
        self.assertEqual(page_url, "https://www.ebi.ac.uk/gxa/experiments/E-GEOD-1294/Results")

    def test_rnaseq_samples_geo_link(self):
        '''
        @status this test verifies the geo link on the RNA-Seq samples page is correct.
        @see GXD-RNASeq-samples-3
        '''
        print ("BEGIN test_rnaseq_samples_geo_link")
        
        self.driver.find_element(By.ID, 'strainNameAC').send_keys('C57BL/6J')#finds the age list and select the E4.0 option
        #find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        #find the View button of the second result and click it
        self.driver.find_element(By.ID, 'row1button').click()
        #switch focus the the popup samples window
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #find the GEO link GSE868 and click it
        self.driver.find_element(By.LINK_TEXT, 'GSE868').click()
        time.sleep(2)
        #switch focus to the next tab(geo page)
        self.driver.switch_to.window(self.driver.window_handles[-2])
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
        self.driver.find_element(By.ID, 'submit1').click()
        #find the View button of the first result and click it
        self.driver.find_element(By.ID, 'row0button').click()
        #switch focus the the popup samples window
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #Find the sample table and locate the Note column
        sample_tbl = self.driver.find_element(By.ID, 'sampleTable')
        table = Table(sample_tbl)
        #Iterate and print the Note column data
        muts = table.get_column_cells('Note')
        notes = iterate.getTextAsList(muts)
        print(notes)
        #Assert the first note field is correct
        self.assertEqual(notes[1], "Conditional mutant. day 6 of pregnancy")
    
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxdRnaSeqSamples))
    return suite 
       
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))