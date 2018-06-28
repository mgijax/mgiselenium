'''
Created on Jun 20, 2018

@author: jeffc
'''
import unittest
import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

import sys,os.path
#from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
from util import wait, iterate
from util.table import Table
import config
from selenium.webdriver.common.by import By
from config import TEST_URL

class Test(unittest.TestCase):


    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/marker/")
        self.driver.implicitly_wait(10)


    def test_tss_detail_start_site(self):
        '''
        @status this test opens the TSS Detail page and verifies the Transcription Start site contains a link to it's marker and
        @note in parenthesis how many base pair from the 5'-end of the gene. Confirm the details against the marker detail page 
        @note tssdetail-sum-1
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pax6').click() 
        #Click the link for Tssr19250 and click it
        self.driver.find_element(By.XPATH, '//*[@id="templateBodyInsert"]/div[2]/div[1]/div[2]/section[2]/ul/li[5]/div[2]/a[1]').click()  
        time.sleep(2)
        #find the Transcription Start Site field info
        trans = self.driver.find_element(By.XPATH, '//*[@id="templateBodyInsert"]/div[2]/div[1]/div[2]/section[2]/ul/li[2]/div[2]')  
        print trans.text
        self.assertEqual(trans.text, "Pax6 (1 bp from 5'-end of gene)", 'The Transcription Start Site info is not correct!')
        #find the Pax6 link in the Transcription Start Site for field and click it.
        self.driver.find_element(By.LINK_TEXT, 'Pax6').click()        
        #Find the All TSS link and click it
        self.driver.find_element(By.ID, 'showTss').click()
        time.sleep(2)
        tss_table = self.driver.find_element(By.ID, 'tssTable')
        table = Table(tss_table)
        #Iterate the table Location column
        cells = table.get_row_cells(1)
        row_cells = iterate.getTextAsList(cells) 
        print row_cells    
        #Verify the TSS table locations are correct and in the correct order.
        self.assertEqual(row_cells, ['Tssr19250', 'Chr2:105668888-105668914 (+)', '1 bp'])
               
        
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()        
        
        