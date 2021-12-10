'''
Created on Oct 30, 2018

This test verifies searching within the Marker module.

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
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table




# Tests

class TestEiMrkSearchHistory(unittest.TestCase):
    """
    @status Test Literature Triage search using J number, etc
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/marker")
    
    def tearDown(self):
        self.driver.close()
        
    def testTypeGeneSearch(self):
        """
        @Status tests that a basic Marker Type Gene search works
        @see pwi-mrk-search-1
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element(By.ID, "markerType")).select_by_value('string:2')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct marker symbol and marker type is returned
        self.assertEqual(symbol1, ['03.MMHAP34FRA.seq'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element(By.ID, 'markerType').get_attribute('value')
        self.assertEqual(mrktype, 'string:2')#2 equals "DNA Segment"

    def testTypeDnaSegSearch(self):
        """
        @Status tests that a basic Marker Type DNA Segment Marker search works
        @note: A DNA Segment type should not display Feature Type
        @see pwi-mrk-search-2
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element(By.ID, "markerType")).select_by_value('string:2')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #symbols_cells = table.get_column_cells('Marker')
        self.assertEqual(symbol1, ['03.MMHAP34FRA.seq'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element(By.ID, 'markerType').get_attribute('value')
        self.assertEqual(mrktype, 'string:2')#2 equals "DNA Segment"

    def testTypeQtlSearch(self):
        """
        @Status tests that a basic Marker Type QTL Marker search works
        @note: A QTL type should not display Feature Type
        @see pwi-mrk-search-3 
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element(By.ID, "markerType")).select_by_value('string:6')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        self.assertEqual(symbol1, ['Aaaq1'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element(By.ID, 'markerType').get_attribute('value')
        self.assertEqual(mrktype, 'string:6')#9 equals "QTL"

    def testTypeTransSearch(self):
        """
        @Status tests that a basic Marker Type Transgene Marker search works
        @note: A Transgene type should not display Feature Type
        @see pwi-mrk-search-4
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element(By.ID, "markerType")).select_by_value('string:12')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        self.assertEqual(symbol1, ['Del(3Gpr89-Prkab2)4Tac'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element(By.ID, 'markerType').get_attribute('value')
        self.assertEqual(mrktype, 'string:12')#12 equals "Transgene"

    def testTypeComplexSearch(self):
        """
        @Status tests that a basic Marker Type Complex/Cluster/Region Marker search works
        @note: A Complex/Cluster/Region type should not display Feature Type
        @see pwi-mrk-search-5
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element(By.ID, "markerType")).select_by_value('string:10')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        self.assertEqual(symbol1, ['Amy'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element(By.ID, 'markerType').get_attribute('value')
        self.assertEqual(mrktype, 'string:10')#10 equals "Complex/Cluster/Region"

    def testTypeCytoSearch(self):
        """
        @Status tests that a basic Marker Type Cytogenetic Marker search works
        @see pwi-mrk-search-6
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element(By.ID, "markerType")).select_by_value('string:3')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        self.assertEqual(symbol1, ['Del(10)12H'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element(By.ID, 'markerType').get_attribute('value')
        self.assertEqual(mrktype, 'string:3')#3 equals "Cytogenetic Marker"

    def testTypeBacYacSearch(self):
        """
        @Status tests that a basic Marker Type BAC/YAC search works
        @note: A BAC/YAC end type should not display Feature Type
        @see pwi-mrk-search-7
        """
        driver = self.driver
        #finds the results table and iterates through the table
        Select(driver.find_element(By.ID, "markerType")).select_by_value('string:8')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)

        # print row 1
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        self.assertEqual(symbol1, ['03B03F'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element(By.ID, 'markerType').get_attribute('value')
        self.assertEqual(mrktype, 'string:8')#8 equals "BAC/YAC end"

    def testTypePseudoSearch(self):
        """
        @Status tests that a basic Marker Type Pseudogene Marker search works
        @see pwi-mrk-search-8
        """
        driver = self.driver
        #finds the marker type pseudogene and selects it, then selects chromosome 16 to narrow down results set
        Select(driver.find_element(By.ID, "markerType")).select_by_value('string:7')
        driver.find_element(By.ID, 'chromosome').clear();
        driver.find_element(By.ID, 'chromosome').send_keys("16");
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        self.assertEqual(symbol1, ['100039035'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element(By.ID, 'markerType').get_attribute('value')
        self.assertEqual(mrktype, 'string:7')#7 equals "Pseudogene"

    def testTypeOtherSearch(self):
        """
        @Status tests that a basic Marker Type Other Genome Feature search works
        @see pwi-mrk-search-9
        """
        driver = self.driver
        #finds the Marker Type field and select the Other Genome Feature option, then selects chromosome 16 to narrow down search results
        Select(driver.find_element(By.ID, "markerType")).select_by_value('string:9')
        driver.find_element(By.ID, 'chromosome').clear();
        driver.find_element(By.ID, 'chromosome').send_keys("16");
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #get the first row of data and print it's symbol
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #assert the symbol is correct
        self.assertEqual(symbol1, ['Actb-rs1'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element(By.ID, 'markerType').get_attribute('value')
        self.assertEqual(mrktype, 'string:9')#9 equals "Other Genome Feature"

    def testWithdrawnSymbolSearch(self):
        """
        @Status tests that a basic Withdrawn Symbol search works
        @see pwi-mrk-search-10
        """
        driver = self.driver
        #finds the Symbol field . Enter Asun and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("Asun")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # find the first row of data
        cells = table.get_row(0)
        #print the first row result
        print(cells.text)
        #locate the Name field and verify the result is correct
        mrkname = driver.find_element(By.ID, 'markerName').get_attribute('value')
        self.assertEqual(mrkname, 'withdrawn, = Ints13')
        
    def testStatusOfficialSearch(self):
        """
        @Status tests that a basic Marker status Official search works
        @see pwi-mrk-search-11
        """
        driver = self.driver
        #finds the Marker Status field, selects the option Official and Chromosome 16, then clicks search
        Select(driver.find_element(By.ID, "markerStatus")).select_by_value('string:1')
        driver.find_element(By.ID, 'chromosome').clear();
        driver.find_element(By.ID, 'chromosome').send_keys("16");
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        #print column 1
        print(cells.text)
        #assert the symbol is correct
        self.assertEqual(cells.text, '0610009F21Rik')
        #locate the Marker status field and assert it is correct
        mrkstatus = driver.find_element(By.ID, 'markerStatus').get_attribute('value')
        self.assertEqual(mrkstatus, 'string:1')#1 equals "Official"

    def testStatusWithdrawnSearch(self):
        """
        @Status tests that a basic Marker status Withdrawn search works
        @see pwi-mrk-search-12
        """
        driver = self.driver
        #finds the Marker Status field, selects the option Withdrawn, selects chromosome 16 and clicks search
        Select(driver.find_element(By.ID, "markerStatus")).select_by_value('string:2')
        driver.find_element(By.ID, 'chromosome').clear();
        driver.find_element(By.ID, 'chromosome').send_keys("16");
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        #print column 1
        print(cells.text)
        #assert the symbol is correct
        self.assertEqual(cells.text, '0610006N12Rik')
        #locate the Marker status field and assert it is correct
        mrkstatus = driver.find_element(By.ID, 'markerStatus').get_attribute('value')
        self.assertEqual(mrkstatus, 'string:2')#2 equals "Withdrawn"

    def testStatusReservedSearch(self):
        """
        @Status tests that a basic Marker status Reserved search works
        @see pwi-mrk-search-13
        """
        driver = self.driver
        #finds the Marker Status field, selects the option Reserved and clicks search
        Select(driver.find_element(By.ID, "markerStatus")).select_by_value('string:3')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        #print column 1
        print(cells.text)
        #assert the symbol is correct
        self.assertEqual(cells.text, 'Acadlm')
        #locate the Marker status field and assert it is correct
        mrkstatus = driver.find_element(By.ID, 'markerStatus').get_attribute('value')
        self.assertEqual(mrkstatus, 'string:3')#3 equals "Reserved"
    
    def testSymbolSearch(self):
        """
        @Status tests that a basic Symbol search works
        @see pwi-mrk-search-16
        """
        driver = self.driver
        #finds the Symbol field, enters a symbol and clicks search
        driver.find_element(By.ID, "markerSymbol").send_keys("10S")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        print(cells.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cells.text, '10S')
        #Assert the correct Symbol is returned in the symbol field
        mrksymbol = driver.find_element(By.ID, 'markerSymbol').get_attribute('value')
        self.assertEqual(mrksymbol, '10S')
  
    def testNameSearch(self):
        """
        @Status tests that a basic Name search works
        @see pwi-mrk-search-17
        """
        driver = self.driver
        #finds the Name field, enters a name and clicks search
        driver.find_element(By.ID, "markerName").send_keys("sonic hedgehog")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        print(cells.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cells.text, 'Shh')
        #Assert the correct Symbol is returned in the symbol field
        mrksymbol = driver.find_element(By.ID, 'markerSymbol').get_attribute('value')
        self.assertEqual(mrksymbol, 'Shh')
        #Assert the correct Name is returned in the name field
        mrkname = driver.find_element(By.ID, 'markerName').get_attribute('value')
        self.assertEqual(mrkname, 'sonic hedgehog')  

    def testMGIAccIDSearch(self):
        """
        @Status tests that a basic Accession ID search using an MGI ID works
        @see pwi-mrk-search-18(broken)
        """
        driver = self.driver
        #form = self.form
        #form.enter_value('accessionForm', 'MGI:87875')
        #form.click_search()
        #finds the accession ID field, enters an ID and hits the search button
        driver.find_element(By.ID, "accIdQuery").send_keys("MGI:87875")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        time.sleep(2)
        print(cells.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cells.text, 'Acf1')
        #Assert the correct Symbol is returned in the symbol field
        mrksymbol = driver.find_element(By.ID, 'markerSymbol').get_attribute('value')
        self.assertEqual(mrksymbol, 'Acf1')
        #Assert the correct Name is returned in the name field
        mrkname = driver.find_element(By.ID, 'markerName').get_attribute('value')
        self.assertEqual(mrkname, 'albumin conformation factor 1')  

    def testMGDAccIDSearch(self):
        """
        @Status tests that a basic Accession ID search using an MGD ID works
        @see pwi-mrk-search-19(had to use MGI ID as old MGD IDs did not work)!!Broken
        """
        driver = self.driver
        #finds the accession ID field, enters an ID and hits the search button
        driver.find_element(By.ID, "accIdQuery").send_keys("MGI:98297")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(10)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        time.sleep(2)
        print(cells.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cells.text, 'Shh')
        #Assert the correct Symbol is returned in the symbol field
        mrksymbol = driver.find_element(By.ID, 'markerSymbol').get_attribute('value')
        self.assertEqual(mrksymbol, 'Shh')
        #Assert the correct Name is returned in the name field
        mrkname = driver.find_element(By.ID, 'markerName').get_attribute('value')
        self.assertEqual(mrkname, 'sonic hedgehog')  

    #def testECAccIDSearch(self):
        """  
        @Status tests that a basic Accession ID search using an EC ID works
        @see pwi-mrk-search-20(broken)
        
        driver = self.driver
        #finds the accession ID field, enters an ID and hits the search button
        driver.find_element(By.ID, "accIdQuery").send_keys("2.3.1.5")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        print cells.text
        #Assert the correct symbol has been returned in the results table
        self.assertEquals(cells.text, 'Aanat')
        #Assert the correct Symbol is returned in the symbol field
        mrksymbol = driver.find_element(By.ID, 'markerSymbol').get_attribute('value')
        self.assertEqual(mrksymbol, 'Aanat')
        #Assert the correct Name is returned in the name field
        mrkname = driver.find_element(By.ID, 'markerName').get_attribute('value')
        self.assertEqual(mrkname, 'arylalkylamine N-acetyltransferase')  
        """
    def testSymbolWildSearch(self):
        """
        @Status tests that a marker symbol search using a wildcard works
        @see pwi-mrk-search-21
        """
        driver = self.driver
        #finds the marker symbol field, enters a symbol and hits the search button
        driver.find_element(By.ID, "markerSymbol").send_keys("Pax%")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cells = table.get_rows()
        print(cells[0].text)
        #Assert the correct symbols have been returned in the results table(only verifies the first 4 and last 4 results of the table)
        self.assertEqual(cells[0].text, 'Pax1')
        self.assertEqual(cells[1].text, 'Pax-1')
        self.assertEqual(cells[2].text, 'Pax2')
        self.assertEqual(cells[3].text, 'Pax-2')
        self.assertEqual(cells[18].text, 'Pax-9')
        self.assertEqual(cells[19].text, 'Paxbp1')
        self.assertEqual(cells[20].text, 'Paxip1')
        self.assertEqual(cells[21].text, 'Paxx')

    def testNameWildSearch(self):
        """
        @Status tests that a marker name search using a wildcard works
        @see pwi-mrk-search-22
        """
        driver = self.driver
        #finds the marker name field, enters a name and hits the search button
        driver.find_element(By.ID, "markerName").send_keys("casein%")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # print row 1
        cells = table.get_rows()
        print(cells[0].text)
        #Assert the correct symbols have been returned in the results table(only verifies the first 4 and last 4 results of the table)
        self.assertEqual(cells[0].text, 'Clpp')
        self.assertEqual(cells[1].text, 'Clpx')
        self.assertEqual(cells[2].text, 'Csn1s1')
        self.assertEqual(cells[3].text, 'Csn1s2a')
        self.assertEqual(cells[18].text, 'Csnk2a1-ps2')
        self.assertEqual(cells[19].text, 'Csnk2a1-ps3')
        self.assertEqual(cells[20].text, 'Csnk2a1-ps4')
        self.assertEqual(cells[21].text, 'Csn')

    #def testAccIDWildSearch(self):
        """
        @Status tests that an Accession ID search using a wildcard works
        @see pwi-mrk-search-23(broken) appears wildcards not allowed in accid search?
        
        driver = self.driver
        #finds the accession ID field, enters an ID and hits the search button
        driver.find_element(By.ID, "accIdQuery").send_keys("MGD-MRK-890%")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
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
        """
    def testCreateUserSearch(self):
        """
        @Status tests that a basic Create User search works
        @see pwi-mrk-det-date-search-1
        """
        driver = self.driver
        #finds the Created By field, enters a User name
        driver.find_element(By.ID, "markerCreatedBy").send_keys("yz")
        #finds the Creation date field, enters a date
        driver.find_element(By.ID, "markerCreationDate").send_keys("2001-07-03")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'Aff4')
        self.assertEqual(cell1.text, 'Mthfr-rs1')
        #Assert the correct User Name is returned in the Created By field
        createname = driver.find_element(By.ID, 'markerCreatedBy').get_attribute('value')
        self.assertEqual(createname, 'yz')

    def testModifyUserSearch(self):
        """
        @Status tests that a basic Modified User search works
        @see pwi-mrk-det-date-search-2
        """
        driver = self.driver
        #finds the Modified By field, enters a User name
        driver.find_element(By.ID, "markerModifiedBy").send_keys("monikat")
        #finds the Modification date field, enters a date
        driver.find_element(By.ID, "markerModificationDate").send_keys("2014-09-08")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'Lbp')
        self.assertEqual(cell1.text, 'Lrp8')
        #Assert the correct User Name is returned in the Created By field
        createname = driver.find_element(By.ID, 'markerModifiedBy').get_attribute('value')
        self.assertEqual(createname, 'monikat')   
             
    def testCreateDateSearch(self):
        """
        @Status tests that a basic Creation Date search works
        @see pwi-mrk-det-date-search-3
        """
        driver = self.driver
        #finds the Creation Date field, enters a Date
        driver.find_element(By.ID, "markerCreationDate").send_keys("2008-10-03")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, '100038882')
        self.assertEqual(cell1.text, 'Rgsc1520')
        #Assert the correct Creation Name is returned in the Creation Date field
        createdate = driver.find_element(By.ID, 'markerCreationDate').get_attribute('value')
        self.assertEqual(createdate, '2008-10-03')        
             
    def testModifyDateSearch(self):
        """
        @Status tests that a basic Modification Date search works
        @see pwi-mrk-det-date-search-4
        """
        driver = self.driver
        #finds the Modification Date field, enters a Date
        driver.find_element(By.ID, "markerModificationDate").send_keys("2008-10-10")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, '2300002M23Rik')
        #Assert the correct Creation Name is returned in the Creation Date field
        modifydate = driver.find_element(By.ID, 'markerModificationDate').get_attribute('value')
        self.assertEqual(modifydate, '2008-10-10')        

    def testModifyDateLessSearch(self):
        """
        @Status tests that a basic Modification Date by less than works
        @see pwi-mrk-det-date-search-7
        """
        driver = self.driver
        #finds the Modified By field, enters a User name
        driver.find_element(By.ID, "markerModifiedBy").send_keys("cms")
        #finds the Modification Date field, enters a Date with less than symbol
        driver.find_element(By.ID, "markerModificationDate").send_keys('<2004-12-15')
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, '4930500I12Rik')
        self.assertEqual(cell1.text, 'AY243472')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element(By.ID, 'markerModificationDate').get_attribute('value')
        self.assertEqual(modifydate, '2004-06-22')        

    def testModifyDateLessEqualSearch(self):
        """
        @Status tests that a basic Modification Date by less than equals works
        @see pwi-mrk-det-date-search-8
        """
        driver = self.driver
        #finds the Modified By field, enters a User name
        driver.find_element(By.ID, "markerModifiedBy").send_keys("cms")
        #finds the Modification Date field, enters a Date with less than symbol
        driver.find_element(By.ID, "markerModificationDate").send_keys('<=2004-12-15')
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, '4930500I12Rik')
        self.assertEqual(cell1.text, 'AI838599')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element(By.ID, 'markerModificationDate').get_attribute('value')
        self.assertEqual(modifydate, '2004-06-22')        
      
    def testModifyDateRangeSearch(self):
        """
        @Status tests that a basic Modification Date by range search works
        @see pwi-mrk-det-date-search-9
        """
        driver = self.driver
        #finds the Modified By field, enters a User name
        driver.find_element(By.ID, "markerModifiedBy").send_keys("monikat")
        #finds the Modification Date field, enters a range of Dates
        driver.find_element(By.ID, "markerModificationDate").send_keys("2018-11-26..2018-11-27")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'Tg(Alb-SND1)3aDsar')
        self.assertEqual(cell1.text, 'Tg(KRT5-Terf2)PMBlas')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element(By.ID, 'markerModificationDate').get_attribute('value')
        self.assertEqual(modifydate, '2018-11-26')        
        

    def testCreateDateLessSearch(self):
        """
        @Status tests that a basic Creation Date by less than works
        @see pwi-mrk-det-date-search-12
        """
        driver = self.driver
        #finds the Created By field, enters a User name
        driver.find_element(By.ID, "markerCreatedBy").send_keys("cms")
        #finds the Creation Date field, enters a Date with less than symbol
        driver.find_element(By.ID, "markerCreationDate").send_keys('<2002-05-20')
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'Huc1')
        self.assertEqual(cell1.text, 'Huc2')
        #Assert the correct Creation Date is returned in the Modification Date field
        modifydate = driver.find_element(By.ID, 'markerCreationDate').get_attribute('value')
        self.assertEqual(modifydate, '2002-03-27')        

    def testCreateDateLessEqualSearch(self):
        """
        @Status tests that a basic Creation Date by less than equals works
        @see pwi-mrk-det-date-search-13
        """
        driver = self.driver
        #finds the Modified By field, enters a User name
        driver.find_element(By.ID, "markerCreatedBy").send_keys("cms")
        #finds the Creation Date field, enters a Date with less than symbol
        driver.find_element(By.ID, "markerCreationDate").send_keys('<=2002-05-20')
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'Atxn7')
        self.assertEqual(cell1.text, 'Huc1')
        #Assert the correct Creation Date is returned in the Creation Date field
        createdate = driver.find_element(By.ID, 'markerCreationDate').get_attribute('value')
        self.assertEqual(createdate, '2002-05-20')        
      
    def testCreateDateRangeSearch(self):
        """
        @Status tests that a basic Modification Date by range search works
        @see pwi-mrk-det-date-search-14
        """
        driver = self.driver
        #finds the Created By field, enters a User name
        driver.find_element(By.ID, "markerCreatedBy").send_keys("cms")
        #finds the Creation Date field, enters a range of Dates
        driver.find_element(By.ID, "markerCreationDate").send_keys("2002-05-20..2002-05-21")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbols has been returned in the results table
        self.assertEqual(cell0.text, 'Atxn7')
        self.assertEqual(cell1.text, 'Galnt5')
        #Assert the correct Creation Date is returned in the Creation Date field
        createdate = driver.find_element(By.ID, 'markerCreationDate').get_attribute('value')
        self.assertEqual(createdate, '2002-05-20')        

    def testSynonymTypeSearch(self):
        """
        @Status tests that a basic Synonym type search works
        @see pwi-mrk-det-syn-search-1
        """
        driver = self.driver
        #finds the Synonym Type field and selects the type of "Broad"
        Select(driver.find_element(By.ID, "synonymType-0")).select_by_value('string:1006')
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the synonym results table type column row 5
        syn_type = driver.find_element(By.ID, 'synonymType-4').get_attribute('value')
        print(syn_type)
        #Assert the fith synonym type returned(row5) is correct
        self.assertEqual(syn_type, 'string:1006')#string:1006  equals synonym type Broad
        
    def testSynonymNameSearch(self):
        """
        @Status tests that a basic Synonym name search works
        @see pwi-mrk-det-syn-search-2
        """
        driver = self.driver
        #finds the Synonym name field, enters a synonym name
        driver.find_element(By.ID, "synonymName-0").send_keys("Gf-1")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the synonym results table type column row 5
        syn_name = driver.find_element(By.ID, 'synonymName-1').get_attribute('value')
        print(syn_name)
        #Assert the second synonym name returned(row2) is correct
        self.assertEqual(syn_name, 'Gf-1')
        
    def testSynonymJnumSearch(self):
        """
        @Status tests that a basic Synonym J number search works
        @see pwi-mrk-det-syn-search-3 
        """
        driver = self.driver
        #finds the Synonym J number field, enters a J number
        driver.find_element(By.ID, "synjnumID-0").send_keys("J:9808")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        syn_jnum = driver.find_element(By.ID, 'synjnumID-1').get_attribute('value')
        print(syn_jnum)
        #Assert the synonym J number is correct for row 2
        self.assertEqual(syn_jnum, 'J:9808')
        

    def testSynonymJnumSearch2(self):
        """
        @Status tests that a basic Synonym J number search without the J: works
        @see pwi-mrk-det-syn-search-3
        """
        driver = self.driver
        #finds the Synonym J number field, enters a J number
        driver.find_element(By.ID, "synjnumID-0").send_keys("9808")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        syn_jnum = driver.find_element(By.ID, 'synjnumID-1').get_attribute('value')
        print(syn_jnum)
        #Assert the synonym J number is correct for row 2
        self.assertEqual(syn_jnum, 'J:9808') 

    def testSynonymModBySearch(self):
        """
        @Status tests that a basic Synonym Modified By search works
        @see pwi-mrk-det-syn-search-4
        """
        driver = self.driver
        #finds the Synonym Modified By field, enters a user
        driver.find_element(By.ID, "synonymModifiedBy-0").send_keys("honda")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'synonymModification_date-2')))
        # get the data for the Synonym Modified By column, print the row 2 result
        syn_mod = driver.find_element(By.ID, 'synonymModifiedBy-1').get_attribute('value')        
        #Assert the second synonym date returned(row2) is correct
        self.assertEqual(syn_mod, 'honda')         

    def testSynonymDateSearch(self):
        """
        @Status tests that a basic Synonym Date search works
        @see pwi-mrk-det-syn-search-5
        """
        driver = self.driver
        #finds the Synonym Date field, enters a date
        driver.find_element(By.ID, "synonymModification_date-0").send_keys("2015-07-23")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'synonymModification_date-2')))
        # get the data for the Synonym Date column, print the row 2 result
        syn_date = driver.find_element(By.ID, 'synonymModification_date-1').get_attribute('value')        
        #Assert the second synonym date returned(row2) is correct
        self.assertEqual(syn_date, '2015-07-23')      

    def testSynonymSortSearch(self):
        """
        @Status tests that a basic Synonym name search returns  synonyms sorted in the correct order of exact,similiar,broad,narrow
        @see pwi-mrk-det-syn-search-6
        """
        driver = self.driver
        #finds the Synonym name field, enters a synonym name
        driver.find_element(By.ID, "synonymName-0").send_keys("Sqn5")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the synonym results table type column row 5
        syn_type1 = driver.find_element(By.ID, 'synonymType-0').get_attribute('value')
        syn_type2 = driver.find_element(By.ID, 'synonymType-1').get_attribute('value')
        syn_type3 = driver.find_element(By.ID, 'synonymType-2').get_attribute('value')
        print(syn_type1)
        #Assert the  synonym types returned are in the correct order
        self.assertEqual(syn_type1, 'string:1004')#string:1004  equals synonym type exact
        self.assertEqual(syn_type2, 'string:1005')#string:1005  equals synonym type similiar
        self.assertEqual(syn_type3, 'string:1006')#string:1006  equals synonym type Broad

    def testMrkwithSTSMarkersSearch(self):
        """
        @Status tests that a marker search which has STS Markers displays these markers in the STS Markers tab
        @see pwi-mrk-det-detail-4
        """
        driver = self.driver
        #finds the Symbol field . Enter Asun and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("Ncam1")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the STS markers tab and click it
        driver.find_element(By.ID, 'aliasTabButton').click()
        #find the alias results table
        alias_table = self.driver.find_element(By.ID, "aliasesTable")
        table = Table(alias_table)
        # find the Alias column of data
        cells = table.get_column_cells('STS markers')
        time.sleep(2)
        #print the first row result
        print(cells[1].text)
        #locate the Alias fields and verify the results are correct
        self.assertEqual(cells[1].text, 'D9Mit22')
        self.assertEqual(cells[2].text, 'D9Mit26')
        self.assertEqual(cells[3].text, 'D9Mit94')
        self.assertEqual(cells[4].text, 'D9Mit98')
        self.assertEqual(cells[5].text, 'D9Nds6')

    def testMrkwithTssSearch(self):
        """
        @Status tests that a marker search which has TSS Markers displays these markers in the STS Markers tab
        @see pwi-mrk-det-detail-5 
        """
        driver = self.driver
        #finds the Symbol field . Enter Gata1 and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("Gata1")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the TSS tab and click it
        driver.find_element(By.ID, 'tssTabButton').click()
        time.sleep(2)
        #find the tss results table
        alias_table = self.driver.find_element(By.ID, "tssTable")
        table = Table(alias_table)
        # find the tss column of data
        cells = table.get_column_cells('TSS or Gene')
        time.sleep(2)
        #print the first row result
        print(cells[1].text)
        #locate the tss fields and verify the results are correct
        self.assertEqual(cells[1].text, 'Tssr162832')
        self.assertEqual(cells[2].text, 'Tssr162833')
        self.assertEqual(cells[3].text, 'Tssr162834')
        self.assertEqual(cells[4].text, 'Tssr162835')
        self.assertEqual(cells[5].text, 'Tssr162836')
        self.assertEqual(cells[6].text, 'Tssr162837')
        self.assertEqual(cells[7].text, 'Tssr162838')

    def testTssMrkSearch(self):
        """
        @Status tests that a marker search of a TSS Marker displays the correct associated markers in the STS Markers tab
        @see pwi-mrk-det-detail-6
        """
        driver = self.driver
        #finds the Symbol field . Enter Gata1 and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("Tssr162832")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the TSS tab and click it
        driver.find_element(By.ID, 'tssTabButton').click()
        #find the tss results table
        alias_table = self.driver.find_element(By.ID, "tssTable")
        table = Table(alias_table)
        # find the tss column of data
        cells = table.get_column_cells('TSS or Gene')
        time.sleep(2)
        #print the first row result
        print(cells[1].text)
        #locate the tss fields and verify the results are correct
        self.assertEqual(cells[1].text, 'Gata1')

    def testMrkRefGenSearch(self):
        """
        @Status tests that a marker reference search which has reference type of General returns correct data
        @see pwi-mrk-det-ref-search-1 
        """
        driver = self.driver
        #find the Reference tab and click it
        driver.find_element(By.ID, 'refsTabButton').click()
        #find the Type pulldown for reference type and select the General option
        Select(driver.find_element(By.ID, "refAssocType")).select_by_value('string:1018')
        #find the J# field and enter the J number
        refbox = driver.find_element(By.ID, "refjnumID-0")
        refbox.send_keys("J:180800")
        refbox.send_keys(Keys.TAB)
        time.sleep(2)        
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 40 seconds
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.ID, 'refAssocModification_date-1')))
        #waits until the Reference table is displayed on the page    
        #wait.forAngular(self.driver)
        #time.sleep(20)
       
        #find the reference results table type column
        ref_type1 = driver.find_elements(By.ID, 'refAssocType')[0].get_attribute('value')
        ref_type2 = driver.find_elements(By.ID, 'refAssocType')[1].get_attribute('value')
        
        print(ref_type1)
        #Assert the  synonym types returned are in the correct order
        self.assertEqual(ref_type1, 'string:1018')#string:1018  equals reference type general
        self.assertEqual(ref_type2, 'string:1018')#string:1018  equals reference type general

        
    def testMrkRefStrainSearch(self):
        """
        @Status tests that a marker reference search which has reference type of strain-specific marker returns correct data
        @see pwi-mrk-det-ref-search-2 
        """
        driver = self.driver
        #find the Reference tab and click it
        driver.find_element(By.ID, 'refsTabButton').click()
        #find the Type pulldown for references and select the strain-specific marker option
        Select(driver.find_element(By.ID, "refAssocType")).select_by_value('string:1028')
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the Reference table is displayed on the page    
        wait.forAngular(self.driver)
        #find the reference results table type column
        ref_type1 = driver.find_elements(By.ID, 'refAssocType')[16].get_attribute('value')
        ref_type2 = driver.find_elements(By.ID, 'refAssocType')[17].get_attribute('value')        
        print(ref_type1)
        #Assert the  synonym types returned are in the correct order
        self.assertEqual(ref_type1, 'string:1028')#string:1028  equals reference type strain-specific marker
        self.assertEqual(ref_type2, 'string:1028')#string:1028  equals reference type strain-specific marker
           
    def testMrkRefJnumSearch(self):
        """
        @Status tests that a marker reference search using J number returns correct data
        @see pwi-mrk-det-ref-search-3 
        """
        driver = self.driver
        #find the Reference tab and click it
        driver.find_element(By.ID, 'refsTabButton').click()
        #find the references J number field and enter the J number
        driver.find_element(By.ID, "refjnumID-0").send_keys("J:699")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the Reference table is displayed on the page    
        #wait.forAngular(self.driver)
        time.sleep(4)
        #find the reference results table J# column
        ref_jnum1 = driver.find_element(By.ID, 'refjnumID-0').get_attribute('value')
        ref_jnum2 = driver.find_element(By.ID, 'refjnumID-1').get_attribute('value')        
        print(ref_jnum1)
        #Assert the  J numbers returned are correct 
        self.assertEqual(ref_jnum1, 'J:699')
        self.assertEqual(ref_jnum2, 'J:10117')

    def testMrkRefJnumSearch2(self):
        """
        @Status tests that a marker reference search using J number without J: returns correct data
        @see pwi-mrk-det-ref-search-3 
        """
        driver = self.driver
        #find the Reference tab and click it
        driver.find_element(By.ID, 'refsTabButton').click()
        #find the references J number field and enter the J number
        driver.find_element(By.ID, "refjnumID-0").send_keys("699")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the Reference table is displayed on the page    
        wait.forAngular(self.driver)
        #find the Reference results table
        #find the reference results table J# column
        ref_jnum1 = driver.find_element(By.ID, 'refjnumID-0').get_attribute('value')
        ref_jnum2 = driver.find_element(By.ID, 'refjnumID-1').get_attribute('value')        
        print(ref_jnum1)
        #Assert the  J numbers returned are correct 
        self.assertEqual(ref_jnum1, 'J:699')
        self.assertEqual(ref_jnum2, 'J:10117')
           
    def testMrkRefModBySearch(self):
        """
        @Status tests that a marker reference search using the Modified By field returns correct data
        @see pwi-mrk-det-ref-search-4
        """
        driver = self.driver
        #find the Reference tab and click it
        driver.find_element(By.ID, 'refsTabButton').click()
        time.sleep(2)
        #find the references Modified By field and enter the name
        driver.find_element(By.ID, "refAssocModifiedBy-0").send_keys("rbabiuk")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #wait until the Reference table is displayed on the page    
        #wait.forAngular(self.driver)
        time.sleep(20)
        #find the Modified by column eighth row
        mod_by1 = driver.find_element(By.ID, 'refAssocModifiedBy-8').get_attribute('value')
        print(mod_by1)
        #Assert the  Modified By field returned is correct 
        self.assertEqual(mod_by1, 'rbabiuk')

    def testMrkRefDateSearch(self):
        """
        @Status tests that a marker reference search using the Date field returns correct data
        @see pwi-mrk-det-ref-search-5 
        """
        driver = self.driver
        #find the Reference tab and click it
        driver.find_element(By.ID, 'refsTabButton').click()
        #find the references J number field and enter the J number
        driver.find_element(By.ID, "refjnumID-0").send_keys("J:221782")
        #find the references Date field and enter the date
        driver.find_element(By.ID, "refAssocModification_date-0").send_keys("2015-07-13")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the Reference table is displayed on the page    
        wait.forAngular(self.driver)
        #find the Modified by column eighth row
        mod_date1 = driver.find_element(By.ID, 'refAssocModification_date-2').get_attribute('value')
        print(mod_date1)
        #Assert the  Modified By field returned is correct 
        self.assertEqual(mod_date1, '2015-07-13')


    def testMrkRefSortSearch(self):
        """
        @Status tests that a marker reference search sorts the results correctly by Type then J#
        @see pwi-mrk-det-ref-search-6 
        """
        driver = self.driver
        #find the symbol field and enter the marker
        driver.find_element(By.ID, "markerSymbol").send_keys("Cxcl11")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #find the Reference tab and click it
        driver.find_element(By.ID, 'refsTabButton').click()
        #waits until the Reference table is displayed on the page    
        time.sleep(5)
        #find the reference results table type column
        ref_type1 = driver.find_elements(By.ID, 'refAssocType')[7].get_attribute('value')
        ref_type2 = driver.find_elements(By.ID, 'refAssocType')[8].get_attribute('value')        
        print(ref_type1)
        #Assert the  synonym types returned are in the correct order
        self.assertEqual(ref_type1, 'string:1018')#string:1028  equals reference type general
        self.assertEqual(ref_type2, 'string:1028')#string:1028  equals reference type strain-specific marker

    def testMrkRefCiteSearch(self):
        """
        @Status tests that a marker reference search using the Citation field returns correct data
        @see pwi-mrk-det-ref-search-7 
        """
        driver = self.driver
        #find the Reference tab and click it
        driver.find_element(By.ID, 'refsTabButton').click()
        #find the citation field and enter the text search with wildcard
        driver.find_element(By.ID, "refAssocCitation-0").send_keys("Funk CD%")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the Reference table is displayed on the page    
        wait.forAngular(self.driver)
        #find the reference results table type column
        cite = driver.find_element(By.ID, 'refAssocCitation-3').get_attribute('value')       
        print(cite)
        #Assert the citation returned is correct for row4
        self.assertEqual(cite, 'Funk CD, Biochim Biophys Acta 1996 Nov 11;1304(1):65-84')

    def testMrkAccIDOtherSortSearch(self):
        """
        @Status tests that a marker search sorts the AccIDs(other) results correctly by Name then Acc ID
        @see pwi-mrk-det-ref-detail-7 
        """
        driver = self.driver
        #find the symbol field and enter the marker
        driver.find_element(By.ID, "markerSymbol").send_keys("Cdk3")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #find the AccIDs(other) tab and click it
        driver.find_element(By.ID, 'accOtherTabButton').click()
        #waits until the AccIDs(other) table is displayed on the page    
        wait.forAngular(self.driver)
        #find the AccID (other) results table
        acco_table = self.driver.find_element(By.ID, "accidOtherTable")
        table = Table(acco_table)
        wait.forAngular(self.driver)
        #locate the rows and assert the order is correct
        #self.assertEqual(sort, ['Acc Name AccID J# Citation Modified By Date', 'ABA 69681 J:132069 Lein ES, 2008;(): aba_assocload 2012-01-20', 'Affy 1.0 ST 10382779 J:144086 Mouse Genome Informatics Scientific Curators, Database Download 2009;(): Affy_1.0_ST_assocload 2011-06-18', 'Affy 430 2.0 1460472_at J:144087 Mouse Genome Informatics Scientific Curators, Database Download 2009;(): Affy_430_2.0_assocload 2011-06-18', 'Affy U74 110085_at J:157972 Mouse Genome Informatics Scientific Curators, Database Download 2010;(): Affy_U74_assocload 2011-06-18', 'ArrayExpress MGI:1916931 J:153877 Ringwald M, MGI Direct Data Submission 2009;(): arrayexp_assocload 2016-11-14', 'Ensembl Gene Model ENSMUSG00000092300 J:91388 Mouse Genome Informatics Scientific Curators, 2005;(): ensembl_assocload 2019-08-03', 'Ensembl Protein ENSMUSP00000134251 J:91388 Mouse Genome Informatics Scientific Curators, 2005;(): ensembl_proteinassocload 2019-08-03', 'Ensembl Transcript ENSMUST00000173567 J:91388 Mouse Genome Informatics Scientific Curators, 2005;(): ensembl_transcriptassocload 2019-08-03', 'Ensembl Transcript ENSMUST00000174177 J:91388 Mouse Genome Informatics Scientific Curators, 2005;(): ensembl_transcriptassocload 2019-08-03', 'Ensembl Transcript ENSMUST00000174248 J:91388 Mouse Genome Informatics Scientific Curators, 2005;(): ensembl_transcriptassocload 2019-08-03', 'Entrez Gene 69681 J:63103 Mouse Genome Database and National Center for Biotechnology, Database Release 2000;(): entrezgene_load 2019-08-11', 'FuncBase 1916931 J:145067 Bult C, 2009;(): mousefunc_assocload 2015-04-25', 'NCBI Gene Model 69681 J:90438 Mouse Genome Informatics Scientific Curators, 2005;(): ncbi_assocload 2019-01-19', 'RefSeq NR_004853 J:63103 Mouse Genome Database and National Center for Biotechnology, Database Release 2000;(): entrezgene_load 2019-08-11', 'SWISS-PROT Q80YP0 J:53168 Bairoch A, Database Release 1999;(): uniprotload_assocload 2019-08-11', 'UniGene 33677 J:57747 MGI Genome Annotation Group and UniGene Staff, Database Download 2015;(): mgd_dbo 2015-04-26'])
        #find the first column of results
        names = table.get_column_cells('Acc Name')
        name_list = iterate.getTextAsList(names)
        print(name_list)
        #Assert the names are in the correct sort order
        self.assertEqual(name_list, ['Acc Name', 'ABA', 'Affy 1.0 ST', 'Affy 430 2.0', 'Affy U74', 'ArrayExpress', 'Ensembl Gene Model', 'Ensembl Protein', 'Ensembl Transcript', 'Ensembl Transcript', 'Ensembl Transcript', 'Entrez Gene', 'FuncBase', 'NCBI Gene Model', 'RefSeq', 'SWISS-PROT', 'UniGene'])            
        #find the second column of results
        accs = table.get_column_cells('AccID')
        acc_list = iterate.getTextAsList(accs)
        print(acc_list)  
        #Assert the Acc IDs are in the correct sort order
        self.assertEqual(acc_list, ['AccID', '69681', '10382779', '1460472_at', '110085_at', 'MGI:1916931', 'ENSMUSG00000092300', 'ENSMUSP00000134251', 'ENSMUST00000173567', 'ENSMUST00000174177', 'ENSMUST00000174248', '69681', '1916931', '69681', 'NR_004853', 'Q80YP0', '33677'])
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiMrkSearchHistory))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))    
