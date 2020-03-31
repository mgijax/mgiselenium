'''
Created on Nov 17, 2016
This test should check the column headers for correct display and order. It currently verifies the returned genes 
in correct order and the returned diseases and their order, 
Updated: July 2017 (jlewis) - updates to make tests more tolerant to changes in annotations.  e.g. removing counts
@author: jeffc
'''
import unittest
import time
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

class TestHmdcIndex(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/diseasePortal")
        self.driver.implicitly_wait(10)
        
    def test_index_tab_headers(self):
        '''
        @status this test verifies the headings on the Gene Homologs x Phenotypes/Diseases tab( or Index tab) are correct and 
                in the correct order.
        @see: HMDC-grid-# (tab heading, gene column headings)
        '''
        print ("BEGIN test_index_tab_headers")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Gata1")#indentifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        time.sleep(2)
        self.assertIn("Gene Homologs x Phenotypes/Diseases (", grid_tab.text)
        grid_tab.click()
        human_header = self.driver.find_element_by_class_name('hgHeader')
        self.assertEqual(human_header.text, 'Human Gene', 'The human gene header is missing')
        mouse_header = self.driver.find_element_by_class_name('mgHeader')
        self.assertEqual(mouse_header.text, 'Mouse Gene', 'The mouse gene header is missing')
        
    def test_index_tab_diseases(self):
        '''
        @status This test verifies that human/mouse; human only; mouse only disease associations exist as expected by checking the Title of the pop-up
        @see: HMDC-grid-2 (Return row with both mouse/human annoations); HMDC-popup-17 (1 row per genocluster in disease pop-up); 
        '''
        print ("BEGIN test_index_tab_diseases")
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
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print(grid_tab.text)
        grid_tab.click()
        
        #captures all the table data blocks of phenotypes and diseases on the first row of data
        phenoDiseaseCells = self.driver.find_elements_by_css_selector("td.ngc.center.cell.middle")
        parentWindowID = self.driver.current_window_handle
        
        #click on disease cell with human and mouse annotations; verify pop-up title
        phenoDiseaseCells[24].click() #clicks the first phenotype data cell to open up the genotype popup page
        self.driver.switch_to_window(self.driver.window_handles[1])#switches focus to the genotype popup page
        time.sleep(1)
        matching_text = "Human Genes and Mouse Models for hematopoietic system disease and GATA1/Gata1"
        #asserts the heading text is correct in page source
        print(self.driver.title)
        self.assertIn(matching_text, self.driver.title, 'matching mouse/human text not displayed')
        self.driver.close()
        self.driver.switch_to_window(parentWindowID)
        
        #click on disease cell with only human annotations; verify pop-up title
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print(grid_tab.text)
        
        grid_tab.click()
        phenoDiseaseCells[23].click() #clicks the first phenotype data cell to open up the craniofacial phenotype popup page
        self.driver.switch_to_window(self.driver.window_handles[1])#switches focus to the Phenotype popup page
        time.sleep(2)
        matching_text = "Human Genes for chromosomal disease and GATA1/Gata1"
        #asserts the heading text is correct in page source
        print(self.driver.title)
        self.assertIn(matching_text, self.driver.title, 'matching human only text not displayed')
        self.driver.close()
        self.driver.switch_to_window(parentWindowID)
        
        #click on disease cell with only mouse annotations; verify pop-up title
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print(grid_tab.text)
        
        grid_tab.click()
        phenoDiseaseCells[25].click() #clicks the first phenotype data cell to open up the craniofacial phenotype popup page
        self.driver.switch_to_window(self.driver.window_handles[1])#switches focus to the Phenotype popup page
        time.sleep(2)
        matching_text = "Mouse Models for immune system disease and GATA1/Gata1"
        #asserts the heading text is correct in page source
        print(self.driver.title)
        self.assertIn(matching_text, self.driver.title, 'matching mouse only text not displayed')
        
        #Identify the table
        mouse_geno_table = self.driver.find_element_by_class_name("popupTable")
        data = mouse_geno_table.find_element_by_tag_name("td")
        print(data.text)
        #find all the TR tags in the table and iterate through them
        cells = mouse_geno_table.find_elements_by_tag_name("tr")
        print(iterate.getTextAsList(cells))
        
        #move mouse genotype data
        mouseGenotypeRows = iterate.getTextAsList(cells)
        #asserts that one of the genoclusters with annotations to this Phenotype System is returned.
        self.assertIn('Gata1tm2Sho/Gata1tm2Sho', mouseGenotypeRows)
        print("Gata1<tm2Sho> genocluster found in disease pop-up")
        
       
        
    def test_index_tab_genes(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse.  This includes 3 transgenes 
                that are returned due to Expressed Component.  In these cases the transgene has 1 expresses component = mouse gene Gata1.
                
        @see: HMDC-grid-2 (return row with both human and mouse genes); 
              HMDC-GQ-1, 3, 9 (query that matches mouse symbol, human symbol, expressed component that passes roll-up)
              HMDC-grid-27 (return row with transgene w/ expresses component and rolled up genoclusters)
        '''
        print ("BEGIN test_index_tab_genes")
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
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print(grid_tab.text)
        grid_tab.click()
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print(hgenes.text)
        self.assertEqual(hgenes.text, 'GATA1') #returned due to gene nomenclature match
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertIn("Gata1", searchTermItems) #returned due to gene nomenclature match
        self.assertIn("Tg(Gata1)#Mym", searchTermItems) #returned due to Expressed Component w/ rolled up genocluster
        self.assertIn("Tg(Gata1*V205G)1Mym", searchTermItems) #returned due to Expressed Component w/ rolled up genocluster
        self.assertIn("Tg(HBB-Gata1)G4Phi", searchTermItems) #returned due to Expressed Component w/ rolled up genocluster
        print(searchTermItems)
        
    def test_index_tab_genes_Unique_symbol(self):
        '''
        @status this test verifies the correct genes are returned for this query, The symbol used has several unusual characters.
        @see: HMDC-GQ-2 (symbols with special characters); 
              HMDC-grid-6 (Return row with no human gene)
        '''
        print ("BEGIN test_index_tab_genes_Unique_symbol")
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
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print(grid_tab.text)
        
        grid_tab.click()
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Tg(IGH@*)SALed")
        print(searchTermItems)
        
    def test_genotype_popup(self):
        '''
        @status This test verifies that the expected annotations are present under the phenotype systems.
                This includes a system with both mouse and human; a system with only human; and a system with
                only mouse.  The check is made using the Title of the phenotype pop-up.
        @see: HMDC-grid-2; HMDC-popup-1 (display pop-up page by clicking cell); HMDC-popup-11 (return row for mouse genocluster)
        '''
        print ("BEGIN test_genotype_popup")
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Gata1")#identifies the input field and enters Gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Grid tab and print out tab text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print(grid_tab.text)
        
        grid_tab.click()
        #captures all the table data blocks of phenotypes on the first row of data
        phenocells = self.driver.find_elements_by_css_selector("td.ngc.center.cell.middle")
        parentWindowID = self.driver.current_window_handle
        
        # Grid pop-up for a Phenotype System with both Human and Mouse annotations
        phenocells[0].click() #clicks the first phenotype data cell to open up the genotype popup page
        self.driver.switch_to_window(self.driver.window_handles[1])#switches focus to the genotype popup page
        time.sleep(1)
        matching_text = "Human and Mouse cardiovascular system abnormalities for GATA1/Gata1"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.title, 'matching mouse/human text not displayed')
        self.driver.close()
        self.driver.switch_to_window(parentWindowID)
        # Grid pop-up for a Phenotype System with only Human annotations
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print(grid_tab.text)
        
        grid_tab.click()
        phenocells[2].click() #clicks the first phenotype data cell to open up the craniofacial phenotype popup page
        self.driver.switch_to_window(self.driver.window_handles[1])#switches focus to the Phenotype popup page
        time.sleep(2)
        matching_text = "Human craniofacial abnormalities for GATA1/Gata1"
        #asserts the heading text is correct in page source
        print(self.driver.title)
        self.assertIn(matching_text, self.driver.title, 'matching human only text not displayed')
        self.driver.close()
        self.driver.switch_to_window(parentWindowID)
        
        # Grid popup for a Phenotype System with only Mouse annotations
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        print(grid_tab.text)
        
        grid_tab.click()
        phenocells[13].click() #clicks the phenotype data cell to open up the Phenotype popup page
        self.driver.switch_to_window(self.driver.window_handles[1])#switches focus to the genotype popup page
        time.sleep(2)
        matching_text = "Mouse liver/biliary system abnormalities for GATA1/Gata1"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.title, 'matching mouse only text not displayed')
        
        #Identify the table
        mouse_geno_table = self.driver.find_element_by_css_selector("p > table.popupTable ")
        data = mouse_geno_table.find_element_by_tag_name("td")
        print(data.text)
        #find all the TR tags in the table and iterate through them
        cells = mouse_geno_table.find_elements_by_tag_name("tr")
        print(iterate.getTextAsList(cells))
        
        #move mouse genotype data
        mouseGenotypeRows = iterate.getTextAsList(cells)
        #asserts that one of the genoclusters with annotations to this Phenotype System is returned.
        self.assertIn('Gata1tm2Sho/Gata1tm2Sho', mouseGenotypeRows)
        print("Gata1<tm2Sho> genocluster found in phenotype pop-up")
        
                
    
    def tearDown(self):
        self.driver.close()
       
        
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='WebdriverTests'))