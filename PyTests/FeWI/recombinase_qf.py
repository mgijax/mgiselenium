'''
Created on Apr 5, 2022
Tests features(especially search features) of the Recombinase (CRE) query form
@author: jeffc
'''
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys,os.path
from genericpath import exists
from selenium.webdriver.support.wait import WebDriverWait
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
from util.table import Table
import config
from config import TEST_URL
import time

class TestCreSpecificity(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/home/recombinase")
        self.driver.implicitly_wait(10)

    def test_1structure_detected(self):
        '''
        @status This test verifies that searching by a single structure detected return the correct results.
        @note: Recomb-test-1
        '''
        #find the Anatomical Structure field and enter text
        self.driver.find_element(By.NAME, 'structure_1').send_keys('definitive endoderm')
        self.driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'titleBarMainTitle'), 'Recombinase Alleles - Tissue Summary'))
        #find all the results in the Driver column so they can be verified
        driver1 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(1) > div:nth-child(1)')
        print(driver1.text)
        driver2 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec1 > td:nth-child(1) > div:nth-child(1)')
        print(driver2.text)
        driver3 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec2 > td:nth-child(1) > div:nth-child(1)')
        print(driver3.text)
        driver4 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec3 > td:nth-child(1) > div:nth-child(1)')
        print(driver4.text)
        
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('Foxa2', driver1.text, 'driver1 is not correct' )
        self.assertEqual('Krt19', driver2.text, 'driver2 is not correct')
        self.assertEqual('Lhx1', driver3.text, 'driver1 is not correct' )
        self.assertEqual('Sox17', driver4.text, 'driver2 is not correct')

    def test_2structure_detected(self):
        '''
        @status This test verifies that searching by a two structures detected return the correct results.
        @note: Recomb-test-2
        '''
        #find the Anatomical Structure field and enter text
        self.driver.find_element(By.NAME, 'structure_1').send_keys('ductus deferens')
        #find and click the Add structure button
        self.driver.find_element(By.CLASS_NAME, 'addButton').click()
        #find the new structure field and add a second structure
        self.driver.find_element(By.NAME, 'structure_2').send_keys('pons')
        self.driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'titleBarMainTitle'), 'Recombinase Alleles - Tissue Summary'))
        #find all the results in the Driver column so they can be verified
        driver1 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(1) > div:nth-child(1)')
        print(driver1.text)
        
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('EIIA', driver1.text, 'driver1 is not correct' )
     
    def test_2structure_detected_nowhere(self):
        '''
        @status This test verifies that searching by 2 structures detected and no where else return the correct results.
        @note: Recomb-test-3
        '''
        #find the Anatomical Structure field and enter text
        self.driver.find_element(By.NAME, 'structure_1').send_keys('brain stem')
        #find and click the Add structure button
        self.driver.find_element(By.CLASS_NAME, 'addButton').click()
        #find the new structure field and add a second structure
        self.driver.find_element(By.NAME, 'structure_2').send_keys('pons')
        #click the No where else toggle
        self.driver.find_element(By.ID, 'nowhereElse').click()
        self.driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'titleBarMainTitle'), 'Recombinase Alleles - Tissue Summary'))
        #find all the results in the Driver column so they can be verified
        driver1 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(1) > div:nth-child(1)')
        print(driver1.text)
        
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('Calca', driver1.text, 'driver1 is not correct' )
        
    def test_1structure_detected_1notdetected(self):
        '''
        @status This test verifies that searching by 2 structures, 1 detected and 1 not detected return the correct results.
        @note: Recomb-test-4
        '''
        #find the Anatomical Structure field and enter text
        self.driver.find_element(By.NAME, 'structure_1').send_keys('ductus deferens')
        #find and click the Add structure button
        self.driver.find_element(By.CLASS_NAME, 'addButton').click()
        #find the new structure field and add a second structure
        self.driver.find_element(By.NAME, 'structure_2').send_keys('pons')
        #set the not detected option for the structure pons
        self.driver.find_element(By.XPATH, "//input[@name='detected_2' and @value='false']").click()
        self.driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'titleBarMainTitle'), 'Recombinase Alleles - Tissue Summary'))
        #find all the results in the Driver column so they can be verified
        driver1 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(1) > div:nth-child(1)')
        print(driver1.text)
        driver2 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec1 > td:nth-child(1) > div:nth-child(1)')
        print(driver2.text)
        driver3 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec2 > td:nth-child(1) > div:nth-child(1)')
        print(driver3.text)
        driver4 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec3 > td:nth-child(1) > div:nth-child(1)')
        print(driver4.text)
        driver5 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec4 > td:nth-child(1) > div:nth-child(1)')
        print(driver5.text)
        driver6 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec5 > td:nth-child(1) > div:nth-child(1)')
        print(driver6.text)
        driver7 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec6 > td:nth-child(1) > div:nth-child(1)')
        print(driver7.text)
        
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('Ckm', driver1.text, 'driver1 is not correct' )
        self.assertEqual('Ltf', driver2.text, 'driver2 is not correct')
        self.assertEqual('MMTV', driver3.text, 'driver3 is not correct' )
        self.assertEqual('Myh11', driver4.text, 'driver4 is not correct')                
        self.assertEqual('Pax2', driver5.text, 'driver5 is not correct')
        self.assertEqual('Pbsn', driver6.text, 'driver6 is not correct' )
        self.assertEqual('Prlr', driver7.text, 'driver7 is not correct')
        
    def test_1structure_detected_1notdetecteddriver(self):
        '''
        @status This test verifies that searching by 2 structures, 1 detected and 1 not detected and driven by Ltf return the correct results.
        @note: Recomb-test-5
        '''
        #find the Anatomical Structure field and enter text
        self.driver.find_element(By.NAME, 'structure_1').send_keys('ductus deferens')
        #find and click the Add structure button
        self.driver.find_element(By.CLASS_NAME, 'addButton').click()
        #find the new structure field and add a second structure
        self.driver.find_element(By.NAME, 'structure_2').send_keys('pons')
        #set the not detected option for the structure pons
        self.driver.find_element(By.XPATH, "//input[@name='detected_2' and @value='false']").click()
        self.driver.find_element(By.ID, 'creDriverAC').send_keys('Ltf')
        self.driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'titleBarMainTitle'), 'Recombinase Alleles - Tissue Summary'))
        #find all the results in the Driver column so they can be verified
        driver1 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(1) > div:nth-child(1)')
        print(driver1.text)
        
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('Ltf', driver1.text, 'driver1 is not correct' )
                
        
        
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCreSpecificity))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))   