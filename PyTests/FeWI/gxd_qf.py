'''
Created on Oct 19, 2016
This set of tests verifies items found on the Gene Expression query form page
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
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

class TestGXDQF(unittest.TestCase):


    def setUp(self):
    
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/gxd/")
        self.driver.implicitly_wait(10)

    def test_ribbon_locations(self):
        '''
        @status This test verifies the ribbons are being displayed in the correct order on the page.
        '''
        self.driver.find_element(By.ID, 'gxdQueryForm')
        genesribbon = self.driver.find_element(By.CSS_SELECTOR, 'tr.stripe1 > td.cat1Gxd')
        print(genesribbon.text)
        self.assertEqual(genesribbon.text, 'Genes', "heading is incorrect")
        genomelocation = self.driver.find_element(By.CSS_SELECTOR, 'tr.stripe2 > td.cat2Gxd')
        print(genomelocation.text)
        self.assertEqual(genomelocation.text, 'Genome location', "heading is incorrect")
        structurestage = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(4).stripe1 > td.cat1Gxd')
        print(structurestage.text)
        self.assertEqual(structurestage.text, 'Anatomical structure or stage', "heading is incorrect")
        mutantwt = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(5).stripe2 > td.cat2Gxd')
        print(mutantwt.text)
        self.assertEqual(mutantwt.text, 'Mutant / wild type', "heading is incorrect")
        assaytype = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(6).stripe1 > td.cat1Gxd')
        print(assaytype.text)
        self.assertEqual(assaytype.text, 'Assay types', "heading is incorrect")
        
    def test_no_normals(self):
        """
        @status: Tests that the genes tab does not return normals(like Adcy8) or genes with no expression(like Ankfn1)
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'vocabTerm')
        # Enter your phenotype
        genebox.send_keys("taste/olfaction")
        time.sleep(2)
        genebox.send_keys(Keys.RETURN)
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        #finds the Genes tab and clicks it
        driver.find_element(By.ID, 'genestab').click()
        time.sleep(2)
        #locates the genes column and lists the genes found
        genelist = driver.find_element(By.ID, 'genesdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-symbol')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        #assert that this gene is not returned since it is associated to a normal phenotype
        self.assertNotIn('Adcy8', searchTextItems, 'Gene Adcy8 is being returned!')   
        #assert that this gene is not returned since it has no expression annotations
        self.assertNotIn('Ankfn1', searchTextItems, 'Gene Ankfn1 is being returned!') 
        
        
    def test_specimen_mut_gene(self):
        """
        @status: Tests that the option "specimen mutated in Gene" option of the GXD query form works as expected
        @note: GXD-assay-4
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        #find the Specimens mutated in gene option of the Mutant/ Wild type section and click it and enter your gene
        driver.find_element_by_id('mutatedSpecimen').click()
        driver.find_element_by_id('mutatedIn').send_keys('Dppa3')
        #find the InSitu assays and Blot assays check boxes and uncheck them
        driver.find_element(By.CLASS_NAME, 'allInSitu').click()
        driver.find_element(By.ID, 'blotAll').click()
        #find the Whole Genome assays check box and click it
        driver.find_element(By.ID, 'wholeGenomeAll').click()
        #find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        #finds the Assays tab and clicks it
        driver.find_element(By.ID, 'assaystab').click()
        time.sleep(2)
        #locates the References column and lists the references found
        reflist = driver.find_element(By.ID, 'assaysdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = reflist.find_elements(By.CLASS_NAME, 'yui-dt-col-reference')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        time.sleep(2)
        #assert that the Reference column holds the correct reference
        self.assertEqual(searchTextItems, ['E-MTAB-5210 Transcription profiling of wild type and Stella knockout oocytes, wild type and Stella maternal/zygotic knockout embryos to study to the role of Stella in early mouse development'])     
        
    def test_specimen_wild_type_only(self):
        """
        @status: Tests that the option "Wild type specimens only" option of the GXD query form works as expected
        @note GXD-assay-5
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        #find the Detected in option of the Anatomical structure or stage section and click it
        driver.find_element_by_id('detected1').click()
        #find the Wild type specimens only option in the Mutant/wild type section and click it
        driver.find_element_by_id('isWildType').click()
        #find the InSitu assays and Blot assays check boxes and uncheck them
        driver.find_element(By.CLASS_NAME, 'allInSitu').click()
        driver.find_element(By.ID, 'blotAll').click()
        #find the Whole Genome assays check box and click it
        driver.find_element(By.ID, 'wholeGenomeAll').click()
        #find the search button and click it
        #find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        #finds the Assays tab and clicks it
        driver.find_element(By.ID, 'assaystab').click()
        time.sleep(2)
        #locates the gene column and lists the gene found
        genelist = driver.find_element(By.ID, 'assaysdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-gene')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        #assert that the Gene column holds the text "Whole Genome"
        assert "Whole Genome" in searchTextItems  
        time.sleep(2)
        #locates the assay type column and lists the assay types found
        assaylist = driver.find_element(By.ID, 'assaysdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = assaylist.find_elements(By.CLASS_NAME, 'yui-dt-col-assayType')
        searchTextItems1 = iterate.getTextAsList(items)
        print(searchTextItems1)
        #assert that the Assay Type column holds the text "RNA-Seq"
        assert "RNA-Seq" in searchTextItems1  
                   
        
        
        
    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'TestGXDQF.testName']
    unittest.main()                