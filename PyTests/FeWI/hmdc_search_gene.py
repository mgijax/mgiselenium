'''
Created on Jan 6, 2017

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
        
        
    def test_gene_symbol_not_found(self):
        '''
        @status this test verifies that no results are returned when searching by a bogus gene symbol 
        @see: HMDC-GQ-1 (negative test of search by gene symbol)
        '''
        print ("BEGIN test_gene_symbol_not_found")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("football")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print grid_tab.text
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (0 x 0)", "Grid tab is not visible!")
        grid_tab.click()
        
        self.assertIn('No data available for your query.', self.driver.page_source)
       
    def test_multi_human_genes(self):
        '''
        @status This test verifies that multiple human genes for a homology class are returned correctly.  This test also verifies that genoclusters that DO NOT 
        roll up are not returned for this test.
        
        as-of July 2017 -- 2nd part of this test fails: this test hi-lites a known bug that returns 2 genes due to genoclusters that don't pass the roll up rules (low priority fix).  
        This includes genes (Smg6 & Grm7) that are being returned by genoclusters that do not pass the roll-up rules.
        
        @see: HMDC-grid-3 (multiple human genes); HMDC-grid-11 (don't return markers for a query that don't have genoclusters that pass roll-up)
        '''
        print ("BEGIN test_multi_human_genes")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Smn1")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
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
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Bbx")#identifies the input field and enters gata1
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
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("selenbp2")#identifies the input field and enters gata1
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
    
        #asserts that the correct genes in the correct order are returned
        self.assertIn('Selenbp1', geneList)
        self.assertIn('SELENBP1', geneList)
        self.assertIn('Selenbp2', geneList)
        

    def test_gene_name(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. The results will have phenotypes and diseases
        This test is a standard gene name search result.
        @see: HMDC-GQ-44 (multiple token, exact match); HMDC-GQ-45 (multiple token, partial match); HMDC-grid-29 (return Transgenes per Expressed Component nomenclature)
        '''
        print ("BEGIN test_gene_name")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("paired box 6")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #verify PAX6 returned on Grid
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        humanGridGenes = iterate.getTextAsList(hgenes)
        self.assertIn('PAX6', humanGridGenes)
        
        #verify Pax6 returned on Grid
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGridGenes = iterate.getTextAsList(mgenes)
        self.assertIn('Pax6', mouseGridGenes)
        
        #verify Transgene with Pax6 expressed component returned on Grid
        self.assertIn('Tg(PAX6)77Ndha', mouseGridGenes) 
        
        #go to Genes Tab and confirm a return by a partial gene name
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        gene_tab.click()
        
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneTabGeneList = iterate.getTextAsList(cells)
        self.assertIn('Pax6os1', geneTabGeneList)
        
        
    def test_gene_name_symbol(self):
        '''
        @status This test verifies that a gene symbol may be entered into the Gene Name search field and get correct results.  Also returns a gene via a
                partial match to a zebrafish gene name.
        @see: HMDC-GQ-42 (Query by Gene Name field and enter a gene symbol); HMDC-GQ-53 (query by Gene Name field for Ortholog gene names); 
              HMDC-grid-5 (row with multiple human and mouse genes); 
        '''
        print ("BEGIN test_gene_name_symbol")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("C4a")#identifies the input field and enters gata1
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
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("leptin")
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
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
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("leptin")
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #Look for no results message
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
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("paupar")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (0 x 0)", "Grid tab is not visible!")
        grid_tab.click()
        self.assertIn('No data available for your query', self.driver.page_source)
        
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        
        gene_tab.click()
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        #asserts that the correct genes in the correct order are returned
        self.assertIn('Paupar', geneList)
        self.assertIn('PAUPAR', geneList)
        
    def test_gene_name_no_disease(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. The results will have phenotypes and genes, no diseases!
        @see: HMDC-GQ-43 (single token gene name search); HMDC-disease-18 (no diseases returned)
        '''
        print ("BEGIN test_gene_name_no_disease")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("paxillin")#identifies the input field and enters a gene name
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and verify the tab's text
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
        
        #identify the Disease tab and verify the tab's text
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
        
        #identify the Genes tab and verify the tab's text
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
        
        #identify the Genes tab and verify the tab's text
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
        #identify the Genes tab and verify the tab's text
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
       
    def test_gene_name_superscript(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for 
                searching by gene name when the query text contains superscript.  The match is to a mouse synonym (Cdkn2a)
        @see: HMDC-GQ-49
        '''
        print ("BEGIN test_gene_name_superscript")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
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
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
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
        
    def test_gene_symbol_non_mouseall(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene symbol using a non-mouse marker nomenclature term with results for all 3 tabs
        @see: HMDC-??
        '''
        print ("BEGIN test_gene_symbol_non_mouseall")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("LRTOMT")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 5)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, "LRTOMT")
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Lrrc51, Tomt")
        # self.assertEqual(searchTermItems[1], "Tomt")#cells = mgenes.get_all()
        print searchTermItems
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of phenotype/disease data
        pheno1 = cells[2]
        pheno2 = cells[3]
        pheno3 = cells[4]
        pheno4 = cells[5]
        disease1 = cells[7]
        #asserts that the correct phenotypes/diseases(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'behavior/neurological')
        self.assertEqual(pheno2.text, 'growth/size/body')
        self.assertEqual(pheno3.text, 'hearing/vestibular/ear')
        self.assertEqual(pheno4.text, 'nervous system')
        self.assertEqual(disease1.text, 'nervous system disease')
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (3)", "Genes tab is not visible!")
        gene_tab.click()
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        gene1 = cells[1]
        gene2 = cells[2]
        gene3 = cells[3]
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(gene1.text, 'Lrrc51')
        self.assertEqual(gene2.text, 'LRTOMT')
        self.assertEqual(gene3.text, 'Tomt')
        #identify the Genes tab and verify the tab's text
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        self.assertEqual(disease_tab.text, "Diseases (1)", "Diseases tab is not visible!")
        disease_tab.click()
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        cells = disease_table.get_column_cells("Disease")
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        disease1 = cells[1]
        #asserts that the correct diseases in the correct order are returned
        self.assertEqual(disease1.text, 'autosomal recessive nonsyndromic deafness 63')
        
    def test_gene_symbol_non_mousegenetab(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene symbol using a non-mouse marker nomenclature term with results for just the gene tab
        @see: HMDC-??
        '''
        print ("BEGIN test_gene_symbol_non_mousegenetab")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("BMP2KL")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (0 x 0)", "Grid tab is not visible!")
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
        self.assertEqual(gene1.text, 'BMP2KL')
        
    def test_gene_symbol_non_mousegridgene(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene symbol using a non-mouse marker nomenclature term with results for just the grid and gene tabs
        @see: HMDC-??
        '''
        print ("BEGIN test_gene_symbol_non_mousegridgene")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("ZNF366")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(1)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 12)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, "ZNF366")
        mgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes.text
        self.assertEqual(mgenes.text, "Zfp366")
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of phenotype/disease data
        pheno1 = cells[2]
        pheno2 = cells[3]
        pheno3 = cells[4]
        pheno4 = cells[5]
        pheno5 = cells[6]
        pheno6 = cells[7]
        pheno7 = cells[8]
        pheno8 = cells[9]
        pheno9 = cells[10]
        pheno10 = cells[11]
        #asserts that the correct phenotypes/diseases(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'cardiovascular system')
        self.assertEqual(pheno2.text, 'craniofacial')
        self.assertEqual(pheno3.text, 'endocrine/exocrine glands')
        self.assertEqual(pheno4.text, 'growth/size/body')
        self.assertEqual(pheno5.text, 'hematopoietic system')
        self.assertEqual(pheno6.text, 'immune system')
        self.assertEqual(pheno7.text, 'limbs/digits/tail')
        self.assertEqual(pheno8.text, 'renal/urinary system')
        self.assertEqual(pheno9.text, 'skeleton')
        self.assertEqual(pheno10.text, 'vision/eye')
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (2)", "Genes tab is not visible!")
        gene_tab.click()
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        gene1 = cells[1]
        gene2 = cells[2]
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(gene1.text, 'Zfp366')
        self.assertEqual(gene2.text, 'ZNF366')
        
    def test_gene_symbol_mult_homo_class(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene symbol using a symbol that matches multiple gene homology class (ie. Smn1)
        @see: HMDC-??
        '''
        print ("BEGIN test_gene_symbol_mult_homo_class")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("SMN2")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (8 x 17)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[0], "GRM7")
        self.assertEqual(searchTermItems[1], "SMG6")
        self.assertEqual(searchTermItems[2], "SMN1, SMN2")
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Grm7")
        self.assertEqual(searchTermItems[1], "Smg6")
        self.assertEqual(searchTermItems[2], "Smn1")
        self.assertEqual(searchTermItems[3], "Tg(ACTA1-SMN)63Ahmb")
        self.assertEqual(searchTermItems[4], "Tg(ACTA1-SMN)69Ahmb")
        self.assertEqual(searchTermItems[5], "Tg(Prnp-SMN)92Ahmb")
        self.assertEqual(searchTermItems[6], "Tg(SMN2)11Tro")
        self.assertEqual(searchTermItems[7], "Tg(SMN2)46Tro")#cells = mgenes.get_all()
        print searchTermItems
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of phenotype/disease data
        pheno1 = cells[2]
        pheno2 = cells[3]
        pheno3 = cells[4]
        pheno4 = cells[5]
        pheno5 = cells[6]
        pheno6 = cells[7]
        pheno7 = cells[8]
        pheno8 = cells[9]
        pheno9 = cells[10]
        pheno10 = cells[11]
        pheno11 = cells[12]
        pheno12 = cells[13]
        pheno13 = cells[14]
        pheno14 = cells[15]
        pheno15 = cells[16]
        pheno16 = cells[17]
        disease1 = cells[19]
        #asserts that the correct phenotypes/diseases(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'behavior/neurological')
        self.assertEqual(pheno2.text, 'cardiovascular system')
        self.assertEqual(pheno3.text, 'cellular')
        self.assertEqual(pheno4.text, 'craniofacial')
        self.assertEqual(pheno5.text, 'embryo')
        self.assertEqual(pheno6.text, 'growth/size/body')
        self.assertEqual(pheno7.text, 'homeostasis/metabolism')
        self.assertEqual(pheno8.text, 'immune system')
        self.assertEqual(pheno9.text, 'integument')
        self.assertEqual(pheno10.text, 'limbs/digits/tail')
        self.assertEqual(pheno11.text, 'mortality/aging')
        self.assertEqual(pheno12.text, 'muscle')
        self.assertEqual(pheno13.text, 'nervous system')
        self.assertEqual(pheno14.text, 'respiratory system')
        self.assertEqual(pheno15.text, 'skeleton')
        self.assertEqual(pheno16.text, 'normal phenotype')
        self.assertEqual(disease1.text, 'nervous system disease')
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (23)", "Genes tab is not visible!")
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
        self.assertEqual(gene1.text, 'GRM7')
        self.assertEqual(gene2.text, 'Grm7')
        self.assertEqual(gene3.text, 'Smg6')
        self.assertEqual(gene4.text, 'SMN1')
        self.assertEqual(gene5.text, 'Smn1')
        self.assertEqual(gene6.text, 'SMN2')
        '''plus 17 more genes, all transgenes'''
        #identify the Diseases tab and verify the tab's text
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        self.assertEqual(disease_tab.text, "Diseases (4)", "Diseases tab is not visible!")
        disease_tab.click()
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        cells = disease_table.get_column_cells("Disease")
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        disease1 = cells[1]
        disease2 = cells[2]
        disease3 = cells[3]
        disease4 = cells[4]
        #asserts that the correct diseases in the correct order are returned
        self.assertEqual(disease1.text, 'adult spinal muscular atrophy')
        self.assertEqual(disease2.text, 'intermediate spinal muscular atrophy')
        self.assertEqual(disease3.text, 'juvenile spinal muscular atrophy')
        self.assertEqual(disease4.text, 'Werdnig-Hoffmann disease')

    def test_gene_symbol_with_special_char(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene symbol using a symbol that has a special character in it.(ie. -)
        @see: HMDC-GQ-6
        '''
        print ("BEGIN test_gene_symbol_with_special_char")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("ET-BR")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 24)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, "EDNRB")
        mgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes.text
        self.assertEqual(mgenes.text, "Ednrb")
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of phenotype/disease data
        pheno1 = cells[2]
        pheno2 = cells[3]
        pheno3 = cells[4]
        pheno4 = cells[5]
        pheno5 = cells[6]
        pheno6 = cells[7]
        pheno7 = cells[8]
        pheno8 = cells[9]
        pheno9 = cells[10]
        pheno10 = cells[11]
        pheno11 = cells[12]
        pheno12 = cells[13]
        pheno13 = cells[14]
        pheno14 = cells[15]
        pheno15 = cells[16]
        pheno16 = cells[17]
        pheno17 = cells[18]
        pheno18 = cells[19]
        pheno19 = cells[20]
        pheno20 = cells[21]
        pheno21 = cells[22]
        disease1 = cells[24]
        disease2 = cells[25]
        disease3 = cells[26]
        #asserts that the correct phenotypes/diseases(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'behavior/neurological')
        self.assertEqual(pheno2.text, 'cardiovascular system')
        self.assertEqual(pheno3.text, 'cellular')
        self.assertEqual(pheno4.text, 'craniofacial')
        self.assertEqual(pheno5.text, 'digestive/alimentary system')
        self.assertEqual(pheno6.text, 'endocrine/exocrine glands')
        self.assertEqual(pheno7.text, 'growth/size/body')
        self.assertEqual(pheno8.text, 'hearing/vestibular/ear')
        self.assertEqual(pheno9.text, 'homeostasis/metabolism')
        self.assertEqual(pheno10.text, 'immune system')
        self.assertEqual(pheno11.text, 'integument')
        self.assertEqual(pheno12.text, 'limbs/digits/tail')
        self.assertEqual(pheno13.text, 'mortality/aging')
        self.assertEqual(pheno14.text, 'muscle')
        self.assertEqual(pheno15.text, 'neoplasm')
        self.assertEqual(pheno16.text, 'nervous system')
        self.assertEqual(pheno17.text, 'pigmentation')
        self.assertEqual(pheno18.text, 'renal/urinary system')
        self.assertEqual(pheno19.text, 'respiratory system')
        self.assertEqual(pheno20.text, 'skeleton')
        self.assertEqual(pheno21.text, 'vision/eye')
        self.assertEqual(disease1.text, 'autosomal genetic disease')
        self.assertEqual(disease2.text, "gastrointestinal system disease")
        self.assertEqual(disease3.text, "integumentary system disease")
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (2)", "Genes tab is not visible!")
        gene_tab.click()
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        gene1 = cells[1]
        gene2 = cells[2]
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(gene1.text, 'Ednrb')
        self.assertEqual(gene2.text, 'EDNRB')
        #identify the Diseases tab and verify the tab's text
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        self.assertEqual(disease_tab.text, "Diseases (3)", "Diseases tab is not visible!")
        disease_tab.click()
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        cells = disease_table.get_column_cells("Disease")
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        disease1 = cells[1]
        disease2 = cells[2]
        disease3 = cells[3]
        #asserts that the correct diseases in the correct order are returned
        self.assertEqual(disease1.text, 'ABCD syndrome')
        self.assertEqual(disease2.text, "Hirschsprung's disease")
        self.assertEqual(disease3.text, "Waardenburg syndrome type 4A")

    def test_gene_symbol_dual_match(self):
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
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("TP53")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (7 x 38)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[0], "")
        self.assertEqual(searchTermItems[1], "")
        self.assertEqual(searchTermItems[2], "")
        self.assertEqual(searchTermItems[3], "")
        self.assertEqual(searchTermItems[4], "")
        self.assertEqual(searchTermItems[5], "TP53BP1")
        self.assertEqual(searchTermItems[6], "TP53")
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Tg(Trp53)1Srn")
        self.assertEqual(searchTermItems[1], "Tg(Trp53)bSrn")
        self.assertEqual(searchTermItems[2], "Tg(Trp53A135V)L3Ber")
        self.assertEqual(searchTermItems[3], "Tg(Trp53R172H)8512Jmr")
        self.assertEqual(searchTermItems[4], "Tg(Trp53R172L)4491Jmr")
        self.assertEqual(searchTermItems[5], "Trp53bp1")
        self.assertEqual(searchTermItems[6], "Trp53")
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (19)", "Genes tab is not visible!")
        gene_tab.click()
        #identify the Diseases tab and verify the tab's text
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        self.assertEqual(disease_tab.text, "Diseases (14)", "Diseases tab is not visible!")
        disease_tab.click()
        
    def test_gene_symbol_human_syn(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene symbol using a symbol that is a human synonym(LFS1 is a human synonym of Trp53)
        @see: HMDC-GQ-5
        '''
        print ("BEGIN test_gene_symbol_human_syn")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("LFS1")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (6 x 38)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[0], "")
        self.assertEqual(searchTermItems[1], "")
        self.assertEqual(searchTermItems[2], "")
        self.assertEqual(searchTermItems[3], "")
        self.assertEqual(searchTermItems[4], "")
        self.assertEqual(searchTermItems[5], "TP53")
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Tg(Trp53)1Srn")
        self.assertEqual(searchTermItems[1], "Tg(Trp53)bSrn")
        self.assertEqual(searchTermItems[2], "Tg(Trp53A135V)L3Ber")
        self.assertEqual(searchTermItems[3], "Tg(Trp53R172H)8512Jmr")
        self.assertEqual(searchTermItems[4], "Tg(Trp53R172L)4491Jmr")
        self.assertEqual(searchTermItems[5], "Trp53")
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (17)", "Genes tab is not visible!")
        gene_tab.click()
        #identify the Diseases tab and verify the tab's text
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        self.assertEqual(disease_tab.text, "Diseases (14)", "Diseases tab is not visible!")
        disease_tab.click()
        
    def test_gene_symbol_multiples(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by multiple Gene symbols (Foxm1, Lep, Ins2). There are 2 issues with this test, first selenium seems unable to locate the last 4 diseases in the grid so
        they have been commented out. The order of genes on the genes tab has Human symbols first, should be Mouse symbol first.
        @see HMDC-GQ-7
        '''
        print ("BEGIN test_gene_symbol_multiples")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
            
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys('Foxm1, Lep, Ins2')#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #r = requests.post
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (9 x 32)", "Grid tab is not visible!")
        grid_tab.click()
        #time.sleep(10)
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        #print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[0], "FOXM1")
        self.assertEqual(searchTermItems[1], "INS")
        self.assertEqual(searchTermItems[2], "LEP")
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print ("Grid: Human genes check done")
        
        searchTermItems1 = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems1[0], "Foxm1")
        self.assertEqual(searchTermItems1[1], "Ins2")
        self.assertEqual(searchTermItems1[2], "Lep")
        self.assertEqual(searchTermItems1[3], "Tg(Apcs-Lep)1Yog")
        self.assertEqual(searchTermItems1[4], "Tg(Apoe-Lep)1Kry")
        self.assertEqual(searchTermItems1[5], "Tg(Fabp4-LEP)F8Ffc")
        self.assertEqual(searchTermItems1[6], "Tg(H2-Ea-Ins2)1Wehi")
        self.assertEqual(searchTermItems1[7], "Tg(Ins2*Y16A)1Ell")
        self.assertEqual(searchTermItems1[8], "Tg(Ins2*Y16A)3Ell")#cells = mgenes.get_all()
        print ("Grid: Mouse genes check done")
    
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        time.sleep(8)
        #displays each row of phenotype/disease data
        pheno1 = cells[2]
        pheno2 = cells[3]
        pheno3 = cells[4]
        pheno4 = cells[5]
        pheno5 = cells[6]
        pheno6 = cells[7]
        pheno7 = cells[8]
        pheno8 = cells[9]
        pheno9 = cells[10]
        pheno10 = cells[11]
        pheno11 = cells[12]
        pheno12 = cells[13]
        pheno13 = cells[14]
        pheno14 = cells[15]
        pheno15 = cells[16]
        pheno16 = cells[17]
        pheno17 = cells[18]
        pheno18 = cells[19]
        pheno19 = cells[20]
        pheno20 = cells[21]
        pheno21 = cells[22]
        pheno22 = cells[23]
        pheno23 = cells[24]
        pheno24 = cells[25]
        pheno25 = cells[26]
        pheno26 = cells[27]
        disease1 = cells[29]
        disease2 = cells[30]
        disease3 = cells[31]
        disease4 = cells[32]
        disease5 = cells[33]
        disease6 = cells[34]
        #asserts that the correct phenotypes/diseases(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'adipose tissue')
        self.assertEqual(pheno2.text, 'behavior/neurological')
        self.assertEqual(pheno3.text, 'cardiovascular system')
        self.assertEqual(pheno4.text, 'cellular')
        self.assertEqual(pheno5.text, 'craniofacial')
        self.assertEqual(pheno6.text, 'digestive/alimentary system')
        self.assertEqual(pheno7.text, 'embryo')
        self.assertEqual(pheno8.text, 'endocrine/exocrine glands')
        self.assertEqual(pheno9.text, 'growth/size/body')
        self.assertEqual(pheno10.text, 'hearing/vestibular/ear')
        self.assertEqual(pheno11.text, 'hematopoietic system')
        self.assertEqual(pheno12.text, 'homeostasis/metabolism')
        self.assertEqual(pheno13.text, 'immune system')
        self.assertEqual(pheno14.text, 'integument')
        self.assertEqual(pheno15.text, 'limbs/digits/tail')
        self.assertEqual(pheno16.text, 'liver/biliary system')
        self.assertEqual(pheno17.text, 'mortality/aging')
        self.assertEqual(pheno18.text, 'muscle')
        self.assertEqual(pheno19.text, 'neoplasm')
        self.assertEqual(pheno20.text, 'nervous system')
        self.assertEqual(pheno21.text, 'renal/urinary system')
        self.assertEqual(pheno22.text, 'reproductive system')
        self.assertEqual(pheno23.text, 'respiratory system')
        self.assertEqual(pheno24.text, 'skeleton')
        self.assertEqual(pheno25.text, 'vision/eye')
        self.assertEqual(pheno26.text, 'normal phenotype')
        self.assertEqual(disease1.text, 'acquired metabolic disease')
        self.assertEqual(disease2.text, 'cell type cancer')
        self.assertEqual(disease3.text, 'endocrine system disease')
        self.assertEqual(disease4.text, 'gastrointestinal system disease')
        self.assertEqual(disease5.text, 'maturity-onset diabetes of the young')
        self.assertEqual(disease6.text, 'respiratory system disease')
        print ("Grid: phenotypes & diseases check done")
        
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        #print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (16)", "Genes tab is not visible!")
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
        self.assertEqual(gene1.text, 'Foxm1')
        self.assertEqual(gene2.text, 'FOXM1')
        self.assertEqual(gene3.text, 'INS')
        self.assertEqual(gene4.text, 'Ins2')
        self.assertEqual(gene5.text, 'LEP')
        self.assertEqual(gene6.text, 'Lep')
        '''plus 11 more genes, all transgenes'''
        #identify the Diseases tab and verify the tab's text
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        self.assertEqual(disease_tab.text, "Diseases (10)", "Diseases tab is not visible!")
        disease_tab.click()
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        cells = disease_table.get_column_cells("Disease")
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        disease1 = cells[1]
        disease2 = cells[2]
        disease3 = cells[3]
        disease4 = cells[4]
        disease5 = cells[5]
        disease6 = cells[6]
        disease7 = cells[7]
        disease8 = cells[8]
        disease9 = cells[9]
        disease10 = cells[10]
        #asserts that the correct diseases in the correct order are returned
        self.assertEqual(disease1.text, 'hepatocellular carcinoma')
        self.assertEqual(disease2.text, 'lung cancer')
        self.assertEqual(disease3.text, 'maturity-onset diabetes of the young')
        self.assertEqual(disease4.text, 'maturity-onset diabetes of the young type 10')
        self.assertEqual(disease5.text, 'metabolic syndrome X')
        self.assertEqual(disease6.text, 'obesity')
        self.assertEqual(disease7.text, 'permanent neonatal diabetes mellitus')
        self.assertEqual(disease8.text, 'type 1 diabetes mellitus')
        self.assertEqual(disease9.text, 'type 1 diabetes mellitus 2')        
        self.assertEqual(disease10.text, 'type 2 diabetes mellitus')

    
    def tearDown(self):
        self.driver.close()
       
       
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main() 