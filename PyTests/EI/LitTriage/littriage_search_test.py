'''
Created on June 13, 2017

This test verifies searching within the Lit Triage module.

@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import HTMLTestRunner
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

class TestLitSearch(unittest.TestCase):
    """
    @status Test Literature Triage search using J number, etc
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/triage")
    
    def tearDown(self):
        self.driver.close()
        

    def testJnumSearch(self):
        """
        @Status tests that a basic J number search works
        @see MBIB-search-1 (1)
        """
        driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:237402')
        form.click_search()
        #finds the results table and iterates through the table
        result = self.driver.find_element_by_id("resultsTable")
        data = result.find_elements_by_tag_name("td")
        print iterate.getTextAsList(data)
        #finds the Journal field
        Journal = data[0].text
        self.assertEqual(Journal, '10.1002/cne.24025')
        #finds the pmid by field
        PubMedID = data[1].text
        self.assertEqual(PubMedID, '27097562')
        #finds the J number field
        Jnumber = data[2].text
        self.assertEqual(Jnumber, 'J:237402')
        #finds the short citation field
        ShortCite = data[3].text
        self.assertEqual(ShortCite, 'Iwai-Takekoshi L, J Comp Neurol 2016 Dec 15;524(18):3696-3716')
        #finds the title field
        Title = data[4].text
        self.assertEqual(Title, 'Retinal pigment epithelial integrity is compromised in the developing albino mouse retina.')
        
    def testInvalidJnumSearch(self):
        """
        @Status tests that an invalid J number search gives no result back
        @See MBIB-search-2 (2)
        """
        form = self.form
        form.enter_value('accids', "99999999")
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cells = table.get_column_cells(2)
        jnums = iterate.getTextAsList(jnum_cells)
        self.assertEqual(jnums, [''])
        
    def testMultiJnumCommaSearch(self):
        """
        @Status Tests that a list of multiple comma separated J numbers returns the correct J number results
        @See MBIB-search-3 (3)
        """
        form = self.form
        form.enter_value('accids', 'J:173534, J:155845, J:151466, J:136110, J:75187, J:43743, J:23392, J:23389, J:109968, J:182573, J:134667')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cells = table.get_column_cells(2)
        jnums = iterate.getTextAsList(jnum_cells)
        self.assertEquals(jnums, ['','J:136110','J:75187','J:151466','J:23392','J:109968','J:134667','J:155845','J:182573','J:43743','J:173534','J:23389'])
        
    def testMultiJnumSpaceSearch(self):
        """
        @Status Tests that a list of multiple space separated J numbers returns the correct J number results
        @See MBIB-search-3 (5)
        """
        form = self.form
        form.enter_value('accids', 'J:173534 J:155845 J:151466 J:136110 J:75187 J:43743 J:23392 J:23389 J:109968 J:182573 J:134667')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cells = table.get_column_cells(2)
        jnums = iterate.getTextAsList(jnum_cells)
        print jnums
        self.assertEquals(jnums, ['','J:136110','J:75187','J:151466','J:23392','J:109968','J:134667','J:155845','J:182573','J:43743','J:173534','J:23389'])
                       
            
    def testPubMedSearch(self):
        """
        @Status Tests that a search of a Pub Med ID returns the correct J number results
        @See MBIB-search-4 (7)
        """
        form = self.form
        form.enter_value('accids', '10321434')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cell = table.get_cell(1,2)
        #jnum = iterate.getTextAsList(jnum_cells)
        self.assertEqual(jnum_cell.text, 'J:54446')
              
    def testMGIIDSearch(self):
        """
        @Status Tests that a search of an MGI ID returns the correct J number results
        @See MBIB-search-5 (9)
        """
        form = self.form
        form.enter_value('accids', 'MGI:62396')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cell = table.get_cell(1,2)
        #jnum = iterate.getTextAsList(jnum_cells)
        self.assertEqual(jnum_cell.text, 'J:14223')
            
    def testDOIIDSearch(self):
        """
        @Status Tests that a search of a DOI ID returns the correct J number results
        @See MBIB-search-6 (11)
        """
        form = self.form
        form.enter_value('accids', '10.1534/genetics.114.161455')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cell = table.get_cell(1,2)
        #jnum = iterate.getTextAsList(jnum_cells)
        self.assertEqual(jnum_cell.text, 'J:212979')
              
    def testGOIDSearch(self):
        """
        @Status Tests that a search of a GO ID returns the correct J number results
        @See MBIB-search-7 (14)
        """
        form = self.form
        form.enter_value('accids', 'GO_REF:0000033')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cell = table.get_cell(1,2)
        #jnum = iterate.getTextAsList(jnum_cells)
        self.assertEqual(jnum_cell.text, 'J:161428')

    def testTitleExactSearch(self):
        """
        @Status Tests that a search of an exact match title returns the correct J number results.
        @See MBIB-search-9 (17)
        """
        form = self.form
        form.enter_value('title', 'Rescue of the albino phenotype by introduction of a functional tyrosinase gene into mice.')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cell = table.get_cell(1,2)
        #jnum = iterate.getTextAsList(jnum_cells)
        self.assertEqual(jnum_cell.text, 'J:19279')
        
    def testTypeAbstractSearch(self):
        """
        @Status Tests that a search of Reference Type and a partial text abstract with wildcard returns the correct J number results
        @See MBIB-search-22 (58)
        @bug: Test no complete yet, need the Type field added first.
        """
        form = self.form
        form.enter_value('reference_type', 'book')
        form.enter_value('title', 'P-selectin%')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cell = table.get_cell(1,2)
        #jnum = iterate.getTextAsList(jnum_cells)
        self.assertEqual(jnum_cell.text, 'J:28109')
    
    def testTitleAuthorNoteSearch(self):
        """
        @Status Tests that a search of an partial title, partial Author and a partial note with wildcard returns the correct J number results
        @See MBIB-search-21 (59)
        """
        form = self.form
        form.enter_value('authors', '%gal%')
        form.enter_value('title', '%night blindness%')
        form.enter_value('notes', '%allele%')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cell = table.get_cell(1,2)
        #jnum = iterate.getTextAsList(jnum_cells)
        self.assertEqual(jnum_cell.text, 'J:41368')
    
    def testJournalYearVolumeIssuePagesSearch(self):
        """
        @Status Tests that a search of Journal, Year, Volume, Issue, and Pages returns the correct J number results
        @See MBIB-search-21 (60)
        """
        form = self.form
        form.enter_value('journal', 'Nature')
        form.enter_value('year', '2012')
        form.enter_value('volume', '485')
        form.enter_value('issue', '7396')
        form.enter_value('pages', '128%')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cell = table.get_cell(1,2)
        #jnum = iterate.getTextAsList(jnum_cells)
        self.assertEqual(jnum_cell.text, 'J:183831')

    def testAuthorJournalDateSearch(self):
        """
        @Status Tests that a search of Author, Journal, and Date returns the correct J number results
        @See MBIB-search-21 (61)
        """
        form = self.form
        form.enter_value('authors', '%hall%')
        form.enter_value('journal', '%brain%')
        form.enter_value('date', '2007 Dec 5')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cell = table.get_cell(1,2)
        #jnum = iterate.getTextAsList(jnum_cells)
        self.assertEqual(jnum_cell.text, 'J:128739')

    def testYearAuthorReviewTitleSearch(self):
        """
        @Status Tests that a search of Year, Author, is Reviewed, and Title returns the correct J number results
        @See MBIB-search-21 (62)
        """
        form = self.form
        form.enter_value('year', '2000')
        form.enter_value('authors', '%Junker%')
        form.enter_value('is_review', 'Y')
        form.enter_value('title', '%cancer%')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cell = table.get_cell(1,2)
        self.assertEqual(jnum_cell.text, 'J:63615')
     
    def testAPStatusSearch(self):
        """
        @Status Tests that a search for a single AP status returns the correct results
        @See MBIB-search-23,25 (63)
        """
        self.driver.find_element_by_id('status_AP_Rejected').click()
        form = self.form
        form.enter_value('title', 'diabetes%')
        form.enter_value('journal', '%diab%')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cells = table.get_column_cells(2)
        jnums = iterate.getTextAsList(jnum_cells)
        print jnums
        JnumbersReturned = iterate.getTextAsList(jnum_cells)
        #asserts that the following J numbers are returned
        self.assertIn('J:120220', JnumbersReturned)
        self.assertIn('J:107890', JnumbersReturned)
        self.assertIn('J:45421', JnumbersReturned)
        
    def testMultiTumorStatusSearch(self):
        """
        @Status Tests that a search for multple Tumor statuses returns the correct results
        @See MBIB-search-24,25 (70)
        """
        self.driver.find_element_by_id('status_Tumor_Indexed').click()
        self.driver.find_element_by_id('status_Tumor_Fully_curated').click()
        form = self.form
        form.enter_value('year', '1957')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cells = table.get_column_cells(2)
        jnums = iterate.getTextAsList(jnum_cells)
        print jnums
        JnumbersReturned = iterate.getTextAsList(jnum_cells)
        #asserts that the following J numbers are returned
        self.assertIn('J:27973', JnumbersReturned)
        self.assertIn('J:2403', JnumbersReturned)
                
        
    def testStatusAllareasSearch(self):
        """
        @Status Tests that a search for results with a status in each group returns the correct results
        @See MBIB-search-24,25 (73)
        """
        self.driver.find_element_by_id('status_AP_Rejected').click()
        self.driver.find_element_by_id('status_GO_Rejected').click()
        self.driver.find_element_by_id('status_GXD_Rejected').click()
        self.driver.find_element_by_id('status_QTL_Rejected').click()
        self.driver.find_element_by_id('status_Tumor_Rejected').click()
        form = self.form
        form.enter_value('title', '%night blindness%')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cells = table.get_column_cells(2)
        jnums = iterate.getTextAsList(jnum_cells)
        print jnums               
        JnumbersReturned = iterate.getTextAsList(jnum_cells)
        
        #asserts that the following J number is returned
        self.assertIn('J:63277', JnumbersReturned) # All workflow groups are rejected
        
    def testStatusComboSearch(self):
        """
        @Status Tests that a search for results with multiple status with other fields combined returns the correct results
        @See MBIB-search-24,25 (76)
        """
        self.driver.find_element_by_id('status_AP_Chosen').click()
        self.driver.find_element_by_id('status_GO_Chosen').click()
        self.driver.find_element_by_id('status_GXD_Chosen').click()
        self.driver.find_element_by_id('status_QTL_Chosen').click()
        self.driver.find_element_by_id('status_Tumor_Chosen').click()
        self.driver.find_element_by_id('status_AP_Indexed').click()
        self.driver.find_element_by_id('status_GO_Indexed').click()
        self.driver.find_element_by_id('status_GXD_Indexed').click()
        self.driver.find_element_by_id('status_QTL_Indexed').click()
        self.driver.find_element_by_id('status_Tumor_Indexed').click()
        self.driver.find_element_by_id('status_Tumor_Fully_curated').click()
        form = self.form
        form.enter_value('title', '%quantitative trait loci%')
        form.enter_value('year', '2016')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cells = table.get_column_cells(2)
        jnums = iterate.getTextAsList(jnum_cells)
        print jnums               
        JnumbersReturned = iterate.getTextAsList(jnum_cells)
        
        #asserts that the following J number is returned
        self.assertIn('J:237788', JnumbersReturned) # Matches to both QTL statuses selected.
        self.assertIn('J:237571', JnumbersReturned)
        self.assertIn('J:231948', JnumbersReturned)
'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSearch))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main()