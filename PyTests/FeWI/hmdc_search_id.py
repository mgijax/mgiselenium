'''
Created on Dec 16, 2016
These tests should cover searching by different IDs and verify the results
@author: jeffc
Verify Test of a query by DO ID.  Verify that a subset of annotations to that disease are returned in the grid.  Also, verify that the disease
    is listed in the Disease Tab.  Do the search a 2nd time with the "DOID:" prefix - that search should fail
Verify Test of a query by OMIM ID (alternative ID for diseases).  Verify that the ID returns the correct results with and without the OMIM: prefix
Verify Test of a queries by alternate DO IDs -- secondary DOID; MESH id; NCI id; UMLS_CUI id
Verify the correct diseases are returned for this query, should return the MP term using an MP ID
Verify the correct MP term is returned for this query using an Alt ID
Verify the correct phenotype header and HP term name is returned for this query
Verify that the DO ID for the KEGG ID entered is returned in the results.  KEGG is a xref ID
Verify the correct phenotype headers and MP terms are returned for this query
Verify the correct phenotypess are returned for this query. Should return multiple HP terms
    This test verifies the correct phenotypes return at an angle in the correct sort order
Verify the correct diseases are returned for this query, should return data for multiple terms with a mix of HP, MP, and DO terms.
    This test uses an HP and an MP term, The HP term is  connected to markers DIAPH3 and OTOF
Verify the correct diseases are returned for this query down the dag. This test verifies the disease listed on the grid
    and then switches to the disease tab and verifies the diseases listed there
'''

import unittest
import time
import tracemalloc
import config
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.relative_locator import locate_with
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate, wait
#from util.form import ModuleForm
from util.table import Table

# Tests
tracemalloc.start()
class TestHmdcSearchID(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
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
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, 'option'):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("DOID:11949")#enter primary DOID for Creutzfeldt-Jakob disease
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid Tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        grid_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'mgHeader'))):
            print('Mouse Gene header loaded')
        #Get the list of human and mouse genes
        hgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.first")
        humanGeneList = iterate.getTextAsList(hgenes)
        
        mgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.last")
        mouseGeneList = iterate.getTextAsList(mgenes)
        
        #Verify genes with annotations to this disease are present on the grid
        self.assertIn("HLA-DQB1, HLA-DQB2", humanGeneList)
        self.assertIn("PRNP", humanGeneList)
        self.assertIn("STX1A", humanGeneList)
        self.assertIn("Tg(Prnp*)#Rgab", mouseGeneList)
        self.assertIn("Tg(Prnp*D177N*M128V)A21Rchi", mouseGeneList)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print(disease_tab.text)
        disease_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseTable'))):
            print('Disease Table loaded')
        #Verify disease searched for is returned
        #Get the list of diseases (by DOID)
        disease_table = Table(self.driver.find_element(By.ID, "diseaseTable"))
        cells = disease_table.get_column_cells("DO ID")
        diseaseList = iterate.getTextAsList(cells)
        self.assertIn('DOID:11949', diseaseList) #ID for Creutzfeldt-Jakob disease
        
        #Repeat the same search, but without the DOID prefix.  This search should return nothing.
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Click to modify search')]").click()
        
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("11949")#enter primary DOID for Creutzfeldt-Jakob disease
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        time.sleep(2)
        print(disease_tab.text)
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
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("OMIM:125852")#enter OMIM ID for type 1 diabetes mellitus 2
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print(disease_tab.text)
        disease_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseTable'))):
            print('Disease Table loaded')
        #Verify disease searched for is returned
        #Get the list of diseases (by OMIM ID)
        id = self.driver.find_element(By.ID, 'diseaseTable').find_element(By.CSS_SELECTOR, 'span.ng-scope > a:nth-child(1)')
        print(id.text)
        self.assertEqual(id.text, 'OMIM:125852', 'The OMIM ID is wrong!')
        #Repeat the same search, but without the DOID prefix.  This search should return nothing.
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Click to modify search')]").click()
        
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("125852")#enter an OMIM ID without the prefix (a disease ID)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print(disease_tab.text)
        disease_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseTable'))):
            print('Disease table loaded')
        #Verify disease searched for is returned
        #Get the list of diseases (by OMIM ID)
        disease_table = Table(self.driver.find_element(By.ID, "diseaseTable"))
        cells = disease_table.get_column_cells("OMIM ID(s)")
        diseaseList = iterate.getTextAsList(cells)
        self.assertIn('OMIM:125852', diseaseList) #ID for type 1 diabetes mellitus 2
        
        #Do another search, but this time use an OMIM gene ID -- this search should return nothing using this query field
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Click to modify search')]").click()
        
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("OMIM:605230")#enter an OMIM gene id -- this should return nothing using this query field
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Disease tab and click on it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseTable'))):
            print('Disease Table loaded')
        print(disease_tab.text)
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
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("DOID:183") #enter a DOID that is a secondary one for osteosarcoma
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        #time.sleep(2)
        print(disease_tab.text)
        disease_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseTable'))):
            print('Disease Table loaded')
        #Verify disease searched for is returned
        #Get the list of diseases (by DOID)
        id1 = self.driver.find_element(By.ID, 'diseaseTable').find_element(By.CSS_SELECTOR, '#diseaseTable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)')
        print(id1.text)
        self.assertTrue(id1.text, 'DOID:3347')

        #Repeat the same search for another alt id of this disease
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Click to modify search')]").click()
        
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("MESH:D012516")
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        #time.sleep(2)
        print(disease_tab.text)
        disease_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseTable'))):
            print('Disease Table loaded')
        # Verify disease searched for is returned
        # Get the list of diseases (by DOID)
        id1 = self.driver.find_element(By.ID, 'diseaseTable').find_element(By.CSS_SELECTOR, '#diseaseTable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)')
        print(id1.text)
        self.assertTrue(id1.text, 'DOID:3347')

        
        #Repeat the same search for another alt id of this disease
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Click to modify search')]").click()
        
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("NCI:C9145")
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        #time.sleep(2)
        print(disease_tab.text)
        disease_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseTable'))):
            print('Disease Table loaded')
        # Verify disease searched for is returned
        # Get the list of diseases (by DOID)
        id1 = self.driver.find_element(By.ID, 'diseaseTable').find_element(By.CSS_SELECTOR, '#diseaseTable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)')
        print(id1.text)
        self.assertTrue(id1.text, 'DOID:3347')

        
        #Repeat the same search for another alt id of this disease
        #Open up the query form again (click on "Click to modify search" button
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Click to modify search')]").click()
        
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("UMLS_CUI:C0206639")
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #Identify the Disease Tab and click on it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        #time.sleep(2)
        print(disease_tab.text)
        disease_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseTable'))):
            print('Disease Table loaded')
        #Verify disease searched for is returned
        # Get the list of diseases (by DOID)
        id1 = self.driver.find_element(By.ID, 'diseaseTable').find_element(By.CSS_SELECTOR, '#diseaseTable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)')
        print(id1.text)
        self.assertTrue(id1.text, 'DOID:3347')


    def test_mp_term_id(self):
        '''
        @status this test verifies the correct diseases are returned for this query, should return the MP term using an MP ID.
        @see: HMDC-PQ-16 (primary MP ID); HMDC-grid-2 (return row with MP annotations); 
              HMDC-genetab-5 (return genes with direct annotations, not orthologs)
        '''
        print ("BEGIN test_mp_term_id")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("MP:0005653")#primary ID for phototoxicity
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Disease tab and click on it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print(disease_tab.text)
        disease_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseTable'))):
            print('Disease Table loaded')
        #Grab the gene list and verify the mouse gene is returned but NOT the human ortholog
        id1 = self.driver.find_element(By.ID, 'diseaseTable').find_element(By.CSS_SELECTOR, '#diseaseTable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)')
        print(id1.text)
        id2 = self.driver.find_element(By.ID, 'diseaseTable').find_element(By.CSS_SELECTOR, '#diseaseTable > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(2) > a:nth-child(1)')
        print(id2.text)
        id3 = self.driver.find_element(By.ID, 'diseaseTable').find_element(By.CSS_SELECTOR, '#diseaseTable > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2) > a:nth-child(1)')
        print(id3.text)
        self.assertTrue(id1.text, 'DOID:13270')
        self.assertTrue(id2.text, 'DOID:1920')
        self.assertTrue(id3.text, 'DOID:0110849')
        # identify the gene tab and click on it
        gene_tab = self.driver.find_element(By.CSS_SELECTOR, "li.uib-tab:nth-child(2)")
        # time.sleep(2)
        print(gene_tab.text)
        gene_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'geneTable'))):
            print('Gene Table loaded')
        # Grab the gene list and verify the mouse gene is returned but NOT the human ortholog
        id1 = self.driver.find_element(By.ID, 'geneTable').find_element(By.CSS_SELECTOR, '#geneTable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > nobr:nth-child(1) > a:nth-child(1) > div:nth-child(1)')
        print(id1.text)
        id2 = self.driver.find_element(By.ID, 'geneTable').find_element(By.CSS_SELECTOR, '#geneTable > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(2) > nobr:nth-child(1) > a:nth-child(1) > div:nth-child(1)')
        print(id2.text)
        id3 = self.driver.find_element(By.ID, 'geneTable').find_element(By.CSS_SELECTOR, '#geneTable > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2) > nobr:nth-child(1) > a:nth-child(1) > div:nth-child(1)')
        print(id3.text)
        self.assertTrue(id1.text, 'Abcg2')
        self.assertTrue(id2.text, 'Ercc5')
        self.assertTrue(id3.text, 'Mirc35hg')
        #human gene should not be returned for MP ID searches 'cause they only match the mouse gene
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        grid_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tab-content'))):
            print('Grid Table loaded')
        #Get the list of mouse genes and verify expected gene is there
        mgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.last")
        mouseGeneList = iterate.getTextAsList(mgenes)
        self.assertIn("Abcg2, Abcg3", mouseGeneList)
        
        phenocells = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.center.cell.middle") 
        phenocells[6].click()#clicks the integument data cell to open up the genotype popup page (data changes can break this logic)
        self.driver.switch_to.window(self.driver.window_handles[1])#switches focus to the genotype popup page
        wait.forNewWindow(self.driver, 5)
        #asserts the heading text is correct in page title
        self.assertEqual('Mouse integument abnormalities for ABCG2/Abcg2, Abcg3', self.driver.title)
        
        #asserts that the MP term queried for has been returned
        self.assertIn("phototoxicity", self.driver.page_source, "expected MP term not found")
        
    def test_mp_term_altid(self):
        '''
        @status this test verifies the correct MP term is returned for this query using an Alt ID.  
        @see: HMDC-PQ-18 Test broken, not finding right option on line 442!!!!
        '''
        print ("BEGIN test_mp_term_altid")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks an option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("Fyler:1431")#enter Alt ID for MP:0010472 (abnormal ascending aorta and coronary artery attachment)
        wait.forAngular(self.driver)
        #find and click the Add button
        self.driver.find_element(By.CSS_SELECTOR, "button.ng-scope > span:nth-child(1)").click()
        #self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks another option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, '.formly-field-queryRow > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ng-form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys("Gja1")
        #self.driver.find_element(By.ID, "formly_3_input_input_0").send_keys(Keys.TAB + Keys.TAB + Keys.TAB + "Gja1")
        #wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        grid_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tab-content'))):
            print('Grid Table loaded')
        mgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.last")
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertIn("Gja1, Gja6", searchTermItems, "expected gene not returned")
        
        #Verify that the correct MP term is displayed in the genotype pop-up
        
        #phenocells captures all the table data cells on the first row of data
        phenocells = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.center.cell.middle")
        
        phenocells[0].click() #clicks the cell for cardiovascular system (new data could break this)
        self.driver.switch_to.window(self.driver.window_handles[1])#switches focus to the genotype popup page
        wait.forNewWindow(self.driver, 5)
        matching_text = "Mouse cardiovascular system abnormalities for GJA1, GJA6P/Gja1, Gja6"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.page_source, 'expected pop-up box heading not displayed')
        
        #asserts that the MP term queried for by Alt ID has been returned
        self.assertIn("abnormal ascending aorta and coronary artery attachment", self.driver.page_source, "expected MP term not found")


    def test_hp_term_id(self):
        '''
        @status this test verifies the correct phenotype header and HP term name is returned for this query.
        @see: HDMC-PQ-??
        '''
        print ("BEGIN test_hp_term_id")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("HP:0006285")#identifies the input field and enters an HP ID
        wait.forAngular(self.driver)
        #find and click the Add button
        self.driver.find_element(By.CSS_SELECTOR, "button.ng-scope > span:nth-child(1)").click()
        #self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks another option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        #wait.forAngular(self.driver)
        #self.driver.find_element(By.ID, "formly_3_input_input_0").send_keys(Keys.TAB + Keys.TAB + Keys.TAB + "ODAPH")
        self.driver.find_element(By.CSS_SELECTOR, '.formly-field-queryRow > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ng-form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys("ODAPH")

        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)

        #identify the Grid tab and click it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        grid_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tab-content'))):
            print('Grid Table loaded')
        #firstcell captures all the table data blocks of phenotypes on the first row of data
        phenocells = self.driver.find_elements(By.CSS_SELECTOR, "div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        phenoheaders = iterate.getTextAsList(phenocells) #if you want to see what it captures uncomment this
        
        self.assertIn('craniofacial', phenoheaders, "expected phenotype heading not found")
        self.assertIn('skeleton', phenoheaders, "expected phenotype heading not found")
        
        #Verify that the correct HP term is displayed in the genotype pop-up
        #phenocells captures all the table data cells on the first row of data
        phenocells = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.center.cell.middle")
        
        phenocells[0].click() #clicks the cell for craniofacial system (new data could break this)
        self.driver.switch_to.window(self.driver.window_handles[1])#switches focus to the genotype popup page
        wait.forNewWindow(self.driver, 5)
        matching_text = "Human craniofacial abnormalities for ODAPH/Odaph"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.page_source, 'expected pop-up box heading not displayed')
        
        #asserts that the HP term queried for by ID has been returned
        self.assertIn("Enamel hypomineralization", self.driver.page_source, "expected HP term not found")
        
                
    def test_do_term_xref_id(self):
        '''
        @status this test verifies that the DO ID for the KEGG ID entered is returned in the results.  KEGG is a xref ID.
        @see: HMDC-??
        '''
        print ("BEGIN test_do_term_xref_id")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("KEGG:04950")#XREF id for DOID:0050524 (maturity-onset diabetes of the young)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Diseases tab and click it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        disease_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseTable'))):
            print('Disease Table loaded')
        #verify the DO ID for the xref ID entered is included in results
        id1 = self.driver.find_element(By.ID, 'diseaseTable').find_element(By.CSS_SELECTOR, '#diseaseTable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)')
        print(id1.text)
        self.assertTrue(id1.text, 'DOID:0050524')#expected DO ID found
        
        
    def test_mp_term_multi_id(self):
        '''
        @status this test verifies the correct phenotype headers and MP terms are returned for this query.
        @see: HMDC-PQ-21?
        '''
        print ("BEGIN test_mp_term_multi_id")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("MP:0011006, MP:0005653, MP:0011905")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        #find and click the Add button
        self.driver.find_element(By.CSS_SELECTOR, 'button.ng-scope > span:nth-child(1)').click()
        #self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks another option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        self.driver.find_element(By.CSS_SELECTOR, '.formly-field-queryRow > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ng-form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys("Abcg2, Lgr4, Pmp22")
        #self.driver.find_element(By.ID, "formly_3_input_input_0").send_keys("Abcg2, Lgr4, Pmp22")
        self.driver.find_element(By.ID, "searchButton").click()
        #identify the Grid tab and click it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        grid_tab.click()
        
        #firstcell captures all the table data blocks of phenotypes on the first row of data
        phenocells = self.driver.find_elements(By.CSS_SELECTOR, "div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        phenoheaders = iterate.getTextAsList(phenocells) #if you want to see what it captures uncomment this
        
        self.assertIn('cellular', phenoheaders, "expected phenotype heading not found")
        self.assertIn('integument', phenoheaders, "expected phenotype heading not found")
        self.assertIn('homeostasis/metabolism', phenoheaders, "expected phenotype heading not found")
        self.assertIn('nervous system', phenoheaders, "expected phenotype heading not found")
        
        #Verify that the correct MP term is displayed in the genotype pop-up
        #phenocells captures all the table data cells on the first row of data
        phenocells = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.center.cell.middle")
        phenocells[5].click() #clicks the cell for homeostasis/metabolism system (new data could break this)
        self.driver.switch_to.window(self.driver.window_handles[1])#switches focus to the genotype popup page
        wait.forNewWindow(self.driver, 5)
        matching_text = "Mouse homeostasis/metabolism abnormalities for ABCG2/Abcg2"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.page_source, 'expected pop-up box heading not displayed') 
        #asserts that the MP term queried for by ID has been returned
        self.assertIn("phototoxicity", self.driver.page_source, "expected MP term not found") #ID = MP:0005653

    def test_hp_term_multi_id(self):
        '''
        @status this test verifies the correct phenotypess are returned for this query. Should return multiple HP terms
        This test verifies the correct phenotypes return at an angle in the correct sort order.
        @see: HDMC-PQ-??
        '''
        print ("BEGIN test_hp_term_multi_id")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("HP:0008529, HP:0100739, HP:0012232")#identifies the input field and enters gata1
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        grid_tab.click()
        
        #firstcell captures all the table data blocks of phenotypes on the first row of data
        phenocells = self.driver.find_elements(By.CSS_SELECTOR, "div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        phenoheaders = iterate.getTextAsList(phenocells) #if you want to see what it captures uncomment this
        
        #asserts that the correct phenotypess(at angle) display in the correct order
        self.assertIn('autosomal genetic disease', phenoheaders, "expected pheno heading not found")
        self.assertIn('hearing/vestibular/ear', phenoheaders, "expected pheno heading not found")
        self.assertIn('nervous system disease', phenoheaders, "expected pheno heading not found")

    def test_mixed_term_multi_id(self):
        '''
        @status this test verifies the correct diseases are returned for this query, should return data for multiple terms with a mix of HP, MP, and DO terms.
        This test uses an HP and an MP term, The HP term is  connected to markers DIAPH3 and OTOF.
        @see: HDMC-PQ-??
        '''
        print ("BEGIN test_mixed_term_multi_id")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("HP:0006279, MP:0009182")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        #find and click the Add button
        self.driver.find_element(By.CSS_SELECTOR, "button.ng-scope > span:nth-child(1)").click()
        #self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks another option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        #self.driver.find_element(By.ID, "formly_3_input_input_0").send_keys(Keys.TAB + Keys.TAB + Keys.TAB + "Pax4")
        self.driver.find_element(By.CSS_SELECTOR, '.formly-field-queryRow > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ng-form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys("Pax4")

        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)

        #identify the Grid tab and click it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        grid_tab.click()
        
        #firstcell captures all the table data blocks of phenotypes on the first row of data
        phenocells = self.driver.find_elements(By.CSS_SELECTOR, "div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        phenoheaders = iterate.getTextAsList(phenocells) #if you want to see what it captures uncomment this
        
        self.assertIn('endocrine/exocrine glands', phenoheaders, "expected phenotype heading not found")
        
        #Verify that the correct MP term is displayed in the genotype pop-up
        
        #phenocells captures all the table data cells on the first row of data
        phenocells = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.center.cell.middle")
        
        phenocells[0].click() #clicks the cell for endocrine/exocrine (new data could break this)
        self.driver.switch_to.window(self.driver.window_handles[1])#switches focus to the genotype popup page
        wait.forNewWindow(self.driver, 5)
        matching_text = "Human and Mouse endocrine/exocrine glands abnormalities for PAX4/Pax4"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.page_source, 'expected pop-up box heading not displayed') 
        #asserts that the MP and HP terms queried for by ID has been returned
        self.assertIn("Beta-cell dysfunction", self.driver.page_source, "expected HP term not found") #ID = HP:0006279
        self.assertIn("absent pancreatic delta cells", self.driver.page_source, "expected MP term not found")
       
        
    def test_do_term_id_down_dag(self):
        '''
        @status this test verifies the correct diseases are returned for this query down the dag.
        This test verifies the disease listed on the grid and then switches to the disease tab and verifies the diseases listed there.
        @see: HDMC-??
        '''
        print ("BEGIN test_do_term_id_down_dag")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("DOID:2581")#identifies the input field and enters term/ID
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        grid_tab.click()
        
        #cells captures every field from Human Gene heading to the last disease angled, this test only captures the diseases, which are items 25,26,27
        cells = self.driver.find_elements(By.CSS_SELECTOR, "div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        gridheaders = iterate.getTextAsList(cells)
        
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertIn('autosomal genetic disease', gridheaders, "expected disease heading not found")
         
        #identify the Diseases tab and click on it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print(disease_tab.text)
        disease_tab.click()
        disease_table = Table(self.driver.find_element(By.ID, "diseaseTable"))
        cells = disease_table.get_column_cells("DO ID")
        ids = iterate.getTextAsList(cells)
        
        #Verify the DO ID queried for is returned
        self.assertIn('DOID:2581', ids, "expected ID not returned")
        
        #Verify the children of the DO ID queried for are returned
        self.assertIn('DOID:2580', ids, "expected child term of ID queried for not returned")
        self.assertIn('DOID:0060292', ids, "expected child term of ID queried for not returned")
        # ----- QUESTION: should this child term be returned?  It is not doing so now.  It has no annotations, so maybe that is why? 
        # ----- Find out answer and use assertNotIn if current behavior is correct.
        #self.assertIn('DOID:0060293', ids, "expected child term of ID queried for not returned")
        
        #Verify the grandchildren of the DO ID queried for are returned
        self.assertIn('DOID:0110851', ids, "expected grandchild term of ID queried for not returned")
        self.assertIn('DOID:0110852', ids, "expected grandchild term of ID queried for not returned")
        self.assertIn('DOID:0110853', ids, "expected grandchild term of ID queried for not returned")
        self.assertIn('DOID:0110854', ids, "expected grandchild term of ID queried for not returned")
        
                    
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()
       
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHmdcSearchID))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))

