'''
Created on Jul 20, 2016
verified working on Scrum 6/6/2023
@author: jeffc
'''
import tracemalloc
import unittest
import time
import tracemalloc
import config
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import wait, iterate
from config import TEST_PWI_URL

#Tests
tracemalloc.start()
class TestPwiGxdAntibodySummaryPage(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1800, 1000)

    def test_table_headers(self):
        """
        @status: Tests that the GXD Antibody Summary table headers are correct
        Headers are: MGI ID, Name, Type, Alias, Organism, Class, Notes, Name, MGI ID, Organism, Region, Markers, Reference
        """
        driver = self.driver
        driver.get(TEST_PWI_URL)
        #opens the PWI page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        accidbox = driver.find_element(By.ID, 'accessionForm').find_element(By.NAME, 'ids')
        # put your MGI ID number in the box
        accidbox.send_keys("MGI:97281")
        accidbox.send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Antibodies'))) # wait for the Antibodies link to display
        #finds the antibodies link and clicks it
        driver.find_element(By.LINK_TEXT, "Antibodies").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'antibodySummary'))) #wait for the antibody results to display
        #Locates the antibodies summary table and finds the table headings
        headerlist = driver.find_element(By.ID, "antibodySummary")
        items = headerlist.find_elements(By.TAG_NAME, "th")
        searchTextItems = iterate.getTextAsList(items)
        #verifies all the table headings are correct and in order
        self.assertEqual(searchTextItems, ['Antibody Fields','Antigen Fields','','MGI ID','Markers','Name','Alias(es)','Organism','Type','Class','Notes','MGI ID','Name','Organism','Region','Notes','Reference'])
        
    def test_page_sort(self):
        """
        @status: Tests that the default page sort is correct
        sort is by marker symbol, antibody name, antibody ID.
        """
        driver = self.driver
        driver.get(TEST_PWI_URL)
        #opens the Marker detail page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        accidbox = driver.find_element(By.ID, 'accessionForm').find_element(By.NAME, 'ids')
        # put your MGI ID number in the box
        accidbox.send_keys("MGI:97281")
        accidbox.send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Antibodies')))  # wait for the Antibodies link to display
        #finds the antibodies link and clicks it
        driver.find_element(By.LINK_TEXT, "Antibodies").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'antibodySummary')))  # wait for the antibody results to display
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
        print (row2.text)
        print (row8.text)
        print (row11.text)
        #asserts that the rows of data are correct for the first 18 rows
        self.assertEqual(row1.text, "MGI:3623996 Ncam1 12F11 antibody rat Monoclonal IgG2a Affinity chromatography purified. Obtained from BD Pharmingen, clone 12F11, #556323. Recognizes an intracellular epitope of N-CAM. Crossreacts with: Chicken, Human, Rat. MGI:3623995 BALB/c mouse thymocytes mouse, laboratory J:93589, Kolterud A, Development 2004 Nov;131(21):5319-26")
        self.assertEqual(row2.text, "MGI:4843410 Ncam1 12F8 antibody rat Monoclonal Not Specified MGI:3576666 PSA-NCAM Not Specified polysialic acid portion of NCAM J:71338, Chung WW, J Comp Neurol 1991 Dec 8;314(2):290-305")
        self.assertEqual(row3.text, "MGI:6143850 Ncam1 5A5 antibody CD56,anti-NCAM-PSA,anti-PSA mouse, laboratory Monoclonal IgM Obtained from the Developmental Studies Hybridoma Bank, (T. Jessell and J. Dodd). Recognizes proteins from rat and mouse origin. MGI:4359869 PSA-NCAM rat polysialylglycan chain J:19896, Weinstein DC, Cell 1994 Aug 26;78(4):575-88")
        self.assertEqual(row4.text, "MGI:2683335 Ncam1 5B8 antibody anti-NCAM mouse, laboratory Monoclonal IgG1 Obtained from the Developmental Studies Hybridoma Bank, (T. Jessell and J. Dodd). Recognizes proteins from rat and mouse origin. MGI:2683334 spinal cord membranes rat J:62088, Yao J, Mech Dev 2000 May;93(1-2):105-15")
        self.assertEqual(row5.text, "MGI:4843413 Ncam1 8A2 antibody rat Monoclonal Not Specified MGI:4843412 N-CAM (8A2) Not Specified J:71338, Chung WW, J Comp Neurol 1991 Dec 8;314(2):290-305")
        self.assertEqual(row6.text, "MGI:5468461 Ncam1 Anti-N-CAM rat Monoclonal Not Specified The antibody was obtained from Chemicon. MGI:5468460 N-CAM Not Specified J:29480, Aoki K, Anat Embryol (Berl) 1995 Sep;192(3):211-20")
        self.assertEqual(row7.text, "MGI:5505540 Ncam1 Anti-N-CAM rabbit Not Specified Not Specified Antibody preparation was described in Rasmussen, S. et al. (1982) Scand J. Immunol. 15:179-85. MGI:5505539 N-CAM Not Specified J:52451, Esni F, J Cell Biol 1999 Jan 25;144(2):325-37")
        self.assertEqual(row8.text, "MGI:6276310 Ncam1 Anti-N-CAM Not Specified Polyclonal Not Applicable MGI:5505539 N-CAM Not Specified J:46176, Holst BD, Proc Natl Acad Sci U S A 1998 Mar 3;95(5):2597-602")
        self.assertEqual(row9.text, "MGI:6303801 Ncam1 Anti-N-CAM Not Specified Not Specified Not Specified MGI:5468460 N-CAM Not Specified J:47986, Dellovade TL, Brain Res Dev Brain Res 1998 May 15;107(2):233-40")
        self.assertEqual(row10.text, "MGI:5473599 Ncam1 Anti-NCAM rabbit Polyclonal Not Applicable This antibody was obtained from Chemicon. MGI:5473598 NCAM chicken J:34596, Davis JA, J Neurosci 1996 Aug 15;16(16):5082-94")
        self.assertEqual(row11.text, "MGI:5810708 Ncam1 Anti-NCAM Not Specified Monoclonal Not Specified This antibody was obtained from Developmental Studies Hybridoma Bank but no details were provided; multiple antibodies that recognize this protein are available from this vendor. MGI:5490821 NCAM Not Specified J:51645, Mansouri A, Mech Dev 1998 Nov;78(1-2):171-8")
        
        details = resultstable.find_elements(By.CSS_SELECTOR, 'td:nth-child(1)')

        detail4 = details[4]
        detail5 = details[5]
        detail6 = details[6]
        detail7 = details[7]
        
        #asserts the first 4 anti-N-CAM antibodies are listed and in correct sort order
        
        self.assertEqual(detail4.text, "MGI:4843413")
        self.assertEqual(detail5.text, "MGI:5468461")
        self.assertEqual(detail6.text, "MGI:5505540")
        self.assertEqual(detail7.text, "MGI:6276310")
        
        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPwiGxdAntibodySummaryPage))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))