'''
Created on Nov 21, 2018

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
import HTMLTestRunner
import json
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table




# Tests

class TestMrkAddDelete(unittest.TestCase):
    """
    @status Tests you can add and delete markers of various types and statuses
    @see: 
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/marker")
    
    def tearDown(self):
        self.driver.close()
        
    def testTypeGeneAdd(self):
        """
        @Status tests that youcan add a marker of type Gene
        @see pwi-mrk-create-1
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element_by_id("markerType")).select_by_value('1')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print symbol1
        #Assert the correct marker symbol and marker type is returned
        self.assertEquals(symbol1, ['0610005A07Rik'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element_by_id('markerType').get_attribute('value')
        self.assertEqual(mrktype, '1')#1 equals "Gene"

    def testTypeDnaSegSearch(self):
        """
        @Status tests that a basic Marker Type DNA Segment Marker search works
        @see pwi-mrk-search-2
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element_by_id("markerType")).select_by_value('2')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print symbol1
        #symbols_cells = table.get_column_cells('Marker')
        self.assertEquals(symbol1, ['03.MMHAP34FRA.seq'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element_by_id('markerType').get_attribute('value')
        self.assertEqual(mrktype, '2')#2 equals "DNA Segment"

    def testTypeQtlSearch(self):
        """
        @Status tests that a basic Marker Type QTL Marker search works
        @see pwi-mrk-search-3 
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element_by_id("markerType")).select_by_value('6')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print symbol1
        self.assertEquals(symbol1, ['Aaaq1'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element_by_id('markerType').get_attribute('value')
        self.assertEqual(mrktype, '6')#9 equals "QTL"

    def testTypeTransSearch(self):
        """
        @Status tests that a basic Marker Type Transgene Marker search works
        @see pwi-mrk-search-4
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element_by_id("markerType")).select_by_value('12')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print symbol1
        self.assertEquals(symbol1, ['Et(cre/ERT2)119Rdav'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element_by_id('markerType').get_attribute('value')
        self.assertEqual(mrktype, '12')#12 equals "Transgene"

    def testTypeComplexSearch(self):
        """
        @Status tests that a basic Marker Type Complex/Cluster/Region Marker search works
        @see pwi-mrk-search-5
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element_by_id("markerType")).select_by_value('10')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print symbol1
        self.assertEquals(symbol1, ['Amy'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element_by_id('markerType').get_attribute('value')
        self.assertEqual(mrktype, '10')#10 equals "Complex/Cluster/Region"

    def testTypeCytoSearch(self):
        """
        @Status tests that a basic Marker Type Cytogenetic Marker search works
        @see pwi-mrk-search-6
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element_by_id("markerType")).select_by_value('3')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print symbol1
        self.assertEquals(symbol1, ['Del(10)12H'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element_by_id('markerType').get_attribute('value')
        self.assertEqual(mrktype, '3')#3 equals "Cytogenetic Marker"

    def testTypeBacYacSearch(self):
        """
        @Status tests that a basic Marker Type BAC/YAC search works
        @see pwi-mrk-search-7
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element_by_id("markerType")).select_by_value('8')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)

        # print row 1
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print symbol1
        self.assertEquals(symbol1, ['03B03F'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element_by_id('markerType').get_attribute('value')
        self.assertEqual(mrktype, '8')#8 equals "BAC/YAC end"

    def testTypePseudoSearch(self):
        """
        @Status tests that a basic Marker Type Pseudogene Marker search works
        @see pwi-mrk-search-8
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element_by_id("markerType")).select_by_value('7')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print symbol1
        self.assertEquals(symbol1, ['100034662'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element_by_id('markerType').get_attribute('value')
        self.assertEqual(mrktype, '7')#7 equals "Pseudogene"

    def testTypeOtherSearch(self):
        """
        @Status tests that a basic Marker Type Other Genome Feature search works
        @see pwi-mrk-search-9
        """
        driver = self.driver
        #finds the Marker Type field and select the Other Genome Feature option
        Select(driver.find_element_by_id("markerType")).select_by_value('9')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        #get the first row of data and print it's symbol
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print symbol1
        #assert the symbol is correct
        self.assertEquals(symbol1, ['2610021C13Rik'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element_by_id('markerType').get_attribute('value')
        self.assertEqual(mrktype, '9')#9 equals "Other Genome Feature"

    def testWithdrawnSymbolSearch(self):
        """
        @Status tests that a basic Withdrawn Symbol search works
        @see pwi-mrk-search-10
        """
        driver = self.driver
        #finds the Symbol field . Enter Asun and click the Search button
        driver.find_element_by_id("markerSymbol").send_keys("Asun")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # find the first row of data
        cells = table.get_row(0)
        #print the first row result
        print cells.text
        #locate the Name field and verify the result is correct
        mrkname = driver.find_element_by_id('markerName').get_attribute('value')
        self.assertEqual(mrkname, 'withdrawn, = Ints13')
        
    def testStatusOfficialSearch(self):
        """
        @Status tests that a basic Marker status Official search works
        @see pwi-mrk-search-11
        """
        driver = self.driver
        #finds the Marker Status field, selects the option Official and clicks search
        Select(driver.find_element_by_id("markerStatus")).select_by_value('1')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        #print column 1
        print cells.text
        #assert the symbol is correct
        self.assertEquals(cells.text, '0610005C13Rik')
        #locate the Marker status field and assert it is correct
        mrkstatus = driver.find_element_by_id('markerStatus').get_attribute('value')
        self.assertEqual(mrkstatus, '1')#1 equals "Official"

    def testStatusWithdrawnSearch(self):
        """
        @Status tests that a basic Marker status Withdrawn search works
        @see pwi-mrk-search-12
        """
        driver = self.driver
        #finds the Marker Status field, selects the option Withdrawn and clicks search
        Select(driver.find_element_by_id("markerStatus")).select_by_value('2')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        #print column 1
        print cells.text
        #assert the symbol is correct
        self.assertEquals(cells.text, '0610005A07Rik')
        #locate the Marker status field and assert it is correct
        mrkstatus = driver.find_element_by_id('markerStatus').get_attribute('value')
        self.assertEqual(mrkstatus, '2')#2 equals "Withdrawn"

    def testStatusReservedSearch(self):
        """
        @Status tests that a basic Marker status Reserved search works
        @see pwi-mrk-search-13
        """
        driver = self.driver
        #finds the Marker Status field, selects the option Reserved and clicks search
        Select(driver.find_element_by_id("markerStatus")).select_by_value('3')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        #print column 1
        print cells.text
        #assert the symbol is correct
        self.assertEquals(cells.text, 'Acadlm')
        #locate the Marker status field and assert it is correct
        mrkstatus = driver.find_element_by_id('markerStatus').get_attribute('value')
        self.assertEqual(mrkstatus, '3')#3 equals "Reserved"
    
    def testSymbolSearch(self):
        """
        @Status tests that a basic Symbol search works
        @see pwi-mrk-search-16
        """
        driver = self.driver
        #finds the Symbol field, enters a symbol and clicks search
        driver.find_element_by_id("markerSymbol").send_keys("10S")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        print cells.text
        #Assert the correct symbol has been returned in the results table
        self.assertEquals(cells.text, '10S')
        #Assert the correct Symbol is returned in the symbol field
        mrksymbol = driver.find_element_by_id('markerSymbol').get_attribute('value')
        self.assertEqual(mrksymbol, '10S')
  
    def testNameSearch(self):
        """
        @Status tests that a basic Name search works
        @see pwi-mrk-search-17
        """
        driver = self.driver
        #finds the Name field, enters a name and clicks search
        driver.find_element_by_id("markerName").send_keys("sonic hedgehog")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        print cells.text
        #Assert the correct symbol has been returned in the results table
        self.assertEquals(cells.text, 'Shh')
        #Assert the correct Symbol is returned in the symbol field
        mrksymbol = driver.find_element_by_id('markerSymbol').get_attribute('value')
        self.assertEqual(mrksymbol, 'Shh')
        #Assert the correct Name is returned in the name field
        mrkname = driver.find_element_by_id('markerName').get_attribute('value')
        self.assertEqual(mrkname, 'sonic hedgehog')  

    def testMGIAccIDSearch(self):
        """
        @Status tests that a basic Accession ID search using an MGI ID works
        @see pwi-mrk-search-18
        """
        driver = self.driver
        #finds the accession ID field, enters an ID and hits the search button
        driver.find_element_by_id("markerAccID").send_keys("MGI:87875")
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        print cells.text
        #Assert the correct symbol has been returned in the results table
        self.assertEquals(cells.text, 'Acf1')
        #Assert the correct Symbol is returned in the symbol field
        mrksymbol = driver.find_element_by_id('markerSymbol').get_attribute('value')
        self.assertEqual(mrksymbol, 'Acf1')
        #Assert the correct Name is returned in the name field
        mrkname = driver.find_element_by_id('markerName').get_attribute('value')
        self.assertEqual(mrkname, 'albumin conformation factor 1')  

    def testMGDAccIDSearch(self):
        """
        @Status tests that a basic Accession ID search using an MGD ID works
        @see pwi-mrk-search-19
        """
        driver = self.driver
        #finds the accession ID field, enters an ID and hits the search button
        driver.find_element_by_id("markerAccID").send_keys("MGD-MRK-8906")
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        print cells.text
        #Assert the correct symbol has been returned in the results table
        self.assertEquals(cells.text, 'Shh')
        #Assert the correct Symbol is returned in the symbol field
        mrksymbol = driver.find_element_by_id('markerSymbol').get_attribute('value')
        self.assertEqual(mrksymbol, 'Shh')
        #Assert the correct Name is returned in the name field
        mrkname = driver.find_element_by_id('markerName').get_attribute('value')
        self.assertEqual(mrkname, 'sonic hedgehog')  

    def testECAccIDSearch(self):
        """
        @Status tests that a basic Accession ID search using an EC ID works
        @see pwi-mrk-search-20
        """
        driver = self.driver
        #finds the accession ID field, enters an ID and hits the search button
        driver.find_element_by_id("markerAccID").send_keys("2.3.1.5")
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        print cells.text
        #Assert the correct symbol has been returned in the results table
        self.assertEquals(cells.text, 'Aanat')
        #Assert the correct Symbol is returned in the symbol field
        mrksymbol = driver.find_element_by_id('markerSymbol').get_attribute('value')
        self.assertEqual(mrksymbol, 'Aanat')
        #Assert the correct Name is returned in the name field
        mrkname = driver.find_element_by_id('markerName').get_attribute('value')
        self.assertEqual(mrkname, 'arylalkylamine N-acetyltransferase')  

    def testSymbolWildSearch(self):
        """
        @Status tests that a marker symbol search using a wildcard works
        @see pwi-mrk-search-21
        """
        driver = self.driver
        #finds the marker symbol field, enters a symbol and hits the search button
        driver.find_element_by_id("markerSymbol").send_keys("Pax%")
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cells = table.get_rows()
        print cells[0].text
        #Assert the correct symbols have been returned in the results table(only verifies the first 4 and last 4 results of the table)
        self.assertEquals(cells[0].text, 'Pax1')
        self.assertEquals(cells[1].text, 'Pax-1')
        self.assertEquals(cells[2].text, 'Pax2')
        self.assertEquals(cells[3].text, 'Pax-2')
        self.assertEquals(cells[18].text, 'Pax-9')
        self.assertEquals(cells[19].text, 'Paxbp1')
        self.assertEquals(cells[20].text, 'Paxip1')
        self.assertEquals(cells[21].text, 'Paxx')

    def testNameWildSearch(self):
        """
        @Status tests that a marker name search using a wildcard works
        @see pwi-mrk-search-22
        """
        driver = self.driver
        #finds the marker name field, enters a name and hits the search button
        driver.find_element_by_id("markerName").send_keys("casein%")
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cells = table.get_rows()
        print cells[0].text
        #Assert the correct symbols have been returned in the results table(only verifies the first 4 and last 4 results of the table)
        self.assertEquals(cells[0].text, 'Clpp')
        self.assertEquals(cells[1].text, 'Clpx')
        self.assertEquals(cells[2].text, 'Csn1s1')
        self.assertEquals(cells[3].text, 'Csn1s2a')
        self.assertEquals(cells[17].text, 'Csnka2ip')
        self.assertEquals(cells[18].text, 'Csnk2a1-ps')
        self.assertEquals(cells[19].text, 'Csnk2a1-ps1')
        self.assertEquals(cells[20].text, 'Csn')

    def testAccIDWildSearch(self):
        """
        @Status tests that an Accession ID search using a wildcard works
        @see pwi-mrk-search-23
        """
        driver = self.driver
        #finds the accession ID field, enters an ID and hits the search button
        driver.find_element_by_id("markerAccID").send_keys("MGD-MRK-890%")
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cells = table.get_rows()
        print cells[0].text
        #Assert the correct symbols have been returned in the results table(only verifies the first 4 and last 4 results of the table)
        self.assertEquals(cells[0].text, 'Arnt')
        self.assertEquals(cells[1].text, 'Drd5')
        self.assertEquals(cells[2].text, 'Dre')
        self.assertEquals(cells[3].text, 'Ds')
        self.assertEquals(cells[5].text, 'Dsg1a')
        self.assertEquals(cells[6].text, 'Mreg')
        self.assertEquals(cells[7].text, 'Shh')
        self.assertEquals(cells[8].text, 'Dsi1')
            
'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMrkSearch))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main()
    