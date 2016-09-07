'''
Created on Aug 5, 2016

This page is linked to from the Marker detail page
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,os.path
from util import wait, iterate
from config.config import FEWI_URL
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import FEWI_URL

class TestSequenceSummaryPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox() 

    def test_table_headers(self):
        """
        @status: Tests that the Sequence Summary table headers are correct
        Headers are: Select, Sequence, Type, Length, Strain/Species, Description from Sequence Provider, Clone Collection, Marker Symbol
        """
        driver = self.driver
        driver.get(config.FEWI_URL + "/marker")
        genebox = driver.find_element_by_name('nomen')
        # put your marker symbol
        genebox.send_keys("Bloc1s2")
        genebox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the correct marker link and clicks it
        driver.find_element_by_link_text("Bloc1s2").click()
        wait.forAjax(driver)
        #Finds the All sequences link and clicks it
        driver.find_element_by_link_text("15").click()
        wait.forAjax(driver)
        #Locates the marker header table and finds the table headings
        markerheaderlist = driver.find_element_by_class_name("summaryHeaderCat1")
        items = markerheaderlist.find_elements_by_tag_name("div")
        searchTextItems = iterate.getTextAsList(items)
        wait.forAjax(driver)
        #verifies all the table headings are correct and in order
        self.assertEqual(searchTextItems, ['Symbol','Name','ID'])
        wait.forAjax(driver)
        #Locates the sequence summary table and finds the table headings
        columnheaderlist = driver.find_elements_by_class_name("yui-dt-label")
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
        @attention: While this test still works, it might need revisting later to figure out a better way of confirming sort is correct
        """
        driver = self.driver
        driver.get(config.FEWI_URL + "/marker")
        genebox = driver.find_element_by_name('nomen')
        # put your marker symbol
        genebox.send_keys("Gabarap")
        genebox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the correct marker link and clicks it
        driver.find_element_by_link_text("Gabarap").click()
        wait.forAjax(driver)
        #Finds the All sequences link and clicks it
        driver.find_element_by_link_text("28").click()
        wait.forAjax(driver)
        #finds the Type column and then iterates through all items
        seqtypelist = driver.find_elements_by_css_selector("td.yui-dt-col-seqType .yui-dt-liner")
        searchTextItems = iterate.getTextAsList(seqtypelist)
        wait.forAjax(driver)
        #print searchTextItems
        #asserts that the rows of Type data are in correct order
        self.assertEqual(searchTextItems, ['RNA','RNA','RNA','RNA','RNA','RNA','RNA','RNA','RNA','RNA','RNA','RNA','RNA','RNA','RNA','RNA','RNA','RNA','DNA','DNA','DNA','Polypeptide','Polypeptide','Polypeptide','Polypeptide'])
        
        #finds the Sequence column and then iterates through all items
        seqlist = driver.find_elements_by_css_selector("td.yui-dt-col-seqInfo .yui-dt-liner")
        searchTextItems = iterate.getTextAsList(seqlist)
        wait.forAjax(driver)
        #print searchTextItems
        #asserts that the rows of length data are in correct order
        self.assertEqual(searchTextItems, ['OTTMUST00000013495\n  VEGA\n  MGI Sequence Detail','OTTMUST00000013496\n  VEGA\n  MGI Sequence Detail','OTTMUST00000038731\n  VEGA\n  MGI Sequence Detail','OTTMUST00000013497\n  VEGA\n  MGI Sequence Detail','ENSMUST00000018711\n  Ensembl\n  MGI Sequence Detail','ENSMUST00000144443\n  Ensembl\n  MGI Sequence Detail','ENSMUST00000108592\n  Ensembl\n  MGI Sequence Detail','ENSMUST00000139007\n  Ensembl\n  MGI Sequence Detail','NM_019749\n  RefSeq\n  MGI Sequence Detail','BC030350\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail','BC024621\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail','BC002126\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail','AV029091\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail','BC029329\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail','AK002879\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail','AK011731\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail','AF161587\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail','AW124839\n  GenBank | EMBL | DDBJ\n  MGI Sequence Detail','OTTMUSG00000006020\n  VEGA\n  MGI Sequence Detail','ENSMUSG00000018567\n  Ensembl Gene Model\n  MGI Sequence Detail','56486\n  NCBI Gene Model\n  MGI Sequence Detail','OTTMUSP00000006254\n  VEGA\n  MGI Sequence Detail','OTTMUSP00000017319\n  VEGA\n  MGI Sequence Detail','ENSMUSP00000018711\n  Ensembl\n  MGI Sequence Detail','ENSMUSP00000104233\n  Ensembl\n  MGI Sequence Detail'])
        
        #finds the Length column and then iterates through all items
        lengthlist = driver.find_elements_by_css_selector("td.yui-dt-col-length .yui-dt-liner")
        searchTextItems = iterate.getTextAsList(lengthlist)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the rows of length data are in correct order,sort is large to small
        self.assertEqual(searchTextItems, ['1351','932','750','454','1351','932','750','454','1122','1152','924','924','893','879','872','776','565','465','3809','3809','3580','117','106','117','106'])
        
        
    def tearDown(self):
        self.driver.close()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSequenceSummaryPage))
    return suite

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSpecSumByRef']
    unittest.main()