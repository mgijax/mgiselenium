'''
Created on Feb 10, 2016

@author: jeffc
This suite of tests are for QTL allele pages
'''
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
import config
from config import PUBLIC_URL

class TestAlleleDetailQTL(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.PUBLIC_URL + "/allele/")
        self.driver.implicitly_wait(10)

    def test_variant_note(self):
        self.driver.find_element_by_id("phenotype").clear()
        self.driver.find_element_by_id("phenotype").send_keys("Adre")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_css_selector("#yui-rec0 > td.yui-dt0-col-nomen.yui-dt-col-nomen.yui-dt-sortable.yui-dt-first > div > a > sup").click()
        assert "B6.C-H21<sup>c</sup>/ByJ" in self.driver.page_source

    def test_reference_note(self):
        '''
        @status this test verifies a QTL allele that has  QTL Reference Note
        '''
        self.driver.find_element_by_id("phenotype").clear()
        self.driver.find_element_by_id("phenotype").send_keys("Ccc1")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_link_text('Ccc1CC011/Unc').click()
        refnote = self.driver.find_element_by_class_name('qtlRefNoteSec').find_element_by_css_selector('h5')
        #This confirms there is a section called QTL Reference Notes, would not display if not note
        self.assertEqual(refnote.text, "QTL Reference Notes")


    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAlleleDetailQTL))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
