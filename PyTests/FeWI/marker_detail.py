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

class Test(unittest.TestCase):


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
        
    def test_turnstile_behavior(self):
        '''
        @status this test verifies In the Human Diseases section, confirm there are turnstile icons for showing more data
        and clicking the turnstile icon displays the complete Human Diseases table.
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
        
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()