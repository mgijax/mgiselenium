'''
Created on Jan 16, 2018
This set of tests verifies items found on the Recombinase specificity page
@author: jeffc
'''

import unittest
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
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
tracemalloc.start()
class TestCreSpecificity(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/home/recombinase")
        self.driver.implicitly_wait(10)

    def test_project_collection(self):
        '''
        @status This test verifies that the correct project collection is listed in the Mutation Origin section.
        '''
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('MGI:5014205')
        self.driver.find_element(By.NAME, 'submit').click()
        self.driver.find_element(By.ID, 'aLink').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1.1(cre)Mull').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.NAME, 'centeredTitle'), 'Targeted Allele Detail'))
        origin_table = self.driver.find_element(By.ID, 'mutationOriginTable')
        table = Table(origin_table)
        #gets the data found on the Project collection row of the Mutation origin ribbon
        term1 = table.get_cell(3, 0)
        term2 = table.get_cell(3, 1)
        
        print(term1.text)
        print(term2.text)
        time.sleep(2)
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('Project Collection:', term1.text, 'Term1 is not returning' )
        self.assertEqual('Neuroscience Blueprint cre', term2.text, "Term2 is incorrect")
     
    def test_no_project_collection(self):
        '''
        @status this test verifies when a cre allele is not assigned to a project collection that row does not display in the Mutation origin ribbon.
        @note test works 4/5/2022
        '''
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('MGI:2181632')
        self.driver.find_element(By.NAME, 'submit').click()
        self.driver.find_element(By.ID, 'aLink').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1(CAG-cre)Mnn').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.NAME, 'centeredTitle'), 'Targeted Allele Detail'))
        assert 'Project Collection:' not in self.driver.page_source
        
    def test_recomb_image_link(self):
        '''
        @status this test verifies when a recombinase activity detail page images display and the links go to the correct websites.
        @note fixed and tested 6/7/2022
        '''
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('MGI:4365736')
        self.driver.find_element(By.NAME, 'submit').click()
        self.driver.find_element(By.ID, 'aLink').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1(cre)Zjh').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.NAME, 'centeredTitle'), 'Targeted Allele Detail'))
        time.sleep(2)
        #toggles open the Recombinase activity table
        self.driver.find_element(By.ID, 'recomRibbonTeaser').click()
        time.sleep(3)
        #finds the cell for adipose tissue pre-weaning and clicks it
        self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(1) > td:nth-child(6)').click()
        time.sleep(2)
        #switch to the Counts popup
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        #click the link "View All result Deatails and Images" link
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'View All Result').click()
        time.sleep(2)
        #verify the cre image is displayed in the Images section
        self.driver.find_element(By.ID, 'creImg429235').is_displayed()
        
        # verifies the returned terms are the correct terms for this search
        #self.assertEqual('Project Collection:', term1.text, 'Term1 is not returning' )
        #self.assertEqual('Neuroscience Blueprint cre', term2.text, "Term2 is incorrect")
        #assert 'Project Collection:' not in self.driver.page_source

        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCreSpecificity))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))