'''
Created on Oct 21, 2016
These tests were created to verify details on the Genotype detail pages(genoview) and all Genotype page(allgenoviews)
@author: jeffc
'''
import unittest
import time
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import sys,os.path
from selenium.common.exceptions import NoSuchElementException
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
class TestGenotypeDetail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/allele/")
        self.driver.implicitly_wait(10)
        
    def test_genotype_header(self):
        '''
        @status this test verifies the Genotype heading details except 'find mice' information.
        @note
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '132-14Neu').click()
        self.driver.find_element(By.LINK_TEXT, 'hm1').click()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.window(self.driver.window_handles[1])
        mgiid = self.driver.find_element(By.CLASS_NAME, 'genoID')
        self.assertEqual(mgiid.text, "MGI:3707321", "This is not the correct MGI ID")#verifies we have the correct MGI ID  
        hmid = self.driver.find_element(By.CLASS_NAME, 'hmGeno')
        self.assertEqual(hmid.text, "hm1", "This is not the correct hm ID")#verifies we are bringing the hm1 data back  
        gt = self.driver.find_element(By.CLASS_NAME, 'genotypeCombo')
        print(gt.text)
        self.assertEqual(gt.text, "Pax6132-14Neu/Pax6132-14Neu", "This is not the correct genotype combo")#verifies the Allelic Composition is correct 
             
        link = self.driver.find_element(By.LINK_TEXT, 'C3.Cg-Pax6132-14Neu')
        self.assertEqual(link.text, 'C3.Cg-Pax6132-14Neu', 'This is not the correct Genetic Background!')#verifies the Genetic Background is correct
        
    def test_genotype_gb_link(self):
        '''
        @status this test verifies the Genetic Background link is correct.
        @note genodetail-1 
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '132-14Neu').click()
        self.driver.find_element(By.LINK_TEXT, 'hm1').click()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        #click the Genetic Background link     
        self.driver.find_element(By.LINK_TEXT, 'C3.Cg-Pax6132-14Neu').click()
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(2)
        ptitle = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        #Assert the page title is for the correct strain name
        self.assertEqual(ptitle.text, "C3.Cg-Pax6132-14Neu")        
        
    def test_genotype_gb_nolink(self):
        '''
        @status this test verifies the Genetic Background strain is not a link when it has 'involves'.
        @note genodetail-2 BUG!!! Needs work, maybe need to verify link does not exist!!
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Pax62Neu').click()
        self.driver.find_element(By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()
        self.driver.implicitly_wait(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        #click the Genetic Background link 
        strain_link = self.driver.find_element(By.LINK_TEXT, 'involves: 102 * C3H')
        if strain_link.tag_name=='a': #validating the element 
            print('element is link')
        else:
            print('element is text')  
        
        
        #assert  'NoSuchElementException' in  self.driver.page_source
        #if self.driver.strain_link.is_displayed():
            #strain_link.click()
            #print ('Found the strain link and clicked it!')
        #else: 
            #print ("Strain link not found this test passes!") 

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()
       

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGenotypeDetail))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))