'''
Created on Jul 27, 2017
These tests are to confirm results you get back using various result requirements
@author: jeffc
'''
import unittest
from selenium import webdriver
import HTMLTestRunner
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate
from util.form import ModuleForm
from util.table import Table

# Tests

class TestLitDetail(unittest.TestCase):
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
        

    def testGoRefResult(self):
        """
        @Status tests that detail results for a result w/ GO Ref ID is correct
        @see MBIB-detail-1 (2)
        """
        #driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:161428')
        form.click_search()
        
        #finds the Reference Type field and return it's text value
        ref_type = self.driver.find_element_by_id("editTabRefType").get_attribute('value')
        print ref_type
        self.assertEqual(ref_type, 'MGI Curation Record')
        #finds the Authors field and return it's text value
        author = self.driver.find_element_by_id("editTabAuthors").get_attribute('value')
        print author
        self.assertEqual(author, 'Gaudet P; Livstone M; Thomas P; The Reference Genome Project 2010')
        #finds the Title field and return it's text value
        title = self.driver.find_element_by_id("editTabTitle").get_attribute('value')
        print title
        self.assertEqual(title, 'Annotation inferences using phylogenetic trees')
        
        #finds the Reference IDs table and iterates through the table
        table_element = self.driver.find_element_by_id("editRefIdTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        id_col = table.get_column_cells(1)
        ids = iterate.getTextAsList(id_col)
        print ids
        #asserts that the following J number & MGI number are returned
        self.assertIn('J:161428', ids)
        self.assertIn('MGI:4459044', ids)
        #finds the GO-REF field and return it's ID value
        go_ref = self.driver.find_element_by_id("editTabGorefid").get_attribute('value')
        print go_ref
        self.assertEqual(go_ref, 'GO_REF:0000033')
        
    def testRefwReftypeResult(self):
        """
        @Status tests that detail results for a result w/ Reference Type, pubmed ID, DOID is correct
        @see MBIB-detail-2,3,4,5,7 (5)
        """
        #driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:148145')
        form.click_search()
        
        #finds the Reference Type field and return it's text value
        ref_type = self.driver.find_element_by_id("editTabRefType").get_attribute('value')
        print ref_type
        self.assertEqual(ref_type, 'Peer Reviewed Article')
        #finds the Authors field and return it's text value
        author = self.driver.find_element_by_id("editTabAuthors").get_attribute('value')
        print author
        self.assertEqual(author, 'Gregg RG; Kamermans M; Klooster J; Lukasiewicz PD; Peachey NS; Vessey KA; McCall MA')
        #finds the Title field and return it's text value
        title = self.driver.find_element_by_id("editTabTitle").get_attribute('value')
        print title
        self.assertEqual(title, 'Nyctalopin expression in retinal bipolar cells restores visual function in a mouse model of complete X-linked congenital stationary night blindness.')
        #finds the Reference Type field and return it's text value
        journal = self.driver.find_element_by_id("editTabJournal").get_attribute('value')
        print journal
        self.assertEqual(journal, 'J Neurophysiol')
        #finds the Reference IDs table and iterates through the table
        table_element = self.driver.find_element_by_id("editRefIdTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        id_col = table.get_column_cells(1)
        ids = iterate.getTextAsList(id_col)
        print ids
        #asserts that the following J number & MGI number are returned
        self.assertIn('J:148145', ids)
        self.assertIn('MGI:3843587', ids)
        #finds the Pubmed field and return it's ID value
        pub_med = self.driver.find_element_by_id("editTabPubmedid").get_attribute('value')
        print pub_med
        self.assertEqual(pub_med, '17881478')    
        #finds the DOI field and return it's ID value
        do_id = self.driver.find_element_by_id("editTabDoiid").get_attribute('value')
        print do_id
        self.assertEqual(do_id, '10.1152/jn.00608.2007')    
        #finds the GO-REF field and return it's ID value(should be blank/empty)
        go_ref = self.driver.find_element_by_id("editTabGorefid").get_attribute('value')
        print go_ref
        self.assertEqual(go_ref, '')        
        
    def testisReviewResult(self):
        """
        @Status tests that detail results for a result w/ isReview set to yes is correct
        @see MBIB-detail-3 (6)
        """
        #driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:228427')
        form.click_search()
        
        #finds the isReviewed field and return it's text value(should be Yes)
        is_rvw = self.driver.find_element_by_id("refDataIsReview").get_attribute('value')
        print is_rvw
        self.assertEqual(is_rvw, 'Yes')
        #finds the Reference Type field and return it's text value
        journal = self.driver.find_element_by_id("editTabJournal").get_attribute('value')
        print journal
        self.assertEqual(journal, 'Cell Metab')
        
        #finds the Reference IDs table and iterates through the table
        table_element = self.driver.find_element_by_id("editRefIdTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        id_col = table.get_column_cells(1)
        ids = iterate.getTextAsList(id_col)
        print ids
        #asserts that the following J number & MGI number are returned
        self.assertIn('J:228427', ids)
        self.assertIn('MGI:5707085', ids)
        
    def testhasNoteResult(self):
        """
        @Status tests that detail results for a result w/ a note entry is correct
        @see MBIB-detail-6 (8)
        """
        #driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:233396')
        form.click_search()
        
        #finds the isReviewed field and return it's text value(should be Yes)
        is_rvw = self.driver.find_element_by_id("refDataIsReview").get_attribute('value')
        print is_rvw
        self.assertEqual(is_rvw, 'No')
        #finds the Notes field and return it's text value
        note = self.driver.find_element_by_id("editTabRefNote").get_attribute('value')
        print note
        self.assertEqual(note, 'disease= diabetes')
        
        #finds the Reference IDs table and iterates through the table
        table_element = self.driver.find_element_by_id("editRefIdTable")
        table = Table(table_element)
        #finds the J number column and returns all of this columns results
        id_col = table.get_column_cells(1)
        ids = iterate.getTextAsList(id_col)
        print ids
        #asserts that the following J number & MGI number are returned
        self.assertIn('J:233396', ids)
        self.assertIn('MGI:5784588', ids)        
        
    def testMultiFieldResult(self):
        """
        @Status tests that detail results for a result w/ Author,Journal,Date,Vol,Issue,Pages,Year is correct
        @see MBIB-detail-7,8,9,10,11,12 (9)
        """
        driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:63277')
        form.click_search()
        
        #finds the Authors field and return it's text value
        author = self.driver.find_element_by_id("editTabAuthors").get_attribute('value')
        print author
        self.assertEqual(author, 'Naylor MJ; Rancourt DE; Bech-Hansen NT')
        #finds the Title field and return it's text value
        title = self.driver.find_element_by_id("editTabTitle").get_attribute('value')
        print title
        self.assertEqual(title, 'Isolation and characterization of a calcium channel gene, Cacna1f, the murine orthologue of the gene for incomplete X-linked congenital stationary night blindness.')
        #finds the Reference Type field and return it's text value
        journal = self.driver.find_element_by_id("editTabJournal").get_attribute('value')
        print journal
        self.assertEqual(journal, 'Genomics')
        #finds the Date field and return it's text value
        ref_date = self.driver.find_element_by_id("editTabDate").get_attribute('value')
        print ref_date
        self.assertEqual(ref_date, '2000 Jun 15')
        #finds the Volume field and return it's text value
        ref_vol = self.driver.find_element_by_id("editTabVolume").get_attribute('value')
        print ref_vol
        self.assertEqual(ref_vol, '66')
        #finds the Issue field and return it's text value
        ref_issue = self.driver.find_element_by_id("editTabIssue").get_attribute('value')
        print ref_issue
        self.assertEqual(ref_issue, '3')
        #finds the Page field and return it's text value
        ref_page = self.driver.find_element_by_id("editTabPages").get_attribute('value')
        print ref_page
        self.assertEqual(ref_page, '324-7')
        #finds the Year field and return it's text value
        ref_year = self.driver.find_element_by_id("editTabYear").get_attribute('value')
        print ref_year
        self.assertEqual(ref_year, '2000')
        
    def testTitleSSResult(self):
        """
        @Status tests that detail results for a result w/ superscript in the title displays correctly
        @see MBIB-detail-4 (16)
        """
        driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:18640')
        form.click_search()
        
        #finds the Title field and return it's text value
        title = self.driver.find_element_by_id("editTabTitle").get_attribute('value')
        print title
        self.assertEqual(title, 'Allotyping C<m>a and C<m>b DNA and RNA')
        
        
'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSearch))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main()