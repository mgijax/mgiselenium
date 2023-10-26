'''
Created on Jun 26, 2017

@author: jeffc
Tests the results returned when doing certain queries.
'''
import unittest
import time
import tracemalloc
import config
import sys, os.path
# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests
tracemalloc.start()
class TestEiLitTriageSummarySearch(unittest.TestCase):
    """
    @status Test Literature Triage search results setup
    """

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1800, 1000)
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/triageFull")

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

    def testJournalFieldLinkSearch(self):
        """
        @Status tests that a DOI ID displays in the Journal column and the ID links correctly
        @see LitTri-sum-3 (4)
        """
        driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:130344')
        form.click_search()
        # finds the results table and iterates through the table
        table_element = self.driver.find_element(By.ID, "resultsTable")
        table = Table(table_element)
        # finds the DOI ID cell
        doi_cell = table.get_cell(1, 4)
        # asserts the link text found in the DOI ID column is correct
        self.assertEqual(doi_cell.text, '10.1073/pnas.0706671104')
        driver.find_element(By.LINK_TEXT, '10.1073/pnas.0706671104').click()
        # switches focus to the newly opened tab
        self.driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.a2a_listitem_custom:nth-child(2) > a:nth-child(1)')))
        page_title = driver.find_element(By.CSS_SELECTOR,
                                         '.article-container > article:nth-child(2) > header:nth-child(1) > div:nth-child(1) > h1:nth-child(2)')
        print(page_title.text)
        # asserts the page title for this page is correct
        self.assertEqual(page_title.text,
                         'Silencing of OB-RGRP in mouse hypothalamic arcuate nucleus increases leptin receptor signaling and prevents diet-induced obesity',
                         'Title is not displaying from source!')

    def testJournalFieldBlankSearch(self):
        """
        @Status tests that when a DOI ID does not exist the journal field is blank
        @see LitTri-sum-3 (5)
        """
        form = self.form
        form.enter_value('accids', 'J:305143')
        form.click_search()
        # finds the results table and iterates through the table
        table_element = self.driver.find_element(By.ID, "resultsTable")
        table = Table(table_element)
        # finds the DOI ID column
        doi_cell = table.get_cell(1, 4)
        # asserts the link text found in the DOI ID column is correct
        self.assertEqual(doi_cell.text, '')

    def testPubmedFieldLinkSearch(self):
        """
        @Status tests that a Pub Med ID displays in the PMID column and the ID links correctly
        @see LitTri-sum-4 (7)
        """
        driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:130344')
        form.click_search()
        # finds the results table and iterates through the table
        table_element = self.driver.find_element(By.ID, "resultsTable")
        table = Table(table_element)
        # finds the PMID column
        pmid_cell = table.get_cell(1, 3)
        # asserts the link text found in the PMID column is correct
        self.assertEqual(pmid_cell.text, '18042720')
        driver.find_element(By.LINK_TEXT, '18042720').click()
        # switches focus to the newly opened tab
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.search-input-link > a:nth-child(1)')))
        page_title = driver.find_element(By.CSS_SELECTOR, 'h1.heading-title:nth-child(2)')
        print(page_title.text)
        # asserts the page title for this page is correct
        self.assertEqual(page_title.text,
                         'Silencing of OB-RGRP in mouse hypothalamic arcuate nucleus increases leptin receptor signaling and prevents diet-induced obesity',
                         'Title is not displaying from source!')

    def testPubmedFieldBlankSearch(self):
        """
        @Status tests that when a Pub Med ID does not exist the PMID field is blank
        @see LitTri-sum-4 (8)
        """
        form = self.form
        form.enter_value('accids', 'J:23094')
        form.click_search()
        # finds the results table and iterates through the table
        table_element = self.driver.find_element(By.ID, "resultsTable")
        table = Table(table_element)
        # finds the PMID column
        pmid_cell = table.get_cell(1, 3)
        # asserts the link text found in the PMID column is correct
        self.assertEqual(pmid_cell.text, '')

    def testJNumResultSearch(self):
        """
        @Status tests that a J number displays in the J:# column
        @see LitTri-sum-5,28 (9)
        """
        form = self.form
        form.enter_value('accids', 'J:197100')
        form.click_search()
        # finds the results table and iterates through the table
        table_element = self.driver.find_element(By.ID, "resultsTable")
        table = Table(table_element)
        # finds the MGI column
        mgi_cell = table.get_cell(1, 1)
        # asserts the MGI ID found in the MGI column is correct
        self.assertEqual(mgi_cell.text, 'MGI:5490832')
        # finds the J number column
        jnum_cell = table.get_cell(1, 2)
        # asserts the link text found in the J:# column is correct
        self.assertEqual(jnum_cell.text, 'J:197100')

    def testShortCiteSearch(self):
        """
        @Status tests that the Short citation is correct when returning a result that has all the citation components  required
        @see LitTri-sum-6 (10)
        """
        form = self.form
        form.enter_value('accids', 'J:237402')
        form.click_search()
        # finds the results table and iterates through the table
        table_element = self.driver.find_element(By.ID, "resultsTable")
        table = Table(table_element)
        # finds the Short Citation column
        cite_cell = table.get_cell(1, 5)
        # asserts the link text found in the short citation column is correct
        self.assertEqual(cite_cell.text, 'Iwai-Takekoshi L, J Comp Neurol 2016 Dec 15;524(18):3696-3716')

    def testShortCiteNoPagesSearch(self):
        """
        @Status tests that the Short citation is correct when returning a result that has a citation where reference has no pages
        @see LitTri-sum-6 (12)
        """
        form = self.form
        form.enter_value('accids', 'J:148802')
        form.click_search()
        # finds the results table and iterates through the table
        table_element = self.driver.find_element(By.ID, "resultsTable")
        table = Table(table_element)
        # finds the short citation column
        cite_cell = table.get_cell(1, 5)
        # asserts the link text found in the short citation column is correct
        self.assertEqual(cite_cell.text, 'Boles MK, BMC Genet 2009;10():12')

    def testShortCiteBookSearch(self):
        """
        @Status tests that the Short citation is correct when returning a result that has a citation of a book
        @see LitTri-sum-6 (13)
        """
        form = self.form
        form.enter_value('accids', 'J:43743')
        form.click_search()
        # finds the results table and iterates through the table
        table_element = self.driver.find_element(By.ID, "resultsTable")
        table = Table(table_element)
        # finds the short citation column
        cite_cell = table.get_cell(1, 5)
        # asserts the link text found in the short citation column is correct
        self.assertEqual(cite_cell.text, 'Lyon MF, 1996;():')

    def testShortCiteNonLitSearch(self):
        """
        @Status tests that the Short citation is correct when returning a result that has a non-literature reference citation
        @see LitTri-sum-6 (14)
        """
        form = self.form
        form.enter_value('accids', 'J:175295')
        form.click_search()
        # finds the results table and iterates through the table
        table_element = self.driver.find_element(By.ID, "resultsTable")
        table = Table(table_element)
        # finds the short citation column
        cite_cell = table.get_cell(1, 5)
        # asserts the link text found in the short citation column is correct
        self.assertEqual(cite_cell.text,
                         'Mouse Genome Informatics and the Wellcome Trust Sanger Institute Mouse Genetics Project (MGP), Database Release 2011;():')

    def testTitleResultSearch(self):
        """
        @Status Tests that a search returns the correct Title for the reference.
        @See LitTri-sum-7 (15)
        """
        form = self.form
        form.enter_value('accids', 'J:237402')
        form.click_search()
        # finds the results table and iterates through the table
        table_element = self.driver.find_element(By.ID, "resultsTable")
        table = Table(table_element)
        # finds the Title column
        title_cell = table.get_cell(1, 6)
        # asserts the link text found in the title column is correct
        self.assertEqual(title_cell.text,
                         'Retinal pigment epithelial integrity is compromised in the developing albino mouse retina.')

    def testTitleNoResultSearch(self):
        """
        @Status Tests that a search returns No Title for the reference.
        @See LitTri-sum-7 (16)
        """
        form = self.form
        form.enter_value('accids', 'J:43743')
        form.click_search()
        # finds the results table and iterates through the table
        table_element = self.driver.find_element(By.ID, "resultsTable")
        table = Table(table_element)
        # finds the Title column
        title_cell = table.get_cell(1, 6)
        # asserts the link text found in the title column is correct
        self.assertEqual(title_cell.text, 'Genetic Variants and Strains of the Laboratory Mouse')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiLitTriageSummarySearch))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))