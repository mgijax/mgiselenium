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
import HtmlTestRunner
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

class TestEiVariantSearch(unittest.TestCase):
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
        print (symbols)
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Rora<tmgc26>'])
        
    def testVarAlleleSymbolSearch(self):
        """
        @Status tests that a basic Variant Allele Symbol search works
        @see pwi-var-search-2
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele symbol field and enters a symbol
        driver.find_element(By.ID, "alleleSymbol").send_keys('Cntn1<usl>')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print (symbols)
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Cntn1<usl>'])

    def testVarAlleleSymbolWildSearch(self):
        """
        @Status tests that a basic Variant Allele Symbol search using a wildcard works
        @see pwi-var-search-3
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele symbol field and enters a symbol
        driver.find_element(By.ID, "alleleSymbol").send_keys('Cntn%')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print (symbols)
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Cntn1<m1J>', 'Cntn1<usl>', 'Cntnap1<M1Btlr>', 'Cntnap1<shm-5J>'])

    def testVarRefSearch(self):
        """
        @Status tests that a basic variant reference search works
        @see pwi-var-search-4 
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the references field and enters a J number
        driver.find_element(By.ID, "jnumIDs").send_keys('J:13651')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print (symbols)
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Cpe<fat>'])
        
    def testVarRefMultiSearch(self):
        """
        @Status tests that a variant multi reference search works
        @see pwi-var-search-5 currently broken!!!!!
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the history symbol field and enters a symbol
        driver.find_element(By.ID, "jnumIDs").send_keys('J:203032, J:13651')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print (symbols)
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Cntn1<usl>','Cpe<fat>'])
        
    def testVarChromosomeSearch(self):
        """
        @Status tests that a basic Chromosome search works
        @see pwi-var-search-6
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the chromosome field and enters a chromosome
        driver.find_element(By.ID, "chromosome").send_keys('X')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print (symbols[0])
        #assert some of the correct symbols are returned
        self.assertEqual(symbols[0], 'Ace2<em2Shyy>', 'symbol0 is wrong')
        self.assertEqual(symbols[1], 'Arhgap36<em1Seul>', 'symbol1 is wrong')
        self.assertEqual(symbols[2], 'Armcx4<C57BL/6N>', 'symbol2 is wrong')
        self.assertEqual(symbols[3], 'Arx<tm2Kki>', 'symbol3 is wrong')
        self.assertEqual(symbols[4], 'Arx<tm3Kki>', 'symbol4 is wrong')
        self.assertEqual(symbols[5], 'Arx<tm4Kki>', 'symbol5 is wrong')
        self.assertEqual(symbols[6], 'Arx<tm5Kki>', 'symbol6 is wrong')

    def testVarStrandSearch(self):
        """
        @Status tests that a basic Strand search works
        @see pwi-var-search-7 
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the Strand field and enters a Strand
        driver.find_element(By.ID, "strand").send_keys('+')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTableHeader")
        table = Table(results_table)
        time.sleep(4)
        # print row one through three
        row1 = table.get_row(0)
        row2 = table.get_row(1)
        row3 = table.get_row(2)
        row4 = table.get_row(3)
        print (row1.text)
        print (row2.text)
        print (row3.text)
        #assert that the first 3 search results are correct
        self.assertEqual(row1.text, '1700013F07Rik<em1Fuxi>' )
        self.assertEqual(row2.text, '2610301B20Rik<em1Jyang>')
        self.assertEqual(row3.text, '2610301B20Rik<em2Jyang>')
        self.assertEqual(row4.text, 'a<22R>')

    def testVarWithHGVSSearch(self):
        """
        @Status tests that a basic allele search returns HGVS data works
        @see pwi-var-search-8
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the Allele ID field and enters an MGI ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:5705324')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the HGVS description field
        hgvs_data = self.driver.find_element(By.ID, "description").get_attribute('value')
        time.sleep(2)
        print (hgvs_data)
        #assert the hgvs data is correct
        self.assertEquals(hgvs_data, "Alk:NM_007439.2:c.3836G>A:p.(Arg1279Gln)")

    def testVarWithJnumSearch(self):
        """
        @Status tests that a basic allele search returns variant reference data works
        @see pwi-var-search-9
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the Allele ID field and enters an MGI ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:5705324')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the Variant reference field
        var_jnum = self.driver.find_element(By.ID, "variantJnumIDs").get_attribute('value')
        time.sleep(2)
        print (var_jnum)
        #assert the variant reference data is correct
        self.assertEquals(var_jnum, "J:228124")

    def testVarWithNotesSearch(self):
        """
        @Status tests that a basic allele search returns variant notes(public & private) data works
        @see pwi-var-search-11
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the Allele ID field and enters an MGI ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:5491244')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the Public Notes field
        var_pnote = self.driver.find_element(By.ID, "publicNote").get_attribute('value')
        time.sleep(2)
        print (var_pnote)
        #assert the variant reference data is correct
        self.assertEquals(var_pnote, "Low impact")
        #find the curator Notes field
        var_cnote = self.driver.find_element(By.ID, "curatorNote").get_attribute('value')
        time.sleep(2)
        print (var_cnote)
        #assert the variant reference data is correct
        self.assertEquals(var_cnote, "unknown effect on splice donor site of intron 9")

    def testVarStrandNegSearch(self):
        """
        @Status tests that a variant Strand negative search has the stand always with a red background
        @see pwi-var-search-12 
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the Strand field and enters a Strand
        driver.find_element(By.ID, "strand").send_keys('-')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(6)
        #Find the strand for the first result and verify it's background color
        rgb = driver.find_element(By.ID, 'strand').value_of_css_property('background-color')
        print (rgb)
        #verify the RGB code is correct for the color Red
        self.assertEqual(rgb, 'rgba(255, 0, 0, 1)', 'the wrong RGB code is returning')

    def testAlleleWithMultVarSearch(self):
        """
        @Status tests that a basic allele search that has multiple variants displays all data correctly
        @see pwi-var-search-13
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the Allele ID field and enters an MGI ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:5301876')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the variant results table
        results_table = self.driver.find_element(By.ID, "variantTable")
        table = Table(results_table)
        # print row one through three
        row1 = table.get_row(0)
        row2 = table.get_row(1)
        row3 = table.get_row(2)
        row4 = table.get_row(3)
        row5 = table.get_row(4)
        print (row1.text)
        print (row2.text)
        print (row3.text)
        print (row4.text)
        print (row5.text)
        #assert that the first 3 search results are correct
        self.assertEqual(row3.text, 'GRCm39 24901452 24901452 T G - -')
        self.assertEqual(row4.text, 'GRCm39 24901470 24901470 T G - -')
        self.assertEqual(row5.text, 'GRCm39 24901488 24901489 AC GT - -')

    def testAlleleWithSingleVarSearch(self):
        """
        @Status tests that a basic allele search that has omly 1 variant displays all data correctly
        @see pwi-var-search-14, 16
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )       
        #finds the Allele ID field and enters an MGI ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:5616147')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the variant results table
        results_table = self.driver.find_element(By.ID, "variantTable")
        table = Table(results_table)
        # print row one through three
        row1 = table.get_row(0)
        row2 = table.get_row(1)
        row3 = table.get_row(2)
        print (row1.text)
        print (row2.text)
        print (row3.text)
        #assert that the search results are correct, this includes the table headings are correct as well
        self.assertEqual(row1.text, 'Genomic Transcript Polypeptide')
        self.assertEqual(row2.text, 'build start end ref var ID start end ref var ID start end ref var')
        self.assertEqual(row3.text, 'GRCm39 141218575 141218575 T C - -')

    def testVarGenomicRefSearch(self):
        """
        @Status tests that a basic allele search that has a variant with a long Genomic ref displays all data correctly
        @see pwi-var-search-17
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the Allele ID field and enters an MGI ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:5566856')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the variant results table
        results_table = self.driver.find_element(By.ID, "variantTable")
        table = Table(results_table)
        # print row one through three
        row1 = table.get_row(0)
        row2 = table.get_row(1)
        row3 = table.get_row(2)
        print (row1.text)
        print (row2.text)
        print (row3.text)
        #assert that the search results are correct, this variant has a rather long Genomic ref
        self.assertEqual(row3.text, 'GRCm39 122478667 122478680 CTACACGCATCCCA C - -')

    def testVarGenomicVarSearch(self):
        """
        @Status tests that a basic allele search that has a variant with a long Genomic var displays all data correctly
        @see pwi-var-search-18
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the Allele ID field and enters an MGI ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:3838372')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the variant results table
        results_table = self.driver.find_element(By.ID, "variantTable")
        table = Table(results_table)
        # print row one through three
        row1 = table.get_row(0)
        row2 = table.get_row(1)
        row3 = table.get_row(2)
        print (row1.text)
        print (row2.text)
        print (row3.text)
        #assert that the search results are correct, this variant has a rather long Genomic ref
        self.assertEqual(row3.text, 'GRCm39 57322231 57322238 CGGCGCAG GAGGACGA - -')

    def testVarGenomeList(self):
        """
        @Status tests that the picklist for Genome Build is correct
        @see pwi-var-search-19
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the Sourced Genomic Genome Build pulldown list
        dropdown = Select(driver.find_element(By.ID, "srcDnaVersion"))
        print ([o.text for o in dropdown.options])
        #assert that the search results are correct, this includes the table headings are correct as well
        self.assertEqual([o.text for o in dropdown.options], [u'', u'GRCm39 (mm10)\n       ', u'GRCm38.p12 \n       ', u'GRCm38.p11 \n       ', u'GRCm38.p10 \n       ', u'GRCm38.p9 \n       ', u'GRCm38.p8 \n       ', u'GRCm38.p7 \n       ', u'GRCm38.p6 \n       ', u'GRCm38.p5 \n       ', u'GRCm38.p4 \n       ', u'GRCm38.p3 \n       ', u'GRCm38.p2 \n       ', u'NCBI m37 (mm9)\n       ', u'NCBI m36 (mm8)\n       ', u'NCBI m35 (mm7)\n       ', u'NCBI m34 (mm6)\n       ', u'NCBI m33 (mm5)\n       ', u'NCBI m32 (mm4)\n       ', u'NCBI m30 (mm3)\n       ', u'MGSCv3 (mm2)\n       ', u'MGSCv2 (mm1)\n       ', u'Not Specified \n       '])
        
    def testAllelelinkVarSearch(self):
        """
        @Status tests that a basic allele search has a link to it's allele detail page just above the variant table
        @see pwi-var-detail-4
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )       
        #finds the Allele ID field and enters an MGI ID
        driver.find_element(By.ID, "alleleID").send_keys('MGI:3641255')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the Allele detail link above the variant table and locate the href text
        allele_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Myd88').get_attribute('href')
        print (allele_link)
        #Assert the href is correct
        self.assertEqual(allele_link, 'http://prodwww.informatics.jax.org/pwi/detail/allele/MGI:3641255')
                
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiVariantSearch))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
            