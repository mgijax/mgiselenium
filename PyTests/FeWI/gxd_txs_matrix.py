'''
Created on Nov 2, 2017

@author: jeffc
@attention: Beginning  test for Tissue X Stage Matrix
'''

import unittest
import time
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
import config

#Tests
tracemalloc.start()
class TestGXDTissueStageMatrix(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()

    def test_structure_names_sort(self):
        """
        @status: Tests that the high level anatomy terms are displayed in the correct order
        @attention: the time sleeps need to be replaced by expected conditions code
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        #driver.get(config.PUBLIC_URL + "/gxd")
        stagebox = driver.find_element(By.NAME, 'vocabTerm')
        # put your vocabulary term to search in the box
        stagebox.send_keys("mouse")
        stagebox.send_keys(Keys.RETURN)
        #wait.forAjax(driver)
        #find the Tissue x Stage Matrix tab
        tissuestagetab = driver.find_element(By.ID, 'stagegridtab')
        time.sleep(2)
        #click the Tissue x Stage Matrix tab
        tissuestagetab.click()
        time.sleep(5)
        #find the Anatomical systems high level terms
        termslist = driver.find_element(By.ID, 'stagegriddata').find_element(By.ID, 'rowGroupInner')
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('extraembryonic component', searchTextItems)
        self.assertIn('body fluid or substance', searchTextItems)
        self.assertIn('body region', searchTextItems)
        self.assertIn('cavity or lining', searchTextItems)
        self.assertIn('conceptus', searchTextItems)
        self.assertIn('early embryo', searchTextItems)
        self.assertIn('embryo', searchTextItems)
        self.assertIn('germ layer', searchTextItems)
        self.assertIn('organ', searchTextItems)
        self.assertIn('organ system', searchTextItems)
        self.assertIn('tissue', searchTextItems)
        self.assertIn('umbilical or vitelline vessel', searchTextItems)
        
    def test_anat_terms_results(self):
        """
        @status: Tests the correct anatomy terms and Theiler stages are returned for a simple gene search
        @attention: the time sleeps need to be replaced by expected conditions code
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        #driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("Psmb2")
        genebox.send_keys(Keys.RETURN)
        #find the Tissue x Stage Matrix tab
        tissuestagetab = driver.find_element(By.ID, "stagegridtab")
        time.sleep(1)
        #click the Tissue x Matrix tab
        tissuestagetab.click()
        
        time.sleep(2)
        #find the Anatomical Terms column
        termslist = driver.find_element(By.ID, "stagegriddata").find_element(By.ID, 'rowGroupInner')
        items = termslist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('mouse', searchTextItems)
        self.assertIn('embryo', searchTextItems)
        self.assertIn('extraembryonic component', searchTextItems)
        self.assertIn('organ system', searchTextItems)
        self.assertIn('musculoskeletal system', searchTextItems)
        #find the Anatomical Terms column
        termslist = driver.find_element(By.ID, "stagegriddata").find_element(By.ID, 'colGroupInner')
        items = termslist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('TS11', searchTextItems)
        self.assertIn('TS23', searchTextItems)
        
        
    def test_default_sort_specimentype(self):
        """
        @status: Tests the sort order for specimen type using default sort
        sort order is gene first, assay type secondary
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        #driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("Tmem100")
        genebox.send_keys(Keys.RETURN)
        #find the Image tab
        imagetab = driver.find_element(By.ID, "imagestab")
        time.sleep(1)
        #click the image tab
        imagetab.click()
        #wait.forAjax(driver)
        time.sleep(1)
        typelist = driver.find_element(By.ID, "imagesdata").find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-hybridization')
        items = typelist[0].find_elements(By.TAG_NAME, "li")
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
        #driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("shh")
        genebox.send_keys(Keys.RETURN)
        #find the Image tab
        imagetab = driver.find_element(By.ID, "imagestab")
        time.sleep(1)
        #click the image tab
        imagetab.click()
        wait.forAjax(driver)
        time.sleep(1)
        
        imagesdata = driver.find_element(By.ID, "imagesdata")
        genelist = imagesdata.find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-gene')
        items = genelist[0].find_elements(By.TAG_NAME, "li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["Arx", "Olig2", "Shh"])
        geneheader = imagesdata.find_element(By.CSS_SELECTOR, 'th.yui-dt-col-gene')
        #click the gene header column to sort
        geneheader.click()
        #wait.forAjax(driver)
        time.sleep(2)
        genelist = driver.find_element(By.ID, "imagesdata").find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-gene')
        time.sleep(2)
        items = genelist[0].find_elements(By.TAG_NAME, "li")
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
        #driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("pax6")
        genebox.send_keys(Keys.RETURN)
        #find the Image tab
        imagetab = driver.find_element(By.ID, "imagestab")
        time.sleep(1)
        #click the image tab
        imagetab.click()
        wait.forAjax(driver)
        time.sleep(1)
        assaylist = driver.find_element(By.ID, "imagesdata").find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-assayType')
        items = assaylist[0].find_elements(By.TAG_NAME, "li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["Immunohistochemistry", "Immunohistochemistry"])
        assayheader = driver.find_element(By.ID, "imagesdata").find_element(By.CSS_SELECTOR, 'th.yui-dt-col-assayType')
        #click the gene header column to sort
        assayheader.click()
        wait.forAjax(driver)
        time.sleep(2)
        assaylist = driver.find_element(By.ID, "imagesdata").find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-assayType')
        items = assaylist[2].find_elements(By.TAG_NAME, "li")
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
        #driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("hoxa13")
        genebox.send_keys(Keys.RETURN)
        #find the Image tab
        imagetab = driver.find_element(By.ID, "imagestab")
        time.sleep(3)
        #click the image tab
        imagetab.click()
        wait.forAjax(driver)
        time.sleep(3)
        typelist = driver.find_element(By.ID, "imagesdata").find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-hybridization')
        items = typelist[0].find_elements(By.TAG_NAME, "li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["section", "section"])
        specimenheader = driver.find_element(By.ID, "imagesdata").find_element(By.CSS_SELECTOR, 'th.yui-dt-col-hybridization')
        #click the gene header column to sort
        specimenheader.click()
        wait.forAjax(driver)
        time.sleep(2)
        assaylist = driver.find_element(By.ID, "imagesdata").find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-hybridization')
        items = assaylist[0].find_elements(By.TAG_NAME, "li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["whole mount"])
            
                
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGXDTissueStageMatrix))
    return suite
        
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
    