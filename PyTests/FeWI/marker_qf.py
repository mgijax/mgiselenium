'''
Created on Jun 7, 2016

@author: jeffc
This set of tests verifies items found on the marker query form page.
'''
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import sys,os.path
from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
import config
from config import TEST_URL

class TestMarkerQF(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/marker/")
        self.driver.implicitly_wait(10)

    def test_ribbon_locations(self):
        '''
        @status This test verifies the ribbons are being displayed in the correct order on the page.
        '''
        self.driver.find_element(By.NAME, 'markerQF')
        genemarker = self.driver.find_element_by_css_selector('.queryStructureTable > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1)')
        self.assertEqual(genemarker.text, 'Gene/Marker', "heading is incorrect")
        featuretype = self.driver.find_element_by_css_selector('.queryStructureTable > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1)')
        self.assertEqual(featuretype.text, 'Feature type', "heading is incorrect")
        genomelocation = self.driver.find_element_by_css_selector('.queryStructureTable > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1)')
        self.assertEqual(genomelocation.text, 'Genome location', "heading is incorrect")
        geneontclass = self.driver.find_element_by_css_selector('.queryStructureTable > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1)')
        self.assertEqual(geneontclass.text, 'Gene Ontology\nclassifications', "heading is incorrect")
        proteindomain = self.driver.find_element_by_css_selector('.queryStructureTable > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(1)')
        self.assertEqual(proteindomain.text, 'Protein domains', "heading is incorrect")
        mousepheno = self.driver.find_element_by_css_selector('.queryStructureTable > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(1)')
        self.assertEqual(mousepheno.text, 'Mouse phenotypes &\nmouse models of\nhuman disease', "heading is incorrect")
        
        
        
        
        
        
        
        
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMarkerQF))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))              
