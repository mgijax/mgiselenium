'''
Created on Oct 20, 2016

@author: jeffc
This suite of tests are for marker detail pages
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys,os.path
#from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
from util import wait, iterate
from util.table import Table
import config

from config import TEST_URL

class TestMarkerDetail(unittest.TestCase):


    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/marker/")
        self.driver.implicitly_wait(10)

    def test_ribbon_locations(self):
        '''
        @status This test verifies the ribbons are being displayed in the correct order on the page.
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Gata1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Gata1').click()
        time.sleep(2)
        summaryRibbon = self.driver.find_element(By.ID, 'summaryRibbon').find_element(By.CSS_SELECTOR, 'div.header.detailCat1')
        print(summaryRibbon.text)
        self.assertEqual(summaryRibbon.text, 'Summary', "Summary ribbon is missing")
        locationribbon = self.driver.find_element(By.ID, 'locationRibbon').find_element(By.CSS_SELECTOR, 'div.header.detailCat2')
        print(locationribbon.text)
        self.assertEqual(locationribbon.text, "Location &\nMaps", "Location & Maps ribbon is missing")
        strainribbon = self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, 'div.header.detailCat1')
        print(strainribbon.text)
        self.assertEqual(strainribbon.text, "Strain\nComparison", "Strain Comparison ribbon is missing")
        homologyribbon = self.driver.find_element(By.ID, 'homologyRibbon').find_element(By.CSS_SELECTOR, 'div.header.detailCat2')
        print(homologyribbon.text)
        self.assertEqual(homologyribbon.text, 'Homology', "Homology ribbon is missing")
        diseaseribbon = self.driver.find_element(By.ID, 'diseaseRibbon').find_element(By.CSS_SELECTOR, 'div.header.detailCat1')
        self.assertEqual(diseaseribbon.text, "Human Diseases", "Human Diseases ribbon is missing")
        phenoribbon = self.driver.find_element(By.ID, 'phenotypeRibbon').find_element(By.CSS_SELECTOR, 'div.header.detailCat2')
        print(phenoribbon.text)
        self.assertEqual(phenoribbon.text, "Mutations,\nAlleles, and\nPhenotypes", "Phenotype ribbon is missing")
        goribbon = self.driver.find_element(By.ID, 'goRibbon').find_element(By.CSS_SELECTOR, 'div.header.detailCat1')
        print(goribbon.text)
        self.assertEqual(goribbon.text, "Gene Ontology\n(GO)\nClassifications", "GO ribbon is missing")
        gxdribbon = self.driver.find_element(By.ID, 'expressionRibbon').find_element(By.CSS_SELECTOR, 'div.header.detailCat2')
        print(gxdribbon.text)
        self.assertEqual(gxdribbon.text, "Expression", "Expression ribbon is missing")
        interactionsRibbon = self.driver.find_element(By.ID, 'interactionRibbon').find_element(By.CSS_SELECTOR, 'div.header.detailCat1')
        print(interactionsRibbon.text)
        self.assertEqual(interactionsRibbon.text, 'Interactions', "Interactions ribbon is missing")
        sequenceribbon = self.driver.find_element(By.ID, 'sequenceRibbon').find_element(By.CSS_SELECTOR, 'div.header.detailCat2')
        print(sequenceribbon.text)
        self.assertEqual(sequenceribbon.text, "Sequences &\nGene Models", "Sequence ribbon is missing")
        proteinribbon = self.driver.find_element(By.ID, 'proteinInfoRibbon').find_element(By.CSS_SELECTOR, 'div.header.detailCat1')
        print(proteinribbon.text)
        self.assertEqual(proteinribbon.text, "Protein\nInformation", "Protein Information ribbon is missing")
        molecularRibbon = self.driver.find_element(By.ID, 'molecularReagentsRibbon').find_element(By.CSS_SELECTOR, 'div.header.detailCat2')
        print(molecularRibbon.text)
        self.assertEqual(molecularRibbon.text, 'Molecular\nReagents', "Molecular Reagents ribbon is missing")
        otherRibbon = self.driver.find_element(By.ID, 'otherMgiIdsRibbon').find_element(By.CSS_SELECTOR, 'div.header.detailCat1')
        print(otherRibbon.text)
        self.assertEqual(otherRibbon.text, 'Other\nAccession IDs', "Other Accession IDs ribbon is missing")
        referencesRibbon = self.driver.find_element(By.ID, 'referenceRibbon').find_element(By.CSS_SELECTOR, 'div.header.detailCat2')
        print(referencesRibbon.text)
        self.assertEqual(referencesRibbon.text, 'References', "References ribbon is missing")
        
    def test_apf_link(self):
        '''
        @status this test verifies that the APF link for incidential mutations goes to the correct website location.
        @note test works as of 3/29/18
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Alad")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Alad').click()
        apflnk = self.driver.find_element(By.LINK_TEXT, 'APF')
        href = apflnk.find_element_by_xpath("//a").get_attribute('href')
        
        self.assertTrue(href, "https://databases.apf.edu.au/mutations/snpRow/list?mgiAccessionid=MGI:96853")

    def test_tss_display(self):
        '''
        @status this test verifies the link for Transcription exits(and is correctly worded) in the summary ribbon and clicking it displays the popup table 
        @note the sites should be displayed by coordinate order
        @note mrkdetail-sum-1, 2
        '''
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Vwa3b")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Vwa3b').click()
        #Find the Transcription link in the summary ribbon section, verify the link text and click it    
        tss_link = self.driver.find_element(By.ID, 'showTss')        
        print(tss_link.text)
        self.assertEqual(tss_link.text, '8 TSS', 'The tss link text is not correct!')
        tss_link.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'tssDiv_h')))#waits until the TSS table popup is displayed on the page      
        #find the Tss table popup and verify the table heading
        tss_head = self.driver.find_element(By.ID, 'tssDiv_h')
        print(tss_head.text)
        self.assertEqual(tss_head.text, 'TSS for Vwa3b:', 'The TSS table heading is not correct!')
        
        
    def test_tss_table_display_sort(self):
        '''
        @status this test opens the Tss table and verifies the table results are sorted by location coordinates
        @note the sites should be displayed by coordinate order on marker detail but by Distance from Gene 6'-end in Tss table 
        @note mrkdetail-sum-3
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Sgk3")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Sgk3').click()        
        #Find the All TSS link and click it
        self.driver.find_element(By.ID, 'showTss').click()
        tss_table = self.driver.find_element(By.ID, 'tssTable')
        table = Table(tss_table)
        #Iterate the table Location column
        cells = table.get_column_cells('Location')
        loc_cells = iterate.getTextAsList(cells)      
        #Verify the TSS table locations are correct and in the correct order.
        self.assertEqual(loc_cells[1], 'Chr1:9797795-9797809 (+)')
        self.assertEqual(loc_cells[2], 'Chr1:9797812-9797823 (+)')
        self.assertEqual(loc_cells[3], 'Chr1:9797986-9798040 (+)')
        self.assertEqual(loc_cells[4], 'Chr1:9798123-9798216 (+)')
        self.assertEqual(loc_cells[5], 'Chr1:9848270-9848285 (+)') 
        self.assertEqual(loc_cells[6], 'Chr1:9848294-9848362 (+)')
        self.assertEqual(loc_cells[7], 'Chr1:9848375-9848398 (+)')       
        #Iterate the table Distance from Gene 5' -end column
        cells = table.get_column_cells("Distance from Gene 5'-end")
        loc_cells = iterate.getTextAsList(cells)      
        #Verify the TSS table Distance are correct and in the correct order.
        self.assertEqual(loc_cells[1], '-305 bp')
        self.assertEqual(loc_cells[2], '-289 bp')
        self.assertEqual(loc_cells[3], '-94 bp')
        self.assertEqual(loc_cells[4], '63 bp')
        self.assertEqual(loc_cells[5], '50,171 bp') 
        self.assertEqual(loc_cells[6], '50,221 bp')
        self.assertEqual(loc_cells[7], '50,280 bp')        

    def test_tss_detail_link(self):
        '''
        @status this test verifies clicking a Tss site ID takes you to it's detail page
        @note mrkdetail-sum-4
        '''
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Carf")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Carf').click()        
        #Find the TSS link and click it
        self.driver.find_element(By.ID, 'showTss').click()
        #locates the TSS table and verify the tss ID is correct
        tss_table = Table(self.driver.find_element_by_id("tssTable"))
        cell = tss_table.get_cell(1, 0)   
        print(cell.text)
        self.assertEqual(cell.text, 'Tssr6917', 'The TSSR ID is not correct!')
        #find and click the Tssr ID
        self.driver.find_element(By.LINK_TEXT, 'Tssr6917').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'titleBarMainTitle')))#waits until the page title is displayed on the page
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        #Assert that the page title is for Tssr6917
        self.assertEqual(page_title.text, 'Tssr6917') 
        
    def test_strain_table_headings(self):
        '''        
        @status this test verifies the strain table headings in the Genome Context & Strain Distribution ribbon are correctly ordered/displayed.
        @note mrkdetail-strain-1
        ''' 
        driver = self.driver       
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ren1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ren1').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, 'div.toggleImage.hdExpand').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'table_strainMarkers')))#waits until the strain marker table is displayed on the page
        strain_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strain_table)
        #Iterate and print the table headers
        cells = table.get_header_cells()
        header_cells = iterate.getTextAsList(cells)      
        #Verify the strain table headers are correct.
        self.assertEqual(header_cells[0], 'Strain')
        self.assertEqual(header_cells[1], 'Gene Model ID')
        self.assertEqual(header_cells[2], 'Feature Type')
        self.assertEqual(header_cells[3], 'Coordinates')
        self.assertEqual(header_cells[4], 'Select Strains')        

    def test_strain_no_annot(self):
        '''        
        @status this test verifies the strain table(no strain ribbon) is not present in the Strain Comparison ribbon when strains have no annotation.
        @note mrkdetail-strain-2
        '''   
        driver = self.driver      
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Arp")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Arp').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        
        #asserts that the strains ribbon is not displayed on the page
        assert "table_strainRibbon" not in self.driver.page_source  
        

    def test_strain_turnstile_closed(self):
        '''        
        @status this test verifies the Strain Comparison ribbon when the turnstile is closed shows strain annotations, MGV link, SNPs within 2kb(if available).
        @note mrkdetail-strain-3  !!this test needs a rewrite as it no longer works by links but by pulldown menu
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ren1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ren1').click()
        #locate the number of strain annotations
        strain_annot = self.driver.find_element(By.ID, 'annotatedStrainMarkerCount')
        #verify the strain annotations number is correct
        self.assertEqual(strain_annot.text, '16')
        #locate the MGV link
        mgv_link = self.driver.find_element(By.ID, 'sgGoButton')
        print(mgv_link.text)
        #verify the MGV link text is correct
        self.assertEqual(mgv_link.text, 'Multiple Genome Viewer (MGV)')        
        #locate the SNP link
        snp_link = self.driver.find_element(By.ID, 'snpLink')
        print(snp_link.text)
        #verify the SNP link text is correct
        self.assertEqual(snp_link.text, '298')

    def test_strain_turnstile_closed_nostrain_snp(self):
        '''        
        @status this test verifies the Strain Comparison ribbon when the turnstile is closed shows no Annotation Data or SNP Data when none exist.
        @note mrkdetail-strain-4 
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Arp")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Arp').click()
        #verify the strain annotations number is not displayed
        assert "annotatedStrainMarkerCount" not in self.driver.page_source
        #locate the MGV link
        mgv_link = self.driver.find_element(By.ID, 'mgvSpan')
        print(mgv_link.text)
        #verify the MGV link text is correct
        self.assertEqual(mgv_link.text, 'Multiple Genome Viewer (MGV)')
        #Assert the SNPs within 2kb link is not displayed
        assert "snpLink" not in self.driver.page_source
        

    def test_mgv_link_not_exists(self):
        '''        
        @status this test verifies the Multiple Genome Viewer(MGV) link exists only when B6 coordinates exist.
        @note mrkdetail-strain-5
        '''  
        driver = self.driver      
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ren2")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ren2').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #verify the MGV link is correctly not displayed in the Strain Comparison ribbon
        assert "Multiple Genome Viewer (MGV)" not in self.driver.page_source
        

    def test_mgv_link_10kb_flank(self):
        '''        
        @status this test verifies the Multiple Genome Viewer(MGV) has 10kb flanking on each end of the sequence link URL.
        @note mrkdetail-strain-6 
        '''       
        driver = self.driver 
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ren1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ren1').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #clicks the More toggle(turnstile) to display the strain distribution data
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, 'div.toggleImage.hdExpand').click()
        #time.sleep(2)
        #locates all MGV link on the page
        mgv_link = self.driver.find_element(By.LINK_TEXT, 'Multiple Genome Viewer (MGV)')    
        print(mgv_link.get_attribute('href'))
        #verify the MGV link href is correct(the 10KB flanking added is in the url)
        self.assertEqual(mgv_link.get_attribute('href'), 'http://proto.informatics.jax.org/prototypes/mgv/#ref=C57BL/6J&genomes=C57BL/6J+129S1/SvImJ+A/J+AKR/J+BALB/cJ+C3H/HeJ+C57BL/6NJ+CAROLI/EIJ+CAST/EiJ+CBA/J+DBA/2J+FVB/NJ+LP/J+NOD/ShiLtJ+NZO/HlLtJ+PAHARI/EIJ+PWK/PhJ+SPRET/EiJ+WSB/EiJ&chr=1&start=133300674&end=133410320&highlight=MGI:97898', 'The MGV link href flanking is incorrect!')

    def test_strain_table_genemodelid_links(self):
        '''        
        @status this test verifies that the Gene Model IDs in the strains table link to their MGI gene model sequence, found in the Strain Comparison ribbon. (only verifying 1 link of 18)
        @note mrkdetail-strain-9
        '''   
        driver = self.driver      
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Gata1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Gata1').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, ' div.toggleImage.hdExpand').click()
        #time.sleep(2)
        #find the link for C57BL/6J gene model id
        self.driver.find_element(By.LINK_TEXT, 'MGI_C57BL6J_95661').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #time.sleep(2)
        structure_table = self.driver.find_element(By.CLASS_NAME, 'detailStructureTable')
        table = Table(structure_table)
        #Iterate the second row of the disease table
        all_cells = table.get_row('ID/Version')
        print(all_cells.text)
        #verify the ID/Version row of data
        self.assertEqual(all_cells.text, 'ID/Version\nMGI_C57BL6J_95661 Multiple Genome Viewer (MGV) Version: MGI_C57BL6J_95661.GRCm38')
        #switch focus back to the Gene Detail page
        self.driver.switch_to_window(self.driver.window_handles[0])
        #find the link for 129S1/SvImJ gene model id
        self.driver.find_element(By.LINK_TEXT, 'MGP_129S1SvImJ_G0035536').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #time.sleep(2)
        structure_table = self.driver.find_element(By.CLASS_NAME, 'detailStructureTable')
        table = Table(structure_table)
        #Iterate the second row of the disease table
        all_cells = table.get_row('ID/Version')
        print(all_cells.text)
        #verify the ID/Version row of data
        self.assertEqual(all_cells.text, 'ID/Version\nMGP_129S1SvImJ_G0035536 Multiple Genome Viewer (MGV) Version: MGP_129S1SvImJ_G0035536.Ensembl Release 92')

    def test_strain_table_vs_seqmap_noB6(self):
        '''        
        @status this test verifies that when a canonical gene doesn't have a B6 strain gene then the strain table for C57BL/6J says "no annotation"
        @note mrkdetail-strain-10
        '''   
        driver = self.driver      
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Sox1ot")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Sox1ot').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #locate the Sequence Map coordinates
        seq_map = self.driver.find_element(By.XPATH, '//*[@id="templateBodyInsert"]/div[2]/div[2]/div[2]/section[1]/ul/li[1]/div[2]')
        print(seq_map.text)
        #verify the coordinates data for the sequence map
        self.assertEqual(seq_map.text, 'Chr8:12385771-12436732 bp, + strand', 'sequence map coordinates have changed!')
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, 'div.toggleImage.hdExpand').click()
        #find the Gene Model ID column of the strains table
        #time.sleep(2)
        strains_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strains_table)
        #Iterate the second row of the disease table
        all_cells = table.get_column_cells('Gene Model ID')
        print(all_cells[1].text)
        #verify the ID/Version row of data
        self.assertEqual(all_cells[1].text, 'no annotation')
        
    def test_strain_table_vs_seqmap_nomatch(self):
        '''        
        @status this test verifies that the sequence map coordinates do not match the strains table C57BL/6J coordinates when the gene model is not MGI
        @note mrkdetail-strain-11 *this test will go away when we stop using the reference B6 models
        '''
        driver = self.driver          
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pax6').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #locate the Sequence Map coordinates
        seq_map = self.driver.find_element(By.XPATH, '//*[@id="templateBodyInsert"]/div[2]/div[2]/div[2]/section[1]/ul/li[1]/div[2]')
        print(seq_map.text)
        #verify the coordinates data for the sequence map
        self.assertEqual(seq_map.text, 'Chr2:105668900-105697364 bp, + strand', 'sequence map coordinates have changed!')
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, 'div.toggleImage.hdExpand').click()
        #find the coordinates column of the strains table
        #time.sleep(2)
        strains_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strains_table)
        #Iterate the second row of the disease table
        all_cells = table.get_column_cells('Coordinates')
        print(all_cells[1].text)
        #verify the ID/Version row of data
        self.assertEqual(all_cells[1].text, 'Chr2:105668896-105698410 (+)')
        
    def test_strain_table_vs_seqmap_match(self):
        '''        
        @status this test verifies that the sequence map coordinates match the strains table C57BL/6J coordinates when the gene model is MGI
        @note mrkdetail-strain-11A  !!!!!!This test fails because of a data issue(missing strand info) right now 7/18/2018!!!!!
        '''   
        driver = self.driver     
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Igh-8")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Igh-8').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #locate the Sequence Map coordinates
        seq_map = self.driver.find_element(By.XPATH, '//*[@id="locationRibbon"]/div[2]/section[1]/ul/li[1]/div[2]')
        print(seq_map.text)
        #verify the coordinates data for the sequence map
        self.assertEqual(seq_map.text, 'Chr12:113365795-113367226 bp, - strand', 'sequence map coordinates have changed!')
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, 'div.toggleImage.hdExpand').click()
        #find the coordinates column of the strains table
        #time.sleep(2)
        strains_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strains_table)
        #Iterate the second row of the disease table
        all_cells = table.get_column_cells('Coordinates')
        print(all_cells[1].text)
        #verify the ID/Version row of data
        self.assertEqual(all_cells[1].text, 'Chr12:113365796-113367227 (-)')

    def test_strain_table_single_fasta(self):
        '''        
        @status this test verifies that you can download a single FASTA sequence from the Strain table using the download checkbox 
        @note mrkdetail-strain-14 
        '''     
        driver = self.driver
        self.driver.set_window_size(1024, 768)   
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ppnr")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ppnr').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, 'div.toggleImage.hdExpand').click()
        #time.sleep(2)
        #find and select the the Select Strain box for the strain A/J
        self.driver.find_elements(By.CLASS_NAME, 'sgCheckbox')[2].click()
        #time.sleep(2)
        #find and click the 'Go' button with default set as Get FASTA
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[0].click()
        #time.sleep(2)
        #switch focus to the new tab for the FASTA results
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #time.sleep(2)
        #verify the correct sequence is being returned
        assert 'MGP_AJ_G0036915 19:53381666-53386571' in self.driver.page_source 

    def test_strain_table_multiple_fasta(self):
        '''        
        @status this test verifies that you can download multiple FASTA sequences from the Strain table using the download checkboxs 
        @note mrkdetail-strain-15 
        ''' 
        driver = self.driver
        self.driver.set_window_size(1024, 768)       
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pax6').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, 'div.toggleImage.hdExpand').click()
        #time.sleep(2)
        #find and select the the Download boxes for the strains A/J, C3H/HeJ, and CBA/J
        self.driver.find_elements(By.CLASS_NAME, 'sgCheckbox')[2].click()
        self.driver.find_elements(By.CLASS_NAME, 'sgCheckbox')[5].click()
        self.driver.find_elements(By.CLASS_NAME, 'sgCheckbox')[9].click()
        #time.sleep(2)
        #find and click the 'Get FASTA' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[0].click()
        #time.sleep(2)
        #switch focus to the new tab for the FASTA results
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #time.sleep(2)
        #verify the correct sequences are being returned
        assert 'MGP_AJ_G0026191 2:103346997-103376112' in self.driver.page_source 
        assert 'MGP_C3HHeJ_G0025950 2:106465683-106497601' in self.driver.page_source
        assert 'MGP_CBAJ_G0025928 2:115224186-115254439' in self.driver.page_source

    def test_strain_table_B6_fasta(self):
        '''        
        @status this test verifies that you can download a B6 strain gene FASTA sequence from the Strain table using the download checkbox 
        @note mrkdetail-strain-16 
        '''   
        driver = self.driver
        self.driver.set_window_size(1200, 900)     
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Gata1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Gata1').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, 'div.toggleImage.hdExpand').click()
        #time.sleep(2)
        #find and select the the Download box for the strain C57BL/6J
        self.driver.find_elements(By.CLASS_NAME, 'sgCheckbox')[0].click()
        #time.sleep(2)
        #find and click the 'Get FASTA' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[0].click()
        #time.sleep(2)
        #switch focus to the new tab for the FASTA results
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #time.sleep(2)
        #verify the correct sequence is being returned
        assert 'MGI_C57BL6J_95661 X:7959260-7978071' in self.driver.page_source 

    def test_strain_table_all_fasta(self):
        '''        
        @status this test verifies that you can download all FASTA sequences from the Strain table using the 'Check All' button 
        @note mrkdetail-strain-12, 17 
        '''  
        driver = self.driver 
        self.driver.set_window_size(1200, 900)     
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Zim3")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Zim3').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, 'div.toggleImage.hdExpand').click()
        #time.sleep(2)
        #find and click the 'Select All' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[1].click()
        #time.sleep(2)       
        #find the "Get FASTA" option in the pulldown list located above the strain table and select it
        Select (self.driver.find_element(By.NAME, 'strainOp')).select_by_visible_text('Get FASTA')
        time.sleep(2)
        #find and click the 'Go' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[0].click()
        #time.sleep(2)
        #switch focus to the new tab for the FASTA results
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(2)
        #verify the correct sequences are being returned
        assert 'MGI_C57BL6J_2151058 7:6955685-6977420' in self.driver.page_source 
        assert 'MGP_129S1SvImJ_G0004408 7:4064690-4089229' in self.driver.page_source
        assert 'MGP_AJ_G0004385 7:3946706-3968051' in self.driver.page_source
        assert 'MGP_AKRJ_G0004367 7:4199441-4224713' in self.driver.page_source 
        assert 'MGP_BALBcJ_G0004371 7:4050119-4074786' in self.driver.page_source
        assert 'MGP_C3HHeJ_G0004320 7:4032181-4053614' in self.driver.page_source
        assert 'MGP_C57BL6NJ_G0004520 7:4282414-4306205' in self.driver.page_source 
        assert 'MGP_CASTEiJ_G0004280 7:3933580-3955838' in self.driver.page_source
        assert 'MGP_CBAJ_G0004314 7:4422337-4449131' in self.driver.page_source
        assert 'MGP_DBA2J_G0004329 7:3984146-4005522' in self.driver.page_source 
        assert 'MGP_FVBNJ_G0004347 7:3958576-3980320' in self.driver.page_source
        assert 'MGP_LPJ_G0004409 7:4189174-4214764' in self.driver.page_source
        assert 'MGP_NZOHlLtJ_G0004519 7:3984097-4008151' in self.driver.page_source 
        assert 'MGP_PWKPhJ_G0004233 7:4142731-4165139' in self.driver.page_source
        assert 'MGP_SPRETEiJ_G0004175 7:3565285-3587263' in self.driver.page_source
        assert 'MGP_WSBEiJ_G0004319 7:4155212-4179026' in self.driver.page_source

    def test_strain_specific_marker(self):
        '''        
        @status this test verifies that a strain-specific marker is correctly identified in the Strain Comparison ribbon
        @note mrkdetail-strain-18  
        '''   
        driver = self.driver     
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Mx2")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Mx2').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #locate the Strain-specific icon and text in the strain comparison ribbon
        specific = self.driver.find_element(By.LINK_TEXT, 'Strain-Specific Marker')
        print(specific.text)
        #verify the Strain-specific icon and text is displayed in the strain comparison ribbon
        self.assertEqual(specific.text, 'Strain-Specific Marker', 'the Strain-specific icon and text is not displaying!')

    def test_strain_only_coord(self):
        '''        
        @status this test verifies that only the Multiple Genome Viwer (MGV) link exists in the Strain Comparison ribbon when no strain available
        @note mrkdetail-strain-19  
        '''  
        driver = self.driver      
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Arp")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Arp').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #locate the strain comparison ribbon
        strain_ribbon = self.driver.find_element(By.ID, 'strainRibbon')
        print(strain_ribbon.text)
        #verify the Strain-specific icon and text is displayed in the strain comparison ribbon
        self.assertEqual(strain_ribbon.text, 'Strain\nComparison\nmore\nMultiple Genome Viewer (MGV)', 'the Strain Comparison ribbon display has changed!')        

    def test_strain_only_poly(self):
        '''        
        @status this test verifies that only polymorphism data exists in the Strain Comparison ribbon when no strain or coordinates available
        @note mrkdetail-strain-20  
        '''  
        driver = self.driver      
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Act2")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Act2').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #locate the strain comparison ribbon
        strain_ribbon = self.driver.find_element(By.ID, 'strainRibbon')
        time.sleep(2)
        print(strain_ribbon.text)
        #verify the Strain-specific icon and text is displayed in the strain comparison ribbon
        self.assertEqual(strain_ribbon.text, 'Strain\nComparison\nless\nRFLP\n1', 'the Strain Comparison ribbon display has changed!')     

    def test_strain_table_founders_select(self):
        '''        
        @status this test verifies that when you click the Select DO/CC Founders button in the Strain Comparison ribbon the correct strains get selected in the strains table 
        @note mrkdetail-strain-21 
        '''   
        driver = self.driver
        self.driver.set_window_size(1200, 900)     
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pax6').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, 'div.toggleImage.hdExpand').click()
        #time.sleep(2)
        #find and click the 'Select DO/CC Founders' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[2].click()
        #time.sleep(2)
        #verify which Select Strains are checked and which ones are not        
        sel1 = self.driver.find_elements(By.NAME, 'seqs')[0].get_attribute('checked')
        sel2 = self.driver.find_elements(By.NAME, 'seqs')[1].get_attribute('checked')
        sel3 = self.driver.find_elements(By.NAME, 'seqs')[2].get_attribute('checked')
        sel4 = self.driver.find_elements(By.NAME, 'seqs')[3].get_attribute('checked')
        sel5 = self.driver.find_elements(By.NAME, 'seqs')[4].get_attribute('checked')
        sel6 = self.driver.find_elements(By.NAME, 'seqs')[5].get_attribute('checked')
        sel7 = self.driver.find_elements(By.NAME, 'seqs')[6].get_attribute('checked')
        sel8 = self.driver.find_elements(By.NAME, 'seqs')[7].get_attribute('checked')
        sel9 = self.driver.find_elements(By.NAME, 'seqs')[8].get_attribute('checked')
        sel10 = self.driver.find_elements(By.NAME, 'seqs')[9].get_attribute('checked')
        sel11 = self.driver.find_elements(By.NAME, 'seqs')[10].get_attribute('checked')
        sel12 = self.driver.find_elements(By.NAME, 'seqs')[11].get_attribute('checked')
        sel13 = self.driver.find_elements(By.NAME, 'seqs')[12].get_attribute('checked')
        sel14 = self.driver.find_elements(By.NAME, 'seqs')[13].get_attribute('checked')
        sel15 = self.driver.find_elements(By.NAME, 'seqs')[14].get_attribute('checked')
        sel16 = self.driver.find_elements(By.NAME, 'seqs')[15].get_attribute('checked')
        sel17 = self.driver.find_elements(By.NAME, 'seqs')[16].get_attribute('checked')
        sel18 = self.driver.find_elements(By.NAME, 'seqs')[17].get_attribute('checked')
        self.assertTrue(sel1, 'sel1 is not selected')
        self.assertTrue(sel2, 'sel2 is not selected')
        self.assertTrue(sel3, 'sel3 is not selected')
        self.assertFalse(sel4, 'sel4 is not selected')
        self.assertFalse(sel5, 'sel5 is not selected')
        self.assertFalse(sel6, 'sel6 is not selected')
        self.assertFalse(sel7, 'sel7 is not selected')
        self.assertFalse(sel8, 'sel8 is not selected')
        self.assertTrue(sel9, 'sel9 is not selected')
        self.assertFalse(sel10, 'sel10 is not selected')
        self.assertFalse(sel11, 'sel11 is not selected')
        self.assertFalse(sel12, 'sel12 is not selected')
        self.assertFalse(sel13, 'sel13 is not selected')
        self.assertTrue(sel14, 'sel14 is not selected')
        self.assertTrue(sel15, 'sel15 is not selected')
        self.assertTrue(sel16, 'sel16 is not selected')
        self.assertFalse(sel17, 'sel17 is not selected')
        self.assertTrue(sel18, 'sel18 is not selected')

    def test_strain_table_send_sanger(self):
        '''        
        @status this test verifies that you can send Strain table data to Sanger using the pulldown option and it returns the correct data
        @note mrkdetail-strain-22
        '''  
        driver = self.driver 
        self.driver.set_window_size(1200, 900)     
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Zim3")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Zim3').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, 'div.toggleImage.hdExpand').click()
        #time.sleep(2)
        #find and click the 'Select All' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[1].click()
        #time.sleep(2)
        #find the "Send to Sanger SNP Query" option in the pulldown list located above the strain table and select it
        Select (self.driver.find_element(By.NAME, 'strainOp')).select_by_visible_text('Send to Sanger SNP Query (+/- 2kb)')
        time.sleep(2)
        #find and click the 'Go' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[0].click()
        #time.sleep(2)
        #switch focus to the new tab for the Sanger results
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #time.sleep(2)
        #locates the SNPs table and verify the table headers have all the correct strains
        strain_table = Table(self.driver.find_element(By.XPATH, '//*[@id="t_snps_0"]/div[1]/table'))
        cells = strain_table.get_header_cells()
        print(iterate.getTextAsList(cells))
        #time.sleep(5)
        #verify the correct strains are being returned in the header of the table
        print(cells[5].text)
        self.assertEqual(cells[5].text, '129S1/SvImJ', '129S1/SvImJ is not a header')
        self.assertEqual(cells[6].text, 'AKR/J', 'AKR/J is not a header')
        self.assertEqual(cells[7].text, 'A/J', 'A/J is not a header')
        self.assertEqual(cells[8].text, 'BALB/cJ', 'BALB/cJ is not a header')
        self.assertEqual(cells[9].text, 'C3H/HeJ', 'C3H/HeJ is not a header')
        self.assertEqual(cells[10].text, 'C57BL/6NJ', 'C57BL/6NJ is not a header')
        self.assertEqual(cells[11].text, 'CAST/EiJ', 'CAST/EiJ is not a header')
        self.assertEqual(cells[12].text, 'CBA/J', 'CBA/J is not a header')
        self.assertEqual(cells[13].text, 'DBA/2J', 'DBA/2J is not a header')
        self.assertEqual(cells[14].text, 'FVB/NJ', 'FVB/NJ is not a header')
        self.assertEqual(cells[15].text, 'LP/J', 'LP/J is not a header')
        self.assertEqual(cells[16].text, 'NOD/ShiLtJ', 'NOD/ShiLtJ is not a header')
        self.assertEqual(cells[17].text, 'NZO/HlLtJ', 'NZO/HlLtJ is not a header')
        self.assertEqual(cells[18].text, 'PWK/PhJ', 'PWK/PhJ is not a header')
        self.assertEqual(cells[19].text, 'SPRET/EiJ', 'SPRET/EiJ is not a header')
        self.assertEqual(cells[20].text, 'WSB/EiJ', 'WSB/EiJ is not a header')      

    def test_strain_table_multi_models(self):
        '''        
        @status this test verifies that when a gene has multiple gene model IDs to the same strain the strain table displays them correctly
        @note mrkdetail-strain-22
        '''   
        driver = self.driver      
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Rprl1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Rprl1').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, 'div.toggleImage.hdExpand').click()
        #find the Gene Model ID column of the strains table
        #time.sleep(2)
        strains_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strains_table)
        #Iterate the first column of the disease table
        strain_cells = table.get_column_cells('Strain')
        print(strain_cells[1].text)
        #verify the rows of data for the Strain column
        self.assertEqual(strain_cells[1].text, 'C57BL/6J')
        self.assertEqual(strain_cells[2].text, '129S1/SvImJ')
        self.assertEqual(strain_cells[3].text, 'A/J')
        self.assertEqual(strain_cells[4].text, 'A/J')
        self.assertEqual(strain_cells[5].text, 'AKR/J')
        self.assertEqual(strain_cells[6].text, 'AKR/J')
        self.assertEqual(strain_cells[7].text, 'BALB/cJ')
        self.assertEqual(strain_cells[8].text, 'BALB/cJ')
        self.assertEqual(strain_cells[9].text, 'C3H/HeJ')
        #Iterate the second column of the disease table
        model_cells = table.get_column_cells('Gene Model ID')
        print(model_cells[1].text)
        #verify the Gene Model ID column of data
        self.assertEqual(model_cells[1].text, 'MGI_C57BL6J_105105')
        self.assertEqual(model_cells[2].text, 'MGP_129S1SvImJ_G0005544')
        self.assertEqual(model_cells[3].text, 'MGP_AJ_G0006976')
        self.assertEqual(model_cells[4].text, 'MGP_AJ_G0036786')
        self.assertEqual(model_cells[5].text, 'MGP_AKRJ_G0036736')
        self.assertEqual(model_cells[6].text, 'MGP_AKRJ_G0007264')
        self.assertEqual(model_cells[7].text, 'MGP_BALBcJ_G0036776')
        self.assertEqual(model_cells[8].text, 'MGP_BALBcJ_G0006952')
        self.assertEqual(model_cells[9].text, 'no annotation')

        
    def test_turnstile_behavior(self):
        '''
        @status this test verifies In the Human Diseases section, confirm there are turnstile icons for showing more data
        and clicking the turnstile icon displays the complete Human Diseases table.
        @note mrkdetail-hdisease-1
        '''
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Shh")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Shh').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, '#diseaseRibbon > div:nth-child(2) > div:nth-child(1)').click()
        #time.sleep(2)
        diseasetable = self.driver.find_element(By.ID, 'humanDiseaseTable')
        self.assertTrue(diseasetable.is_displayed())        

    def test_disease_tbl_doids(self):
        '''
        @status this test verifies that the disease table in the Human Diseases ribbon now displays the DOID beside
         each disease instead of the OMIM ID
         @bug need to ask Olin why would only certain diseases get captured from the table?
         @note mrkdetail-hdisease-2
        '''
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ins2")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ins2').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, '#diseaseRibbon > div:nth-child(2) > div:nth-child(1)').click()
        #time.sleep(2)
        disease_table = self.driver.find_element(By.ID, 'humanDiseaseTable')
        table = Table(disease_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))        
        # print row 1
        cells = table.get_column_cells("Human Disease")
        disease_cells = iterate.getTextAsList(cells)
        print(disease_cells)
        self.assertEqual(disease_cells[1], 'permanent neonatal diabetes mellitus\nIDs')
        #self.assertEquals(disease_cells[2], 'maturity-onset diabetes of the young\nIDs')
        #self.assertEquals(disease_cells[3], 'type 1 diabetes mellitus\nIDs')
        #self.assertEquals(disease_cells[4], 'type 2 diabetes mellitus\nIDs')
        self.assertEqual(disease_cells[5], 'maturity-onset diabetes of the young type 10\nIDs')
                
    def test_mouse_model_strain_links(self):
        '''
        @status this test verifies In the Human Diseases section, from the Mouse Model popup strains in Genetic background link to their strain 
        detail page.
        @note mrkdetail-hdisease-3
        '''
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pde6b")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pde6b').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, '#diseaseRibbon > div:nth-child(2) > div:nth-child(1)').click()
        #time.sleep(5)
        self.driver.find_element(By.ID, 'showDOID_0110375').click()
        #switch focus to the popup page
        #self.driver.switch_to_window(self.driver.window_handles[-1])
        #Find the link in the Genetic Background column C57BL/6J-Tg(SNCA)ARyot and click it
        self.driver.find_element(By.LINK_TEXT, 'C3H/HeJ').click()
        #time.sleep(2)
        #switch focus to the new tab for strain detail page
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #Asserts that the strain page is for the correct strain
        assert "C3H/HeJ" in self.driver.page_source  

    def test_mpontology_annot_strain_links(self):
        '''
        @status this test verifies when you click the Phenotype summary link(for genetic backgrounds) from the Mutations, Alleles, and Phenotypes ribbon
        to open the MP ontology annotations page you find strains in the genetic background column link to their strain detail page.
        @note mrkdetail-allele-5
        '''
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pde6b")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pde6b').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        self.driver.find_element(By.ID, 'phenoAnnotationLink').click()
        #Find the link in the Genetic Background column C57BL/6J-Pde6b<rd1-2J>/J and click it
        self.driver.find_element(By.LINK_TEXT, 'C57BL/6J-Pde6brd1-2J/J').click()
        #time.sleep(2)
        #switch focus to the new tab for strain detail page
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #time.sleep(2)
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        print(page_title.text)
        #Asserts that the strain page is for the correct strain
        self.assertEqual(page_title.text, 'C57BL/6J-Pde6brd1-2J/J', 'Page title is not correct!')

    def test_mpontology_annot_strain_links2(self):
        '''
        @status this test verifies when you click the Phenotype summary link(for multigenic genotypes) from the Mutations, Alleles, and Phenotypes ribbon
        to open the MP ontology annotations page you find strains in the genetic background column link to their strain detail page.
        @note mrkdetail-allele-6
        '''
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pde6b")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pde6b').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        self.driver.find_element(By.ID, 'phenoMultigenicLink').click()
        #Find the link in the Genetic Background column C57BL/6J-Pde6b<rd1-2J> Pde6a<nmf363>and click it
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'C57BL/6J-Pde6brd1-2J').click()
        #time.sleep(2)
        #switch focus to the new tab for strain detail page
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #time.sleep(2)
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        print(page_title.text)
        #Asserts that the strain page is for the correct strain
        self.assertEqual(page_title.text, 'C57BL/6J-Pde6brd1-2J Pde6anmf363', 'Page title is not correct!')

    def test_mpontology_annot_strain_links3(self):
        '''
        @status this test verifies when you click one of the blue cells in the phenoslim grid from the Mutations, Alleles, and Phenotypes ribbon
        to open the Phenotype annotations related to page, then click a Mouse Genotype to find strains in the genetic background column link to their strain detail page(for Summary ribbon and for Genotype ribbon.
        @note mrkdetail-allele-7
        '''
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Sry")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Sry').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'summaryRibbon')))#waits until the summary ribbon is displayed on the page
        #locates the phenogrid and click on the cell for reproductive System
        self.driver.find_element(By.ID, 'mpSlimgrid23Div').click()
        #pheno_table = Table(self.driver.find_element_by_id("mpSlimgridTable"))
        #pheno_table.get_cell(2, 21).click()
        #switch focus to the new tab for Phenotype annotations related to reproductive System
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #time.sleep(2)        
        #find and click the Mouse Genotype for X/Sry<AKR/J>
        self.driver.find_element(By.XPATH, '//*[@id="fm9638a"]').click()
        #switch focus to the new tab for Phenotypes associated with X/Sry<AKR/J>
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #time.sleep(2) 
        #Locate the Genetic Background column and click the link found there(Summary ribbon)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td[3]/a').click()
        #time.sleep(2) 
        #switch focus to the new tab for strain detail page
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #time.sleep(2)
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        print(page_title.text)
        #Asserts that the strain page is for the correct strain detail
        self.assertEqual(page_title.text, 'AKR/J', 'Page title is not correct!')
        #switch focus back to the tab for Phenotypes associated with X/Sry<AKR/J>
        self.driver.switch_to_window(self.driver.window_handles[+2])
        #time.sleep(8) 
        #Locate the Genetic Background strain in the genotype ribbon and click the link.
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/a').click()
        #time.sleep(2) 
        #switch focus to the new tab for strain detail page
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #time.sleep(2)
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        print(page_title.text)
        #Asserts that the strain page is for the correct strain detail
        self.assertEqual(page_title.text, 'AKR/J', 'Page title is not correct!')
                
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMarkerDetail))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.MarkerDetail']
    unittest.main()