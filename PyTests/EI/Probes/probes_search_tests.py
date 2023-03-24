'''
Created on Sep 8, 2022

@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import HtmlTestRunner
import json
import sys,os.path
from test.test_base64 import BaseXYTestCase
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests

class TestEIProbeSearch(unittest.TestCase):
    """
    @status Test Probe searching, etc
    """

    def setUp(self):
        self.driver = webdriver.Firefox() 
        #self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/probe")
    

    def testProbeSegmentTypeSearch(self):
        """
        @Status tests that a basic probe segment type search works
        @see pwi-probe-search-sum-1
        """
        driver = self.driver
        #finds the Probe segment type field and select the option Mitochondrial, then click the Search Summary button
        Select(driver.find_element(By.ID, "segmentType")).select_by_value('string:63471')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchSummaryButton').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        #find the search results table
        results_table = self.driver.find_element(By.CLASS_NAME, "dataTable")
        table = Table(results_table)
        #Iterate and print the search results for column Type
        col1 = table.get_column_cells('Type')
        segment = iterate.getTextAsList(col1)
        print(segment)
        #Assert the correct antibody is returned
        self.assertEqual(segment, ['Type', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial', 'mitochondrial'])
        
    def testProbeSegmentTypeNameSearch(self):
        """
        @Status tests that a basic probe segment type and name summary search works
        @see pwi-probe-search-sum-2
        """
        driver = self.driver
        #finds the Probe segment type field and select the option Primer, enter mm04% in the name field then click the Search Summary button
        Select(driver.find_element(By.ID, "segmentType")).select_by_value('string:63473')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'name').send_keys('mm04%')
        driver.find_element(By.ID, 'searchSummaryButton').click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        #find the search results table
        results_table = self.driver.find_element(By.CLASS_NAME, "dataTable")
        table = Table(results_table)
        #find and print the search results for row 1 Type field
        type1 = table.get_cell(1, 2)
        print(type1.text)
        #Assert the correct type is returned
        self.assertEqual(type1.text, 'primer')
        #find and print the search results for row 1 Name field
        name1 = table.get_cell(1, 1)
        print(name1.text)      
        #Assert the correct names are returned
        self.assertEqual(name1.text, 'Mm04183367_g1')

    def testProbeNameSearch(self):
        """
        @Status tests that a basic probe name summary search works, this also checks for an Alias
        @see pwi-probe-search-sum-3
        """
        driver = self.driver
        #enter probe1 in the name field then click the Search Summary button
        driver.find_element(By.ID, 'name').send_keys('probe1')
        driver.find_element(By.ID, 'searchSummaryButton').click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        #find the search results table
        results_table = self.driver.find_element(By.CLASS_NAME, "dataTable")
        table = Table(results_table)
        #find and print the search results for row 1 alias field
        alias1 = table.get_cell(1, 7)
        print(alias1.text)
        #Assert the correct alias is returned
        self.assertEqual(alias1.text, 'probe1')
        #find and print the search results for row 2 Name field
        name2 = table.get_cell(2, 1)
        print(name2.text)      
        #Assert the correct names are returned
        self.assertEqual(name2.text, 'probe1')

    def testProbeNamewWildcardSearch(self):
        """
        @Status tests that a basic probe name with wildcard summary search works
        @see pwi-probe-search-sum-3
        """
        driver = self.driver
        #enter probe1 in the name field then click the Search Summary button
        driver.find_element(By.ID, 'name').send_keys('ND3%')
        driver.find_element(By.ID, 'searchSummaryButton').click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        #find the search results table
        results_table = self.driver.find_element(By.CLASS_NAME, "dataTable")
        table = Table(results_table)
        #find and print the search results for row 1,2,3,4 Name field
        name1 = table.get_cell(1, 1)
        name2 = table.get_cell(2, 1)
        name3 = table.get_cell(3, 1)
        name4 = table.get_cell(4, 1)
        print(name4.text)      
        #Assert the correct names are returned
        self.assertEqual(name1.text, 'ND3 mtDNA1')
        self.assertEqual(name2.text, 'ND3 mtDNA2')
        self.assertEqual(name3.text, 'ND3 mtDNA3')
        self.assertEqual(name4.text, 'ND3_riboprobe')
                        
    def tearDown(self):
        self.driver.close()        
        
        
        
        