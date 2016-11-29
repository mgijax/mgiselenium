'''
Created on Nov 15, 2016
This test should check the column headers for correct display and order. It currently verifies the returned diseases and their order and the DO IDs in correct order, 
tests for the other columns need to be added later.
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

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

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.FEWI_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)
        
    def test_diseases_tab_headers(self):
        '''
        @status this test verifies the headings on the disease tab are correct and in the correct order.
        @bug: under construction
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
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        self.assertEqual(disease_tab.text, "Diseases (3)", "Diseases tab is not visible!")
        disease_tab.click()
        disease_table_headers = self.driver.find_element_by_id("diseaseTable").find_element_by_css_selector("tr")
        items = disease_table_headers.find_elements_by_tag_name("th")
        searchTermItems = iterate.getTextAsList(items)
        self.assertEqual(searchTermItems[0], "Disease")
        self.assertEqual(searchTermItems[1], "DO ID")
        self.assertEqual(searchTermItems[2], "OMIM ID(s)")
        self.assertEqual(searchTermItems[3], "Mouse Models")
        self.assertEqual(searchTermItems[4], "Associated Genes from Mouse Models")
        self.assertEqual(searchTermItems[5], "Associated Human Genes (Source)")
        self.assertEqual(searchTermItems[6], "References using\nMouse Models")
        
    def test_diseases_tab_diseases(self):
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
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Diseases (3)", "Diseases tab is not visible!")
        gene_tab.click()
        
        gene_table = Table(self.driver.find_element_by_id("diseaseTable"))
        
        cells = gene_table.get_column_cells("Disease")
        
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        disease1 = cells[1]
        disease2 = cells[2]
        disease3 = cells[3]
        
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(disease1.text, 'Down syndrome')
        self.assertEqual(disease2.text, 'myelofibrosis')
        self.assertEqual(disease3.text, 'thrombocytopenia')
        
    def test_genes_tab_doids(self):
        '''
        @status this test verifies the correct DO IDs are returned for this query.
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
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        
        self.assertEqual(gene_tab.text, "Diseases (3)", "Diseases tab is not visible!")
        gene_tab.click()
        
        gene_table = Table(self.driver.find_element_by_id("diseaseTable"))
        
        cells = gene_table.get_column_cells("DO ID")
        
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        doid1 = cells[1]
        doid2 = cells[2]
        doid3 = cells[3]
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(doid1.text, 'DOID:14250')
        self.assertEqual(doid2.text, 'DOID:4971')
        self.assertEqual(doid3.text, 'DOID:1588')
        
    
    def tearDown(self):
        self.driver.close()
       
        '''
        These tests should NEVER!!!! be run against a production system!!
        def suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(TestAdd))
        return suite
        '''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main() 