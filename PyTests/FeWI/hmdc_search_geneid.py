'''
Created on Jan 9, 2017
Updated: July 2017 (jlewis).  Updates to be more tolerant of data changes.  Cross-reference requirements with test cases. Remove assertions
in tests that are outside scope of requirement being tested.

This file contains the tests for Gene IDs (mouse and human) that are entered via the Gene Symbol(s)/ID(s) query field.  
Tests are organized in this order in the file:  Mouse gene ID tests, Human gene ID tests, and multiple ID tests

@author: jeffc
'''
import unittest
import time
#import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
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

class TestHmdcSearchGeneid(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)
        

    def test_gene_mgi_id(self):
        '''
        @status This test verifies the correct genes are returned for query by mouse MGI ID in the Gene Symbol/ID field.  Return the mouse
                gene and its human ortholog.
                Also verifies that IDs are not accepted in the Gene Name field.
        
        @see: HMDC-GQ-16 (query by MGI ID); HMDC-GQ-50 (don't accept IDs for query by Gene Name); 
        '''
        print ("BEGIN test_gene_mgi_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("MGI:96677")#identifies the input field and enters an MGI ID
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print(grid_tab.text)
        grid_tab.click()
        
        #Grab the human genes displayed on the Grid and verify that KIT is returned (ortholog of gene matched by ID entered)
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        humanGeneList = iterate.getTextAsList(hgenes)
        self.assertIn("KIT", humanGeneList)

        #Grab the mouse genes displayed on the Grid and verify that Kit is returned (gene matching ID entered)
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGeneList = iterate.getTextAsList(mgenes)
        self.assertIn("Kit", mouseGeneList)
        
        #Start over and attempt to query by ID with the Gene Name option -- expect this to return no results
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Repeat query using the Gene Name field
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("MGI:96677")
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print(grid_tab.text)
        grid_tab.click()
        
        #Look for no results message
        self.assertIn('No data available for your query', self.driver.page_source)
        
        
    def test_gene_ncbi_id_1(self):
        '''
        @status This test is for searching by Gene ID using NCBI mouse gene ID.  Expect only results in the Gene Tab for a mouse gene with
        no human ortholog.
        @see: HMDC-GQ-17 (query by mouse NCBI ID)
        '''
        print ("BEGIN test_gene_ncbi_id_1")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("105763")#identifies the input field and enters an NCBI ID
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and check for the gene with this ID.
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        gene1 = cells[1]
        #asserts that the correct genes are returned
        self.assertEqual(gene1.text, 'AA960008')

    def test_gene_ncbi_id_2(self):
        '''
        @status This test is for searching by Gene ID using NCBI gene ID.  Expect mouse gene returned plus human ortholog on Grid 
        and Gene Tabs.  Diseases rolled up for this gene returned to Disease Tab.
        @see: HMDC-GQ-17 (query by mouse NCBI ID)  HMDC-genetab-2 (return genes matching ID plus their ortholog); 
              HMDC-disease-9 (return diseases that roll-up to mouse gene and its human ortholog)
        '''
        print ("BEGIN test_gene_ncbi_id_2")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("14460")#identifies the input field and enters ID for Gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid Tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print(grid_tab.text)
        grid_tab.click()
        
        #Grab the human genes and verify the human homolog is in the list (GATA1)
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        humanGeneList = iterate.getTextAsList(hgenes)
        self.assertIn("GATA1", humanGeneList)
        
        #Grab the mouse genes and verify the mouse gene is in the list (Gata1)
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGeneList = iterate.getTextAsList(mgenes)
        self.assertIn("Gata1", mouseGeneList)
        
        #Switch to the Genes Tab and verify genes are there too
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Gata1', geneList)
        self.assertIn('GATA1', geneList)
        
        #Switch to the Disease Tab and verify diseases for mouse and human are present
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print(disease_tab.text)
        disease_tab.click()
        
        #Get the list of diseases (by DOID)
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        cells = disease_table.get_column_cells("DO ID")
        diseaseList = iterate.getTextAsList(cells)
        self.assertIn('DOID:14250', diseaseList) #ID for Down Syndrome (annotated to GATA1)
        self.assertIn('DOID:4971', diseaseList) #ID for myelofibrosis (annotated to Gata1)
        self.assertIn('DOID:1588', diseaseList) #ID for thrombocytopenia (annotated to both GATA1 and Gata1)
        
       
        
    '''def test_gene_all_vega_ids(self):
        
        @status This test is for searching by a mouse gene ID using a VEGA Gene Model ID, Transcript ID, and Protein ID.  All these queries 
                return the mouse gene and its human ortholog.***this test is no longer valid since Vega is removed from the system**
        @see: HMDC-GQ-19 (VEGA gene model ID, transcript ID, protein ID)
        
        print ("BEGIN test_gene_all_vega_ids")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("OTTMUSG00000005850")# enter VEGA gene model ID
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Ttc19', geneList)
        self.assertIn('TTC19', geneList)
        
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Redo the search using the VEGA transcript ID
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("OTTMUST00000013013")# enter VEGA transcript ID
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Ttc19', geneList)
        self.assertIn('TTC19', geneList)
        
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Redo the search using the VEGA protein ID
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("OTTMUSP00000006049")# enter VEGA protein ID
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Ttc19', geneList)
        self.assertIn('TTC19', geneList)
     '''   
        
    def test_gene_all_ensembl_ids(self):
        '''
        @status This test is for searching by a mouse gene ID using an Ensembl Gene Model ID, Transcript ID, and Protein ID.  All these queries 
                return the mouse gene and its human ortholog.
        @see: HMDC-GQ-18 (Ensembl gene model ID, transcript ID, protein ID)
        '''
        print ("BEGIN test_gene_all_ensembl_ids")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("ENSMUSG00000022098")# enter Ensembl gene model ID
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Bmp1', geneList)
        self.assertIn('BMP1', geneList)
        
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Redo the search using the VEGA transcript ID
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("ENSMUST00000022693")# enter Ensembl transcript ID
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Bmp1', geneList)
        self.assertIn('BMP1', geneList)
        
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Redo the search using the Ensembl protein ID
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("ENSMUSP00000022693")# enter VEGA protein ID
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Bmp1', geneList)
        self.assertIn('BMP1', geneList)
        
        
    def test_gene_all_uniprot_ids(self):
        '''
        @status This test is for searching for genes by the UniProt mouse ID types: SWISS-PROT and TrEMBL.  Verify that the mouse gene is returned 
                and its human ortholog on the Gene Tab.
        @see: HMDC-GQ-20 (SWISS-PROT and TrEMBL ID searches)
        '''
        print ("BEGIN test_gene_all_uniprot_ids")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("P32115") #enter the SWISS-PROT ID for Pax4
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('PAX4', geneList)
        self.assertIn('Pax4', geneList)
        
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Redo the search using a TrEMBL ID for Pax4
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("G3UZE8")# enter VEGA protein ID
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Pax4', geneList)
        self.assertIn('PAX4', geneList)
        
        
    def test_gene_protein_ids(self):
        '''
        @status This test is for searching for genes by the PDB and Protein Ontology mouse IDs.  Verify that the mouse gene is returned 
                and its human ortholog on the Gene Tab.
        @see: HMDC-GQ-21 (PDB ID search); HMDC-GQ-22 (Protein Ontology ID search)
        '''
        print ("BEGIN test_gene_protein_ids")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("PR:000004804") #enter the Protein Ontology ID for Brca2
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('BRCA2', geneList)
        self.assertIn('Brca2', geneList)
        
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Redo the search using a PDB ID
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("1MJE")# enter PDB ID for Brca2
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Brca2', geneList)
        self.assertIn('BRCA2', geneList)
      
        
    def test_gene_genbank_ids(self):
        '''
        @status This test is for searching for genes by a GenBank sequence mouse ID.  Verify that the mouse gene is returned 
                and its human ortholog on the Gene Tab.
        @see: HMDC-GQ-24 (Search by GenBank mouse sequence IDs: genomic and transcripts)
        '''
        print ("BEGIN test_gene_genbank_ids")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("BC111528") #enter a GenBank RNA sequence ID for Sry
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('SRY', geneList)
        self.assertIn('Sry', geneList)
        
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Redo the search using a genomic GenBank DNA sequence for Sry
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("AF068054")# enter GenBank DNA sequence for Sry
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('SRY', geneList)
        self.assertIn('Sry', geneList)
        
    def test_gene_affy_ids(self):
        '''
        @status This test is for searching for genes by Affy mouse IDs.  Verify that the mouse gene is returned 
                and its human ortholog on the Gene Tab.
        @see: HMDC-GQ-25 (Search by Affy IDs: 3 sets: Affy 1.0 ST; Affy 430 2.0; Affy U74)
        '''
        print ("BEGIN test_gene_affy_ids")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("10565422") #enter a Affy 1.0 ST id
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('TYR', geneList)
        self.assertIn('Tyr', geneList)
        
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Redo the search for another Affy ID type
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("1417717_a_at")# enter Affy 430 2.0 id
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('TYR', geneList)
        self.assertIn('Tyr', geneList)
        
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Redo the search for another Affy ID type
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("102666_at")# enter Affy U74 id
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('TYR', geneList)
        self.assertIn('Tyr', geneList)
        
    def test_gene_ec_id(self):
        '''
        @status This test is for searching by Gene ID using EC mouse gene ID.  Verify that the mouse gene is returned 
                and its human ortholog on the Gene Tab.
        @see: HMDC-GQ-26 (query by mouse EC IDs)
        '''
        print ("BEGIN test_gene_ec_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("1.11.1.6") #enter EC id for Cat
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and check for the gene with this ID.
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        #asserts that the correct genes in the correct order are returned
        self.assertIn('Cat', geneList)
        self.assertIn('CAT', geneList)
        
    def test_gene_miRBase_id(self):
        '''
        @status This test is for searching by Gene ID using miRBase mouse gene ID.  Verify that the mouse gene is returned 
                and its human ortholog on the Gene Tab.
        @see: HMDC-GQ-27 (query by mouse miRBase IDs)
        '''
        print ("BEGIN test_gene_miRBase_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("MI0000570") #enter miRBase ID for Mir22
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and check for the gene with this ID.
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        #asserts that the correct genes are returned
        self.assertIn('Mir22', geneList)
       
    
    def test_gene_ccds_id(self):
        '''
        @status This test is for searching by Gene ID using CCDS mouse gene ID.  Verify that the mouse gene is returned 
                and its human ortholog on the Gene Tab.
        @see: HMDC-GQ-28 (query by mouse Consensus CDS Project IDs)
        '''
        print ("BEGIN test_gene_ccds_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("CCDS36046.1") #enter CCDS id for Kitl
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and check for the gene with this ID.
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        #asserts that the correct genes are returned
        self.assertIn('Kitl', geneList)
        self.assertIn('KITLG', geneList)
        
    def test_gene_gtrosa_id(self):
        '''
        @status  The marker Gt(ROSA)26Sor is a special case in the HMDC.  This marker should not be returned to the Grid Tab, but is valid to be
                 returned on the Gene Tab.  This test is a search by its MGI ID.

        @see: HMDC-Grid-1 (don't return Gt(ROSA)26Sor to the Grid)
        '''
        print ("BEGIN test_gene_gtrosa_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("MGI:104735")#identifies the input field and enters Gt(ROSA)26Sor MGI id
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click on it.
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print(grid_tab.text)
        grid_tab.click()
        
        #Look for no results message
        self.assertIn('No data available for your query', self.driver.page_source)
        
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print(gene_tab.text)
        gene_tab.click()
        
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        #asserts that Gt(ROSA)26Sor is returned
        self.assertIn('Gt(ROSA)26Sor', geneList)
        
    def test_allele_id_fails(self):
        '''
        @status This test checks to make sure MGI allele IDs are not accepted in this field in the HMDC.
        
        @see: HMDC-GQ-29 (don't match Allele IDs)
        '''
        print ("BEGIN test_allele_id_fails")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("MGI:1856798") #enter allele MGI ID for A<y>; should return 0 results
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Look for no results message
        self.assertIn('No Matching Genes', self.driver.page_source)
        
    #
    #  HUMAN gene ID tests start here
    #
    
    
    def test_gene_human_ncbi_id(self):
        '''
       @status This test is for searching by Gene ID using NCBI human gene ID.  Expect human gene returned plus mouse ortholog on Grid 
        and Gene Tabs.  Diseases rolled up for these genes returned to Disease Tab.
        @see: HMDC-GQ-30 (query by human NCBI ID)  HMDC-genetab-2 (return genes matching ID plus their ortholog); 
              HMDC-disease-9 (return diseases annotated to human gene and rolled up to its mouse ortholog)
        '''
        print ("BEGIN test_gene_human_ncbi_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("5083")#identifies the input field: enter NCBI ID for human PAX9
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid Tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print(grid_tab.text)
        grid_tab.click()
        
        #Grab the human genes and verify the human gene is in the list (PAX9)
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        humanGeneList = iterate.getTextAsList(hgenes)
        self.assertIn("PAX9", humanGeneList)
        
        #Grab the mouse genes and verify the mouse ortholog is in the list (Pax9)
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGeneList = iterate.getTextAsList(mgenes)
        self.assertIn("Pax9", mouseGeneList)
        
        #Switch to the Genes Tab and verify genes are there too
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Pax9', geneList)
        self.assertIn('PAX9', geneList)
        
        #Switch to the Disease Tab and verify diseases for mouse and human are present
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print(disease_tab.text)
        disease_tab.click()
        
        #Get the list of diseases (by DOID)
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        cells = disease_table.get_column_cells("DO ID")
        diseaseList = iterate.getTextAsList(cells)
        self.assertIn('DOID:0050591', diseaseList) #ID for tooth agenesis (annotated to PAX9 and Pax9)
        
        
    def test_gene_human_uniprot_id(self):
        '''
        @status This test is for searching for genes by the UniProt human sequence id.  Verify that the human gene is returned 
                and its mouse ortholog on the Gene Tab.
        @see: HMDC-GQ-31 (human UniProt sequence id searches)
        '''
        print ("BEGIN test_gene_human_uniprot_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("P01116") #enter human uniprot id
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('KRAS', geneList)
        self.assertIn('Kras', geneList)
        
    def test_gene_human_nextprot_id(self):
        '''
        @status This test is for searching for genes by the NeXtProt id.  Verify that the human gene is returned 
                and its mouse ortholog on the Gene Tab.
        @see: HMDC-GQ-32 (human NeXtProt id searches)
        '''
        print ("BEGIN test_gene_human_nextprot_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("NX_Q99884") #enter human NeXtProt id
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Slc6a7', geneList)
        self.assertIn('SLC6A7', geneList)
        
    def test_gene_human_refseq_id(self):
        '''
        @status This test is for searching for genes by the RefSeq sequence id.  Verify that the human gene is returned 
                and its mouse ortholog on the Gene Tab.
        @see: HMDC-GQ-33 (human RefSeq sequence id searches)
        '''
        print ("BEGIN test_gene_human_refseq_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("NM_001672") #enter human RefSeq sequence id
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('a', geneList)
        self.assertIn('ASIP', geneList)
    
    def test_gene_human_genbank_id(self):
        '''
        @status This test is for searching for genes by the GenBank sequence id.  Verify that the human gene is returned 
                and its mouse ortholog on the Gene Tab.
        @see: HMDC-GQ-34 (human GenBank sequence id searches)
        '''
        print ("BEGIN test_gene_human_refseq_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("AK131274") #enter human GenBank sequence id
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Zfp704', geneList)
        self.assertIn('ZNF704', geneList)
    

    def test_gene_human_OMIM_id(self):
        '''
        @status This tests that an OMIM ID for a human gene returns that gene and its mouse ortholog.
        @see: HMDC-GQ-35 (OMIM gene IDs); HMDC-GQ-38 (do NOT return matches to OMIM Disease IDs)
        '''
        print ("BEGIN test_gene_human_OMIM_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("OMIM:191170")#identifies the input field and enters an OMIM gene ID
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Trp53', geneList)
        self.assertIn('TP53', geneList)
        
        #Open up the query form again (click on "Click to modify search" button)
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Redo the search for an OMIM disease ID -- should return no results using this query field
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("OMIM:222100")# OMIM disease ID
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Look for no results message
        self.assertIn('No Matching Genes', self.driver.page_source)
        

    def test_gene_human_hgnc_id(self):
        '''
        @status This tests that a HGNC ID for a human gene returns that gene and its mouse ortholog.
        @see: HMDC-GQ-36 (query by human HGNC id)
        '''
        print ("BEGIN test_gene_human_hgnc_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("HGNC:6554")#identifies the input field and enters an HGNC ID for LEPR
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Lepr', geneList)
        self.assertIn('LEPR', geneList)

    def test_gene_ID_rgd(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by RGD ID for a rat gene(RGD:2466 is associated to marker Cyp2b10 )
        @see: HMDC-GQ-37 (search by RGD id)
        '''
        print ("BEGIN test_gene_ID_rgd")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("RGD:2466") 
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        #asserts that the correct genes are returned
        self.assertIn('CYP2B6', geneList)
        self.assertIn('Cyp2b10', geneList)


    def test_gene_id_multiples(self):
        '''
        @status This is a test of a list of IDs in one query of Gene Symbols/IDs.  This is a mix of mouse gene IDs and human gene IDs.  The gene matching the ID
                is expected in the results plus their mouse or human ortholog.
        @see: HGNC-GQ-39 (list of IDs -- comma separated and space separated tests)
        '''
        print ("BEGIN test_gene_id_multiples")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element_by_name("formly_3_input_input_0").send_keys('MGI:1347487, HGNC:6553, MGI:96573') #IDs for Foxm1, LEP, Ins2
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Foxm1', geneList)
        self.assertIn('FOXM1', geneList)
        self.assertIn('Ins2', geneList)
        self.assertIn('INS', geneList)
        self.assertIn('Lep', geneList)
        self.assertIn('LEP', geneList)
        
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        #Do this search again -- this time space delimit the IDs
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
      
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys('MGI:1347487 HGNC:6553 MGI:96573') #IDs for Foxm1, LEP, Ins2
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes Tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        
        #Grab the list of genes and verify both mouse and human genes are present
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        self.assertIn('Foxm1', geneList)
        self.assertIn('FOXM1', geneList)
        self.assertIn('Ins2', geneList)
        self.assertIn('INS', geneList)
        self.assertIn('Lep', geneList)
        self.assertIn('LEP', geneList)

    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHmdcSearchGeneid))
    return suite
       
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
