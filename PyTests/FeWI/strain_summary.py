'''
Created on May 15, 2018
@author: jeffc
Verify that the text is correct for the 'you searched for section
Verify that the text is correct for the 'you searched for section when searching for name and attribute
Verify that the strain summary page table headings are correct
Verify that the strain name link on a strain summary page goes to the correct page
Verify that the Reference link on a strain summary page goes to the correct page
Verify that all the ID have a prefix to further identify them
Verify that you can filter results by an attribute
'''
import unittest
import time
import tracemalloc
import config
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select as WebDriverSelect
from selenium.webdriver.support.ui import Select
from util.table import Table
from util.form import ModuleForm
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from genericpath import exists
from _elementtree import Element
from util import wait, iterate
from config import TEST_URL

#Tests
tracemalloc.start()
class TestStrainSummary(unittest.TestCase):


    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        self.driver.implicitly_wait(10)

    def test_summary_you_searched_for(self):
        """
        @status: Tests that the text is correct for the 'you searched for section
        @note: Strain-sum-id-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("101/H")
        strainsearchbox.send_keys(Keys.RETURN)
        #locates the 'you searched for' text to verify it is correct correct
        you_srch = driver.find_element(By.ID, 'ysf')
        print(you_srch.text)
        #asserts that the following IDs are returned
        self.assertEqual('You Searched For...\nName/Synonym/ID: equals 101/H searching current names and synonyms', you_srch.text) # You Searched for text
                        
    def test_summary_ysf_name_attrib(self):
        """
        @status: Tests that the text is correct for the 'you searched for section when searching for name and attribute
        @note: Strain-sum-id-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("101/H")
        #find the inbred strain option in the list and select it
        Select (driver.find_element(By.NAME, 'attributes')).select_by_visible_text('inbred strain')
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        #locates the 'you searched for' text to verify it is correct correct
        you_srch = driver.find_element(By.ID, 'ysf')
        print(you_srch.text)
        #asserts that the following IDs are returned
        self.assertEqual('You Searched For...\nName/Synonym/ID: equals 101/H searching current names and synonyms\nAttributes: inbred strain', you_srch.text) # You Searched for text                           
                
    def test_summary_strain_headings(self):
        """
        @status: Tests that the strain summary page table headings are correct
        @note: Strain-sum-id-3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("BALB/cJ")
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        #locates the strain table and verify the IDs/Links are correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        headings = strain_table.get_header_cells()
        print(iterate.getTextAsList(headings))
        hdsReturned = iterate.getTextAsList(headings)
        #asserts that the Headings are correct
        self.assertEqual(['Strain/Stock Name', 'Synonyms', 'Attributes', 'IDs', 'References'], hdsReturned) # ID link
        

    def test_summary_strain_strain_link(self):
        """
        @status: Tests that the strain name link on a strain summary page goes to the correct page
        @note: Strain-sum-id-4
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("129(B6)-Elf5<tm1Mapr>")
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        #locates the link for the official strain name
        driver.find_element(By.PARTIAL_LINK_TEXT, '129').click()
        #switch focus to the new tab for strain detail page
        driver.switch_to.window(self.driver.window_handles[-1])
        tpage = driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        print(tpage.text)
        #asserts that the correct page is returned or not
        self.assertEqual('B6;129S4-Elf5tm1Mapr/Apb', tpage.text, 'The page title is not correct!')   

    def test_summary_strain_reference_link(self):
        """
        @status: Tests that the Reference link on a strain summary page goes to the correct page
        @note: Strain-sum-id-5
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("B6Ei.LT-Y(IsXPAR;Y)Ei/EiJ")
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        #locates the link for the references
        driver.find_element(By.CLASS_NAME, 'referenceLink').click()
        #switch focus to the new tab for strain detail page
        driver.switch_to.window(self.driver.window_handles[-1])
        sname = driver.find_element(By.CLASS_NAME, 'symbolLink')
        print(sname.text)
        #asserts that the correct page is returned or not
        self.assertEqual('B6Ei.LT-Y(IsXPAR;Y)Ei/EiJ', sname.text, 'The strain name is not correct!')  
        

    def test_summary_strain_id_prefix(self):
        """
        @status: Tests that all the ID have a prefix to further identify them
        @note: Strain-sum-id-6
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("129S1/SvImJ")
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        #locates the strain table and verify the IDs are correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        ids = strain_table.get_column_cells('IDs')
        print(iterate.getTextAsList(ids))
        idsReturned = iterate.getTextAsList(ids)
        #asserts that the Headings are correct
        self.assertEqual(['IDs','MGI:3037980\nJAX:002448\nMPD:3'], idsReturned) # ID link
        
    def test_summary_attribute_filter(self):
        """
        @status: Tests that you can filter results by an attribute
        @note: Strain-sum-7
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("SL*")
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        #locates the attribute filter and click it to display the list of filter options
        self.driver.find_element(By.CLASS_NAME, 'filterButton').click()
        self.driver.find_elements(By.CLASS_NAME, 'attributeFilter')
        #find the option 'congenic' and click it
        element = self.driver.find_element(By.CSS_SELECTOR, "input[value='congenic'][type='checkbox']")        
        ActionChains(driver).click(element)\
            .send_keys(Keys.ENTER)\
            .perform()
        #locate the Filter button below the filter by attributes list and click it
        self.driver.find_element(By.ID, 'yui-gen0-button').click()
        #locates the strain table and verify the Attributes are correct for each of the 5 results
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        ids = strain_table.get_column_cells('Attributes')
        print(iterate.getTextAsList(ids))
        idsReturned = iterate.getTextAsList(ids)
        #asserts that the Headings are correct
        self.assertEqual('congenic\nmutant strain\ntargeted mutation', idsReturned[1]) #Assert the first row of attributes are correct
        self.assertEqual('congenic\nmutant strain\ntargeted mutation', idsReturned[2]) #Assert the second row of attributes are correct 
        self.assertEqual('congenic\nmutant strain\ntargeted mutation', idsReturned[3]) #Assert the third row of attributes are correct 
        self.assertEqual('congenic\nmutant strain\ntargeted mutation\ntransgenic', idsReturned[4]) #Assert the fourth row of attributes are correct 
        self.assertEqual('congenic\nmutant strain', idsReturned[5]) #Assert the fifth row of attributes are correct

              
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestStrainSummary))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
