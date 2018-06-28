'''
Created on May 31, 2018

@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from util.table import Table
import sys,os.path
from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
import config
from config import TEST_URL

class TestBatchQuery(unittest.TestCase):


    def setUp(self):
    
        self.driver = webdriver.Firefox()
        self.driver.get(config.TEST_URL + "/batch")
        self.driver.implicitly_wait(10)

    def test_bq_strain_column(self):
        """
        @status: Tests that all batch queries results have a Strains column
        @note: batch-id-1,2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/batch")
        idsearchbox = driver.find_element(By.ID, 'ids')
        # Enter an MGP ID into the ID/Symbols field
        idsearchbox.send_keys("MGP_CBAJ_G0024006")
        idsearchbox.submit()
        #time.sleep(2)
        #locates the strain column, find all the rows of data and print it to the console
        strain_header = self.driver.find_element(By.ID, 'yui-dt0-th-strain')
        print strain_header.text        
        #asserts that the Strain header is correct
        self.assertEqual('Strain', strain_header.text) 
        #Find the strain field in the first row of data
        row1_strain = self.driver.find_element(By.XPATH, '//*[@id="yui-rec0"]/td[6]/div')
        print row1_strain.text
        #Assert that the row1 strain is C57BL/6J
        self.assertEqual(row1_strain.text, 'C57BL/6J')
        #Find the strain field in the second row of data
        row2_strain = self.driver.find_element(By.XPATH, '//*[@id="yui-rec1"]/td[6]/div')
        print row2_strain.text
        #Assert that the row2 strain is CBA/J
        self.assertEqual(row2_strain.text, 'CBA/J')

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
        #time.sleep(2)
        #locates the Input column, find all the rows of data and print it to the console
        input_header = self.driver.find_element(By.ID, 'yui-dt0-th-term-liner')
        print input_header.text        
        #asserts that the Input header is correct
        self.assertEqual('Input', input_header.text) 
        #Find the input field in each row of data
        row1_input = self.driver.find_element(By.XPATH, '//*[@id="yui-rec0"]/td[1]/div')
        row2_input = self.driver.find_element(By.XPATH, '//*[@id="yui-rec1"]/td[1]/div')
        row3_input = self.driver.find_element(By.XPATH, '//*[@id="yui-rec2"]/td[1]/div')
        row4_input = self.driver.find_element(By.XPATH, '//*[@id="yui-rec3"]/td[1]/div')
        row5_input = self.driver.find_element(By.XPATH, '//*[@id="yui-rec4"]/td[1]/div')
        row6_input = self.driver.find_element(By.XPATH, '//*[@id="yui-rec5"]/td[1]/div')
        row7_input = self.driver.find_element(By.XPATH, '//*[@id="yui-rec6"]/td[1]/div')
        row8_input = self.driver.find_element(By.XPATH, '//*[@id="yui-rec7"]/td[1]/div')
        print row1_input.text
        print row2_input.text
        print row3_input.text
        print row4_input.text
        print row5_input.text
        print row6_input.text
        print row7_input.text
        print row8_input.text
        #Assert that the input field is correct for each row
        self.assertEqual(row1_input.text, 'MGP_CBAJ_G0024006')
        self.assertEqual(row2_input.text, 'MGP_CBAJ_G0024006')
        self.assertEqual(row3_input.text, 'MGP_NZOHlLtJ_G0024761')
        self.assertEqual(row4_input.text, 'MGP_NZOHlLtJ_G0024761')
        self.assertEqual(row5_input.text, 'MGP_AJ_G0024271')
        self.assertEqual(row6_input.text, 'MGP_AJ_G0024271')
        self.assertEqual(row7_input.text, 'MGP_WSBEiJ_G0023575')
        self.assertEqual(row8_input.text, 'MGP_WSBEiJ_G0023575')
        
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
        #time.sleep(2)
        #locates the Input column, find all the rows of data and print it to the console
        input_header = self.driver.find_element(By.ID, 'yui-dt0-th-term-liner')
        print input_header.text        
        #asserts that the Input header is correct
        self.assertEqual('Input', input_header.text) 
        #capture the data for all 6 row results
        row1_data = self.driver.find_element(By.ID, 'yui-rec0')
        row2_data = self.driver.find_element(By.ID, 'yui-rec1')
        row3_data = self.driver.find_element(By.ID, 'yui-rec2')
        row4_data = self.driver.find_element(By.ID, 'yui-rec3')
        row5_data = self.driver.find_element(By.ID, 'yui-rec4')
        row6_data = self.driver.find_element(By.ID, 'yui-rec5')
        #print each row of data to the console
        print row1_data.text
        print row2_data.text
        print row3_data.text
        print row4_data.text
        print row5_data.text
        print row6_data.text
        #Assert each row of data is correct
        self.assertEqual(row1_data.text, 'MGP_CBAJ_G0024006\nMouse Genome Project\nMGI:2447322\nPcdha9\nprotocadherin alpha 9\nC57BL/6J\nprotein coding gene', 'Row1 data is not correct!')
        self.assertEqual(row2_data.text, 'MGP_CBAJ_G0024006\nMouse Genome Project\nMGI:2447322\nPcdha9\nprotocadherin alpha 9\nCBA/J\nprotein_coding', 'Row2 data is not correct!')
        self.assertEqual(row3_data.text, 'NM_008089\nRefSeq\nMGI:95661\nGata1\nGATA binding protein 1\nC57BL/6J\nprotein coding gene', 'Row3 data is not correct!')
        self.assertEqual(row4_data.text, 'MGP_AJ_G0024271\nMouse Genome Project\nMGI:2447322\nPcdha9\nprotocadherin alpha 9\nC57BL/6J\nprotein coding gene', 'Row4 data is not correct!')
        self.assertEqual(row5_data.text, 'MGP_AJ_G0024271\nMouse Genome Project\nMGI:2447322\nPcdha9\nprotocadherin alpha 9\nA/J\nprotein_coding', 'Row5 data is not correct!')
        self.assertEqual(row6_data.text, 'MGI:95661\nMGI\nMGI:95661\nGata1\nGATA binding protein 1\nC57BL/6J\nprotein coding gene', 'Row6 data is not correct!')
        
    def test_bq_mgp_ids_has_b6coord(self):
        """
        @status: Tests that batch queries  on an MGP ID that has B6 coordinates displays those coordinates
        @note: batch-id-5
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/batch")
        #locate the Genome Location checkbox in the Gene Attributes output section and click it.
        driver.find_element(By.ID, 'attributes2').click()
        idsearchbox = driver.find_element(By.ID, 'ids')
        # Enter an MGP ID into the ID/Symbols field
        idsearchbox.send_keys("MGP_CBAJ_G0024006")
        idsearchbox.submit()
        #time.sleep(2)
        #locates the Input column, find all the rows of data and print it to the console
        input_header = self.driver.find_element(By.ID, 'yui-dt0-th-term-liner')
        print input_header.text        
        #asserts that the Input header is correct
        self.assertEqual('Input', input_header.text) 
        #capture the data for all 6 row results
        row1_data = self.driver.find_element(By.ID, 'yui-rec0')
        row2_data = self.driver.find_element(By.ID, 'yui-rec1')
        
        #print each row of data to the console
        print row1_data.text
        print row2_data.text
        
        #Assert each row of data is correct
        self.assertEqual(row1_data.text, 'MGP_CBAJ_G0024006\nMouse Genome Project\nMGI:2447322\nPcdha9\nprotocadherin alpha 9\nC57BL/6J\nprotein coding gene\n18\n+\n36997880\n37187657', 'Row1 data is not correct!')
        self.assertEqual(row2_data.text, 'MGP_CBAJ_G0024006\nMouse Genome Project\nMGI:2447322\nPcdha9\nprotocadherin alpha 9\nCBA/J\nprotein_coding\n18\n+\n37745369\n37945878', 'Row2 data is not correct!')

    def test_bq_mgp_ids_has_no_b6coord(self):
        """
        @status: Tests that batch queries on an MGP ID that has NO B6 coordinates displays only the strain gene and it's coordinates
        @note: batch-id-6
        @bug: blank Name field makes this test fail, waiting for resolution by PIs
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/batch")
        #locate the Genome Location checkbox in the Gene Attributes output section and click it.
        driver.find_element(By.ID, 'attributes2').click()
        idsearchbox = driver.find_element(By.ID, 'ids')
        # Enter an MGP ID into the ID/Symbols field
        idsearchbox.send_keys("MGP_AKRJ_G0020754")
        idsearchbox.submit()
        #time.sleep(2)
        #locates the Input column, find all the rows of data and print it to the console
        input_header = self.driver.find_element(By.ID, 'yui-dt0-th-term-liner')
        print input_header.text        
        #asserts that the Input header is correct
        self.assertEqual('Input', input_header.text) 
        #capture the data for all 6 row results
        row1_data = self.driver.find_element(By.ID, 'yui-rec0')
        
        #print each row of data to the console
        print row1_data.text
        time.sleep(4)
        #Assert each row of data is correct
        self.assertEqual(row1_data.text, 'MGP_AKRJ_G0020754\nMouse Genome Project\nMGP_AKRJ_G0020754\nMGP_AKRJ_G0020754\n \nAKR/J\nprotein coding\n13\n-\n94228187\n94249372', 'Row1 data is not correct!')

    def test_bq_mgi_gm_ids_has_b6coord(self):
        """
        @status: Tests that batch queries on an MGI Gene Model ID that the correct results are returned
        @note: batch-id-10
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/batch")
        #locate the Genome Location checkbox in the Gene Attributes output section and click it.
        driver.find_element(By.ID, 'attributes2').click()
        idsearchbox = driver.find_element(By.ID, 'ids')
        # Enter an MGP ID into the ID/Symbols field
        idsearchbox.send_keys("MGI_C57BL6J_98660")
        idsearchbox.submit()
        #time.sleep(2)
        #locates the Input column, find all the rows of data and print it to the console
        input_header = self.driver.find_element(By.ID, 'yui-dt0-th-term-liner')
        print input_header.text        
        #asserts that the Input header is correct
        self.assertEqual('Input', input_header.text) 
        #capture the data for all 6 row results
        row1_data = self.driver.find_element(By.ID, 'yui-rec0')
        row2_data = self.driver.find_element(By.ID, 'yui-rec1')
        
        #print each row of data to the console
        print row1_data.text
        print row2_data.text
        
        #Assert each row of data is correct
        self.assertEqual(row1_data.text, 'MGI_C57BL6J_98660\nMGI Strain Gene\nMGI:98660\nSry\nsex determining region of Chr Y\nC57BL/6J\nprotein coding gene\nY\n-\n2662471\n2663658', 'Row1 data is not correct!')
        self.assertEqual(row2_data.text, 'MGI_C57BL6J_98660\nMGI Strain Gene\nMGI:98660\nSry\nsex determining region of Chr Y\nC57BL/6J\nprotein-coding\nY\n-\n2662471\n2663658', 'Row2 data is not correct!')

    def test_bq_strain_links(self):
        """
        @status: Tests that all strains listed in the strains column go to their respective detail pages
        @note: batch-id-11
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/batch")
        idsearchbox = driver.find_element(By.ID, 'ids')
        # Enter an MGP ID into the ID/Symbols field
        idsearchbox.send_keys("MGP_CBAJ_G0024006")
        idsearchbox.submit()
        #locates the strain column, and click the first strain(C57BL/6J)
        self.driver.find_element(By.LINK_TEXT, '(C57BL/6J)').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #Identify the page title
        page_header = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')      
        #asserts that the Page header is correct
        self.assertEqual('C57BL/6J', page_header.text) 
        #switch focus back to the batch query summary
        driver.switch_to_window(self.driver.window_handles[0])
        #locates the strain column, and click the second strain(CBA/J)
        self.driver.find_element(By.LINK_TEXT, '(CBA/J)').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-2])
        #Identify the page title
        page_header = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')      
        #asserts that the Page header is correct
        self.assert_(expr, msg) 

        
    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBatchQuery))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'TestBatchQuery.testName']
    unittest.main()  
