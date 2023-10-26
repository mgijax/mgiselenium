'''
Created on Dec 12, 2016
@author: jeffc
Tests the GXD Image summary page.
Verify that the genes column sorts genes result correctly
Verify the sort order for assay type using default sort
Verify the sort order for specimen type using default sort
Verify that the Gene column sort works correctly
Verify that the assay type column sort works correctly
Verify that the specimen type column sort works correctly
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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import wait, iterate

#Test
tracemalloc.start()
class TestGxdImageSummary(unittest.TestCase):


    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.implicitly_wait(10)

    def test_default_sort_genes(self):
        """
        @status: Tests that the genes column sorts genes result correctly
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("pax6")
        genebox.send_keys(Keys.RETURN)
        time.sleep(2)
        #finds the Images tab and clicks it
        driver.find_element(By.ID, 'imagestab').click()
        #locates the genes column and lists the genes found
        genelist = driver.find_element(By.ID, 'imagesdata').find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-gene')
        items = genelist[15].find_elements(By.TAG_NAME, 'li')
        print(items[0].text)
        print(items[1].text)
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["Auts2", "Pax6"])
        
    def test_default_sort_assaytype(self):
        """
        @status: Tests the sort order for assay type using default sort
        sort order is gene first, assay type secondary
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("Igfbpl1")
        genebox.send_keys(Keys.RETURN)
        time.sleep(2)
        #finds the Images tab and clicks it
        driver.find_element(By.ID, 'imagestab').click()
        #finds the first row of data and verifies the Assay Type data
        assaylist = driver.find_element(By.ID, 'imagesdata').find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-assayType')
        items = assaylist[0].find_elements(By.TAG_NAME, 'li')
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["RNA in situ", "Immunohistochemistry", "Immunohistochemistry"])
        
    def test_default_sort_specimentype(self):
        """
        @status: Tests the sort order for specimen type using default sort
        sort order is gene first, assay type secondary
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("Tmem100")
        genebox.send_keys(Keys.RETURN)
        time.sleep(1)
        #finds the Images tab and clicks it
        driver.find_element(By.ID, "imagestab").click()
        #finds the first row of data and verifies the Specimen Type data
        typelist = driver.find_element(By.ID, 'imagesdata').find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-hybridization')
        items = typelist[0].find_elements(By.TAG_NAME, 'li')
        searchTextItems = iterate.getTextAsList(items)
        time.sleep(1)
        self.assertEqual(searchTextItems, ["section", "section from whole mount"])
                
    def test_gene_column_sort(self):
        """
        @status: Tests that the Gene column sort works correctly
        Gene column:
        * sort order is gene, then assay type
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("shh")
        genebox.send_keys(Keys.RETURN)
        time.sleep(1)
        #find the Images tab and clicks it
        driver.find_element(By.ID, 'imagestab').click()
        #finds the first row of data and verifies the genes column sort
        imagesdata = driver.find_element(By.ID, 'imagesdata')
        genelist = imagesdata.find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-gene')
        items = genelist[0].find_elements(By.TAG_NAME, 'li')
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["Arx", "Olig2", "Shh"])
        #find the genes header
        geneheader = imagesdata.find_element(By.CSS_SELECTOR, 'th.yui-dt-col-gene')
        #click the gene header column to re-sort
        geneheader.click()
        genelist = driver.find_element(By.ID, 'imagesdata').find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-gene')
        items = genelist[0].find_elements(By.TAG_NAME, 'li')
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["Ano1", "Cftr", "Shh"])
        
    def test_assaytype_column_sort(self):
        """
        @status: Tests that the assay type column sort works correctly
        Assay Type column:
        * Not applicable is not shown
        * sort order should be type (with not specified last), followed by assay type and gene
        * reverse order should still leave not specified last
        * blot assays are last by default
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("pax6")
        genebox.send_keys(Keys.RETURN)
        time.sleep(2)
        #find the Image tab and click it
        driver.find_element(By.ID, 'imagestab').click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'imagesdata'))):
            print('Images Tab details loaded')
        assaylist = driver.find_element(By.ID, 'imagesdata').find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-assayType')
        items = assaylist[0].find_elements(By.TAG_NAME, 'li')
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["Immunohistochemistry", "Immunohistochemistry"])
        assayheader = driver.find_element(By.ID, 'imagesdata').find_element(By.CSS_SELECTOR, 'th.yui-dt-col-assayType')
        #click the gene header column to re-sort
        assayheader.click()
        #time.sleep(1)
        #find the second row of data and verify the assay type
        assaylist = driver.find_element(By.ID, 'imagesdata').find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-assayType')
        items = assaylist[2].find_elements(By.TAG_NAME, 'li')
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["RT-PCR"])
    
    def test_specimentype_column_sort(self):
        """
        @status: Tests that the specimen type column sort works correctly
        The order for the specimen type sort is the order in the EI menu:
        *whole mount
        *section
        *section from whole mount
        *optical section
        *not specified
        *blots
        
        Reverse would be specified as:
        *optical section
        *section from whole mount
        *section
        *whole mount
        *not specified
        *blots
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("hoxa13")
        genebox.send_keys(Keys.RETURN)
        time.sleep(2)
        #find the Image tab and click it
        driver.find_element(By.ID, 'imagestab').click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'imagesdata'))):
            print('Images Tab details loaded')
        #Find the first row of data and verify the specimen type
        typelist = driver.find_element(By.ID, 'imagesdata').find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-hybridization')
        items = typelist[0].find_elements(By.TAG_NAME, 'li')
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["section", "section"])
        specimenheader = driver.find_element(By.ID, 'imagesdata').find_element(By.CSS_SELECTOR, 'th.yui-dt-col-hybridization')
        #click the gene header column to sort
        specimenheader.click()
        assaylist = driver.find_element(By.ID, 'imagesdata').find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-hybridization')
        items = assaylist[0].find_elements(By.TAG_NAME, 'li')
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["whole mount"])
            
                
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxdImageSummary))
    return suite
        
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
    