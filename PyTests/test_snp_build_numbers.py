'''
Created on Mar 21, 2016
Tests that the SNP build number or mouse build numbe ris correct for the following pages:
SNP query form
SNP summary page
GXD query form
Marker query form
Marker detail page
HMDC query page
@author: jeffc
'''
import unittest
import time
import tracemalloc
import time
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
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate
from config.config import PUBLIC_URL
from util import iterate, wait

#Tests
tracemalloc.start()
class TestSnpBuildNumbers(unittest.TestCase):


    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.PUBLIC_URL)
        

    def test_snp_qf(self):
        """
        @Status this test works
        Checks the dbSNp and mouse build numbers on the snp query form and snp summary page
        """
        print ("BEGIN test_snp_qf")
        self.driver.get(PUBLIC_URL + "/snp/")
        #finds the build number at the top of the snp QF page Search by Region tab
        self.driver.find_element(By.ID, 'ui-id-2').click
        buildlabel = self.driver.find_element(By.CSS_SELECTOR, '#form2 > div:nth-child(2)').get_attribute("outerHTML")
        #print (buildlabel)
        self.assertIn("GRCm39", buildlabel)

        #click back to the Search by Gene tab
        self.driver.find_element(By.ID, 'ui-id-1').click
        genebox = self.driver.find_element(By.ID, 'nomen')
        #enters pax6 in the Gene Symbol/Name box
        genebox.send_keys("pax6")
        genebox.send_keys(Keys.RETURN)
        #Does a webdriver wait until the export buttons are present so we know the page is loaded
        if WebDriverWait(self.driver, 8).until(ec.presence_of_element_located((By.ID, 'exportButtons'))):
            print('page loaded')
        #finds the snp build number in the heading of SNP ID column
        snpidLabel = self.driver.find_element(By.ID, 'snpSummaryTable').find_element(By.ID, 'snp_id')
        self.assertIn("(GRCm39)", snpidLabel.text)
        #finds the GRC build number in the heading of Map Position column
        mapLabel = self.driver.find_element(By.ID, 'snpSummaryTable').find_element(By.ID, 'map_position')
        self.assertIn("(GRCm39)", mapLabel.text)

    def test_gxd_qf(self):
        """
        @Status this test works
        Checks the mouse build numbers on the gxd query form
        """
        print ("BEGIN test_gxd_qf")
        self.driver.get(PUBLIC_URL + "/gxd/")
        #finds the build number in the Genome Location of the gxd QF page
        formLabel = self.driver.find_element(By.CSS_SELECTOR, '#gxdQueryForm > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2)')
        self.assertIn("genome build GRCm39", formLabel.text)
        
    def test_mrk_detail_build(self):
        """
        @Status this test works
        Checks the mouse build number on a marker detail page
        """
        print ("BEGIN test_mrk_detail_build")
        #displays the marker detail page for pax6
        self.driver.get(PUBLIC_URL + "/marker/MGI:1096368")
        time.sleep(2)
        #opens the Location & Maps section
        #self.driver.find_element(By.ID, 'lmToggle').click()
        #finds the build number in the Sequence map section
        seqmapLabel = self.driver.find_element(By.CLASS_NAME, 'detailData2').find_element(By.CLASS_NAME, 'summarySec1').find_element(By.CSS_SELECTOR, 'div.value')
        print(seqmapLabel.text)
        #verifies GRCm39 is displayed in this section
        self.assertIn("GRCm39", seqmapLabel.text)

    def test_mrk_qf_build(self):
        """
        @Status this test works
        Checks the mouse build number on the marker query form
        """
        print ("BEGIN test_mrk_qf_build")
        #displays the marker qf
        self.driver.get(PUBLIC_URL + "/marker")
        #finds the genome coordinates link
        genocoord = self.driver.find_element(By.LINK_TEXT, 'Genome Coordinates')
        # get the parent element
        gcParent = genocoord.find_element(By.XPATH, '..')
        #confirms  that GRCm39 is displayed
        self.assertIn("GRCm39", gcParent.text)
        
    def test_hmdc_build(self):
        """
        @Status this test has been updated for the new hmdc pages
        checks the human and mouse build numbers on the HMDC query page
        @bug need to figure out why assertion for my_select.text not working!
        """
        print ("BEGIN test_hmdc_build")
        #displays the HMDC qf
        self.driver.get(PUBLIC_URL + "/diseasePortal")
        #find the pulldown and select Genome Location
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        print(my_select.text)
        # verifies all the items listed in the pulldown are correct and in order
        #self.assertEqual(my_select.text,['Please select a field\nGene Symbol(s) or ID(s)\nGene Name\nDisease or Phenotype Name\nDisease or Phenotype ID(s)\nGenome Location\nGene File Upload'])
        #select option Genome Location
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Genome Location':
                option.click()
                break

        #finds the human and mouse genome build numbers
        buildnumber = self.driver.find_element(By.CLASS_NAME, 'radio-group')
        # get the parent element
        mainbuild = buildnumber.find_elements(By.TAG_NAME, 'label')
        #confirms that GRCh38 is displayed
        searchTextItems = iterate.getTextAsList(mainbuild)
        self.assertEqual(searchTextItems, ['Human (GRCh38)', 'Mouse (GRCm39)'])
       
        """
        def test_hmdc_summary_build(self):
        
        
        @Status this test no longer required with new hmdc pages
        checks the mouse build number on the HMDC result/summary page
        
        #displays the HMDC qf
        self.driver.get(PUBLIC_URL + "/humanDisease.shtml")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Autism AND").click()
        wait.forAjax(self.driver)
        #clicks the gene tab of the hmdc results page
        self.driver.find_element(By.ID, "genestab").click()
        time.sleep(1)
        # get all the elements in the Genome Coordinates column
        coorddata = self.driver.find_elements(By.CLASS_NAME, 'yui-dt-col-coordinate')
        #finds the mouse build number
        searchTreeItems = iterate.getTextAsList(coorddata)
        #confirms that GRCh38 is displayed somewhere within this field of data
        self.assertIn("GRCm38", searchTreeItems[1])
        """
        
        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSnpBuildNumbers))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))