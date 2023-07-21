'''
Created on Jul 27, 2017
These tests are to confirm results you get back using various result requirements
@author: jeffc
'''
import unittest
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys, os.path

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)
import time
import config
from util import iterate
from util.form import ModuleForm
from util.table import Table


# Tests
tracemalloc.start()
class TestEiLitTriageDetail(unittest.TestCase):
    """
    @status Test Literature Triage search using J number, etc
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/triageFull")

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

    def testGoRefResult(self):
        """
        @Status tests that detail results for a result w/ GO Ref ID is correct
        @see LitTri-detail-1 (2)
        """
        # driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:161428')
        form.click_search()
        # finds the Reference Type field and return it's value; 31576686 = MGI Curation Record
        ref_type = self.driver.find_element(By.ID, "editTabRefType").get_attribute('value')
        print(ref_type)
        self.assertEqual(ref_type, '31576686')
        # finds the Authors field and return it's text value
        author = self.driver.find_element(By.ID, "editTabAuthors").get_attribute('value')
        print(author)
        self.assertEqual(author, 'Gaudet P; Livstone M; Thomas P; The Reference Genome Project 2010')
        # finds the Title field and return it's text value
        title = self.driver.find_element(By.ID, "editTabTitle").get_attribute('value')
        print(title)
        self.assertEqual(title, 'Annotation inferences using phylogenetic trees')

        # finds the Reference IDs table and iterates through the table
        table_element = self.driver.find_element(By.ID, "resultsTable")
        table = Table(table_element)
        # finds the J number column and returns all of this columns results
        id_col = table.get_column_cells(1)
        ids = iterate.getTextAsList(id_col)

        # finds the GO-REF field and return it's ID value
        go_ref = self.driver.find_element(By.ID, "gorefId").get_attribute('value')
        print(go_ref)
        self.assertEqual(go_ref, 'GO_REF:0000033')

    def testRefwReftypeResult(self):
        """
        @Status tests that detail results for a result w/ Reference Type, pubmed ID, DOID is correct
        @see LitTri-detail-2,3,4,5,7 (5)
        """
        # driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:148145')
        form.click_search()
        # finds the Reference Type field and return it's value; 31576687 = Peer Reviewed Article
        ref_type = self.driver.find_element(By.ID, "editTabRefType").get_attribute('value')
        print(ref_type)
        self.assertEqual(ref_type, '31576687')
        # finds the Authors field and return it's text value
        author = self.driver.find_element(By.ID, "editTabAuthors").get_attribute('value')
        print(author)
        self.assertEqual(author, 'Gregg RG; Kamermans M; Klooster J; Lukasiewicz PD; Peachey NS; Vessey KA; McCall MA')
        # finds the Title field and return it's text value
        title = self.driver.find_element(By.ID, "editTabTitle").get_attribute('value')
        print(title)
        self.assertEqual(title,
                         'Nyctalopin expression in retinal bipolar cells restores visual function in a mouse model of complete X-linked congenital stationary night blindness.')
        # finds the Reference Type field and return it's text value
        journal = self.driver.find_element(By.ID, "editTabJournal").get_attribute('value')
        print(journal)
        self.assertEqual(journal, 'J Neurophysiol')
        # finds the Reference IDs table and iterates through the table
        table_element = self.driver.find_element(By.ID, "resultsTable")
        table = Table(table_element)
        # finds the J number column and returns all of this columns results
        id_col = table.get_column_cells(1)
        ids = iterate.getTextAsList(id_col)

        # finds the Pubmed field and return it's ID value
        pub_med = self.driver.find_element(By.ID, "pubmedId").get_attribute('value')
        print(pub_med)
        self.assertEqual(pub_med, '17881478')
        # finds the DOI field and return it's ID value
        do_id = self.driver.find_element(By.ID, "doiId").get_attribute('value')
        print(do_id)
        self.assertEqual(do_id, '10.1152/jn.00608.2007')
        # finds the GO-REF field and return it's ID value(should be blank/empty)
        go_ref = self.driver.find_element(By.ID, "gorefId").get_attribute('value')
        print(go_ref)
        self.assertEqual(go_ref, '')

    def testisReviewResult(self):
        """
        @Status tests that detail results for a result w/ isReview set to yes is correct
        @see LitTri-detail-3 (6)
        """
        # driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:228427')
        form.click_search()
        # finds the isReviewed field and return it's value of 1(1 is equal to Yes)
        is_rvw = self.driver.find_element(By.ID, "refDataIsReview").get_attribute('value')
        print(is_rvw)
        self.assertEqual(is_rvw, '1')
        # finds the Reference Type field and return it's text value
        journal = self.driver.find_element(By.ID, "editTabJournal").get_attribute('value')
        print(journal)
        self.assertEqual(journal, 'Cell Metab')

    def testhasNoteResult(self):
        """
        @Status tests that detail results for a result w/ a note entry is correct
        @see LitTri-detail-6 (8)
        """
        # driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:233396')
        form.click_search()
        # finds the isReviewed field and return it's value of 0(0 is equal to No)
        is_rvw = self.driver.find_element(By.ID, "refDataIsReview").get_attribute('value')
        print(is_rvw)
        self.assertEqual(is_rvw, '0')
        # finds the Notes field and return it's text value
        note = self.driver.find_element(By.ID, "editTabRefNote").get_attribute('value')
        print(note)
        self.assertEqual(note, 'disease= diabetes')

    def testMultiFieldResult(self):
        """
        @Status tests that detail results for a result w/ Author,Journal,Date,Vol,Issue,Pages,Year is correct
        @see LitTri-detail-7,8,9,10,11,12 (9)
        """
        driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:63277')
        form.click_search()
        # finds the Authors field and return it's text value
        author = self.driver.find_element(By.ID, "editTabAuthors").get_attribute('value')
        print(author)
        self.assertEqual(author, 'Naylor MJ; Rancourt DE; Bech-Hansen NT')
        # finds the Title field and return it's text value
        title = self.driver.find_element(By.ID, "editTabTitle").get_attribute('value')
        print(title)
        self.assertEqual(title,
                         'Isolation and characterization of a calcium channel gene, Cacna1f, the murine orthologue of the gene for incomplete X-linked congenital stationary night blindness.')
        # finds the Reference Type field and return it's text value
        journal = self.driver.find_element(By.ID, "editTabJournal").get_attribute('value')
        print(journal)
        self.assertEqual(journal, 'Genomics')
        # finds the Date field and return it's text value
        ref_date = self.driver.find_element(By.ID, "editTabDate").get_attribute('value')
        print(ref_date)
        self.assertEqual(ref_date, '2000 Jun 15')
        # finds the Volume field and return it's text value
        ref_vol = self.driver.find_element(By.ID, "editTabVolume").get_attribute('value')
        print(ref_vol)
        self.assertEqual(ref_vol, '66')
        # finds the Issue field and return it's text value
        ref_issue = self.driver.find_element(By.ID, "editTabIssue").get_attribute('value')
        print(ref_issue)
        self.assertEqual(ref_issue, '3')
        # finds the Page field and return it's text value
        ref_page = self.driver.find_element(By.ID, "editTabPages").get_attribute('value')
        print(ref_page)
        self.assertEqual(ref_page, '324-7')
        # finds the Year field and return it's text value
        ref_year = self.driver.find_element(By.ID, "editTabYear").get_attribute('value')
        print(ref_year)
        self.assertEqual(ref_year, '2000')

    def testTitleSSResult(self):
        """
        @Status tests that detail results for a result w/ superscript in the title displays correctly
        @see LitTri-detail-4 (16)
        """
        driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:18640')
        form.click_search()
        # finds the Title field and return it's text value
        title = self.driver.find_element(By.ID, "editTabTitle").get_attribute('value')
        print(title)
        self.assertEqual(title, 'Allotyping C<sup>m</sup>a and C<sup>m</sup>b DNA and RNA,')

    def testAlleleAssocTable(self):
        """
        @Status tests that the Allele Associations table displays correctly for a reference with associations
        @see LitTri-allele-assoc-1
        """
        # driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:7537')
        form.click_search()
        # find the Allele Associations button and click it
        self.driver.find_element(By.ID, 'alleleTabButton').click()
        # finds the Allele Association table and gets the first row of data
        type_used = self.driver.find_elements(By.CLASS_NAME, 'alleleAssocType')[0].get_property(
            'value')  # value will be 1017 which associates to 'Used-FC'
        allele_used = self.driver.find_elements(By.CLASS_NAME, "alleleSymbol")[0].get_property('value')
        allele_id = self.driver.find_elements(By.CLASS_NAME, "alleleAccID")[0].get_property('value')
        mrk = self.driver.find_elements(By.CLASS_NAME, 'alleleMarkerSymbol')[0]
        print(type_used)
        print(allele_used)
        print(allele_id)
        print(mrk.text)
        # finds the Allele Association table and gets the second row of data
        type1_used = self.driver.find_elements(By.CLASS_NAME, 'alleleAssocType')[1].get_property(
            'value')  # value will be 1017 which associates to 'Used-FC'
        allele1_used = self.driver.find_elements(By.CLASS_NAME, "alleleSymbol")[1].get_property('value')
        allele1_id = self.driver.find_elements(By.CLASS_NAME, "alleleAccID")[1].get_property('value')
        mrk1 = self.driver.find_elements(By.CLASS_NAME, 'alleleMarkerSymbol')[1]
        print(type1_used)
        print(allele1_used)
        print(allele1_id)
        print(mrk1.text)
        # assert the row results are correct
        self.assertEqual(type_used, '1017')
        self.assertEqual(allele_used, 'Cdk5rap2<an>')
        self.assertEqual(allele_id, 'MGI:1856646')
        self.assertEqual(mrk.text, 'Cdk5rap2')
        self.assertEqual(type1_used, '1017')
        self.assertEqual(allele1_used, 'Tyrp1<B-lt>')
        self.assertEqual(allele1_id, 'MGI:1855962')
        self.assertEqual(mrk1.text, 'Tyrp1')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiLitTriageDetail))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))