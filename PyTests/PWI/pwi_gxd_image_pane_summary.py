'''
Created on Apr 13, 2016
This page is linked to from the References page
@author: jeffc
'''
import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,os.path
from util import wait, iterate
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import TEST_PWI_URL

class TestPwiGxdImagePanePage(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome() 
        self.driver = webdriver.Firefox()

    def test_table_headers(self):
        """
        @status: Tests that the image pane table headers are correct
        Image, Figure Label, Pane Label, Assay (Gene), Specimen label
        """
        driver = self.driver
        driver.get(TEST_PWI_URL)
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
        self.assertEqual(searchTextItems, ['Image', 'Figure', 'Pane', 'Specimen', 'Assay (Gene)', 'Assay Type'])
        
    def test_page_sort(self):
        """
        @status: Tests that the default page sort is correct
        sort is by Figure, Pane, Assay Marker Symbol
        @attention: This test also tests specimens align with their correct assay type
        """
        driver = self.driver
        driver.get(TEST_PWI_URL)
        #opens the PWI reference form
        driver.find_element_by_link_text("Reference Form").click()
        accidbox = driver.find_element_by_id('accids')
        # put your J number in the box
        accidbox.send_keys("J:213157")
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
        row19 = rows[19]
        row20 = rows[20]
        row21 = rows[21]
        row22 = rows[22]
        row23 = rows[23]
        row24 = rows[24]
        row25 = rows[25]
        row26 = rows[26]
        row27 = rows[27]
        row28 = rows[28]
        row29 = rows[29]
        row30 = rows[30]
        row31 = rows[31]
        row32 = rows[32]
        row33 = rows[33]
        row34 = rows[34]
        row35 = rows[35]
        row36 = rows[36]
        row37 = rows[37]
        row38 = rows[38]
        row39 = rows[39]
        row40 = rows[40]
        row41 = rows[41]
        row42 = rows[42]
        row43 = rows[43]
        row44 = rows[44]
        row45 = rows[45]
        #asserts that the rows of data are correct for the first 18 rows
        self.assertEqual(row1.text, 'MGI:5619605\n1 F 1F MGI:5619609 (Gata3) In situ reporter (knock in)')
        self.assertEqual(row2.text, 'MGI:5619605\n1 G 1G MGI:5619609 (Gata3) In situ reporter (knock in)')
        self.assertEqual(row3.text, 'MGI:5619568\n3 A 3A MGI:5619549 (Gata3) Recombinase reporter')
        self.assertEqual(row4.text, 'MGI:5619568\n3 F 3F MGI:5619666 (Calb1) Immunohistochemistry')
        self.assertEqual(row5.text, '3F MGI:5619668 (Slc17a1) Immunohistochemistry')
        self.assertEqual(row6.text, "MGI:5619568\n3 G 3G MGI:5619666 (Calb1) Immunohistochemistry")
        self.assertEqual(row7.text, "3G MGI:5619668 (Slc17a1) Immunohistochemistry")
        self.assertEqual(row8.text, "MGI:5619422\nS2 B S2B MGI:5619502 (Gata3) Recombinase reporter")
        self.assertEqual(row9.text, "S2B MGI:5619674 (Gata3) Immunohistochemistry")
        self.assertEqual(row10.text, "MGI:5619422\nS2 B' S2B MGI:5619502 (Gata3) Recombinase reporter")
        self.assertEqual(row11.text, "MGI:5619422\nS2 C S2C MGI:5619502 (Gata3) Recombinase reporter")
        self.assertEqual(row12.text, 'S2C MGI:5619511 (Gata3) In situ reporter (knock in)')
        self.assertEqual(row13.text, "S2C MGI:5619672 (Vsx2) Immunohistochemistry")
        self.assertEqual(row14.text, "MGI:5619422\nS2 C' S2C MGI:5619502 (Gata3) Recombinase reporter")
        self.assertEqual(row15.text, "S2C MGI:5619672 (Vsx2) Immunohistochemistry")
        self.assertEqual(row16.text, 'MGI:5619422\nS2 D S2D/E MGI:5619513 (Gata3) Recombinase reporter')
        self.assertEqual(row17.text, 'S2D/E MGI:5619674 (Gata3) Immunohistochemistry')
        self.assertEqual(row18.text, 'MGI:5619422\nS2 E S2D/E MGI:5619674 (Gata3) Immunohistochemistry')
        self.assertEqual(row19.text, "MGI:5619422\nS2 F S2F MGI:5619513 (Gata3) Recombinase reporter")
        self.assertEqual(row20.text, "S2F MGI:5619752 (Lbx1) Immunohistochemistry")
        self.assertEqual(row21.text, "MGI:5619422\nS2 G S2G MGI:5619513 (Gata3) Recombinase reporter")
        self.assertEqual(row22.text, "S2G MGI:5619753 (Evx1) Immunohistochemistry")
        self.assertEqual(row23.text, "MGI:5619422\nS2 H S2H MGI:5619513 (Gata3) Recombinase reporter")
        self.assertEqual(row24.text, "S2H MGI:5619754 (En1) Immunohistochemistry")
        self.assertEqual(row25.text, 'MGI:5619422\nS2 I S2I MGI:5619513 (Gata3) Recombinase reporter')
        self.assertEqual(row26.text, "S2I MGI:5619672 (Vsx2) Immunohistochemistry")
        self.assertEqual(row27.text, "MGI:5619422\nS2 J S2J MGI:5619513 (Gata3) Recombinase reporter")
        self.assertEqual(row28.text, "S2J MGI:5619755 (Mnx1) Immunohistochemistry")
        self.assertEqual(row29.text, 'MGI:5619422\nS2 K S2K MGI:5619513 (Gata3) Recombinase reporter')
        self.assertEqual(row30.text, 'S2K MGI:5619756 (Sim1) Immunohistochemistry')
        self.assertEqual(row31.text, "MGI:5619422\nS2 L S2L/M/M'/N/N' MGI:5619513 (Gata3) Recombinase reporter")
        self.assertEqual(row32.text, "S2L MGI:5619759 (Gata3) Immunohistochemistry")
        self.assertEqual(row33.text, "S2L MGI:5619760 (Gata2) Immunohistochemistry")
        self.assertEqual(row34.text, "MGI:5619422\nS2 M S2L/M/M'/N/N' MGI:5619513 (Gata3) Recombinase reporter")
        self.assertEqual(row35.text, "MGI:5619422\nS2 M' S2L MGI:5619759 (Gata3) Immunohistochemistry")
        self.assertEqual(row36.text, "S2L MGI:5619760 (Gata2) Immunohistochemistry")
        self.assertEqual(row37.text, "MGI:5619422\nS2 M'' S2L/M/M'/N/N' MGI:5619513 (Gata3) Recombinase reporter")
        self.assertEqual(row38.text, 'S2L MGI:5619759 (Gata3) Immunohistochemistry')
        self.assertEqual(row39.text, "S2L MGI:5619760 (Gata2) Immunohistochemistry")
        self.assertEqual(row40.text, "MGI:5619422\nS2 N S2L/M/M'/N/N' MGI:5619513 (Gata3) Recombinase reporter")
        self.assertEqual(row41.text, "MGI:5619422\nS2 N' S2L MGI:5619759 (Gata3) Immunohistochemistry")
        self.assertEqual(row42.text, 'S2L MGI:5619760 (Gata2) Immunohistochemistry')
        self.assertEqual(row43.text, "MGI:5619422\nS2 N'' S2L/M/M'/N/N' MGI:5619513 (Gata3) Recombinase reporter")
        self.assertEqual(row44.text, 'S2L MGI:5619759 (Gata3) Immunohistochemistry')
        self.assertEqual(row45.text, 'S2L MGI:5619760 (Gata2) Immunohistochemistry')
        
    def test_multispecs_diffassay(self):
        """
        @status: Tests the display for image panes with multiple specimens from different assays
        each specimen/assay should have it's own row per image
        """
        driver = self.driver
        driver.get(TEST_PWI_URL)
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
        row19 = rows[19]
        #asserts that the rows of data are correct for the first 18 rows
        self.assertEqual(row1.text, 'MGI:3522445\n1 _Syndecan-1 MGI:3522591 (Sdc1) RT-PCR')
        self.assertEqual(row2.text, 'MGI:3522445\n1 _Syndecan-2 MGI:3522592 (Sdc2) RT-PCR')
        self.assertEqual(row3.text, 'MGI:3522445\n1 _Syndecan-3 MGI:3522593 (Sdc3) RT-PCR')
        self.assertEqual(row4.text, 'MGI:3522445\n1 _Syndecan-4 MGI:3522594 (Sdc4) RT-PCR')
        self.assertEqual(row5.text, 'MGI:3522448\n2 A 2A MGI:3522619 (Sdc1) Immunohistochemistry')
        self.assertEqual(row6.text, "2A MGI:3522621 (Hspg2) Immunohistochemistry")
        self.assertEqual(row7.text, "2A MGI:3522624 (Tubb3) Immunohistochemistry")
        self.assertEqual(row8.text, "MGI:3522448\n2 B 2B,2B'' MGI:3522621 (Hspg2) Immunohistochemistry")
        self.assertEqual(row9.text, "2B,2B'' MGI:3522624 (Tubb3) Immunohistochemistry")
        self.assertEqual(row10.text, "MGI:3522448\n2 B' 2B',2B'' MGI:3522619 (Sdc1) Immunohistochemistry")
        self.assertEqual(row11.text, "MGI:3522448\n2 B'' 2B',2B'' MGI:3522619 (Sdc1) Immunohistochemistry")
        self.assertEqual(row12.text, "2B,2B'' MGI:3522621 (Hspg2) Immunohistochemistry")
        self.assertEqual(row13.text, "2B,2B'' MGI:3522624 (Tubb3) Immunohistochemistry")
        self.assertEqual(row14.text, "MGI:3522448\n2 C 2C,2C'' MGI:3522621 (Hspg2) Immunohistochemistry")
        self.assertEqual(row15.text, "2C,2C'' MGI:3522624 (Tubb3) Immunohistochemistry")
        self.assertEqual(row16.text, "MGI:3522448\n2 C' 2C',2C'' MGI:3522619 (Sdc1) Immunohistochemistry")
        self.assertEqual(row17.text, "2C,2C'' MGI:3522624 (Tubb3) Immunohistochemistry")
        self.assertEqual(row18.text, "MGI:3522448\n2 C'' 2C',2C'' MGI:3522619 (Sdc1) Immunohistochemistry")
        self.assertEqual(row19.text, "2C,2C'' MGI:3522621 (Hspg2) Immunohistochemistry")
        
    def test_multispecs_samegene_assay(self):
        """
        @status: Tests the display for image panes with multiple specimens for the same gene and assay
        all the specimens should be displayed on the same row
        """
        driver = self.driver
        driver.get(TEST_PWI_URL)
        #opens the PWI reference form
        driver.find_element_by_link_text("Reference Form").click()
        accidbox = driver.find_element_by_id('accids')
        # put your J number in the box
        accidbox.send_keys("J:85300")
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
        row19 = rows[19]
        row20 = rows[20]
        row21 = rows[21]
        row22 = rows[22]
        row23 = rows[23]
        row24 = rows[24]
        row25 = rows[25]
        
        #asserts that the rows of data are correct for the first 18 rows
        self.assertEqual(row1.text, 'MGI:3763145\n1 A 1A MGI:3763234 (Etv4) RNA in situ')
        self.assertEqual(row2.text, 'MGI:3763145\n1 B 1B MGI:3763234 (Etv4) RNA in situ')
        self.assertEqual(row3.text, 'MGI:3763145\n1 C 1C MGI:3763235 (Isl1) RNA in situ')
        self.assertEqual(row4.text, 'MGI:3763145\n1 D 1D MGI:3763235 (Isl1) RNA in situ')
        self.assertEqual(row5.text, 'MGI:3763147\n2 A 2A MGI:3763236 (Myod1) RNA in situ')
        self.assertEqual(row6.text, "MGI:3763147\n2 B 2B MGI:3763236 (Myod1) RNA in situ")
        self.assertEqual(row7.text, "MGI:3763147\n2 C 2C MGI:3763236 (Myod1) RNA in situ")
        self.assertEqual(row8.text, "MGI:3763147\n2 D 2D MGI:3763237 (Isl1) Immunohistochemistry")
        self.assertEqual(row9.text, "2D MGI:3763238 (Etv4) Immunohistochemistry")
        self.assertEqual(row10.text, "2D MGI:3763239 (Isl2) Immunohistochemistry")
        self.assertEqual(row11.text, "MGI:3763147\n2 E 2E MGI:3763237 (Isl1) Immunohistochemistry")
        self.assertEqual(row12.text, '2E MGI:3763238 (Etv4) Immunohistochemistry')
        self.assertEqual(row13.text, "2E MGI:3763239 (Isl2) Immunohistochemistry")
        self.assertEqual(row14.text, "MGI:3763147\n2 F 2F MGI:3763237 (Isl1) Immunohistochemistry")
        self.assertEqual(row15.text, "2F MGI:3763238 (Etv4) Immunohistochemistry")
        self.assertEqual(row16.text, '2F MGI:3763239 (Isl2) Immunohistochemistry')
        self.assertEqual(row17.text, 'MGI:3763149\n3 A 3A 40s MGI:3763245 (Etv4) In situ reporter (knock in)')
        self.assertEqual(row18.text, 'MGI:3763149\n3 B 3B 41s MGI:3763245 (Etv4) In situ reporter (knock in)')
        self.assertEqual(row19.text, "MGI:3763149\n3 C 3C 43s MGI:3763245 (Etv4) In situ reporter (knock in)")
        self.assertEqual(row20.text, "MGI:3763149\n3 D 3D 58s MGI:3763245 (Etv4) In situ reporter (knock in)")
        self.assertEqual(row21.text, 'MGI:3763149\n3 E 3E 39s, 3E 40s, 3E 41s, 3E 43-45s, 3E 47-48s MGI:3763245 (Etv4) In situ reporter (knock in)')
        self.assertEqual(row22.text, "MGI:3763151\n4 4 MGI:3763238 (Etv4) Immunohistochemistry")
        self.assertEqual(row23.text, "MGI:3763153\n5 F left 5F MGI:3776083 (Met) RNA in situ")
        self.assertEqual(row24.text, "MGI:3763153\n5 F right 5F right MGI:3776080 (Etv4) RNA in situ")
        self.assertEqual(row25.text, '5F MGI:3776083 (Met) RNA in situ')
        
        
    def test_multispecs_sameassay_samepane(self):
        """
        @status: Tests the display for image panes with multiple specimens from the same assay using the same image pane
        each specimen should have it's own row
        """
        driver = self.driver
        driver.get(TEST_PWI_URL)
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
        print(row1.text)
        print(row2.text)
        print(row3.text)
        print(row4.text)
        print(row5.text)
        print(row6.text)
        #asserts that the rows of data are correct for the first 13 rows
        self.assertEqual(row1.text, 'MGI:5750634\n3 A MGI:5750650 (H13) Northern blot')
        self.assertEqual(row2.text, 'MGI:5750637\n4 A 4A MGI:5750680 (H13) RNA in situ')
        self.assertEqual(row3.text, 'MGI:5750637\n4 B 4B MGI:5750680 (H13) RNA in situ')
        self.assertEqual(row4.text, 'MGI:5750637\n4 C 4C MGI:5750680 (H13) RNA in situ')
        self.assertEqual(row5.text, 'MGI:5750638\n5 _E5.5 5 E5.5 embryo, 5 E5.5 mother MGI:5750680 (H13) RNA in situ')
        self.assertEqual(row6.text, 'MGI:5750638\n5 _E6.5 5 E6.5 embryo, 5 E6.5 mother MGI:5750680 (H13) RNA in situ')
        self.assertEqual(row7.text, 'MGI:5750638\n5 _E7.5 5 E7.5 embryo, 5 E7.5 mother MGI:5750680 (H13) RNA in situ')
        self.assertEqual(row8.text, 'MGI:5750638\n5 _E8.5 5 E8.5 embryo, 5 E8.5 mother MGI:5750680 (H13) RNA in situ')
        self.assertEqual(row9.text, 'MGI:5750638\n5 _E9.5 5 E9.5 embryo, 5 E9.5 mother MGI:5750680 (H13) RNA in situ')
        self.assertEqual(row10.text, 'MGI:5750639\n6 _E10.5 6 E10.5 MGI:5750680 (H13) RNA in situ')
        self.assertEqual(row11.text, 'MGI:5750639\n6 _E11.5 6 E11.5 MGI:5750680 (H13) RNA in situ')
        self.assertEqual(row12.text, 'MGI:5750639\n6 _E13.5 6 E13.5 MGI:5750680 (H13) RNA in situ')
        self.assertEqual(row13.text, 'MGI:5750639\n6 _E14.5 6 E14.5 MGI:5750680 (H13) RNA in situ')

    def test_images_noassay(self):
        """
        @status: Tests the display for image panes with no attached assay
        each image and figure displayed but no assay or specimen
        """
        driver = self.driver
        driver.get(TEST_PWI_URL)
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
        #displays each row of data for the first 16 rows
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
        #asserts that the rows of data are correct for the first 16 rows
        self.assertEqual(row1.text, 'MGI:4453601\n2 b Fig. 1b MGI:4453599 (Tg(Scgb1a1-cre)1Tauc) In situ reporter (transgenic)')
        self.assertEqual(row2.text, 'MGI:4453603\n3 a Fig. 3a MGI:4453606 (Tg(Scgb1a1-cre)1Tauc) Recombinase reporter')
        self.assertEqual(row3.text, 'MGI:4453603\n3 c Fig. 3c MGI:4453606 (Tg(Scgb1a1-cre)1Tauc) Recombinase reporter')
        self.assertEqual(row4.text, 'MGI:4453603\n3 e Fig. 3e MGI:4453606 (Tg(Scgb1a1-cre)1Tauc) Recombinase reporter')
        self.assertEqual(row5.text, 'MGI:4453605\n4 a Fig. 4a MGI:4453606 (Tg(Scgb1a1-cre)1Tauc) Recombinase reporter')
        self.assertEqual(row6.text, 'MGI:4453605\n4 b Fig. 4b MGI:4453606 (Tg(Scgb1a1-cre)1Tauc) Recombinase reporter')
        self.assertEqual(row7.text, 'MGI:4453605\n4 c Fig. 4c MGI:4453606 (Tg(Scgb1a1-cre)1Tauc) Recombinase reporter')
        self.assertEqual(row8.text, 'MGI:4453605\n4 d Fig. 4d MGI:4453606 (Tg(Scgb1a1-cre)1Tauc) Recombinase reporter')
        self.assertEqual(row9.text, 'MGI:4453605\n4 e Fig. 4e MGI:4453606 (Tg(Scgb1a1-cre)1Tauc) Recombinase reporter')
        self.assertEqual(row10.text, 'MGI:4453605\n4 f Fig. 4f MGI:4453606 (Tg(Scgb1a1-cre)1Tauc) Recombinase reporter')
        self.assertEqual(row11.text, 'MGI:4453605\n4 g Fig. 4g MGI:4453606 (Tg(Scgb1a1-cre)1Tauc) Recombinase reporter')
        self.assertEqual(row12.text, 'MGI:4453605\n4 h Fig. 4h MGI:4453606 (Tg(Scgb1a1-cre)1Tauc) Recombinase reporter')
        self.assertEqual(row13.text, 'MGI:4453605\n4 i Fig. 4i MGI:4453606 (Tg(Scgb1a1-cre)1Tauc) Recombinase reporter')
        self.assertEqual(row14.text, 'MGI:4453605\n4 j Fig. 4j MGI:4453606 (Tg(Scgb1a1-cre)1Tauc) Recombinase reporter')
        self.assertEqual(row15.text, 'MGI:4453605\n4 k')
        self.assertEqual(row16.text, 'MGI:4453605\n4 l')
        

    def test_images_nospecimen(self):
        """
        @status: Tests the display for image panes with no specimen label
        each image, figure label, pane label, and assay displayed but no specimen label
        """
        driver = self.driver
        driver.get(TEST_PWI_URL)
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
        self.assertEqual(row1.text, 'MGI:4441359\n1 A 2ar MGI:4441369 (Spp1) Northern blot')
        self.assertEqual(row2.text, 'MGI:4441359\n1 A SPARC MGI:4441372 (Sparc) Northern blot')
        self.assertEqual(row3.text, 'MGI:4441359\n1 B 2ar MGI:4441380 (Spp1) Northern blot')
        self.assertEqual(row4.text, 'MGI:4441359\n1 B SPARC MGI:4441384 (Sparc) Northern blot')
        self.assertEqual(row5.text, 'MGI:4441361\n2 a/e 2a,e MGI:4441386 (Spp1) RNA in situ')
        self.assertEqual(row6.text, 'MGI:4441361\n2 b/f 2b,f MGI:4441386 (Spp1) RNA in situ')
        self.assertEqual(row7.text, 'MGI:4441361\n2 d/h 2d,h - decidua, 2d,h - embryo MGI:4441386 (Spp1) RNA in situ')
        self.assertEqual(row8.text, 'MGI:4441363\n3 a 3a MGI:4441386 (Spp1) RNA in situ')
        self.assertEqual(row9.text, 'MGI:4441363\n3 d/e 3d MGI:4441386 (Spp1) RNA in situ')
           
                   
    def tearDown(self):
        self.driver.close()
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPwiGxdImagePanePage))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))