'''
Created on Mar 21, 2019
These tests verify the various copy functions within the Marker module.
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
#from.selenium.webdriver.support.color import Color
import HtmlTestRunner
import json
import sys,os.path
from selenium.webdriver.support.color import Color
from selenium.webdriver.remote.webelement import WebElement
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests

class TestEiVariantCopy(unittest.TestCase):
    """
    @status Test the Copy functions of the variant module
    @attention: under construction
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        #self.form.get_module("bhmgipwi02lt:5099/pwi/edit/variant/")
        self.form.get_module(config.TEST_PWI_URL + "/edit/variant/")
        username = self.driver.find_element(By.NAME, 'user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = self.driver.find_element(By.NAME, 'password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = self.driver.find_element(By.NAME, "submit") #Find the Login button
        submit.click() #click the login button
    
    def tearDown(self):
        self.driver.close()
        
    def testVarCopyAll(self):
        """
        @Status tests that the Copy All function works
        @see pwi-var-copy-1 **under construction**
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters a symbol
        driver.find_element(By.ID, "alleleID").send_keys('MGI:2670437')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print(symbols)
        #assert all the correct symbols are returned
        self.assertEqual(symbols, ['Rora<tmgc26>'])
        
    def testVarCopyCoords1(self):
        """
        @Status tests that the Copy Coords function works for sourced Genomic
        @see pwi-var-copy-2
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters a ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:5563413')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        sgbld = driver.find_element(By.ID, "srcDnaVersion").get_attribute("value")#locate the sourced Genomic Genome Build field
        print(sgbld)
        #checks if the Genomic sequence already exists, if not it will add it along with the other sequence data
        if "GRCm38" not in self.driver.find_element(By.ID, "srcDnaVersion").get_attribute("value"):
            print("Sourced Genomic Version field is empty")
            driver.find_element(By.ID, "srcDnaVersion").send_keys('GRCm38(mm10)')#add sourced Genomic data
            time.sleep(2)
            driver.find_element(By.ID, "srcDnaStart").send_keys('51782639')#add sourced Genomic start coordinate data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcDnaEnd").send_keys('51782639')#add sourced Genomic stop coordinate data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcDnaRefAllele").send_keys('A')#add sourced Genomic Reference Allele data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcDnaVarAllele").send_keys('T')#add sourced Genomic Variant Allele data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, 'updateVariantButton').click()#find the Modify button and click it
            WebDriverWait(driver, 10)
            
        WebDriverWait(driver, 10)
        sgbld = driver.find_element(By.ID, "srcDnaVersion").get_attribute("value")#locate the sourced Genomic Genome Build field again
        #assert the correct Version is in the Sourced Genomic Genome Build field
        self.assertEqual(sgbld, 'GRCm38')
        #Find the Sourced Genomic Coords button and click it
        driver.find_element(By.ID, 'cpGenomicCoord').click()
        WebDriverWait(driver, 10)
        
        cgbld = driver.find_element(By.ID, "curDnaVersion").get_attribute("value")#locate the curated Curated Genome Build field again
        time.sleep(4)
        #assert the correct Version is in the curated Genome Build field
        self.assertEqual(cgbld, 'GRCm38')   

        
    def testVarCopyCoords2(self):
        """
        @Status tests that the Copy Coords function works for sourced Transcript
        @see pwi-var-copy-2 
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters a ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:5563413')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        tid = self.driver.find_element(By.ID, "srcRnaID").get_attribute("value")
        print(tid)
        #checks if the transcript already exists, if not it will add it along with the other sequence data
        if "XM_006519628" not in self.driver.find_element(By.ID, "srcRnaID").get_attribute("value"):
            print("Sourced Transcript field is empty")
            driver.find_element(By.ID, "srcRnaID").send_keys('XM_006519628')#add sourced Transcript data
            time.sleep(2)
            driver.find_element(By.ID, "srcRnaStart").send_keys('23456')#add sourced Transcript start coordinate data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcRnaEnd").send_keys('23456')#add sourced Transcript stop coordinate data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcRnaRefAllele").send_keys('A')#add sourced Transcript Reference Allele data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcRnaVarAllele").send_keys('T')#add sourced Transcript Variant Allele data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, 'updateVariantButton').click()#find the Modify button and click it
            WebDriverWait(driver, 10)
            
        WebDriverWait(driver, 10)
        trans = driver.find_element(By.ID, "srcRnaID").get_attribute("value")#locate the sourced Transcript ID field again
        time.sleep(4)
        #assert the correct ID is in the Sourced Transcript ID field
        self.assertEqual(trans, 'XM_006519628')
        #Find the Sourced Transcript Coords button and click it
        driver.find_element(By.ID, 'cpTranscriptCoord').click()
        WebDriverWait(driver, 10)
        
        cur = driver.find_element(By.ID, "curRnaID").get_attribute("value")#locate the curated Transcript ID field again
        time.sleep(4)
        #assert the correct ID is in the curated Transcript ID field
        self.assertEqual(cur, 'XM_006519628')   

    def testVarCopyCoords3(self):
        """
        @Status tests that the Copy Coords function works for sourced Polypeptide
        @see pwi-var-copy-2 
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters a ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:5563413')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #checks if the Polypeptide already exists, if not it will add it along with the other sequence data
        if "Q8C2Q2" not in self.driver.find_element(By.ID, "srcProteinID").get_attribute("value"):
            print("Sourced Polypeptide field is empty")
            driver.find_element(By.ID, "srcProteinID").send_keys('Q8C2Q2')#add sourced Polypeptide data
            time.sleep(2)
            driver.find_element(By.ID, "srcProteinStart").send_keys('51782639')#add sourced Polypeptide start coordinate data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcProteinEnd").send_keys('51782639')#add sourced Polypeptide stop coordinate data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcProteinRefAllele").send_keys('A')#add sourced Polypeptide Reference Allele data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcProteinVarAllele").send_keys('T')#add sourced Polypeptide Variant Allele data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, 'updateVariantButton').click()#find the Modify button and click it
            WebDriverWait(driver, 10)
            
        WebDriverWait(driver, 10)
        spoly = driver.find_element(By.ID, "srcProteinID").get_attribute("value")#locate the sourced Polypeptide ID field again
        time.sleep(2)
        #assert the correct ID is in the Sourced Polypeptide ID field
        self.assertEqual(spoly, 'Q8C2Q2')
        #Find the Sourced Polypeptide Coords button and click it
        driver.find_element(By.ID, 'cpPolypeptideCoord').click()
        WebDriverWait(driver, 10)
        
        cpoly = driver.find_element(By.ID, "curProteinID").get_attribute("value")#locate the curated Polypeptide ID field again
        time.sleep(2)
        #assert the correct ID is in the curated Polypeptide ID field
        self.assertEqual(cpoly, 'Q8C2Q2')   

        
    def testVarCopyAlleles1(self):
        """
        @Status tests that the Copy Alleles function works for sourced Genomic
        @see pwi-var-copy-3
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters a ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:5547989')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        gid = self.driver.find_element(By.ID, "srcDnaVersion").get_attribute("value")
        print(gid)
        #checks if the Genomic sequence already exists, if not it will add it along with the other sequence data
        if "GRCm38" not in self.driver.find_element(By.ID, "srcDnaVersion").get_attribute("value"):
            print("Sourced Genomic Version field is empty")
            driver.find_element(By.ID, "srcDnaVersion").send_keys('GRCm38')#add sourced Genomic data
            time.sleep(2)
            driver.find_element(By.ID, "srcDnaStart").send_keys('47016337')#add sourced Genomic start coordinate data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcDnaEnd").send_keys('47016337')#add sourced Genomic stop coordinate data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcDnaRefAllele").send_keys('A')#add sourced Genomic Reference Allele data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcDnaVarAllele").send_keys('C')#add sourced Genomic Variant Allele data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, 'updateVariantButton').click()#find the Modify button and click it
            WebDriverWait(driver, 10)
            
        WebDriverWait(driver, 10)
        sall = driver.find_element(By.ID, "srcDnaRefAllele").get_attribute("value")#locate the sourced Reference Allele field again
        time.sleep(4)
        #assert the correct Version is in the Sourced Genomic Genome Build field
        self.assertEqual(sall, 'A')
        #Find the Sourced Genomic Alleles button and click it
        driver.find_element(By.ID, 'cpGenomicAlleles').click()
        WebDriverWait(driver, 10)
        
        cuall = driver.find_element(By.ID, "curDnaRefAllele").get_attribute("value")#locate the curated Reference Allele field again
        time.sleep(4)
        #assert the correct Version is in the curated Genome Build field
        self.assertEqual(cuall, 'A')   

        
    def testVarCopyAlleles2(self):
        """
        @Status tests that the Copy Alleles function works for sourced Transcript
        @see pwi-var-copy-3 
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters a ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:5547989')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        tid = self.driver.find_element(By.ID, "srcRnaID").get_attribute("value")
        print(tid)
        #checks if the transcript already exists, if not it will add it along with the other sequence data
        if "NM_009170" not in self.driver.find_element(By.ID, "srcRnaID").get_attribute("value"):
            print("Sourced Transcript field is empty")
            driver.find_element(By.ID, "srcRnaID").send_keys('NM_028966')#add sourced Transcript data
            time.sleep(2)
            driver.find_element(By.ID, "srcRnaStart").send_keys('123')#add sourced Transcript start coordinate data
            WebDriverWait(driver, 2)
            driver.find_element(By.ID, "srcRnaEnd").send_keys('123')#add sourced Transcript stop coordinate data
            WebDriverWait(driver, 2)
            driver.find_element(By.ID, "srcRnaRefAllele").send_keys('A')#add sourced Transcript Reference Allele data
            WebDriverWait(driver, 2)
            driver.find_element(By.ID, "srcRnaVarAllele").send_keys('T')#add sourced Transcript Variant Allele data
            WebDriverWait(driver, 2)
            #driver.find_element(By.ID, 'updateVariantButton').click()#find the Modify button and click it
            driver.find_element(By.ID, 'createVariantButton').click()#find the Modify button and click it
            WebDriverWait(driver, 2)
            
        WebDriverWait(driver, 10)
        transRef = driver.find_element(By.ID, "srcRnaRefAllele").get_attribute("value")#locate the sourced Transcript Reference Allele field again
        time.sleep(4)
        #assert the correct reference allele is in the Sourced Transcript Reference Allele field
        self.assertEqual(transRef, 'A')
        time.sleep(2)
        #Find the Sourced Transcript Alleles copy  button and click it
        driver.find_element(By.ID, 'cpTranscriptAlleles').click()
        WebDriverWait(driver, 10)
        
        curRef = driver.find_element(By.ID, "curRnaRefAllele").get_attribute("value")#locate the curated Transcript Reference Allele field again
        time.sleep(4)
        #assert the correct ID is in the curated Transcript ID field
        self.assertEqual(curRef, 'A')   

    def testVarCopyAlleles3(self):
        """
        @Status tests that the Copy Alleles function works for sourced Polypeptide
        @see pwi-var-copy-3 
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters a ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:5547989')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #checks if the Polypeptide already exists, if not it will add it along with the other sequence data
        if "NP_083242" not in self.driver.find_element(By.ID, "srcProteinID").get_attribute("value"):
            print("Sourced Polypeptide field is empty")
            driver.find_element(By.ID, "srcProteinID").send_keys('NP_083242')#add sourced Polypeptide data
            time.sleep(2)
            driver.find_element(By.ID, "srcProteinStart").send_keys('123')#add sourced Polypeptide start coordinate data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcProteinEnd").send_keys('123')#add sourced Polypeptide stop coordinate data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcProteinRefAllele").send_keys('A')#add sourced Polypeptide Reference Allele data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "srcProteinVarAllele").send_keys('T')#add sourced Polypeptide Variant Allele data
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, 'updateVariantButton').click()#find the Modify button and click it
            WebDriverWait(driver, 10)
            
        WebDriverWait(driver, 10)
        spolyRef = driver.find_element(By.ID, "srcProteinRefAllele").get_attribute("value")#locate the sourced Polypeptide Reference Allele field again
        time.sleep(2)
        #assert the correct Reference Allele is in the Sourced Polypeptide Reference Allele field
        self.assertEqual(spolyRef, 'A')
        #Find the Sourced Polypeptide Alleles button and click it
        driver.find_element(By.ID, 'cpPolypeptideAlleles').click()
        WebDriverWait(driver, 10)
        
        cpolyRef = driver.find_element(By.ID, "curProteinRefAllele").get_attribute("value")#locate the curated Polypeptide Reference Allele field again
        time.sleep(2)
        #assert the correct Reference Allele is in the curated Polypeptide Reference Allele field
        self.assertEqual(cpolyRef, 'A')   

    def testVarDupAllele(self):
        """
        @Status tests that the Duplicate Allele function works for the Variant Module
        @see pwi-var-copy-4
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters a ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:5547989')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #Find the Create button and verify it is inactive(disabled)
        self.assertFalse(driver.find_element(By.ID, 'createVariantButton').is_enabled(), "Create button is enabled")
        #Find the Duplicate Allele button and click it
        driver.find_element(By.ID, 'cpAllele').click()
            
        WebDriverWait(driver, 10)
        sstart = driver.find_element(By.ID, "srcDnaStart").get_attribute("value")#locate the sourced Genomic Start field
        time.sleep(4)
        #assert the Sourced Genomic Start field is empty
        self.assertEqual(sstart, '')
        #Find the Create button and verify it is active(enabled)
        self.assertTrue(driver.find_element(By.ID, 'createVariantButton').is_enabled(), "Create button is not enabled")
        
    def testVarDupVariant(self):
        """
        @Status tests that the Duplicate Variant function works for the Variant Module
        @see pwi-var-copy-5
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters a ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:5547989')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #Find the Create button and verify it is inactive(disabled)
        self.assertFalse(driver.find_element(By.ID, 'createVariantButton').is_enabled(), "Create button is enabled")
        #Find the Duplicate Variant button and click it
        driver.find_element(By.ID, 'cpVariant').click()
        WebDriverWait(driver, 10)
        Asym = driver.find_element(By.ID, "alleleSymbol").get_attribute('value')#locate the Allele Symbol field and get it's text
        #Assert the Allele Symbol field contains just the Marker symbol
        self.assertEqual(Asym, 'Samd4', 'The marker symbol is not correct!')
        sstart = driver.find_element(By.ID, "curDnaStart").get_attribute("value")#locate the curated Genomic Start field
        time.sleep(4)
        #assert the Curated Genomic Start field is correct
        self.assertEqual(sstart, '47016337')
        #Find the Create button and verify it is active(enabled)
        self.assertTrue(driver.find_element(By.ID, 'createVariantButton').is_enabled(), "Create button is not enabled")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiVariantCopy))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
                    
        