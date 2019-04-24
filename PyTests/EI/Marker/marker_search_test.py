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

class TestMrkSearch(unittest.TestCase):
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
        @note: A DNA Segment type should not display Feature Type
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
        @note: A QTL type should not display Feature Type
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
        @note: A Transgene type should not display Feature Type
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
        @note: A Complex/Cluster/Region type should not display Feature Type
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
        @note: A BAC/YAC end type should not display Feature Type
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
        cells = table.get_row(1)
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
        @see pwi-mrk-search-18(broken)
        """
        driver = self.driver
        #finds the accession ID field, enters an ID and hits the search button
        driver.find_element_by_name("ids").send_keys("MGI:87875")
        searchAcc = driver.find_element_by_xpath('[type=submit]').click()
        searchAcc.submit()
        time.sleep(10)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print row 1
        cells = table.get_row(0)
        time.sleep(2)
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
        @see pwi-mrk-search-19(broken)
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
        @see pwi-mrk-search-20(broken)
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
        @see pwi-mrk-search-23(broken)
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

    def testCreateUserSearch(self):
        """
        @Status tests that a basic Create User search works
        @see pwi-mrk-det-date-search-1
        """
        driver = self.driver
        #finds the Created By field, enters a User name
        driver.find_element_by_id("markerCreatedBy").send_keys("yz")
        #finds the Creation date field, enters a date
        driver.find_element_by_id("markerCreationDate").send_keys("2001-07-03")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # get and print the 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'Aff4')
        self.assertEqual(cell1.text, 'Mthfr-rs1')
        #Assert the correct User Name is returned in the Created By field
        createname = driver.find_element_by_id('markerCreatedBy').get_attribute('value')
        self.assertEqual(createname, 'yz')

    def testModifyUserSearch(self):
        """
        @Status tests that a basic Modified User search works
        @see pwi-mrk-det-date-search-2
        """
        driver = self.driver
        #finds the Modified By field, enters a User name
        driver.find_element_by_id("markerModifiedBy").send_keys("monikat")
        #finds the Modification date field, enters a date
        driver.find_element_by_id("markerModificationDate").send_keys("2014-09-08")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # get and print the 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'Lbp')
        self.assertEqual(cell1.text, 'Lrp8')
        #Assert the correct User Name is returned in the Created By field
        createname = driver.find_element_by_id('markerModifiedBy').get_attribute('value')
        self.assertEqual(createname, 'monikat')   
             
    def testCreateDateSearch(self):
        """
        @Status tests that a basic Creation Date search works
        @see pwi-mrk-det-date-search-3
        """
        driver = self.driver
        #finds the Creation Date field, enters a Date
        driver.find_element_by_id("markerCreationDate").send_keys("2008-10-03")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, '100038882')
        self.assertEqual(cell1.text, 'Rgsc1520')
        #Assert the correct Creation Name is returned in the Creation Date field
        createdate = driver.find_element_by_id('markerCreationDate').get_attribute('value')
        self.assertEqual(createdate, '2008-10-03')        
             
    def testModifyDateSearch(self):
        """
        @Status tests that a basic Modification Date search works
        @see pwi-mrk-det-date-search-4
        """
        driver = self.driver
        #finds the Modification Date field, enters a Date
        driver.find_element_by_id("markerModificationDate").send_keys("2008-10-10")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, '2300002M23Rik')
        #Assert the correct Creation Name is returned in the Creation Date field
        modifydate = driver.find_element_by_id('markerModificationDate').get_attribute('value')
        self.assertEqual(modifydate, '2008-10-10')        

    def testModifyDateLessSearch(self):
        """
        @Status tests that a basic Modification Date by less than works
        @see pwi-mrk-det-date-search-7
        """
        driver = self.driver
        #finds the Modified By field, enters a User name
        driver.find_element_by_id("markerModifiedBy").send_keys("cms")
        #finds the Modification Date field, enters a Date with less than symbol
        driver.find_element_by_id("markerModificationDate").send_keys('<2004-12-15')
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, '4930500I12Rik')
        self.assertEqual(cell1.text, 'AY243472')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('markerModificationDate').get_attribute('value')
        self.assertEqual(modifydate, '2004-06-22')        

    def testModifyDateLessEqualSearch(self):
        """
        @Status tests that a basic Modification Date by less than equals works
        @see pwi-mrk-det-date-search-8
        """
        driver = self.driver
        #finds the Modified By field, enters a User name
        driver.find_element_by_id("markerModifiedBy").send_keys("cms")
        #finds the Modification Date field, enters a Date with less than symbol
        driver.find_element_by_id("markerModificationDate").send_keys('<=2004-12-15')
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, '4930500I12Rik')
        self.assertEqual(cell1.text, 'AI838599')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('markerModificationDate').get_attribute('value')
        self.assertEqual(modifydate, '2004-06-22')        
      
    def testModifyDateRangeSearch(self):
        """
        @Status tests that a basic Modification Date by range search works
        @see pwi-mrk-det-date-search-9
        """
        driver = self.driver
        #finds the Modified By field, enters a User name
        driver.find_element_by_id("markerModifiedBy").send_keys("monikat")
        #finds the Modification Date field, enters a range of Dates
        driver.find_element_by_id("markerModificationDate").send_keys("2018-11-26..2018-11-27")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'Tg(Alb-SND1)3aDsar')
        self.assertEqual(cell1.text, 'Tg(KRT5-Terf2)PMBlas')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('markerModificationDate').get_attribute('value')
        self.assertEqual(modifydate, '2018-11-26')        
        

    def testCreateDateLessSearch(self):
        """
        @Status tests that a basic Creation Date by less than works
        @see pwi-mrk-det-date-search-12
        """
        driver = self.driver
        #finds the Created By field, enters a User name
        driver.find_element_by_id("markerCreatedBy").send_keys("cms")
        #finds the Creation Date field, enters a Date with less than symbol
        driver.find_element_by_id("markerCreationDate").send_keys('<2002-05-20')
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'Huc1')
        self.assertEqual(cell1.text, 'Huc2')
        #Assert the correct Creation Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('markerCreationDate').get_attribute('value')
        self.assertEqual(modifydate, '2002-03-27')        

    def testCreateDateLessEqualSearch(self):
        """
        @Status tests that a basic Creation Date by less than equals works
        @see pwi-mrk-det-date-search-13
        """
        driver = self.driver
        #finds the Modified By field, enters a User name
        driver.find_element_by_id("markerCreatedBy").send_keys("cms")
        #finds the Creation Date field, enters a Date with less than symbol
        driver.find_element_by_id("markerCreationDate").send_keys('<=2002-05-20')
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'Atxn7')
        self.assertEqual(cell1.text, 'Huc1')
        #Assert the correct Creation Date is returned in the Creation Date field
        modifydate = driver.find_element_by_id('markerCreationDate').get_attribute('value')
        self.assertEqual(modifydate, '2002-05-20')        
      
    def testCreateDateRangeSearch(self):
        """
        @Status tests that a basic Modification Date by range search works
        @see pwi-mrk-det-date-search-14
        """
        driver = self.driver
        #finds the Created By field, enters a User name
        driver.find_element_by_id("markerCreatedBy").send_keys("cms")
        #finds the Creation Date field, enters a range of Dates
        driver.find_element_by_id("markerCreationDate").send_keys("2002-05-20..2002-05-21")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct symbols has been returned in the results table
        self.assertEqual(cell0.text, 'Atxn7')
        self.assertEqual(cell1.text, 'Galnt5')
        #Assert the correct Creation Date is returned in the Creation Date field
        createdate = driver.find_element_by_id('markerCreationDate').get_attribute('value')
        self.assertEqual(createdate, '2002-05-20')        

    def testSynonymTypeSearch(self):
        """
        @Status tests that a basic Synonym type search works
        @see pwi-mrk-det-syn-search-1
        """
        driver = self.driver
        #finds the Synonym Type field and selects the type of "Broad"
        Select(driver.find_element_by_id("markerSynonymTypeQueryID")).select_by_value('1006')
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the synonym results table
        syn_table = self.driver.find_element_by_id("synonymTable")
        table = Table(syn_table)
        # get the data for the Synonym Type column, print the row 5 result
        cell = table.get_column_cells('Type')
        print cell[5].text
        #Assert the fith synonym type returned(row5) is correct
        self.assertEqual(cell[5].text, 'broad')
        
    def testSynonymNameSearch(self):
        """
        @Status tests that a basic Synonym name search works
        @see pwi-mrk-det-syn-search-2
        """
        driver = self.driver
        #finds the Synonym name field, enters a synonym name
        driver.find_element_by_id("markerSynonymID").send_keys("Gf-1")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the synonym results table
        syn_table = self.driver.find_element_by_id("synonymTable")
        table = Table(syn_table)
        # get the data for the Synonym column, print the row 2 result
        cell = table.get_column_cells('Synonym')
        print cell[2].text
        #Assert the second synonym name returned(row2) is correct
        self.assertEqual(cell[2].text, 'Gf-1')
        
    def testSynonymJnumSearch(self):
        """
        @Status tests that a basic Synonym J number search works
        @see pwi-mrk-det-syn-search-3
        """
        driver = self.driver
        #finds the Synonym J number field, enters a J number
        driver.find_element_by_id("markerSynonymJnumID").send_keys("J:9808")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the synonym results table
        syn_table = self.driver.find_element_by_id("synonymTable")
        table = Table(syn_table)
        # get the data for the Synonym J# column, print the row 2 result
        cell = table.get_column_cells('J:#')
        print cell[2].text
        #Assert the second synonym J number returned(row2) is correct
        self.assertEqual(cell[2].text, 'J:9808')              

    def testSynonymJnumSearch2(self):
        """
        @Status tests that a basic Synonym J number search without the J: works
        @see pwi-mrk-det-syn-search-3
        """
        driver = self.driver
        #finds the Synonym J number field, enters a J number
        driver.find_element_by_id("markerSynonymJnumID").send_keys("J:9808")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the synonym results table
        syn_table = self.driver.find_element_by_id("synonymTable")
        table = Table(syn_table)
        # get the data for the Synonym J# column, print the row 2 result
        cell = table.get_column_cells('J:#')
        print cell[2].text
        #Assert the second synonym J number returned(row2) is correct
        self.assertEqual(cell[2].text, 'J:9808')    

    def testSynonymModBySearch(self):
        """
        @Status tests that a basic Synonym Modified By search works
        @see pwi-mrk-det-syn-search-4
        """
        driver = self.driver
        #finds the Synonym Modified By field, enters a user
        driver.find_element_by_id("markerSynonymModByID").send_keys("honda")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the synonym results table
        syn_table = self.driver.find_element_by_id("synonymTable")
        table = Table(syn_table)
        # get the data for the Synonym Modified By column, print the row 2 result
        cell = table.get_column_cells('Modified By')
        print cell[2].text
        #Assert the second synonym J number returned(row2) is correct
        self.assertEqual(cell[2].text, 'honda')        

    def testSynonymDateSearch(self):
        """
        @Status tests that a basic Synonym Date search works
        @see pwi-mrk-det-syn-search-5
        """
        driver = self.driver
        #finds the Synonym Date field, enters a date
        driver.find_element_by_id("markerSynonymDateID").send_keys("2015-07-23")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the synonym results table
        syn_table = self.driver.find_element_by_id("synonymTable")
        table = Table(syn_table)
        # get the data for the Synonym Date column, print the row 2 result
        cell = table.get_column_cells('Date')
        print cell[2].text
        #Assert the second synonym J number returned(row2) is correct
        self.assertEqual(cell[2].text, '2015-07-23')      

    def testSynonymSortSearch(self):
        """
        @Status tests that a basic Synonym name search returns  synonyms sorted in the correct order of exact,similiar,broad,narrow
        @see pwi-mrk-det-syn-search-6
        """
        driver = self.driver
        #finds the Synonym name field, enters a synonym name
        driver.find_element_by_id("markerSynonymID").send_keys("Sqn5")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(10)
        #find the synonym results table
        syn_table = self.driver.find_element_by_id("synonymTable")
        table = Table(syn_table)
        # get the data for the Synonym Type column, print the results
        cell = table.get_column_cells('Type')
        print cell[1].text
        print cell[2].text
        print cell[3].text
        #Assert the synonym types returned are in the correct order
        self.assertEqual(cell[1].text, 'exact')
        self.assertEqual(cell[2].text, 'similar')
        self.assertEqual(cell[3].text, 'broad')

    def testMrkwithSTSMarkersSearch(self):
        """
        @Status tests that a marker search which has STS Markers displays these markers in the STS Markers tab
        @see pwi-mrk-det-detail-4
        """
        driver = self.driver
        #finds the Symbol field . Enter Asun and click the Search button
        driver.find_element_by_id("markerSymbol").send_keys("Ncam1")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the STS markers tab and click it
        driver.find_element_by_id('aliasTabButton').click()
        #find the alias results table
        alias_table = self.driver.find_element_by_id("aliasesTable")
        table = Table(alias_table)
        # find the Alias column of data
        cells = table.get_column_cells('STS markers')
        time.sleep(2)
        #print the first row result
        print cells[1].text
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
        driver.find_element_by_id("markerSymbol").send_keys("Gata1")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the TSS tab and click it
        driver.find_element_by_id('tssTabButton').click()
        time.sleep(2)
        #find the tss results table
        alias_table = self.driver.find_element_by_id("tssTable")
        table = Table(alias_table)
        # find the tss column of data
        cells = table.get_column_cells('TSS or Gene')
        time.sleep(2)
        #print the first row result
        print cells[1].text
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
        driver.find_element_by_id("markerSymbol").send_keys("Tssr162832")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the TSS tab and click it
        driver.find_element_by_id('tssTabButton').click()
        #find the tss results table
        alias_table = self.driver.find_element_by_id("tssTable")
        table = Table(alias_table)
        # find the tss column of data
        cells = table.get_column_cells('TSS or Gene')
        time.sleep(2)
        #print the first row result
        print cells[1].text
        #locate the tss fields and verify the results are correct
        self.assertEqual(cells[1].text, 'Gata1')

    def testMrkRefGenSearch(self):
        """
        @Status tests that a marker reference search which has reference type of General returns correct data
        @see pwi-mrk-det-ref-search-1 **note: might need rewrite to properly  do assertIn correctly if we want  to use assertIn!!
        """
        driver = self.driver
        #find the Reference tab and click it
        driver.find_element_by_id('refsTabButton').click()
        #find the Type pulldown for references and select the General option
        Select(driver.find_element_by_id("markerSynonymTypeQueryID")).select_by_value('1018')
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #waits until the Reference table is displayed on the page    
        wait.forAngular(self.driver)
        #find the Reference results table
        refs_table = self.driver.find_element_by_id("refsTable")
        table = Table(refs_table)
        # find the first row of data
        cells = table.get_row(1)
        #print the first row result
        print cells.text
        #locate the first row of reference data and verify it is correct
        self.assertEqual(cells.text, 'General J:234813 Luo S, Cell Stem Cell 2016 May 5;18(5):637-52 pm2geneload 2019-03-31')
        
    def testMrkRefStrainSearch(self):
        """
        @Status tests that a marker reference search which has reference type of strain-specific marker returns correct data
        @see pwi-mrk-det-ref-search-2 
        """
        driver = self.driver
        #find the Reference tab and click it
        driver.find_element_by_id('refsTabButton').click()
        #find the Type pulldown for references and select the strain-specific marker option
        Select(driver.find_element_by_id("markerSynonymTypeQueryID")).select_by_value('1028')
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #waits until the Reference table is displayed on the page    
        wait.forAngular(self.driver)
        #find the Reference results table
        refs_table = self.driver.find_element_by_id("refsTable")
        reftable = Table(refs_table)
        # find the first row of data
        cells = reftable.get_column_cells('Type')
        types = iterate.getTextAsList(cells)
        #print the Types column results
        print types
        #locate the Types column of reference data and verify the strain-specific marker type is disaplyed at least once
        self.assertIn('Strain-Specific Marker', types)
           
    def testMrkRefJnumSearch(self):
        """
        @Status tests that a marker reference search using J number returns correct data
        @see pwi-mrk-det-ref-search-3 
        """
        driver = self.driver
        #find the Reference tab and click it
        driver.find_element_by_id('refsTabButton').click()
        #find the references J number field and enter the J number
        driver.find_element_by_id("markerRefJnumID").send_keys("J:699")
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #waits until the Reference table is displayed on the page    
        wait.forAngular(self.driver)
        #find the Reference results table
        refs_table = self.driver.find_element_by_id("refsTable")
        table = Table(refs_table)
        # find the column of data for J numbers
        cells = table.get_column_cells('J:#')
        jnums = iterate.getTextAsList(cells)
        #print the J numbers column data
        print jnums
        #locate the column of reference J number data and verify that J:699 exists on one of the rows
        self.assertIn('J:699', jnums)

    def testMrkRefJnumSearch2(self):
        """
        @Status tests that a marker reference search using J number without J: returns correct data
        @see pwi-mrk-det-ref-search-3 
        """
        driver = self.driver
        #find the Reference tab and click it
        driver.find_element_by_id('refsTabButton').click()
        #find the references J number field and enter the J number
        driver.find_element_by_id("markerRefJnumID").send_keys("699")
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #waits until the Reference table is displayed on the page    
        wait.forAngular(self.driver)
        #find the Reference results table
        refs_table = self.driver.find_element_by_id("refsTable")
        table = Table(refs_table)
        # find the column of data for J numbers
        cells = table.get_column_cells('J:#')
        jnums = iterate.getTextAsList(cells)
        #print the J numbers column data
        print jnums
        #locate the column of reference J number data and verify that J:699 exists on one of the rows
        self.assertIn('J:699', jnums)
           
    def testMrkRefModBySearch(self):
        """
        @Status tests that a marker reference search using the Modified By field returns correct data
        @see pwi-mrk-det-ref-search-4
        """
        driver = self.driver
        #find the Reference tab and click it
        driver.find_element_by_id('refsTabButton').click()
        #find the references J number field and enter the J number
        driver.find_element_by_id("markerRefModByID").send_keys("honda")
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #wait until the Reference table is displayed on the page    
        wait.forAngular(self.driver)
        #find the Reference results table
        refs_table = self.driver.find_element_by_id("refsTable")
        table = Table(refs_table)
        # find the column of data for Modified by
        cells = table.get_column_cells('Modified By')
        modby = iterate.getTextAsList(cells)
        #print the column of data for Modified by
        print modby
        #locate the column of Modified by data and verify that honda exists on at least one of the rows
        self.assertIn('honda', modby)

    def testMrkRefDateSearch(self):
        """
        @Status tests that a marker reference search using the Date field returns correct data
        @see pwi-mrk-det-ref-search-5 
        """
        driver = self.driver
        #find the Reference tab and click it
        driver.find_element_by_id('refsTabButton').click()
        #find the references Date field and enter the date
        driver.find_element_by_id("markerRefDateID").send_keys("2015-07-13")
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #waits until the Reference table is displayed on the page    
        wait.forAngular(self.driver)
        #find the Reference results table
        refs_table = self.driver.find_element_by_id("refsTable")
        table = Table(refs_table)
        # find the column of data for Date
        cells = table.get_column_cells('Date')
        dates = iterate.getTextAsList(cells)
        #print the column results for the Date column
        print dates
        #locate the column of Date data and verify that 2015-07-13 exists on at least one of the rows
        self.assertIn('2015-07-13', dates)

    def testMrkRefSortSearch(self):
        """
        @Status tests that a marker reference search sorts the results correctly by Type then J#
        @see pwi-mrk-det-ref-search-6 
        """
        driver = self.driver
        #find the symbol field and enter the marker
        driver.find_element_by_id("markerSymbol").send_keys("Cxcl11")
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #find the Reference tab and click it
        driver.find_element_by_id('refsTabButton').click()
        #waits until the Reference table is displayed on the page    
        wait.forAngular(self.driver)
        #find the Reference results table
        refs_table = self.driver.find_element_by_id("refsTable")
        table = Table(refs_table)
        # find the rows of data
        allrows = table.get_rows()
        sort = iterate.getTextAsList(allrows)
        wait.forAngular(self.driver)
        #print the results of the Citation column
        print sort
        wait.forAngular(self.driver)
        #locate the rows and assert the order is correct
        self.assertEqual(sort, ['Type J:# Citation Modified By Date', 'General J:62788 Meyer M, Cytogenet Cell Genet 2000;88(3-4):278-82 pm2geneload 2019-03-31', 'General J:62835 Widney DP, J Immunol 2000 Jun 15;164(12):6322-31 pm2geneload 2019-03-31', 'General J:139937 Yates CC, Am J Pathol 2008 Sep;173(3):643-52 mmh 2009-06-24', 'General J:147166 Crawford MA, Infect Immun 2009 Apr;77(4):1664-78 csmith 2009-05-04', 'General J:212764 Zohar Y, J Clin Invest 2014 May 1;124(5):2009-22 pm2geneload 2019-03-31', 'General J:223165 Li S, PLoS One 2014;9(8):e104107 mmh 2015-08-28', 'General J:240190 Ha Y, Am J Pathol 2017 Feb;187(2):352-365 wilmil 2017-04-24', 'Strain-Specific Marker J:62788 Meyer M, Cytogenet Cell Genet 2000;88(3-4):278-82 yz 2015-06-25', 'Strain-Specific Marker J:124878 Sierro F, Proc Natl Acad Sci U S A 2007 Sep 11;104(37):14759-64 yz 2015-06-25'])


    def testMrkRefCiteSearch(self):
        """
        @Status tests that a marker reference search using the Citation field returns correct data
        @see pwi-mrk-det-ref-search-7 
        """
        driver = self.driver
        #find the Reference tab and click it
        driver.find_element_by_id('refsTabButton').click()
        #find the citation field and enter the text search with wildcard
        driver.find_element_by_id("markerRefCitationID").send_keys("Funk CD%")
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #waits until the Reference table is displayed on the page    
        wait.forAngular(self.driver)
        #find the Reference results table
        refs_table = self.driver.find_element_by_id("refsTable")
        table = Table(refs_table)
        # find the column of data for Citation
        cells = table.get_column_cells('Citation')
        cites = iterate.getTextAsList(cells)
        wait.forAngular(self.driver)
        #print the results of the Citation column
        print cites
        #locate the column of reference Citation data and verify that Funk CD exists on at least one of the rows
        self.assertIn('Funk CD, Biochim Biophys Acta 1996 Nov 11;1304(1):65-84', cites)

    def testMrkAccIDOtherSortSearch(self):
        """
        @Status tests that a marker search sorts the AccIDs(other) results correctly by Name then Acc ID
        @see pwi-mrk-det-ref-detail-7 
        """
        driver = self.driver
        #find the symbol field and enter the marker
        driver.find_element_by_id("markerSymbol").send_keys("Cdk3")
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #find the AccIDs(other) tab and click it
        driver.find_element_by_id('accOtherTabButton').click()
        #waits until the AccIDs(other) table is displayed on the page    
        wait.forAngular(self.driver)
        #find the AccID (other) results table
        acco_table = self.driver.find_element_by_id("accidOtherTable")
        table = Table(acco_table)
        # find the rows of data
        allrows = table.get_rows()
        sort = iterate.getTextAsList(allrows)
        wait.forAngular(self.driver)
        #print the results of the Citation column
        print sort
        wait.forAngular(self.driver)
        #locate the rows and assert the order is correct
        self.assertEqual(sort, ['Acc Name AccID J:# Citation Modified By Date', 'ABA 69681 J:132069 Lein ES, 2008;(): aba_assocload 2012-01-20', 'Affy 1.0 ST 10382779 J:144086 Mouse Genome Informatics Scientific Curators, Database Download 2009;(): Affy_1.0_ST_assocload 2011-06-18', 'Affy 430 2.0 1460472_at J:144087 Mouse Genome Informatics Scientific Curators, Database Download 2009;(): Affy_430_2.0_assocload 2011-06-18', 'Affy U74 110085_at J:157972 Mouse Genome Informatics Scientific Curators, Database Download 2010;(): Affy_U74_assocload 2011-06-18', 'ArrayExpress MGI:1916931 J:153877 Ringwald M, MGI Direct Data Submission 2009;(): arrayexp_assocload 2016-11-14', 'Ensembl Gene Model ENSMUSG00000092300 J:91388 Mouse Genome Informatics Scientific Curators, 2005;(): ensembl_assocload 2019-02-02', 'Ensembl Protein ENSMUSP00000134251 J:91388 Mouse Genome Informatics Scientific Curators, 2005;(): ensembl_proteinassocload 2019-02-02', 'Ensembl Transcript ENSMUST00000173567 J:91388 Mouse Genome Informatics Scientific Curators, 2005;(): ensembl_transcriptassocload 2019-02-02', 'Ensembl Transcript ENSMUST00000174177 J:91388 Mouse Genome Informatics Scientific Curators, 2005;(): ensembl_transcriptassocload 2019-02-02', 'Ensembl Transcript ENSMUST00000174248 J:91388 Mouse Genome Informatics Scientific Curators, 2005;(): ensembl_transcriptassocload 2019-02-02', 'Entrez Gene 69681 J:63103 Mouse Genome Database and National Center for Biotechnology, Database Release 2000;(): entrezgene_load 2019-03-31', 'FuncBase 1916931 J:145067 Bult C, 2009;(): mousefunc_assocload 2015-04-25', 'NCBI Gene Model 69681 J:90438 Mouse Genome Informatics Scientific Curators, 2005;(): ncbi_assocload 2019-01-19', 'RefSeq NR_004853 J:63103 Mouse Genome Database and National Center for Biotechnology, Database Release 2000;(): entrezgene_load 2019-03-31', 'SWISS-PROT Q80YP0 J:53168 Bairoch A, Database Release 1999;(): uniprotload_assocload 2019-03-31', 'UniGene 33677 J:57747 MGI Genome Annotation Group and UniGene Staff, Database Download 2015;(): mgd_dbo 2015-04-26'])

            
'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMrkSearch))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main()
    