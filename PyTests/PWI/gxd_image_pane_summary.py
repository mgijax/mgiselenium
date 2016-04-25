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
        @status: Tests that the image pane table headers are correct
        Image, Figure Label, Pane Label, Assay (Gene), Specimen label
        """
        driver = self.driver
        driver.get(PWI_URL)
        #opens the PWI reference form
        driver.find_element_by_link_text("Reference Form").click()
        accidbox = driver.find_element_by_id('accids')
        # put your J number in the box
        accidbox.send_keys("J:83696")
        accidbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the specimens link and clicks it
        driver.find_element_by_link_text("Exp Images").click()
        wait.forAjax(driver)
        #Locates the summary table and finds the table headings
        headerlist = driver.find_element_by_id("paneSummaryTable")
        items = headerlist.find_elements_by_tag_name("th")
        searchTextItems = iterate.getTextAsList(items)
        wait.forAjax(driver)
        #verifies all the table headings are correct and in order
        self.assertEqual(searchTextItems, ['Image', 'Figure', 'Pane', 'Specimen', 'Assay (Gene)'])
        
    def verify_page_sort(self):
        """
        @status: Tests that the default page sort is correct
        sort is by GXD data first then CRE data, Figure, Pane, Assay Marker Symbol
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
        driver.find_element_by_link_text("Exp Images").click()
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
        
    def verify_multispecs_diffassay(self):
        """
        @status: Tests the display for image panes with multiple specimens from different assays
        each specimen/assay should have it's own row per image
        """
        driver = self.driver
        driver.get(PWI_URL)
        #opens the PWI reference form
        driver.find_element_by_link_text("Reference Form").click()
        accidbox = driver.find_element_by_id('accids')
        # put your J number in the box
        accidbox.send_keys("J:83696")
        accidbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the specimens link and clicks it
        driver.find_element_by_link_text("Exp Images").click()
        wait.forAjax(driver)
        #Locates the images table and finds the table headings
        imagestable = driver.find_element_by_id("paneSummaryTable")
        rows = imagestable.find_elements_by_css_selector('tr')
        #displays each row of data for the first 18 rows
        row1 = rows[1]
        row2 = rows[2]
        row3 = rows[3]
        row4 = rows[4]
        row5 = rows[5]
        row6 = rows[6]
        row7 = rows[7]
        row8 = rows[8]
        row9 = rows[9]
        row10 = rows[10]
        row11 = rows[11]
        row12 = rows[12]
        row13 = rows[13]
        row14 = rows[14]
        row15 = rows[15]
        row16 = rows[16]
        row17 = rows[17]
        row18 = rows[18]
        #asserts that the rows of data are correct for the first 18 rows
        self.assertEqual(row1.text, 'MGI:3522445\n1 Syndecan-1 MGI:3522591 (Sdc1)')
        self.assertEqual(row2.text, 'MGI:3522445\n1 Syndecan-2 MGI:3522592 (Sdc2)')
        self.assertEqual(row3.text, 'MGI:3522445\n1 Syndecan-3 MGI:3522593 (Sdc3)')
        self.assertEqual(row4.text, 'MGI:3522445\n1 Syndecan-4 MGI:3522594 (Sdc4)')
        self.assertEqual(row5.text, 'MGI:3522448\n2 A 2A\n2A\n2A MGI:3522619 (Sdc1)\nMGI:3522621 (Hspg2)\nMGI:3522624 (Tubb3)')
        self.assertEqual(row6.text, "MGI:3522448\n2 B 2B,2B''\n2B,2B'' MGI:3522621 (Hspg2)\nMGI:3522624 (Tubb3)")
        self.assertEqual(row7.text, "MGI:3522448\n2 B' 2B',2B'' MGI:3522619 (Sdc1)")
        self.assertEqual(row8.text, "MGI:3522448\n2 B'' 2B',2B''\n2B,2B''\n2B,2B'' MGI:3522619 (Sdc1)\nMGI:3522621 (Hspg2)\nMGI:3522624 (Tubb3)")
        self.assertEqual(row9.text, "MGI:3522448\n2 C 2C,2C''\n2C,2C'' MGI:3522621 (Hspg2)\nMGI:3522624 (Tubb3)")
        self.assertEqual(row10.text, "MGI:3522448\n2 C' 2C',2C''\n2C,2C'' MGI:3522619 (Sdc1)\nMGI:3522624 (Tubb3)")
        self.assertEqual(row11.text, "MGI:3522448\n2 C'' 2C',2C''\n2C,2C'' MGI:3522619 (Sdc1)\nMGI:3522621 (Hspg2)")
        self.assertEqual(row12.text, 'MGI:3522448\n2 D 2D MGI:3522626 (Sdc4)')
        self.assertEqual(row13.text, "MGI:3522448\n2 E 2E,2E'' MGI:3522626 (Sdc4)")
        self.assertEqual(row14.text, "MGI:3522448\n2 E' 2E,2E'' MGI:5578043 (Sdc1)")
        self.assertEqual(row15.text, "MGI:3522448\n2 E'' 2E,2E''\n2E,2E'' MGI:3522626 (Sdc4)\nMGI:5578043 (Sdc1)")
        self.assertEqual(row16.text, 'MGI:3522448\n2 F 2F\n2F MGI:3522624 (Tubb3)\nMGI:3522626 (Sdc4)')
        self.assertEqual(row17.text, 'MGI:3522449\n3 A 3A MGI:3522624 (Tubb3)')
        self.assertEqual(row18.text, 'MGI:3522449\n3 B 3B MGI:3522627 (Sdc3)')
        
           
    def verify_multispecs_sameassay_samepane(self):
        """
        @status: Tests the display for image panes with multiple specimens from the same assay using the same image pane
        each specimen should have it's own row
        """
        driver = self.driver
        driver.get(PWI_URL)
        #opens the PWI reference form
        driver.find_element_by_link_text("Reference Form").click()
        accidbox = driver.find_element_by_id('accids')
        # put your J number in the box
        accidbox.send_keys("J:85638")
        accidbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the specimens link and clicks it
        driver.find_element_by_link_text("Exp Images").click()
        wait.forAjax(driver)
        #Locates the images table and finds the table headings
        imagestable = driver.find_element_by_id("paneSummaryTable")
        rows = imagestable.find_elements_by_css_selector('tr')
        #displays each row of data for the first 13 rows
        row1 = rows[1]
        row2 = rows[2]
        row3 = rows[3]
        row4 = rows[4]
        row5 = rows[5]
        row6 = rows[6]
        row7 = rows[7]
        row8 = rows[8]
        row9 = rows[9]
        row10 = rows[10]
        row11 = rows[11]
        row12 = rows[12]
        row13 = rows[13]
        #asserts that the rows of data are correct for the first 13 rows
        self.assertEqual(row1.text, 'MGI:5750634\n3 A MGI:5750650 (H13)')
        self.assertEqual(row2.text, 'MGI:5750637\n4 A 4A MGI:5750680 (H13)')
        self.assertEqual(row3.text, 'MGI:5750637\n4 B 4B MGI:5750680 (H13)')
        self.assertEqual(row4.text, 'MGI:5750637\n4 C 4C MGI:5750680 (H13)')
        self.assertEqual(row5.text, 'MGI:5750638\n5 E5.5 5 E5.5 embryo\n5 E5.5 mother MGI:5750680 (H13)')
        self.assertEqual(row6.text, 'MGI:5750638\n5 E6.5 5 E6.5 embryo\n5 E6.5 mother MGI:5750680 (H13)')
        self.assertEqual(row7.text, 'MGI:5750638\n5 E7.5 5 E7.5 embryo\n5 E7.5 mother MGI:5750680 (H13)')
        self.assertEqual(row8.text, 'MGI:5750638\n5 E8.5 5 E8.5 embryo\n5 E8.5 mother MGI:5750680 (H13)')
        self.assertEqual(row9.text, 'MGI:5750638\n5 E9.5 5 E9.5 embryo\n5 E9.5 mother MGI:5750680 (H13)')
        self.assertEqual(row10.text, 'MGI:5750639\n6 E10.5 6 E10.5 MGI:5750680 (H13)')
        self.assertEqual(row11.text, 'MGI:5750639\n6 E11.5 6 E11.5 MGI:5750680 (H13)')
        self.assertEqual(row12.text, 'MGI:5750639\n6 E13.5 6 E13.5 MGI:5750680 (H13)')
        self.assertEqual(row13.text, 'MGI:5750639\n6 E14.5 6 E14.5 MGI:5750680 (H13)')

    def verify_images_noassay(self):
        """
        @status: Tests the display for image panes with no attached assay
        each image and figure displayed but no assay or specimen
        @todo: data issue needs to be fixed for test to pass, jackie is working on it."""
        driver = self.driver
        driver.get(PWI_URL)
        #opens the PWI reference form
        driver.find_element_by_link_text("Reference Form").click()
        accidbox = driver.find_element_by_id('accids')
        # put your J number in the box
        accidbox.send_keys("J:102285")
        accidbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the specimens link and clicks it
        driver.find_element_by_link_text("Exp Images").click()
        wait.forAjax(driver)
        #Locates the images table and finds the table headings
        imagestable = driver.find_element_by_id("paneSummaryTable")
        rows = imagestable.find_elements_by_css_selector('tr')
        print [x.text for x in rows]
        #displays each row of data for the first 17 rows
        row1 = rows[1]
        row2 = rows[2]
        row3 = rows[3]
        row4 = rows[4]
        row5 = rows[5]
        row6 = rows[6]
        row7 = rows[7]
        row8 = rows[8]
        row9 = rows[9]
        row10 = rows[10]
        row11 = rows[11]
        row12 = rows[12]
        row13 = rows[13]
        row14 = rows[14]
        row15 = rows[15]
        row16 = rows[16]
        #asserts that the rows of data are correct for the first 17 rows
        self.assertEqual(row1.text, 'MGI:4453601\n2 b Fig. 1b MGI:4453599 (Tg(Scgb1a1-cre)1Tauc)')
        self.assertEqual(row2.text, 'MGI:4453603\n3 a Fig. 3a MGI:4453606 (Tg(Scgb1a1-cre)1Tauc)')
        self.assertEqual(row3.text, 'MGI:4453603\n3 c Fig. 3c MGI:4453606 (Tg(Scgb1a1-cre)1Tauc)')
        self.assertEqual(row4.text, 'MGI:4453603\n3 e Fig. 3e MGI:4453606 (Tg(Scgb1a1-cre)1Tauc)')
        self.assertEqual(row5.text, 'MGI:4453605\n4 a Fig. 4a MGI:4453606 (Tg(Scgb1a1-cre)1Tauc)')
        self.assertEqual(row6.text, 'MGI:4453605\n4 b Fig. 4b MGI:4453606 (Tg(Scgb1a1-cre)1Tauc)')
        self.assertEqual(row7.text, 'MGI:4453605\n4 c Fig. 4c MGI:4453606 (Tg(Scgb1a1-cre)1Tauc)')
        self.assertEqual(row8.text, 'MGI:4453605\n4 d Fig. 4d MGI:4453606 (Tg(Scgb1a1-cre)1Tauc)')
        self.assertEqual(row9.text, 'MGI:4453605\n4 e Fig. 4e MGI:4453606 (Tg(Scgb1a1-cre)1Tauc)')
        self.assertEqual(row10.text, 'MGI:4453605\n4 f Fig. 4f MGI:4453606 (Tg(Scgb1a1-cre)1Tauc)')
        self.assertEqual(row11.text, 'MGI:4453605\n4 g Fig. 4g MGI:4453606 (Tg(Scgb1a1-cre)1Tauc)')
        self.assertEqual(row12.text, 'MGI:4453605\n4 h Fig. 4h MGI:4453606 (Tg(Scgb1a1-cre)1Tauc)')
        self.assertEqual(row13.text, 'MGI:4453605\n4 i Fig. 4i MGI:4453606 (Tg(Scgb1a1-cre)1Tauc)')
        self.assertEqual(row14.text, 'MGI:4453605\n4 j Fig. 4j MGI:4453606 (Tg(Scgb1a1-cre)1Tauc)')
        self.assertEqual(row15.text, 'MGI:4453605\n4 k Fig. 4k ')
        self.assertEqual(row16.text, 'MGI:4453605\n4 l Fig. 4l ')
        

    def verify_images_nospecimen(self):
        """
        @status: Tests the display for image panes with no specimen label
        each image, figure label, pane label, and assay displayed but no specimen label
        """
        driver = self.driver
        driver.get(PWI_URL)
        #opens the PWI reference form
        driver.find_element_by_link_text("Reference Form").click()
        accidbox = driver.find_element_by_id('accids')
        # put your J number in the box
        accidbox.send_keys("J:9026")
        accidbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the specimens link and clicks it
        driver.find_element_by_link_text("Exp Images").click()
        wait.forAjax(driver)
        #Locates the images table and finds the table headings
        imagestable = driver.find_element_by_id("paneSummaryTable")
        rows = imagestable.find_elements_by_css_selector('tr')
        #displays each row of data for the first 9 rows
        row1 = rows[1]
        row2 = rows[2]
        row3 = rows[3]
        row4 = rows[4]
        row5 = rows[5]
        row6 = rows[6]
        row7 = rows[7]
        row8 = rows[8]
        row9 = rows[9]
        #asserts that the rows of data are correct for the first 9 rows
        self.assertEqual(row1.text, 'MGI:4441359\n1 A 2ar MGI:4441369 (Spp1)')
        self.assertEqual(row2.text, 'MGI:4441359\n1 A SPARC MGI:4441372 (Sparc)')
        self.assertEqual(row3.text, 'MGI:4441359\n1 B 2ar MGI:4441380 (Spp1)')
        self.assertEqual(row4.text, 'MGI:4441359\n1 B SPARC MGI:4441384 (Sparc)')
        self.assertEqual(row5.text, 'MGI:4441361\n2 a/e 2a,e MGI:4441386 (Spp1)')
        self.assertEqual(row6.text, 'MGI:4441361\n2 b/f 2b,f MGI:4441386 (Spp1)')
        self.assertEqual(row7.text, 'MGI:4441361\n2 d/h 2d,h - decidua\n2d,h - embryo MGI:4441386 (Spp1)')
        self.assertEqual(row8.text, 'MGI:4441363\n3 a 3a MGI:4441386 (Spp1)')
        self.assertEqual(row9.text, 'MGI:4441363\n3 d/e 3d MGI:4441386 (Spp1)')
           
                   
    def tearDown(self):
        self.driver.close()
        



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSpecSumByRef']
    unittest.main()