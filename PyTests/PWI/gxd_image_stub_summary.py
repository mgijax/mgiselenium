'''
Created on Apr 13, 2016
This page is linked to from the References page
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,os.path
from util import wait, iterate
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import PWI_URL

class TestImageStubPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox() 

    def verify_table_headers(self):
        """
        @status: Tests that the image stub table headers are correct
        MGI ID, Figure label, Image Pane, MGI Assay ID, Specimen label
        """
        driver = self.driver
        driver.get(PWI_URL)
        #opens the PWI reference form
        driver.find_element_by_link_text("Reference Form").click()
        accidbox = driver.find_element_by_id('accids')
        # put your J number in the box
        accidbox.send_keys("J:84605")
        accidbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the specimens link and clicks it
        driver.find_element_by_link_text("Specimens").click()
        wait.forAjax(driver)
        #Locates the summary table and finds the table headings
        headerlist = driver.find_element_by_id("specimenSummaryTable")
        items = headerlist.find_elements_by_tag_name("th")
        searchTextItems = iterate.getTextAsList(items)
        wait.forAjax(driver)
        #verifies all the table headings are correct and in order
        self.assertEqual(searchTextItems, ['Assay ID','Marker Symbol','Assay Type','Specimen Label','Age','Age Note','Sex','Hybridization','Fixation','Embedding','Background','Allele(s)','Specimen Note'])
        
    def verify_page_sort(self):
        """
        @status: Tests that the default page sort is correct
        sort is by ascii so 10 would come before 4 or 5, or 6, etc.
        """
        driver = self.driver
        driver.get(PWI_URL)
        #opens the PWI reference form
        driver.find_element_by_link_text("Reference Form").click()
        accidbox = driver.find_element_by_id('accids')
        # put your J number in the box
        accidbox.send_keys("J:40904")
        accidbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the specimens link and clicks it
        driver.find_element_by_link_text("Specimens").click()
        wait.forAjax(driver)
        #finds the specimen label column and then the first 12 items
        summarytable = driver.find_element_by_id("specimenSummaryTable")
        specimens = summarytable.find_elements_by_css_selector('td:nth-child(4)')
        specimen1 = specimens[0]
        specimen2 = specimens[1]
        specimen3 = specimens[2]
        specimen4 = specimens[3]
        specimen5 = specimens[4]
        specimen6 = specimens[5]
        specimen7 = specimens[6]
        specimen8 = specimens[7]
        specimen9 = specimens[8]
        specimen10 = specimens[9]
        specimen11 = specimens[10]
        specimen12 = specimens[11]
        #asserts the first 12 specimen labels are correct and in correct order
        self.assertEqual(specimen1.text, "10A")
        self.assertEqual(specimen2.text, "10B")
        self.assertEqual(specimen3.text, "10C")
        self.assertEqual(specimen4.text, "10D")
        self.assertEqual(specimen5.text, "10E/F")
        self.assertEqual(specimen6.text, "4A")
        self.assertEqual(specimen7.text, "4B")
        self.assertEqual(specimen8.text, "4C")
        self.assertEqual(specimen9.text, "4D")
        self.assertEqual(specimen10.text, "4E")
        self.assertEqual(specimen11.text, "4F")
        self.assertEqual(specimen12.text, "5A")
        
        
    def tearDown(self):
        self.driver.close()
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSpecSumByRef']
    unittest.main()