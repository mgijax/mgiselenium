'''
Created on Dec 13, 2016
These tests should cover searching by different terms and verify the results
@author: jeffc
'''

import unittest
import time
import requests
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

class TestSearchTerm(unittest.TestCase):

    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)
        
    def test_index_tab_headers(self):
        '''
        @status this test verifies the headings on the Gene Homologs x Phenotypes/Diseases tab( or Index tab) are correct and in the correct order.
        @see: HMDC-
        '''
        print ("BEGIN test_index_tab_headers")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        self.driver.find_element_by_id("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Gata1")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        wait.forAngular(self.driver)
        print grid_tab.text
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (4 x 25)", "Grid tab is not visible!")
        grid_tab.click()
        human_header = self.driver.find_element_by_class_name('hgHeader')
        self.assertEqual(human_header.text, 'Human Gene', 'The human gene header is missing')
        mouse_header = self.driver.find_element_by_class_name('mgHeader')
        self.assertEqual(mouse_header.text, 'Mouse Gene', 'The mouse gene header is missing')
        #self.driver.execute_script(script)
        
    def test_do_term_name(self):
        '''
        @status this test verifies the correct diseases are returned for this query. This Disease term Heading should
        only bring back the disease mucosulfatidosis. Verified by clicking the genotype popup and confirming this is the only disease
        @see: HMDC-DQ-1
        '''
        print("BEGIN test_do_term_name")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("mucosulfatidosis")#identifies the input field and enters term/ID
        #time.sleep(5)
        self.driver.find_element_by_id("searchButton").click()
        #identify the Grid tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        wait.forAngular(self.driver)
        time.sleep(3)
        print grid_tab.text
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 18)", "Grid tab is not visible!")
        grid_tab.click()
        
        #cells captures every field from Human Gene heading to the last disease angled, this test only captures the diseases.
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each angled column of disease heading, note that there is 1 blank field between pheno headings and disease headings.
        disease1 = cells[20]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(disease1.text, 'inherited metabolic disorder')
        #firstcell captures all the table data blocks of phenotypes on the first row of data
        phenocells = self.driver.find_elements_by_css_selector("td.ngc.center.cell.middle")
        
        print iterate.getTextAsList(phenocells) #if you want to see what it captures uncomment this
        phenocells[18].click()#clicks the second phenotype data cell to open up the genotype popup page
        self.driver.switch_to_window(self.driver.window_handles[1])#switches focus to the genotype popup page
        #time.sleep(5)
        matching_text = "Human Genes and Mouse Models for inherited metabolic disorder and SUMF1/Sumf1"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.page_source, 'matching text not displayed')
        #Identify the table that contains the disease angled text
        popup_table = self.driver.find_element_by_class_name("popupTable")
        
        disease_data = popup_table.find_element_by_css_selector("span > a")
        print disease_data.text
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
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the phenotype name option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("meteorism")#identifies the input field and enters term
        wait.forAngular(self.driver)
        #self.driver.find_element_by_id("addConditionButton").click()
        print self.driver.find_element_by_xpath("//*[contains(text(), 'Add')]")
        self.driver.find_element_by_xpath("//*[contains(text(), 'Add')]").click()
        my_select1 = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_4')]")#identifies the select field and picks the phenotype name option
        for option in my_select1.find_elements_by_tag_name("option"):
            print option.text
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_id("formly_3_input_input_0").clear()
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Celsr3")#identifies the input field and enters Celsr3
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Grid tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print ("grid tab counts =", grid_tab.text)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 8)", "Grid tab is not visible!")
        grid_tab.click()
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        
        searchTermItems = iterate.getTextAsList(mgenes)
     
        self.assertEqual(searchTermItems[0], "Celsr3")
        
        print searchTermItems
        
        # Add checks for Phenotype Categories returned
        
        

    def test_hp_term_name(self):
        '''
        @status this test  Should return the HP term
        This test is verifying the correct phenotypes(for Human) are coming back on the grid tab.
        @see: HMDC-PQ-9
        '''
        print("BEGIN test_hp_term_name")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("fusion of middle ear ossicles")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print grid_tab.text
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (6 x 25)", "Grid tab is not visible!")
        grid_tab.click()
        
        #firstcell captures all the table data blocks of phenotypes on the first row of data
        phenocells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        searchTermItems = iterate.getTextAsList(phenocells)
        print searchTermItems #if you want to see what it captures uncomment this
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(searchTermItems[2], 'behavior/neurological')
        self.assertEqual(searchTermItems[5], 'craniofacial')
        self.assertEqual(searchTermItems[6], 'digestive/alimentary system')
        self.assertEqual(searchTermItems[8], 'endocrine/exocrine glands')
        self.assertEqual(searchTermItems[9], 'growth/size/body')
        self.assertEqual(searchTermItems[10], 'hearing/vestibular/ear')
        self.assertEqual(searchTermItems[12], 'homeostasis/metabolism')
        self.assertEqual(searchTermItems[13], 'immune system')
        self.assertEqual(searchTermItems[14], 'integument')
        self.assertEqual(searchTermItems[15], 'limbs/digits/tail')
        self.assertEqual(searchTermItems[17], 'muscle')
        self.assertEqual(searchTermItems[18], 'neoplasm')
        self.assertEqual(searchTermItems[19], 'nervous system')
        self.assertEqual(searchTermItems[20], 'renal/urinary system')
        self.assertEqual(searchTermItems[21], 'reproductive system')
        self.assertEqual(searchTermItems[23], 'skeleton')
        self.assertEqual(searchTermItems[24], 'vision/eye')
        
        
        
                
    def test_do_term_syn_name(self):
        '''
        @status this test verifies the correct diseases are returned for this query. This is a synonym term 
        This test verifies the diseases on the grid tab and then verifies the diseases on the disease tab.
        @see: HMDC-DQ-4
        '''
        print("BEGIN test_do_term_syn_name")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("rickets, vitamin D-resistant")#identifies the input field and enters term/ID
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print grid_tab.text
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (4 x 20)", "Grid tab is not visible!")
        grid_tab.click()
        
        #cells captures every field from Human Gene heading to the last disease angled, this test only captures the diseases, which are items 25,26,27
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of gene data
        disease1 = cells[21]
        disease2 = cells[22]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(disease1.text, 'musculoskeletal system disease')
        self.assertEqual(disease2.text, 'nervous system disease')
        #identify the Disease tab and verify the tab's text
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
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(disease1.text, 'autosomal dominant hypophosphatemic rickets')
        self.assertEqual(disease2.text, 'autosomal recessive hypophosphatemic rickets')
        self.assertEqual(disease3.text, 'otitis media')
        self.assertEqual(disease4.text, 'X-linked hypophosphatemic rickets')
        
    def test_mp_term_syn_name(self):
        '''
        @status this test verifies the correct diseases are returned for this query, should return the MP synonym term.
        This test verifies the mouse genes returned on the grid tab and then goes to the disease tab to verify the diseases. Breat Cancer due to
        common genocluster(HMDC-disease-11) and Mastitis is a DO synonym (HMDC-disease-10)
        @see: HMDC-PQ-4, HMDC-disease-11, HMDC-disease-10
        '''
        print("BEGIN test_mp_term_syn_name")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        #breast inflammation is an MP synonym of mastitis
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("breast inflammation")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (10 x 10)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, 'MFGE8')
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        
        searchTermItems = iterate.getTextAsList(mgenes)
     
        self.assertEqual(searchTermItems[0], "Mfge8")
        
        print searchTermItems
        #identify the Disease tab and verify the tab's text
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        self.assertEqual(disease_tab.text, "Diseases (2)", "Diseases tab is not visible!")
        disease_tab.click()
        
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        
        cells = disease_table.get_column_cells("Disease")
        
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        disease1 = cells[1]
        disease2 = cells[2]
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(disease1.text, 'breast cancer')
        self.assertEqual(disease2.text, 'mastitis')
        

    def test_hp_term_syn_name(self):
        '''
        @status this test verifies the correct diseases are returned for this query. Should return the HP synonym term
        This test verifies the diseases on the grid tab and then on the disease tab
        @see: HMDC-PQ-9, HMDC-disease-16
        '''
        print("BEGIN test_hp_term_syn_name")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("Gower sign")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print grid_tab.text
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (39 x 24)", "Grid tab is not visible!")
        grid_tab.click()
        #cells captures every field from Human Gene heading to the last disease angled, this test only captures the diseases, which are items 25,26,27
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of gene data
        disease1 = cells[24]
        disease2 = cells[25]
        disease3 = cells[26]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(disease1.text, 'inherited metabolic disorder')
        self.assertEqual(disease2.text, 'musculoskeletal system disease')
        self.assertEqual(disease3.text, 'nervous system disease')
        #identify the Disease tab and verify the tab's text
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        self.assertEqual(disease_tab.text, "Diseases (23)", "Diseases tab is not visible!")
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
        disease11 = cells[11]
        disease12 = cells[12]
        disease13 = cells[13]
        disease14 = cells[14]
        disease15 = cells[15]
        disease16 = cells[16]
        disease17 = cells[17]
        disease18 = cells[18]
        disease19 = cells[19]
        disease20 = cells[20]
        disease21 = cells[21]
        disease22 = cells[22]
        disease23 = cells[23]
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(disease1.text, 'AGAT deficiency')
        self.assertEqual(disease2.text, 'autosomal dominant limb-girdle muscular dystrophy type 1C')
        self.assertEqual(disease3.text, 'autosomal dominant limb-girdle muscular dystrophy type 1E')
        self.assertEqual(disease4.text, 'autosomal recessive limb-girdle muscular dystrophy type 2C')
        self.assertEqual(disease5.text, 'autosomal recessive limb-girdle muscular dystrophy type 2H')
        self.assertEqual(disease6.text, 'autosomal recessive limb-girdle muscular dystrophy type 2M')
        self.assertEqual(disease7.text, 'autosomal recessive limb-girdle muscular dystrophy type 2O')
        self.assertEqual(disease8.text, 'autosomal recessive limb-girdle muscular dystrophy type 2P')
        self.assertEqual(disease9.text, 'autosomal recessive limb-girdle muscular dystrophy type 2Q')
        self.assertEqual(disease10.text, 'centronuclear myopathy')
        self.assertEqual(disease11.text, 'congenital myasthenic syndrome 1B')
        self.assertEqual(disease12.text, 'congenital myasthenic syndrome 4C')
        self.assertEqual(disease13.text, 'congenital myasthenic syndrome 9')
        self.assertEqual(disease14.text, 'congenital myasthenic syndrome 10')
        self.assertEqual(disease15.text, 'congenital myasthenic syndrome 11')
        self.assertEqual(disease16.text, 'congenital myasthenic syndrome 12')
        self.assertEqual(disease17.text, 'congenital myasthenic syndrome 14')
        self.assertEqual(disease18.text, 'Duchenne muscular dystrophy')
        self.assertEqual(disease19.text, 'megaconial type congenital muscular dystrophy')
        self.assertEqual(disease20.text, 'mitochondrial DNA depletion syndrome 2')
        self.assertEqual(disease21.text, 'muscular dystrophy-dystroglycanopathy')
        self.assertEqual(disease22.text, 'nemaline myopathy 4')
        self.assertEqual(disease23.text, 'nemaline myopathy 7')
        
    def test_do_term_down_dag(self):
        '''
        @status this test verifies the correct diseases are returned for this query down the dag.
        This test verifies that the diseases on the grid tab and on the diseases tab are correct and sorted correctly
        @see: HMDC-Grid-18, HMDC-disease-15
        '''
        print("BEGIN test_do_term_down_dag")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("ciliopathy")#identifies the input field and enters term/ID
        wait.forAngular(self.driver)
        time.sleep(4)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print grid_tab.text
        time.sleep(3)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (82 x 32)", "Grid tab is not visible!")
        grid_tab.click()
        
        #cells captures every field from Human Gene heading to the last disease angled, this test only captures the diseases, which are items 25,26,27
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        time.sleep(1)
        print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        
        #displays each row of gene data
        disease1 = cells[27]
        disease2 = cells[28]
        disease3 = cells[29]
        disease4 = cells[30]
        
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(disease1.text, 'cardiovascular system disease')
        self.assertEqual(disease2.text, 'ciliopathy')
        self.assertEqual(disease3.text, 'nervous system disease')
        self.assertEqual(disease4.text, 'physical disorder')

        #identify the Disease tab and verify the tab's text
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        disease_tab.click()
        self.assertEqual(disease_tab.text, "Diseases (67)", "Diseases tab is not visible!")
        disease_table = Table(self.driver.find_element_by_id("diseaseTable"))
        
        cells = disease_table.get_column_cells("Disease")
        
        print iterate.getTextAsList(cells)
        #displays each row of diseases
        disease1 = cells[1]
        disease2 = cells[2]
        disease3 = cells[3]
        disease4 = cells[4]
        disease5 = cells[5]
        disease6 = cells[6]
        disease7 = cells[7]
        disease8 = cells[8]
        disease9 = cells[9]
       
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(disease1.text, 'ciliopathy')
        self.assertEqual(disease2.text, 'Joubert syndrome')
        self.assertEqual(disease3.text, 'Joubert syndrome 1')
        self.assertEqual(disease4.text, 'Joubert syndrome 2')
        self.assertEqual(disease5.text, 'Joubert syndrome 3')
        self.assertEqual(disease6.text, 'Joubert syndrome 4')
        self.assertEqual(disease7.text, 'Joubert syndrome 5')
        self.assertEqual(disease8.text, 'Joubert syndrome 6')
        self.assertEqual(disease9.text, 'Joubert syndrome 7')

    def test_mp_term_normal_models(self):
        '''
        @status this test verifies that normal model genes are returned for this query, should return the gene Pax6 and 3 transgenes
        Normal models.
        @see: HMDC-grid-7
        '''
        print("BEGIN test_mp_term_normal_models")
        
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
            
        #breast inflammation is an MP synonym of mastitis
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Pax6")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print grid_tab.text
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (4 x 26)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        #searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(hgenes.text, 'PAX6')
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        
        searchTermItems = iterate.getTextAsList(mgenes)
     
        self.assertEqual(searchTermItems[0], "Pax6")
        
    def test_mp_term_simple_Homozygous(self):
        '''
        @status this test verifies that genes with a simple homozygous genotype annotated to an MP term are returned for this query. 
        Should return the gene Aars to verify
        @see: HMDC-??
        '''
        print("BEGIN test_mp_term_simple_Homozygous")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        #breast inflammation is an MP synonym of mastitis
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("tremors")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(4)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (639 x 47)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[1], 'AARS')
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[1], "Aars")
        
    def test_mp_term_simple_Hemizygous(self):
        '''
        @status this test verifies that genes with a simple hemizygous genotype annotated to an MP term are returned for this query. 
        Should return the gene Tg(Camk2a-tTA)1Mmay to verify
        @see: HMDC-??
        '''
        print("BEGIN test_mp_term_simple_Hemizygous")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        #breast inflammation is an MP synonym of mastitis
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("hippocampal neuron degeneration")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (41 x 29)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[23], '')
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[23], "Tg(Camk2a-tTA)1Mmay")

    def test_mp_term_simple_Indeterminate(self):
        '''
        @status this test verifies that genes with a simple indeterminate genotype annotated to an MP term are returned for this query. 
        Should return the gene Eda to verify
        @see: HMDC-??
        '''
        print("BEGIN test_mp_term_simple_Indeterminate")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        #breast inflammation is an MP synonym of mastitis
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("increased incidence of corneal inflammation")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (21 x 30)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[7], 'EDA')
        print searchTermItems
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        searchTermItems = iterate.getTextAsList(mgenes)
        print searchTermItems
        self.assertEqual(searchTermItems[7], "Eda")

    def test_mp_term_Cond_Recomb(self):
        '''
        @status Simple Genotype: Conditional Recombinase: When there are only 2 markers in the genotype, the genotype is 
        conditional, and one marker's allele is "recombinase" (has a Driver note), return the non-recombinase marker for 
        the disease. Do NOT return the recombinase marker.
        @see: HMDC-??
        '''
        print("BEGIN test_mp_term_Cond_Recomb")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        #breast inflammation is an MP synonym of mastitis
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("abnormal liver morphology")#identifies the input field and enters gata1
        #wait.forAngular(self.driver)
        time.sleep(5)
        self.driver.find_element_by_id("searchButton").click()
        time.sleep(10)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(5)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1317 x 56)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[3], 'ABCB7')
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[3], "Abcb7")
        self.assertIsNot(searchTermItems, "Tg(Alb-cre)21Mgn", 'this transgene is being returned, it should not!')

    def test_mp_term_Cond_Recomb_1(self):
        '''
        @status Simple Genotype: Conditional Recombinase: When there are only 2 markers in the genotype, the genotype is 
        conditional, and one marker's allele is "recombinase" (has a Driver note), return the non-recombinase marker for 
        the disease. Do NOT return the recombinase marker.
        (Genotype MGI:5314535 has Hesx1 recombinase and Ctnnb1 alleles, but is not Conditional, so whole genotype should 
        be excluded. Hesx1 comes back in due to other alleles and genotypes.) 
        @see: HMDC-??
        '''
        print("BEGIN test_mp_term_Cond_Recomb_1")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        #breast inflammation is an MP synonym of mastitis
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("small embryonic telencephalon")#identifies the input field and enters gata1
        #wait.forAngular(self.driver)
        time.sleep(5)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(4)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (18 x 28)", "Grid tab is not visible!")
        time.sleep(2)
        grid_tab.click()
        
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[4], 'HESX1')
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[4], "Hesx1")
        self.assertIsNot(searchTermItems, "Ctnnb1", 'this gene is being returned, it should not!')

    def test_mp_term_Cond_Recomb_2(self):
        '''
        @status Simple Genotype: Conditional Recombinase: When there are only 2 markers in the genotype, the genotype is 
        conditional, and one marker's allele is "recombinase" (has a Driver note), return the non-recombinase marker for 
        the disease. Do NOT return the recombinase marker.
        (Genotype MGI:5304807MGI:5304807 has Kras alleles and is Conditional, but has no recombinase alleles, so it should NOT be excluded.)
        @see: HMDC-?? 
        '''
        print("BEGIN test_mp_term_Cond_Recomb_2")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        #breast inflammation is an MP synonym of mastitis
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("increased lung adenoma incidence")#identifies the input field and enters gata1
        #wait.forAngular(self.driver)
        time.sleep(5)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (53 x 33)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[12], 'KRAS')
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[12], "Kras")

    def test_mp_term_Trans_Reporter(self):
        '''
        @status Simple Genotype: Transgenic Reporter: When there are only 2 markers in the genotype, and one marker's allele is of 
        type "Transgenic (Reporter)", return the non-Transgenic (Reporter) marker for the disease. Do NOT return 
        the Transgenic (Reporter) marker. 
        @bug: This test has a known issue that it does not capture genes past the 26th one, so 27th item is not found!!!
        @see: HMDC-??
        '''
        print("BEGIN test_mp_term_Trans_Reporter")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        #
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("abnormal cerebral cortex pyramidal cell morphology")#identifies the input field and enters term
        #wait.forAngular(self.driver)
        time.sleep(5)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (42 x 32)", "Grid tab is not visible!")
        grid_tab.click()
        wait.forAngular(self.driver)
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        time.sleep(2)
        self.assertEqual(searchTermItems[27], 'NRP1')
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[27], "Nrp1")
        self.assertIsNot(searchTermItems, "Tg(Thy1-YFP)16Jrs", 'this transgene is being returned, it should not!')

    def test_mp_term_Large_Complex_Geno(self):
        '''
        @status Large, Complex Genotypes: A marker is not returned for a disease if it participates only in genotypes having 3 markers (3 allele "pairs") that do 
        not meet the "Conditional + Reporter" or "Tet-Induced Conditional" rules above. 
        @bug having problems collecting the genes after row 26, no answer to this issue as of yet
        @see: HMDC-??
        '''
        print("BEGIN test_mp_term_Large_Complex_Geno")
        #self.setUpPost("gridQuery")
        
        #self.driver = webdriver.Chrome()
        #self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        #self.driver.implicitly_wait(10)
        
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break
        #breast inflammation is an MP synonym of mastitis
        self.driver.find_element_by_name("formly_3_autocomplete_input_0").send_keys("dermatitis")#identifies the input field and enters gata1
        #wait.forAngular(self.driver)
        time.sleep(5)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Grid tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        #self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (278 x 43)", "Grid tab is not visible!")
        time.sleep(5)
        grid_tab.click()
        
       
        payload = {"operator":"AND","queries":[{"field":"tsDtext","condition":{"parameters":[],"input":"dermatitis"}}]}
        diseaseresult = requests.post('http://www.informatics.jax.org/diseasePortal/gridQuery', json=payload)
        #print(diseaseresult.json())
        data = diseaseresult.json()
        print data['gridDiseaseHeaders']
        
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        searchTermItems = iterate.getTextAsList(mgenes)
        #searchTermItems.location_once_scrolled_into_view
        print searchTermItems
        self.assertIsNot(searchTermItems, "Agreg", 'this gene is being returned, it should not!')
        self.assertIsNot(searchTermItems, "Egf", 'this gene is being returned, it should not!')
        self.assertIsNot(searchTermItems, "Aga", 'this gene is being returned, it should not!')
        

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