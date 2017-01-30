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
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (4 x 24)", "Grid tab is not visible!")
        grid_tab.click()
        human_header = self.driver.find_element_by_class_name('hgHeader')
        self.assertEqual(human_header.text, 'Human Gene', 'The human gene header is missing')
        mouse_header = self.driver.find_element_by_class_name('mgHeader')
        self.assertEqual(mouse_header.text, 'Mouse Gene', 'The mouse gene header is missing')
        
    def test_gene_symbol(self):
        '''
        @status this test verifies the correct results are returned when searching by a gene symbol with both mouse and human phenotypes.
        
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Pax4")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print grid_tab.text
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 13)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, 'PAX4')
        mgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes.text
        self.assertEqual(mgenes.text, 'Pax4')
        #cells captures every field from Human Gene heading to the last disease angled, this test only captures the diseases, which are items 25,26,27
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of disease data
        disease1 = cells[14]
        disease2 = cells[15]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(disease1.text, 'acquired metabolic disease')
        self.assertEqual(disease2.text, 'maturity-onset diabetes of the young')

    def test_gene_symbol_rollup_error(self):
        '''
        @status this test verifies the correct results are returned when searching by a gene symbol with multiple human genes.
        Search returning 8/21/4 instead of expected 6/20/4. This includes genes (Smg6 & Grm7) that are being returned by Expressed Components that do not pass the roll-up rules.(known issue)
        '''
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
        print grid_tab.text
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (8 x 17)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
     
        self.assertEqual(searchTermItems[0], "GRM7")
        self.assertEqual(searchTermItems[1], "SMG6")
        self.assertEqual(searchTermItems[2], "SMN1, SMN2")
        #cells = hgenes.get_all()
        print searchTermItems
        
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
        self.assertEqual(searchTermItems[7], "Tg(SMN2)46Tro")
        #cells = mgenes.get_all()
        #cells captures every field from Human Gene heading to the last disease angled, this test only captures the diseases, which are items 25,26,27
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of disease data
        disease1 = cells[19]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(disease1.text, 'nervous system disease')
                
    def test_gene_symbol_nodiseases(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. The results will have phenotypes but no diseases
        '''
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
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 6)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, 'BBX')
        mgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes.text
        self.assertEqual(mgenes.text, "Bbx")#cells = mgenes.get_all()
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and makes sure no diseases
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of disease data
        pheno1 = cells[2]
        pheno2 = cells[3]
        pheno3 = cells[4]
        pheno4 = cells[5]
        pheno5 = cells[6]
        pheno6 = cells[7]
        disease1 = cells[9]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'cardiovascular system')
        self.assertEqual(pheno2.text, 'craniofacial')
        self.assertEqual(pheno3.text, 'growth/size/body')
        self.assertEqual(pheno4.text, 'hematopoietic system')
        self.assertEqual(pheno5.text, 'immune system')
        self.assertEqual(pheno6.text, 'skeleton')
        self.assertEqual(disease1.text, '')

    def test_gene_symbol_union(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. The results will have phenotypes and 1 disease
        This test is unique, 2 rows returned (via homology union). Human annotations on proper row not in Tomt row.
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Tomt")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (2 x 5)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, 'LRTOMT')
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Lrrc51")
        self.assertEqual(searchTermItems[1], "Tomt")#cells = mgenes.get_all()
        print searchTermItems
        #cells = mgenes.get_all()
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of phenotype/disease data
        pheno1 = cells[2]
        pheno2 = cells[3]
        pheno3 = cells[4]
        pheno4 = cells[5]
        disease1 = cells[7]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'behavior/neurological')
        self.assertEqual(pheno2.text, 'growth/size/body')
        self.assertEqual(pheno3.text, 'hearing/vestibular/ear')
        self.assertEqual(pheno4.text, 'nervous system')
        self.assertEqual(disease1.text, 'nervous system disease')

    def test_gene_name(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. The results will have phenotypes and diseases
        This test is a standard gene name search result.
        '''
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
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (4 x 26)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, 'PAX6')
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], 'Pax6')
        self.assertEqual(searchTermItems[1], 'Tg(CAG-EGFP,-Pax6*5a,-lacZ)1Stoy')
        self.assertEqual(searchTermItems[2], 'Tg(CAG-EGFP,-Pax6,-lacZ)1Stoy')
        self.assertEqual(searchTermItems[3], 'Tg(PAX6)77Ndha')#cells = mgenes.get_all()
        print searchTermItems
        #cells = mgenes.get_all()
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of phenotype/disease data
        pheno1 = cells[2]
        pheno2 = cells[3]
        pheno3 = cells[4]
        pheno4 = cells[5]
        disease1 = cells[27]
        disease2 = cells[28]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'behavior/neurological')
        self.assertEqual(pheno2.text, 'cardiovascular system')
        self.assertEqual(pheno3.text, 'cellular')
        self.assertEqual(pheno4.text, 'craniofacial')
        '''plus 20 more phenotypes'''
        self.assertEqual(disease1.text, 'chromosomal disease')
        self.assertEqual(disease2.text, 'nervous system disease')

    def test_gene_name_symbol1(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. The is one of 2 tests
        because the results are different if you search by gene symbols/IDs or by 
        Gene Name. This test is for searching by gene symbol or ID. Treated as a list by Gene ID/Symbol query and returns matches 
        to Kit results=4/7/2. Note: returns Gt(ROSA) in Genes tab due to a bug with EC return. (known Issue)
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("kit ligand")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (4 x 28)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, 'KIT')
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Kit")
        self.assertEqual(searchTermItems[1], "Tg(Kit*D814V)1Roer")
        self.assertEqual(searchTermItems[2], "Tg(Kit*D814V)2Roer")
        self.assertEqual(searchTermItems[3], "Tg(Kit*D814V)3Roer")
        print searchTermItems
        #cells = mgenes.get_all()
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of phenotype/disease data
        disease1 = cells[29]
        disease2 = cells[30]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(disease1.text, 'autosomal genetic disease')
        self.assertEqual(disease2.text, 'gastrointestinal system cancer')
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (7)", "Genes tab is not visible!")
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
        gene7 = cells[7]
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(gene1.text, 'Gt(ROSA)26Sor')
        self.assertEqual(gene2.text, 'KIT')
        self.assertEqual(gene3.text, 'Kit')
        self.assertEqual(gene4.text, 'Tg(Kit*D814V)1Roer')
        self.assertEqual(gene5.text, 'Tg(Kit*D814V)2Roer')
        self.assertEqual(gene6.text, 'Tg(Kit*D814V)3Roer')
        self.assertEqual(gene7.text, 'Tg(RP24-330G11-EGFP)1Mik')

    def test_gene_name_symbol2(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. The is one of 2 tests
        because the results are different if you search by gene symbols/IDs or by 
        Gene Name. This test is for searching by gene name. TGene Name query returns the KITL/Kitl row and transgenes with
        EC of Kitl (as expected)
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("kit ligand")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (2 x 22)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, 'KITLG')
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Kitl")
        self.assertEqual(searchTermItems[1], "Tg(PGK1-KITLG*220)441Daw")#cells = mgenes.get_all()
        print searchTermItems
        #cells = mgenes.get_all()
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of phenotype/disease data
        disease1 = cells[24]
        
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(disease1.text, 'nervous system disease')
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (7)", "Genes tab is not visible!")
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
        gene7 = cells[7]
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(gene1.text, 'Kitl')
        self.assertEqual(gene2.text, 'KITLG')
        self.assertEqual(gene3.text, 'Tg(CMV-IL3,CSF2,KITLG)1Eav')
        self.assertEqual(gene4.text, 'Tg(KITLG)3Ygy')
        self.assertEqual(gene5.text, 'Tg(KRT14-Kitl)1Takk')
        self.assertEqual(gene6.text, 'Tg(KRT14-Kitl*)4XTG2Bjl')
        self.assertEqual(gene7.text, 'Tg(PGK1-KITLG*220)441Daw')
        
    def test_gene_symbol_only_genes(self):
        '''
        @status this test verifies the correct genes are returned for this query, The symbol is unique because it has no grid or diseases, only genes.
        '''
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
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (0 x 0)", "Grid tab is not visible!")
        grid_tab.click()
        
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
        self.assertEqual(gene1.text, 'Paupar')
        self.assertEqual(gene2.text, 'PAUPAR')
        
    def test_gene_name_no_disease(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. The results will have phenotypes and genes, no diseases!
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("paxillin")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 6)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, 'PXN')
        mgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes.text
        self.assertEqual(mgenes.text, "Pxn")
        #cells = mgenes.get_all()
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
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'cardiovascular system')
        self.assertEqual(pheno2.text, 'cellular')
        self.assertEqual(pheno3.text, 'digestive/alimentary system')
        self.assertEqual(pheno4.text, 'embryo')
        self.assertEqual(pheno5.text, 'growth/size/body')
        self.assertEqual(pheno6.text, 'mortality/aging')

    def test_gene_name_only(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. 
        This test is a multi token synonym search, matches by gene name, but not by gene symbol.
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("dickie's small eye")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (4 x 26)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, 'PAX6')
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Pax6")
        self.assertEqual(searchTermItems[1], "Tg(CAG-EGFP,-Pax6*5a,-lacZ)1Stoy")
        self.assertEqual(searchTermItems[2], "Tg(CAG-EGFP,-Pax6,-lacZ)1Stoy")
        self.assertEqual(searchTermItems[3], "Tg(PAX6)77Ndha")#cells = mgenes.get_all()
        print searchTermItems
        #cells = mgenes.get_all()
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of phenotype/disease data
        pheno1 = cells[2]
        pheno2 = cells[3]
        pheno3 = cells[4]
        pheno4 = cells[5]
        disease1 = cells[27]
        disease2 = cells[28]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'behavior/neurological')
        self.assertEqual(pheno2.text, 'cardiovascular system')
        self.assertEqual(pheno3.text, 'cellular')
        self.assertEqual(pheno4.text, 'craniofacial')
        '''plus 20 more phenotypes'''
        self.assertEqual(disease1.text, 'chromosomal disease')
        self.assertEqual(disease2.text, 'nervous system disease')

    def test_gene_syn_only_genestab(self):
        '''
        @status this test verifies the correct genes are returned for this query, A synonym match, it has no grid or diseases, only genes.
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Solt")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (0 x 0)", "Grid tab is not visible!")
        grid_tab.click()
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
        self.assertEqual(gene1.text, 'Cenpk')
        self.assertEqual(gene2.text, 'CENPK')

    def test_gene_syn_no_diseasestab(self):
        '''
        @status this test verifies the correct genes are returned for this query, A synonym match, it has a grid and genes, no diseases.
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Prhx")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (3 x 16)", "Grid tab is not visible!")
        grid_tab.click()
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (4)", "Genes tab is not visible!")
        gene_tab.click()
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        gene1 = cells[1]
        gene2 = cells[2]
        gene3 = cells[3]
        gene4 = cells[4]
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(gene1.text, 'Hhex')
        self.assertEqual(gene2.text, 'HHEX')
        self.assertEqual(gene3.text, 'Tg(ITGAL-Hhex)2Hro')
        self.assertEqual(gene4.text, 'Tg(Lck-Hhex)1Hro')

    def test_gene_name_superscript(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by gene name when the name contains superscript.
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("p19<ARF>")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (3 x 29)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[0], "CDKN2A")
        self.assertEqual(searchTermItems[1], "COL1A1")
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Cdkn2a")
        self.assertEqual(searchTermItems[1], "Col1a1")
        self.assertEqual(searchTermItems[2], "Tg(TTR-p19Cdkn2a)2Tvd")#cells = mgenes.get_all()
        print searchTermItems
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of phenotype/disease data
        time.sleep(2)
        disease1 = cells[30]
        disease2 = cells[31]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(disease1.text, 'autosomal genetic disease')
        self.assertEqual(disease2.text, 'musculoskeletal system disease')
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (4)", "Genes tab is not visible!")
        gene_tab.click()
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        gene1 = cells[1]
        gene2 = cells[2]
        gene3 = cells[3]
        gene4 = cells[4]
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(gene1.text, 'Cdkn2a')
        self.assertEqual(gene2.text, 'CDKN2A')
        self.assertEqual(gene3.text, 'Col1a1')
        self.assertEqual(gene4.text, 'Tg(TTR-p19Cdkn2a)2Tvd')

    def test_gene_name_not_disease(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by gene name when the result has a NOT disease.
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Adam33")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 1)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, "ADAM33")
        mgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes.text
        self.assertEqual(mgenes.text, "Adam33")
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of phenotype/disease data
        pheno1 = cells[2]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'normal phenotype')
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
        self.assertEqual(gene1.text, 'Adam33')
        self.assertEqual(gene2.text, 'ADAM33')
        cells2 = gene_table.get_column_cells("References in MGI")
        print iterate.getTextAsList(cells2)
        #displays each row of References in MGI data
        ref1 = cells2[1]
        ref2 = cells2[2]
        #asserts that the References in MGI column displays a Disease Relevant link since the is a NOT disease
        self.assertEqual(ref1.text, 'All Mouse: 39\nDisease Relevant: 1')
        self.assertEqual(ref2.text, '')

    def test_gene_name_gtrosa(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  gene name when results would have the Gt(ROSA)26Sor,
        Gt(ROSA)26Sor should not display on the grid(Gt(Rosa) transgenes are fine to display on the grid) but is fine displaying in the Genes tab.
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Gt(ROSA)26Sor")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (5 x 10)", "Grid tab is not visible!")
        grid_tab.click()
        
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, "NUP210L")
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Nup210l")
        self.assertEqual(searchTermItems[1], "Tg(Gt(ROSA)26Sor-BCHE*G117H)837Loc")
        self.assertEqual(searchTermItems[2], "Tg(Gt(ROSA)26Sor-BCHE*G117H)844Loc")
        self.assertEqual(searchTermItems[3], "Tg(Gt(ROSA)26Sor-EGFP)I1Able")
        self.assertEqual(searchTermItems[4], "Tg(Gt(ROSA)26Sor-Foxe1)#Tme")#cells = mgenes.get_all()
        print searchTermItems
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (12)", "Genes tab is not visible!")
        gene_tab.click()
        gene_table = Table(self.driver.find_element_by_id("geneTable"))
        cells = gene_table.get_column_cells("Gene Symbol")
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        gene1 = cells[1]
        gene2 = cells[2]
        #asserts that the correct genes in the correct order are returned
        self.assertEqual(gene1.text, 'Gt(ROSA)26Sor')
        self.assertEqual(gene2.text, 'NUP210L')
        '''plus 10 more genes'''

    def test_gene_name_mltgene_homolog(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by gene name when grid 
        returns synonym to a mouse in a multi-gene homology class(C4A, C4B)
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Name':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Slp")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (9 x 27)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes
        searchTermItems = iterate.getTextAsList(hgenes)
        self.assertEqual(searchTermItems[0], "BLNK")
        self.assertEqual(searchTermItems[1], "C4A, C4B")
        self.assertEqual(searchTermItems[2], "LCP2")
        self.assertEqual(searchTermItems[3], "")
        self.assertEqual(searchTermItems[4], "SCIMP")
        self.assertEqual(searchTermItems[5], "STOML1")
        self.assertEqual(searchTermItems[6], "STOML2")
        self.assertEqual(searchTermItems[7], "SYTL1")
        self.assertEqual(searchTermItems[8], "VPS54")#cells = mgenes.get_all()
        print searchTermItems
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Blnk")
        self.assertEqual(searchTermItems[1], "C4a, C4b")
        self.assertEqual(searchTermItems[2], "Lcp2")
        self.assertEqual(searchTermItems[3], "rsl")
        self.assertEqual(searchTermItems[4], "Scimp")
        self.assertEqual(searchTermItems[5], "Stoml1")
        self.assertEqual(searchTermItems[6], "Stoml2")
        self.assertEqual(searchTermItems[7], "Sytl1")
        self.assertEqual(searchTermItems[8], "Vps54")#cells = mgenes.get_all()
        print searchTermItems
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
        self.assertEqual(gene1.text, 'Blnk')
        self.assertEqual(gene2.text, 'BLNK')
        self.assertEqual(gene3.text, 'C4A')
        self.assertEqual(gene4.text, 'C4a')
        self.assertEqual(gene5.text, 'C4B')
        self.assertEqual(gene6.text, 'C4b')
        '''plus 17 more genes'''

    def test_genotype_popup(self):
        '''
        @status this test verifies the correct genotypes are returned when clicking on a particular phenotype cell.
        under construction!, does not test the genotype popup yet other than the page heading
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
        #firstcell captures all the table data blocks of phenotypes on the first row of data
        phenocells = self.driver.find_elements_by_css_selector("td.ngc.center.cell.middle")
        
        print iterate.getTextAsList(phenocells) #if you want to see what it captures uncomment this
        phenocells[1].click()#clicks the second phenotype data cell to open up the genotype popup page
        self.driver.switch_to_window(self.driver.window_handles[1])#switches focus to the genotype popup page
        matching_text = "Human and Mouse cellular abnormalities for GATA1/Gata1"
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
        
        #asserts that the correct genotypes in the correct order are returned
        self.assertEqual(genotype1.text, 'Gata1Plt13/Gata1+')
        self.assertEqual(genotype2.text, 'Gata1tm2.1Sho/Gata1+')
        self.assertEqual(genotype3.text, 'Gata1tm2Sho/Gata1+')
        self.assertEqual(genotype4.text, 'Gata1tm1Mym/Y\nTg(Gata1*V205G)1Mym/0')
        self.assertEqual(genotype5.text, 'Gata1tm2.1Sho/Y')
        self.assertEqual(genotype6.text, 'Gata1tm2Sho/Y')
        self.assertEqual(genotype7.text, 'Gata1tm4Sho/Y')
    
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