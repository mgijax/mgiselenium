'''
Created on Oct 30, 2018

These tests verify searching within the Marker module.

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

class TestMrkHistSearch(unittest.TestCase):
    """
    @status Test Marker History search fields
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/marker")
    
    def tearDown(self):
        self.driver.close()
        
    def testSymbolHistorySearch(self):
        """
        @Status tests that a basic Marker History Symbol search works
        @see pwi-mrk-det-hist-search-1
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
        
    def testSymbolHistoryWildSearch(self):
        """
        @Status tests that a basic Marker History Symbol search with a wildcard works
        @see pwi-mrk-det-hist-search-2
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

    def testNameHistorySearch(self):
        """
        @Status tests that a basic Marker History Name search works
        @see pwi-mrk-det-hist-search-3
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
        
    def testNameHistoryWildSearch(self):
        """
        @Status tests that a basic Marker History Name search with a wildcard works
        @see pwi-mrk-det-hist-search-4
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
        
    def testDateHistorySearch(self):
        """
        @Status tests that a basic Marker History Date search works
        @see pwi-mrk-det-hist-search-5
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

    def testJnumHistorySearch(self):
        """
        @Status tests that a basic Marker History J number search works
        @see pwi-mrk-det-hist-search-6
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

    def testJnumHistorySearch2(self):
        """
        @Status tests that a basic Marker History J number search works when the J: is not added
        @see pwi-mrk-det-hist-search-6
        """
        driver = self.driver
        #finds the J# field and enters a J number
        driver.find_element_by_id("markerHistoryJNumID").send_keys('2944')
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

    def testCitationHistorySearch(self):
        """
        @Status tests that a basic Marker History Citation search works
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


    def testCitationHistoryWildcardSearch(self):
        """
        @Status tests that a basic Marker History Citation search with wildcard works
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

    def testHistoryEventNotSpecifiedSearch(self):
        """
        @Status tests that a basic Marker History Event of Not Specified search works
        @see pwi-mrk-det-hist-search-10
        """
        driver = self.driver
        #finds the Event field and selects the option "Not Specified"
        Select(driver.find_element_by_id("markerHistoryEventID")).select_by_value('Not Specified')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #Iterate and print the search results column of Citation
        evt = table.get_column_cells('Event')
        evts = iterate.getTextAsList(evt)
        print evts
        #Assert the correct event searched is returned for the first result(Smim4)
        self.assertIn('Not Specified', evts)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Smim4'])

    def testHistoryEventSplitSearch(self):
        """
        @Status tests that a basic Marker History Event of Split search works
        @see pwi-mrk-det-hist-search-11
        """
        driver = self.driver
        #finds the Event field and selects the option "Split"
        Select(driver.find_element_by_id("markerHistoryEventID")).select_by_value('split')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #Iterate and print the search results column of Citation
        evt = table.get_column_cells('Event')
        evts = iterate.getTextAsList(evt)
        print evts
        #Assert the correct event searched is returned for the first result(Adam1a)
        self.assertIn('split', evts)

    def testHistoryEventReasonSearch(self):
        """
        @Status tests that a basic Marker History Event Reason search works
        @see pwi-mrk-det-hist-search-12
        """
        driver = self.driver
        #finds the Event Reason field and selects the option "per personal comm w/Chromosome Committee"
        Select(driver.find_element_by_id("markerHistoryEventReasonID")).select_by_value('per personal comm w/Chromosome Committee')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #Iterate and print the search results column of Reason
        evtr = table.get_column_cells('Reason')
        evtrs = iterate.getTextAsList(evtr)
        print evtrs
        #Assert the correct event reason searched is returned for the first result(Ak6)
        self.assertIn('per personal comm w/Chromosome Committee', evtrs)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Ak6', 'Comt', 'Cops7a', 'Dyrk1a', 'Pakap', 'Psme2b', 'D17Leh54', 'Rpl19-rs7'])

    def testHistoryModBySearch(self):
        """
        @Status tests that a basic Marker History Modified by search works
        @see pwi-mrk-det-hist-search-13
        """
        driver = self.driver
        #finds the Modified By field and enters a search name
        driver.find_element_by_id("markerHistoryModByID").send_keys('hjd')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #Iterate and print the search results column of Modified By
        modby = table.get_column_cells('Mod By')
        modbys = iterate.getTextAsList(modby)
        print modbys
        #Assert the correct Modified By searched is returned for the first result(Cdk12)
        self.assertIn('hjd', modbys)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Cdk12','Esd','Hat1','Kdm3b','Kdm6b','Lsm2','Myh10','Neu4','S100a16','Sptlc2','Tinf2','Actb-rs1','Actb-rs2'])

    def testHistoryModByWildcardSearch(self):
        """
        @Status tests that a basic Marker History Modified by search with wildcard works
        @see pwi-mrk-det-hist-search-14
        """
        driver = self.driver
        #finds the Modified By field and enters a search name with wildcard
        driver.find_element_by_id("markerHistoryModByID").send_keys('hj%')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #Iterate and print the search results column of Modified By
        modby = table.get_column_cells('Mod By')
        modbys = iterate.getTextAsList(modby)
        print modbys
        #Assert the correct Modified By searched is returned for the first result(Cdk12)
        self.assertIn('hjd', modbys)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Cdk12','Esd','Hat1','Kdm3b','Kdm6b','Lsm2','Myh10','Neu4','S100a16','Sptlc2','Tinf2','Actb-rs1','Actb-rs2'])

        
'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMrkSearch))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main()
            
