'''
Created on Apr 27, 2018
This set of tests verifies the Strains detail page results
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        self.driver.implicitly_wait(10)

    def test_strain_det_ribbon_order(self):
        """
        @status: Tests that the ribbons are displayed in the correct order. *no example has all ribbons as of 7/20/2018
        @note: sort order is: summary, description, snps, associated mutations, phenotypes, find mice, references
        @note: Project Fevah GF-71
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("C57BL/6NHsd")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for C57BL/6NHsd and clicks it
        driver.find_element(By.LINK_TEXT, 'C57BL/6NHsd').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        summary_ribbon = driver.find_element(By.ID, 'summaryRibbonLabel')#find the Summary Ribbon's title
        print summary_ribbon.text#print the summary ribbon's title to the console screen
        self.assertEqual(summary_ribbon.text, 'Summary', 'the summary ribbon is missing!')
        description_ribbon = driver.find_element(By.ID, 'descriptionRibbonLabel')#find the description Ribbon's title
        print description_ribbon.text#print the description ribbon's title to the console screen
        self.assertEqual(description_ribbon.text, 'Description', 'the description ribbon is missing!')
        mutation_ribbon = driver.find_element(By.ID, 'mutationRibbonLabel')#find the Mutation Ribbon's title
        print mutation_ribbon.text#print the mutation ribbon's title to the console screen
        self.assertEqual(mutation_ribbon.text, 'Associated\nMutations,\nMarkers,\nand QTL', 'the mutation ribbon is missing!')
        reference_ribbon = driver.find_element(By.ID, 'referenceRibbonLabel')#find the Reference Ribbon's title
        print reference_ribbon.text#print the reference ribbon's title to the console screen
        self.assertEqual(reference_ribbon.text, 'References', 'the reference ribbon is missing!')

    def test_strain_det_ribbon_order2(self):
        """
        @status: Tests that the ribbons are displayed in the correct order. *no example has all ribbons as of 7/20/2018
        @note: sort order is: summary, description, snps, associated mutations, phenotypes, find mice, references
        @note: Project Fevah GF-71
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
        summary_ribbon = driver.find_element(By.ID, 'summaryRibbonLabel')#find the Summary Ribbon's title
        print summary_ribbon.text#print the summary ribbon's title to the console screen
        self.assertEqual(summary_ribbon.text, 'Summary', 'the summary ribbon is missing!')
        snp_ribbon = driver.find_element(By.ID, 'snpRibbonLabel')#find the Summary Ribbon's title
        print snp_ribbon.text#print the summary ribbon's title to the console screen
        self.assertEqual(snp_ribbon.text, 'SNPs', 'the snps ribbon is missing!')
        mutation_ribbon = driver.find_element(By.ID, 'mutationRibbonLabel')#find the Mutation Ribbon's title
        print mutation_ribbon.text#print the mutation ribbon's title to the console screen
        self.assertEqual(mutation_ribbon.text, 'Associated\nMutations,\nMarkers,\nand QTL', 'the mutation ribbon is missing!')
        disease_ribbon = driver.find_element(By.ID, 'diseaseRibbonLabel')#find the Diseases Ribbon's title
        print disease_ribbon.text#print the diseases ribbon's title to the console screen
        self.assertEqual(disease_ribbon.text, 'Associated\nPhenotypes', 'the disease/phenotypes ribbon is missing!')
        imsr_ribbon = driver.find_element(By.ID, 'imsrRibbonLabel')#find the imsr Ribbon's title
        print imsr_ribbon.text#print the imsr ribbon's title to the console screen
        self.assertEqual(imsr_ribbon.text, 'Find Mice (IMSR)', 'the imsr ribbon is missing!')
        reference_ribbon = driver.find_element(By.ID, 'referenceRibbonLabel')#find the Reference Ribbon's title
        print reference_ribbon.text#print the reference ribbon's title to the console screen
        self.assertEqual(reference_ribbon.text, 'References', 'the reference ribbon is missing!')

    def test_strain_det_nomen_strain_name(self):
        """
        @status: Tests that the strain name found in the Nomenclature ribbon is correct
        @note: Strain-det-sum-1
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
        #locate the strain name  in the nomenclature ribbon
        strain_name = driver.find_element(By.ID, 'strainName')
        print strain_name.text#print the strain name to the console screen
        self.assertIn('C57BL/6J', strain_name.text, 'strain name is incorrect')#assert the strain name is correct

    def test_strain_det_nomen_mgi_id(self):
        """
        @status: Tests that the strain MGI ID found in the Nomenclature ribbon is correct
        @note: Strain-det-sum-2
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

    #def test_strain_det_nomen_approveNo(self):
        """
        @status: Tests that when a strain is set to standard=no it displays (interim) after the strain in the nomenclature ribbon   
        @note: Strain-det-sum-3 ***This test disabled because the FeWI no longer puts 'Interim' after a non standard strain!!
        """
        #driver = self.driver
        #driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        #strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        #strainsearchbox.send_keys("101-A<y>")
        #time.sleep(2)
        #find the search button and click it
        #driver.find_element(By.CLASS_NAME, 'goButton').click()
        #time.sleep(2)
        #locate the link for 101-A<y> and click it
        #driver.find_element(By.PARTIAL_LINK_TEXT, '101-A').click()
        #time.sleep(2)
        #switch focus to the new tab for strain detail page
        #driver.switch_to_window(self.driver.window_handles[-1])
        #locates the earliest reference link and clicks it
        #pend = driver.find_element(By.ID, 'strainIsStandard')
        #self.assertEqual(pend.text, '(interim)')         
    
    
    def test_strain_det_nomen_approveYes(self):
        """
        @status: Tests that when a strain is set to standard=yes it does not display (interim) after the strain in the nomenclature ribbon   
        @note: Strain-det-sum-4
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

    def test_strain_det_nomen_syn(self):
        """
        @status: Tests that the strain synonyms found in the Nomenclature ribbon are correct
        @note: Strain-det-sum-5
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
        @note: Strain-det-sum-6 !fails because the (see attribute definitions) text has not yet been removed
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
  

    def test_strain_mpd_link(self):
        """
        @status: Tests that when a strain is associated to MPD it has a link in the nomenclature ribbon   
        @note: Strain-det-sum-7
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
        driver.find_element(By.LINK_TEXT, 'Mouse Phenome Database (MPD)').click()
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
        @note: Strain-det-sum-8
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
        driver.find_element(By.LINK_TEXT, 'Multiple Genome Viewer (MGV)').click()
        time.sleep(2)
        #switch focus to the new tab for the mpd page
        driver.switch_to_window(self.driver.window_handles[-1])
        #Identify the page title
        time.sleep(3)
        title = driver.find_element(By.CLASS_NAME, 'title')
        print title.text
        #verify the Page Title is correct
        self.assertEqual(title.text, 'Genome View', 'page title is not correct!')   

    def test_strain_mgv_link_canon_gene(self):
        """
        @status: Tests that an MGV link exists for the canonical gene strain in the nomenclature ribbon   
        @note: Strain-det-sum-9
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
        driver.find_element(By.LINK_TEXT, 'Multiple Genome Viewer (MGV)').click()
        time.sleep(2)
        #switch focus to the new tab for the mpd page
        driver.switch_to_window(self.driver.window_handles[-1])
        #Identify the page title
        time.sleep(3)
        title = driver.find_element(By.ID, 'genomeView')
        print title.text
        #verify the Page Title is correct
        self.assertEqual(title.text, 'Genome View', 'page title is not correct!')   

    def test_strain_alt_ids(self):
        """
        @status: Tests that Alternate IDs are displayed in the Nomenclature ribbon and are correct
        @note: Strain-det-sum-10
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

    def test_strain_founder_strain(self):
        """
        @status: Tests that when a DO/CC Founder strain is displayed in the Nomenclature ribbon the Collection says DO/CC Founder
        @note: Strain-det-sum-12
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("WSB/EiJ")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for WSB/EiJ and clicks it
        driver.find_element(By.LINK_TEXT, 'WSB/EiJ').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        collect = driver.find_element(By.ID, 'strainCollection')#find the collection field
        print collect.text#print the collection to the console screen
        self.assertEqual(collect.text, 'DO/CC Founder')#assert the collection field is correct    

    def test_strain_strain_fam_link(self):
        """
        @status: Tests that Strain Family Member link is displayed in the Nomenclature ribbon for all Strain Family strains
        @note: Strain-det-sum-13
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        #find the strain family option in the list and select it
        Select (driver.find_element(By.NAME, 'attributes')).select_by_visible_text('strain family')
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for CBA/StMs and clicks it
        driver.find_element(By.LINK_TEXT, '129').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(2)
        fam_mem = driver.find_element(By.ID, 'relatedStrains')#find the Strain Family Member link
        print fam_mem.text#print the strain family member to the console screen
        self.assertEqual(fam_mem.text, '90')#assert the strain family member link is correct    

    def test_strain_desc_small(self):
        """
        @status: Tests the display when the strain description is only 5 characters
        @note: Strain-det-desc-1**broken 10/24/19 need a new example that has short description**
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:6143482")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for CBA/StMs and clicks it
        driver.find_element(By.PARTIAL_LINK_TEXT, 'C57BL/6NCrl-Clcnkb').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        desc_field = driver.find_element(By.ID, 'description')#find the description field
        print desc_field.text#print the description field to the console screen
        self.assertEqual(desc_field.text, 'CR1475')#assert the text of the description field is correct    

    def test_strain_desc_link(self):
        """
        @status: Tests the display when the strain description has a link in it
        @note: Strain-det-desc-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:6156919")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for CBA/StMs and clicks it
        driver.find_element(By.PARTIAL_LINK_TEXT, 'SJL/JCrHsd').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(10)
        desc_field = driver.find_element(By.ID, 'description')#find the description field
        print desc_field.text#print the description field to the console screen
        self.assertEqual(desc_field.text, 'Envigo')#assert the text of the description field is correct    

    def test_strain_desc_large(self):
        """
        @status: Tests the display when the strain description is so large it needs a scroll bar
        @note: Strain-det-desc-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:6156918")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for CBA/StMs and clicks it
        driver.find_element(By.PARTIAL_LINK_TEXT, 'SAMR1/TaHsd').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        desc_field = driver.find_element(By.ID, 'description')#find the description field
        print desc_field.text#print the description field to the console screen
        self.assertEqual(desc_field.text, 'Envigo')#assert the text of the description field is correct    

    def test_strain_snp_comp(self):
        """
        @status: Tests the SNPs for a strain display the correct comparison strains
        @note: Strain-det-snp-1,3,4
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:2159745")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for AKR/J and clicks it
        driver.find_element(By.PARTIAL_LINK_TEXT, 'AKR/J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        comp_count = driver.find_element(By.ID, 'comparisonStrainCount')#find the Comparison Strains count field
        print comp_count.text#print the description field to the console screen
        self.assertEqual(comp_count.text, '86')#asserts the Comparison Strains count is correct
        #clicks the More toggle(turnstile) to display the snps table
        self.driver.find_element(By.ID, 'snpToggle').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'snpContainer')))#waits until the snp table is displayed on the page
        snphead_table = self.driver.find_element(By.ID, 'snpTableHeader')
        table = Table(snphead_table)
        #Iterate and print to the screen all the headers(does not capture the word Chromosomes)
        row1_cells = table.get_row_cells(1)        
        print iterate.getTextAsList(row1_cells)  
        time.sleep(4)       
        #Verify the header cells are correct for the first 4 and last 3 headings
        self.assertEqual(row1_cells[0].text, 'Comparison Strain')
        self.assertEqual(row1_cells[1].text, '1')
        self.assertEqual(row1_cells[2].text, '2')
        self.assertEqual(row1_cells[3].text, '3')
        self.assertEqual(row1_cells[20].text, 'X')
        self.assertEqual(row1_cells[21].text, 'Y')
        self.assertEqual(row1_cells[22].text, 'MT')        
        #locate the SNP table and find the rows of strains     
        snp_table = self.driver.find_element(By.ID, 'snpTable')
        table = Table(snp_table)
        # print all items found in the Comparison Strain column
        cells = table.get_rows()
        strain_cells = iterate.getTextAsList(cells)
        print strain_cells
        #verifies that the right strains appear and in the correct order
        self.assertEquals(strain_cells, [u'129/Sv', u'129S1/SvImJ', u'129S4/SvJae', u'129S6/SvEvTac', u'129X1/Sv', u'129X1/SvJ', u'A', u'A/He', u'A/HeJ', u'A/J', u'AKR', u'AVZ/Ms', u'B10.D2-H2d', u'B10.D2-Hc0 H2d H2-T18c/oSnJ', u'BALB/c', u'BALB/cA', u'BALB/cBy', u'BALB/cByJ', u'BALB/cJ', u'BALB/cUcsd', u'BFM/2Ms', u'BLG2/Ms', u'BTBR T+ Itpr3tf/J', u'BUB', u'BUB/BnJ', u'C3H/He', u'C3H/HeJ', u'C57BL/6', u'C57BL/6J', u'C57BL/10J', u'C57BLKS/J', u'C57BR/cdJ', u'C57L/J', u'C58/J', u'CAST/EiJ', u'CBA/J', u'CE/J', u'CHD/Ms', u'CZECHII/EiJ', u'DBA/1J', u'DBA/2', u'DBA/2J', u'DDK/Pas', u'FVB', u'FVB/NJ', u'HMI/Ms', u'I/LnJ', u'JF1/Ms', u'KJR/Ms', u'KK/HlJ', u'LG/J', u'LP/J', u'MA/MyJ', u'MAI/Pas', u'MOLF', u'MOLF/EiJ', u'MRL/Mp', u'MRL/MpJ', u'MSM', u'MSM/Ms', u'NJL/Ms', u'NOD/ShiLtJ', u'NON/ShiLtJ', u'NZB/BlN', u'NZB/BlNJ', u'NZW/Lac', u'NZW/LacJ', u'PERA', u'PERA/EiJ', u'PGN2/Ms', u'PL/J', u'PWD/PhJ', u'RIIIS/J', u'SAMP1', u'SAMP8', u'SEA/GnJ', u'SEG/Pas', u'SJL/J', u'SM/J', u'SPRET/EiJ', u'ST/bJ', u'SWN/Ms', u'SWR/J', u'TSOD', u'WSB/EiJ', u'ZALENDE/EiJ'])
        
    def test_strain_snp_no_snps(self):
        """
        @status: Tests the SNPs ribbon does not display when no SNPs are associated to a strain
        @note: Strain-det-snp-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:6156918")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for SAMR1/TaHsd and clicks it
        driver.find_element(By.PARTIAL_LINK_TEXT, 'SAMR1/TaHsd').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #asserts that the strains table is not displayed in the Strains Comparison ribbon
        assert "snpRibbon" not in self.driver.page_source  

    def test_strain_snp_cell_counts(self):
        """
        @status: Tests that counts on a cell hover match the number found from it's corresponding SNP summary page
        @note: Strain-det-snp-5
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:2159745")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for AKR/J and clicks it
        driver.find_element(By.PARTIAL_LINK_TEXT, 'AKR/J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])        
        #clicks the More toggle(turnstile) to display the snps table
        self.driver.find_element(By.ID, 'snpToggle').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'snpContainer')))#waits until the snp table is displayed on the page
        #locate the cell for strain 129S1/SvImJ Chromosome 1
        myelement = driver.find_element(By.CSS_SELECTOR, '#snpTable > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)')
        tooltipText = myelement.get_attribute('title')#Get the title text
        print tooltipText#print the title text to the console
        self.assertEquals(tooltipText, '590,392 SNPs', 'The hover text for strain 129S1/SvImJ Chromosome 1 is not correct')
        #locate the cell for strain 129S1/SvImJ Chromosome 1 and click it
        driver.find_element(By.CSS_SELECTOR, '#snpTable > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)').click()
        #switch focus to the new tab for Mouse SNP Summary page
        driver.switch_to_window(self.driver.window_handles[-1]) 
        #locate the page title
        self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'snpSummaryTable')))#waits until the snp summary table is displayed on the page 
        #assert the number of SNPs is correct as found in the upper right corner under pagination 
        assert "Showing SNP(s) 1 - 100 of 590392" in self.driver.page_source
        
    def test_strain_snp_strain_superscript(self):
        """
        @status: Tests that when you have a strain with multiple superscripting it displays correctly  in the SNP ribbon
        @note: Strain-det-snp-8
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:2162761")
        #time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain name link for BTBR T<+> Itpr3<tf>/J and clicks it
        driver.find_element(By.PARTIAL_LINK_TEXT, 'BTBR').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])        
        
        #locate the involving strain text in the SNP ribbon 
        involvedtext = driver.find_element(By.CLASS_NAME, 'rightLabelSnp')
        print involvedtext.text#print the title text to the console
        self.assertEquals(involvedtext.text, 'SNPs Involving BTBR T+ Itpr3tf/J', 'The Involving strain text is not displaying superscipt properly')
        
                    
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
        self.assertEquals(mut_cells, ['Mutation Carried', 'AanatC57BL/6J', 'Ahrb-1', 'Apobec3Rfv3-r', 'Cd5b', 'Cdh23ahl', 'Cox7a2ls', 'Fbrwt1C57BL/6J', 'Fbrwt2C57BL/6J', 'Gluchos1C57BL/6J', 'Gluchos2C57BL/6J', 'Gluchos3C57BL/6J', 'Micrln', 'Mx1s1', 'n-TRtct5m1J', 'Nlrp12C57BL/6J', 'NntC57BL/6J', 'P2rx7P451L'])
        #print all items found in the Gene column
        cells1 = table.get_column_cells("Marker")
        gene_cells = iterate.getTextAsList(cells1)
        print gene_cells
        #verifies that the right genes appear and in the correct order
        self.assertEquals(gene_cells, ['Marker', 'Aanat', 'Ahr', 'Apobec3', 'Cd5', 'Cdh23', 'Cox7a2l', 'Fbrwt1', 'Fbrwt2', 'Gluchos1', 'Gluchos2', 'Gluchos3', 'Micrl', 'Mx1', 'n-TRtct5', 'Nlrp12', 'Nnt', 'P2rx7'])
        
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
        cells1 = table.get_column_cells("Marker")
        gene_cells = iterate.getTextAsList(cells1)
        print gene_cells
        #verifies that the right genes appear and in the correct order
        self.assertEquals(gene_cells, ['Marker', 'Foxc1'])
                     
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
        cells1 = table.get_column_cells("Marker")
        gene_cells = iterate.getTextAsList(cells1)
        print gene_cells
        #verifies that the right genes appear and in the correct order
        self.assertEquals(gene_cells, ['Marker', 'Rb(11.14)1Dn'])
                     
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
        cells1 = table.get_column_cells("Marker")
        gene_cells = iterate.getTextAsList(cells1)
        print gene_cells
        #verifies that the right genes appear and in the correct order
        self.assertEquals(gene_cells, ['Marker', 'Ddc', 'Tg(Ggt1-cre)M3Egn'])

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
        print mut_count.text
        self.assertEqual(mut_count.text, '17 associated mutations', 'associated mutations count/text is wrong')
        
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

    def test_strain_det_mut_mrk_hover(self):
        """
        @status: Tests that when you hover over a marker symbol in associated mutations table description text appears
        @note: Strain-det-mut-10
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
        ahr_mrk = self.driver.find_element(By.XPATH, '//*[@id="mutationSummaryTable"]/tbody/tr[3]/td[2]/a')
        title_text = ahr_mrk.get_attribute('title')
        print title_text   
        #verifies that the hover text  for Ahr is correct
        self.assertEquals(title_text, 'aryl-hydrocarbon receptor')
                  
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
        cells1 = table.get_column_cells("Marker")
        gene_cells = iterate.getTextAsList(cells1)
        print gene_cells
        #verifies that the right genes appear and in the correct order
        self.assertEquals(gene_cells, ['Marker', 'Bomb1', 'Esl1', 'Foc1', 'lla', 'Lyr2', 'Msmr1', 'Msmr2', 'Tlsm1'])
                     
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
        cells1 = table.get_column_cells("Marker")
        gene_cells = iterate.getTextAsList(cells1)
        print gene_cells
        #verifies that the right genes appear and in the correct order
        self.assertEquals(gene_cells, ['Marker', 'Cfcd', 'Cfcd', 'Opfa', 'Opfa'])  

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
        self.assertEqual(qtl_count[2].text, '2629 associated QTL', 'associated QTL count/text is wrong')
        
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

    def test_strain_det_qtl_mrk_hover(self):
        """
        @status: Tests that when you hover over a marker symbol in associated qtl table description text appears
        @note: Strain-det-qtl-7
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
        aaaq1_mrk = self.driver.find_element(By.XPATH, '//*[@id="qtlSummaryTable"]/tbody/tr[2]/td[2]/a')
        title_text = aaaq1_mrk.get_attribute('title')
        print title_text   
        #verifies that the hover text  for Ahr is correct
        self.assertEquals(title_text, 'aortic arch angle QTL 1')
    
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
        # Enter your strain name/ID
        strainsearchbox.send_keys("MGI:2161574")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locate the link for B6.Cg-Phex<Hyp>/J and click it
        driver.find_element(By.PARTIAL_LINK_TEXT, 'B6.Cg-Phex').click()
        time.sleep(3)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #set browser window to max size
        driver.maximize_window()
        time.sleep(1)
        #locates the human disease link and clicks it
        driver.find_element(By.PARTIAL_LINK_TEXT, 'X-linked').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        #verify the Disease name and DOID are correct for this page
        disname = driver.find_element(By.ID, 'diseaseNameID')
        print disname.text
        self.assertEquals(disname.text, 'X-linked dominant hypophosphatemic rickets (DOID:0050445)')       

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
        #find and print the human diseases in the table, 1 by 1
        dis_cell1 = table.get_cell(1, 0)
        print dis_cell1.text
        dis_cell2 = table.get_cell(2, 0)
        print dis_cell2.text
        dis_cell3 = table.get_cell(3, 0)
        print dis_cell3.text
        dis_cell4 = table.get_cell(4, 0)
        print dis_cell4.text
        dis_cell5 = table.get_cell(5, 0)
        print dis_cell5.text
        dis_cell6 = table.get_cell(6, 0)
        print dis_cell6.text
        dis_cell7 = table.get_cell(7, 0)
        print dis_cell7.text
        #verify the Disease names
        self.assertEqual(dis_cell1.text, 'acromesomelic dysplasia, Grebe type')
        self.assertEqual(dis_cell2.text, 'acromesomelic dysplasia, Hunter-Thompson type')
        self.assertEqual(dis_cell3.text, 'brachydactyly type A1C')
        self.assertEqual(dis_cell4.text, 'brachydactyly type A2')
        self.assertEqual(dis_cell5.text, 'brachydactyly type C')
        self.assertEqual(dis_cell6.text, 'fibular hypoplasia and complex brachydactyly')
        self.assertEqual(dis_cell7.text, 'multiple synostoses syndrome')
        
    def test_strain_humdis_multi_models(self):
        """
        @status: Tests that the page can display more than 1 model in the Associated Diseases ribbon
        @note: Strain-det-disease-4
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:2161574")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locate the link for B6.Cg-Phex<Hyp>/J and click it
        driver.find_element(By.PARTIAL_LINK_TEXT, 'B6.Cg-Phex').click()
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
        #self.assertEqual(all_cells[1].text, 'model 1')
        #self.assertEqual(all_cells[2].text, 'model 2')        
        
    '''def test_strain_humdis_assoc_diseases(self):
        """
        @status: Tests that text number of associated diseases above the disease table matches the table's results in the Associated Diseases ribbon
        @note: Strain-det-disease-6 This test is no longer needed as they removed the text
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
     '''   
    def test_strain_pheno_1_geno(self):
        """
        @status: Tests that the display is fine when phenogrid has association to just 1 genotype
        @note: Strain-det-disease-9, 13 
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
        #locate the link for C57BL/6J-Gdf5Bp-5J/GrsrJ and click it
        driver.find_element(By.LINK_TEXT, 'C57BL/6J-Gdf5Bp-5J/GrsrJ').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(2)
        #locates the phenogrid and click on the cell for growth/size/body
        driver.find_element(By.ID, 'mpSlimgrid9Div').click()
        time.sleep(2)
        #switch focus to the new tab for Phenotype annotations related to growth/size/body
        driver.switch_to_window(self.driver.window_handles[+2])
        time.sleep(2)
        geno = driver.find_element(By.ID, 'fm66877a')
        print geno.text
        self.assertTrue(geno.text, "Gdf5Bp-5J/Gdf5+")

    def test_strain_pheno_multi_geno(self):
        """
        @status: Tests that the display is fine when phenogrid has association to multiple genotypes
        @note: Strain-det-disease-10, no assertion on genotype 8 since it is blank. 8 genotypes for 13 annotations
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
        time.sleep(2)
        #locates the phenogrid and click on the cell for homeostasis/metabolism
        driver.find_element(By.ID, 'mpSlimgrid12Div').click()
        time.sleep(2)
        #switch focus to the new tab for Phenotype annotations related to growth/size/body
        driver.switch_to_window(self.driver.window_handles[+2])
        time.sleep(2)
        geno1 = driver.find_element(By.ID, 'fm12338a')
        geno2 = driver.find_element(By.ID, 'fm12586a')
        geno3 = driver.find_element(By.ID, 'fm30511a')
        geno4 = driver.find_element(By.ID, 'fm70664a')
        geno5 = driver.find_element(By.ID, 'fm30510a')
        geno6 = driver.find_element(By.ID, 'fm19624a')
        geno7 = driver.find_element(By.ID, 'fm1a')
        print geno1.text
        print geno2.text
        print geno3.text
        print geno4.text
        print geno5.text
        print geno6.text
        print geno7.text
        self.assertTrue(geno1.text, "Ahrb-1/Ahrb-1")
        self.assertTrue(geno2.text, "Aliq4C57BL/6J/Aliq4C57BL/6J")
        self.assertTrue(geno3.text, "Gluchos1C57BL/6J/Gluchos1C57BL/6J")
        self.assertTrue(geno4.text, "n-TRtct5m1J/n-TRtct5m1J")
        self.assertTrue(geno5.text, "NntC57BL/6J/NntC57BL/6J")
        self.assertTrue(geno6.text, "Tph2Pro447/Tph2Pro447")
        
    def test_strain_pheno_annot_hover(self):
        """
        @status: Tests that when you hover over a blue box in the Phonoslimgrid it gives you the number of annotations associated
        @note: Strain-det-disease-12 !this test fails because it can't capture the on hover text of the phenogrid boxes.
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
        #locate the link for DBA/1 and click it
        driver.find_element(By.LINK_TEXT, 'A/J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(2)
        #locates the phenogrid box for behavior/neurological and capture it's title
        value1 = driver.find_element(By.ID, 'mpSlimgrid12Div').get_attribute("title")
        #value1 = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/section/div/div[3]/table/tbody/tr[3]/td[2]').get_attribute("title")
        print value1
        #self.assertTrue(value1, "2 annotation(s)")
        #locates the phenogrid box for growth/size/body and capture it's title
        value2 = driver.find_element(By.ID, 'mpSlimgrid9Div').get_attribute("title")
        #value2 = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/section/div/div[3]/table/tbody/tr[3]/td[9]').get_attribute("title")
        print value2
        #self.assertTrue(value2, "1 annotation(s)")
        #locates the phenogrid box for hearing/vestibular/ear and capture it's title
        value3 = driver.find_element(By.ID, 'mpSlimgrid10Div').get_attribute("title")
        #value3 = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/section/div/div[3]/table/tbody/tr[3]/td[10]').get_attribute("title")
        print value3
        #self.assertTrue(value3, "4 annotation(s)")
        #locates the phenogrid box for muscle and capture it's title
        value4 = driver.find_element(By.ID, 'mpSlimgrid18Div').get_attribute("title")
        #value4 = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/section/div/div[3]/table/tbody/tr[3]/td[17]').get_attribute("title")
        print value4
        #self.assertTrue(value4, "1 annotation(s)")
        #locates the phenogrid box for neoplasm and capture it's title
        value5 = driver.find_element(By.ID, 'mpSlimgrid19Div').get_attribute("title")
        #value5 = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/section/div/div[3]/table/tbody/tr[3]/td[18]').get_attribute("title")
        print value5
        #self.assertTrue(value5, "1 annotation(s)")
        #locates the phenogrid box for reproductive system and capture it's title
        value6 = driver.find_element(By.ID, 'mpSlimgrid24Div').get_attribute("title")
        #value6 = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[2]/section/div/div[3]/table/tbody/tr[3]/td[24]').get_attribute("title")
        print value6
        #self.assertTrue(value6, "9 annotation(s)")
            
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
        driver.find_element(By.LINK_TEXT, 'J:22753').click()
        #time.sleep(2)
        #verify the J number J:6835 exists on this page
        assert "J:22753" in self.driver.page_source        
        
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