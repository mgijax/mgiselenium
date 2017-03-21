'''
Created on Mar 21, 2016

@author: jeffc
'''
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
from util import wait, iterate
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
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(4)
        self.driver.get(config.PUBLIC_URL)
        

    def test_snp_qf(self):
        """
        @Status this test works
        Checks the dbSNp and mouse build numbers on the snp query form and snp summary page
        """
        self.driver.get(PUBLIC_URL + "/snp/")
        #finds the build number at the top of the snp QF page
        formLabel = self.driver.find_element_by_css_selector("#form1 > div:nth-child(2)")
        self.assertIn("from dbSNP Build 142", formLabel.text)

        genebox = self.driver.find_element_by_id("nomen")
        #enters pax6 in the Gene Symbol/Name box
        genebox.send_keys("pax6")
        genebox.send_keys(Keys.RETURN)
        #wait.forAjax(self.driver)
        time.sleep(2)
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
        @Status this test has been updated for the new hmdc pages
        checks the human and mouse build numbers on the HMDC query page
        """
        #displays the HMDC qf
        self.driver.get(PUBLIC_URL + "/diseasePortal")
        #find the pulldown and select Genome Location
        selectorbox = self.driver.find_element_by_class_name("queryBuilder")
        pulldown = selectorbox.find_element_by_tag_name("select").find_elements_by_tag_name("option")
        #print [x.text for x in pulldown]
        searchTextItems = iterate.getTextAsList(pulldown)
        #verifies all the items listed in the pulldown are correct and in order
        self.assertEqual(searchTextItems, ['Please select a field', 'Gene Symbol(s) or ID(s)','Gene Name','Phenotype or Disease Name', 'Phenotype or Disease ID(s)', 'Genome Location', 'Gene File Upload'])
        #click the Genome Location option
        pulldown[5].click()
        #self.assertIn("Genome Location", pulldown[3].Text)
        #finds the human and mouse genome build numbers
        buildnumber = self.driver.find_element_by_class_name('radio-group')
        # get the parent element
        mainbuild = buildnumber.find_elements_by_tag_name('label')
        wait.forAjax(self.driver)
        #confirms that GRCh38 is displayed
        #print [x.text for x in mainbuild]
        searchTextItems = iterate.getTextAsList(mainbuild)
        self.assertEqual(searchTextItems, ['Human (GRCh38)', 'Mouse (GRCm38)'])
       
        """
        def test_hmdc_summary_build(self):
        
        
        @Status this test no longer required with new hmdc pages
        checks the mouse build number on the HMDC result/summary page
        
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
        """
        
        
    def tearDown(self):
        self.driver.quit()
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSnpBuild))
    return suite


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()