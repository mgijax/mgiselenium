'''
Created on Apr 15, 2022

These tests use the short form of the Lit Triage module.

@author: jeffc
'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import HtmlTestRunner
import json
import sys, os.path

# from curses.ascii import TAB
# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table


# Tests

class TestEiLitTriageShortSearch(unittest.TestCase):
    """
    @status Test Literature Triage short form search using allele symbol, allele ID, Marker symbol, marker ID,
    strain symbol, strain ID
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/triageShort")

    def tearDown(self):
        self.driver.close()

    def testAlleleSymbolSearch(self):
        """
        @Status tests that searching by Allele symbol works
        @see LitTri-search-67
        @note: passed 4/18/2022
        """
        driver = self.driver
        # find the Allele Associations button and click it
        driver.find_element(By.ID, 'alleleTabButton').click()
        # enter the allele symbol is the allele symbol field
        driver.find_element(By.CLASS_NAME, 'alleleSymbol').send_keys('Gata1<Plt13>')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # finds the results table and iterates through the table
        result = self.driver.find_element(By.ID, "resultsTable")
        data = result.find_elements(By.TAG_NAME, "td")
        print(iterate.getTextAsList(data))
        # finds the MGI field
        mgiid = data[1].text
        self.assertEqual(mgiid, 'MGI:3836492')
        # finds the J number field
        Jnumber = data[2].text
        self.assertEqual(Jnumber, 'J:145995')
        # finds the pmid by field
        PubMedID = data[3].text
        self.assertEqual(PubMedID, '19109561')
        # finds the DOI field
        doi = data[4].text
        self.assertEqual(doi, '10.1182/blood-2008-06-161422')
        # finds the short citation field
        ShortCite = data[5].text
        self.assertEqual(ShortCite, 'Carmichael CL, Blood 2009 Feb 26;113(9):1929-37')
        # finds the title field
        Title = data[6].text
        self.assertEqual(Title, 'Hematopoietic defects in the Ts1Cje mouse model of Down syndrome.')
        # finds the MGI field(line2)
        mgiid1 = data[14].text
        self.assertEqual(mgiid1, 'MGI:3687579')
        # finds the J number field(line2)
        Jnumber1 = data[15].text
        self.assertEqual(Jnumber1, 'J:113720')
        # finds the pmid by field(line2)
        PubMedID1 = data[16].text
        self.assertEqual(PubMedID1, '16966598')
        # finds the Journal field(line2)
        doi1 = data[17].text
        self.assertEqual(doi1, '10.1073/pnas.0606439103')
        # finds the short citation field(line2)
        ShortCite1 = data[18].text
        self.assertEqual(ShortCite1, 'Majewski IJ, Proc Natl Acad Sci U S A 2006 Sep 19;103(38):14146-51')
        # finds the title field(line2)
        Title1 = data[19].text
        self.assertEqual(Title1,
                         'A mutation in the translation initiation codon of Gata-1 disrupts megakaryocyte maturation and causes thrombocytopenia.')

    def testMarkerSymbolSearch(self):
        """
        @Status tests that a search by marker symbol using marker association tab field works
        @See LitTri-search-68
        @note: passed 04/18/2022
        """
        driver = self.driver
        # find the Marker Associations button and click it
        driver.find_element(By.ID, 'markerTabButton').click()
        # enter the allele symbol is the allele symbol field
        driver.find_element(By.ID, 'markerSymbol').send_keys('Il27ra')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        # finds the results table and iterates through the table
        result = self.driver.find_element(By.ID, "resultsTable")
        data = result.find_elements(By.TAG_NAME, "td")
        print(iterate.getTextAsList(data))
        # finds the MGI field
        mgiid = data[1].text
        self.assertEqual(mgiid, 'MGI:6727238')
        # finds the J number field
        Jnumber = data[2].text
        self.assertEqual(Jnumber, 'J:331147')
        # finds the pmid by field
        PubMedID = data[3].text
        self.assertEqual(PubMedID, '33863788')
        # finds the DOI field
        doi = data[4].text
        self.assertEqual(doi, '10.4049/jimmunol.2000957')
        # finds the short citation field
        ShortCite = data[5].text
        self.assertEqual(ShortCite, 'Zha X, J Immunol 2021 May 1;206(9):2160-2169')
        # finds the title field
        Title = data[6].text
        self.assertEqual(Title,
                         'IL-27/IL-27R Mediates Protective Immunity against Chlamydial Infection by Suppressing Excessive Th17 Responses and Reducing Neutrophil Inflammation.')
        # finds the MGI field(line2)
        mgiid1 = data[14].text
        self.assertEqual(mgiid1, 'MGI:7328884')
        # finds the J number field(line2)
        Jnumber1 = data[15].text
        self.assertEqual(Jnumber1, 'J:327180')
        # finds the pmid by field(line2)
        PubMedID1 = data[16].text
        self.assertEqual(PubMedID1, '35723626')
        # finds the Journal field(line2)
        doi1 = data[17].text
        self.assertEqual(doi1, '10.1158/2159-8290.CD-20-1628')
        # finds the short citation field(line2)
        ShortCite1 = data[18].text
        self.assertEqual(ShortCite1, 'Aghayev T, Cancer Discov 2022 Aug 5;12(8):1960-1983')
        # finds the title field(line2)
        Title1 = data[19].text
        self.assertEqual(Title1,
                         'IL27 Signaling Serves as an Immunologic Checkpoint for Innate Cytotoxic Cells to Promote Hepatocellular Carcinoma.')

    def testStrainSymbolSearch(self):
        """
        @Status tests that a search by strain symbol using strain association tab field works
        @See LitTri-search-69
        @note: passed 04/18/2022
        """
        driver = self.driver
        # find the Marker Associations button and click it
        driver.find_element(By.ID, 'strainTabButton').click()
        # enter the allele symbol is the allele symbol field
        driver.find_element(By.ID, 'strainSymbol').send_keys('STOCK In(13)31Rk/J')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        # finds the results table and iterates through the table
        result = self.driver.find_element(By.ID, "resultsTable")
        data = result.find_elements(By.TAG_NAME, "td")
        print(iterate.getTextAsList(data))
        # finds the MGI field
        mgiid = data[1].text
        self.assertEqual(mgiid, 'MGI:1277880')
        # finds the J number field
        Jnumber = data[2].text
        self.assertEqual(Jnumber, 'J:43743')
        # finds the pmid by field
        PubMedID = data[3].text
        self.assertEqual(PubMedID, '')
        # finds the DOI field
        doi = data[4].text
        self.assertEqual(doi, '')
        # finds the short citation field
        ShortCite = data[5].text
        self.assertEqual(ShortCite, 'Lyon MF, 1996;():')
        # finds the title field
        Title = data[6].text
        self.assertEqual(Title, 'Genetic Variants and Strains of the Laboratory Mouse')
        # finds the MGI field(line2)
        mgiid1 = data[14].text
        self.assertEqual(mgiid1, 'MGI:71289')
        # finds the J number field(line2)
        Jnumber1 = data[15].text
        self.assertEqual(Jnumber1, 'J:23389')
        # finds the pmid by field(line2)
        PubMedID1 = data[16].text
        self.assertEqual(PubMedID1, '')
        # finds the Journal field(line2)
        doi1 = data[17].text
        self.assertEqual(doi1, '')
        # finds the short citation field(line2)
        ShortCite1 = data[18].text
        self.assertEqual(ShortCite1, 'Roderick TH, 1983;():135-67')
        # finds the title field(line2)
        Title1 = data[19].text
        self.assertEqual(Title1, 'Using inversions to detect and study recessive lethals and detrimentals in mice')

    def testJnumAlleleSymbolSearch(self):
        """
        @Status tests that a search by J number and Allele Symbol works
        @See LitTri-search-70
        @note: passed 04/18/2022
        """
        driver = self.driver
        # find the Accession IDs field and enter the J number
        driver.find_element(By.ID, 'accids').send_keys('J:284955')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # find the Allele Associations button and click it
        driver.find_element(By.ID, 'alleleTabButton').click()
        # enter the allele symbol is the allele symbol field
        driver.find_element(By.CLASS_NAME, 'alleleSymbol').send_keys('Sirt6<tm1Fwa>')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        # finds the results table and iterates through the table
        result = self.driver.find_element(By.ID, "resultsTable")
        data = result.find_elements(By.TAG_NAME, "td")
        print(iterate.getTextAsList(data))
        # finds the MGI field
        mgiid = data[1].text
        self.assertEqual(mgiid, 'MGI:6384955')
        # finds the J number field
        Jnumber = data[2].text
        self.assertEqual(Jnumber, 'J:284955')
        # finds the pmid by field
        PubMedID = data[3].text
        self.assertEqual(PubMedID, '31744885')
        # finds the DOI field
        doi = data[4].text
        self.assertEqual(doi, '10.1074/jbc.RA118.007212')
        # finds the short citation field
        ShortCite = data[5].text
        self.assertEqual(ShortCite, 'Maity S, J Biol Chem 2020 Jan 10;295(2):415-434')
        # finds the title field
        Title = data[6].text
        self.assertEqual(Title,
                         'Sirtuin 6 deficiency transcriptionally up-regulates TGF-beta signaling and induces fibrosis in mice.')

    def testJnumMarkerSymbolSearch(self):
        """
        @Status tests that a search by J number and Marker Symbol works
        @See LitTri-search-71
        @note: passed 04/18/2022
        """
        driver = self.driver
        # find the Accession IDs field and enter the J number
        driver.find_element(By.ID, 'accids').send_keys('J:23349')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # find the Marker Associations button and click it
        driver.find_element(By.ID, 'markerTabButton').click()
        # enter the marker symbol is the marker symbol field
        driver.find_element(By.ID, 'markerSymbol').send_keys('Gnb2')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        # finds the results table and iterates through the table
        result = self.driver.find_element(By.ID, "resultsTable")
        data = result.find_elements(By.TAG_NAME, "td")
        print(iterate.getTextAsList(data))
        # finds the MGI field
        mgiid = data[1].text
        self.assertEqual(mgiid, 'MGI:71603')
        # finds the J number field
        Jnumber = data[2].text
        self.assertEqual(Jnumber, 'J:23349')
        # finds the pmid by field
        PubMedID = data[3].text
        self.assertEqual(PubMedID, '1372395')
        # finds the DOI field
        doi = data[4].text
        self.assertEqual(doi, '10.1038/356340a0')
        # finds the short citation field
        ShortCite = data[5].text
        self.assertEqual(ShortCite, 'Clark SG, Nature 1992 Mar 26;356(6367):340-4')
        # finds the title field
        Title = data[6].text
        self.assertEqual(Title,
                         'C. elegans cell-signalling gene sem-5 encodes a protein with SH2 and SH3 domains [see comments]')

    def testJnumStrainSymbolSearch(self):
        """
        @Status tests that a search by J number and Strain Symbol works
        @See LitTri-search-72
        @note: passed 04/18/2022
        """
        driver = self.driver
        # find the Accession IDs field and enter the J number
        driver.find_element(By.ID, 'accids').send_keys('J:109968')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # find the Strain Associations button and click it
        driver.find_element(By.ID, 'strainTabButton').click()
        # enter the strain symbol is the strain symbol field
        driver.find_element(By.ID, 'strainSymbol').send_keys('STOCK In(5)2Rk/J')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        # finds the results table and iterates through the table
        result = self.driver.find_element(By.ID, "resultsTable")
        data = result.find_elements(By.TAG_NAME, "td")
        print(iterate.getTextAsList(data))
        # finds the MGI field
        mgiid = data[1].text
        self.assertEqual(mgiid, 'MGI:3630144')
        # finds the J number field
        Jnumber = data[2].text
        self.assertEqual(Jnumber, 'J:109968')
        # finds the pmid by field
        PubMedID = data[3].text
        self.assertEqual(PubMedID, '4361911')
        # finds the DOI field
        doi = data[4].text
        self.assertEqual(doi, '')
        # finds the short citation field
        ShortCite = data[5].text
        self.assertEqual(ShortCite, 'Roderick TH, Genetics 1974 Jan;76(1):109-17')
        # finds the title field
        Title = data[6].text
        self.assertEqual(Title, 'Nineteen paracentric chromosomal inversions in mice.')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiLitTriageShortSearch))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))