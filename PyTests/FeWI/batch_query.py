"""
Created on May 31, 2018
@author: jeffc
Verify searching by an MGP ID
Verify searching by multiple MGP IDs
Verify searching by MGP ID and other IDs
Verify searching by MGP ID with B6 coordinates
Verify searching by MGP ID with no B6 coordinates
Verify searching by MGI gene model ID with B6 coordinates
"""
import os.path
import sys
import tracemalloc
import unittest

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import config

# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
# Tests
tracemalloc.start()
class TestBatchQuery(unittest.TestCase):


    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/batch")
        self.driver.implicitly_wait(10)

    def test_bq_single_mgp_id(self):
        """
        @status: Tests batch queries results when searching for a single MGP ID
        @note: batch-id-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/batch")
        idsearchbox = driver.find_element(By.ID, 'ids')
        # Enter an MGP ID into the ID/Symbols field
        idsearchbox.send_keys("MGP_CBAJ_G0024006")
        idsearchbox.submit()
        # locates the Input Type column, find all the rows of data and print it to the console
        type_header = self.driver.find_element(By.ID, 'yui-dt0-th-type')
        print(type_header.text)        
        # asserts that the Input Type header is correct
        self.assertEqual('Input\nType', type_header.text) 
        # Find the Input Type field in the first row of data
        row1_type = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[6]/table/tbody[2]/tr/td[2]/div')
        print(row1_type.text)
        # Assert that the row1 Input Type is Mouse Genome Project
        self.assertEqual(row1_type.text, 'Mouse Genome Project')

    def test_bq_multi_mgp_ids(self):
        """
        @status: Tests that batch queries can be done using multiple MGP IDs
        @note: batch-id-3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/batch")
        idsearchbox = driver.find_element(By.ID, 'ids')
        # Enter an MGP ID into the ID/Symbols field
        idsearchbox.send_keys("MGP_CBAJ_G0024006, MGP_NZOHlLtJ_G0024761, MGP_AJ_G0024271, MGP_WSBEiJ_G0023575")
        idsearchbox.submit()
        # locates the Input column, find all the rows of data and print it to the console
        input_header = self.driver.find_element(By.ID, 'yui-dt0-th-term-liner')
        print(input_header.text)        
        # asserts that the Input header is correct
        self.assertEqual('Input', input_header.text) 
        # Find the input field in each row of data
        row1_input = self.driver.find_element(By.XPATH, '//*[@id="yui-rec0"]/td[1]/div')
        row2_input = self.driver.find_element(By.XPATH, '//*[@id="yui-rec1"]/td[1]/div')
        row3_input = self.driver.find_element(By.XPATH, '//*[@id="yui-rec2"]/td[1]/div')
        row4_input = self.driver.find_element(By.XPATH, '//*[@id="yui-rec3"]/td[1]/div')
        print(row1_input.text)
        print(row2_input.text)
        print(row3_input.text)
        print(row4_input.text)
        
        # Assert that the input field is correct for each row
        self.assertEqual(row1_input.text, 'MGP_CBAJ_G0024006')
        self.assertEqual(row2_input.text, 'MGP_NZOHlLtJ_G0024761')
        self.assertEqual(row3_input.text, 'MGP_AJ_G0024271')
        self.assertEqual(row4_input.text, 'MGP_WSBEiJ_G0023575')
        
    def test_bq_mgp_ids_other_ids(self):
        """
        @status: Tests that batch queries can be done using MGP IDs and other IDs
        @note: batch-id-4
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/batch")
        idsearchbox = driver.find_element(By.ID, 'ids')
        # Enter an MGP ID into the ID/Symbols field
        idsearchbox.send_keys("MGP_CBAJ_G0024006, NM_008089, MGP_AJ_G0024271, MGI:95661")
        idsearchbox.submit()
        # locates the Input column, find all the rows of data and print it to the console
        input_header = self.driver.find_element(By.ID, 'yui-dt0-th-term-liner')
        print(input_header.text)        
        # asserts that the Input header is correct
        self.assertEqual('Input', input_header.text) 
        # capture the data for all 6 row results
        row1_data = self.driver.find_element(By.ID, 'yui-rec0')
        row2_data = self.driver.find_element(By.ID, 'yui-rec1')
        row3_data = self.driver.find_element(By.ID, 'yui-rec2')
        row4_data = self.driver.find_element(By.ID, 'yui-rec3')
        # print each row of data to the console
        print(row1_data.text)
        print(row2_data.text)
        print(row3_data.text)
        print(row4_data.text)
        # Assert each row of data is correct
        self.assertEqual(row1_data.text, 'MGP_CBAJ_G0024006\nMouse Genome Project\nMGI:2447322\nPcdha9\nprotocadherin alpha 9\nprotein coding gene', 'Row1 data is not correct!')
        self.assertEqual(row2_data.text, 'NM_008089\nRefSeq\nMGI:95661\nGata1\nGATA binding protein 1\nprotein coding gene', 'Row2 data is not correct!')
        self.assertEqual(row3_data.text, 'MGP_AJ_G0024271\nMouse Genome Project\nMGI:2447322\nPcdha9\nprotocadherin alpha 9\nprotein coding gene', 'Row3 data is not correct!')
        self.assertEqual(row4_data.text, 'MGI:95661\nMGI\nMGI:95661\nGata1\nGATA binding protein 1\nprotein coding gene', 'Row4 data is not correct!')
        
    def test_bq_mgp_ids_has_b6coord(self):
        """
        @status: Tests that batch queries on an MGP ID that has B6 coordinates displays those coordinates
        @note: batch-id-5
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/batch")
        # locate the C57BL/6J Genome Location checkbox in the Gene Attributes output section and click it.
        driver.find_element(By.ID, 'attributes2').click()
        idsearchbox = driver.find_element(By.ID, 'ids')
        # Enter an MGP ID into the ID/Symbols field
        idsearchbox.send_keys("MGP_CBAJ_G0024006")
        idsearchbox.submit()
        # locates the Input column, find all the rows of data and print it to the console
        input_header = self.driver.find_element(By.ID, 'yui-dt0-th-term-liner')
        print(input_header.text)        
        # asserts that the Input header is correct
        self.assertEqual('Input', input_header.text) 
        # capture the data for all 6 row results
        row1_data = self.driver.find_element(By.ID, 'yui-rec0')        
        # print each row of data to the console
        print(row1_data.text)        
        # Assert each row of data is correct
        self.assertEqual(row1_data.text, 'MGP_CBAJ_G0024006\nMouse Genome Project\nMGI:2447322\nPcdha9\nprotocadherin alpha 9\nprotein coding gene\n18\n+\n37130933\n37320710', 'Row1 data is not correct!')
       
    def test_bq_mgp_ids_has_no_b6coord(self):
        """
        @status: Tests that batch queries on an MGP ID that has NO B6 coordinates displays "no associated gene" in the MGI Gene/Marker ID field
        @note: batch-id-6
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/batch")
        # locate the Genome Location checkbox in the Gene Attributes output section and click it.
        driver.find_element(By.ID, 'attributes2').click()
        idsearchbox = driver.find_element(By.ID, 'ids')
        # Enter an MGP ID into the ID/Symbols field
        idsearchbox.send_keys("MGP_DBA2J*")
        idsearchbox.submit()
        # locates the Input column row1
        input_1 = self.driver.find_element(By.CSS_SELECTOR, 'td.yui-dt0-col-term > div:nth-child(1)')
        print(input_1.text)        
        # asserts that the Input row1 data is correct
        self.assertEqual(input_1.text, 'MGP_DBA2J') 
        # locates the MGI Gene/Marker ID row1
        input_3 = self.driver.find_element(By.CSS_SELECTOR, 'td.yui-dt0-col-markerId > div:nth-child(1)')
        print(input_3.text)
        # Assert that the MGI Gene/Marker ID row1 data is correct
        self.assertEqual(input_3.text, 'No associated gene', 'Row1 data is not correct!')

    def test_bq_mgi_gm_ids_has_b6coord(self):
        """
        @status: Tests that batch queries on an MGI Gene Model ID that the correct results are returned
        @note: batch-id-10
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/batch")
        # locate the C57BL/6J Genome Location checkbox in the Gene Attributes output section and click it.
        driver.find_element(By.ID, 'attributes2').click()
        idsearchbox = driver.find_element(By.ID, 'ids')
        # Enter an MGP ID into the ID/Symbols field
        idsearchbox.send_keys("MGI_C57BL6J_98660")
        idsearchbox.submit()
        # locates the Input column, find all the rows of data and print it to the console
        input_header = self.driver.find_element(By.ID, 'yui-dt0-th-term-liner')
        print(input_header.text)        
        # asserts that the Input header is correct
        self.assertEqual('Input', input_header.text) 
        # capture the data for all 6 row results
        row1_data = self.driver.find_element(By.ID, 'yui-rec0')   
        # print each row of data to the console
        print(row1_data.text) 
        # Assert each row of data is correct
        self.assertEqual(row1_data.text, 'MGI_C57BL6J_98660\nMGI Strain Gene\nMGI:98660\nSry\nsex determining region of Chr Y\nprotein coding gene\nY\n-\n2662471\n2663658', 'Row1 data is not correct!')

        
    def tearDown(self):
        # self.driver.close()
        self.driver.quit()
        tracemalloc.stop()
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBatchQuery))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
