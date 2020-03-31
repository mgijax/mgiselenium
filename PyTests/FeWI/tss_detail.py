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
        @status this test opens the TSS Detail table and verifies it is sorted correctly by distance from the marker.
        @note  
        @note tssdetail-sum-1
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pax6').click() 
        #Click the link for the TSS popup table
        self.driver.find_element(By.ID, 'showTss').click()        
        time.sleep(2)
        tss_table = self.driver.find_element(By.ID, 'tssTable')
        table = Table(tss_table)
        #Capture each row of the TSS table(only the first 5 rows)
        cells1 = table.get_row(1)
        cells2 = table.get_row(2)
        cells3 = table.get_row(3)
        cells4 = table.get_row(4)
        cells5 = table.get_row(5)
        print(cells1.text)    
        #Verify the TSS table locations are correct and in the correct order.
        self.assertEqual(cells1.text, 'Tssr19250 Chr2:105668888-105668914 (+) 1 bp')
        self.assertEqual(cells2.text, 'Tssr19251 Chr2:105668943-105668950 (+) 47 bp')
        self.assertEqual(cells3.text, 'Tssr19252 Chr2:105674406-105674422 (+) 5,514 bp')
        self.assertEqual(cells4.text, 'Tssr19253 Chr2:105674426-105674437 (+) 5,532 bp')
        self.assertEqual(cells5.text, 'Tssr19254 Chr2:105674543-105674558 (+) 5,651 bp')
               
        
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()        
        
        