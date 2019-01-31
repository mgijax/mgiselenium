'''
Created on Jan 23, 2019

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

class TestMrkEditHist(unittest.TestCase):
    """
    @status Test Marker History search fields
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/marker")
        username = self.driver.find_element_by_name('user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = self.driver.find_element_by_name('password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = self.driver.find_element_by_name("submit") #Find the Login button
        submit.click() #click the login button
    
    def tearDown(self):
        self.driver.close()
        
    def testSymbolHistorySearch(self):
        """
        @Status tests that a basic Marker History Symbol search  works
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
        #Assert the correct marker symbols are returned for the first result(Pax1)
        self.assertEqual(symbols, ['Symbol','Hhg1','Hhg1','Shh','Dsh','Hx','Hx','Hx','Hxl3','Hxl3'])
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        # print all rows
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print symbols
        #assert all the correct symbols are returned
        self.assertEquals(symbols, ['Shh'])
     
        
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
        self.assertEquals(symbols, ['Ak6', 'Comt', 'Cops7a', 'Dyrk1a', 'Psme2b', 'D17Leh54', 'Rpl19-rs7'])

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
        modby = table.get_column_cells('Modified By')
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
        modby = table.get_column_cells('Modified By')
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
        
    def testSymbolHistoryEdit(self):
        """
        @Status tests that an edit of Marker History Symbol works
        @see pwi-mrk-det-hist-search-15
        """
        driver = self.driver
        #finds the history symbol field and enters a symbol
        driver.find_element_by_id("markerHistorySymbolID").send_keys('Dsh')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #click on the fifth row of data to set row to edit mode
        table.get_row(5).click()
        #find the symbol field of the 5th row and double click it to highlight and then send new text to the field all with actionChains
        sym_field = table.get_cell(5, 1).click()
        actionChains = ActionChains(driver)        
        actionChains.double_click(sym_field)
        actionChains.send_keys('Hxl3')
        actionChains.send_keys(Keys.TAB)
        actionChains.perform()
        time.sleep(2)
        #find and click the Modify button
        driver.find_element_by_id('updateMarkerButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #find the fifth row of data
        table.get_row(5)
        #find the symbol field of the 5th row 
        sym_field = table.get_cell(5, 1)
        print sym_field.text
        #Assert the symbol field is now displaying the symbol Hxl3
        self.assertEqual('Hxl3', sym_field.text)
        #find the symbol field of the 5th row
        sym = table.get_column_cells('Symbol')
        symbols = iterate.getTextAsList(sym)
        print symbols
        

    def testSymbolHistoryValidateEdit(self):
        """
        @Status tests that an edit of Marker History Symbol and validate works
        @see pwi-mrk-det-hist-search-16
        """
        driver = self.driver
        #finds the history symbol field and enters a symbol
        driver.find_element_by_id("markerHistorySymbolID").send_keys('Dsh')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #click on the fifth row of data to set row to edit mode
        table.get_row(5).click()
        #find the symbol field of the 5th row and double click it to highlight and then send new text to the field all with actionChains
        sym_field = table.get_cell(5, 1).click()
        actionChains = ActionChains(driver)        
        actionChains.double_click(sym_field)
        actionChains.send_keys('Dsh1')
        actionChains.send_keys(Keys.TAB)
        actionChains.perform()
        time.sleep(2)
        #switch to the popup alert box
        alert = self.driver.switch_to_alert()
        #get the alert box text
        alert_text = alert.text
        #Assert the correct alert text is displayed
        self.assertEqual('Marker Symbol could not be validated: Dsh1', alert_text)
        #click on alert OK button
        alert.accept()
           
    def testJnumHistoryEdit(self):
        """
        @Status tests that an edit of a J number History works
        @see pwi-mrk-det-hist-search-19
        """
        driver = self.driver
        #finds the history symbol field and enters a symbol
        driver.find_element_by_id("markerHistorySymbolID").send_keys('Dsh')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #click on the fifth row of data to set row to edit mode
        table.get_row(5).click()
        #find the J# field of the 5th row and double click it to highlight and then send new text to the field all with actionChains
        jnum_field = table.get_cell(5, 4).click()
        actionChains = ActionChains(driver)        
        actionChains.double_click(jnum_field)
        actionChains.send_keys('13476')
        actionChains.send_keys(Keys.TAB)
        actionChains.perform()
        time.sleep(2)
        #find and click the Modify button
        driver.find_element_by_id('updateMarkerButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #find the fifth row of data
        table.get_row(5)
        #find the symbol field of the 5th row and double click it to highlight and then send new text to the field all with actionChains
        jnum_field = table.get_cell(5, 4)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #find the J# column of the 5th row
        jnum = table.get_column_cells('J#')
        jnums = iterate.getTextAsList(jnum)
        print jnum_field.text
        print jnums
        #Assert the J# field is now displaying the J number J:13476
        self.assertEqual('J:13476', jnum_field.text)

    def testJnumHistoryValidateEdit(self):
        """
        @Status tests that an edit of J number History and validate works
        @see pwi-mrk-det-hist-search-20 
        """
        driver = self.driver
        #finds the Marker History field and enters a marker
        driver.find_element_by_id("markerHistorySymbolID").send_keys('Dsh')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the history results table
        history_table = self.driver.find_element_by_id("historyTable")
        table = Table(history_table)
        #click on the sixth row of data to set row to edit mode
        table.get_row(6).click()
        #find the J# field of the 6th row and double click it to highlight and then send new text to the field all with actionChains
        sym_field = table.get_cell(6, 4).click()
        actionChains = ActionChains(driver)        
        actionChains.double_click(sym_field)
        actionChains.send_keys('00000')
        actionChains.send_keys(Keys.TAB)
        actionChains.perform()
        time.sleep(2)
        #switch to the popup alert box
        alert = self.driver.switch_to_alert()
        #get the alert box text
        alert_text = alert.text
        #Assert the correct alert text is displayed
        self.assertEqual('Marker jnum could not be validated: J:00000', alert_text)
        #click on alert OK button
        alert.accept()
       
        
'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMrkSearch))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main()
            