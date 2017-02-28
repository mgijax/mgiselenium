'''
Created on Nov 17, 2016
This test should check the column headers for correct display and order. It currently verifies the returned genes in correct order and the returned diseases and their order, 
tests for the other columns need to be added later.
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

class TestHmdcIndex(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)
        
    def test_index_tab_headers(self):
        '''
        @status this test verifies the headings on the Gene Homologs x Phenotypes/Diseases tab( or Index tab) are correct and in the correct order.
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
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print grid_tab.text
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (4 x 24)", "Grid tab is not visible!")
        grid_tab.click()
        human_header = self.driver.find_element_by_class_name('hgHeader')
        self.assertEqual(human_header.text, 'Human Gene', 'The human gene header is missing')
        mouse_header = self.driver.find_element_by_class_name('mgHeader')
        self.assertEqual(mouse_header.text, 'Mouse Gene', 'The mouse gene header is missing')
        
    def test_index_tab_diseases(self):
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
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print grid_tab.text
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (4 x 24)", "Grid tab is not visible!")
        grid_tab.click()
        #cells captures every field from Human Gene heading to the last disease angled, this test only captures the diseases, which are items 25,26,27
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of gene data
        disease1 = cells[25]
        disease2 = cells[26]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(disease1.text, 'chromosomal disease')
        self.assertEqual(disease2.text, 'immune system disease')
        
    def test_index_tab_genes(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse.
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
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (4 x 24)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, 'GATA1')
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Gata1")
        self.assertEqual(searchTermItems[1], "Tg(Gata1)#Mym")
        self.assertEqual(searchTermItems[2], "Tg(Gata1*V205G)1Mym")
        self.assertEqual(searchTermItems[3], "Tg(HBB-Gata1)G4Phi")#cells = mgenes.get_all()
        print searchTermItems
        
    def test_index_tab_genes_Unique_symbol(self):
        '''
        @status this test verifies the correct genes are returned for this query, The symbol used has several unusual characters.
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
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 2)", "Grid tab is not visible!")
        grid_tab.click()
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Tg(IGH@*)SALed")
        print searchTermItems
        
    def test_genotype_popup(self):
        '''
        @status this test verifies the correct genotypes are returned when clicking on a particular phenotype cell.
        In this case we are clicking the liver/biliary system box and verifying the correct Mouse Genotypes are listed in the popup
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
        #identify the Grid tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print grid_tab.text
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (4 x 24)", "Grid tab is not visible!")
        grid_tab.click()
        #firstcell captures all the table data blocks of phenotypes on the first row of data
        phenocells = self.driver.find_elements_by_css_selector("td.ngc.center.cell.middle")
        
        print iterate.getTextAsList(phenocells) #if you want to see what it captures uncomment this
        phenocells[13].click()#clicks the second phenotype data cell to open up the genotype popup page
        self.driver.switch_to_window(self.driver.window_handles[1])#switches focus to the genotype popup page
        time.sleep(1)
        matching_text = "Mouse liver/biliary system abnormalities for GATA1/Gata1"
        #asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.page_source, 'matching text not displayed')
        #Identify the table
        mouse_geno_table = self.driver.find_element_by_css_selector("p > table.popupTable ")
        data = mouse_geno_table.find_element_by_tag_name("td")
        print data.text
        #find all the TR tags in the table and iterate through them
        cells = mouse_geno_table.find_elements_by_tag_name("tr")
        print iterate.getTextAsList(cells)
        print cells
        #displays each row of mouse genotype data
        genotype1 = cells[2]
        genotype2 = cells[3]
        genotype3 = cells[4]
        genotype4 = cells[5]
        genotype5 = cells[6]
        genotype6 = cells[7]
        genotype7 = cells[8]
        genotype8 = cells[9]
        #asserts that the correct genotypes in the correct order are returned
        self.assertEqual(genotype1.text, 'Gata1tm2Sho/Gata1tm2Sho')
        self.assertEqual(genotype2.text, 'Gata1tm7Sho/Gata1tm7Sho')
        self.assertEqual(genotype3.text, 'Gata1tm8.2Sho/Gata1tm8.2Sho')
        self.assertEqual(genotype4.text, 'Gata1Plt13/Y')
        self.assertEqual(genotype5.text, 'Gata1tm1Mym/Y')
        self.assertEqual(genotype6.text, 'Gata1tm2Sho/Y')
        self.assertEqual(genotype7.text, 'Gata1tm7Sho/Y')
        self.assertEqual(genotype8.text, 'Gata1tm8.2Sho/Y')
                
    
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