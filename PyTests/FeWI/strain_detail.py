'''
Created on Apr 27, 2018
This set of tests verifies the Strains detail page results
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from util.table import Table
import sys,os.path
from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
import config
from config import TEST_URL

class TestStrainDetail(unittest.TestCase):


    def setUp(self):
    
        self.driver = webdriver.Firefox()
        self.driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        self.driver.implicitly_wait(10)

    def test_strain_det_nomen_strain_name(self):
        """
        @status: Tests that the strain name found in the Nomenclature ribbon is correct
        @note: Strain-det-nom-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("C57BL/6J")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for C57BL/6J and clicks it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        time.sleep(2)
        #switch foucus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        title = driver.find_element(By.ID, 'titleBarWrapper')#find the page's title
        print title.text#print the page title to the console screen
        #locate the strain name  in the nomenclature ribbon
        strain_name = driver.find_element(By.CSS_SELECTOR, 'section.summarySec1').find_element(By.CLASS_NAME, 'value')
        print strain_name.text#print the strain name to the console screen
        self.assertIn('C57BL/6J', strain_name.text, 'strain name is incorrect')#assert the strain name is correct

    def test_strain_det_nomen_mgi_id(self):
        """
        @status: Tests that the strain MGI ID found in the Nomenclature ribbon is correct
        @note: Strain-det-nom-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("C57BL/6J")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for C57BL/6J and clicks it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        title = driver.find_element(By.ID, 'titleBarWrapper')#find the page's title
        print title.text#print the page title to the console screen
        #locate the strain MGI ID in the nomenclature ribbon
        mgiid = driver.find_element(By.ID, 'strainPrimaryID')
        print mgiid.text#print the strain MGI ID to the console screen
        self.assertIn('MGI:3028467', mgiid.text, 'MGI ID is incorrect')#assert the MGI ID is correct        

    def test_strain_det_nomen_syn(self):
        """
        @status: Tests that the strain synonyms found in the Nomenclature ribbon are correct
        @note: Strain-det-nom-5
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("C57BL/6J")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for C57BL/6J and clicks it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        title = driver.find_element(By.ID, 'titleBarWrapper')#find the page's title
        print title.text#print the page title to the console screen
        #locate the strain Synonyms in the nomenclature ribbon
        syn = driver.find_element(By.ID, 'strainSynonyms')
        print syn.text#print the strain synonyms to the console screen
        self.assertEqual(syn.text, 'B6, B6J, Black 6, C57 Black')#assert the synonyms are correct        

    def test_strain_det_nomen_attrib(self):
        """
        @status: Tests that the strain attributes found in the Nomenclature ribbon are correct
        @note: Strain-det-nom-6
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("C57BL*")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for B6 x B10.D1-H2q/SgJ-Nox3het-2J/J and clicks it
        driver.find_element(By.LINK_TEXT, 'B6 x B10.D1-H2q/SgJ-Nox3het-2J/J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        title = driver.find_element(By.ID, 'titleBarWrapper')#find the page's title
        print title.text#print the page title to the console screen
        #locate the strain attributes in the nomenclature ribbon
        attrib = driver.find_element(By.ID, 'strainAttributes')
        print attrib.text#print the strain synonyms to the console screen
        self.assertEqual(attrib.text, 'coisogenic, congenic, major histocompatibility congenic, mutant stock, spontaneous mutation')#assert the synonyms are correct    

    def test_strain_det_nomen_approveNo(self):
        """
        @status: Tests that when a strain is set to standard=no it displays (interim) after the strain in the nomenclature ribbon   
        @note: Strain-det-nom-3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("101-A<y>")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locate the link for 101-A<y> and click it
        driver.find_element(By.PARTIAL_LINK_TEXT, '101-A').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #locates the earliest reference link and clicks it
        pend = driver.find_element(By.ID, 'strainIsStandard')
        self.assertEqual(pend.text, '(interim)') 
        
        
    def test_strain_det_nomen_approveYes(self):
        """
        @status: Tests that when a strain is set to standard=yes it does not display (interim) after the strain in the nomenclature ribbon   
        @note: Strain-det-nom-4
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("101/HY")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locate the link for C57BL/6J and click it
        driver.find_element(By.LINK_TEXT, '101/HY').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #verify (pending review) is not displayed on the page
        assert '<span id="strainIsStandard">(interim)</span>' not in driver.page_source        

    def test_strain_mpd_link(self):
        """
        @status: Tests that when a strain is associated to MPD it has a link in the nomenclature ribbon   
        @note: Strain-det-nom-7
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("A/J")
        strainsearchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #locate the link for A/J and click it
        driver.find_element(By.LINK_TEXT, 'A/J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #Click the MPD link
        driver.find_element(By.LINK_TEXT, 'View Phenomic Data').click()
        time.sleep(2)
        #switch focus to the new tab for the mpd page
        driver.switch_to_window(self.driver.window_handles[-1])
        #Identify the page title
        title = driver.find_element(By.CLASS_NAME, 'pagetitle')
        print title.text
        #verify the Page Title is correct
        self.assertEqual(title.text, 'Mouse strain: A/J', 'page title is not correct!')      

    def test_strain_mgv_link_seq_Strain(self):
        """
        @status: Tests that an MGV link exists for sequenced strain in the nomenclature ribbon   
        @note: Strain-det-nom-8
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("A/J")
        strainsearchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #locate the link for A/J and click it
        driver.find_element(By.LINK_TEXT, 'A/J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #Click the MGV link
        driver.find_element(By.LINK_TEXT, 'View Genome').click()
        time.sleep(2)
        #switch focus to the new tab for the mpd page
        driver.switch_to_window(self.driver.window_handles[-1])
        #Identify the page title
        title = driver.find_element(By.CLASS_NAME, 'title')
        print title.text
        #verify the Page Title is correct
        self.assertEqual(title.text, 'A/J', 'page title is not correct!')   

    def test_strain_mgv_link_canon_gene(self):
        """
        @status: Tests that an MGV link exists for the canonical gene strain in the nomenclature ribbon   
        @note: Strain-det-nom-9
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("C57BL/6J")
        strainsearchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #locate the link for C57BL/6J and click it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #Click the MGV link
        driver.find_element(By.LINK_TEXT, 'View Genome').click()
        time.sleep(2)
        #switch focus to the new tab for the mpd page
        driver.switch_to_window(self.driver.window_handles[-1])
        #Identify the page title
        title = driver.find_element(By.CLASS_NAME, 'title')
        print title.text
        #verify the Page Title is correct
        self.assertEqual(title.text, 'C57BL/6J', 'page title is not correct!')   

    def test_strain_alt_ids(self):
        """
        @status: Tests that Alternate IDs are displayed in the Nomenclature ribbon and are correct
        @note: Strain-det-nom-10
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("CBA/StMs")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for CBA/StMs and clicks it
        driver.find_element(By.LINK_TEXT, 'CBA/StMs').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        alt_ids = driver.find_element(By.ID, 'otherIDs')#find the alternate IDs
        print alt_ids.text#print the alt IDs to the console screen
        self.assertEqual(alt_ids.text, 'RBRC00636, NIG:143')#assert the alt IDs are correct    
        
    def test_strain_det_mut_multi_assoc(self):
        """
        @status: Tests that the results are correct and ordered correctly for associated mutations and markers when you have multiple mutations/genes
        @note: Strain-det-mut-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("C57BL/6J")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for this strain and clicks it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])        
        mutation_table = self.driver.find_element(By.ID, 'mutationSummaryTable')
        table = Table(mutation_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print iterate.getTextAsList(header_cells)        
        # print all items found in the Mutation Carried column
        cells = table.get_column_cells("Mutation Carried")
        mut_cells = iterate.getTextAsList(cells)
        print mut_cells
        #verifies that the right mutations appear and in the correct order
        self.assertEquals(mut_cells, ['Mutation Carried', 'Ahrb-1', 'Cdh23ahl', 'Fbrwt1C57BL/6J', 'Fbrwt2C57BL/6J', 'Gluchos1C57BL/6J', 'Gluchos2C57BL/6J', 'Gluchos3C57BL/6J', 'Micrln', 'n-TRtct5m1J', 'Nlrp12C57BL/6J', 'NntC57BL/6J', 'P2rx7P451L'])
        #print all items found in the Gene column
        cells1 = table.get_column_cells("Gene")
        gene_cells = iterate.getTextAsList(cells1)
        print gene_cells
        #verifies that the right genes appear and in the correct order
        self.assertEquals(gene_cells, ['Gene', 'Ahr', 'Cdh23', 'Fbrwt1', 'Fbrwt2', 'Gluchos1', 'Gluchos2', 'Gluchos3', 'Micrl', 'n-TRtct5', 'Nlrp12', 'Nnt', 'P2rx7'])
        
    def test_strain_det_mut_single_assoc(self):
        """
        @status: Tests that the results are correct when only one associated mutation and marker
        @note: Strain-det-mut-2 NOTE: this detail page has no QTL Mapped table
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("129S6/SvEvTac-Foxc1<tm1Blh>")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for this strain and clicks it
        driver.find_element(By.PARTIAL_LINK_TEXT, '129S6/SvEvTac-Foxc1').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])        
        mutation_table = self.driver.find_element(By.ID, 'mutationSummaryTable')
        table = Table(mutation_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print iterate.getTextAsList(header_cells)        
        # print all items found in the Mutation Carried column
        cells = table.get_column_cells("Mutation Carried")
        mut_cells = iterate.getTextAsList(cells)
        print mut_cells
        #verifies that the right mutations appear and in the correct order
        self.assertEquals(mut_cells, ['Mutation Carried', 'Foxc1tm1Blh'])
        #print all items found in the Gene column
        cells1 = table.get_column_cells("Gene")
        gene_cells = iterate.getTextAsList(cells1)
        print gene_cells
        #verifies that the right genes appear and in the correct order
        self.assertEquals(gene_cells, ['Gene', 'Foxc1'])
                     
    def test_strain_det_no_mut(self):
        """
        @status: Tests that the results are correct when no associated mutation and only one marker
        @note: Strain-det-mut-4 NOTE: this detail page has no QTL Mapped table
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("AEJ/GnRk-Rb(11.14)1Dn/J")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for this strain and clicks it
        driver.find_element(By.LINK_TEXT, 'AEJ/GnRk-Rb(11.14)1Dn/J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])        
        mutation_table = self.driver.find_element(By.ID, 'mutationSummaryTable')
        table = Table(mutation_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print iterate.getTextAsList(header_cells)        
        # print all items found in the Mutation Carried column
        cells = table.get_column_cells("Mutation Carried")
        mut_cells = iterate.getTextAsList(cells)
        print mut_cells
        #verifies that the right mutations appear and in the correct order
        self.assertEquals(mut_cells, ['Mutation Carried', ''])
        #print all items found in the Gene column
        cells1 = table.get_column_cells("Gene")
        gene_cells = iterate.getTextAsList(cells1)
        print gene_cells
        #verifies that the right genes appear and in the correct order
        self.assertEquals(gene_cells, ['Gene', 'Rb(11.14)1Dn'])
                     
    def test_strain_det_mut_tg(self):
        """
        @status: Tests that the results are correct when have associated mutation, marker, and Transgene
        @note: Strain-det-mut-5 NOTE: this detail page has no QTL Mapped table
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("129.Cg-Ddc<tm1.1Rhrs> Tg(Ggt1-cre)M3Egn")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for this strain and clicks it
        driver.find_element(By.LINK_TEXT, '129.Cg-Ddctm1.1Rhrs Tg(Ggt1-cre)M3Egn').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])        
        mutation_table = self.driver.find_element(By.ID, 'mutationSummaryTable')
        table = Table(mutation_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print iterate.getTextAsList(header_cells)        
        # print all items found in the Mutation Carried column
        cells = table.get_column_cells("Mutation Carried")
        mut_cells = iterate.getTextAsList(cells)
        print mut_cells
        #verifies that the right mutations appear and in the correct order
        self.assertEquals(mut_cells, ['Mutation Carried', 'Ddctm1.1Rhrs', 'Tg(Ggt1-cre)M3Egn'])
        #print all items found in the Gene column
        cells1 = table.get_column_cells("Gene")
        gene_cells = iterate.getTextAsList(cells1)
        print gene_cells
        #verifies that the right genes appear and in the correct order
        self.assertEquals(gene_cells, ['Gene', 'Ddc', 'Tg(Ggt1-cre)M3Egn'])

    def test_strain_det_mut_assocnum(self):
        """
        @status: Tests that the number count and text is correct just above the Mutations table 
        @note: Strain-det-mut-6 test will probably need rewrite once IDs added to scrumdev
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("C57BL/6J")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for this strain and clicks it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1]) 
        #locate the count and text above the mutations table       
        mut_count = self.driver.find_element(By.CLASS_NAME, 'indented')
        self.assertEqual(mut_count.text, '12 associated mutations and markers', 'associated mutations count/text is wrong')
        
    def test_strain_det_mut_showall(self):
        """
        @status: Tests that the show all/showless buttons work correctly in the Associated Mutatations,Markers, and QTL ribbon
        @note: Strain-det-mut-7/8 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:4838014")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for this strain and clicks it
        driver.find_element(By.PARTIAL_LINK_TEXT, 'STOCK').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1]) 
        #locate the Show All button in the Associated Mutations, Markers, and QTL ribbon      
        show_all = self.driver.find_element(By.ID, 'mutationButton')
        print show_all.text
        self.assertEqual(show_all.text, 'Show All', 'The Show All button has a problem!') 
        #locate the Show All button in the Associated Mutations, Markers, and QTL ribbon and click it      
        show_all.click()
        print show_all.text
        self.assertEqual(show_all.text, 'Show Less', 'The Show Less button has a problem!')         

    def test_strain_det_mut_noshowall(self):
        """
        @status: Tests that the when less than 4 results the show all/show less buttons does not display in the Associated Mutatations, Markers, and QTL ribbon
        @note: Strain-det-mut-9 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:5437707")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for this strain and clicks it
        driver.find_element(By.LINK_TEXT, 'FRCH.Cg-Tenm4l7Rn3-2R').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1]) 
        #assert the Show All button in the Associated Mutations, Markers, and QTL ribbon is not displayed      
        assert '<span id="mutationButton" class="searchToolButton indented">Show All</span>' not in driver.page_source
    
                     
    def test_strain_det_qtl_sort(self):
        """
        @status: Tests that the results are correct when have associated QTL and Marker in the mutations, Marker, and QTL ribbon, verifies sorting as well
        @note: Strain-det-qtl-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("SL/KhStmRbrc")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for this strain and clicks it
        driver.find_element(By.LINK_TEXT, 'SL/KhStmRbrc').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])        
        mutation_table = self.driver.find_element(By.ID, 'qtlSummaryTable')
        table = Table(mutation_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print iterate.getTextAsList(header_cells)        
        # print all items found in the Allele column of the QTL Table
        cells = table.get_column_cells("Allele")
        allele_cells = iterate.getTextAsList(cells)
        print allele_cells
        #verifies that the right alleles appear and in the correct order
        self.assertEquals(allele_cells, ['Allele', 'Bomb1SL/Kh', 'Esl1SL/Kh', 'Foc1SL/Kh','llaSL/Kh', 'Lyr2SL/Kh', 'Msmr1SL/Kh', 'Msmr2SL/Kh', 'Tlsm1SL/Kh'  ])
        #print all items found in the Gene column of the QTL table
        cells1 = table.get_column_cells("Gene")
        gene_cells = iterate.getTextAsList(cells1)
        print gene_cells
        #verifies that the right genes appear and in the correct order
        self.assertEquals(gene_cells, ['Gene', 'Bomb1', 'Esl1', 'Foc1', 'lla', 'Lyr2', 'Msmr1', 'Msmr2', 'Tlsm1'])
                     
    def test_strain_det_qtl_nomut_ribbon(self):
        """
        @status: Tests that the results are correct when have associated QTL and Marker in the mutatations, markers, and QTL ribbon even when no Associated Mutatations ribbon
        @note: Strain-det-qtl-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("Boulder heterogeneous stock")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for this strain and clicks it
        driver.find_element(By.LINK_TEXT, 'Boulder heterogeneous stock').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])        
        mutation_table = self.driver.find_element(By.ID, 'qtlSummaryTable')
        table = Table(mutation_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print iterate.getTextAsList(header_cells)        
        # print all items found in the Allele column of the QTL table
        cells = table.get_column_cells("Allele")
        allele_cells = iterate.getTextAsList(cells)
        print allele_cells
        #verifies that the right alleles appear and in the correct order
        self.assertEquals(allele_cells, ['Allele', 'CfcdBoulder', 'CfcdNorthport', 'OpfaBoulder','OpfaNorthport' ])
        #print all items found in the Gene column of the QTL table
        cells1 = table.get_column_cells("Gene")
        gene_cells = iterate.getTextAsList(cells1)
        print gene_cells
        #verifies that the right genes appear and in the correct order
        self.assertEquals(gene_cells, ['Gene', 'Cfcd', 'Cfcd', 'Opfa', 'Opfa'])  

    def test_strain_det_qtl_assocnum(self):
        """
        @status: Tests that the number count and text is correct just above the QTL table in the mutations, markers, and QTL ribbon
        @note: Strain-det-qtl-3 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:3028467")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for this strain and clicks it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1]) 
        #locate the count and text above the qtl table       
        qtl_count = self.driver.find_elements(By.CLASS_NAME, 'indented')
        print qtl_count[2].text
        self.assertEqual(qtl_count[2].text, '2587 associated QTL', 'associated QTL count/text is wrong')
        
    def test_strain_det_qtl_showall(self):
        """
        @status: Tests that the show all/show less buttons work correctly in the QTL Mapped with this Strain ribbon
        @note: Strain-det-mut-4/5 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:5749398")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for this strain and clicks it
        driver.find_element(By.LINK_TEXT, 'CC011/Unc').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1]) 
        #locate the Show All button in the QTL Mapped with this Strain ribbon      
        show_all = self.driver.find_element(By.ID, 'qtlButton')
        print show_all.text
        self.assertEqual(show_all.text, 'Show All', 'The Show All button has a problem!') 
        #locate the Show All button in the QTL Mapped with this Strain ribbon and click it      
        show_all.click()
        print show_all.text
        self.assertEqual(show_all.text, 'Show Less', 'The Show Less button has a problem!')         

    def test_strain_det_qtl_noshowall(self):
        """
        @status: Tests that the when less than 4 results the show all/show less buttons do not display in the QTL Mapped with this Strain ribbon
        @note: Strain-det-qtl-6 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:2164311")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for this strain and clicks it
        driver.find_element(By.LINK_TEXT, 'NZO/Hl').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1]) 
        #assert the Show All button in the QTL Mapped with this Strain ribbon is not displayed      
        assert '<span id="qtlButton" class="searchToolButton indented">Show All</span>' not in driver.page_source
    
    def test_strain_imsr_jax_link(self):
        """
        @status: Tests that an IMSR link exists to the correct IMSR page in the IMSR ribbon   
        @note: Strain-det-imsr-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("C57BL/6J")
        strainsearchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #locate the link for C57BL/6J and click it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #Click the IMSR link
        driver.find_element(By.LINK_TEXT, 'JAX:000664').click()
        time.sleep(2)
        #switch focus to the new tab for the IMSR page
        driver.switch_to_window(self.driver.window_handles[-1])
        #Identify the strain name
        name = driver.find_element(By.LINK_TEXT, 'C57BL/6J')
        print name.text
        #verify the strain name is correct
        self.assertEqual(name.text, 'C57BL/6J', 'strain is not correct!')   

    def test_strain_humdis_disease_link(self):
        """
        @status: Tests that the Disease link is correct and the link goes to the correct page from Associated Diseases ribbon
        @note: Strain-det-disease-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:3028467")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locate the link for C57BL/6J and click it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #locates the human disease link and clicks it
        driver.find_element(By.LINK_TEXT, 'X-linked hypophosphatemic rickets').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #verify the Disease name and DOID are correct for this page
        disname = driver.find_element(By.ID, 'diseaseNameID')
        print disname.text
        self.assertEquals(disname.text, 'X-linked hypophosphatemic rickets (DOID:0050445)')       

    def test_strain_humdis_model_link(self):
        """
        @status: Tests that the Model link is correct and the link goes to the correct page from Associated Diseases ribbon
        @note: Strain-det-disease-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:2159747")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locate the link for C57BL/6J and click it
        driver.find_element(By.LINK_TEXT, 'A/J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #locates the model 1 link and clicks it
        driver.find_element(By.LINK_TEXT, 'model 1').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #verify the Disease name and DOID are correct for this page
        strain_link = self.driver.find_element(By.LINK_TEXT, 'A/J')
        print strain_link.text
        self.assertEquals(strain_link.text, 'A/J')     

    def test_strain_humdis_multi_disease(self):
        """
        @status: Tests that the page can display more than 1 disease in the Associated Diseases ribbon
        @note: Strain-det-disease-3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:5509376")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locate the link for C57BL/6J and click it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J-Gdf5Bp-5J/GrsrJ').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #locates the Human Disease table
        time.sleep(2)
        disease_table = self.driver.find_element(By.ID, 'diseaseSummaryTable')
        table = Table(disease_table)
        #Iterate and print the search results headers
        dis_cells = table.get_column_cells("Human Diseases")
        print iterate.getTextAsList(dis_cells)
        #verify the Disease names
        self.assertEqual(dis_cells[1].text, 'acromesomelic dysplasia, Grebe type')
        self.assertEqual(dis_cells[2].text, 'acromesomelic dysplasia, Hunter-Thompson type')
        self.assertEqual(dis_cells[3].text, 'brachydactyly type A1C')
        self.assertEqual(dis_cells[4].text, 'brachydactyly type A2')
        self.assertEqual(dis_cells[5].text, 'brachydactyly type C')
        self.assertEqual(dis_cells[6].text, 'fibular hypoplasia and complex brachydactyly')
        self.assertEqual(dis_cells[7].text, 'multiple synostoses syndrome')
        
    def test_strain_humdis_multi_models(self):
        """
        @status: Tests that the page can display more than 1 model in the Associated Diseases ribbon
        @note: Strain-det-disease-4
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:3028467")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locate the link for C57BL/6J and click it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #locates the Human Disease table
        time.sleep(2)
        disease_table = self.driver.find_element(By.ID, 'diseaseSummaryTable')
        table = Table(disease_table)
        #Iterate and print the header headers
        head_cells = table.get_header_cells()
        print iterate.getTextAsList(head_cells)
        #verify the Model headers text
        self.assertEqual(head_cells[1].text, 'model 1')
        self.assertEqual(head_cells[2].text, 'model 2')
            
    def test_strain_humdis_disease_not(self):
        """
        @status: Tests that the page can display NOTs as well as  diseases in the Associated Diseases ribbon
        @note: Strain-det-disease-5 This test is not fully functional until I can figure out how to capture NOT image in the disease table!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:2160951")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locate the link for C57BL/6J and click it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J-Pax3Sp-d').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #locates the Human Disease table
        time.sleep(2)
        disease_table = self.driver.find_element(By.ID, 'diseaseSummaryTable')
        table = Table(disease_table)
        #Iterate the second row of the disease table
        all_cells = table.get_rows()
        print iterate.getTextAsList(all_cells)
        #verify the Model headers text
        #self.assertEqual(head_cells[1].text, 'model 1')
        #self.assertEqual(head_cells[2].text, 'model 2')        
        
    def test_strain_humdis_assoc_diseases(self):
        """
        @status: Tests that text number of associated diseases above the disease table matches the table's results in the Associated Diseases ribbon
        @note: Strain-det-disease-6
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:5509376")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locate the link for C57BL/6J and click it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J-Gdf5Bp-5J/GrsrJ').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #locates the text above the tables on the page(there are 3)
        result_text = driver.find_elements(By.CLASS_NAME, 'indented')
        indented_text = iterate.getTextAsList(result_text)
        print indented_text
        #verify the text matches the number of diseases returned(the 3rd instance)
        self.assertEquals(indented_text[3], '7 associated diseases')          
        
    def test_strain_ref_early_link(self):
        """
        @status: Tests that the earlist reference is the correct one and the link goes to the correct page from Reference ribbon
        @note: Strain-det-ref-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("C57BL/6J")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locate the link for C57BL/6J and click it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #locates the earliest reference link and clicks it
        driver.find_element(By.LINK_TEXT, 'J:84245').click()
        #time.sleep(2)
        #verify the J number J:6835 exists on this page
        assert "J:84245" in self.driver.page_source        
        
    def test_strain_ref_allref_link(self):
        """
        @status: Tests that the All reference link is correct and the link goes to the correct page from Reference ribbon
        @note: Strain-det-ref-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("C57BL/6J")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locate the link for C57BL/6J and click it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #locates the earliest reference link and clicks it
        driver.find_element(By.ID, 'allRefs').click()
        time.sleep(2)
        #verify the MGI number is correct for this page
        mginum = driver.find_element_by_css_selector("#templateBodyInsert > table.summaryHeader > tbody > tr > td.summaryHeaderData1 > span")
        print mginum.text
        self.assertEquals(mginum.text, 'MGI:3028467')       


        
    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestStrainDetail))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'TestStrainDetail.testName']
    unittest.main()         