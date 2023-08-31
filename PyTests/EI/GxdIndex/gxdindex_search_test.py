'''
Created on Sep 7, 2016
This test verifies searching within the EmapA module, Both a term search and a stage search
@author: jeffc
Verify that a basic J number search works
Verify that a marker symbol search works, verifies the details of the first result listed
Verify that a wildcard search for a marker works
Verify that a wildcard search for a note works
Verify that a multiple marker search works
Verify that searching by marker, priority, conditional, and coded fields gives the correct results
Verify that searching the Created by user field gives the correct results
Verify that searching the Modified by user field gives the correct results
Verify that searching by created date gives the correct results
Verify that searching by modified date gives the correct results
Verify that searching by less than created by date gives the correct results
Verify that searching by less than created by date gives the correct results
Verify that searching by inclusive dates gives the correct results
Verify that an index record(s) can be searched
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import HtmlTestRunner
import sys,os.path
from selenium.webdriver.support.wait import WebDriverWait
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
        self.driver = webdriver.Firefox() 
        #self.driver = webdriver.Chrome()
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
        form.enter_value('jnumID', '173543')
        form.click_search()
        #finds the citation field
        citation = form.get_value('short_citation')
        print(citation)
        self.assertEqual(citation, 'Harper J, Proc Natl Acad Sci U S A 2011 Jun 28;108(26):10585-90')
        #finds the marker field
        marker_symbol = form.get_value('markerSymbol')
        print(marker_symbol)
        self.assertEqual(marker_symbol, '1810065E05Rik')
        #finds the coded? field
        is_coded = form.get_value('isFullCoded')
        print(is_coded)
        self.assertEqual(is_coded, 'string:0')#No option
        #finds the priority field
        priority = form.get_selected_text('priority')
        print(priority)
        self.assertEqual(priority, 'Low')
        #finds the conditional mutants field
        conditional = form.get_selected_text('conditional')
        print(conditional)
        self.assertEqual(conditional, 'Conditional')
        #finds the created by field
        created_user = form.get_value('createdBy')
        print(created_user)
        self.assertEqual(created_user, 'jx')
        #finds the modified by field
        modified_user = form.get_value('modifiedBy')#.find_element_by_css_selector('td')
        print(modified_user)
        self.assertEqual(modified_user, 'terryh')
        #finds the created by date field
        created_date = form.get_value('creationDate')
        print(created_date)
        self.assertEqual(created_date, '2011-07-26')
        #finds the created by date field
        modified_date = form.get_value('modificationDate')
        print(modified_date)
        self.assertEqual(modified_date, '2022-10-19')
        
    """def testInvalidJnumSearch(self):
        
        @Status tests that an invalid J number search gives an error
        this test can no longer work because the error is browser base so not accessible
        
        form = self.form
        form.enter_value('jnumID', "99999999")
        form.press_tab()
        error = form.get_error_message()
        self.assertEqual("No Reference for J Number=J:99999999", error)
        """
    def testMarkerSearch(self):
        """
        @Status Tests that a marker symbol search works, verifies the details of the first result listed
        
        """
        form = self.form
        form.enter_value('markerSymbol', 'Pax6')
        form.click_search()
        #finds the J number field
        jnumid = form.get_value('jnumID')
        print(jnumid)
        self.assertEqual(jnumid, 'J:193837')
        #finds the citation field
        citation = form.get_value('short_citation')
        print(citation)
        self.assertEqual(citation, 'Abdelhamed ZA, Hum Mol Genet 2013 Apr 1;22(7):1358-72')
        #finds the coded? field
        is_coded = form.get_value('isFullCoded')
        print(is_coded)
        self.assertEqual(is_coded, 'string:0')#No option
        #finds the priority field
        priority = form.get_selected_text('priority')
        print(priority)
        self.assertEqual(priority, 'Medium')
        #finds the conditional field
        conditional = form.get_selected_text('conditional')
        print(conditional)
        self.assertEqual(conditional, 'Not Applicable')
        #finds the created by field
        created_user = form.get_value('createdBy')
        print(created_user)
        self.assertEqual(created_user, 'terryh')
        #finds the modified by field
        modified_user = form.get_value('modifiedBy')#.find_element_by_css_selector('td')
        print(modified_user)
        self.assertEqual(modified_user, 'terryh')
        #finds the created by date field
        created_date = form.get_value('creationDate')
        print(created_date)
        self.assertEqual(created_date, '2013-03-26')
        #finds the created by date field
        modified_date = form.get_value('modificationDate')
        print(modified_date)
        self.assertEqual(modified_date, '2013-03-26')
        
    def testMrkWildcardSearch(self):
        """
        @Status tests that a wildcard search for a marker works
        
        """
        form = self.form
        
        form.enter_value('markerSymbol', 'unc5%')
        form.enter_value('priority', 'low')
        form.click_search()
        
        marker_symbol = form.get_value('markerSymbol')
        self.assertEqual(marker_symbol, 'Unc5a')
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results(first 4 results)
        row1 = table.get_row(0)
        row2 = table.get_row(1)
        row3 = table.get_row(2)
        row4 = table.get_row(3)
        row5 = table.get_row(4)
        #cells = table.get_row_cells(1)
        print(row1.text)
        print(row2.text)
        
        self.assertEqual(row1.text, 'Unc5a, J:103829, Chen B, Proc Natl Acad Sci U S A 2005 Nov 22;102(47):17184-9')
        self.assertEqual(row2.text, 'Unc5a, J:126240, Lu X, Nature 2004 Nov 11;432(7014):179-86')
        self.assertEqual(row3.text, 'Unc5b, J:103829, Chen B, Proc Natl Acad Sci U S A 2005 Nov 22;102(47):17184-9')
        self.assertEqual(row4.text, 'Unc5b, J:126240, Lu X, Nature 2004 Nov 11;432(7014):179-86')
        self.assertEqual(row5.text, 'Unc5c, J:108241, Desai J, Hum Mol Genet 2006 Apr 15;15(8):1329-41')
              
     
    """def testCitationWildcardSearch(self):
        
        @Status tests that a wildcard search for a citation works
        This test is no longer valid as wildcard search does not work for citation now.
        
        form = self.form
        form.enter_value('short_citation', '%Blood 1991% ')
        form.click_search()
        time.sleep(60)
        marker_symbol = form.get_value('markerSymbol')
        self.assertEqual(marker_symbol, 'Ptpn1')
        #finds the citation field
        citation = form.get_value('citation')
        self.assertEqual(citation, 'Yi T, Blood 1991 Nov 1;78(9):2222-8')
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
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
        """
    def testNotesWildcardSearch(self):
        """
        @Status tests that a wildcard search for a note works
        
        """
        self.driver.find_element(By.ID, 'note').send_keys('%RT-PCR data%')
        Select(self.driver.find_element(By.ID, 'priority')).select_by_value('string:74714')#High option
        Select(self.driver.find_element(By.ID, 'conditional')).select_by_value('string:4834242')#not applicable option 
        Select(self.driver.find_element(By.ID, 'isFullCoded')).select_by_value('string:1')#Yes option
        self.driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the note field
        noteinfo = self.driver.find_element(By.ID, 'note')
        #self.assertEqual(noteinfo.text, 'Age of embryo at noon of plug day not specified in reference.  Some of the RT-PCR data was obtained using quantitative RT-PCR.')
        #finds the citation field
        citation = self.driver.find_element(By.ID, 'short_citation')
        #self.assertEqual(citation.text, 'Haitchi HM, Eur Respir J 2009 May;33(5):1095-104')
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results(first 4 results)
        row1 = table.get_row(0)
        row2 = table.get_row(1)
        row3 = table.get_row(2)
        row4 = table.get_row(3)
        row5 = table.get_row(4)
        #cells = table.get_row_cells(1)
        print(row1.text)
        print(row2.text)
        
        self.assertEqual(row1.text, '1110017D15Rik, J:180800, Haitchi HM, Eur Respir J 2009 May;33(5):1095-104')
        self.assertEqual(row2.text, 'Ace2, J:183115, Song R, Pediatr Res 2012 Jan;71(1):13-9')
        self.assertEqual(row3.text, 'Acta1, J:194471, Borensztein M, Development 2013 Mar;140(6):1231-9')
        self.assertEqual(row4.text, 'Actc1, J:194471, Borensztein M, Development 2013 Mar;140(6):1231-9')
        self.assertEqual(row5.text, 'Afp, J:187541, Schievenbusch S, Stem Cells Dev 2012 Sep 20;21(14):2656-66')
              
                
    """def testWithdrawnMrkSearch(self):
        
        @Status tests that a search for a withdrawn marker gives an error
        This test can no longer capture the error as it's now a browser error that can't be captured!
        
        #self.driver.find_element(By.ID, 'markerSymbol').send_keys('dw')
        form = self.form
        form.enter_value('markerSymbol', 'dw')
        form.press_tab()
        error = form.get_error_message()
        # error message will display current symbol for dw
        self.assertIn("dw", error )
        # marker entry should be cleared
        marker_symbol = form.get_value('markerSymbol')
        self.assertEqual(marker_symbol, '')
     """   
    """def testInvalidMrkSearch(self):
        
        @Status tests that an error message is displayed when invalid marker symbol entered
        @bug is this still a valid  test?
        
        form = self.form
        form.enter_value('markerSymbol', 'test12345')
        form.press_tab()
        error = form.get_error_message()
        self.assertEqual(error, "Invalid marker symbol test12345")
        # marker entry should be cleared
        marker_symbol = form.get_value('markerSymbol')
        self.assertEqual(marker_symbol, '')
        """
    """def testQTLErrorMsg(self):
        
        @Status tests that an error message is displayed when selecting a QTL
        @bug is this still a valid  test?
        
        form = self.form
        form.enter_value('markerSymbol', 'iba1')
        form.press_tab()
        error = form.get_error_message()
        self.assertEqual(error, "You selected a QTL type marker: Iba1")
        # marker should still be selected, even though error is displayed
        marker_symbol = form.get_value('markerSymbol')
        self.assertEqual(marker_symbol, 'Iba1')
        """
    """def testHeritPhenoMrkErrorMsg(self):
        
        @Status tests that an error(Warning) message is displayed when selecting a heritable phenotypic marker
        @bug is this still a valid  test?
        
        form = self.form
        form.enter_value('markerSymbol', 'act')
        form.press_tab()
        error = form.get_error_message()
        self.assertEqual(error, "You selected a heritable phenotypic marker: act")
        # marker should still be selected, even though warning error is displayed
        marker_symbol = form.get_value('markerSymbol')
        self.assertEqual(marker_symbol, 'act')
        """    
    def testMultipleMrkSearch(self):
        """
        @Status tests that a multiple marker search works
        """
        self.driver.find_element(By.ID, 'markerSymbol').send_keys("t")#marker symbol
        self.driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results(first 4 results)
        row1 = table.get_row(0)
        row2 = table.get_row(1)        
        #assert the results  are  the correct marker symbol
        self.assertEqual(row1.text, 'T, J:91405, Abdelkhalek HB, Genes Dev 2004 Jul 15;18(14):1725-36')
        self.assertEqual(row2.text, 'T, J:314668, Abrams SR, Elife 2021 Oct 21;10():e68558')
        
    
    def testMultiFieldSearch(self):
        """
        @Status tests that searching by marker, priority, conditional, and coded fields gives the correct results
        
        """
        self.driver.find_element(By.ID, 'markerSymbol').send_keys("Bmp4")#marker symbol
        Select(self.driver.find_element(By.ID, 'priority')).select_by_value('string:74715')#Medium option
        Select(self.driver.find_element(By.ID, 'conditional')).select_by_value('string:4834240')#conditional option 
        Select(self.driver.find_element(By.ID, 'isFullCoded')).select_by_value('string:1')#Yes option
        self.driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results(first 4 results)
        row1 = table.get_row(0)
        row2 = table.get_row(1)
        row3 = table.get_row(2)
        row4 = table.get_row(3)
        row5 = table.get_row(4)
        #cells = table.get_row_cells(1)
        print(row1.text)
        print(row2.text)
        
        self.assertEqual(row1.text, 'Bmp4, J:153554, Chen J, Dev Biol 2009 Oct 1;334(1):174-85')
        self.assertEqual(row2.text, 'Bmp4, J:206541, Engelhard C, Elife 2013;2():e01160')
        self.assertEqual(row3.text, 'Bmp4, J:138379, Gu S, Mech Dev 2008 Aug;125(8):729-42')
        self.assertEqual(row4.text, 'Bmp4, J:231083, Hines EA, Dev Dyn 2016 Apr;245(4):497-507')
        self.assertEqual(row5.text, 'Bmp4, J:138715, Li WY, Mech Dev 2008 Sep-Oct;125(9-10):874-82')
              
  
    def testCreatededBySearch(self):
        """
        @Status tests that searching the Created by user field gives the correct results
        
        """
        Select(self.driver.find_element(By.ID, 'priority')).select_by_value('string:74714')#High option
        Select(self.driver.find_element(By.ID, 'conditional')).select_by_value('string:4834240')#conditional option 
        Select(self.driver.find_element(By.ID, 'isFullCoded')).select_by_value('string:1')#Yes option
        self.driver.find_element(By.ID, 'createdBy').send_keys("ijm")
        self.driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results(first 4 results)
        row1 = table.get_row(0)
        row2 = table.get_row(1)
        row3 = table.get_row(2)
        row4 = table.get_row(3)
        row5 = table.get_row(4)
        #cells = table.get_row_cells(1)
        print(row1.text)
        print(row2.text)
        
        self.assertEqual(row1.text, 'Acan, J:110714, Barrionuevo F, Dev Biol 2006 Jul 1;295(1):128-40')
        self.assertEqual(row2.text, 'Acta2, J:124920, Garrison WD, Gastroenterology 2006 Apr;130(4):1207-20')
        self.assertEqual(row3.text, 'Adm, J:265444, Matsumoto L, J Clin Invest 2018 Jul 2;128(7):3186-3197')
        self.assertEqual(row4.text, 'Akt1, J:265444, Matsumoto L, J Clin Invest 2018 Jul 2;128(7):3186-3197')
        self.assertEqual(row5.text, 'Aldob, J:124920, Garrison WD, Gastroenterology 2006 Apr;130(4):1207-20')
              
                        
    def testModifiedBySearch(self):
        """
        @Status tests that searching the Modified by user field gives the correct results
        
        """
        Select(self.driver.find_element(By.ID, 'priority')).select_by_value('string:74715')#Medium option
        Select(self.driver.find_element(By.ID, 'conditional')).select_by_value('string:4834240')#conditional option 
        Select(self.driver.find_element(By.ID, 'isFullCoded')).select_by_value('string:1')#Yes option
        self.driver.find_element(By.ID, 'modifiedBy').send_keys("ijm")
        self.driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results(first 4 results)
        row1 = table.get_row(0)
        row2 = table.get_row(1)
        row3 = table.get_row(2)
        row4 = table.get_row(3)
        row5 = table.get_row(4)
        #cells = table.get_row_cells(1)
        print(row1.text)
        print(row2.text)
        
        self.assertEqual(row1.text, 'Acta2, J:152859, Varadkar PA, Genesis 2009 Aug;47(8):573-8')
        self.assertEqual(row2.text, 'Ascl1, J:220452, Nasif S, Proc Natl Acad Sci U S A 2015 Apr 14;112(15):E1861-70')
        self.assertEqual(row3.text, 'Fabp7, J:98585, Stolt CC, Dev Biol 2005 May 15;281(2):309-17')
        self.assertEqual(row4.text, 'Hand1, J:152859, Varadkar PA, Genesis 2009 Aug;47(8):573-8')
        self.assertEqual(row5.text, 'Mbp, J:98585, Stolt CC, Dev Biol 2005 May 15;281(2):309-17')
      
    
    def testCreateDateSearch(self):
        """
        @Status tests that searching by created date gives the correct results
        
        """
        #Select(self.driver.find_element(By.ID, 'priority')).select_by_value('string:74716')#Low option
        #Select(self.driver.find_element(By.ID, 'conditional')).select_by_value('string:4834242')#Not Applicable option 
        #Select(self.driver.find_element(By.ID, 'isFullCoded')).select_by_value('string:0')#No option
        self.driver.find_element(By.ID, 'creationDate').send_keys("05/06/2015")
        self.driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results(first 4 results)
        row1 = table.get_row(0)
        row2 = table.get_row(1)
        #cells = table.get_row_cells(1)
        print(row1.text)
        print(row2.text)
        
        self.assertEqual(row1.text, 'Mbp, J:142504, Park J, J Neurosci 2008 Nov 26;28(48):12815-9')
        self.assertEqual(row2.text, 'Sst, J:53372, Charollais A, Dev Genet 1999;24(1-2):13-26')
        
            
    def testModifyDateSearch(self):
        """
        @Status tests that searching by modified date gives the correct results
        
        """
        Select(self.driver.find_element(By.ID, 'priority')).select_by_value('string:74716')#Low option
        Select(self.driver.find_element(By.ID, 'conditional')).select_by_value('string:4834242')#Not Applicable option 
        Select(self.driver.find_element(By.ID, 'isFullCoded')).select_by_value('string:0')#No option
        self.driver.find_element(By.ID, 'modificationDate').send_keys("<05/06/2009")
        self.driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results(first 4 results)
        row1 = table.get_row(1)
        row2 = table.get_row(2)
        row3 = table.get_row(3)
        row4 = table.get_row(4)
        #cells = table.get_row_cells(1)
        print(row1.text)
        print(row2.text)
        print(row3.text)
        print(row4.text)
        
        self.assertEqual(row1.text, 'Acadm, J:106993, Briancon N, EMBO J 2006 Mar 22;25(6):1253-62')
        self.assertEqual(row2.text, 'Acox1, J:106993, Briancon N, EMBO J 2006 Mar 22;25(6):1253-62')
        self.assertEqual(row3.text, 'Acox1, J:91859, Yubero P, Endocrinology 2004 Sep;145(9):4268-77')
        self.assertEqual(row4.text, 'Acox2, J:91859, Yubero P, Endocrinology 2004 Sep;145(9):4268-77')   
        
            
    def testLessThanDateSearch(self):
        """
        @Status tests that searching by less than created by date gives the correct results
        
        """
        Select(self.driver.find_element(By.ID, 'priority')).select_by_value('string:74715')#Medium option
        Select(self.driver.find_element(By.ID, 'conditional')).select_by_value('string:4834241')#Conditional (minor) option 
        Select(self.driver.find_element(By.ID, 'isFullCoded')).select_by_value('string:0')#No option
        self.driver.find_element(By.ID, 'creationDate').send_keys("<05/06/2009")
        self.driver.find_element(By.ID, 'searchButton').click()
        time.sleep(1)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results(first 4 results)
        row1 = table.get_row(1)
        row2 = table.get_row(2)
        row3 = table.get_row(3)
        row4 = table.get_row(4)
        #cells = table.get_row_cells(1)
        print(row1.text)
        print(row2.text)
        print(row3.text)
        print(row4.text)
        
        self.assertEqual(row1.text, 'Acta2, J:102947, Wilm B, Development 2005 Dec;132(23):5317-28')
        self.assertEqual(row2.text, 'Adar, J:87714, Wang Q, J Biol Chem 2004 Feb 6;279(6):4952-61')
        self.assertEqual(row3.text, 'Aldh1a2, J:103924, Tarchini B, Genes Dev 2005 Dec 1;19(23):2862-76')
        self.assertEqual(row4.text, 'Arr3, J:103124, Wang Y, Development 2005 Nov;132(22):5103-13')   
        
            
    def testLessThanEqualDateSearch(self):
        """
        @Status tests that searching by less than created by date gives the correct results
        
        """
        Select(self.driver.find_element(By.ID, 'priority')).select_by_value('string:74715')#Medium option
        Select(self.driver.find_element(By.ID, 'conditional')).select_by_value('string:4834241')#Conditional (minor) option 
        Select(self.driver.find_element(By.ID, 'isFullCoded')).select_by_value('string:1')#Yes option
        self.driver.find_element(By.ID, 'creationDate').send_keys("<=09/28/2010")
        self.driver.find_element(By.ID, 'searchButton').click()
        time.sleep(1)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results(first 4 results)
        row1 = table.get_row(1)
        row2 = table.get_row(2)
        row3 = table.get_row(3)
        row4 = table.get_row(4)
        #cells = table.get_row_cells(1)
        print(row1.text)
        print(row2.text)
        print(row3.text)
        print(row4.text)
        
        self.assertEqual(row1.text, 'Atoh1, J:102293, Matei V, Dev Dyn 2005 Nov;234(3):633-50')
        self.assertEqual(row2.text, 'Bdnf, J:102293, Matei V, Dev Dyn 2005 Nov;234(3):633-50')
        self.assertEqual(row3.text, 'Clec1b, J:162815, Bertozzi CC, Blood 2010 Jul 29;116(4):661-70')
        self.assertEqual(row4.text, 'Cryaa, J:101730, Yoshimoto A, Development 2005 Oct;132(20):4437-48')   
            
    def testBetweenDateSearch(self):
        """
        @Status tests that searching by inclusive dates gives the correct results
        
        """
        Select(self.driver.find_element(By.ID, 'priority')).select_by_value('string:74715')#Medium option
        Select(self.driver.find_element(By.ID, 'conditional')).select_by_value('string:4834241')#Conditional (minor) option 
        Select(self.driver.find_element(By.ID, 'isFullCoded')).select_by_value('string:1')#Yes option
        self.driver.find_element(By.ID, 'creationDate').send_keys("10/01/2015..12/01/2015")
        self.driver.find_element(By.ID, 'searchButton').click()
        #find the search results table
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results(first 4 results)
        row1 = table.get_row(0)
        row2 = table.get_row(1)
        row3 = table.get_row(2)
        row4 = table.get_row(3)
        row5 = table.get_row(4)
        row6 = table.get_row(5)
        row7 = table.get_row(6)
        row8 = table.get_row(7)
        #print the first 4 row of results
        print(row1.text)
        print(row2.text)
        print(row3.text)
        print(row4.text)
        #assert the 8 results returned are correct
        self.assertEqual(row1.text, 'Acta2, J:225159, Rudat C, PLoS One 2014;9(11):e112112')
        self.assertEqual(row2.text, 'Aqp2, J:225159, Rudat C, PLoS One 2014;9(11):e112112')
        self.assertEqual(row3.text, 'Emcn, J:225159, Rudat C, PLoS One 2014;9(11):e112112')
        self.assertEqual(row4.text, 'Postn, J:225159, Rudat C, PLoS One 2014;9(11):e112112')
        self.assertEqual(row5.text, 'Tagln, J:225159, Rudat C, PLoS One 2014;9(11):e112112')
        self.assertEqual(row6.text, 'Upk1b, J:225159, Rudat C, PLoS One 2014;9(11):e112112')
        self.assertEqual(row7.text, 'Upk3a, J:225159, Rudat C, PLoS One 2014;9(11):e112112')
        self.assertEqual(row8.text, 'Upk3b, J:225159, Rudat C, PLoS One 2014;9(11):e112112')   
        

    def testSearchIndex(self):
        """
        @Status tests that an index record(s) can be searched
        """
        driver = self.driver
        form = self.form
        #find the Index grid
        table_element = driver.find_element(By.ID, "indexGrid")
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
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results(first 4 results)
        row1 = table.get_row(0)
        row2 = table.get_row(1)
        row3 = table.get_row(2)
        row4 = table.get_row(3)
        row5 = table.get_row(4)
        row6 = table.get_row(5)
        row7 = table.get_row(6)
        row8 = table.get_row(7)
        #print the first 4 row of results
        print(row1.text)
        print(row2.text)
        print(row3.text)
        print(row4.text)
        #assert the 8 results returned are correct
        self.assertEqual(row1.text, 'Adipoq, J:170133, Kim ST, Hum Reprod 2011 Jan;26(1):82-95')
        self.assertEqual(row2.text, 'Adipor1, J:170133, Kim ST, Hum Reprod 2011 Jan;26(1):82-95')
        self.assertEqual(row3.text, 'Adipor2, J:170133, Kim ST, Hum Reprod 2011 Jan;26(1):82-95')
        self.assertEqual(row4.text, 'Bmi1, J:134477, Puschendorf M, Nat Genet 2008 Apr;40(4):411-20')
        self.assertEqual(row5.text, 'Cbx2, J:134477, Puschendorf M, Nat Genet 2008 Apr;40(4):411-20')
        self.assertEqual(row6.text, 'Cbx5, J:315732, Meglicki M, Cell Cycle 2012 Jun 1;11(11):2189-205')
        self.assertEqual(row7.text, 'Cnot3, J:316544, Zheng X, Stem Cell Reports 2016 Nov 8;7(5):897-910')
        self.assertEqual(row8.text, 'Dnmt1, J:76510, Ratnam S, Dev Biol 2002 May 15;245(2):304-14')   
               
            
    """def testResultsTable(self):
        
        An example of getting data from the results table using
            Table class
            
        NOTE: this is only for example purposes. Not a real test
        
        #   driver = self.driver
        #  form = self.form
        
        #   form.enter_value('jnumid', '121946')
        #   form.press_tab()
        
        #   form.click_search()
        
        #   results_table = driver.find_element(By.ID, "indexGrid")
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
        """

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiGxdIndexSearch))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))