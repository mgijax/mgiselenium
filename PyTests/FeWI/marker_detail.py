'''
Created on Oct 20, 2016

@author: jeffc
This suite of tests are for marker detail pages
'''
import unittest
import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

import sys,os.path
#from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
from util import wait, iterate
from util.table import Table
import config
from selenium.webdriver.common.by import By
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
        summaryRibbon = self.driver.find_element(By.CSS_SELECTOR, 'div.row > div.header.detailCat1')
        print summaryRibbon.text
        self.assertEqual(summaryRibbon.text, 'Summary', "Summary ribbon is missing")
        locationribbon = self.driver.find_element(By.CSS_SELECTOR, 'div.row.locationRibbon > div.header.detailCat2')
        self.assertEqual(locationribbon.text, "Genome Context & Strain Distribution", "Genome Context & Strain Distribution ribbon is missing")
        homologyRibbon = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(3).row > div.header.detailCat1')
        print homologyRibbon.text
        self.assertEqual(homologyRibbon.text, 'Homology', "Homology ribbon is missing")
        diseaseribbon = self.driver.find_element(By.CSS_SELECTOR, 'div.row.diseaseRibbon > div.header.detailCat2')
        self.assertEqual(diseaseribbon.text, "Human Diseases", "Human Diseases ribbon is missing")
        phenoribbon = self.driver.find_element(By.CSS_SELECTOR, 'div.row.phenoRibbon > div.header.detailCat1')
        print phenoribbon.text
        self.assertEqual(phenoribbon.text, "Mutations,\nAlleles, and\nPhenotypes", "Phenotype ribbon is missing")
        goribbon = self.driver.find_element(By.CSS_SELECTOR, 'div.row.goRibbon > div.header.detailCat2')
        print goribbon.text
        self.assertEqual(goribbon.text, "Gene Ontology\n(GO)\nClassifications", "GO ribbon is missing")
        gxdribbon = self.driver.find_element(By.CSS_SELECTOR, 'div.row.gxdRibbon > div.header.detailCat1')
        print gxdribbon.text
        self.assertEqual(gxdribbon.text, "Expression", "Expression ribbon is missing")
        interactionsRibbon = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(8).row > div.header.detailCat2')
        print interactionsRibbon.text
        self.assertEqual(interactionsRibbon.text, 'Interactions', "Interactions ribbon is missing")
        sequenceribbon = self.driver.find_element(By.CSS_SELECTOR, 'div.row.sequenceRibbon > div.header.detailCat1')
        print sequenceribbon.text
        self.assertEqual(sequenceribbon.text, "Sequences &\nGene Models", "Sequence ribbon is missing")
        polymorphismsRibbon = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(11).row > div.header.detailCat2')
        print polymorphismsRibbon.text
        self.assertEqual(polymorphismsRibbon.text, 'Polymorphisms', "Polymorphisms ribbon is missing")
        proteinribbon = self.driver.find_element(By.CSS_SELECTOR, 'div.row.proteinRibbon > div.header.detailCat1')
        print proteinribbon.text
        self.assertEqual(proteinribbon.text, "Protein\nInformation", "Protein Information ribbon is missing")
        molecularRibbon = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(13).row > div.header.detailCat2')
        print molecularRibbon.text
        self.assertEqual(molecularRibbon.text, 'Molecular\nReagents', "Molecular Reagents ribbon is missing")
        otherRibbon = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(14).row > div.header.detailCat1')
        print otherRibbon.text
        self.assertEqual(otherRibbon.text, 'Other\nAccession IDs', "Other Accession IDs ribbon is missing")
        referencesRibbon = self.driver.find_element(By.CSS_SELECTOR, 'div:nth-child(15).row > div.header.detailCat2')
        print referencesRibbon.text
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
        @status this test verifies that a list of TSS sites  is displayed in the summary section of certain detail pages
        @note the sites should be displayed by coordinate order
        @note mrkdetail-sum-1, 2
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Vwa3b")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Vwa3b').click()
        #Find the first 3 TSS site ID     
        tss_sites1 = self.driver.find_element(By.XPATH, '//*[@id="templateBodyInsert"]/div[2]/div[1]/div[2]/section[2]/ul/li[4]/div[2]/a[1]')
        print tss_sites1.text
        tss_sites2 = self.driver.find_element(By.XPATH, '//*[@id="templateBodyInsert"]/div[2]/div[1]/div[2]/section[2]/ul/li[4]/div[2]/a[2]')
        print tss_sites2.text
        tss_sites3 = self.driver.find_element(By.XPATH, '//*[@id="templateBodyInsert"]/div[2]/div[1]/div[2]/section[2]/ul/li[4]/div[2]/a[3]')
        print tss_sites3.text
        self.assertEqual(tss_sites1.text, 'Tssr6295', 'The first TSS id is not correct!')
        self.assertEqual(tss_sites2.text, 'Tssr6296', 'The second TSS id is not correct!')
        self.assertEqual(tss_sites3.text, 'Tssr6297', 'The third TSS id is not correct!')
        
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
        self.assertEquals(loc_cells[2], 'Chr1:9797812-9797823 (+)')
        self.assertEquals(loc_cells[3], 'Chr1:9797986-9798040 (+)')
        self.assertEquals(loc_cells[4], 'Chr1:9798123-9798216 (+)')
        self.assertEquals(loc_cells[5], 'Chr1:9848270-9848285 (+)') 
        self.assertEquals(loc_cells[6], 'Chr1:9848294-9848362 (+)')
        self.assertEquals(loc_cells[7], 'Chr1:9848375-9848398 (+)')       
        #Iterate the table Distance from Gene 5' -end column
        cells = table.get_column_cells("Distance from Gene 5'-end")
        loc_cells = iterate.getTextAsList(cells)      
        #Verify the TSS table Distance are correct and in the correct order.
        self.assertEqual(loc_cells[1], '-305 bp')
        self.assertEquals(loc_cells[2], '-289 bp')
        self.assertEquals(loc_cells[3], '-94 bp')
        self.assertEquals(loc_cells[4], '63 bp')
        self.assertEquals(loc_cells[5], '50,171 bp') 
        self.assertEquals(loc_cells[6], '50,221 bp')
        self.assertEquals(loc_cells[7], '50,280 bp')        

    def test_tss_detail_link(self):
        '''
        @status this test verifies clicking a Tss site ID takes you to it's detail page
        @note mrkdetail-sum-4
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Carf")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Carf').click()        
        #Find the TSS link for Tssr6917 and click it
        self.driver.find_element(By.LINK_TEXT, 'Tssr6917').click()
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        #Assert that the page title is for TSS Tssr6917
        self.assertEquals(page_title.text, 'Tssr6917')      

    def test_strain_table_headings(self):
        '''        
        @status this test verifies the strain table headings in the Genome Context & Strain Distribution ribbon are correctly ordered/displayed.
        @note mrkdetail-loc-1
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ren1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ren1').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.locationRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
        time.sleep(2)
        strain_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strain_table)
        #Iterate and print the table headers
        cells = table.get_header_cells()
        header_cells = iterate.getTextAsList(cells)      
        #Verify the strain table headers are correct.
        self.assertEqual(header_cells[0], 'Strain')
        self.assertEquals(header_cells[1], 'Gene Model ID')
        self.assertEquals(header_cells[2], 'Feature Type')
        self.assertEquals(header_cells[3], 'Coordinates')
        self.assertEquals(header_cells[4], 'Downloads')        

    def test_strain_no_annot(self):
        '''        
        @status this test verifies the strain table results in the Genome Context & Strain Distribution ribbon when strains have no annotation.
        @note mrkdetail-loc-2
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ren1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ren1').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.locationRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
        time.sleep(2)
        strain_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strain_table)
        #Iterate and print the table headers
        header_cells = table.get_header_cells()
        print iterate.getTextAsList(header_cells)
        
        # print all the results in the Gene Model ID column
        cells = table.get_column_cells("Gene Model ID")
        gmodel_cells = iterate.getTextAsList(cells)
        print gmodel_cells
        #Verify the first 5 results are correct. When a strain  has no results print 'no annotaions' in this field.
        self.assertEquals(gmodel_cells[1], 'ENSMUSG00000070645\n19701')
        self.assertEquals(gmodel_cells[2], 'no annotation')
        self.assertEquals(gmodel_cells[3], 'no annotation')
        self.assertEquals(gmodel_cells[4], 'no annotation')
        self.assertEquals(gmodel_cells[5], 'MGP_BALBcJ_G0016428')

    def test_strain_turnstile_closed(self):
        '''        
        @status this test verifies the Genome Context & Strain Distribution ribbon when the turnstile is closed shows B6 coordinates and genetic map location.
        @note mrkdetail-loc-3
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ren1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ren1').click()
        #locate the Sequence map information
        seq_map = self.driver.find_element(By.CSS_SELECTOR, 'div.detail.detailData2 > section.summarySec1 > ul > li > div.value')
        print seq_map.text
        #verify the sequence map information is correct
        self.assertEqual(seq_map.text, 'Chr1:133350510-133360325 bp, + strand')
        #locate the genetic map information
        gen_map = self.driver.find_element(By.CSS_SELECTOR, 'div.detail.detailData2 > section.summarySec2 > ul > li > div.value')
        print gen_map.text
        #verify the genetic map information is correct
        self.assertEqual(gen_map.text, 'Chromosome 1, 57.91 cM')

    def test_strain_turnstile_closed_nob6(self):
        '''        
        @status this test verifies the Genome Context & Strain Distribution ribbon when the turnstile is closed with no B6 coordinates and has genetic map location.
        @note mrkdetail-loc-4
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ren2")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ren2').click()
        #locate the Sequence map information
        seq_map = self.driver.find_element(By.CSS_SELECTOR, 'div.detail.detailData2 > section.summarySec1 > ul > li > div.value')
        print seq_map.text
        #verify the sequence map information is correct
        self.assertEqual(seq_map.text, 'Genome coordinates not available')
        #locate the genetic map information
        gen_map = self.driver.find_element(By.CSS_SELECTOR, 'div.detail.detailData2 > section.summarySec2 > ul > li > div.value')
        print gen_map.text
        #verify the genetic map information is correct
        self.assertEqual(gen_map.text, 'Chromosome 1, Syntenic')

    def test_mgv_link_exists(self):
        '''        
        @status this test verifies the Multiple Genome Viewer(MGV) link when B6 coordinates exist.
        @note mrkdetail-loc-5
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ren1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ren1').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #clicks the More toggle(turnstile) to display the strain distribution data
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.locationRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
        time.sleep(2)
        #locate the MGV link
        mgv = self.driver.find_element(By.LINK_TEXT, 'Multiple Genome Viewer (MGV)')
        print mgv.text
        #verify the MGV link is correct
        self.assertEqual(mgv.text, 'Multiple Genome Viewer (MGV)', 'The MGV link is missing!')
        
    def test_mgv_link_not_exist(self):
        '''        
        @status this test verifies the MGV link does not exist when no B6 coordinates exist.
        @note mrkdetail-loc-5
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ren2")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ren2').click()
        #locate the Sequence map information
        seq_map = self.driver.find_element(By.CSS_SELECTOR, 'div.detail.detailData2 > section.summarySec1 > ul > li > div.value')
        print seq_map.text
        #verify the MGV link does not exist
        assert 'Multiple Genome Viewer (MGV)' not in self.driver.page_source 

    def test_mgv_link_10kb_flank(self):
        '''        
        @status this test verifies the Multiple Genome Viewer(MGV) has 10kb flanking on each end of the sequence link URL.
        @note mrkdetail-loc-6
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ren1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ren1').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #clicks the More toggle(turnstile) to display the strain distribution data
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.locationRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
        time.sleep(2)
        #locates all Href links on the page
        elems = self.driver.find_elements(By.XPATH, '//a[@href]')
        for elem in elems:
            print elem.get_attribute('href')      
        print elems[113].get_attribute('href')
        #verify the MGV link href is correct(the 10KB flanking added is in the url)
        self.assertEqual(elems[113].get_attribute('href'), 'http://proto.informatics.jax.org/prototypes/mgv/#ref=C57BL/6J&genomes=C57BL/6J+129S1/SvImJ+A/J+AKR/J+BALB/cJ+C3H/HeJ+C57BL/6NJ+CAROLI/EIJ+CAST/EiJ+CBA/J+DBA/2J+FVB/NJ+LP/J+NOD/ShiLtJ+NZO/HlLtJ+PAHARI/EIJ+PWK/PhJ+SPRET/EiJ+WSB/EiJ&chr=1&start=133340510&end=133370325&highlight=MGI:97898', 'The MGV link href flanking is incorrect!')

    def test_strain_table_genemodelid_links(self):
        '''        
        @status this test verifies that the Gene Model IDs in the strains table link to their MGI gene model sequence, found in the Genome Context ribbon. (only verifying 1 link of 18)
        @note mrkdetail-loc-9
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Gata1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Gata1').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.locationRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
        time.sleep(2)
        #find the link for C57BL/6J gene model id
        self.driver.find_element(By.LINK_TEXT, 'MGI_C57BL6J_95661').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(2)
        structure_table = self.driver.find_element(By.CLASS_NAME, 'detailStructureTable')
        table = Table(structure_table)
        #Iterate the second row of the disease table
        all_cells = table.get_row('ID/Version')
        print all_cells.text
        #verify the ID/Version row of data
        self.assertEqual(all_cells.text, 'ID/Version\nMGI_C57BL6J_95661 () Version: MGI_C57BL6J_95661.GRCm38')
        #switch focus back to the Gene Detail page
        self.driver.switch_to_window(self.driver.window_handles[0])
        #find the link for 129S1/SvImJ gene model id
        self.driver.find_element(By.LINK_TEXT, 'MGP_129S1SvImJ_G0035536').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(2)
        structure_table = self.driver.find_element(By.CLASS_NAME, 'detailStructureTable')
        table = Table(structure_table)
        #Iterate the second row of the disease table
        all_cells = table.get_row('ID/Version')
        print all_cells.text
        #verify the ID/Version row of data
        self.assertEqual(all_cells.text, 'ID/Version\nMGP_129S1SvImJ_G0035536 () Version: MGP_129S1SvImJ_G0035536.MGP Release 91')

    def test_strain_table_vs_seqmap_noB6(self):
        '''        
        @status this test verifies that when a canonical gene doesn't have a B6 strain gene then the strain table for C57BL/6J says "no annotation"
        @note mrkdetail-loc-10
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ppnr")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ppnr').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #locate the Sequence Map coordinates
        seq_map = self.driver.find_element(By.XPATH, '//*[@id="templateBodyInsert"]/div[2]/div[2]/div[2]/section[1]/ul/li[1]/div[2]')
        print seq_map.text
        #verify the coordinates data for the sequence map
        self.assertEqual(seq_map.text, 'Chr19:55841672-55845897 bp, + strand', 'sequence map coordinates have changed!')
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.locationRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
        #find the coordinates column of the strains table
        time.sleep(2)
        strains_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strains_table)
        #Iterate the second row of the disease table
        all_cells = table.get_column_cells('Gene Model ID')
        print all_cells[1].text
        #verify the ID/Version row of data
        self.assertEqual(all_cells[1].text, 'no annotation')
        
    def test_strain_table_vs_seqmap_nomatch(self):
        '''        
        @status this test verifies that the sequence map coordinates do not match the strains table C57BL/6J coordinates when the gene model is not MGI
        @note mrkdetail-loc-11 *this test will go away when we stop using the reference B6 models
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pax6').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #locate the Sequence Map coordinates
        seq_map = self.driver.find_element(By.XPATH, '//*[@id="templateBodyInsert"]/div[2]/div[2]/div[2]/section[1]/ul/li[1]/div[2]')
        print seq_map.text
        #verify the coordinates data for the sequence map
        self.assertEqual(seq_map.text, 'Chr2:105668900-105697364 bp, + strand', 'sequence map coordinates have changed!')
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.locationRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
        #find the coordinates column of the strains table
        time.sleep(2)
        strains_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strains_table)
        #Iterate the second row of the disease table
        all_cells = table.get_column_cells('Coordinates')
        print all_cells[1].text
        #verify the ID/Version row of data
        self.assertEqual(all_cells[1].text, 'Chr2:105668896-105698410 (+)')
        
    def test_strain_table_vs_seqmap_match(self):
        '''        
        @status this test verifies that the sequence map coordinates match the strains table C57BL/6J coordinates when the gene model is MGI
        @note mrkdetail-loc-12 
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Gata1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Gata1').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #locate the Sequence Map coordinates
        seq_map = self.driver.find_element(By.XPATH, '//*[@id="templateBodyInsert"]/div[2]/div[2]/div[2]/section[1]/ul/li[1]/div[2]')
        print seq_map.text
        #verify the coordinates data for the sequence map
        self.assertEqual(seq_map.text, 'ChrX:7959260-7976682 bp, - strand', 'sequence map coordinates have changed!')
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.locationRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
        #find the coordinates column of the strains table
        time.sleep(2)
        strains_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strains_table)
        #Iterate the second row of the disease table
        all_cells = table.get_column_cells('Coordinates')
        print all_cells[1].text
        #verify the ID/Version row of data
        self.assertEqual(all_cells[1].text, 'ChrX:7959260-7976682 (-)')

    def test_strain_table_single_fasta(self):
        '''        
        @status this test verifies that you can download a single FASTA sequence from the Strain table using the download checkbox 
        @note mrkdetail-loc-14 
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ppnr")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ppnr').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.locationRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
        #time.sleep(2)
        #find and select the the Download box for the strain A/J
        self.driver.find_elements(By.CLASS_NAME, 'sgCheckbox')[1].click()
        #time.sleep(2)
        #find and click the 'Get FASTA' button
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
        @note mrkdetail-loc-15 
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pax6').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.locationRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
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
        @note mrkdetail-loc-16 
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Gata1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Gata1').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.locationRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
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
        @note mrkdetail-loc-12, 17 
        '''        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Zim3")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Zim3').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.locationRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
        #time.sleep(2)
        #find and click the 'Check All' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[1].click()
        #time.sleep(2)
        #find and click the 'Get FASTA' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[0].click()
        #time.sleep(2)
        #switch focus to the new tab for the FASTA results
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #time.sleep(2)
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
         
    def test_turnstile_behavior(self):
        '''
        @status this test verifies In the Human Diseases section, confirm there are turnstile icons for showing more data
        and clicking the turnstile icon displays the complete Human Diseases table.
        @note mrkdetail-hdisease-1
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Shh")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Shh').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.diseaseRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
        time.sleep(2)
        diseasetable = self.driver.find_element(By.ID, 'humanDiseaseTable')
        self.assertTrue(diseasetable.is_displayed())        

    def test_disease_tbl_doids(self):
        '''
        @status this test verifies that the disease table in the Human Diseases ribbon now displays the DOID beside
         each disease instead of the OMIM ID
         @bug need to ask Olin why would only certain diseases get captured from the table?
         @note mrkdetail-hdisease-2
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ins2")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ins2').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.diseaseRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
        time.sleep(2)
        disease_table = self.driver.find_element(By.ID, 'humanDiseaseTable')
        table = Table(disease_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print iterate.getTextAsList(header_cells)
        
        # print row 1
        cells = table.get_column_cells("Human Disease")
        disease_cells = iterate.getTextAsList(cells)
        print disease_cells
        self.assertEquals(disease_cells[1], 'permanent neonatal diabetes mellitus\nIDs')
        #self.assertEquals(disease_cells[2], 'maturity-onset diabetes of the young\nIDs')
        #self.assertEquals(disease_cells[3], 'type 1 diabetes mellitus\nIDs')
        #self.assertEquals(disease_cells[4], 'type 2 diabetes mellitus\nIDs')
        self.assertEquals(disease_cells[5], 'maturity-onset diabetes of the young type 10\nIDs')
                
    def test_mouse_model_strain_links(self):
        '''
        @status this test verifies In the Human Diseases section, from the Mouse Model popup strains in Genetic background link to their strain 
        detail page.
        @note mrkdetail-hdisease-3
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pde6b")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pde6b').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, 'div.row.diseaseRibbon > div.detail.detailData2 > div.toggleImage.hdExpand').click()
        time.sleep(5)
        self.driver.find_element(By.ID, 'showDOID_0110375').click()
        #switch focus to the popup page
        #self.driver.switch_to_window(self.driver.window_handles[-1])
        #Find the link in the Genetic Background column C57BL/6J-Tg(SNCA)ARyot and click it
        self.driver.find_element(By.LINK_TEXT, 'C3H/HeJ').click()
        time.sleep(2)
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
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pde6b")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pde6b').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        self.driver.find_element(By.ID, 'phenoAnnotationLink').click()
        #Find the link in the Genetic Background column C57BL/6J-Pde6b<rd1-2J>/J and click it
        self.driver.find_element(By.LINK_TEXT, 'C57BL/6J-Pde6brd1-2J/J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(2)
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        print page_title.text
        #Asserts that the strain page is for the correct strain
        self.assertEqual(page_title.text, 'C57BL/6J-Pde6brd1-2J/J', 'Page title is not correct!')

    def test_mpontology_annot_strain_links2(self):
        '''
        @status this test verifies when you click the Phenotype summary link(for multigenic genotypes) from the Mutations, Alleles, and Phenotypes ribbon
        to open the MP ontology annotations page you find strains in the genetic background column link to their strain detail page.
        @note mrkdetail-allele-6
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pde6b")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pde6b').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        self.driver.find_element(By.ID, 'phenoMultigenicLink').click()
        #Find the link in the Genetic Background column C57BL/6J-Pde6b<rd1-2J> Pde6a<nmf363>and click it
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'C57BL/6J-Pde6brd1-2J').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        self.driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(2)
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        print page_title.text
        #Asserts that the strain page is for the correct strain
        self.assertEqual(page_title.text, 'C57BL/6J-Pde6brd1-2J Pde6anmf363', 'Page title is not correct!')
                
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMarkerDetail))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.MarkerDetail']
    unittest.main()