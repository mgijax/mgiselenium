'''
Created on Apr 4, 2016

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

class TestSpecSumByRef(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox() 

    def test_table_headers(self):
        """
        @status: Tests that the summaries table headers are correct
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
        
    def test_page_sort(self):
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

    def test_age_note(self):
        """
        @status: Tests that the age notes are correct
        an age note is represented by a asterisk.
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
        #finds the age note column and then the first 12 items
        summarytable = driver.find_element_by_id("specimenSummaryTable")
        agenotes = summarytable.find_elements_by_css_selector('td:nth-child(6)')
        agenote1 = agenotes[0]
        agenote2 = agenotes[1]
        agenote3 = agenotes[2]
        agenote4 = agenotes[3]
        agenote5 = agenotes[4]
        agenote6 = agenotes[5]
        agenote7 = agenotes[6]
        #asserts the first 7 age notes are correct and in correct order
        self.assertEqual(agenote1.text, "*  ")
        self.assertEqual(agenote2.text, "*  ")
        self.assertEqual(agenote3.text, "*  ")
        self.assertEqual(agenote4.text, "*  ")
        self.assertEqual(agenote5.text, "*  ")
        self.assertEqual(agenote6.text, "*  ")
        self.assertEqual(agenote7.text, "*  ")
        

    def test_specimen_note(self):
        """
        @status: Tests that the specimen notes are correctly displayed
        specimen notes should be fully displayed
        """
        driver = self.driver
        driver.get(PWI_URL)
        #opens the PWI reference form
        driver.find_element_by_link_text("Reference Form").click()
        accidbox = driver.find_element_by_id('accids')
        # put your J number in the box
        accidbox.send_keys("J:36691")
        accidbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the specimens link and clicks it
        driver.find_element_by_link_text("Specimens").click()
        wait.forAjax(driver)
        #finds the specimen notes column and then the first 7 items
        summarytable = driver.find_element_by_id("specimenSummaryTable")
        specnotes = summarytable.find_elements_by_css_selector('td:nth-child(13)')
        specnote1 = specnotes[0]
        specnote2 = specnotes[1]
        specnote3 = specnotes[2]
        specnote4 = specnotes[3]
        specnote5 = specnotes[4]
        specnote6 = specnotes[5]
        specnote7 = specnotes[6]
        #asserts the first 7 specimen notes are correct and in correct order
        self.assertEqual(specnote1.text, "2.5% paraformaldehyde  ")
        self.assertEqual(specnote2.text, "2.5% paraformaldehyde  ")
        self.assertEqual(specnote3.text, "Fixed in 2.5% paraformaldehyde. With N-glycannase pretreatment.  ")
        self.assertEqual(specnote4.text, "2.5% paraformaldehyde  ")
        self.assertEqual(specnote5.text, "2.5% paraformaldehyde  ")
        self.assertEqual(specnote6.text, "2.5% paraformaldehyde  ")
        self.assertEqual(specnote7.text, "2.5% paraformaldehyde  ")
        

    def test_assay_detail_links(self):
        """
        @status: Tests that the Assay IDs link to correct assay detail pages
        
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
        #finds the assay id column and then clicks the link for the first row
        summarytable = driver.find_element_by_id("specimenSummaryTable")
        assayids = summarytable.find_elements_by_css_selector('td:nth-child(1)')
        assayid1 = assayids[0]
        assayid1.click()
        wait.forAjax(driver)
        #finds the MGI id on the page and asserts it is correct
        details = self.driver.find_element_by_class_name('detailPageListData')
        mgiid = details.find_elements_by_css_selector('dd')
        assayid = mgiid[3].text
        self.assertEqual(assayid, 'MGI:3037440')
        
    def test_cre_assay(self):
        """
        @status: Tests that all cre assays are correctly displayed at the bottom
        cre assays are Recombinase reporter and  In situ reporter (transgenic)
        """
        driver = self.driver
        driver.get(PWI_URL)
        #opens the PWI reference form
        driver.find_element_by_link_text("Reference Form").click()
        accidbox = driver.find_element_by_id('accids')
        # put your J number in the box
        accidbox.send_keys("J:105186")
        accidbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the specimens link and clicks it
        driver.find_element_by_link_text("Specimens").click()
        wait.forAjax(driver)
        #finds the specimen notes column and then the first 7 items
        summarytable = driver.find_element_by_id("specimenSummaryTable")
        assaytypes = summarytable.find_elements_by_css_selector('td:nth-child(3)')
        assaytype1 = assaytypes[13]
        assaytype2 = assaytypes[14]
        assaytype3 = assaytypes[15]
        assaytype4 = assaytypes[16]
        assaytype5 = assaytypes[17]
        assaytype6 = assaytypes[18]
        assaytype7 = assaytypes[19]
        #asserts the first 7 specimen notes are correct and in correct order
        self.assertEqual(assaytype1.text, "In situ reporter (knock in)")
        self.assertEqual(assaytype2.text, "In situ reporter (transgenic)")
        self.assertEqual(assaytype3.text, "In situ reporter (transgenic)")
        self.assertEqual(assaytype4.text, "In situ reporter (transgenic)")
        self.assertEqual(assaytype5.text, "Recombinase reporter")
        self.assertEqual(assaytype6.text, "Recombinase reporter")
        self.assertEqual(assaytype7.text, "Recombinase reporter")
        

    def tearDown(self):
        self.driver.close()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSpecSumByRef))
    return suite

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSpecSumByRef']
    unittest.main()