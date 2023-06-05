'''
Created on Feb 10, 2016

@author: jeffc
This suite of tests are for QTL allele pages
'''
import unittest
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
import config
from config import TEST_URL

#Tests
tracemalloc.start()
class TestAlleleDetailQTL(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/allele/")
        self.driver.implicitly_wait(10)

    def test_variant_note(self):
        self.driver.find_element(By.ID, "phenotype").clear()
        self.driver.find_element(By.ID, "phenotype").send_keys("Adre")
        self.driver.find_element(By.CLASS_NAME, "buttonLabel").click()
        self.driver.find_element(By.CSS_SELECTOR, "#yui-rec0 > td.yui-dt0-col-nomen.yui-dt-col-nomen.yui-dt-sortable.yui-dt-first > div > a > sup").click()
        assert "B6.C-H21<sup>c</sup>/ByJ" in self.driver.page_source

    def test_reference_note(self):
        '''
        @status this test verifies a QTL allele that has  QTL Reference Note
        '''
        self.driver.find_element(By.ID, "phenotype").clear()
        self.driver.find_element(By.ID, "phenotype").send_keys("Ccc1")
        self.driver.find_element(By.CLASS_NAME, "buttonLabel").click()
        self.driver.find_element(By.LINK_TEXT, 'Ccc1CC011/Unc').click()
        refnote = self.driver.find_element(By.CLASS_NAME, 'qtlRefNoteSec').find_element(By.CSS_SELECTOR, 'h5')
        #This confirms there is a section called QTL Reference Notes, would not display if not note
        self.assertEqual(refnote.text, "QTL Reference Notes")


    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAlleleDetailQTL))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
