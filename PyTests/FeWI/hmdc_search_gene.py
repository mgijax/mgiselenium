'''
Created on Jan 6, 2017
Updated: July 2017 (jlewis).  Updates to be more tolerant of data changes.  Cross-reference requirements with test cases. 
Remove assertions in tests that are outside scope of requirement being tested.

This file contains the tests for Gene nomenclature searches (mouse and human) that are entered via the Gene Symbol(s)/ID(s)
query field and/or the Gene Name query fields. 
Tests are organized in this order in the file:  Negative tests; gene symbol tests, gene name tests, and multiple field tests

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
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table



# Tests

class TestGenesSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)
        
        
    def test_gene_symbol_name_not_found(self):
        '''
        @status these tests verify that no results are returned when searching by a bogus gene symbol or gene name
        @see: HMDC-GQ-1 (negative test: search by gene symbol); HMDC-GQ-44 (negative test: search by gene name)
        '''
        print ("BEGIN test_gene_symbol_not_found")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("football")#identifies the input field and a bogus symbol
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print grid_tab.text
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (0 x 0)", "Grid tab is not visible!")
        grid_tab.click()
        
        self.assertIn('No data available for your query.', self.driver.page_source)
        
        #Open up the query form again (click on "Click to modify search" button)
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Try this search using the Gene Name query field -- no results should be returned as it does not accept a list
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene name option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
      
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys('football game') #multi token query string that should return nothing
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        gene_tab.click()
        
        #Check for no results message
        self.assertIn('No Matching Genes', self.driver.page_source)
        
    def test_no_wildcards(self):
        '''
        @status this test verifies that wildcards are not valid for the Gene Symbol query field.
        @see: HMDC-GQ-13 (Gene Symbol query field: wildcards not supported)
        '''
        print ("BEGIN test_no_wildcards")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Pax6*")#identifies the input field and a symbol with an appended asterisk
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        gene_tab.click()
        
        #Check for no results message - returns nothing because the asterisk is NOT a wildcard in the HMDC
        self.assertIn('No Matching Genes', self.driver.page_source)
        
        
       
    def test_multi_gene_homology_class(self):
        '''
        @status This test verifies that multiple human genes for a homology class are returned correctly.  This test also verifies 
        that genoclusters that DO NOT roll up are not returned for this test.  The first search uses text that matches either the mouse or 
        human symbol.  The second search matches only one of the human symbols.
        
        as-of July 2017 -- 2nd part of this test fails: this test hi-lites a known bug that returns 2 genes due to genoclusters that don't pass the roll up rules (low priority fix).  
        This includes genes (Smg6 & Grm7) that are being returned by genoclusters that do not pass the roll-up rules.
        
        @see: HMDC-grid-3 (multiple human genes); HMDC-grid-11 (don't return markers for a query that don't have genoclusters that pass roll-up)
        '''
        print ("BEGIN test_multi_gene_homology_class")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Smn1")#identifies the input field and enters a gene symbol
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
       
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #Get human genes returned to grid
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        searchTermItems = iterate.getTextAsList(hgenes)
     
        #Verify multiple human genes displayed for a row
        self.assertIn("SMN1, SMN2", searchTermItems)

        #Get mouse genes returned to grid
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        searchTermItems = iterate.getTextAsList(mgenes)
        
        #Verify gene not returned due to complex genocluster
        self.assertNotIn("Grm7", searchTermItems, "Grm7 is part of a complex genotype and should not be returned - this is an error")
        
        #Do this again using the Human Symbol -- same results expected
        
        #Open up the query form again (click on "Click to modify search" button)
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Try this search using the Gene Name query field -- no results should be returned as it does not accept a list
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
      
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys('SMN2') #human symbol for a homology class with multiple human symbols
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
     
        #identify the Genes tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
       
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #Get human genes returned to grid
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        searchTermItems = iterate.getTextAsList(hgenes)
     
        #Verify multiple human genes displayed for a row
        self.assertIn("SMN1, SMN2", searchTermItems)

        #Get mouse genes returned to grid
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        searchTermItems = iterate.getTextAsList(mgenes)
        
        #Verify gene not returned due to complex genocluster
        self.assertNotIn("Grm7", searchTermItems, "Grm7 is part of a complex genotype and should not be returned - this is an error")
                
    def test_gene_symbol_nodiseases(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. The results will have phenotypes but no diseases
        @see: HMDC-GQ-1 (query by gene symbol); HMDC-disease-9 (don't return diseases if none are associated to the Gene queried)
        '''
        print ("BEGIN test_gene_symbol_nodiseases")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Bbx")#identifies the input field and a gene symbol
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        
        grid_tab.click()
        
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
         
        self.assertEqual(hgenes.text, 'BBX')
        mgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.last")
        
        self.assertEqual(mgenes.text, "Bbx")#cells = mgenes.get_all()
        
        #Click on the Disease Tab and verify the no data message displayed.
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        time.sleep(2)
        print disease_tab.text
        
        disease_tab.click()
        
        self.assertIn('No Matching Diseases', self.driver.page_source)
       
        

    def test_gene_homology_union(self):
        '''
        @status This test verifies the correct genes are returned when a "homology union" case applies.  This happens when HomoloGene and HGNC have conflicting
        sets of genes associated to a mouse gene.  The HMDC search returns the union of both sets to the user.  To verify this test we are using the Genes Tab. 
        Both Selenbp2 and Selenbp1 are associated with the human gene SELENBP1.  All 3 of these genes are returned in the Genes Tab.  Selenbp1/SELENBP1 is 
        the selected homology set using the Homology Hybrid rules and is therefore displayed as 1 row in the grid. "If" Selenbp2 had annotations it would be
        on a separate row in the grid.
        @see: HMDC-grid-26 (display the Homology Hybrid on the Grid);  HMDC-genetab-20 (return the union of a set of conflicting homology sets)
        '''
        print ("BEGIN test_gene_homology_union")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("selenbp2")#enter a symbol that is in 2 different homology classes
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        
        gene_tab.click()
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        
        cells = gene_table.get_column_cells("Gene Symbol")
        
        geneList = iterate.getTextAsList(cells)
    
        #asserts that the genes from 2 different homology classes are returned (the "homology union")
        self.assertIn('Selenbp1', geneList)
        self.assertIn('SELENBP1', geneList)
        self.assertIn('Selenbp2', geneList)
        

    def test_gene_name(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. The results will have phenotypes and diseases
        This test is a standard gene name search result.
        @see: HMDC-GQ-44 (multiple token, exact match); HMDC-GQ-45 (multiple token, partial match); HMDC-GQ-47 (multiple token human Gene Name - exact match)
              HMDC-grid-29 (return Transgenes per Expressed Component nomenclature)
        '''
        print ("BEGIN test_gene_name")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene name option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("transformation related protein 53") #mouse gene name for Trp53
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #verify TP53 returned on Grid
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        humanGridGenes = iterate.getTextAsList(hgenes)
        self.assertIn('TP53', humanGridGenes)
        
        #verify Trp53 returned on Grid
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGridGenes = iterate.getTextAsList(mgenes)
        self.assertIn('Trp53', mouseGridGenes)
        
        #verify Transgene with Trp53 expressed component returned on Grid
        self.assertIn('Tg(Trp53)1Srn', mouseGridGenes) 
        
        #verify gene returned by a partial gene name
        self.assertIn('Trp53bp1', mouseGridGenes)
        
        #Do another search -- this time by the Human gene name for TP53.
        #Open up the query form again (click on "Click to modify search" button)
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene name option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("tumor protein p53") #mouse gene name for Trp53
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #verify TP53 returned on Grid
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        humanGridGenes = iterate.getTextAsList(hgenes)
        self.assertIn('TP53', humanGridGenes)
        
        #verify Trp53 returned on Grid
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGridGenes = iterate.getTextAsList(mgenes)
        self.assertIn('Trp53', mouseGridGenes)
        
        #verify gene returned by a partial gene name
        self.assertIn('Trp53cor1', mouseGridGenes)
        
        
    def test_gene_name_symbol(self):
        '''
        @status This test verifies that a gene symbol may be entered into the Gene Name search field and get correct results.  Also returns a gene via a
                partial match to a zebrafish gene name.
        @see: HMDC-GQ-42 (Query by Gene Name field and enter a gene symbol); HMDC-GQ-53 (query by Gene Name field for Ortholog gene names); 
              HMDC-grid-5 (row with multiple human and mouse genes); 
        '''
        print ("BEGIN test_gene_name_symbol")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene name option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("C4a")#identifies the input field and enters a gene symbol
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #Grab the human and mouse genes displayed on the grid
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        
        humanGridGenes = iterate.getTextAsList(hgenes)
        mouseGridGenes = iterate.getTextAsList(mgenes)
        
        #Verify homology class with multiple human and mouse genes are returned
        self.assertIn("C4A, C4B", humanGridGenes)
        self.assertIn("C4a, C4b", mouseGridGenes)
        
        #Verify genes matched via zebrafish name (ortholog match) is returned
        self.assertIn("HOXC4", humanGridGenes)
        self.assertIn("Hoxc4", mouseGridGenes)
        
        

    def test_gene_name_leptin(self):
        '''
        @status Tests the Gene Name field using a single token gene name and verifies return.  Also verifies that the same value 
                entered in the Gene Symbol/ID field returns no results.
        @see: HMDC-GQ-43 (single token Gene Name); HMDC-GQ-12 (gene names not matched for query by ID/symbol)
        '''
        print ("BEGIN test_gene_name_leptin")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene name option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("leptin") #enter a single token gene name
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #Grab mouse and human genes returned to the Grid
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        
        humanGridGenes = iterate.getTextAsList(hgenes)
        mouseGridGenes = iterate.getTextAsList(mgenes)
        
        #Verify homology class with multiple human and mouse genes are returned
        self.assertIn("LEP", humanGridGenes)
        self.assertIn("Lep", mouseGridGenes)
        
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Repeat query using the Gene ID/Symbol field
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("leptin") #enter a single token gene name
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #Look for no results message - entering a gene name in the Gene Symbol/ID field returns no results
        self.assertIn('No data available for your query', self.driver.page_source)
       
        
    def test_gene_symbol_only_genes(self):
        '''
        @status this test verifies the correct genes are returned for this query, The symbol is unique because it has no grid or diseases, only genes.
        @see: HMDC-genetab-2 (search returns rows on Gene tab); HMDC-grid-30 (display a 'no data' message when no rows are returned on Grid)
        '''
        print ("BEGIN test_gene_symbol_only_genes")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("paupar")#identifies the input field and enters a gene symbol
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (0 x 0)", "Grid tab is not visible!")
        grid_tab.click()
        self.assertIn('No data available for your query', self.driver.page_source)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        
        gene_tab.click()
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        #asserts that the correct genes are returned
        self.assertIn('Paupar', geneList)
        self.assertIn('PAUPAR', geneList)
        
    def test_gene_name_no_disease(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. The results will have phenotypes and genes, no diseases!
        @see: HMDC-GQ-43 (single token gene name search); HMDC-disease-18 (no diseases returned)
        '''
        print ("BEGIN test_gene_name_no_disease")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene name option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("paxillin")#identifies the input field and enters a gene name
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #verify expected human and mouse gene returned
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        humanGeneList = iterate.getTextAsList(hgenes)
        self.assertIn('PXN', humanGeneList)
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGeneList = iterate.getTextAsList(mgenes)
        self.assertIn("Pxn", mouseGeneList)
        
        #identify the Disease tab and click on it
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        
        disease_tab.click()
        
        #Look for no results message
        self.assertIn('No Matching Diseases', self.driver.page_source)
        
        
        
    def test_gene_mult_token_syn(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. 
        This test is a multi token synonym search, matches by gene name, but not by gene symbol.
        @see: HMDC-GQ-14 (multiple token synonyms not matched via Symbol/ID search); 
              HMDC-GQ-48 (multiple token synonyms matched via Gene Name search)
        '''
        print ("BEGIN test_gene_mult_token_syn")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the Gene Name option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("dickie's small eye")#identifies the input field and enters multiple token synonym
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #get the mouse and human genes returned and verify PAX6 and Pax6 are included
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        humanGeneList = iterate.getTextAsList(hgenes)
        self.assertIn('PAX6', humanGeneList)
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGeneList = iterate.getTextAsList(mgenes)
        self.assertIn('Pax6', mouseGeneList)
        
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Repeat query using the Gene ID/Symbol field -- expecting Pax6/PAX6 not to be returned
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("dickie's small eye")
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid Tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #get the mouse and human genes returned and verify PAX6 and Pax6 are NOT included
        #FYI - there are 2 genes returned for this query.  The text entered is being
        #interpreted as a list of symbols--a valid option for the Gene Symbol/ID field.  
        #The "S" is considered one of the tokens in the list and is returning 2 genes 
        #due to nomenclature matches.  A query by just "S" returns the same 2 genes.
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        humanGeneList = iterate.getTextAsList(hgenes)
        self.assertNotIn('PAX6', humanGeneList)
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGeneList = iterate.getTextAsList(mgenes)
        self.assertNotIn('Pax6', mouseGeneList)
        

    def test_gene_mouse_synonym(self):
        '''
        @status this test verifies the correct genes are returned for a query by a mouse synonym.  It has no 
                grid or diseases, only genes.
        @see: HMDC-GQ-4 (query by mouse synonym); HMDC-genetab-2 (return matched genes to gene tab plus their ortholog)
        '''
        print ("BEGIN test_gene_mouse_synonym")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Solt")#identifies the input field and enters a mouse synonym
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        gene_tab.click()
        
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        #Verify expected genes are returned
        self.assertIn('Cenpk', geneList)
        self.assertIn('CENPK', geneList)

    def test_gene_human_synonym(self):
        '''
        @status this test verifies the correct genes are returned for this query by human synonym.  It has a grid and genes, no diseases.
        @see: HMDC-GQ-5 (query by human synonym); HMDC-genetab-2 (return matched genes to gene tab plus their ortholog)
        '''
        print ("BEGIN test_gene_human_synonym")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("HMPH")#identifies the input field and enters a human synonym
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid Tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        gene_tab.click()
        
        #get the list of genes
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        #asserts that the correct genes are part of the returned data
        self.assertIn('Hhex', geneList)
        self.assertIn('HHEX', geneList)
       
    def test_gene_search_superscript(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for 
                searching by Gene Name and Gene Symbol/ID when the query text contains superscript.  The match is to a mouse synonym (Cdkn2a)
        @see: HMDC-GQ-49 (gene name search with superscript); HMDC-GQ-15 (gene symbol search with superscript: matching a gene synonym)
        '''
        print ("BEGIN test_gene_search_superscript")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene name option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("p19<ARF>")#identifies the input field and enter the synonym with a superscript
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #Grab the human genes returned on the Grid Tab and verify associated human gene is returned
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        humanGeneList = iterate.getTextAsList(hgenes)
        self.assertIn("CDKN2A", humanGeneList)        
        
        #Grab the mouse genes returned on the Grid Tab and verify associate mouse gene is returned
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGeneList = iterate.getTextAsList(mgenes)
        self.assertIn("Cdkn2a", mouseGeneList)
        
        #Do this search again using the Gene Symbol/ID query field
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Repeat query using the Gene ID/Symbol field
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("p19<ARF>")#identifies the input field and enter the synonym with a superscript
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #Grab the human genes returned on the Grid Tab and verify associated human gene is returned
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        humanGeneList = iterate.getTextAsList(hgenes)
        self.assertIn("CDKN2A", humanGeneList)        
        
        #Grab the mouse genes returned on the Grid Tab and verify associate mouse gene is returned
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGeneList = iterate.getTextAsList(mgenes)
        self.assertIn("Cdkn2a", mouseGeneList)
        

    def test_gene_NOT_disease(self):
        '''
        @status This test verifies that a NOT disease annotation is not included in the results for a query by the Gene Symbol
                with that annotation.  In this case the NOT annotation is to DOID:2841 (asthma) for gene Adam33.  This test checks the 
                Grid and Disease tabs.
        @see: HMDC-grid-12 (NOT disease annotations not displayed on Grid); HMDC-disease-19 (NOT disease annotations not 
              displayed on Disease Tab); HMDC-genetab-19 (NOT references included in Disease relevant reference count/link)
        '''
        print ("BEGIN test_gene_NOT_disease")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Adam33")#identifies the input field and enters the symbol
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab, print the text, and click on the Tab
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #cells captures every field from Human Gene heading to the last phenotype/disease name displayed (the angled text)
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        #Verify that the parent term for "Asthma" is not present on the grid
        phenoDiseaseList = iterate.getTextAsList(cells)
        self.assertNotIn('respiratory system disease', phenoDiseaseList )
        
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        gene_tab.click()
        
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        
        #save each row of gene data and verify the expected genes are returned
        gene1 = cells[1]
        gene2 = cells[2]
        self.assertEqual(gene1.text, 'Adam33')
        self.assertEqual(gene2.text, 'ADAM33')
        
        cells2 = gene_table.get_column_cells("References in MGI")
       
        #save each row of References in MGI data and verify the disease relevant reference is found.  This is the reference for the
        #NOT annotation.  NOT model references are recognized here.
        ref1 = cells2[1]
        ref2 = cells2[2]
        #asserts that the References in MGI column displays a Disease Relevant link since the is a NOT disease
        self.assertEqual(ref1.text, 'All Mouse: 39\nDisease Relevant: 1')
        self.assertEqual(ref2.text, '')
        
        #identify the Disease tab and verify the tab's text
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        
        disease_tab.click()
        
        #Look for no results message
        self.assertIn('No Matching Diseases', self.driver.page_source)

    def test_gene_gtrosa(self):
        '''
        @status This test verifies the requirement that a match to the Gene Symbol Gt(ROSA)26Sor will not return a row on the Grid for 
                this gene.  It is okay to return this gene on the Genes Tab.  Transgenes that have this text as part of their marker 
                nomenclature are okay to be displayed on the Grid.  Verify using query by Gene Symbol and also by Gene Name.  Special 
                logic throughout the HMDC to exclude this gene from various results.
        @see: HMDC-grid-1
        '''
        print ("BEGIN test_gene_gtrosa")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Gt(ROSA)26Sor")#identifies the input field and enters symbol of Gt(ROSA)26Sor
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid Tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #No rows should be displayed on the Grid -- look for no results message
        self.assertIn('No data available for your query', self.driver.page_source)
        
        #Go to the Genes Tab and verify it is returned there as expected
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        gene_tab.click()
        
        #Get list of genes and verify Gt(ROSA)26Sor is displayed on the Genes Tab
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Gt(ROSA)26Sor', geneList)
        
        #Do this check again -- this time using the Gene Name query option.
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Repeat query using the Gene Name field
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene name option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Gt(ROSA)26Sor")
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGeneList = iterate.getTextAsList(mgenes)
        self.assertNotIn("Gt(ROSA)26Sor", mouseGeneList)
        
        #Go to the Genes Tab and verify it is returned there as expected
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        gene_tab.click()
        
        #Get list of genes and verify Gt(ROSA)26Sor is displayed on the Genes Tab
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Gt(ROSA)26Sor', geneList)

    def test_gene_mltgene_homology(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. 
        This test is for searching by gene name when grid returns synonym to a mouse in a multi-gene 
        homology class(C4A, C4B)
        @see: HMDC-GQ-4 (mouse synonym); HMDC-grid-3,4 (row w/ multiple mouse/human genes);
              HMDC-genetab-2 (orthologs and homologs returned)
        '''
        print ("BEGIN test_gene_mltgene_homology")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Slp")#identifies the input field and enters mouse synonym for C4a
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #get human and mouse genes on the grid and verify C4a/C4b/C4A/C4B homology class
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        humanGeneList = iterate.getTextAsList(hgenes)
        self.assertIn("C4A, C4B", humanGeneList)
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGeneList = iterate.getTextAsList(mgenes)
        self.assertIn("C4a, C4b", mouseGeneList)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        gene_tab.click()
        
        #get the list of genes and verify the multiple gene homology class
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
    
        self.assertIn('C4A', geneList)
        self.assertIn('C4a', geneList)
        self.assertIn('C4B', geneList)
        self.assertIn('C4b', geneList)

    def test_genotype_popup(self):
        '''
        @status this test verifies the correct genotypes are returned when clicking on a particular phenotype cell.
                Checks for a normal MP annotation; 1-marker genocluster (OMG); Conditional genocluster that passes roll-up
        @see: HMDC-GQ-1 (mouse symbol)
              HMDC-grid-7, 8, 9 (Return row with Normal MP annotations; Return row with one marker genoclusters;
                 Return row with conditional genocluster that pass roll-up rules)
              HMDC-popup-11 (1 row per genocluster); HMDC-popup-13 (Normal annotation)
        '''
        print ("BEGIN test_genotype_popup")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Foxm1")#identifies the input field and enters a mouse symbol
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #firstcell captures all the table data blocks of phenotypes on the first row of data
        phenocells = self.driver.find_elements_by_css_selector("td.ngc.center.cell.middle")
         
        phenocells[0].click()#clicks the second phenotype data cell to open up the genotype popup page
        self.driver.switch_to_window(self.driver.window_handles[1])#switches focus to the genotype popup page
        
        #asserts the heading text is correct in page title
        self.assertEqual("Mouse cardiovascular system abnormalities for FOXM1/Foxm1", self.driver.title)
        
        #asserts the special "normal" text is in the legend
        self.assertIn("Aspects of the system are reported to show a normal phenotype", self.driver.page_source)
        
        #Identify the table
        mouse_geno_table = self.driver.find_element_by_css_selector("p > table.popupTable ")
        data = mouse_geno_table.find_element_by_tag_name("td")
        print data.text
        #find all the TR tags in the table and iterate through them
        cells = mouse_geno_table.find_elements_by_tag_name("tr")
        genoClusterList = iterate.getTextAsList(cells)
        
        #asserts that the correct genotypes in the correct order are returned
        self.assertIn('Foxm1tm1.1Rhc/Foxm1tm1.1Rhc', genoClusterList) #test case for 1-marker genoclusters - this one has multiple genotypes
        self.assertIn('Foxm1tm1Rhc/Foxm1tm1Rhc\nTg(Tek-cre)1Ywa/0  (conditional) *', genoClusterList) #test case for conditional genotype and normal annotation
        
    def test_gene_name_spec_char(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene Name with a name that includes special characters
        @see: HMDC-GQ-46 (Gene Name with special characters)
        '''
        print ("BEGIN test_gene_name_spec_char")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene name option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("phenylalkylamine Ca2+ antagonist (emopamil) binding protein")#enter a gene name
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        gene_tab.click()
        
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        #asserts that the correct genes in the correct order are returned
        self.assertIn('Ebp', geneList)
        self.assertIn('EBP', geneList)
        
        #Do another search for a gene name with other special characters
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene name option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("RTF1, Paf1/RNA polymerase II complex component")#enter a gene name
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        gene_tab.click()
        
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        #asserts that the correct genes are returned
        self.assertIn('Rtf1', geneList)
        self.assertIn('RTF1', geneList)
        
    def test_gene_synonym_special_char(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene symbol using a human synonym that has a special character in it.(ie. -)
        @see: HMDC-GQ-6
        '''
        print ("BEGIN test_gene_synonym_special_char")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("ET-BR")#identifies the input field and enters a synonym
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        gene_tab.click()
        
        #Grab the list of genes and verify expected genes are in the list
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        self.assertIn("Ednrb", geneList)
        self.assertIn("EDNRB", geneList)
    
        
        
    def test_gene_human_no_homology(self):
        '''
        @status This test searches for a human gene that is not in a homology class (not linked) and only appears on the Genes Tab.  This category of
                human genes is easy to spot as they are not linked.
        @see: HMDC-grid-31 (return row with no mouse gene)
        '''
        print ("BEGIN test_gene_symbol_non_mousegenetab")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("AA06")#identifies the input field and enters a human symbol
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        gene_tab.click()
        
        #get the list of genes and verify the one we searched for is there
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        self.assertIn('AA06', geneList)
        
    def test_gene_ortholog_symbol(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by a gene symbol of a species other than mouse or human.  The mouse and human genes in the same homology class are returned in the HMDC.
        @see: HMDC-GQ-52 (query by rat symbol - return mouse and human genes in the same homology class)
        '''
        print ("BEGIN test_gene_symbol_non_mousegridgene")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("RGD1560248") #enter a rat symbol
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        gene_tab.click()
        
        #get the list of genes and verify the one we searched for is there
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        self.assertIn('Fmnl2', geneList)
        self.assertIn('FMNL2', geneList)
        
    
    def test_gene_human_symbol(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene symbol using a symbol that has a human symbol match and a human synonym match (Trp53, Trp53bp1)
        @see: HMDC-GQ-3
        '''
        print ("BEGIN test_gene_symbol_dual_match")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("TP53")#enter a human symbol
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        gene_tab.click()
        
        #get the list of genes and verify the one we searched for is there
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        self.assertIn('Trp53', geneList)
        self.assertIn('TP53', geneList)
        
        
    
        
        
    def test_gene_symbol_multiples(self):
        '''
        @status Test that a list of symbols may be entered with comma or space delimiters.  Verify the correct genes are returned on the Genes Tab.
                Return the matching symbol and its human/mouse ortholog
        @see HMDC-GQ-7 (list of comma or space delimited symbols)
             HMDC-GQ-51 (don't accept a list of symbols for the Gene Name query)
        '''
        print ("BEGIN test_gene_symbol_multiples")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
            
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys('KITLG, Foxm1, Lepr') #Enter a mix of mouse and human symbols
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        gene_tab.click()
        
        #Grab the list of genes and verify that expected ones are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        self.assertIn('Foxm1', geneList)
        self.assertIn('FOXM1', geneList)
        self.assertIn('KITLG', geneList)
        self.assertIn('Kitl', geneList)
        self.assertIn('LEPR', geneList)
        self.assertIn('Lepr', geneList)
        
        
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Do this search again -- this time space delimit the IDs
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
      
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys('KITLG Foxm1 Lepr') #IDs for Foxm1, LEP, Ins2
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        gene_tab.click()
        
        #Grab the list of genes and verify that expected ones are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        self.assertIn('Foxm1', geneList)
        self.assertIn('FOXM1', geneList)
        self.assertIn('KITLG', geneList)
        self.assertIn('Kitl', geneList)
        self.assertIn('LEPR', geneList)
        self.assertIn('Lepr', geneList)
        
        #Open up the query form again (click on "Click to modify search" button)
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Try this search using the Gene Name query field -- no results should be returned as it does not accept a list
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene name option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
      
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys('KITLG, Foxm1, Lepr') #comma delimited list of symbols
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        gene_tab.click()
        
        #Check for no results message - list of symbols not valid for Gene Name search
        self.assertIn('No Matching Genes', self.driver.page_source)
    
    def tearDown(self):
        self.driver.close()
       
       
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main() 