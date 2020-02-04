'''
Created on Oct 19, 2016
This set of tests verifies items found on the allele query form page
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys,os.path
from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
from util.table import Table
import config
from config import TEST_URL

class TestAlleleQueryForm(unittest.TestCase):


    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/allele/")
        self.driver.implicitly_wait(10)

    def test_ribbon_locations(self):
        '''
        @status This test verifies the ribbons are being displayed in the correct order on the page.
        '''
        self.driver.find_element_by_name("alleleQueryForm")
        phenotypesdisease = self.driver.find_element_by_css_selector("tr.stripe1 > td.cat1")
        print phenotypesdisease.text
        self.assertEquals(phenotypesdisease.text, 'Mouse phenotypes &\nmouse models of\nhuman disease', "heading is incorrect")
        nomengenomelocation = self.driver.find_element_by_css_selector("tr.stripe2 > td.cat2")
        print nomengenomelocation.text
        self.assertEquals(nomengenomelocation.text, 'Nomenclature\n& genome location', "heading is incorrect")
        categories = self.driver.find_element_by_css_selector("tr:nth-child(4).stripe1 > td.cat1")
        print categories.text
        self.assertEquals(categories.text, 'Categories', "heading is incorrect")
     
    def test_doids_search(self):
        '''
        @status this test verifies  you can search by a DOID in the phenotypes box of the allele query form.
        @bug under construction, need the summary table to have an ID or Name OR do it like non table(MP annotation PWI)
        '''
        self.driver.find_element_by_name("phenotype").clear()
        self.driver.find_element_by_name("phenotype").send_keys("DOID:5737")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.assertTrue(self.driver.page_source, 'Phenotypes/Diseases: including text DOID:5737')       
        #disease_table = self.driver.find_element_by_id('')
        #table = Table(disease_table)
        #Iterate and print the search results headers
        #header_cells = table.get_header_cells()
        #print iterate.getTextAsList(header_cells)
        
        # print row 1
        #cells = table.get_column_cells("Human Diseases")
        #disease_cells = iterate.getTextAsList(cells)
        #print disease_cells
        #self.assertEquals(disease_cells[1], 'myelofibrosis   DOID:4971')

        
             
        
        
        
        
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAlleleQueryForm))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()                
