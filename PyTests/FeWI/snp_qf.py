'''
Created on Sep 7, 2018
This set of tests verifies the SNP query form
@author: jeffc
'''

import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
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

class TestSnpQF(unittest.TestCase):


    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/snp")
        self.driver.implicitly_wait(10)

    def test_search_1_ref_strain_nocompare(self):
        """
        @status: Tests that you can search for snps using a single reference strain
        @note: snp-qf-gene-3 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        genesearchbox = driver.find_element(By.ID, 'nomen')
        # Enter your Gene symbol
        genesearchbox.send_keys("shh")
        time.sleep(2)
        #find the Yes button for comparing to one or more Reference strains and click it
        self.driver.find_element(By.XPATH, ".//input[@name='referenceMode' and @value='yes']").click()        
        #time.sleep(2)
        #driver.find_element(By.XPATH, ".//input[@name='selectedStrains' and @value='A/J']").click()
        time.sleep(2)
        #find the Reference box for strain A/J and click it
        elem = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/J']"));
        driver.execute_script("arguments[0].click();", elem)
        #find the search button and click it
        driver.find_element(By.ID, 'geneSearch').click()
        time.sleep(2)
        #locates the SNP summary table and verify the rs IDs returned are correct
        snp_table = Table(self.driver.find_element_by_id("snpSummaryTable"))
        cells = snp_table.get_column_cells("SNP ID\n(dbSNP Build 142)")
        print(iterate.getTextAsList(cells))     
        rsReturned = iterate.getTextAsList(cells)        
        #asserts that the following rs IDs are returned
        self.assertEqual(['SNP ID\n(dbSNP Build 142)', 'rs33674412\ndbSNP | MGI SNP Detail', 'rs108198781\ndbSNP | MGI SNP Detail', 'rs108778547\ndbSNP | MGI SNP Detail', 'rs29729942\ndbSNP | MGI SNP Detail', 'rs33485416\ndbSNP | MGI SNP Detail', 'rs33068028\ndbSNP | MGI SNP Detail', 'rs29682823\ndbSNP | MGI SNP Detail', 'rs33133952\ndbSNP | MGI SNP Detail', 'rs33181672\ndbSNP | MGI SNP Detail', 'rs48089243\ndbSNP | MGI SNP Detail', 'rs33541793\ndbSNP | MGI SNP Detail', 'rs33746193\ndbSNP | MGI SNP Detail', 'rs33214222\ndbSNP | MGI SNP Detail', 'rs33285952\ndbSNP | MGI SNP Detail', 'rs33560337\ndbSNP | MGI SNP Detail', 'rs33259009\ndbSNP | MGI SNP Detail', 'rs29727180\ndbSNP | MGI SNP Detail', 'rs33735948\ndbSNP | MGI SNP Detail', 'rs33682898\ndbSNP | MGI SNP Detail', 'rs51528487\ndbSNP | MGI SNP Detail', 'rs29676307\ndbSNP | MGI SNP Detail', 'rs33455132\ndbSNP | MGI SNP Detail', 'rs29562835\ndbSNP | MGI SNP Detail', 'rs33112153\ndbSNP | MGI SNP Detail', 'rs29530423\ndbSNP | MGI SNP Detail', 'SNP ID\n(dbSNP Build 142)', 'rs29733217\ndbSNP | MGI SNP Detail'], rsReturned) # this is all the data returned from the SNP ID column
 
    def test_search_1_ref_strain_different(self):
        """
        @status: Tests that you can search for snps using a single reference strain and the option Different from the reference strain
        @note: snp-qf-gene-3 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        genesearchbox = driver.find_element(By.ID, 'nomen')
        # Enter your Gene symbol
        genesearchbox.send_keys("shh")
        time.sleep(2)
        #find the Yes button for comparing to one or more Reference strains and click it
        self.driver.find_element(By.XPATH, ".//input[@name='referenceMode' and @value='yes']").click()        
        time.sleep(2)
        #find the Reference box for strain A/J and click it
        elem = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/J']"));
        driver.execute_script("arguments[0].click();", elem)
        #find the search button and click it
        driver.find_element(By.ID, 'geneSearch').click()
        time.sleep(2)
        driver.find_element(By.ID, 'alleleAgreementFilter').click()
        #find the allele agreement filter for "All reference strains agree and all comparison strains differ with reference" and select it
        alleleFil = driver.find_element(By.XPATH, (".//input[@name='alleleAgreementFilter' and @value='All reference strains agree and all comparison strains differ from reference']"));
        driver.execute_script("arguments[0].click();", alleleFil)
        #find and click the Filter button
        driver.find_element(By.ID, 'yui-gen0-button').click()
        time.sleep(2)
        #locates the SNP summary table and verify the rs IDs returned are correct
        snp_table = Table(self.driver.find_element_by_id("snpSummaryTable"))
        cells = snp_table.get_column_cells("SNP ID\n(dbSNP Build 142)")
        print(iterate.getTextAsList(cells))     
        rsReturned = iterate.getTextAsList(cells)        
        #asserts that the following rs IDs are returned
        self.assertEqual(['SNP ID\n(dbSNP Build 142)', 'rs108198781\ndbSNP | MGI SNP Detail'], rsReturned) # this is all the data returned from the SNP ID column
        
    def test_search_1_ref_strain_same(self):
        """
        @status: Tests that you can search for snps using a single reference strain and the Allele Agreement filter All reference strains agree and all comparison strains agree with reference 
        @note: snp-qf-gene-3 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        genesearchbox = driver.find_element(By.ID, 'nomen')
        # Enter your Gene symbol
        genesearchbox.send_keys("shh")
        time.sleep(4)
        #find the Yes button for comparing to one or more Reference strains and click it
        self.driver.find_element(By.XPATH, ".//input[@name='referenceMode' and @value='yes']").click()        
        time.sleep(2)
        #find the Reference box for strain A/J and click it
        elem = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/J']"));
        driver.execute_script("arguments[0].click();", elem)
        #find the search button and click it
        driver.find_element(By.ID, 'geneSearch').click()
        time.sleep(2)
        #find the allele agreement filter for "All reference strains agree and all comparison strains agree with reference" and select it
        driver.find_element(By.ID, 'alleleAgreementFilter').click()
        time.sleep(2)
        alleleFil = driver.find_element(By.XPATH, (".//input[@name='alleleAgreementFilter' and @value='All reference strains agree and all comparison strains agree with reference']"));
        driver.execute_script("arguments[0].click();", alleleFil)
        #find and click the Filter button
        driver.find_element(By.ID, 'yui-gen0-button').click()
        time.sleep(2)
        #locates the SNP summary table and verify the rs IDs returned are correct
        snp_table = Table(self.driver.find_element_by_id("snpSummaryTable"))
        cells = snp_table.get_column_cells("SNP ID\n(dbSNP Build 142)")
        print(iterate.getTextAsList(cells))     
        rsReturned = iterate.getTextAsList(cells)        
        #asserts that the following rs IDs are returned
        
        self.assertEqual(['SNP ID\n(dbSNP Build 142)', 'rs51528487\ndbSNP | MGI SNP Detail'], rsReturned) # this is all the data returned from the SNP ID column
      
        
    def test_search_multi_ref_strain(self):
        """
        @status: Tests that you can search for snps using multiple reference strains and selective comparison strains
        this example is actually biologically significant.  All of the Reference strains in this example show what is 
        called the AH+ phenotype (for Ahr), while all of the comparison strains show the AH- phenotype (for Ahr).
        The SNPs returned are all candidates for the genetic variation that defines the AH+ vs. AH- phenotype.
        @note: snp-qf-gene-4 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        genesearchbox = driver.find_element(By.ID, 'nomen')
        # Enter your Gene symbol
        genesearchbox.send_keys("Ahr")
        time.sleep(2)
        #find the Yes button for comparing to one or more Reference strains and click it
        self.driver.find_element(By.XPATH, ".//input[@name='referenceMode' and @value='yes']").click()        
        #find the comparison strains button for "Clear All" and click it
        driver.find_element(By.ID, 'deselectButton').click()
        time.sleep(2)      
        #find the Comparison box for strain 129S1/SvImJ and click it
        comelem = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='129S1/SvImJ']"));
        driver.execute_script("arguments[0].click();", comelem)
        #find the Comparison box for strain AKR/J and click it
        comelem1 = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='AKR/J']"));
        driver.execute_script("arguments[0].click();", comelem1)
        #find the Comparison box for strain DBA/2J and click it
        comelem2 = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='DBA/2J']"));
        driver.execute_script("arguments[0].click();", comelem2)
        #find the Comparison box for strain NZB/B1NJ and click it
        comelem3 = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='NZB/BlNJ']"));
        driver.execute_script("arguments[0].click();", comelem3)
        #find the Comparison box for strain NZW/LacJ and click it
        comelem4 = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='NZW/LacJ']"));
        driver.execute_script("arguments[0].click();", comelem4)
              
        #find the Reference box for strain A/Hej and click it
        refelem = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/HeJ']"));
        driver.execute_script("arguments[0].click();", refelem)
        #find the Reference box for strain A/J and click it
        refelem1 = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/J']"));
        driver.execute_script("arguments[0].click();", refelem1)
        #find the Reference box for strain B10.D2-Hc<0> H2<d> H2-T18<c>/oSnJ and click it
        refelem2 = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='B10.D2-Hc<0> H2<d> H2-T18<c>/oSnJ']"));
        driver.execute_script("arguments[0].click();", refelem2)
        #find the Reference box for strain BALB/cJ and click it
        refelem3 = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='BALB/cJ']"));
        driver.execute_script("arguments[0].click();", refelem3)
        #find the Reference box for strain C3H/HeJ and click it
        refelem4 = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='C3H/HeJ']"));
        driver.execute_script("arguments[0].click();", refelem4)
        #find the Reference box for strain C57BL/6J and click it
        refelem5 = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='C57BL/6J']"));
        driver.execute_script("arguments[0].click();", refelem5)
        
        #find the search button and click it
        driver.find_element(By.ID, 'geneSearch').click()
        time.sleep(2)
        driver.find_element(By.ID, 'alleleAgreementFilter').click()
        #find the Allele Agreement filter, select it and choose the option "All reference strains agree and all comparison strains differ from reference".
        alleleFil = driver.find_element(By.XPATH, (".//input[@name='alleleAgreementFilter' and @value='All reference strains agree and all comparison strains differ from reference']"));
        driver.execute_script("arguments[0].click();", alleleFil)
        driver.find_element(By.ID, 'yui-gen0-button').click()
        #locates the SNP summary table and verify the rs IDs returned are correct, strains returned are correct
        snp_table = Table(self.driver.find_element_by_id("snpSummaryTable"))
        cells = snp_table.get_column_cells("SNP ID\n(dbSNP Build 142)")
        print(iterate.getTextAsList(cells))     
        rsReturned = iterate.getTextAsList(cells)        
        #asserts that the following rs IDs are returned
        self.assertEqual(['SNP ID\n(dbSNP Build 142)', 'rs3021544\ndbSNP | MGI SNP Detail', 'rs3021927\ndbSNP | MGI SNP Detail', 'rs3021928\ndbSNP | MGI SNP Detail', 'rs3021931\ndbSNP | MGI SNP Detail', 'rs3021868\ndbSNP | MGI SNP Detail'], rsReturned) # this is all the data returned from the SNP ID column currently 5 IDs as of 9/1218
        cells1 = snp_table.get_header_cells()
        print(iterate.getTextAsList(cells1))  
        #print cells1[14].text   
        self.assertEqual(cells1[5].text, 'A/HeJ', 'The first ref strain is not A/HeJ')
        self.assertEqual(cells1[6].text, 'A/J', 'The second ref strain is not A/J')
        self.assertEqual(cells1[7].text, 'B10.D2-Hc<0> H2<d> H2-T18<c>/oSnJ', 'The third ref strain is not B10.D2-Hc<0> H2<d> H2-T18<c>/oSnJ')
        self.assertEqual(cells1[8].text, 'BALB/cJ', 'The fourth ref strain is not BALB/cJ')
        self.assertEqual(cells1[9].text, 'C3H/HeJ', 'The fifth ref strain is not C3H/HeJ')
        self.assertEqual(cells1[10].text, 'C57BL/6J', 'The sixth ref strain is not C57BL/6J')
        self.assertEqual(cells1[11].text, '129S1/SvImJ', 'The first comparison strain is not 129S1/SvImJ')
        self.assertEqual(cells1[12].text, 'AKR/J', 'The second comparison strain is not AKR/J')
        self.assertEqual(cells1[13].text, 'DBA/2J', 'The third comparison strain is not DBA/2J')
        self.assertEqual(cells1[14].text, 'NZB/BlNJ', 'The fourth comparison strain is not NZB/B1NJ')
        self.assertEqual(cells1[15].text, 'NZW/LacJ', 'The fifth comparison strain is not NZW/LacJ')
           
        
    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSnpQF))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))        