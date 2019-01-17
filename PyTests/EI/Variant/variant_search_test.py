'''
Created on Jan 14, 2019
Tests the searching features of the Variant module
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
import HTMLTestRunner
import json
import sys,os.pathfrom selenium.webdriver.support.color import Color

# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests

class TestVarSearch(unittest.TestCase):
    """
    @status Test Variant search fields
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        #self.form.get_module("bhmgipwi02lt:5099/pwi/edit/variant/")
        self.form.get_module(config.TEST_PWI_URL + "/edit/variant/")
    
    def tearDown(self):
        self.driver.close()
        
    def testVarAlleleIDSearch(self):
        """
        @Status tests that a basic Variant Allele ID search works
        @see pwi-var-search-1
        """
        driver = self.driver
        #finds the allele ID field and enters a symbol
        driver.find_element_by_id("alleleID").send_keys('MGI:2670437')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Rora<tmgc26>'])
        
    def testVarAlleleSymbolSearch(self):
        """
        @Status tests that a basic Variant Allele Symbol search works
        @see pwi-var-search-2
        """
        driver = self.driver
        #finds the allele symbol field and enters a symbol
        driver.find_element_by_id("alleleSymbol").send_keys('Cntn1<usl>')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Cntn1<usl>'])

    def testVarAlleleSymbolWildSearch(self):
        """
        @Status tests that a basic Variant Allele Symbol search using a wildcard works
        @see pwi-var-search-3
        """
        driver = self.driver
        #finds the allele symbol field and enters a symbol
        driver.find_element_by_id("alleleSymbol").send_keys('Cntn%')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Cntn1<usl>', 'Cntnap1<M1Btlr>'])

    def testVarRefSearch(self):
        """
        @Status tests that a basic variant reference search works
        @see pwi-var-search-4 
        """
        driver = self.driver
        #finds the references field and enters a J number
        driver.find_element_by_id("jnumIDs").send_keys('J:13651')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Cpe<fat>'])
        
    def testVarRefMultiSearch(self):
        """
        @Status tests that a variant multi reference search works
        @see pwi-var-search-5 
        """
        driver = self.driver
        #finds the history symbol field and enters a symbol
        driver.find_element_by_id("jnumIDs").send_keys('J:203032, J:13651')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Cntn1<usl>','Cpe<fat>'])
        
    def testVarChromosomeSearch(self):
        """
        @Status tests that a basic Chromosome search works
        @see pwi-var-search-6
        """
        driver = self.driver
        #finds the chromosome field and enters a chromosome
        driver.find_element_by_id("chromosome").send_keys('X')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Atp11c<m1Btlr>','Atp11c<m2Btlr>','Foxp3<m1Btlr>','Pou3f4<sdl>','Was<tm1Itl>','Was<tm2Itl>','Yipf6<M1Btlr>','Zic3<Ka>'])

    def testVarStrandSearch(self):
        """
        @Status tests that a basic Strand search works
        @see pwi-var-search-7 
        """
        driver = self.driver
        #finds the Strand field and enters a Strand
        driver.find_element_by_id("strand").send_keys('+')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row one through three
        row1 = table.get_row(0)
        row2 = table.get_row(1)
        row3 = table.get_row(2)
        print row1.text
        print row2.text
        print row3.text
        #assert that the first 3 search results are correct
        self.assertEqual(row1.text, 'Acan<b2b183Clo>')
        self.assertEqual(row2.text, 'Adamts6<b2b1879.1Clo>')
        self.assertEqual(row3.text, 'Adamts6<b2b2029Clo>')

    def testVarWithHGVSSearch(self):
        """
        @Status tests that a basic allele search returns HGVS data works
        @see pwi-var-search-8
        """
        driver = self.driver
        #finds the Allele ID field and enters an MGI ID
        driver.find_element_by_id("alleleID").send_keys('MGI:5705324')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the HGVS description field
        hgvs_data = self.driver.find_element_by_id("description").get_attribute('value')
        time.sleep(2)
        print hgvs_data
        #assert the hgvs data is correct
        self.assertEquals(hgvs_data, "Alk:NM_007439.2:c.3836G>A:p.(Arg1279Gln)")

    def testVarWithJnumSearch(self):
        """
        @Status tests that a basic allele search returns variant reference data works
        @see pwi-var-search-9
        """
        driver = self.driver
        #finds the Allele ID field and enters an MGI ID
        driver.find_element_by_id("alleleID").send_keys('MGI:5705324')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the Variant reference field
        var_jnum = self.driver.find_element_by_id("variantJnumIDs").get_attribute('value')
        time.sleep(2)
        print var_jnum
        #assert the variant reference data is correct
        self.assertEquals(var_jnum, "J:228124")

    def testVarStrandNegSearch(self):
        """
        @Status tests that a variant Strand negative search has  the stand always with a red background
        @see pwi-var-search-12 
        """
        driver = self.driver
        #finds the Strand field and enters a Strand
        driver.find_element_by_id("strand").send_keys('-')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Find the strand for the first result and verify it's background color
        rgb = driver.find_element_by_id('strand').value_of_css_property('background-color')
        print rgb
        #verify the RGB code is correct for the color Red
        self.assertEqual(rgb, 'rgba(255, 0, 0, 1)', 'the wrong RGB code is returning')

        
'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestVarSearch))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main()
            