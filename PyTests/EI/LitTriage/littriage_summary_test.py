'''
Created on Jun 26, 2017

@author: jeffc
Tests the results returned when doing certain queries.
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

class TestEiLitTriageSummarySearch(unittest.TestCase):
    """
    @status Test Literature Triage search results setup
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/triageFull")
    
    def tearDown(self):
        self.driver.close()
        

    def testJournalFieldLinkSearch(self):
        """
        @Status tests that a DOI ID displays in the Journal column and the ID links correctly
        @see MBIB-sum-3 (4)
        """
        driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:130344')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the DOI ID cell
        doi_cell = table.get_cell(1,4)
        #asserts the link text found in the DOI ID column is correct
        self.assertEqual(doi_cell.text, '10.1073/pnas.0706671104')
        driver.find_element_by_link_text('10.1073/pnas.0706671104').click()
        #switches focus to the newly opened tab
        driver.switch_to_window(driver.window_handles[-1])
        page_title = driver.find_element_by_id('page-title')
        print(page_title.text)
        #asserts the page title for this page is correct
        self.assertEqual(page_title.text, 'Silencing of OB-RGRP in mouse hypothalamic arcuate nucleus increases leptin receptor signaling and prevents diet-induced obesity', 'Title is not displaying from source!')
        
    def testJournalFieldBlankSearch(self):
        """
        @Status tests that when a DOI ID does not exist the journal field is blank
        @see MBIB-sum-3 (5)
        """
        form = self.form
        form.enter_value('accids', 'J:41759')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the DOI ID column
        doi_cell = table.get_cell(1,4)
        #asserts the link text found in the DOI ID column is correct
        self.assertEqual(doi_cell.text, '')
        
    def testPubmedFieldLinkSearch(self):
        """
        @Status tests that a Pub Med ID displays in the PMID column and the ID links correctly
        @see MBIB-sum-4 (7)
        """
        driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:130344')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the PMID column
        pmid_cell = table.get_cell(1,3)
        #asserts the link text found in the PMID column is correct
        self.assertEqual(pmid_cell.text, '18042720')
        driver.find_element_by_link_text('18042720').click()
        #switches focus to the newly opened tab
        driver.switch_to_window(driver.window_handles[-1])
        page_title = driver.find_element_by_id('heading').find_element_by_tag_name('h1')
        print(page_title.text)
        #asserts the page title for this page is correct
        self.assertEqual(page_title.text, 'Silencing of OB-RGRP in mouse hypothalamic arcuate nucleus increases leptin receptor signaling and prevents diet-induced obesity', 'Title is not displaying from source!')
        
    def testPubmedFieldBlankSearch(self):
        """
        @Status tests that when a Pub Med ID does not exist the PMID field is blank
        @see MBIB-sum-4 (8)
        """
        form = self.form
        form.enter_value('accids', 'J:23094')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the PMID column
        pmid_cell = table.get_cell(1,3)
        #asserts the link text found in the PMID column is correct
        self.assertEqual(pmid_cell.text, '')

    def testJNumResultSearch(self):
        """
        @Status tests that a J number displays in the J:# column
        @see MBIB-sum-5,28 (9)
        """
        form = self.form
        form.enter_value('accids', 'J:197100')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the MGI column
        mgi_cell = table.get_cell(1,1)
        #asserts the MGI ID found in the MGI column is correct
        self.assertEqual(mgi_cell.text, 'MGI:5490832')
        #finds the J number column
        jnum_cell = table.get_cell(1,2)
        #asserts the link text found in the J:# column is correct
        self.assertEqual(jnum_cell.text, 'J:197100')

    def testShortCiteSearch(self):
        """
        @Status tests that the Short citation is correct when returning a result that has all the citation components  required
        @see MBIB-sum-6 (10)
        """
        form = self.form
        form.enter_value('accids', 'J:237402')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the Short Citation column
        cite_cell = table.get_cell(1,5)
        #asserts the link text found in the short citation column is correct
        self.assertEqual(cite_cell.text, 'Iwai-Takekoshi L, J Comp Neurol 2016 Dec 15;524(18):3696-3716')
    
    def testShortCiteNoPagesSearch(self):
        """
        @Status tests that the Short citation is correct when returning a result that has a citation where reference has no pages
        @see MBIB-sum-6 (12)
        """
        form = self.form
        form.enter_value('accids', 'J:148802')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the short citation column
        cite_cell = table.get_cell(1,5)
        #asserts the link text found in the short citation column is correct
        self.assertEqual(cite_cell.text, 'Boles MK, BMC Genet 2009;10():12')
    
    def testShortCiteBookSearch(self):
        """
        @Status tests that the Short citation is correct when returning a result that has a citation of a book
        @see MBIB-sum-6 (13)
        """
        form = self.form
        form.enter_value('accids', 'J:43743')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the short citation column
        cite_cell = table.get_cell(1,5)
        #asserts the link text found in the short citation column is correct
        self.assertEqual(cite_cell.text, 'Lyon MF, 1996;():')
    
    def testShortCiteNonLitSearch(self):
        """
        @Status tests that the Short citation is correct when returning a result that has a non-literature reference citation
        @see MBIB-sum-6 (14)
        """
        form = self.form
        form.enter_value('accids', 'J:175295')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the short citation column
        cite_cell = table.get_cell(1,5)
        #asserts the link text found in the short citation column is correct
        self.assertEqual(cite_cell.text, 'Mouse Genome Informatics and the Wellcome Trust Sanger Insti, Database Release 2011;():')
    
    def testTitleResultSearch(self):
        """
        @Status Tests that a search returns the correct Title for the reference.
        @See MBIB-sum-7 (15)
        """
        form = self.form
        form.enter_value('accids', 'J:237402')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the Title column
        title_cell = table.get_cell(1,6)
        #asserts the link text found in the title column is correct
        self.assertEqual(title_cell.text, 'Retinal pigment epithelial integrity is compromised in the developing albino mouse retina.')
        
    def testTitleNoResultSearch(self):
        """
        @Status Tests that a search returns No Title for the reference.
        @See MBIB-sum-7 (16)
        """
        form = self.form
        form.enter_value('accids', 'J:43743')
        form.click_search()
        #finds the results table and iterates through the table
        table_element = self.driver.find_element_by_id("resultsTable")
        table = Table(table_element)
        #finds the Title column
        title_cell = table.get_cell(1,6)
        #asserts the link text found in the title column is correct
        self.assertEqual(title_cell.text, '')
           
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiLitTriageSummarySearch))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))