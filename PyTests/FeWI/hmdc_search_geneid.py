'''
Created on Jan 9, 2017

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

class TestGeneid(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)
        



    def testGeneIDMgiid(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene ID using an MGI ID
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("MGI:96677")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (4 x 28)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, "KIT")
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Kit")
        self.assertEqual(searchTermItems[1], "Tg(Kit*D814V)1Roer")
        self.assertEqual(searchTermItems[2], "Tg(Kit*D814V)2Roer")
        self.assertEqual(searchTermItems[3], "Tg(Kit*D814V)3Roer")#cells = mgenes.get_all()
        print searchTermItems
        
    def test_gene_id_entrez(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene ID using an Entrez gene ID, should only  have 1 gene(AA960008), no grid or disease
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("105763")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (0 x 0)", "Grid tab is not visible!")
        grid_tab.click()
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
        self.assertEqual(gene1.text, 'AA960008')

    def test_gene_id_ncbi_model(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene ID using an NCBI Gene Model ID
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("14460")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (4 x 25)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, "GATA1")
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Gata1")
        self.assertEqual(searchTermItems[1], "Tg(Gata1)#Mym")
        self.assertEqual(searchTermItems[2], "Tg(Gata1*V205G)1Mym")
        self.assertEqual(searchTermItems[3], "Tg(HBB-Gata1)G4Phi")#cells = mgenes.get_all()
        print searchTermItems
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (6)", "Genes tab is not visible!")
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
        self.assertEqual(gene1.text, 'Gata1')
        self.assertEqual(gene2.text, 'GATA1')
        self.assertEqual(gene3.text, 'Tg(Gata1)#Mym')
        self.assertEqual(gene4.text, 'Tg(Gata1*)#Mym')
        self.assertEqual(gene5.text, 'Tg(Gata1*V205G)1Mym')
        self.assertEqual(gene6.text, 'Tg(HBB-Gata1)G4Phi')
        
    def test_gene_id_vega_model(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene ID using a Vega Gene Model ID
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("OTTMUSG00000005850")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 6)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, "TTC19")
        mgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes.text
        self.assertEqual(mgenes.text, "Ttc19")
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of phenotype/disease data
        pheno1 = cells[2]
        pheno2 = cells[3]
        pheno3 = cells[4]
        pheno4 = cells[5]
        pheno5 = cells[6]
        disease1 = cells[8]
        #asserts that the correct diseases(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'behavior/neurological')
        self.assertEqual(pheno2.text, 'hearing/vestibular/ear')
        self.assertEqual(pheno3.text, 'muscle')
        self.assertEqual(pheno4.text, 'nervous system')
        self.assertEqual(pheno5.text, 'vision/eye')
        self.assertEqual(disease1.text, 'inherited metabolic disorder')
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
        self.assertEqual(gene1.text, 'Ttc19')
        self.assertEqual(gene2.text, 'TTC19')
        
    def test_gene_id_swiss_prot(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene ID using a swiss-prot ID
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("Q61838")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 3)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, "")
        mgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes.text
        self.assertEqual(mgenes.text, "Pzp")
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        #print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
        #displays each row of phenotype/disease data
        pheno1 = cells[2]
        pheno2 = cells[3]
        pheno3 = cells[4]
        #asserts that the correct phenotypes/diseases(at angle) display in the correct order
        self.assertEqual(pheno1.text, 'behavior/neurological')
        self.assertEqual(pheno2.text, 'cardiovascular system')
        self.assertEqual(pheno3.text, 'skeleton')
        
    def test_gene_id_gtrosa(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  gene name when results would have the Gt(ROSA)26Sor,
        Gt(ROSA)26Sor should not display on the grid(in this case  no grid at all) but, is fine displaying in the Genes tab.
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("MGI:104735")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
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
        self.assertEqual(gene1.text, 'Gt(ROSA)26Sor')
        self.assertEqual(gene2.text, 'THUMPD3-AS1')
        
    def test_gene_symbol_non_mouseall(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene symbol using a non-mouse marker nomenclature term with results for all 3 tabs
        '''
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
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (2 x 5)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, "LRTOMT")
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Lrrc51")
        self.assertEqual(searchTermItems[1], "Tomt")#cells = mgenes.get_all()
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
        '''
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
        '''
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
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (1 x 10)", "Grid tab is not visible!")
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
        '''
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
        '''
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
        self.assertEqual(pheno15.text, 'nervous system')
        self.assertEqual(pheno16.text, 'pigmentation')
        self.assertEqual(pheno17.text, 'renal/urinary system')
        self.assertEqual(pheno18.text, 'reproductive system')
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
        self.assertEqual(disease3.text, "Waardenburg's syndrome")

    def test_gene_symbol_dual_match(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene symbol using a symbol that has a human symbol match and a human synonym match (Trp53, Trp53bp1)
        '''
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
        self.assertEqual(disease_tab.text, "Diseases (13)", "Diseases tab is not visible!")
        disease_tab.click()
        
    def test_gene_symbol_human_syn(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene symbol using a symbol that is a human synonym(LFS1 is a human synonym of Trp53)
        '''
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
        self.assertEqual(disease_tab.text, "Diseases (13)", "Diseases tab is not visible!")
        disease_tab.click()

    def test_gene_ID_human_entrez(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by Gene ID for human Entrez gene(729991 is an ID for Borcs8)
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("729991")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
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
        self.assertEqual(gene1.text, 'Borcs8')
        self.assertEqual(gene2.text, 'BORCS8')

    def test_gene_ID_OMIM(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by OMIM ID(human)(191150 is associated to marker Trp53)
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("191170")#identifies the input field and enters gata1
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
        self.assertEqual(disease_tab.text, "Diseases (13)", "Diseases tab is not visible!")
        disease_tab.click()

    def test_gene_ID_hgnc(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by HGNC ID(human)(HGNC:6554 is associated to marker Lepr)
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("HGNC:6554")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
        self.assertEqual(grid_tab.text, "Gene Homologs x Phenotypes/Diseases (2 x 25)", "Grid tab is not visible!")
        grid_tab.click()
        hgenes = self.driver.find_element_by_css_selector("td.ngc.left.middle.cell.first")
        print hgenes.text
        self.assertEqual(hgenes.text, "LEPR")
        mgenes = self.driver.find_elements_by_css_selector("td.ngc.left.middle.cell.last")
        print mgenes
        searchTermItems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchTermItems[0], "Lepr")
        self.assertEqual(searchTermItems[1], "Tg(Apoe-Lepr)1Kry")
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (4)", "Genes tab is not visible!")
        gene_tab.click()
        #identify the Diseases tab and verify the tab's text
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        self.assertEqual(disease_tab.text, "Diseases (2)", "Diseases tab is not visible!")
        disease_tab.click()

    def test_gene_ID_rgd(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by RGD ID for a rat gene(RGD:2466 is associated to marker Cyp2b10 )
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break
        
        self.driver.find_element_by_name("formly_3_input_input_0").send_keys("RGD:2466")#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
        #identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        time.sleep(2)
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
        self.assertEqual(gene1.text, 'CYP2B6')
        self.assertEqual(gene2.text, 'Cyp2b10')

    def test_gene_symbol_multiples(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by multiple Gene symbols (Foxm1, Lep, Ins2). There are 2 issues with this test, first selenium seems unable to locate the last 4 diseases in the grid so
        they have been commented out. The order of genes on the genes tab has Human symbols first, should be Mouse symbol first.
        '''
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
        #print mgenes
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
        #print searchTermItems
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
        #disease5 = cells[33]Selenium is not recognizing these last 2 diseases, maybe because not displayed in browser window?
        #disease6 = cells[34]
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
        #self.assertEqual(disease5.text, 'maturity-onset diabetes of the young')
        #self.assertEqual(disease6.text, 'respiratory system disease')
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
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
        self.assertEqual(gene1.text, 'FOXM1')
        self.assertEqual(gene2.text, 'Foxm1')
        self.assertEqual(gene3.text, 'INS')
        self.assertEqual(gene4.text, 'Ins2')
        self.assertEqual(gene5.text, 'Lep')
        self.assertEqual(gene6.text, 'LEP')
        '''plus 10 more genes, all transgenes'''
        #identify the Diseases tab and verify the tab's text
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        self.assertEqual(disease_tab.text, "Diseases (9)", "Diseases tab is not visible!")
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
        #asserts that the correct diseases in the correct order are returned
        self.assertEqual(disease1.text, 'hepatocellular carcinoma')
        self.assertEqual(disease2.text, 'lung cancer')
        self.assertEqual(disease3.text, 'maturity-onset diabetes of the young')
        self.assertEqual(disease4.text, 'metabolic syndrome X')
        self.assertEqual(disease5.text, 'obesity')
        self.assertEqual(disease6.text, 'permanent neonatal diabetes mellitus')
        self.assertEqual(disease7.text, 'type 1 diabetes mellitus')
        self.assertEqual(disease8.text, 'type 1 diabetes mellitus 2')        
        self.assertEqual(disease9.text, 'type 2 diabetes mellitus')

    def test_gene_id_multiples(self):
        '''
        @status this test verifies the correct genes are returned for this query, both human and mouse. This test is for searching by  
        by multiple Gene IDs (MGI:1347487, MGI:104663, MGI:96573). There are 2 issues with this test, first selenium seems unable to locate the last 4 diseases in the grid so
        they have been commented out. The order of genes on the genes tab has Human symbols first, should be Mouse symbol first.
        '''
        my_select = self.driver.find_element_by_xpath("//select[starts-with(@id, 'field_0_')]")#identifies the select field and picks the gene symbols option
        for option in my_select.find_elements_by_tag_name("option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element_by_name("formly_3_input_input_0").send_keys('MGI:1347487, MGI:104663, MGI:96573')#identifies the input field and enters gata1
        wait.forAngular(self.driver)
        self.driver.find_element_by_id("searchButton").click()
        wait.forAngular(self.driver)
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
        #print mgenes
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
        #print searchTermItems
        #cells captures every field from Human Gene heading to the last disease angled, this test captures the phenotypes and 1 disease
        cells = self.driver.find_elements_by_css_selector("div.ngc.cell-content.ngc-custom-html.ng-binding.ng-scope")
        print iterate.getTextAsList(cells) #if you want to see what it captures uncomment this
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
        #these last 4 diseases can not be picked up by selenium, exactly why is unknown
        #disease5 = cells[33]
        #disease6 = cells[34]
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
        #self.assertEqual(disease5.text, 'maturity-onset diabetes of the young')
        #self.assertEqual(disease6.text, 'respiratory system disease')
        #identify the Genes tab and verify the tab's text
        gene_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(2) > a.nav-link.ng-binding")
        print gene_tab.text
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
        self.assertEqual(gene1.text, 'FOXM1')
        self.assertEqual(gene2.text, 'Foxm1')
        self.assertEqual(gene3.text, 'INS')
        self.assertEqual(gene4.text, 'Ins2')
        self.assertEqual(gene5.text, 'LEP')
        self.assertEqual(gene6.text, 'Lep')
        '''plus 10 more genes, all transgenes'''
        #identify the Diseases tab and verify the tab's text
        disease_tab = self.driver.find_element_by_css_selector("ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print disease_tab.text
        time.sleep(2)
        self.assertEqual(disease_tab.text, "Diseases (9)", "Diseases tab is not visible!")
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
        #asserts that the correct diseases in the correct order are returned
        self.assertEqual(disease1.text, 'hepatocellular carcinoma')
        self.assertEqual(disease2.text, 'lung cancer')
        self.assertEqual(disease3.text, 'maturity-onset diabetes of the young')
        self.assertEqual(disease4.text, 'metabolic syndrome X')
        self.assertEqual(disease5.text, 'obesity')
        self.assertEqual(disease6.text, 'permanent neonatal diabetes mellitus')
        self.assertEqual(disease7.text, 'type 1 diabetes mellitus')
        self.assertEqual(disease8.text, 'type 1 diabetes mellitus 2')
        self.assertEqual(disease9.text, 'type 2 diabetes mellitus')



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