'''
Created on Sep 7, 2016

This test verifies searching within the EmapA module, Both a term search and a stage search

@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
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

class TestEiGxdIndexSearch(unittest.TestCase):
    """
    @status Test GXD Index browser search using J number, marker symbol, ???
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/gxdindex")
    
    def tearDown(self):
        self.driver.close()
        

    def testJnumSearch(self):
        """
        @Status tests that a basic J number search works
        
        """
        driver = self.driver
        form = self.form
        form.enter_value('jnumid', '173543')
        form.click_search()
        #finds the citation field
        citation = form.get_value('citation')
        print(citation)
        self.assertEqual(citation, 'Harper J, Proc Natl Acad Sci U S A 2011 Jun 28;108(26):10585-90')
        #finds the marker field
        marker_symbol = form.get_value('marker_symbol')
        print(marker_symbol)
        self.assertEqual(marker_symbol, '1810065E05Rik')
        #finds the coded? field
        is_coded = form.get_value('is_coded')
        print(is_coded)
        self.assertEqual(is_coded, 'false')
        #finds the priority field
        priority = form.get_selected_text('_priority_key')
        print(priority)
        self.assertEqual(priority, 'High')
        #finds the conditional mutants field
        conditional = form.get_selected_text('_conditionalmutants_key')
        print(conditional)
        self.assertEqual(conditional, 'Conditional')
        #finds the created by field
        created_user = form.get_value('createdby_login')
        print(created_user)
        self.assertEqual(created_user, 'jx')
        #finds the modified by field
        modified_user = form.get_value('modifiedby_login')#.find_element_by_css_selector('td')
        print(modified_user)
        self.assertEqual(modified_user, 'jx')
        #finds the created by date field
        created_date = form.get_value('creation_date')
        print(created_date)
        self.assertEqual(created_date, '07/26/2011')
        #finds the created by date field
        modified_date = form.get_value('modification_date')
        print(modified_date)
        self.assertEqual(modified_date, '12/12/2011')
        
    def testInvalidJnumSearch(self):
        """
        @Status tests that an invalid J number search gives an error
        
        """
        form = self.form
        form.enter_value('jnumid', "99999999")
        form.press_tab()
        error = form.get_error_message()
        self.assertEqual("No Reference for J Number=J:99999999", error)
        
    def testMarkerSearch(self):
        """
        @Status Tests that a marker symbol search works, verifies the details of the first result listed
        
        """
        form = self.form
        form.enter_value('marker_symbol', 'Pax6')
        form.click_search()
        #finds the J number field
        jnumid = form.get_value('jnumid')
        print(jnumid)
        self.assertEqual(jnumid, 'J:278544')
        #finds the citation field
        citation = form.get_value('citation')
        print(citation)
        self.assertEqual(citation, 'Abdelhamed ZA, Sci Rep 2019 Apr 1;9(1):5446')
        #finds the coded? field
        is_coded = form.get_value('is_coded')
        print(is_coded)
        self.assertEqual(is_coded, 'false')
        #finds the priority field
        priority = form.get_selected_text('_priority_key')
        print(priority)
        self.assertEqual(priority, 'High')
        #finds the conditional field
        conditional = form.get_selected_text('_conditionalmutants_key')
        print(conditional)
        self.assertEqual(conditional, 'Not Applicable')
        #finds the created by field
        created_user = form.get_value('createdby_login')
        print(created_user)
        self.assertEqual(created_user, 'jfinger')
        #finds the modified by field
        modified_user = form.get_value('modifiedby_login')#.find_element_by_css_selector('td')
        print(modified_user)
        self.assertEqual(modified_user, 'jfinger')
        #finds the created by date field
        created_date = form.get_value('creation_date')
        print(created_date)
        self.assertEqual(created_date, '10/17/2019')
        #finds the created by date field
        modified_date = form.get_value('modification_date')
        print(modified_date)
        self.assertEqual(modified_date, '10/17/2019')
        
    def testMrkWildcardSearch(self):
        """
        @Status tests that a wildcard search for a marker works
        
        """
        form = self.form
        
        form.enter_value('marker_symbol', 'unc5%')
        form.enter_value('_priority_key', 'low')
        form.click_search()
        
        marker_symbol = form.get_value('marker_symbol')
        self.assertEqual(marker_symbol, 'Unc5a')
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))
        
        # print row 1
        cells = table.get_row_cells(1)
        print(iterate.getTextAsList(cells))
        #print column 1
        symbols_cells = table.get_column_cells('Marker')
        symbols = iterate.getTextAsList(symbols_cells)
        self.assertEqual(symbols, ['Marker','Unc5a', 'Unc5a', 'Unc5b', 'Unc5b', 'Unc5b', 'Unc5c', 'Unc5c', 'Unc5c', 'Unc5d', 'Unc5d', 'Unc5d'])
            
    def testCitationWildcardSearch(self):
        """
        @Status tests that a wildcard search for a citation works
        
        """
        form = self.form
        form.enter_value('citation', '%Blood 1991% ')
        form.click_search()
        marker_symbol = form.get_value('marker_symbol')
        self.assertEqual(marker_symbol, 'Ptpn1')
        #finds the citation field
        citation = form.get_value('citation')
        self.assertEqual(citation, 'Yi T, Blood 1991 Nov 1;78(9):2222-8')
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))
        # print row 1, the table headers
        cells = table.get_row_cells(1)
        print(iterate.getTextAsList(cells))
        #print column 1, the marker symbols
        symbols_cells = table.get_column_cells('Marker')
        symbols = iterate.getTextAsList(symbols_cells)
        self.assertEqual(symbols, ['Marker','Ptpn1', 'Ptpn12', 'Ptpn6', 'Ptpra', 'Ptprc', 'Ptpre', 'Ptprj'])
        
    def testNotesWildcardSearch(self):
        """
        @Status tests that a wildcard search for a noteworks
        
        """
        form = self.form
        form.enter_value('comments', '%slot%')
        form.press_tab()
        form.enter_value('_priority_key', 'High')
        form.press_tab()
        form.enter_value('_conditionalmutants_key', '4834242')
        form.press_tab()
        form.enter_value('is_coded', 'true')
        form.press_tab()
        form.click_search()
        note = form.get_value('comments')
        self.assertEqual(note, 'Some of the northern data was obtained using slot blots.  Age of embryo at noon of plug day not specified in reference.')
        #finds the citation field
        citation = form.get_value('citation')
        self.assertEqual(citation, 'Chianale J, Biochim Biophys Acta 1995 Dec 27;1264(3):369-76')
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))
        # print row 1, the table headers
        cells = table.get_row_cells(1)
        print(iterate.getTextAsList(cells))
        #print column 1, the marker symbols
        symbols_cells = table.get_column_cells('Marker')
        symbols = iterate.getTextAsList(symbols_cells)
        print(symbols)
        self.assertEqual(symbols, ['Marker','Abcb1a', 'Sdc1', 'Sptb', 'Sptbn1'])
                
    def testWithdrawnMrkSearch(self):
        """
        @Status tests that a search for a withdrawn marker gives an error
        """
        form = self.form
        form.enter_value('marker_symbol', 'dw')
        form.press_tab()
        error = form.get_error_message()
        # error message will display current symbol for dw
        self.assertIn("dw", error )
        # marker entry should be cleared
        marker_symbol = form.get_value('marker_symbol')
        self.assertEqual(marker_symbol, '')
        
    def testInvalidMrkSearch(self):
        """
        @Status tests that an error message is displayed when invalid marker symbol entered
        
        """
        form = self.form
        form.enter_value('marker_symbol', 'test12345')
        form.press_tab()
        error = form.get_error_message()
        self.assertEqual(error, "Invalid marker symbol test12345")
        # marker entry should be cleared
        marker_symbol = form.get_value('marker_symbol')
        self.assertEqual(marker_symbol, '')
        
    def testQTLErrorMsg(self):
        """
        @Status tests that an error message is displayed when selecting a QTL
        
        """
        form = self.form
        form.enter_value('marker_symbol', 'iba1')
        form.press_tab()
        error = form.get_error_message()
        self.assertEqual(error, "You selected a QTL type marker: Iba1")
        # marker should still be selected, even though error is displayed
        marker_symbol = form.get_value('marker_symbol')
        self.assertEqual(marker_symbol, 'Iba1')
        
    def testHeritPhenoMrkErrorMsg(self):
        """
        @Status tests that an error(Warning) message is displayed when selecting a heritable phenotypic marker
        
        """
        form = self.form
        form.enter_value('marker_symbol', 'act')
        form.press_tab()
        error = form.get_error_message()
        self.assertEqual(error, "You selected a heritable phenotypic marker: act")
        # marker should still be selected, even though warning error is displayed
        marker_symbol = form.get_value('marker_symbol')
        self.assertEqual(marker_symbol, 'act')
            
    def testMultipleMrkSearch(self):
        """
        @Status tests that a multiple marker search works
        """
        driver = self.driver
        form = self.form
        
        form.enter_value('marker_symbol', 't')
        form.press_tab()
        wait.forAngular(driver)
        
        # verify that display with two markers is shown
        mrkrows = driver.find_elements_by_css_selector(".markerSelections td")
        markers = [r.text for r in mrkrows]
        print(markers)
        self.assertEqual(len(markers), 2)
        self.assertEqual(markers[0], "t, t-complex, Chr 17, Band")
        self.assertEqual(markers[1], "T, brachyury, T-box transcription factor T, Chr 17, Band")
        
        #form.press_enter()
        mrkrows[1].click()
        wait.forAngular(driver)
        
        # marker T should be selected
        marker_symbol = form.get_value('marker_symbol')
        self.assertEqual(marker_symbol, 'T')
    
    def testMultiFieldSearch(self):
        """
        @Status tests that searching by marker, priority, conditional, and coded fields gives the correct results
        
        """
        form = self.form
        form.enter_value('marker_symbol', 'Bmp4')
        form.press_tab()
        form.enter_value('_priority_key', 'Medium')
        form.press_tab()
        form.enter_value('_conditionalmutants_key', 'Conditional')
        form.press_tab()
        form.enter_value('is_coded', 'Yes')
        form.press_tab()
        form.click_search()#click the search button
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))
        # print row 1
        cells = table.get_row_cells(1)
        print(iterate.getTextAsList(cells))
        #print column 1
        symbols_cells = table.get_column_cells('Marker')
        symbols = iterate.getTextAsList(symbols_cells)
        self.assertEqual(symbols, ['Marker', 'Bmp4', 'Bmp4', 'Bmp4', 'Bmp4', 'Bmp4', 'Bmp4', 'Bmp4', 'Bmp4'])

    def testCreatededBySearch(self):
        """
        @Status tests that searching the Created by user field gives the correct results
        
        """
        form = self.form
        form.enter_value('_priority_key', 'High')
        form.enter_value('_conditionalmutants_key', 'Conditional')
        form.enter_value('is_coded', 'Yes')
        form.enter_value('createdby_login', 'ijm')
        form.press_tab()
        form.click_search()#click the search button
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))
        # print row 1
        cells = table.get_row_cells(1)
        print(iterate.getTextAsList(cells))
        #print column 1
        symbols_cells = table.get_column_cells('Marker')
        symbols = iterate.getTextAsList(symbols_cells)
        self.assertEqual(symbols[1], 'Acta2')
        self.assertEqual(symbols[2], 'Aldob')
        self.assertEqual(symbols[3], 'Apob')
        self.assertEqual(symbols[4], 'Apoc2')
        self.assertEqual(symbols[5], 'Aqp4')
        
                        
    def testModifiedBySearch(self):
        """
        @Status tests that searching the Modified by user field gives the correct results
        
        """
        form = self.form
        form.enter_value('_priority_key', 'Medium')
        form.enter_value('_conditionalmutants_key', 'Conditional')
        form.enter_value('is_coded', 'Yes')
        form.enter_value('modifiedby_login', 'ijm')
        form.press_tab()
        form.click_search()#click the search button
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))
        # print row 1
        cells = table.get_row_cells(1)
        print(iterate.getTextAsList(cells))
        #print column 1
        symbols_cells = table.get_column_cells('Marker')
        symbols = iterate.getTextAsList(symbols_cells)
        self.assertEqual(symbols, ['Marker', 'Acta2', 'Fabp7', 'Hand1', 'Mbp'])
      
    
    def testCreateDateSearch(self):
        """
        @Status tests that searching by created date gives the correct results
        
        """
        form = self.form
        form.enter_value('creation_date', '05/06/2015')
        form.press_tab()
        form.click_search()#click the search button
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))
        # print row 1
        cells = table.get_row_cells(1)
        print(iterate.getTextAsList(cells))
        #print column 1
        symbols_cells = table.get_column_cells('Marker')
        symbols = iterate.getTextAsList(symbols_cells)
        self.assertEqual(symbols, ['Marker','Mbp', 'Sst'])
            
    def testModifyDateSearch(self):
        """
        @Status tests that searching by modified date gives the correct results
        
        """
        form = self.form
        form.enter_value('modification_date', '05/06/2015')
        form.press_tab()
        form.click_search()#click the search button
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))
        # print row 1
        cells = table.get_row_cells(1)
        print(iterate.getTextAsList(cells))
        #print column 1
        symbols_cells = table.get_column_cells('Marker')
        symbols = iterate.getTextAsList(symbols_cells)
        self.assertEqual(symbols, ['Marker', 'Emp1', 'Gcg', 'Gjb1', 'Gjc1', 'Mbp', 'Sst', 'Zdbf2'])
            
    def testLessThanDateSearch(self):
        """
        @Status tests that searching by less than created by date gives the correct results
        
        """
        form = self.form
        form.enter_value('_priority_key', 'Medium')
        form.press_tab()
        form.enter_value('_conditionalmutants_key', 'Conditional (minor)')
        form.press_tab()
        form.enter_value('is_coded', 'No')
        form.press_tab()
        form.enter_value('creation_date', '<05/06/2009')
        form.press_tab()
        form.click_search()#click the search button
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))
        # print row 1
        cells = table.get_row_cells(1)
        print(iterate.getTextAsList(cells))
        #print column 1
        symbols_cells = table.get_column_cells('Marker')
        symbols = iterate.getTextAsList(symbols_cells)
        self.assertEqual(symbols, ['Marker', 'En1', 'En2', 'Fgf17', 'Fgf8', 'Gbx2', 'Otx2', 'Spry1', 'Wnt1'])
            
    def testLessThanEqualDateSearch(self):
        """
        @Status tests that searching by less than created by date gives the correct results
        
        """
        form = self.form
        form.enter_value('_priority_key', 'Medium')
        form.press_tab()
        form.enter_value('_conditionalmutants_key', 'Conditional (minor)')
        form.press_tab()
        form.enter_value('is_coded', 'Yes')
        form.press_tab()
        form.enter_value('creation_date', "<=09/28/2010")
        form.press_tab()
        form.click_search()#click the search button
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))
        # print row 1
        cells = table.get_row_cells(1)
        print(iterate.getTextAsList(cells))
        #print column 1
        symbols_cells = table.get_column_cells('Marker')
        symbols = iterate.getTextAsList(symbols_cells)
        self.assertEqual(symbols, ['Marker', 'Clec1b', 'Fgf8', 'Lmx1b', 'Lyve1', 'Pdpn', 'Wnt7a'])
            
            
    
            
    def testBetweenDateSearch(self):
        """
        @Status tests that searching by inclusive dates gives the correct results
        
        """
        form = self.form
        form.enter_value('_priority_key', 'Medium')
        form.press_tab()
        form.enter_value('_conditionalmutants_key', 'Conditional')
        form.press_tab()
        form.enter_value('is_coded', 'Yes')
        form.press_tab()
        form.enter_value('creation_date', "10/01/2015..12/01/2015")
        form.press_tab()
        wait.forAngular(self.driver)
        form.click_search()#click the search button
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))
        # print row 1
        cells = table.get_row_cells(1)
        print(iterate.getTextAsList(cells))
        #print column 1
        symbols_cells = table.get_column_cells('Marker')
        symbols = iterate.getTextAsList(symbols_cells)
        self.assertEqual(symbols, ['Marker', 'Flrt3', 'Ntn1', 'Pecam1', 'Slit1', 'Tlx1'])
            
          
                  
    def testSearchIndex(self):
        """
        @Status tests that an index record(s) can be searched
        """
        driver = self.driver
        form = self.form
        #find the Index grid
        table_element = driver.find_element_by_id("indexGrid")
        table = Table(table_element)
        #puts an X in the first assay/age cell
        cell = table.get_cell(1,1)
        cell.click()
        #puts an X in the eighth assay row/fourth age cell
        cell = table.get_cell(8,4)
        cell.click()
        wait.forAngular(driver)
        form.click_search()#click the search button
        wait.forAngular(driver)
        #find the search results table
        results_table = driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))
        # print row 1
        cells = table.get_row_cells(1)
        print(iterate.getTextAsList(cells))
        #print column 1
        symbols_cells = table.get_column_cells('Marker')
        symbols = iterate.getTextAsList(symbols_cells)
        self.assertIn("Eed",symbols)
        
        
            
    #def testResultsTable(self):
        """
        An example of getting data from the results table using
            Table class
            
        NOTE: this is only for example purposes. Not a real test
        """
        #   driver = self.driver
        #  form = self.form
        
        #   form.enter_value('jnumid', '121946')
        #   form.press_tab()
        
        #   form.click_search()
        
        #   results_table = driver.find_element_by_id("indexGrid")
        #   table = Table(results_table)
        
        #   header_cells = table.get_header_cells()
        #   print iterate.getTextAsList(header_cells)
        # print row 1
        #   cells = table.get_row_cells(1)
        #   print iterate.getTextAsList(cells)
        # single cell
        #   cell = table.get_cell("RNA-WM", "10.5")
        #   print cell.text
        # empty cell
        #   cell = table.get_cell("prot-sxn", "A")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiGxdIndexSearch))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))