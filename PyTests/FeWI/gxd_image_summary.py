'''
Created on Feb 22, 2016

@author: jeffc
A work in progress, bringing back data but now need to figure how to apply it.
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,os.path
from util import wait, iterate
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import DEV_URL

class TestImageSummary(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox() 


    def test_default_sort_genes(self):
        """
        @status: Tests that the genes column sorts genes result correctly
        """
        driver = self.driver
        driver.get(config.DEV_URL + "/gxd")
        genebox = driver.find_element_by_name('nomenclature')
        # put your marker symbol
        genebox.send_keys("pax6")
        genebox.send_keys(Keys.RETURN)
        #find the Image tab
        imagetab = driver.find_element_by_id("imagestab")
        #click the image tab
        imagetab.click()
        wait.forAjax(driver)
        genelist = driver.find_element_by_id("imagesdata").find_elements_by_class_name('yui-dt-col-gene')
        items = genelist[17].find_elements_by_tag_name("li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["Gsx2", "Nkx2-1", "Pax6"])
        
    def test_default_sort_assaytype(self):
        """
        @status: Tests the sort order for assay type using default sort
        sort order is gene first, assay type secondary
        """
        driver = self.driver
        driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element_by_name('nomenclature')
        # put your marker symbol
        genebox.send_keys("Igfbpl1")
        genebox.send_keys(Keys.RETURN)
        #find the Image tab
        imagetab = driver.find_element_by_id("imagestab")
        #click the image tab
        imagetab.click()
        wait.forAjax(driver)
        assaylist = driver.find_element_by_id("imagesdata").find_elements_by_class_name('yui-dt-col-assayType')
        items = assaylist[1].find_elements_by_tag_name("li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["RNA in situ", "Immunohistochemistry", "Immunohistochemistry"])
        
    def test_default_sort_specimentype(self):
        """
        @status: Tests the sort order for specimen type using default sort
        sort order is gene first, assay type secondary
        """
        driver = self.driver
        driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element_by_name('nomenclature')
        # put your marker symbol
        genebox.send_keys("Tmem100")
        genebox.send_keys(Keys.RETURN)
        #find the Image tab
        imagetab = driver.find_element_by_id("imagestab")
        #click the image tab
        imagetab.click()
        wait.forAjax(driver)
        typelist = driver.find_element_by_id("imagesdata").find_elements_by_class_name('yui-dt-col-hybridization')
        items = typelist[1].find_elements_by_tag_name("li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["section", "section from whole mount"])
                
    def test_gene_column_sort(self):
        """
        @status: Tests that the Gene column sort works correctly
        Gene column:
        * sort order is gene, then assay type
        """
        driver = self.driver
        driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element_by_name('nomenclature')
        # put your marker symbol
        genebox.send_keys("shh")
        genebox.send_keys(Keys.RETURN)
        #find the Image tab
        imagetab = driver.find_element_by_id("imagestab")
        #click the image tab
        imagetab.click()
        wait.forAjax(driver)
        
        imagesdata = driver.find_element_by_id("imagesdata")
        genelist = imagesdata.find_elements_by_class_name('yui-dt-col-gene')
        items = genelist[1].find_elements_by_tag_name("li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["Bmp4", "Shh"])
        geneheader = imagesdata.find_element_by_css_selector('th.yui-dt-col-gene')
        #click the gene header column to sort
        geneheader.click()
        time.sleep(3)
        genelist = driver.find_element_by_id("imagesdata").find_elements_by_class_name('yui-dt-col-gene')
        items = genelist[1].find_elements_by_tag_name("li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["Arx", "Shh"])
        
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
        driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element_by_name('nomenclature')
        # put your marker symbol
        genebox.send_keys("pax6")
        genebox.send_keys(Keys.RETURN)
        #find the Image tab
        imagetab = driver.find_element_by_id("imagestab")
        #click the image tab
        imagetab.click()
        wait.forAjax(driver)
        assaylist = driver.find_element_by_id("imagesdata").find_elements_by_class_name('yui-dt-col-assayType')
        items = assaylist[1].find_elements_by_tag_name("li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["Immunohistochemistry", "Immunohistochemistry"])
        assayheader = driver.find_element_by_id("imagesdata").find_element_by_css_selector('th.yui-dt-col-assayType')
        #click the gene header column to sort
        assayheader.click()
        time.sleep(3)
        assaylist = driver.find_element_by_id("imagesdata").find_elements_by_class_name('yui-dt-col-assayType')
        items = assaylist[1].find_elements_by_tag_name("li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["RNase protection"])
    
    def test_specimentype_column_sort(self):
        """
        @status: Tests that the specimen type column sort works correctly
        The order for the spcimen type sort is the order in the EI menu:
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
        driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element_by_name('nomenclature')
        # put your marker symbol
        genebox.send_keys("hoxa13")
        genebox.send_keys(Keys.RETURN)
        #find the Image tab
        imagetab = driver.find_element_by_id("imagestab")
        #click the image tab
        imagetab.click()
        wait.forAjax(driver)
        typelist = driver.find_element_by_id("imagesdata").find_elements_by_class_name('yui-dt-col-hybridization')
        items = typelist[1].find_elements_by_tag_name("li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["section", "section"])
        specimenheader = driver.find_element_by_id("imagesdata").find_element_by_css_selector('th.yui-dt-col-hybridization')
        #click the gene header column to sort
        specimenheader.click()
        time.sleep(3)
        assaylist = driver.find_element_by_id("imagesdata").find_elements_by_class_name('yui-dt-col-hybridization')
        items = assaylist[1].find_elements_by_tag_name("li")
        searchTextItems = iterate.getTextAsList(items)
        self.assertEqual(searchTextItems, ["whole mount"])
    
        
        
           
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestImageSummary))
    return suite
        
if __name__ == "__main__":
    unittest.main() 
    
