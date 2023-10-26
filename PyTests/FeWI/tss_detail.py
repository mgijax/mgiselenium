'''
Created on Jun 20, 2018
@author: jeffc
Verify opens the TSS Detail table and verifies it is sorted correctly by distance from the marker
'''
import unittest
import time
import tracemalloc
import config
import sys,os.path
#from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import wait, iterate
from util.table import Table
from selenium.webdriver.common.by import By
from config import TEST_URL

#Test
tracemalloc.start()
class TestTssDetail(unittest.TestCase):


    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
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
        self.assertEqual(cells1.text, 'Tssr19250 Chr2:105499233-105499259 (+) 1 bp')
        self.assertEqual(cells2.text, 'Tssr19251 Chr2:105499288-105499295 (+) 47 bp')
        self.assertEqual(cells3.text, 'Tssr19252 Chr2:105504751-105504767 (+) 5,514 bp')
        self.assertEqual(cells4.text, 'Tssr19253 Chr2:105504771-105504782 (+) 5,532 bp')
        self.assertEqual(cells5.text, 'Tssr19254 Chr2:105504888-105504903 (+) 5,651 bp')
               
        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTssDetail))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
        