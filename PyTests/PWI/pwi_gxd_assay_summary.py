'''

Created on Apr 18, 2016
verified working on Scrum 6/6/2023
@author: jeffc
'''
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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table
from config import TEST_PWI_URL

#Tests
tracemalloc.start()
class TestPwiGxdAssaySummaryPage(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1800, 1000)

    def test_table_headers(self):
        """
        @status: Tests that the GXD/CRE Assays Summary table headers are correct
        Result Details, Gene, Assay Type, Reference
        """
        driver = self.driver
        driver.get(TEST_PWI_URL)
        self.form = ModuleForm(self.driver)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        #find the Acc ID(s) / Gene Symbol box and enter text
        accbox = driver.find_element(By.NAME, 'ids')
        # put your J number in the box
        accbox.send_keys("J:208450")
        accbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Assays')))#waits until the Assays link is displayed on the page
        #finds the specimens link and clicks it
        driver.find_element(By.LINK_TEXT, "Assays").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'dataTable')))  # wait for the assay results to display
        #Locates the summary table and finds the table headings
        headerlist = driver.find_element(By.CLASS_NAME, "dataTable")
        items = headerlist.find_elements(By.TAG_NAME, "th")
        searchTextItems = iterate.getTextAsList(items)
        #verifies all the table headings are correct and in order
        self.assertEqual(searchTextItems, ['Result Details','Gene','Assay Type','Reference', 'Assay Notes'])

    def test_page_sort(self):
        """
        @status: Tests that the default page sort is correct
        sort is by marker, assay type, first reference author, and MGI ID.
        """
        driver = self.driver
        driver.get(TEST_PWI_URL)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)'))) # waits until the PWI ACC input field is displayed on the page
        #find the Acc ID(s) / Gene Symbol box and enter text
        accbox = driver.find_element(By.NAME, 'ids')
        # put your J number in the box
        accbox.send_keys("J:208450")
        accbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, 'Assays')))#waits until the Assays link is displayed on the page
        #finds the GXD/CRE Assays link and clicks it
        driver.find_element(By.LINK_TEXT, "Assays").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'dataTable')))  # wait for the assay results to display
        #finds the specimen label column and then the first 12 items
        resultstable = driver.find_element(By.CLASS_NAME, "dataTable")
        rows = resultstable.find_elements(By.CSS_SELECTOR, 'tr')
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
        self.assertEqual(row1.text, "MGI:5688746 Agtr2 RNA in situ J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711")
        self.assertEqual(row2.text, "MGI:5688735 Agtr2 RT-PCR J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711")
        self.assertEqual(row3.text, "MGI:5688736 Agtr2 RT-PCR J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711")
        self.assertEqual(row4.text, "MGI:5688737 Agtr2 RT-PCR J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711")
        self.assertEqual(row5.text, "MGI:5688738 Agtr2 RT-PCR J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711")
        self.assertEqual(row6.text, "MGI:5688739 Agtr2 RT-PCR J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711")
        self.assertEqual(row7.text, "MGI:5688740 Agtr2 RT-PCR J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711")
        self.assertEqual(row8.text, "MGI:5688741 Agtr2 RT-PCR J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711")
        self.assertEqual(row9.text, "MGI:5688742 Agtr2 RT-PCR J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711")
        self.assertEqual(row10.text, "MGI:5688754 Mtus1 Immunohistochemistry J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711")
        self.assertEqual(row11.text, "MGI:5688745 Mtus1 RNA in situ J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711")
        self.assertEqual(row12.text, "MGI:5688744 Mtus1 In situ reporter (knock in) J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711")
        self.assertEqual(row13.text, "MGI:5688692 Mtus1 RT-PCR J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711 The primer set used in this assay is designed to amplify all three murine isoforms.")
        self.assertEqual(row14.text, "MGI:5688694 Mtus1 RT-PCR J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711 The primer set used in this assay is designed to amplify all three murine isoforms.")
        self.assertEqual(row15.text, "MGI:5688695 Mtus1 RT-PCR J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711 The primer set used in this assay is designed to amplify all three murine isoforms.")
        self.assertEqual(row16.text, "MGI:5688696 Mtus1 RT-PCR J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711 The primer set used in this assay is designed to amplify all three murine isoforms.")
        self.assertEqual(row17.text, "MGI:5688697 Mtus1 RT-PCR J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711 The primer set used in this assay is designed to amplify all three murine isoforms.")
        self.assertEqual(row18.text, "MGI:5688698 Mtus1 RT-PCR J:208450 Bundschu K, Dev Dyn 2014 May;243(5):699-711 The primer set used in this assay is designed to amplify all three murine isoforms.")
        
        details = resultstable.find_elements(By.CSS_SELECTOR, 'td:nth-child(1)')
        detail1 = details[0]
        detail2 = details[1]
        detail3 = details[2]
        detail4 = details[3]
        detail5 = details[4]
        detail6 = details[5]
        detail7 = details[6]
        detail8 = details[7]
        detail9 = details[8]
        detail10 = details[9]
        detail11 = details[10]
        detail12 = details[11]
        detail13 = details[12]
        detail14 = details[13]
        detail15 = details[14]
        detail16 = details[15]
        #asserts the first 16 specimen labels are correct and in correct order
        self.assertEqual(detail1.text, "MGI:5688746")
        self.assertEqual(detail2.text, "MGI:5688735")
        self.assertEqual(detail3.text, "MGI:5688736")
        self.assertEqual(detail4.text, "MGI:5688737")
        self.assertEqual(detail5.text, "MGI:5688738")
        self.assertEqual(detail6.text, "MGI:5688739")
        self.assertEqual(detail7.text, "MGI:5688740")
        self.assertEqual(detail8.text, "MGI:5688741")
        self.assertEqual(detail9.text, "MGI:5688742")
        self.assertEqual(detail10.text, "MGI:5688754")
        self.assertEqual(detail11.text, "MGI:5688745")
        self.assertEqual(detail12.text, "MGI:5688744")
        self.assertEqual(detail13.text, "MGI:5688692")
        self.assertEqual(detail14.text, "MGI:5688694")
        self.assertEqual(detail15.text, "MGI:5688695")
        self.assertEqual(detail16.text, "MGI:5688696")
        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPwiGxdAssaySummaryPage))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))