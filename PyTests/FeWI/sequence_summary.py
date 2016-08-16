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

class TestAssaySummaryPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox() 

    def test_table_headers(self):
        """
        @status: Tests that the GXD Antibody Summary table headers are correct
        Headers are: MGI ID, Name, Type, Alias, Organism, Class, Notes, Name, MGI ID, Organism, Region, Markers, Reference
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
        @status: Tests that the default page sort is correct
        sort is by marker symbol, antibody name, antibody ID.
        """
        driver = self.driver
        driver.get(FEWI_URL)
        #opens the Marker detail page
        accidbox = driver.find_element_by_id('accessionForm').find_element_by_name('ids')
        # put your MGI ID number in the box
        accidbox.send_keys("MGI:97281")
        accidbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the antibodies link and clicks it
        driver.find_element_by_link_text("Antibodies").click()
        wait.forAjax(driver)
        #finds the antibody name column and then the first 12 items
        resultstable = driver.find_element_by_id("antibodySummary")
        rows = resultstable.find_elements_by_css_selector('tr')
        #displays each row of data for the first 18 rows
        row1 = rows[2]
        row2 = rows[3]
        row3 = rows[4]
        row4 = rows[5]
        row5 = rows[6]
        row6 = rows[7]
        row7 = rows[8]
        row8 = rows[9]
        row9 = rows[10]
        row10 = rows[11]
        row11 = rows[12]
        row12 = rows[13]
        row13 = rows[14]
        row14 = rows[15]
        row15 = rows[16]
        row16 = rows[17]
        row17 = rows[18]
        row18 = rows[19]
        #asserts that the rows of data are correct for the first 18 rows
        self.assertEqual(row1.text, "MGI:4843410 12F8 antibody rat Monoclonal Not Specified MGI:3576666 PSA-NCAM Not Specified polysialic acid portion of NCAM Ncam1 J:71338, Chung WW, J Comp Neurol 1991 Dec 8;314(2):290-305")
        self.assertEqual(row2.text, "MGI:2683335 5B8 anti-NCAM mouse, laboratory Monoclonal IgG1 Obtained from the Developmental Studies Hybridoma Bank, (T. Jessell and J. Dodd). Recognizes proteins from rat and mouse origin. MGI:2683334 spinal cord membranes rat Ncam1 J:51645, Mansouri A, Mech Dev 1998 Nov;78(1-2):171-8")
        self.assertEqual(row3.text, "MGI:4843413 8A2 antibody rat Monoclonal Not Specified MGI:4843412 N-CAM (8A2) Not Specified Ncam1 J:71338, Chung WW, J Comp Neurol 1991 Dec 8;314(2):290-305")
        self.assertEqual(row4.text, "MGI:5468461 Anti-N-CAM rat Monoclonal Not Specified The antibody was obtained from Chemicon. MGI:5468460 N-CAM Not Specified Ncam1 J:29480, Aoki K, Anat Embryol (Berl) 1995 Sep;192(3):211-20")
        self.assertEqual(row5.text, "MGI:5505540 Anti-N-CAM rabbit Not Specified Not Specified Antibody preparation was described in Rasmussen, S. et al. (1982) Scand J. Immunol. 15:179-85. MGI:5505539 N-CAM Not Specified Ncam1 J:52451, Esni F, J Cell Biol 1999 Jan 25;144(2):325-37")
        self.assertEqual(row6.text, "MGI:5473599 Anti-NCAM rabbit Polyclonal Not Applicable This antibody was obtained from Chemicon. MGI:5473598 NCAM chicken Ncam1 J:34596, Davis JA, J Neurosci 1996 Aug 15;16(16):5082-94")
        self.assertEqual(row7.text, "MGI:2676461 E-NCAM antibody mouse, laboratory Not Specified IgG1 Recognizes the polysialylyated embryonic form of the protein. MGI:2676460 E-NCAM Not Specified This represents the sialylated form of NCAM. Ncam1 J:83933, Cheng A, Dev Biol 2003 Jun 15;258(2):319-33")
        self.assertEqual(row8.text, "MGI:5490822 H28 Not Specified Not Specified Not Specified MGI:5490821 NCAM Not Specified Ncam1 J:30289, Matsunami H, Dev Biol 1995 Dec;172(2):466-78")
        self.assertEqual(row9.text, "MGI:1934887 H28.123 H28123 rat Monoclonal IgG2a Antibody was purchased from AMAC Inc., Westbrook, ME or Chemicon. MGI:4359385 Neural Cell Adhesion Molecule mouse, laboratory glycoprotein fraction Ncam1 J:2360, Moase CE, Development 1991 Nov;113(3):1049-58")
        self.assertEqual(row10.text, "MGI:1934839 N-CAM polyclonal antibody rabbit Polyclonal Not Applicable Antibody was provided by Dr. Urs Rutishauser. Antibody detects the various N-CAM isoforms. MGI:1934201 NCAM mouse, laboratory The antigen domain is located near or at the cytoplasmic side of the plasma membrane. Ncam1 J:2360, Moase CE, Development 1991 Nov;113(3):1049-58")
        self.assertEqual(row11.text, "MGI:1289934 NCAM ab rabbit Polyclonal Not Specified MGI:1277577 neural cell adhesion molecule Not Specified Ncam1 J:49909, Ba-Charvet KT, Development 1998 Nov;125(21):4273-82")
        self.assertEqual(row12.text, "MGI:3043764 NCAM antibody Not Specified Not Specified Not Specified MGI:1277577 neural cell adhesion molecule Not Specified Ncam1 J:63183, Kramer PR, Mech Dev 2000 Jun;94(1-2):79-94")
        self.assertEqual(row13.text, "MGI:3578932 NCAM antibody rabbit Polyclonal Not Specified MGI:1277577 neural cell adhesion molecule Not Specified Ncam1 J:90285, Gittenberger-De Groot AC, Dev Dyn 2004 Jun;230(2):378-84")
        self.assertEqual(row14.text, "MGI:5491181 NCAM antibody Not Specified Monoclonal Not Specified MGI:1277577 neural cell adhesion molecule Not Specified Ncam1 J:25271, Whitesides JG 3rd, Dev Biol 1995 May;169(1):229-41")
        self.assertEqual(row15.text, "MGI:5556104 NCAM antibody (AB5032) rabbit Polyclonal Not Specified Affinity purified. Obtained from Chemicon. MGI:5556102 NCAM chicken highly purified Ncam1 J:130159, Van den Akker NM, Dev Dyn 2008 Feb;237(2):494-503")
        self.assertEqual(row16.text, "MGI:3574201 PSA-NCAM anti-Men B mouse, laboratory Monoclonal IgM Antibody can be obtained from Chemicon, clone 2-2B. Reacts with alpha 2-8 linked neuraminic acid (NeuAc-alpha 2-8) n with n>10. MGI:3574200 Viable Meningococcus group B (strain 355) bacteria Ncam1 J:32118, Boisseau S, Development 1991 May;112(1):69-82")
        self.assertEqual(row17.text, "MGI:3576668 PSA-NCAM (12E3) mouse, laboratory Monoclonal IgM Antibody described in Seki and Arai; Anat Embryol (Berl). 1991;184(4):395-401. MGI:3576666 PSA-NCAM Not Specified polysialic acid portion of NCAM Ncam1 J:95331, Daniel D, Gene Expr Patterns 2005 Feb;5(3):317-22")
        self.assertEqual(row18.text, "MGI:5467593 anti-N-CAM Not Specified Not Specified Not Specified This antibody recognizes all polypeptide forms. MGI:1277577 neural cell adhesion molecule Not Specified Ncam1 J:21489, Wray S, Dev Biol 1994 Nov;166(1):349-54")
        
        
        details = resultstable.find_elements_by_css_selector('td:nth-child(1)')

        detail17 = details[17]
        detail18 = details[18]
        detail19 = details[19]
        detail20 = details[20]
        
        #asserts the first 4 anti-N-CAM antibodies are listed and in correct sort order
        
        self.assertEqual(detail17.text, "MGI:5467593")
        self.assertEqual(detail18.text, "MGI:5608897")
        self.assertEqual(detail19.text, "MGI:5758921")
        self.assertEqual(detail20.text, "MGI:5608904")
        
        
    def tearDown(self):
        self.driver.close()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAssaySummaryPage))
    return suite

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSpecSumByRef']
    unittest.main()