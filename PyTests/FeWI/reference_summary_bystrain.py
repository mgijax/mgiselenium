'''
Created on May 18, 2018

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

class TestReferenceSummaryStrain(unittest.TestCase):


    def setUp(self):
    
        self.driver = webdriver.Firefox()
        self.driver.get(config.TEST_URL + "/reference")
        self.driver.implicitly_wait(10)

    def test_ref_summary_both_reftype(self):
        """
        @status: Tests that all the reference results are correct when you have a strain with both normal references and curator added references
        @note: ref-sum-bystrain-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/reference")
        idsearchbox = driver.find_element(By.ID, 'id')
        # Enter your J number in the searchbox
        idsearchbox.send_keys("J:24637")
        idsearchbox.submit()
        #time.sleep(2)
        #find the link beside the word Strains in the Curated Data column and click it
        self.driver.find_element_by_link_text('2').click()
        #locates the strain summary table, find all the rows of data and print it to the console
        strain_table = Table(self.driver.find_element_by_id("strainSummaryTable"))
        straindata = strain_table.get_rows()
        print iterate.getTextAsList(straindata)
        idsReturned = iterate.getTextAsList(straindata)
        #asserts that the 2 rows of data are correct
        self.assertEqual(['Official Strain Name Synonyms Attributes IDs References', 'BUB/BnJ BUB/BnJ-Pde6brd1\ninbred strain\nMGI:2159907\nJAX:000653\nMPD:24\n70', 'SF/CamEiJ San Franciscan\ninbred strain\nwild-derived\nMGI:2159978\nJAX:000280\nMPD:159\n18'], idsReturned) 
        #The reason we brought back all the rows of data is because we needed to make sure the reference counts were correct and it did not bring back duplicate J numbers
        #example BUB/BnJ shows 67 references, in the EI it shows 69 between the two reference tables. The 2 extra references are because both EI tables have J:6844 and J:17601,
        #duplicate J numbers are not displayed in the FEWI strain summary for reference page. 
              
    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestReferenceSummaryStrain))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'TestReferenceSummaryStrain.testName']
    unittest.main()  
