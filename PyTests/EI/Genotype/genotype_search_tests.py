'''
Created on Dec 19, 2019
These are tests that check the searching options of the Genotype module
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import HtmlTestRunner
import json
import sys,os.path
from test.test_base64 import BaseXYTestCase
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests

class TestEiGenotypeSearch(unittest.TestCase):
    """
    @status Test Genotype searching, etc
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/genotype")
    
    def tearDown(self):
        self.driver.close()

    def testGenoStrainSearch(self):
        """
        @Status tests that a basic genotype strain search works
        @see pwi-geno-search-1
        """
        driver = self.driver
        #finds the Strain field and enters a strain w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "strain").send_keys('129.B6-Adamts13%')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        an_table = self.driver.find_element(By.ID, 'allelePairTable')
        table = Table(an_table)
        #Iterate and print the table results
        header_cells = table.get_header_cells()
        headings = iterate.getTextAsList(header_cells)
        print(headings)
        #assert the headers are correct
        self.assertEqual(headings, ['', '#', 'Chr', 'Marker', 'Allele 1', 'Allele 2', 'State', 'Compound', 'Mutant 1', 'Mutant 2'])
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'alleleDetailNote')))
        #find the search results table first row of data
        mrk1 = driver.find_element(By.ID, 'markerSymbol-0').get_property('value')
        print(mrk1)
        al1 = driver.find_element(By.ID, 'allele1-0').get_property('value')
        print(al1)
        al2 = driver.find_element(By.ID, 'allele2-0').get_property('value')
        print(al2)
        state1 = driver.find_element(By.ID, 'pairState-0').get_property('value')#value should be 'string:847138' that equals Homozygous
        print(state1)
        cmpd1 = driver.find_element(By.ID, 'compound-0').get_property('value')#value should be 'string:847167' that equals Not Applicable
        print(cmpd1)        
        disply = driver.find_element(By.ID, 'alleleDetailNote').get_property('value')
        print(disply)
        #we are asserting the first row of data plus Allele Detail Display is correct
        self.assertEqual(mrk1, 'Adamts13')
        self.assertEqual(al1, 'Adamts13<s>')
        self.assertEqual(al2, 'Adamts13<s>')
        self.assertEqual(state1, 'string:847138')
        self.assertEqual(cmpd1, 'string:847167')
        self.assertEqual(disply, 'Adamts13<s>/Adamts13<s>\n')
        

    def testGenotypeCondTargetSearch(self):
        """
        @Status tests that a Conditionally Targeted = Yes search works
        @see pwi-geno-search-2
        """
        driver = self.driver
        #finds the Conditionally Targetted field and selects the Yes option, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "isConditional").send_keys('Yes')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'alleleDetailNote')))
        #find the Conditionally Targeted field and confirm it is Yes
        contar = driver.find_element(By.ID, 'isConditional').get_property('value')
        print(contar)
        #we are asserting the Conditionally Targeted field is Yes for the first result
        self.assertEqual(contar, 'string:1')#string:1 equals Yes
        
    def testGenoExistsCellLineSearch(self):
        """
        @Status tests that a basic genotype exists as 'Cell Line' search works
        @see pwi-geno-search-3
        """
        driver = self.driver
        #finds the Genotype Exists as field and then selects the right option, then clicks the Search button
        driver.find_element(By.ID, "existsAs").send_keys('Cell Line')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'resultsTable')))
        #find the search Genotype Exista as field and get it's value
        exists0 = driver.find_element(By.ID, 'existsAs').get_property('value')
        print(exists0)    
        #we are asserting the Genotype Exists as field is correct, should be string:3982947 which is Cell Line
        self.assertEqual(exists0, 'string:3982947')
        
    def testGenoExistsChimericSearch(self):
        """
        @Status tests that a basic genotype exists as 'Chimeric' search works
        @see pwi-geno-search-4
        """
        driver = self.driver
        #finds the Genotype Exists as field and then selects the right option, then clicks the Search button
        driver.find_element(By.ID, "existsAs").send_keys('Chimeric')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'resultsTable')))
        #find the search Genotype Exista as field and get it's value
        exists0 = driver.find_element(By.ID, 'existsAs').get_property('value')
        print(exists0)    
        #we are asserting the Genotype Exists as field is correct, should be string:3982948 which is Chimeric
        self.assertEqual(exists0, 'string:3982948')

    def testGenoExistsMouseLineSearch(self):
        """
        @Status tests that a basic genotype exists as 'Mouse Line' search works
        @see pwi-geno-search-5
        """
        driver = self.driver
        #finds the Genotype Exists as field and then selects the right option, then clicks the Search button
        driver.find_element(By.ID, "existsAs").send_keys('Mouse Line')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'resultsTable')))
        #find the search Genotype Exista as field and get it's value
        exists0 = driver.find_element(By.ID, 'existsAs').get_property('value')
        print(exists0)    
        #we are asserting the Genotype Exists as field is correct, should be string:3982946 which is Mouse Line
        self.assertEqual(exists0, 'string:3982946')

    def testGenoExistsNotSpecifiedSearch(self):
        """
        @Status tests that a basic genotype exists as 'Not Specified' search works
        @see pwi-geno-search-6
        """
        driver = self.driver
        #finds the Genotype Exists as field and then selects the right option, then clicks the Search button
        driver.find_element(By.ID, "existsAs").send_keys('Not Specified')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'resultsTable')))
        #find the search Genotype Exista as field and get it's value
        exists0 = driver.find_element(By.ID, 'existsAs').get_property('value')
        print(exists0)    
        #we are asserting the Genotype Exists as field is correct, should be string:3982949 which is Not Specified
        self.assertEqual(exists0, 'string:3982949')


    def testGenoChromosomeSearch(self):
        """
        @Status tests that a basic Genotype Chromosome search works
        @see pwi-geno-search-7 
        """
        driver = self.driver
        #finds the Conditionally Targeted field and selects the No option, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "isConditional").send_keys('No')
        #finds the Chromosome field and select 'Y' 
        driver.find_element(By.ID, "chromsome-0").send_keys('X')        
        #You do not tab out of the Chromosome field or it will break the search because it tries to validate an empty marker field.
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'resultsTable')))
        #find the chromosone field of the first row
        chrom0 = driver.find_element(By.ID, 'chromsome-0').get_property('value')
        time.sleep(2)
        print(chrom0)
        #we are asserting the chromosome data is correct
        self.assertEqual(chrom0, 'string:X')

    def testGenoMrkSymSearch(self):
        """
        @Status tests that a basic genotype marker symbol search works
        @see pwi-geno-search-8
        """
        driver = self.driver
        #finds the Marker as field and then enters text, then clicks the Search button
        driver.find_element(By.ID, "markerSymbol-0").send_keys('Gata1')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'resultsTable')))
        #find the marker field and get it's value
        mrksym0 = driver.find_element(By.ID, 'markerSymbol-0').get_property('value')
        print(mrksym0)    
        #we are asserting the marker field is correct
        self.assertEqual(mrksym0, 'Gata1')

    def testGenoAlleleSearch(self):
        """
        @Status tests that a basic genotype allele symbol search works
        @see pwi-geno-search-9 *Tested 4-13-2020
        """
        driver = self.driver
        #finds the Allele 1 field and then enters text, then clicks the Search button
        driver.find_element(By.ID, "allele1-0").send_keys('Slc11a1<r>')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'resultsTable')))
        #find the Allele 1 field for row 1 and get it's value
        allsym1 = driver.find_element(By.ID, 'allele1-0').get_property('value')
        print(allsym1)    
        #we are asserting the allele1 field is correct
        self.assertEqual(allsym1, 'Slc11a1<r>')

    def testGenoStateSearch(self):
        """
        @Status tests that a basic State search works
        @see pwi-geno-search-10
        """
        driver = self.driver
        #finds the State field and then selects the right option, then clicks the Search button
        driver.find_element(By.ID, "pairState-0").send_keys('Homoplasmic')
        #You do not tab out of the State field or it will break the search because it tries to validate an empty marker field.
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'resultsTable')))
        #find the State field and get it's value
        state0 = driver.find_element(By.ID, 'pairState-0').get_property('value')
        print(state0)    
        #we are asserting the State field is correct, should be string:7107400 which is Homoplasmic
        self.assertEqual(state0, 'string:7107400')            

    def testGenoCompoundSearch(self):
        """
        @Status tests that a basic Compound search works
        @see pwi-geno-search-11
        """
        driver = self.driver
        #finds the Compound field and then selects the right option, then clicks the Search button
        driver.find_element(By.ID, "compound-0").send_keys('Top')
        #You do not tab out of the Compound field or it will break the search because it tries to validate an empty marker field.
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'resultsTable')))
        #find the Compound field and get it's value
        cmpd0 = driver.find_element(By.ID, 'compound-0').get_property('value')
        print(cmpd0)    
        #we are asserting the Compound field is correct, should be string:847165 which is Top
        self.assertEqual(cmpd0, 'string:847165')     

    def testGenoJnumSearch(self):
        """
        @Status tests that a basic J number search works
        @see pwi-geno-search-15
        """
        driver = self.driver
        #finds the J# field and then enters text, then clicks the Search button
        driver.find_element(By.ID, "jnum-0").send_keys('J:124405')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'jnum-0')))
        #find the J# field and get it's value
        jnumber = driver.find_element(By.ID, 'jnum-0').get_property('value')
        time.sleep(2)
        print(jnumber)    
        #we are asserting the J# field is correct
        self.assertEqual(jnumber, 'J:124405')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiGenotypeSearch))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
    