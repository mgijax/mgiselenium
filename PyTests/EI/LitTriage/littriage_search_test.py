'''
Created on June 13, 2017

This test verifies searching within the Lit Triage module.

@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
        Journal = data[1].text
        self.assertEqual(Journal, '10.1002/cne.24025')
        #finds the pmid by field
        PubMedID = data[2].text
        self.assertEqual(PubMedID, '27097562')
        #finds the J number field
        Jnumber = data[3].text
        self.assertEqual(Jnumber, 'J:237402')
        #finds the short citation field
        ShortCite = data[4].text
        self.assertEqual(ShortCite, 'Iwai-Takekoshi L, J Comp Neurol 2016 Dec 15;524(18):3696-3716')
        #finds the title field
        Title = data[5].text
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
        jnum_cells = table.get_column_cells(3)
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
        jnum_cells = table.get_column_cells(3)
        jnums = iterate.getTextAsList(jnum_cells)
        print jnums
        self.assertEquals(jnums, ['','J:182573', 'J:173534', 'J:155845', 'J:151466', 'J:136110', 'J:134667', 'J:109968', 'J:75187', 'J:43743', 'J:23392', 'J:23389'])
        
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
        jnum_cells = table.get_column_cells(3)
        jnums = iterate.getTextAsList(jnum_cells)
        print jnums
        self.assertEquals(jnums, ['','J:182573', 'J:173534', 'J:155845', 'J:151466', 'J:136110', 'J:134667', 'J:109968', 'J:75187', 'J:43743', 'J:23392', 'J:23389'])
                       
            
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
        jnum_cell = table.get_cell(1,3)
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
        jnum_cell = table.get_cell(1,3)
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
        jnum_cell = table.get_cell(1,3)
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
        jnum_cell = table.get_cell(1,3)
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
        jnum_cell = table.get_cell(1,3)
        #jnum = iterate.getTextAsList(jnum_cells)
        self.assertEqual(jnum_cell.text, 'J:19279')
        
    def testTypeAbstractSearch(self):
        """
        @Status Tests that a search of Reference Type and a partial text abstract with wildcard returns the correct J number results
        @See MBIB-search-22 (58)
        """
        form = self.form
        form.enter_value('reference_type', 'book')
        form.enter_value('title', 'P-selectin%')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cell = table.get_cell(1,3)
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
        jnum_cell = table.get_cell(1,3)
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
        jnum_cell = table.get_cell(1,3)
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
        jnum_cell = table.get_cell(1,3)
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
        jnum_cell = table.get_cell(1,3)
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
        jnum_cells = table.get_column_cells(3)
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
        self.driver.find_element_by_id('status_Tumor_Full_coded').click()
        form = self.form
        form.enter_value('year', '1957')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cells = table.get_column_cells(3)
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
        jnum_cells = table.get_column_cells(3)
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
        self.driver.find_element_by_id('status_Tumor_Full_coded').click()
        form = self.form
        form.enter_value('title', '%quantitative trait loci%')
        form.enter_value('year', '2016')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        jnum_cells = table.get_column_cells(3)
        jnums = iterate.getTextAsList(jnum_cells)
        print jnums               
        JnumbersReturned = iterate.getTextAsList(jnum_cells)
        
        #asserts that the following J number is returned
        self.assertIn('J:237788', JnumbersReturned) # Matches to both QTL statuses selected.
        self.assertIn('J:242947', JnumbersReturned)
        self.assertIn('J:231948', JnumbersReturned)
        
    def testDiscardSearch(self):
        """
        @Status Tests that a search for results with Only Discard returns the correct results
        @See MBIB-search-26 (78)
        """
        #This finds the pull down menu for Discard? and then selects the second option
        dl = self.driver.find_element_by_id('is_discard')
        for option in dl.find_elements_by_tag_name("option"):
            if option.text == 'Only Discard':
                option.click()
                break
        form = self.form
        form.click_search() 
        #Confirms that the MGI Discard box is checked(selected)
        self.driver.find_element_by_id("editTabIsDiscard").is_selected()

    def testSingleTagSearch(self):
        """
        @Status Tests that a search of a single workflow tag returns the correct results
        @See MBIB-search-27 (81)
        """
        form = self.form
        form.enter_value('year', '2003')
        form.enter_value('workflow_tag1', 'MGI:NoAbstract')
        form.enter_value('title', '%anemia%')
        form.click_search()
        #finds the Tag list and verifies the required tag is listed.
        table_element = self.driver.find_element_by_id("editTabTags")
        table = Table(table_element)
        #finds the selected tags column and verified it contains the added tag
        sel_tags = table.get_column_cells(1)
        used_tags = iterate.getTextAsList(sel_tags)
        print used_tags
        #asserts that the following J numbers are returned
        self.assertIn('MGI:NoAbstract', used_tags)
         
    def testMultiStatusORSearch(self):
        """
        @Status tests that searching for multiple statuses on multiple workflows(OR) returns correct results
        @see MBIB-search-28 (87)
        """
        form = self.form
        time.sleep(5)
        form.enter_value('title', '%cancer%')
        form.enter_value('year', '2007')
        self.driver.find_element_by_id("status_AP_Indexed").click()
        self.driver.find_element_by_id("status_AP_Full_coded").click()
        self.driver.find_element_by_id("status_GO_Indexed").click()
        self.driver.find_element_by_id("status_GO_Full_coded").click()
        #Do not need to click the OR option because that is the default selection.
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("editTabWorkFlowStatus")
        table = Table(table_element)
        #finds the Indexed column for AP and returns it's status of selected
        ap_indexed = table.get_cell(1,3)
        self.assertTrue(ap_indexed.is_selected, "Indexed for AP is not selected")
        #finds the Full Coded column for AP and returns it's status of selected
        ap_full_coded = table.get_cell(1,6)
        self.assertTrue(ap_full_coded.is_selected, "Full Coded for AP is not selected")
        #finds the Indexed column for GO and returns it's status of selected
        go_indexed = table.get_cell(2,3)
        self.assertTrue(go_indexed.is_selected, "Indexed for GO is not selected")     
        #finds the Full Coded column for GO and returns it's status of selected
        go_full_coded = table.get_cell(2,6)
        self.assertTrue(go_full_coded.is_selected, "Full Coded for GO is not selected")
        #finds the 1st and 6th fields of the summary table for AP and GO indexed and Full-coded columns and returns text value
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        ap_cell1 = table.get_cell(4,6)
        ap_cell2 = table.get_cell(5,6)
        go_cell1 = table.get_cell(3,7)
        go_cell2 = table.get_cell(2,7)
        time.sleep(1)
        self.assertEquals(ap_cell1.text, "Indexed", 'AP is not routed')
        self.assertEquals(ap_cell2.text, "Full-coded", 'AP is not full-coded')
        self.assertEquals(go_cell1.text, "Full-coded", 'GO is not routed')
        self.assertEquals(go_cell2.text, "Indexed", 'GO is not full-coded')
        print ap_cell1.text
        print ap_cell2.text
        print go_cell1.text
        print go_cell2.text
        
    def testMultiStatusANDSearch(self):
        """
        @Status tests that searching for multiple statuses on multiple workflows(OR) returns correct results
        @see MBIB-search-28 (88) 
        @bug: needs work because data has changed, not finding resultTable cells correctly!!!
        """
        form = self.form
        time.sleep(5)
        form.enter_value('title', '%cancer%')
        form.enter_value('year', '2016')
        self.driver.find_element(By.ID, 'status_AP_Routed').click()
        self.driver.find_element(By.ID, 'status_AP_Indexed').click()
        self.driver.find_element(By.ID, 'status_GO_Routed').click()
        self.driver.find_element(By.ID, 'status_GO_Indexed').click()
        #click the AND option
        self.driver.find_element(By.XPATH, "//input[@value='AND']").click()
        
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element(By.ID, 'editTabWorkFlowStatus')
        table = Table(table_element)
        #finds the Routed column for AP and returns it's status of selected
        ap_routed = table.get_cell(2,3)
        self.assertTrue(ap_routed.is_selected, "Routed for AP is not selected")
        #finds the Full Coded column for AP and returns it's status of selected
        ap_indexed = table.get_cell(1,3)
        self.assertTrue(ap_indexed.is_selected, "Indexed for AP is not selected")
        #finds the Routed column for GO and returns it's status of selected
        go_routed = table.get_cell(2,4)
        self.assertTrue(go_routed.is_selected, "Routed for GO is not selected")     
        #finds the Full Coded column for GO and returns it's status of selected
        go_indexed = table.get_cell(5,4)
        self.assertTrue(go_indexed.is_selected, "Indexed for GO is not selected")
        #finds the 1st and 2nd fields of the summary table for AP and GO routed and Full-coded columns and returns text value
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        ap_cell1 = table.get_cell(1,6)
        ap_cell2 = table.get_cell(2,6)
        go_cell1 = table.get_cell(8,7)
        go_cell2 = table.get_cell(1,7)
        
        time.sleep(2)
        self.assertEquals(ap_cell1.text, "Routed", 'AP is not indexed')
        self.assertEquals(ap_cell2.text, "Indexed", 'AP is not routed')
        self.assertEquals(go_cell1.text, "Routed", 'GO is not rejected')
        self.assertEquals(go_cell2.text, "Indexed", 'GO is not indexed')
        print ap_cell1.text
        print ap_cell2.text
        print go_cell1.text
        print go_cell2.text
        
'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLitSearch))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main()
    