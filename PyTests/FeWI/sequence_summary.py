'''
Created on Aug 5, 2016

This page is linked to from the Marker detail page
@author: jeffc
'''
import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys,os.path
from util import wait, iterate
from config.config import TEST_URL
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import TEST_URL

class TestSequenceSummaryPage(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
    def test_table_headers(self):
        """
        @status: Tests that the Sequence Summary table headers are correct
        Headers are: Select, Sequence, Type, Length, Strain/Species, Description from Sequence Provider, Clone Collection, Marker Symbol
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker")
        genebox = driver.find_element(By.NAME, 'nomen')
        # put your marker symbol
        genebox.send_keys("Bloc1s2")
        genebox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the correct marker link and clicks it
        driver.find_element(By.LINK_TEXT, 'Bloc1s2').click()
        time.sleep(2)
        #Finds the All sequences link and clicks it
        driver.find_element(By.ID, 'allSeqLink').click()
        wait.forAjax(driver)
        #Locates the marker header table and finds the table headings
        markerheaderlist = driver.find_element(By.CLASS_NAME, 'summaryHeaderCat1')
        items = markerheaderlist.find_elements(By.TAG_NAME, 'div')
        searchTextItems = iterate.getTextAsList(items)
        wait.forAjax(driver)
        #verifies all the table headings are correct and in order
        self.assertEqual(searchTextItems, ['Symbol','Name','ID'])
        wait.forAjax(driver)
        #Locates the sequence summary table and finds the table headings
        columnheaderlist = driver.find_elements(By.CLASS_NAME, 'yui-dt-label')
        searchTextItems = iterate.getTextAsList(columnheaderlist)
        wait.forAjax(driver)
        #verifies all the table headings are correct and in order
        self.assertEqual(searchTextItems, ['Select','Sequence','Type','Length','Strain/Species','Description From\nSequence Provider','Clone\nCollection','Marker\nSymbol'])

    def test_page_sort(self):
        """
        @status: Tests that the default page sort is correct for sequence summary by marker
        sort is by type, sequence provider, length
        """
        """
        @attention: While this test still works, it might need revisiting later to figure out a better way of confirming sort is correct
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker")
        genebox = driver.find_element(By.NAME, 'nomen')
        # put your marker symbol
        genebox.send_keys("Gabarap")
        genebox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the correct marker link and clicks it
        driver.find_element(By.LINK_TEXT, 'Gabarap').click()
        time.sleep(2)
        #Finds the All sequences link and clicks it
        driver.find_element(By.ID, 'allSeqLink').click()
        time.sleep(2)
        #finds the Type column and then iterates through all items
        seqtypelist = driver.find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-seqType .yui-dt-liner')
        searchTextItems = iterate.getTextAsList(seqtypelist)
        time.sleep(2)
        print(searchTextItems)
        #asserts that the rows of Type data are in correct order
        self.assertEqual(searchTextItems, ['RNA', 'RNA', 'RNA', 'RNA', 'RNA', 'RNA', 'RNA', 'RNA', 'RNA', 'RNA', 'RNA', 'RNA', 'RNA', 'RNA', 'RNA', 'DNA', 'DNA', 'DNA', 'DNA', 'DNA', 'DNA', 'DNA', 'DNA', 'DNA', 'DNA'])
        
        #finds the Sequence column and then iterates through all items
        seqlist = driver.find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-seqInfo .yui-dt-liner')
        searchTextItems = iterate.getTextAsList(seqlist)
        time.sleep(2)
        print(searchTextItems)
        #asserts that the rows of length data are in correct order
        self.assertEqual(searchTextItems, ['ENSMUST00000018711\n  Ensembl\n  MGI Sequence Detail', 'ENSMUST00000144443\n  Ensembl\n  MGI Sequence Detail', 'ENSMUST00000108592\n  Ensembl\n  MGI Sequence Detail', 'ENSMUST00000139007\n  Ensembl\n  MGI Sequence Detail', 'NM_019749\n  RefSeq\n  MGI Sequence Detail', 'BC030350\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', 'BC002126\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', 'BC024621\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', 'AV029091\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', 'BC029329\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', 'AK002879\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', 'AK011731\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', 'AF161587\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', 'KY499680\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', 'AW124839\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', 'ENSMUSG00000018567\n  Ensembl Gene Model\n  MGI Sequence Detail', '56486\n  NCBI Gene Model\n  MGI Sequence Detail', 'MGP_129S1SvImJ_G0018575\n  Ensembl\n  MGI Sequence Detail', 'MGP_WSBEiJ_G0017937\n  Ensembl\n  MGI Sequence Detail', 'MGP_NODShiLtJ_G0018423\n  Ensembl\n  MGI Sequence Detail', 'MGP_PWKPhJ_G0017657\n  Ensembl\n  MGI Sequence Detail', 'MGP_NZOHlLtJ_G0019008\n  Ensembl\n  MGI Sequence Detail', 'MGP_C3HHeJ_G0018328\n  Ensembl\n  MGI Sequence Detail', 'MGP_BALBcJ_G0018515\n  Ensembl\n  MGI Sequence Detail', 'MGP_C57BL6NJ_G0018966\n  Ensembl\n  MGI Sequence Detail'])
        
        #finds the Length column and then iterates through all items
        lengthlist = driver.find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-length .yui-dt-liner')
        searchTextItems = iterate.getTextAsList(lengthlist)
        time.sleep(2)
        print(searchTextItems)
        #asserts that the rows of length data are in correct order,sort is large to small
        self.assertEqual(searchTextItems, ['1351', '932', '750', '454', '1122', '1152', '924', '899', '893', '879', '872', '776', '565', '492', '465', '3809', '3580', '6111', '5983', '5196', '4974', '4641', '4400', '3763', '3731'])
        
    def test_mgp_links(self):
        """
        @status: Tests that am MGP sequence has a link to Mouse Genomes Project and the link is correct
        It then goes back to the sequence summary page and verifies the MGI Sequence Detail link for the same sequence is correct
        @note: seq-summary-3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker")
        genebox = driver.find_element(By.NAME, 'nomen')
        # put your marker symbol
        genebox.send_keys("Ppnr")
        genebox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the correct marker link and clicks it
        driver.find_element(By.LINK_TEXT, 'Ppnr').click()
        time.sleep(2)
        #Finds the All sequences link and clicks it
        driver.find_element(By.ID, 'allSeqLink').click()
        time.sleep(2)
        #finds the link for Ensembl of sequence MGP_CBAJ_G0036567 and clicks it.
        driver.find_element(By.CSS_SELECTOR, '#yui-rec5 > td:nth-child(2) > div:nth-child(1) > a:nth-child(2)').click()
        time.sleep(2)
        species_m = driver.find_element(By.CLASS_NAME, 'species')
        #asserts that the link takes you to the correct sequence at ensembl.
        self.assertEqual(species_m.text, 'Mouse CBA/J')
        driver.back()
        time.sleep(2)
        #finds the link for MGI Sequence Detail of sequence MGP_CBAJ_G0036567 and clicks it.
        driver.find_element(By.CSS_SELECTOR, '#yui-rec5 > td:nth-child(2) > div:nth-child(1) > a:nth-child(4)').click()
        time.sleep(2)
        #find the ID listed in the ID/Version ribbon of the sequence detail page
        seq_id = driver.find_element(By.CSS_SELECTOR, '#seqIdTable > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > b:nth-child(1)')
        #asserts that the link takes you to the correct sequence detail page.
        self.assertEqual(seq_id.text, 'MGP_CBAJ_G0036567')

    def test_mgi_b6_links(self):
        """
        @status: Tests that am MGI sequence(b6) has a link to its Sequence Detail page and the link is correct
        @note: seq-summary-4
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker")
        genebox = driver.find_element(By.NAME, 'nomen')
        # put your marker symbol
        genebox.send_keys("Ppnr")
        genebox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the correct marker link and clicks it
        driver.find_element(By.LINK_TEXT, 'Ppnr').click()
        time.sleep(2)
        #Finds the All sequences link and clicks it
        driver.find_element(By.ID, 'allSeqLink').click()
        time.sleep(2)
        #finds the link for MGI Sequence Detail of sequence MGI_C57BL6J_1349458 and clicks it.
        driver.find_element(By.CSS_SELECTOR, '#yui-rec21 > td:nth-child(2) > div:nth-child(1) > a:nth-child(2)').click()
        time.sleep(2)
        #find the ID listed in the ID/Version ribbon of the sequence detail page
        seq_id = driver.find_element(By.CSS_SELECTOR, '#seqIdTable > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > b:nth-child(1)')
        #asserts that the link takes you to the correct sequence detail page.
        self.assertEqual(seq_id.text, 'MGI_C57BL6J_1349458')
        
    def tearDown(self):
        self.driver.close()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSequenceSummaryPage))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))