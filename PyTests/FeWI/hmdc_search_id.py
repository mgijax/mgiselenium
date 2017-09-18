'''
Created on Dec 16, 2016
These tests should cover searching by different IDs and verify the results
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

class TestHmdcSearchID(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)
        
        
    def test_do_term_id(self):
        '''
        @status Test of a query by DO ID.  Verify that a subset of annotations to that disease are returned in the grid.  Also, verify that the disease 
                is listed in the Disease Tab.  Do the search a 2nd time with the "DOID:" prefix - that search should fail.
        @see: HDMC-DQ-9 (primary DOID); HMDC-DQ-12 (DOID prefix required for search)
              HMDC-disease-10 (return matching diseases to Disease Tab); HMDC-grid-2 (return rows with annotations to DO term searched)
        '''
        print ("BEGIN test_do_term_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("DOID:11949")#enter primary DOID for Creutzfeldt-Jakob disease
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid Tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #Get the list of human and mouse genes
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        humanGeneList = iterate.getTextAsList(hgenes)
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGeneList = iterate.getTextAsList(mgenes)
        
        #Verify genes with annotations to this disease are present on the grid
        self.assertIn("HLA-DQB1", humanGeneList)
        self.assertIn("PRNP", humanGeneList)
        self.assertIn("H2-Ab1", mouseGeneList)
        self.assertIn("Prnp", mouseGeneList)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        time.sleep(2)
        print disease_tab.text
        disease_tab.click()
        
        #Verify disease searched for is returned
        #Get the list of diseases (by DOID)
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        cells = disease_table.get_column_cells("DO ID")
        diseaseList = iterate.getTextAsList(cells)
        self.assertIn('DOID:11949', diseaseList) #ID for Creutzfeldt-Jakob disease
        
        #Repeat the same search, but without the DOID prefix.  This search should return nothing.
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("11949")#enter primary DOID for Creutzfeldt-Jakob disease
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        time.sleep(2)
        print disease_tab.text
        disease_tab.click()
        
        #Verify no diseases are returned
        self.assertIn('No Matching Diseases', self.driver.page_source)

    def test_OMIM_term_id(self):
        '''
        @status Test of a query by OMIM ID (alternative ID for diseases).  Verify that the ID returns the correct results with and without the OMIM: prefix.
        @see: HMDC-DQ-11 (OMIM id with and without a prefix); HMDC-DQ-13 (OMIM gene IDs should return nothing when using this query field.)
              HMDC-grid-2 (return rows with annotations to DO term searched)
        '''
        print ("BEGIN test_do_term_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("OMIM:125852")#enter OMIM ID for type 1 diabetes mellitus 2
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        time.sleep(2)
        print disease_tab.text
        disease_tab.click()
        
        #Verify disease searched for is returned
        #Get the list of diseases (by OMIM ID)
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        cells = disease_table.get_column_cells("OMIM ID(s)")
        diseaseList = iterate.getTextAsList(cells)
        self.assertIn('OMIM:125852', diseaseList) #ID for type 1 diabetes mellitus 2
        
        #Repeat the same search, but without the DOID prefix.  This search should return nothing.
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("125852")#enter an OMIM ID without the prefix (a disease ID)
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        time.sleep(2)
        print disease_tab.text
        disease_tab.click()
        
        #Verify disease searched for is returned
        #Get the list of diseases (by OMIM ID)
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        cells = disease_table.get_column_cells("OMIM ID(s)")
        diseaseList = iterate.getTextAsList(cells)
        self.assertIn('OMIM:125852', diseaseList) #ID for type 1 diabetes mellitus 2
        
        #Do another search, but this time use an OMIM gene ID -- this search should return nothing using this query field
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("OMIM:605230")#enter an OMIM gene id -- this should return nothing using this query field
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Disease tab and click on it
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        time.sleep(2)
        print disease_tab.text
        disease_tab.click()
        
        #Look for no results message
        self.assertIn('No Matching Diseases', self.driver.page_source)
        
        
    def test_do_alt_ids(self):
        '''
        @status Test of a queries by alternate DO IDs -- secondary DOID; MESH id; NCI id; UMLS_CUI id
        @see: HDMC-DQ-10 (secondary DOIDs)
              HMDC-disease-10 (return matching diseases to Disease Tab); HMDC-grid-2 (return rows with annotations to DO term searched)
        '''
        print ("BEGIN test_do_term_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("DOID:183") #enter a DOID that is a secondary one for osteosarcoma
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        time.sleep(2)
        print disease_tab.text
        disease_tab.click()
        
        #Verify disease searched for is returned
        #Get the list of diseases (by DOID)
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        cells = disease_table.get_column_cells("DO ID")
        diseaseList = iterate.getTextAsList(cells)
        self.assertIn('DOID:3347', diseaseList) #primary DOID for osteosarcoma
        
        #Repeat the same search for another alt id of this disease
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("MESH:D012516") 
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        time.sleep(2)
        print disease_tab.text
        disease_tab.click()
        
        #Verify disease searched for is returned
        #Get the list of diseases (by DOID)
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        cells = disease_table.get_column_cells("DO ID")
        diseaseList = iterate.getTextAsList(cells)
        self.assertIn('DOID:3347', diseaseList) #primary DOID for osteosarcoma
        
        #Repeat the same search for another alt id of this disease
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("NCI:C9145") 
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        time.sleep(2)
        print disease_tab.text
        disease_tab.click()
        
        #Verify disease searched for is returned
        #Get the list of diseases (by DOID)
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        cells = disease_table.get_column_cells("DO ID")
        diseaseList = iterate.getTextAsList(cells)
        self.assertIn('DOID:3347', diseaseList) #primary DOID for osteosarcoma
        
        #Repeat the same search for another alt id of this disease
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element_by_xpath("//*[contains(text(), 'Click to modify search')]").click()
        
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("UMLS_CUI:C0206639") 
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        time.sleep(2)
        print disease_tab.text
        disease_tab.click()
        
        #Verify disease searched for is returned
        #Get the list of diseases (by DOID)
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        cells = disease_table.get_column_cells("DO ID")
        diseaseList = iterate.getTextAsList(cells)
        self.assertIn('DOID:3347', diseaseList) #primary DOID for osteosarcoma
        


    def test_mp_term_id(self):
        '''
        @status this test verifies the correct diseases are returned for this query, should return the MP term using an MP ID.
        @see: HMDC-PQ-16 (primary MP ID); HMDC-grid-2 (return row with MP annotations); 
              HMDC-genetab-5 (return genes with direct annotations, not orthologs)
        '''
        print ("BEGIN test_mp_term_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("MP:0005653")#primary ID for phototoxicity
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Gene tab and click on it
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        time.sleep(2)
        print gene_tab.text
        gene_tab.click()
        
        #Grab the gene list and verify the mouse gene is returned but NOT the human ortholog
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        geneList = iterate.getTextAsList(cells)
        
        self.assertIn('Ercc5', geneList)
        self.assertNotIn('ERCC5', geneList) #human gene should not be returned for MP ID searches 'cause they only match the mouse gene
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        grid_tab.click()
        
        #Get the list of mouse genes and verify expected gene is there
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        mouseGeneList = iterate.getTextAsList(mgenes)
        self.assertIn("Abcg2", mouseGeneList)
        
        #Click on the appropriate cell and verify the term searched for is in the pop-up
        #get the headings
        #phenocells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope") 
        #phenoHeaders = iterate.getTextAsList(phenocells)
        #self.assertIn("integument", phenoHeaders)
        
        phenocells = self.driver.find_elements_by_css_selector("td.ngc.center.cell.middle") 
        phenocells[6].click()#clicks the second phenotype data cell to open up the genotype popup page
        self.driver.switch_to_window(self.driver.window_handles[1])#switches focus to the genotype popup page
        
        #asserts the heading text is correct in page title
        self.assertEqual("Mouse integument abnormalities for ABCG2/Abcg2", self.driver.title)
        
        popup_table = Table(self.driver.find_elements_by_css_selector("p > table.popupTable "))
        cells = popup_table.get_header_cells()
        columnHeadings = iterate.getTextAsList(cells)
        print columnHeadings
        
        
        
        #Identify the table
        #mouse_geno_table = self.driver.find_element_by_css_selector("p > table.popupTable ")
        #data = mouse_geno_table.find_element_by_tag_name("td")
        #print data.text
        #find all the TR tags in the table and iterate through them
        #cells = mouse_geno_table.find_elements_by_tag_name("tr")
        #genoClusterList = iterate.getTextAsList(cells)
        
        #popupColHdg = self.driver.find_element_by_tag_name("mark")
        #print popupColHdg
        
    def test_mp_term_altid(self):
        '''
        @status this test verifies the correct diseases are returned for this query, should return the MP term using an alternate ID.
        @see: HMDC-PQ-18
        '''
        print ("BEGIN test_mp_term_altid")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Fyler:1431")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (25 x 32)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[0], "ATP2A2")
        self.assertEqual(searchTermItems[1], "ATP7A")
        self.assertEqual(searchTermItems[2], "")
        self.assertEqual(searchTermItems[3], "")
        self.assertEqual(searchTermItems[4], "")
        self.assertEqual(searchTermItems[5], "")
        self.assertEqual(searchTermItems[6], "ECE1")
        self.assertEqual(searchTermItems[7], "EDNRA")
        self.assertEqual(searchTermItems[8], "EFEMP2")
        self.assertEqual(searchTermItems[9], "FBLN5")
        self.assertEqual(searchTermItems[10], "FBN1")
        self.assertEqual(searchTermItems[11], "FOXE3")
        self.assertEqual(searchTermItems[12], "GATA5")
        self.assertEqual(searchTermItems[13], "GJA1")
        self.assertEqual(searchTermItems[14], "HECTD1")
        self.assertEqual(searchTermItems[15], "HSPG2")
        self.assertEqual(searchTermItems[16], "LOX")
        self.assertEqual(searchTermItems[17], "LTBP1")
        self.assertEqual(searchTermItems[18], "MUS81")
        self.assertEqual(searchTermItems[19], "PDGFRB")
        self.assertEqual(searchTermItems[20], "PLXND1")
        self.assertEqual(searchTermItems[21], "SMARCA4")
        self.assertEqual(searchTermItems[22], "TGFB2")
        self.assertEqual(searchTermItems[23], "TGFBR1")
        self.assertEqual(searchTermItems[24], "TGFBR2")
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Atp2a2")
        self.assertEqual(searchTermItems[1], "Atp7a")
        self.assertEqual(searchTermItems[2], "b2b370.1Clo")
        self.assertEqual(searchTermItems[3], "b2b370Clo")
        self.assertEqual(searchTermItems[4], "b2b635Clo")
        self.assertEqual(searchTermItems[5], "b2b1298Clo")
        self.assertEqual(searchTermItems[6], "Ece1")
        self.assertEqual(searchTermItems[7], "Ednra")
        self.assertEqual(searchTermItems[8], "Efemp2")
        self.assertEqual(searchTermItems[9], "Fbln5")
        self.assertEqual(searchTermItems[10], "Fbn1")
        self.assertEqual(searchTermItems[11], "Foxe3")
        self.assertEqual(searchTermItems[12], "Gata5")
        self.assertEqual(searchTermItems[13], "Gja1")
        self.assertEqual(searchTermItems[14], "Hectd1")
        self.assertEqual(searchTermItems[15], "Hspg2")
        self.assertEqual(searchTermItems[16], "Lox")
        self.assertEqual(searchTermItems[17], "Ltbp1")
        self.assertEqual(searchTermItems[18], "Mus81")
        self.assertEqual(searchTermItems[19], "Pdgfrb")
        self.assertEqual(searchTermItems[20], "Plxnd1")
        self.assertEqual(searchTermItems[21], "Smarca4")
        self.assertEqual(searchTermItems[22], "Tgfb2")
        self.assertEqual(searchTermItems[23], "Tgfbr1")
        self.assertEqual(searchTermItems[24], "Tgfbr2")
        #cells = mgenes.get_all()
        print searchTermItems

    def test_hp_term_id(self):
        '''
        @status this test verifies the correct phenotypes are returned for this query. Should return the HP term
        This test verifies the phenotypes displayed at an angle in correct sort order.
        @see: HDMC-PQ-??
        '''
        print ("BEGIN test_hp_term_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("HP:0006285")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print grid_tab.text
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (4 x 10)", "Grid tab is not visible!")
        grid_tab.click()
        #firstcell captures all the table data blocks of phenotypes on the first row of data
        phenocells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        print iterate.getTextAsList(phenocells) #if you want to see what it captures uncomment this
        
        pheno1 = phenocells[2]
        pheno2 = phenocells[3]
        pheno3 = phenocells[4]
        pheno4 = phenocells[5]
        pheno5 = phenocells[6]
        pheno6 = phenocells[7]
        pheno7 = phenocells[8]
        pheno8 = phenocells[9]
        #asserts that the correct phenotypess(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'craniofacial')
        self.assertEqual(pheno2.text, 'endocrine/exocrine glands')
        self.assertEqual(pheno3.text, 'growth/size/body')
        self.assertEqual(pheno4.text, 'homeostasis/metabolism')
        self.assertEqual(pheno5.text, 'limbs/digits/tail')
        self.assertEqual(pheno6.text, 'nervous system')
        self.assertEqual(pheno7.text, 'renal/urinary system')
        self.assertEqual(pheno8.text, 'skeleton')
                
    def test_do_term_xref_id(self):
        '''
        @status this test verifies the correct diseases are returned for this query. This is an alternate ID search 
        This test verifies the correct diseases are displayed on an angle in correct sort order.
        @see: HMDC-??
        '''
        print ("BEGIN test_do_term_xref_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("KEGG:04950")#identifies the input field and enters term/ID
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print grid_tab.text
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (17 x 20)", "Grid tab is not visible!")
        grid_tab.click()
        
        #cells captures every field from Human Gene heading to the last disease angled, this test only captures the diseases, which are items 25,26,27
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of gene data
        disease1 = cells[21]
        disease2 = cells[22]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(disease1.text, 'acquired metabolic disease')
        self.assertEqual(disease2.text, 'maturity-onset diabetes of the young')
        
    def test_mp_term_multi_id(self):
        '''
        @status this test verifies the correct genes are returned for this query, should return multiple MP terms results.
        @see: HMDC-PQ-21?
        '''
        print ("BEGIN test_mp_term_multi_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("MP:0011006, MP:0005653, MP:0011905")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (8 x 22)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[0], 'ABCG2')
        self.assertEqual(searchTermItems[1], 'CHST14')
        self.assertEqual(searchTermItems[2], 'EGR2')
        self.assertEqual(searchTermItems[3], 'ERCC5')
        self.assertEqual(searchTermItems[4], 'LGR4')
        self.assertEqual(searchTermItems[6], 'PMP22')
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        
        searchTermItems = iterate.getTextAsList(mgenes)
     
        self.assertEqual(searchTermItems[0], "Abcg2")
        self.assertEqual(searchTermItems[1], "Chst14")
        self.assertEqual(searchTermItems[2], "Egr2")
        self.assertEqual(searchTermItems[3], "Ercc5")
        self.assertEqual(searchTermItems[4], "Lgr4")
        self.assertEqual(searchTermItems[5], "Mirc35hg")
        self.assertEqual(searchTermItems[6], "Pmp22")
        self.assertEqual(searchTermItems[7], "Tg(Mpz-RAF1/ESR1)A668Ayld")
        #cells = mgenes.get_all()
        print searchTermItems
        

    def test_hp_term_multi_id(self):
        '''
        @status this test verifies the correct phenotypess are returned for this query. Should return multiple HP terms
        This test verifies the correct phenotypes return at an angle in the correct sort order.
        @see: HDMC-PQ-??
        '''
        print ("BEGIN test_hp_term_multi_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("HP:0008529, HP:0100739, HP:0012232")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print grid_tab.text
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (8 x 7)", "Grid tab is not visible!")
        grid_tab.click()
        
        #firstcell captures all the table data blocks of phenotypes on the first row of data
        phenocells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        print iterate.getTextAsList(phenocells) #if you want to see what it captures uncomment this
        
        pheno1 = phenocells[2]
        pheno2 = phenocells[3]
        pheno3 = phenocells[4]
        pheno4 = phenocells[5]
        #asserts that the correct phenotypess(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'behavior/neurological')
        self.assertEqual(pheno2.text, 'cardiovascular system')
        self.assertEqual(pheno3.text, 'hearing/vestibular/ear')
        self.assertEqual(pheno4.text, 'nervous system')

    def test_mixed_term_multi_id(self):
        '''
        @status this test verifies the correct diseases are returned for this query, should return data for multiple terms with a mix of HP, MP, and DO terms.
        This test uses an HP and an MP term, The HP term is  connected to markers DIAPH3 and OTOF.
        @see: HDMC-PQ-??
        '''
        print ("BEGIN test_mixed_term_multi_id")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("HP:0008529, MP:0008237")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (13 x 15)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[0], 'ASIP')
        self.assertEqual(searchTermItems[1], '')
        self.assertEqual(searchTermItems[2], '')
        self.assertEqual(searchTermItems[3], 'DIAPH3')
        self.assertEqual(searchTermItems[4], 'KIT')
        self.assertEqual(searchTermItems[5], 'KITLG')
        self.assertEqual(searchTermItems[6], 'OTOF')
        self.assertEqual(searchTermItems[7], '')
        self.assertEqual(searchTermItems[8], '')
        self.assertEqual(searchTermItems[9], '')
        self.assertEqual(searchTermItems[10], '')
        self.assertEqual(searchTermItems[11], 'TBX19')
        self.assertEqual(searchTermItems[12], 'USF2')
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        
        searchTermItems = iterate.getTextAsList(mgenes)
     
        self.assertEqual(searchTermItems[0], "a")
        self.assertEqual(searchTermItems[1], "Btnt")
        self.assertEqual(searchTermItems[2], "Btnt2")
        self.assertEqual(searchTermItems[3], "Diaph3")#cells = mgenes.get_all()
        self.assertEqual(searchTermItems[4], "Kit")
        self.assertEqual(searchTermItems[5], "Kitl")
        self.assertEqual(searchTermItems[6], "Otof")
        self.assertEqual(searchTermItems[7], "Rgsc71")
        self.assertEqual(searchTermItems[8], "Rgsc1246")
        self.assertEqual(searchTermItems[9], "Rgsc1513")
        self.assertEqual(searchTermItems[10], "rs")
        self.assertEqual(searchTermItems[11], "Tbx19")
        self.assertEqual(searchTermItems[12], "Usf2")
        
        print searchTermItems
        
    def test_do_term_id_down_dag(self):
        '''
        @status this test verifies the correct diseases are returned for this query down the dag.
        This test verifies the disease listed on the grid and then switches to the disease tab and verifies the 3 diseases listed there.
        @see: HDMC-??
        '''
        print ("BEGIN test_do_term_id_down_dag")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("DOID:2581")#identifies the input field and enters term/ID
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print grid_tab.text
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (7 x 24)", "Grid tab is not visible!")
        grid_tab.click()
        #cells captures every field from Human Gene heading to the last disease angled, this test only captures the diseases, which are items 25,26,27
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of gene data
        disease1 = cells[26]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(disease1.text, 'chondrodysplasia punctata')
        #self.assertEqual(disease2.text, 'X-linked chondrodysplasia punctata')
        wait.forAngular(self.driver)
        #identify the Diseases tab and verify the tab's text
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        self.assertEqual(disease_tab.text, "Diseases (7)", "Diseases tab is not visible!")
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
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(disease1.text, 'chondrodysplasia punctata')
        self.assertEqual(disease2.text, 'rhizomelic chondrodysplasia punctata')
        self.assertEqual(disease3.text, 'rhizomelic chondrodysplasia punctata type 1')
        self.assertEqual(disease4.text, 'rhizomelic chondrodysplasia punctata type 2')
        self.assertEqual(disease5.text, 'rhizomelic chondrodysplasia punctata type 3')
        self.assertEqual(disease6.text, 'rhizomelic chondrodysplasia punctata type 5')
        self.assertEqual(disease7.text, 'X-linked chondrodysplasia punctata')
        
                    
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
    HTMLTestRunner.main() 

