'''
Created on Dec 13, 2016
These tests should cover searching by different terms and verify the results.  Updated November 2017 (jlewis).  Reworked each test to be less vulnerable to data changes.
E.g. removed assertions re: counts; changed assertEqual to assertIn; etc.  All tests worked as-of Nov 15 2017 using the Test WI.
@author: jeffc
'''

import unittest
import time
#import requests
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
#from util.form import ModuleForm
from util.table import Table

# Tests
tracemalloc.start()
class TestHmdcSearchTerm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)
        
    def test_index_tab_headers(self):
        '''
        @status this test verifies the headings on the Gene Homologs x Phenotypes/Diseases tab
                ( or Index tab) are correct and in the correct order.
        @see: HMDC-
        '''
        print ("BEGIN test_index_tab_headers")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        self.driver.find_element(By.ID, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("Gata1")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        wait.forAngular(self.driver)
        print(grid_tab.text)
        time.sleep(2)
        self.assertIn("Gene Homologs x Phenotypes/Diseases", grid_tab.text, "Grid tab is not visible!")
        grid_tab.click()
        human_header = self.driver.find_element(By.CLASS_NAME, 'hgHeader')
        self.assertEqual(human_header.text, 'Human Gene', 'The human gene header is missing')
        mouse_header = self.driver.find_element(By.CLASS_NAME, 'mgHeader')
        self.assertEqual(mouse_header.text, 'Mouse Gene', 'The mouse gene header is missing')
        #self.driver.execute_script(script)
        
    def test_do_term_name(self):
        '''
        @status this test verifies the correct diseases are returned for this query. This Disease term Heading should
        only bring back the disease mucosulfatidosis. Verified by clicking the disease pop-up and confirming this is the only disease.  Add'l annotations that return
        a new phenotype column will break this test.  
        @see: HMDC-DQ-1
        '''
        print("BEGIN test_do_term_name")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys("mucosulfatidosis")#identifies the input field and enters term/ID
        #time.sleep(5)
        self.driver.find_element(By.ID, "searchButton").click()
        #identify the Grid tab and verify the tab's text
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        wait.forAngular(self.driver)
        time.sleep(3)
        print(grid_tab.text)
        time.sleep(2)
        self.assertIn(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 20)", "Data has changed for this test - update may be needed")
        grid_tab.click()
        
        #cells captures every field from Human Gene heading to the last disease angled, this test is only testing the disease.
        cells = self.driver.find_elements(By.CSS_SELECTOR, "div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each angled column of disease heading, note that there is 1 blank field between pheno headings and disease headings.
        disease1 = cells[22]
        print(disease1.text)
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(disease1.text, 'inherited metabolic disorder')
        
        #phenocells captures the inherited metabolic disorder cell on the first row of data
        phenocells = self.driver.find_element(By.CSS_SELECTOR, "td.middle:nth-child(23) > div:nth-child(1) > div:nth-child(1)")
        phenocells.click() #clicks the disease cell (last one in list) to open up the genotype popup page
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])#switches focus to the genotype popup page
        time.sleep(5)
        matching_text = "Human Genes and Mouse Models for inherited metabolic disorder and SUMF1/Sumf1"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.page_source, 'matching text not displayed')
        
        #Identify the table that contains the disease angled text
        popup_table = self.driver.find_element(By.CLASS_NAME, "popupTable")
        
        disease_data = popup_table.find_element(By.CSS_SELECTOR, "span > a")
        print(disease_data.text)
        #asserts that the correct disease is displayed
        self.assertEqual(disease_data.text, 'mucosulfatidosis')
        
        
    def test_mp_term_name(self):
        '''
        @status this test verifies the correct diseases are returned for this query, should return the MP term.
        This test is verifying the correct mouse genes are returned.
        @bug: need to figure out how to identify second search by option field.
        @see: HMDC-PQ-1
        '''
        print("BEGIN test_mp_term_name")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the phenotype name option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys("meteorism")#identifies the input field and enters term
        wait.forAngular(self.driver)
        
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks the phenotype name option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            print(option.text)
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.ID, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("Celsr3")#identifies the input field and enters Celsr3
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and verify the tab's text
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print(("grid tab counts =", grid_tab.text))
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 8)", "Grid tab is not visible!")
        grid_tab.click()
        
        mgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.last")
        
        searchTermItems = iterate.getTextAsList(mgenes)
     
        self.assertEqual(searchTermItems[0], "Celsr3")
        print(searchTermItems)
        
        # Add checks for Phenotype Categories returned
        #cells captures every field from Human Gene heading to the last angled term -- this test checks that the 2 MP headers associated with this term are displayed
        cells = self.driver.find_elements(By.CSS_SELECTOR, "div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        cellHeadings = iterate.getTextAsList(cells)
       
        self.assertIn('digestive/alimentary system', cellHeadings, "expected MP header not found")
        self.assertIn('growth/size/body', cellHeadings, "expected MP header not found")

    def test_hp_term_name(self):
        '''
        @status this test  Should return the HP term queried for in the results of the Grid and also the pop-up genotype.
        This test is verifying the correct phenotypes(for Human) are coming back on the grid tab.  Include a specific
        gene in the search so that only human annotations are returned.
        @see: HMDC-PQ-9
        '''
        print("BEGIN test_hp_term_name")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys("fusion of middle ear ossicles")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks the phenotype name option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            print(option.text)
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.ID, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("TFAP2A")#identifies the input field and enters Celsr3
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        
        #Identify the grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        time.sleep(2)
        grid_tab.click()
        
        #headingcells captures all column headings of the grid
        headingcells = self.driver.find_elements(By.CSS_SELECTOR, "div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        searchTermItems = iterate.getTextAsList(headingcells)
        print(searchTermItems) #if you want to see what it captures uncomment this
        
        #verify that the correct MP header terms for this phenotype term are included in the grid
         
        self.assertIn('hearing/vestibular/ear', searchTermItems, "expected MP header not returned")
        self.assertIn('skeleton', searchTermItems, "expected MP header not returned")
        
        #Verify that the actual term is displayed in the genotype pop-up
        
        #phenocell captures the table hearing/vestibular/ear cell on the first row of data
        phenocell = self.driver.find_element(By.CSS_SELECTOR, "td.middle:nth-child(9) > div:nth-child(1) > div:nth-child(1)")
        
        phenocell.click() #clicks the cell for hearing/vestibular/ear (new data could break this)
        self.driver.switch_to.window(self.driver.window_handles[1])#switches focus to the genotype popup page
        time.sleep(2)
        matching_text = "Human hearing/vestibular/ear abnormalities for TFAP2A/Tfap2a"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.page_source, 'expected pop-up box heading not displayed')
        
        #asserts that the HP term queried for has been returned
        self.assertIn("Fusion of middle ear ossicles", self.driver.page_source, "expected HP term not found")
        
                
    def test_do_term_syn_name(self):
        '''
        @status this test verifies the correct diseases are returned for this query. This is a synonym term 
        This test verifies the disease header on the grid tab and then verifies the specific DO ID is returned in the Disease Tab.
        @see: HMDC-DQ-4
        '''
        print("BEGIN test_do_term_syn_name")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys("rickets, vitamin D-resistant")#synonym for DOID:0050445; X-linked hypophosphatemic
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        #identify the grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        grid_tab.click()
        
        #cells captures every field from Human Gene heading to the last disease angled, this test only captures the diseases, which are items 25,26,27
        cells = self.driver.find_elements(By.CSS_SELECTOR, "div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        cellheadings = iterate.getTextAsList(cells)
        print(cellheadings)
        
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertIn('musculoskeletal system disease', cellheadings, "expected disease header not displayed")
        
        #identify the Disease tab, print it, and click it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print(disease_tab.text)
        disease_tab.click()
        
        disease_table = Table(self.driver.find_element(By.ID, "diseaseTable"))
        
        cells = disease_table.get_column_cells("DO ID")
        
        print(iterate.getTextAsList(cells))
        ids = iterate.getTextAsList(cells)
        
        #asserts that the expected disease is returned
        self.assertIn('DOID:0050445', ids, "expected DO ID is not returned")
        
    def test_mp_term_syn_name(self):
        '''
        @status this test verifies the correct results are returned for a query by MP synonyms.  The synonym "albino coat" is a synonym for 
        "absent coat pigmentation".  This test verifies the mouse phenotype returned on the grid tab.   The disease tab is checked to verify a 
        disease associated to a common genocluster is returned.  (HMDC-disease-11)
        @see: HMDC-PQ-4, HMDC-disease-11
        '''
        print("BEGIN test_mp_term_syn_name")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the Phenotype Name option.
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        #albino coat is a MP synonym for 'absent coat pigmentation'
        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys("albino coat") #identifies the input field and enters the MP synonym
        wait.forAngular(self.driver)
        
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks the phenotype name option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            print(option.text)
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.ID, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("Mitf")#identifies the input field and enters a specific gene symbol
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Disease tab and click it
        #disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "li.uib-tab:nth-child(3) > a:nth-child(1)")
        time.sleep(2)
        disease_tab.click()
        time.sleep(2)
        disease_table = Table(self.driver.find_element(By.ID, "diseaseTable"))
        
        cells = disease_table.get_column_cells("DO ID")
        ids = iterate.getTextAsList(cells)
        
        #asserts that the correct disease is returned
        #Disease is returned because it is annotated to the same genotype as the term "absent coat pigmentation"
        self.assertIn("DOID:4997", ids, "expected disease not returned")
         
        
        #identify the grid tab and click it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        grid_tab.click()
        
        #headingcells captures all column headings of the grid
        headingcells = self.driver.find_elements(By.CSS_SELECTOR, "div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        searchTermItems = iterate.getTextAsList(headingcells)
        print(searchTermItems) #if you want to see what it captures uncomment this
        
        #verify that the correct MP header terms for this phenotype term are included in the grid
         
        self.assertIn('integument', searchTermItems, "expected MP header not returned")
        self.assertIn('pigmentation', searchTermItems, "expected MP header not returned")
        
        #Verify that the actual term is displayed in the genotype pop-up
        
        #phenocells captures all the table data cells on the first row of data
        phenocells = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.center.cell.middle")
        
        phenocells[10].click() #clicks the cell for hearing/vestibular/ear (new data could break this)
        self.driver.switch_to.window(self.driver.window_handles[1])#switches focus to the genotype popup page
        time.sleep(2)
        matching_text = "Mouse integument abnormalities for MITF/Mitf"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.page_source, 'expected pop-up box heading not displayed')
        
        #asserts that the HP term queried for has been returned
        self.assertIn("absent coat pigmentation", self.driver.page_source, "expected MP term not found")
        

    def test_hp_term_syn_name(self):
        '''
        @status this test verifies the correct diseases are returned for this query. Should return the HP synonym term
        This test verifies the diseases on the grid tab and then on the disease tab
        @see: HMDC-PQ-9, HMDC-disease-16
        '''
        print("BEGIN test_hp_term_syn_name")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys("Gower sign")#this is a synonym for the HP term "Gowers sign"
        wait.forAngular(self.driver)
        
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks the phenotype name option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            print(option.text)
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.ID, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("ALG2")#identifies the input field and enters a specific gene symbol
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Disease tab and click on it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        time.sleep(2)
        disease_tab.click()
        
        disease_table = Table(self.driver.find_element(By.ID, "diseaseTable"))
        
        cells = disease_table.get_column_cells("DO ID")
    
        ids = iterate.getTextAsList(cells)
        self.assertIn("DOID:0110669", ids, "expected DO ID not returned in results")
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        grid_tab.click()
        #cells captures every field from Human Gene heading to the last disease angled, this test only captures the diseases, which are items 25,26,27
        cells = self.driver.find_elements(By.CSS_SELECTOR, "div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        cellheadings = iterate.getTextAsList(cells)
        
        #asserts that the correct Phenotype header is included in the results (muscle)
        self.assertIn("muscle", cellheadings, "expected phenotype header not in results")
        
        #Verify that the actual term (Gowers sign) is displayed in the genotype pop-up
        
        #phenocells captures all the table data cells on the first row of data
        phenocells = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.center.cell.middle")
        
        phenocells[3].click() #clicks the cell for muscle (new data could break this)
        self.driver.switch_to.window(self.driver.window_handles[1])#switches focus to the genotype popup page
        time.sleep(2)
        matching_text = "Human muscle abnormalities for ALG2/Alg2"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.page_source, 'expected pop-up box heading not displayed')
        
        #asserts that the HP term queried for has been returned
        self.assertIn("Gowers sign", self.driver.page_source, "expected HP term not found")
    
        
    def test_do_term_down_dag(self):
        '''
        @status this test verifies the correct diseases are returned for this query down the dag.  In this case,
        Joubert syndrome 3 is a child of the disease term Ciliopathy.
        This test verifies that the disease header on the grid tab and the diseases on the disease tab are correct.
        @see: HMDC-Grid-18, HMDC-disease-15
        '''
        print("BEGIN test_do_term_down_dag")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys("ciliopathy")#identifies the input field and enters term/ID
        wait.forAngular(self.driver)
      
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks the phenotype name option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            print(option.text)
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.ID, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("Ahi1")#identifies the input field and enters a specific gene symbol
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid Tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        grid_tab.click()
        
        #cells captures every field from Human Gene heading to the last disease angled
        cells = self.driver.find_elements(By.CSS_SELECTOR, "div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        cellheadings = iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertIn('nervous system disease', cellheadings, "expected disease header not found")
        
        #identify the Disease tab and verify the tab's text
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        time.sleep(2)
        disease_tab.click()
        disease_table = Table(self.driver.find_element(By.ID, "diseaseTable"))
        
        cells = disease_table.get_column_cells("DO ID")
        
        ids = iterate.getTextAsList(cells)
       
        #asserts that the disease that is a child of Ciliopathy is returned -- Joubert syndrome 3
        self.assertIn('DOID:0110998', ids, "expected DO ID not found")
       

    def test_mp_term_normal_models(self):
        '''
        @status this test verifies that normal model genes are returned for this query.  Query by Pax9 returns 1 row with a normal annotation (noted by N in cell)
                for the reproductive system column.
        @see: HMDC-grid-7
        '''
        print("BEGIN test_mp_term_normal_models")
        
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("Pax9")#identifies the input field and enters Pax9
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        grid_tab.click()
        
        #headingcells captures all column headings of the grid
        headingcells = self.driver.find_elements(By.CSS_SELECTOR, "div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        phenoheading = iterate.getTextAsList(headingcells)
        
        #verify that the correct MP header terms for this phenotype term are included in the grid    
        self.assertIn('reproductive system', phenoheading, "expected MP header not returned")
        
        #capture N display
        pcells = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.center.cell.middle")
        print(iterate.getTextAsList(pcells))
        
        pcellsnormal = iterate.getTextAsList(pcells)
        self.assertIn('N', pcellsnormal, "Normal flag not found")
        
        
    def test_mp_term_simple_Homozygous(self):
        '''
        @status this test verifies that genes with a simple homozygous genotype annotated to an MP term are returned for this query.  Verify genotype in the
        genotype pop-up.
        @see: HMDC-??
        '''
        print("BEGIN test_mp_term_simple_Homozygous")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys("tremors")#identifies the input field and enters term
        wait.forAngular(self.driver)
      
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks the phenotype name option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            print(option.text)
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.ID, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("Aars")#identifies the input field and enters a specific gene symbol
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        grid_tab.click()
        
        mgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.last")
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertIn("Aars", searchTermItems, "expected gene not returned")
        
        #Verify that the simple genotype is displayed in the genotype pop-up
        
        #phenocell captures all the table behavior/neurological cell on the first row of data
        phenocell = self.driver.find_element(By.CSS_SELECTOR, "td.middle:nth-child(4) > div:nth-child(1) > div:nth-child(1)")
        phenocell.click() #clicks the cell for behavior/neurological (new data could break this)
        self.driver.switch_to.window(self.driver.window_handles[1])#switches focus to the genotype popup page
        time.sleep(2)
        matching_text = "Mouse behavior/neurological abnormalities for AARS1/Aars"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.page_source, 'expected pop-up box heading not displayed')
        
        #asserts that the MP term queried for has been returned
        self.assertIn("Aars<sup>sti</sup>/Aars<sup>sti</sup>", self.driver.page_source, "expected simple genotype not found")
        
    def test_mp_term_simple_Hemizygous(self):
        '''
        @status this test verifies that genes with a simple hemizygous genotype annotated to an MP term are returned for this query. 
        Verify the hemizygous genotype in the genotype pop-up.
        @see: HMDC-??
        '''
        print("BEGIN test_mp_term_simple_Hemizygous")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys("hippocampal neuron degeneration")#identifies the input field and enters term
        wait.forAngular(self.driver)
      
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks the phenotype name option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            print(option.text)
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.ID, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("Tg(Camk2a-tTA)1Mmay")#identifies the input field and enters a specific gene symbol
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        grid_tab.click()
        
        mgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.last")
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertIn("Tg(Camk2a-tTA)1Mmay", searchTermItems, "expected gene not returned")
        
        #Verify that the simple genotype is displayed in the genotype pop-up
        
        #phenocells captures all the table data cells on the first row of data
        phenocells = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.center.cell.middle")
        
        phenocells[1].click() #clicks the cell for nervous system (new data could break this)
        self.driver.switch_to.window(self.driver.window_handles[1])#switches focus to the genotype popup page
        time.sleep(2)
        matching_text = "Mouse nervous system abnormalities for Tg(Camk2a-tTA)1Mmay"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.page_source, 'expected pop-up box heading not displayed')
        
        #asserts that the MP term queried for has been returned
        self.assertIn("Tg(Camk2a-tTA)1Mmay/0", self.driver.page_source, "expected hemizygous genotype not found")
        

    def test_mp_term_simple_Indeterminate(self):
        '''
        @status this test verifies that genes with a simple indeterminate genotype annotated to an MP term are returned for this query. 
        Should return the gene Eda to verify
        @see: HMDC-??
        '''
        print("BEGIN test_mp_term_simple_Indeterminate")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys("increased incidence of corneal inflammation")#identifies the input field and enters term
        wait.forAngular(self.driver)
      
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks the phenotype name option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            print(option.text)
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.ID, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("Eda")#identifies the input field and enters a specific gene symbol
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        grid_tab.click()
        
        mgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.last")
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertIn("Eda", searchTermItems, "expected gene not returned")
        
        #Verify that the Indeterminate genotype is displayed in the genotype pop-up
        
        #phenocells captures all the table data cells on the first row of data
        phenocells = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.center.cell.middle")
        
        phenocells[4].click() #clicks the cell for immune system (new data could break this)
        self.driver.switch_to.window(self.driver.window_handles[1])#switches focus to the genotype popup page
        time.sleep(2)
        matching_text = "Mouse immune system abnormalities for EDA/Eda"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.page_source, 'expected pop-up box heading not displayed')
        
        #asserts that the MP term queried for has been returned
        self.assertIn("Eda<sup>Ta-6J</sup>/Y", self.driver.page_source, "expected indeterminate genotype not found")

    def test_mp_term_Cond_Recomb(self):
        '''
        @status Simple Genotype: Conditional Recombinase: When there are only 2 markers in the genotype, the genotype is 
        conditional, and one marker's allele is "recombinase" (has a Driver note), return the non-recombinase marker for 
        the disease. Do NOT return the recombinase marker.
        @see: HMDC-??
        '''
        print("BEGIN test_mp_term_Cond_Recomb")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys("abnormal liver morphology")#identifies the input field and enters term
        wait.forAngular(self.driver)
      
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks the phenotype name option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            print(option.text)
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.ID, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("Abcb7, Tg(Alb-cre)21Mgn")#identifies the input field and enters a specific gene symbol
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        grid_tab.click()
        
        mgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.last")
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertIn("Abcb7", searchTermItems, "expected gene not returned")
        self.assertNotIn("Tg(Alb-cre)21Mgn", searchTermItems, "gene found that should NOT be returned")

    def test_mp_term_Cond_Recomb_1(self):
        '''
        @status Simple Genotype: Recombinase alleles present in a non-conditional simple genotype pass the roll up rules.  
                genotype = MGI:3822764 is an example of this type of genotype.  Case where we WANT to return the Cre allele
        @see: HMDC-??
        '''
        print("BEGIN test_mp_term_Cond_Recomb_1")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the phenotype name option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys("abnormal eye development")#identifies the input field and enters term
        wait.forAngular(self.driver)
        
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks the phenotype name option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            print(option.text)
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.ID, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("Hesx1")#identifies the input field and both genes of the complex genotype
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid Tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        grid_tab.click()
        
        mgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.last")
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertIn("Hesx1", searchTermItems, "expected gene not found" )
        

    def test_mp_term_Cond_Recomb_2(self):
        '''
        @status Simple Genotype: Conditional Recombinase: When there are only 2 markers in the genotype, the genotype is 
        conditional, and one marker's allele is "recombinase" (Type = Transgenic (Recombinase), return the non-recombinase marker for 
        the disease. Do NOT return the recombinase marker.
        (Genotype MGI:5304807MGI:5304807 has Kras alleles and is Conditional, but has no recombinase alleles, so it should NOT be excluded.)
        @see: HMDC-?? 
        '''
        print("BEGIN test_mp_term_Cond_Recomb_2")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the phenotype name option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys("increased lung adenoma incidence")#identifies the input field and enters term
        wait.forAngular(self.driver)
        
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks the phenotype name option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            print(option.text)
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.ID, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("Kras")#identifies the input field and both genes of the complex genotype
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        grid_tab.click()
        
        mgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.last")
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertIn("Kras", searchTermItems, "expected gene not found")
        self.assertNotIn("Tg(CMV-cre)1Cgn", searchTermItems, "recombinase transgene returned when it should not be")

    def test_mp_term_Trans_Reporter(self):
        '''
        @status Complex Genotype: Transgenic Reporter: When there are only 2 markers in the genotype, and one marker's allele is of 
        type "Transgenic (Reporter)", return the non-Transgenic (Reporter) marker for the disease. Do NOT return 
        the Transgenic (Reporter) marker. 
        @see: HMDC-??
        '''
        print("BEGIN test_mp_term_Trans_Reporter")
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the phenotype name option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys("abnormal cerebral cortex pyramidal cell morphology")#identifies the input field and enters term
        wait.forAngular(self.driver)
        
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks the phenotype name option
        for option in my_select1.find_elements(By.TAG_NAME, "option"):
            print(option.text)
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element(By.ID, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("Nrp1, Tg(Thy1-YFP)16Jrs")#identifies the input field and both genes of the complex genotype
        wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        grid_tab.click()
        wait.forAngular(self.driver)
        
        #Get the list of mouse genes returned
        mgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.last")
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertIn("Nrp1", searchTermItems, "expected gene not returned")
        self.assertNotIn("Tg(Thy1-YFP)16Jrs", searchTermItems, "this transgenic reporter is being returned, it should not be!")

    def test_mp_term_Large_Complex_Geno(self):
        '''
        @status Pick a complex/conditional genotype that should not roll up to the marker.  Verify that it is not returned for a query by an MP ID that it is annotated to.
                In this case the genotype = MGI:3831545.  (jlewis - 11/2017)
        @see: HMDC-??
        '''
        print("BEGIN test_mp_term_Large_Complex_Geno")
        #self.setUpPost("gridQuery")
        
        #self.driver = webdriver.Chrome()
        #self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        #self.driver.implicitly_wait(10)
        
        my_select = self.driver.find_element(By.XPATH, "//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break
            
        #Enter MP ID for term = increased activated T cell number
        self.driver.find_element(By.ID, "formly_3_input_input_0").clear()
        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys("MP:0001829")#identifies the input field and enters an ID
        wait.forAngular(self.driver)
        
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        grid_tab.click()
        
        mgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.last")
        mousegenes = iterate.getTextAsList(mgenes)
        
        #Verify that Brca2 is not returned -- only annotation is to a complex conditional genotype (as-of Nov 2017)
        self.assertIsNot(mousegenes, "Brca2", 'this gene is being returned, it should not!')    

    def tearDown(self):
        self.driver.close()
        tracemalloc.stop()
       
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHmdcSearchTerm))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))