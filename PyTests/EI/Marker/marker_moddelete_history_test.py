'''
Created on Feb 1, 2019
Tests the update and derlete features for the Marker History table
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

class TestMrkHistUpdateDelete(unittest.TestCase):
    """
    @status Test Marker History update and delete fields
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/marker")
    
    def tearDown(self):
        self.driver.close()
        
    def testSymbolHistoryUpdate(self):
        """
        @Status tests that marker history symbol can be modified
        @see pwi-mrk-det-hist-update-1 
        """
        driver = self.driver
        #finds the history symbol field and enters a symbol
        driver.find_element_by_id("markerHistorySymbolID").send_keys('Dsh')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #Iterate and print the search results column of Symbols
        sym = table.get_column_cells('Symbol')
        symbols = iterate.getTextAsList(sym)
        print symbols
        #Assert the correct marker symbols are returned
        self.assertEqual(symbols, ['Symbol', 'Hhg1', 'Hhg1', 'Shh', 'Dsh', 'Dsh', 'Hx', 'Hx', 'Hxl3', 'Hxl3'])
        
    def testSymbolHistoryValidation(self):
        """
        @Status tests that the symbol history validation works
        @see pwi-mrk-det-hist-update-2 
        """
        driver = self.driver
        #finds the history symbol field and enters a symbol
        driver.find_element_by_id("markerHistorySymbolID").send_keys('Pax%')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #Iterate and print the search results column of Symbols
        sym = table.get_column_cells('Symbol')
        symbols = iterate.getTextAsList(sym)
        print symbols
        #Assert the correct marker symbols are returned for the first result(Pax1)
        self.assertEqual(symbols, ['Symbol', 'hbs', 'hbs', 'wt', 'wt', 'un', 'un', 'Pax-1', 'Pax-1', 'Pax1'])
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Pax1','Pax2','Pax3','Pax4','Pax5','Pax6','Pax6os1','Pax7','Pax8','Pax9','Paxbp1','Paxip1','Paxx'])

    def testNameHistoryModify(self):
        """
        @Status tests that a basic Marker History Name can be modified
        @see pwi-mrk-det-hist-update-3 
        """
        driver = self.driver
        #finds the history name field and enters a name
        driver.find_element_by_id("markerHistoryNameID").send_keys('sonic hedgehog')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #Iterate and print the search results column of Symbols
        sym = table.get_column_cells('Symbol')
        symbols = iterate.getTextAsList(sym)
        print symbols
        #Assert the correct marker symbols are returned
        self.assertEqual(symbols, ['Symbol', 'Hhg1', 'Hhg1', 'Shh', 'Dsh', 'Dsh', 'Hx', 'Hx', 'Hxl3', 'Hxl3'])
        
    def testDateHistoryModify(self):
        """
        @Status tests that a basic Marker History Date can be modified
        @see pwi-mrk-det-hist-update-4 
        """
        driver = self.driver
        #finds the history symbol field and enters a symbol
        driver.find_element_by_id("markerHistoryNameID").send_keys('splotch-like%')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #Iterate and print the search results column of Symbols
        sym = table.get_column_cells('Symbol')
        symbols = iterate.getTextAsList(sym)
        print symbols
        #Assert the correct marker symbols are returned for the first result(Pax1)
        self.assertEqual(symbols, ['Symbol', 'Pax-3', 'Pax-3', 'Pax3', 'Sp', 'Sp', 'Splchl2', 'Splchl2'])
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Pax3','Splchl'])
        
    def testJnumHistoryModify(self):
        """
        @Status tests that a basic Marker History J# can be modified
        @see pwi-mrk-det-hist-update-5
        """
        driver = self.driver
        #finds the history name field and enters a name
        driver.find_element_by_id("markerHistoryModDateID").send_keys('2018-09-20')
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
        self.assertEquals(symbols, ['Shs','Tg(CAG-MYC,-GFP*)#Rugg', 'Tg(Rho-GSTP1)#Psbe'])

    def testJnumHistoryValid(self):
        """
        @Status tests that a basic Marker History J number update verifies
        @see pwi-mrk-det-hist-update-6
        """
        driver = self.driver
        #finds the J# field and enters a J number
        driver.find_element_by_id("markerHistoryJNumID").send_keys('J:2944')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #Iterate and print the search results column of J#
        sym = table.get_column_cells('J#')
        jnums = iterate.getTextAsList(sym)
        print jnums
        #Assert the correct J# searched is returned for the first result(Pax1)
        self.assertIn('J:2944', jnums)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Pax3','Del(1)3H'])

    def testEventHistoryModify(self):
        """
        @Status tests that a basic Marker History Event can be modified
        @see pwi-mrk-det-hist-search-8
        """
        driver = self.driver
        #finds the Citation field and enters a citation string
        driver.find_element_by_id("markerHistoryCitationID").send_keys('Balling R, Cell 1988 Nov 4;55(3):531-5')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #Iterate and print the search results column of Citation
        cite = table.get_column_cells('Citation')
        cites = iterate.getTextAsList(cite)
        print cites
        #Assert the correct citation searched is returned for the first result(Pax1)
        self.assertIn('Balling R, Cell 1988 Nov 4;55(3):531-5', cites)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Pax1'])


    def testEventReasonHistoryModify(self):
        """
        @Status tests that a basic Marker History Event Reason can be modified
        @see pwi-mrk-det-hist-search-9 
        """
        driver = self.driver
        #finds the Citation field and enters a citation string
        driver.find_element_by_id("markerHistoryCitationID").send_keys('Selby P%')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #Iterate and print the search results column of Citation
        cite = table.get_column_cells('Citation')
        cites = iterate.getTextAsList(cite)
        print cites
        #Assert the correct citation searched is returned for the first result(Ccd)
        self.assertIn('Selby P, Mouse News Lett 1985;72():123', cites)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Ccd', 'Shh'])


    def testHistoryDeleteConfirm(self):
        """
        @Status tests that a basic Marker History row deletion gives a validation popup confirmation and the row gets highlighted.
        @see pwi-mrk-det-hist-update-12 
        """
        driver = self.driver
        #finds the history symbol field and enters a symbol
        driver.find_element_by_id("markerHistorySymbolID").send_keys('Gata1')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #click the first cell of the fifth row to put it in edit mode
        del_cell = table.get_cell(5, 0)
        del_cell.click()
        #locate the span tag inside the cell and click it to bring up the popup
        del_cell.find_element_by_css_selector('tr.ng-scope:nth-child(6)>td:nth-child(1)>span:nth-child(1)').click()
        time.sleep(2)
        #switch to the popup alert box
        alert = self.driver.switch_to_alert()
        #get the alert box text
        alert_text = alert.text
        #Assert the correct alert text is displayed
        self.assertEqual('Are you sure you want to delete this history row?', alert_text)
        #click on alert OK button
        alert.accept()
        #find the fifth row of data
        driver.find_element_by_css_selector('tr.ng-scope:nth-child(6)')
        #locate the class name  for this row
        del_class = driver.find_element_by_class_name('deletedHistoryRow')
        #Assert that the class name is true which means the row is highlighted for deletion
        self.assertTrue(del_class, 'class is missing')
        
        
'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMrkSearch))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main()
       