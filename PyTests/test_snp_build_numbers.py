'''
Created on Mar 21, 2016

@author: jeffc
'''
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
from config.config import PUBLIC_URL
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import time
import config
from util import iterate, wait


class TestSnpBuild(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(config.PUBLIC_URL)
        

    def test_snp_qf(self):
        """
        @Status this test works
        Checks the dbSNp and mouse build numbers on the snp query form and snp summary page
        """
        self.driver.get(PUBLIC_URL + "/snp/")
        #finds the build number at the top of the snp QF page
        formLabel = self.driver.find_element_by_css_selector("#form1 > div:nth-child(2)")
        self.assertIn("dbSNP Build 142", formLabel.text)

        genebox = self.driver.find_element_by_id("nomen")
        #enters pax6 in the Gene Symbol/Name box
        genebox.send_keys("pax6")
        genebox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        #finds the snp build number in the heading of SNP ID column
        snpidLabel = self.driver.find_element_by_id("snpSummaryTable").find_element_by_id("snp_id")
        self.assertIn("(dbSNP Build 142)", snpidLabel.text)
        #finds the GRC build number in the heading of Map Position column
        mapLabel = self.driver.find_element_by_id("snpSummaryTable").find_element_by_id("map_position")
        self.assertIn("(GRCm38)", mapLabel.text)
        
    def test_mrk_detail_build(self):
        """
        @Status this test works
        Checks the mouse build number on a marker detail page
        """
        #displays the marker detail page for pax6
        self.driver.get(PUBLIC_URL + "/marker/MGI:1096368")
        #opens the Location & Maps section
        self.driver.find_element_by_class_name("toggleImage").click()
        wait.forAjax(self.driver)
        #finds the build number at the top of the snp QF page
        seqmapLabel = self.driver.find_element_by_class_name("detailData2").find_element_by_class_name("closed").find_element_by_css_selector("div.value")
        #verifies GRCm38 is displayed in this section
        self.assertIn("GRCm38", seqmapLabel.text)

    def test_mrk_qf_build(self):
        """
        @Status this test works
        Checks the mouse build number on the marker query form
        """
        #displays the marker qf
        self.driver.get(PUBLIC_URL + "/marker")
        #finds the genome coordinates link
        genocoord = self.driver.find_element_by_link_text('Genome Coordinates')
        # get the parent element
        gcParent = genocoord.find_element_by_xpath('..')
        #confirms  that GRCm38 is displayed
        self.assertIn("GRCm38", gcParent.text)
        
    def test_hmdc_build(self):
        """
        @Status this test works
        checks the human and mouse build numbers(twice) on the HMDC query page
        """
        #displays the HMDC qf
        self.driver.get(PUBLIC_URL + "/humanDisease.shtml")
        #finds the human build number
        humanbuild1 = self.driver.find_element_by_id('organismHuman1')
        # get the parent element
        hparent1 = humanbuild1.find_element_by_xpath('..')
        wait.forAjax(self.driver)
        #confirms that GRCh38 is displayed
        self.assertIn("Human(GRCh38)", hparent1.text) 
        #finds the human build number
        mousebuild1 = self.driver.find_element_by_id('organismMouse1')
        # get the parent element
        mparent1 = mousebuild1.find_element_by_xpath('..')
        wait.forAjax(self.driver)
        #confirms that GRCm38 is displayed
        self.assertIn("Mouse(GRCm38)", mparent1.text)
        #finds the human build number
        humanbuild2 = self.driver.find_element_by_id('organismHuman2')
        # get the parent element
        hparent2 = humanbuild2.find_element_by_xpath('..')
        wait.forAjax(self.driver)
        #confirms that GRCh38 is displayed 
        self.assertIn("Human(GRCh38)", hparent2.text)
        #finds the human build number
        mousebuild2 = self.driver.find_element_by_id('organismMouse2')
        # get the parent element
        mparent2 = mousebuild2.find_element_by_xpath('..')
        wait.forAjax(self.driver)
        #confirms that GRCm38 is displayed 
        self.assertIn("Mouse(GRCm38)", mparent2.text) 
        
    def test_hmdc_summary_build(self):
        """
        @Status this test works
        checks the mouse build number on the HMDC result/summary page
        """
        #displays the HMDC qf
        self.driver.get(PUBLIC_URL + "/humanDisease.shtml")
        self.driver.find_element_by_partial_link_text("Autism AND").click()
        wait.forAjax(self.driver)
        #clicks the gene tab of the hmdc results page
        self.driver.find_element_by_id("genestab").click()
        time.sleep(1)
        # get all the elements in the Genome Coordinates column
        coorddata = self.driver.find_elements_by_class_name('yui-dt-col-coordinate')
        #finds the mouse build number
        searchTreeItems = iterate.getTextAsList(coorddata)
        #confirms that GRCh38 is displayed somewhere within this field of data
        self.assertIn("GRCm38", searchTreeItems[1])
        
        
        
    #def tearDown(self):
    #    self.closeAllWindows()
        




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()