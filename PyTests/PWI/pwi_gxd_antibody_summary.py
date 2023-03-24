'''
Created on Jul 20, 2016

This page is linked to from the References page
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
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import TEST_PWI_URL

class TestPwiGxdAntibodySummaryPage(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox() 

    def test_table_headers(self):
        """
        @status: Tests that the GXD Antibody Summary table headers are correct
        Headers are: MGI ID, Name, Type, Alias, Organism, Class, Notes, Name, MGI ID, Organism, Region, Markers, Reference
        """
        driver = self.driver
        driver.get(TEST_PWI_URL)
        #opens the Marker detail page
        accidbox = driver.find_element(By.ID, 'accessionForm').find_element(By.NAME, 'ids')
        # put your MGI ID number in the box
        accidbox.send_keys("MGI:97281")
        accidbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the antibodies link and clicks it
        driver.find_element(By.LINK_TEXT, "Antibodies").click()
        wait.forAjax(driver)
        #Locates the antibodies summary table and finds the table headings
        headerlist = driver.find_element(By.ID, "antibodySummary")
        items = headerlist.find_elements(By.TAG_NAME, "th")
        searchTextItems = iterate.getTextAsList(items)
        wait.forAjax(driver)
        #verifies all the table headings are correct and in order
        self.assertEqual(searchTextItems, ['Antibody Fields','Antigen Fields','','MGI ID', 'Name','Alias(es)','Organism','Type','Class','Notes','MGI ID','Name','Organism','Region','Notes','Markers','Reference'])
        
    def test_page_sort(self):
        """
        @status: Tests that the default page sort is correct
        sort is by marker symbol, antibody name, antibody ID.
        """
        driver = self.driver
        driver.get(TEST_PWI_URL)
        #opens the Marker detail page
        accidbox = driver.find_element(By.ID, 'accessionForm').find_element(By.NAME, 'ids')
        # put your MGI ID number in the box
        accidbox.send_keys("MGI:97281")
        accidbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the antibodies link and clicks it
        driver.find_element(By.LINK_TEXT, "Antibodies").click()
        wait.forAjax(driver)
        #finds the antibody name column and then the first 12 items
        resultstable = driver.find_element(By.ID, "antibodySummary")
        rows = resultstable.find_elements(By.CSS_SELECTOR, 'tr')
        #displays each row of data for the first 21 rows
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
        row19 = rows[20]
        row20 = rows[21]
        row21 = rows[22]
        row22 = rows[23]
        row23 = rows[24]
        row24 = rows[25]
        row25 = rows[26]
        row26 = rows[27]
        row27 = rows[28]
        row28 = rows[29]
        row29 = rows[30]
        print (row2.text)
        print (row8.text)
        print (row11.text)
        print (row16.text)
        #asserts that the rows of data are correct for the first 18 rows
        self.assertEqual(row1.text, "MGI:4843410 12F8 antibody [] rat Monoclonal Not Specified MGI:3576666 PSA-NCAM Not Specified polysialic acid portion of NCAM Ncam1 J:18836, Hankin MH, J Neurobiol 1994 May;25(5):472-87")
        self.assertEqual(row2.text, "MGI:6143850 5A5 anti-NCAM-PSA, CD56, anti-PSA mouse, laboratory Monoclonal IgM Obtained from the Developmental Studies Hybridoma Bank, (T. Jessell and J. Dodd). Recognizes proteins from rat and mouse origin. MGI:4359869 PSA-NCAM rat polysialylglycan chain Ncam1 J:19896, Weinstein DC, Cell 1994 Aug 26;78(4):575-88")
        self.assertEqual(row3.text, "MGI:2683335 5B8 anti-NCAM mouse, laboratory Monoclonal IgG1 Obtained from the Developmental Studies Hybridoma Bank, (T. Jessell and J. Dodd). Recognizes proteins from rat and mouse origin. MGI:2683334 spinal cord membranes rat Ncam1 J:51645, Mansouri A, Mech Dev 1998 Nov;78(1-2):171-8")
        self.assertEqual(row4.text, "MGI:4843413 8A2 antibody [] rat Monoclonal Not Specified MGI:4843412 N-CAM (8A2) Not Specified Ncam1 J:71338, Chung WW, J Comp Neurol 1991 Dec 8;314(2):290-305")
        self.assertEqual(row5.text, "MGI:5468461 Anti-N-CAM [] rat Monoclonal Not Specified The antibody was obtained from Chemicon. MGI:5468460 N-CAM Not Specified Ncam1 J:29480, Aoki K, Anat Embryol (Berl) 1995 Sep;192(3):211-20")
        self.assertEqual(row6.text, "MGI:5505540 Anti-N-CAM [] rabbit Not Specified Not Specified Antibody preparation was described in Rasmussen, S. et al. (1982) Scand J. Immunol. 15:179-85. MGI:5505539 N-CAM Not Specified Ncam1 J:52451, Esni F, J Cell Biol 1999 Jan 25;144(2):325-37")
        self.assertEqual(row7.text, "MGI:6276310 Anti-N-CAM [] Not Specified Polyclonal Not Applicable MGI:5505539 N-CAM Not Specified Ncam1 J:46176, Holst BD, Proc Natl Acad Sci U S A 1998 Mar 3;95(5):2597-602")
        self.assertEqual(row8.text, "MGI:6303801 Anti-N-CAM [] Not Specified Not Specified Not Specified MGI:5468460 N-CAM Not Specified Ncam1 J:47986, Dellovade TL, Brain Res Dev Brain Res 1998 May 15;107(2):233-40")
        self.assertEqual(row9.text, "MGI:5473599 Anti-NCAM [] rabbit Polyclonal Not Applicable This antibody was obtained from Chemicon. MGI:5473598 NCAM chicken Ncam1 J:34596, Davis JA, J Neurosci 1996 Aug 15;16(16):5082-94")
        self.assertEqual(row10.text, "MGI:5810708 Anti-NCAM [] Not Specified Monoclonal Not Specified This antibody was obtained from Developmental Studies Hybridoma Bank but no details were provided; multiple antibodies that recognize this protein are available from this vendor. MGI:5490821 NCAM Not Specified Ncam1 J:51645, Mansouri A, Mech Dev 1998 Nov;78(1-2):171-8")
        self.assertEqual(row11.text, "MGI:6258395 Anti-NCAM [] rabbit Polyclonal Not Applicable This antibody was obtained from Chemicon. MGI:6198740 NCAM rat Ncam1 J:31081, Wilson DB, J Craniofac Genet Dev Biol 1995 Oct-Dec;15(4):182-9")
        self.assertEqual(row12.text, "MGI:6115364 Anti-PSA-NCAM [] Not Specified Not Specified Not Specified The antibody recognized the polysialylated form of the protein. MGI:5490821 NCAM Not Specified Ncam1 J:128536, Watanabe A, PLoS Biol 2007 Nov;5(11):e297")
        self.assertEqual(row13.text, "MGI:6389031 Anti-PSA-NCAM [] mouse, laboratory Monoclonal Not Specified This antibody was obtained from AbCys, but no details were provided. MGI:5490821 NCAM Not Specified Ncam1 J:262004, Espana-Serrano L, Cereb Cortex 2017 May 1;27(5):2809-2819")
        self.assertEqual(row14.text, "MGI:2676461 E-NCAM antibody [] mouse, laboratory Not Specified IgG1 Recognizes the polysialylyated embryonic form of the protein. MGI:2676460 E-NCAM Not Specified This represents the sialylated form of NCAM. Ncam1 J:83933, Cheng A, Dev Biol 2003 Jun 15;258(2):319-33")
        self.assertEqual(row15.text, "MGI:5490822 H28 [] Not Specified Not Specified Not Specified MGI:5490821 NCAM Not Specified Ncam1 J:30289, Matsunami H, Dev Biol 1995 Dec;172(2):466-78")
        self.assertEqual(row16.text, "MGI:6452844 H28 antibody [] rat Monoclonal Not Specified Antibody preparation is described in Hirn et al., 1981 Brain Res. 214, 433-439. This antibody reacts with an extracellular domain and recognizes the three isofroms of this protein. MGI:6452842 glycoprotein mouse, laboratory High molecular weight glycoproteins were extracted from crude membranes of whole brain. Ncam1 J:290840, Klein G, Development 1988 Apr;102(4):749-61")
        self.assertEqual(row17.text, "MGI:1934887 H28.123 H28123 rat Monoclonal IgG2a Antibody was purchased from GeneTex, Boehringer Mannheim, AMAC Inc., Westbrook, ME or Chemicon. MGI:4359385 Neural Cell Adhesion Molecule mouse, laboratory glycoprotein fraction Ncam1 J:2360, Moase CE, Development 1991 Nov;113(3):1049-58")
        self.assertEqual(row18.text, "MGI:5897397 N-CAM antibody [] rabbit Polyclonal Not Applicable MGI:5897394 N-CAM rat Ncam1 J:22338, Kimber SJ, Eur J Cell Biol 1994 Feb;63(1):102-13")
        self.assertEqual(row19.text, "MGI:5882120 N-CAM antibody H28 [] mouse, laboratory Monoclonal Not Specified This antibody was obtained from Boehringer Mannheim. MGI:5468460 N-CAM Not Specified Ncam1 J:21481, Rose O, Dev Dyn 1994 Nov;201(3):245-59")
        self.assertEqual(row20.text, "MGI:1934839 N-CAM polyclonal antibody [] rabbit Polyclonal Not Applicable Antibody was provided by Dr. Urs Rutishauser. Antibody detects the various N-CAM isoforms. MGI:1934201 NCAM mouse, laboratory The antigen domain is located near or at the cytoplasmic side of the plasma membrane. Ncam1 J:2360, Moase CE, Development 1991 Nov;113(3):1049-58")
        self.assertEqual(row21.text, "MGI:1289934 NCAM ab [] rabbit Polyclonal Not Specified MGI:1277577 neural cell adhesion molecule Not Specified Ncam1 J:49909, Ba-Charvet KT, Development 1998 Nov;125(21):4273-82")
        self.assertEqual(row22.text, "MGI:3043764 NCAM antibody [] Not Specified Not Specified Not Specified MGI:1277577 neural cell adhesion molecule Not Specified Ncam1 J:63183, Kramer PR, Mech Dev 2000 Jun;94(1-2):79-94")
        self.assertEqual(row23.text, "MGI:3578932 NCAM antibody [] rabbit Polyclonal Not Specified MGI:1277577 neural cell adhesion molecule Not Specified Ncam1 J:90285, Gittenberger-De Groot AC, Dev Dyn 2004 Jun;230(2):378-84")
        self.assertEqual(row24.text, "MGI:5491181 NCAM antibody [] Not Specified Monoclonal Not Specified MGI:1277577 neural cell adhesion molecule Not Specified Ncam1 J:25271, Whitesides JG 3rd, Dev Biol 1995 May;169(1):229-41")
        self.assertEqual(row25.text, "MGI:5556104 NCAM antibody (AB5032) [] rabbit Polyclonal Not Specified Affinity purified. Obtained from Chemicon. MGI:5556102 NCAM chicken highly purified Ncam1 J:130159, Van den Akker NM, Dev Dyn 2008 Feb;237(2):494-503")
        self.assertEqual(row26.text, "MGI:6478223 NCAM-H antibody [] mouse, laboratory Monoclonal Not Specified Described in Seki T (1992) Anat Embryol 184(4):395-401. MGI:6478217 NCAM-H Not Specified polysialic acid chains Ncam1 J:48402, Ohyama K, Brain Res Dev Brain Res 1998 May 15;107(2):219-26")
        self.assertEqual(row27.text, "MGI:3576668 PSA-NCAM (12E3) [] mouse, laboratory Monoclonal IgM Antibody described in Seki and Arai; Anat Embryol (Berl). 1991;184(4):395-401. MGI:3576666 PSA-NCAM Not Specified polysialic acid portion of NCAM Ncam1 J:95331, Daniel D, Gene Expr Patterns 2005 Feb;5(3):317-22")
        self.assertEqual(row28.text, "MGI:3574201 PSA-NCAM (clone 2-2B) anti-Men B mouse, laboratory Monoclonal IgM Antibody obtained from Chemicon/Millipore. Reacts with alpha 2-8 linked neuraminic acid (NeuAc-alpha 2-8) n with n>10. MGI:3574200 Viable Meningococcus group B (strain 355) bacteria Ncam1 J:32118, Boisseau S, Development 1991 May;112(1):69-82")
        self.assertEqual(row29.text, "MGI:5467593 anti-N-CAM [] Not Specified Not Specified Not Specified This antibody recognizes all polypeptide forms. MGI:1277577 neural cell adhesion molecule Not Specified Ncam1 J:21489, Wray S, Dev Biol 1994 Nov;166(1):349-54")
        
        
        details = resultstable.find_elements(By.CSS_SELECTOR, 'td:nth-child(1)')

        detail4 = details[4]
        detail5 = details[5]
        detail6 = details[6]
        detail7 = details[7]
        
        #asserts the first 4 anti-N-CAM antibodies are listed and in correct sort order
        
        self.assertEqual(detail4.text, "MGI:5468461")
        self.assertEqual(detail5.text, "MGI:5505540")
        self.assertEqual(detail6.text, "MGI:6276310")
        self.assertEqual(detail7.text, "MGI:6303801")
        
        
    def tearDown(self):
        self.driver.close()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPwiGxdAntibodySummaryPage))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))