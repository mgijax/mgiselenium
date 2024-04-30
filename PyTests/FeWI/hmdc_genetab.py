"""
Created on Nov 8, 2016
These tests cover the the data and layout of the Genes tab results
updated: July 2017 (jlewis) - updates to make Gene Tab tests more tolerant to changes in annotations.  e.g. removing counts
@author: jeffc
Verify all the table headers on the genes tab are correct and in the correct order
Verify the correct genes are returned for a gene symbol query
Verify the correct genes are returned for this query, in particular genes with special characters in their symbol.
Verify the correct diseases are returned for this query
"""
import os.path
import sys
import tracemalloc
import unittest
import config

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate, wait
from util.table import Table

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../..', )
)

# Tests
tracemalloc.start()


class TestHmdcGeneTab(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)

    def test_genes_tab_headers(self):
        """
        @status this test verifies all the table headers on the genes tab are correct and in the correct order.
        @see HMDC-GQ-1 (single token mouse symbol); HMDC-genetab-1 (column headings)
        """
        print("BEGIN test_genes_tab_headers")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Gata1")  # identifies the input field and enters gata1
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print(gene_tab.text)
        gene_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                               '#geneTable > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2) > nobr:nth-child(1) > a:nth-child(1) > div:nth-child(1)'))):
            print('HMDC disease tab data loaded')
        gene_table_headers = self.driver.find_element(By.ID, "geneTable").find_element(By.CSS_SELECTOR, "tr")
        items = gene_table_headers.find_elements(By.TAG_NAME, "th")
        searchTermItems = iterate.getTextAsList(items)
        self.assertEqual(searchTermItems[0], "Organism")
        self.assertEqual(searchTermItems[1], "Gene Symbol")
        self.assertEqual(searchTermItems[2], "Genetic Location")
        self.assertEqual(searchTermItems[3], "Genome Coordinates")
        self.assertEqual(searchTermItems[4], "Associated Human Diseases (Source)")
        self.assertEqual(searchTermItems[5], "Abnormal Mouse Phenotypes\nReported in these Systems")
        self.assertEqual(searchTermItems[6], "References in MGI")
        self.assertEqual(searchTermItems[7], "Mice With Mutations\nIn this Gene (IMSR)")

    def test_genes_tab_genes(self):
        """
        @status this test verifies the correct genes are returned for a gene symbol query.
        @see HMDC-GQ-1 (single token mouse symbol); HMDC-genetab-2 (return matches by Gene symbol: mouse and human)
        """
        print("BEGIN test_genes_tab_genes")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Gata1")  # identifies the input field and enters gata1
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print(gene_tab.text)
        gene_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                               '#geneTable > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2) > nobr:nth-child(1) > a:nth-child(1) > div:nth-child(1)'))):
            print('HMDC disease tab data loaded')
        gene_table = Table(self.driver.find_element(By.ID, "geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        print(iterate.getTextAsList(cells))
        genesymbolsreturned = iterate.getTextAsList(cells)

        # asserts that the matching mouse and human genes are returned
        self.assertIn('Gata1', genesymbolsreturned)
        self.assertIn('GATA1', genesymbolsreturned)

    def test_uniquegenes_tab_genes(self):
        """
        @status this test verifies the correct genes are returned for this query, in particular genes with special
                characters in their symbol.
        @see HMDC-GQ-2 (symbol w/ special characters)
        """
        print("BEGIN test_uniquegenes_tab_genes")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Tg(IGH@*)SALed")  # identifies the input field and enters gata1
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print(gene_tab.text)
        gene_tab.click()
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a.ng-scope > div:nth-child(1)'))):
            print('HMDC disease tab data loaded')
        gene_table = Table(self.driver.find_element(By.ID, "geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        print(iterate.getTextAsList(cells))
        # displays each row of gene data
        gene1 = cells[1]
        # asserts that the correct genes in the correct order are returned
        self.assertEqual(gene1.text, 'Tg(IGH@*)SALed')

    def test_genes_tab_diseases(self):
        """
        @status this test verifies the correct diseases are returned for this query.
        @see: HMDC-genetab-15, 16 (Associated Human Diseases column)
        @bug: this test is failing but why I do not understand!
        """
        print("BEGIN test_genes_tab_diseases")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Gata1")  # identifies the input field and enters gata1
        # wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print(gene_tab.text)
        gene_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                               '#geneTable > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2) > nobr:nth-child(1) > a:nth-child(1) > div:nth-child(1)'))):
            print('HMDC disease tab data loaded')
        gene_table = Table(self.driver.find_element(By.ID, "geneTable"))
        cells = gene_table.get_column_cells("Associated Human Diseases (Source)")
        assochumandiseases = iterate.getTextAsList(cells)
        print(assochumandiseases)
        # asserts that the expected diseases are returned for these genes
        self.assertIn(
            'beta thalassemia\ncolon adenocarcinoma\ndepressive disorder\nDown syndrome\nmyeloid leukemia associated with Down Syndrome\nthrombocytopenia\ntransient myeloproliferative syndrome\nX-linked dyserythropoietic anemia\nX-linked thrombocytopenia with beta-thalassemia',
            assochumandiseases)  # diseases associated to Gata1
        self.assertIn('myelodysplastic syndrome\nmyelofibrosis', assochumandiseases)  # diseases associated to GATA1

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHmdcGeneTab))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
