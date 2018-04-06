'''
Created on Oct 20, 2016

@author: jeffc
This suite of tests are for marker detail pages
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
from util import wait, iterate
from util.table import Table
import config
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
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Gata1")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_link_text("Gata1").click()
        time.sleep(2)
        summaryRibbon = self.driver.find_element_by_css_selector("div.row > div.header.detailCat1")
        print summaryRibbon.text
        self.assertEqual(summaryRibbon.text, 'Summary', "Summary ribbon is missing")
        locationribbon = self.driver.find_element_by_css_selector("div.row.locationRibbon > div.header.detailCat2")
        self.assertEqual(locationribbon.text, "Location & Maps", "Locations & Maps ribbon is missing")
        homologyRibbon = self.driver.find_element_by_css_selector("div:nth-child(3).row > div.header.detailCat1")
        print homologyRibbon.text
        self.assertEqual(homologyRibbon.text, 'Homology', "Homology ribbon is missing")
        diseaseribbon = self.driver.find_element_by_css_selector("div.row.diseaseRibbon > div.header.detailCat2")
        self.assertEqual(diseaseribbon.text, "Human Diseases", "Human Diseases ribbon is missing")
        phenoribbon = self.driver.find_element_by_css_selector("div.row.phenoRibbon > div.header.detailCat1")
        print phenoribbon.text
        self.assertEqual(phenoribbon.text, "Mutations,\nAlleles, and\nPhenotypes", "Phenotype ribbon is missing")
        goribbon = self.driver.find_element_by_css_selector("div.row.goRibbon > div.header.detailCat2")
        print goribbon.text
        self.assertEqual(goribbon.text, "Gene Ontology\n(GO)\nClassifications", "GO ribbon is missing")
        gxdribbon = self.driver.find_element_by_css_selector("div.row.gxdRibbon > div.header.detailCat1")
        print gxdribbon.text
        self.assertEqual(gxdribbon.text, "Expression", "Expression ribbon is missing")
        interactionsRibbon = self.driver.find_element_by_css_selector("div:nth-child(8).row > div.header.detailCat2")
        print interactionsRibbon.text
        self.assertEqual(interactionsRibbon.text, 'Interactions', "Interactions ribbon is missing")
        sequenceribbon = self.driver.find_element_by_css_selector("div.row.sequenceRibbon > div.header.detailCat1")
        print sequenceribbon.text
        self.assertEqual(sequenceribbon.text, "Sequences &\nGene Models", "Sequence ribbon is missing")
        polymorphismsRibbon = self.driver.find_element_by_css_selector("div:nth-child(11).row > div.header.detailCat2")
        print polymorphismsRibbon.text
        self.assertEqual(polymorphismsRibbon.text, 'Polymorphisms', "Polymorphisms ribbon is missing")
        proteinribbon = self.driver.find_element_by_css_selector("div.row.proteinRibbon > div.header.detailCat1")
        print proteinribbon.text
        self.assertEqual(proteinribbon.text, "Protein\nInformation", "Protein Information ribbon is missing")
        molecularRibbon = self.driver.find_element_by_css_selector("div:nth-child(13).row > div.header.detailCat2")
        print molecularRibbon.text
        self.assertEqual(molecularRibbon.text, 'Molecular\nReagents', "Molecular Reagents ribbon is missing")
        otherRibbon = self.driver.find_element_by_css_selector("div:nth-child(14).row > div.header.detailCat1")
        print otherRibbon.text
        self.assertEqual(otherRibbon.text, 'Other\nAccession IDs', "Other Accession IDs ribbon is missing")
        referencesRibbon = self.driver.find_element_by_css_selector("div:nth-child(15).row > div.header.detailCat2")
        print referencesRibbon.text
        self.assertEqual(referencesRibbon.text, 'References', "References ribbon is missing")
        
    def test_turnstile_behavior(self):
        '''
        @status this test verifies In the Human Diseases section, confirm there are turnstile icons for showing more data
        and clicking the turnstile icon displays the complete Human Diseases table.
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Shh")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_link_text('Shh').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element_by_css_selector("div.row.diseaseRibbon > div.detail.detailData2 > div.toggleImage.hdExpand").click()
        time.sleep(2)
        diseasetable = self.driver.find_element_by_id('humanDiseaseTable')
        self.assertTrue(diseasetable.is_displayed())
    
    def test_disease_tbl_doids(self):
        '''
        @status this test verifies that the disease table in the Human Diseases ribbon now displays the DOID beside
         each disease instead of the OMIM ID
         @bug need to ask Olin why would only certain diseases get captured from the table?
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Ins2")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_link_text('Ins2').click()
        time.sleep(8)#long timeout to compensate for intermittent lagging
        #clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element_by_css_selector("div.row.diseaseRibbon > div.detail.detailData2 > div.toggleImage.hdExpand").click()
        time.sleep(2)
        disease_table = self.driver.find_element_by_id('humanDiseaseTable')
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
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Alad")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_link_text('Alad').click()
        apflnk = self.driver.find_element_by_link_text('APF')
        href = apflnk.find_element_by_xpath("//a").get_attribute('href')
        
        self.assertTrue(href, "https://databases.apf.edu.au/mutations/snpRow/list?mgiAccessionid=MGI:96853")
        
        '''
    def test_????(self):
        
        @status this is just a placeholder test for now.
        @bug: under construction
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Tgm3")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('tm1Sjo').click()
        
        image = self.driver.find_element_by_id('mutationDescriptionTable').find_element_by_css_selector('a img')
        self.assertTrue(image.is_displayed(), 'the image is not displaying')
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Dock2")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('Hsd').click()
        
        image = self.driver.find_element_by_id('mutationDescriptionTable').find_element_by_css_selector('a img')
        self.assertTrue(image.is_displayed(), 'the image is not displaying')
        
        
    def test_???(self):
        
        @status this is just a placeholder test for now
        @bug under construction
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Blnk")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('m1Btlr').click()
        mutagenetixlink = self.driver.find_element_by_link_text('incidental mutations')
        actualurl = self.driver.find_element_by_link_text('incidental mutations').get_attribute("href")
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, config.WI_URL + '/downloads/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Irf7")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('m1Btlr').click()
        mutagenetixlink = self.driver.find_element_by_link_text('incidental mutations')
        actualurl = self.driver.find_element_by_link_text('incidental mutations').get_attribute("href")
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, config.WI_URL + '/downloads/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.FEWI_URL + "/allele/")
            
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Col4a4")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('m1Btlr').click()
        mutagenetixlink = self.driver.find_element_by_link_text('incidental mutations')
        actualurl = self.driver.find_element_by_link_text('incidental mutations').get_attribute("href")
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, config.WI_URL + '/downloads/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Nfkbid")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('m1Btlr').click()
        mutagenetixlink = self.driver.find_element_by_link_text('incidental mutations')
        actualurl = self.driver.find_element_by_link_text('incidental mutations').get_attribute("href")
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, config.WI_URL + '/downloads/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Unc93b1")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('3d').click()
        mutagenetixlink = self.driver.find_element_by_link_text('incidental mutations')
        actualurl = self.driver.find_element_by_link_text('incidental mutations').get_attribute("href")
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, config.WI_URL + '/downloads/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.FEWI_URL + "/allele/")
    
    def test_???(self):
        
        @status this is just a placeholder test for now
        @bug: This page needs the table to have an ID before a test can really be written
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Stk11")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('tm1.1Jish').click()
        
        caption = self.driver.find_element_by_id('mutationDescriptionTable').find_element_by_css_selector('span.small')
        self.assertTrue(caption.is_displayed(), 'the caption is not displaying')
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Supv3l1")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('tm2.1Jkl').click()
        
        caption = self.driver.find_element_by_id('mutationDescriptionTable').find_element_by_css_selector('span')
        self.assertTrue(caption.is_displayed(), 'the caption is not displaying')
        self.driver.get(config.FEWI_URL + "/allele/")
        
        #6.The correct image/caption is displayed to the left of the molecular image in the molecular description ribbon when more than one thumbnail exists for an allele.
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Dock2")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('Hsd').click()
        
        caption = self.driver.find_element_by_id('mutationDescriptionTable').find_element_by_css_selector('span')
        self.assertEquals(caption.text, 'Schematic showing the duplication and location of the premature stop codon in the Dock2<mu> allele found in Irf5<tm1Ttg>/Irf5<tm1Ttg> mice')
        '''
        

        
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()