'''
Created on Nov 8, 2016
These tests cover the the data and layout of the Genes tab results
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import HTMLTestRunner
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table



# Tests

class TestGeneTab(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)
        
    def test_genes_tab_headers(self):
        '''
        @status this test verifies all the table headers on the genes tab are correct and in the correct order.
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Gata1")#indentifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (6)", "Genes tab is not visible!")
        gene_tab.click()
        gene_table_headers = self.driver.find_element_by_id("geneTable").find_element_by_css_selector("tr")
        items = gene_table_headers.find_elements_by_tag_name("th")
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
        '''
        @status this test verifies the correct genes are returned for this query.
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Gata1")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (6)", "Genes tab is not visible!")
        gene_tab.click()
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        gene1 = cells[1]
        gene2 = cells[2]
        gene3 = cells[3]
        gene4 = cells[4]
        gene5 = cells[5]
        gene6 = cells[6]
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(gene1.text, 'Gata1')
        self.assertEqual(gene2.text, 'GATA1')
        self.assertEqual(gene3.text, 'Tg(Gata1)#Mym')
        self.assertEqual(gene4.text, 'Tg(Gata1*)#Mym')
        self.assertEqual(gene5.text, 'Tg(Gata1*V205G)1Mym')
        self.assertEqual(gene6.text, 'Tg(HBB-Gata1)G4Phi')
        
    def test_uniquegenes_tab_genes(self):
        '''
        @status this test verifies the correct genes are returned for this query, in particular genes with special characters in their symbol.
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Tg(IGH@*)SALed")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (1)", "Genes tab is not visible!")
        gene_tab.click()
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        gene1 = cells[1]
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(gene1.text, 'Tg(IGH@*)SALed')
        
    def test_genes_tab_diseases(self):
        '''
        @status this test verifies the correct diseases are returned for this query.
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Gata1")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        self.assertEqual(gene_tab.text, "Genes (6)", "Genes tab is not visible!")
        gene_tab.click()
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Associated Human Diseases (Source)")
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        disease1 = cells[1]
        disease2 = cells[2]
        disease3 = cells[3]
        disease4 = cells[4]
        disease5 = cells[5]
        disease6 = cells[6]
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(disease1.text, 'myelofibrosis\nthrombocytopenia')
        self.assertEqual(disease2.text, 'Down syndrome\nthrombocytopenia')
        self.assertEqual(disease3.text, '')
        self.assertEqual(disease4.text, '')
        self.assertEqual(disease5.text, 'thrombocytopenia')
        self.assertEqual(disease6.text, '')        
        
    
    def tearDown(self):
        self.driver.close()
       
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main() 
