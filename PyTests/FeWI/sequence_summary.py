'''
Created on Aug 5, 2016

This page is linked to from the Marker detail page
@author: jeffc
'''
import unittest
import time
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
        self.driver = webdriver.Firefox() 

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
        wait.forAjax(driver)
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
        wait.forAjax(driver)
        #Finds the All sequences link and clicks it
        driver.find_element(By.ID, 'allSeqLink').click()
        time.sleep(2)
        #finds the Type column and then iterates through all items
        seqtypelist = driver.find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-seqType .yui-dt-liner')
        searchTextItems = iterate.getTextAsList(seqtypelist)
        time.sleep(2)
        print searchTextItems
        #asserts that the rows of Type data are in correct order
        self.assertEqual(searchTextItems, [u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'RNA', u'DNA', u'DNA', u'DNA', u'Polypeptide', u'Polypeptide', u'Polypeptide'])
        
        #finds the Sequence column and then iterates through all items
        seqlist = driver.find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-seqInfo .yui-dt-liner')
        searchTextItems = iterate.getTextAsList(seqlist)
        time.sleep(2)
        print searchTextItems
        #asserts that the rows of length data are in correct order
        self.assertEqual(searchTextItems, ['OTTMUST00000013495\n  VEGA\n  MGI Sequence Detail', u'OTTMUST00000013496\n  VEGA\n  MGI Sequence Detail', u'OTTMUST00000038731\n  VEGA\n  MGI Sequence Detail', u'OTTMUST00000013497\n  VEGA\n  MGI Sequence Detail', u'ENSMUST00000018711\n  Ensembl\n  MGI Sequence Detail', u'ENSMUST00000144443\n  Ensembl\n  MGI Sequence Detail', u'ENSMUST00000108592\n  Ensembl\n  MGI Sequence Detail', u'ENSMUST00000139007\n  Ensembl\n  MGI Sequence Detail', u'NM_019749\n  RefSeq\n  MGI Sequence Detail', u'BC030350\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', u'BC002126\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', u'BC024621\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', u'AV029091\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', u'BC029329\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', u'AK002879\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', u'AK011731\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', u'AF161587\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', u'KY499680\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', u'AW124839\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail', u'OTTMUSG00000006020\n  VEGA\n  MGI Sequence Detail', u'ENSMUSG00000018567\n  Ensembl Gene Model\n  MGI Sequence Detail', u'56486\n  NCBI Gene Model\n  MGI Sequence Detail', u'OTTMUSP00000006254\n  VEGA\n  MGI Sequence Detail', u'OTTMUSP00000017319\n  VEGA\n  MGI Sequence Detail', u'ENSMUSP00000018711\n  Ensembl\n  MGI Sequence Detail'])
        
        #finds the Length column and then iterates through all items
        lengthlist = driver.find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-length .yui-dt-liner')
        searchTextItems = iterate.getTextAsList(lengthlist)
        time.sleep(2)
        print searchTextItems
        #asserts that the rows of length data are in correct order,sort is large to small
        self.assertEqual(searchTextItems, [u'1351', u'932', u'750', u'454', u'1351', u'932', u'750', u'454', u'1122', u'1152', u'924', u'899', u'893', u'879', u'872', u'776', u'565', u'492', u'465', u'3809', u'3809', u'3580', u'117', u'106', u'117'])
        
        
    def tearDown(self):
        self.driver.close()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSequenceSummaryPage))
    return suite

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSpecSumByRef']
    unittest.main()