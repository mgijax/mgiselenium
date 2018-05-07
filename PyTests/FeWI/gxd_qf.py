'''
Created on Oct 19, 2016
This set of tests verifies items found on the Gene Expression query form page
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from util.table import Table
import sys,os.path
from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
import config
from config import TEST_URL

class TestGXDQF(unittest.TestCase):


    def setUp(self):
    
        self.driver = webdriver.Firefox()
        self.driver.get(config.TEST_URL + "/gxd/")
        self.driver.implicitly_wait(10)

    def test_ribbon_locations(self):
        '''
        @status This test verifies the ribbons are being displayed in the correct order on the page.
        '''
        self.driver.find_element(By.ID, 'gxdQueryForm')
        genesribbon = self.driver.find_element(By.CSS_SELECTOR, 'tr.stripe1 > td.cat1Gxd')
        print genesribbon.text
        self.assertEquals(genesribbon.text, 'Genes', "heading is incorrect")
        genomelocation = self.driver.find_element(By.CSS_SELECTOR, 'tr.stripe2 > td.cat2Gxd')
        print genomelocation.text
        self.assertEquals(genomelocation.text, 'Genome location', "heading is incorrect")
        structurestage = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(4).stripe1 > td.cat1Gxd')
        print structurestage.text
        self.assertEquals(structurestage.text, 'Anatomical structure or stage', "heading is incorrect")
        mutantwt = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(5).stripe2 > td.cat2Gxd')
        print mutantwt.text
        self.assertEquals(mutantwt.text, 'Mutant / wild type', "heading is incorrect")
        assaytype = self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(6).stripe1 > td.cat1Gxd')
        print assaytype.text
        self.assertEquals(assaytype.text, 'Assay types', "heading is incorrect")
        
    def test_no_normals(self):
        """
        @status: Tests that the genes tab does not return normals(like Adcy8) or genes with no expression(like Ankfn1)
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'vocabTerm')
        # Enter your phenotype
        genebox.send_keys("taste/olfaction")
        time.sleep(2)
        genebox.send_keys(Keys.RETURN)
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        #finds the Genes tab and clicks it
        driver.find_element(By.ID, 'genestab').click()
        time.sleep(2)
        #locates the genes column and lists the genes found
        genelist = driver.find_element(By.ID, 'genesdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-symbol')
        searchTextItems = iterate.getTextAsList(items)
        print searchTextItems
        #assert that this gene is not returned since it is associated to a normal phenotype
        self.assertNotIn('Adcy8', searchTextItems, 'Gene Adcy8 is being returned!')   
        #assert that this gene is not returned since it has no expression annotations
        self.assertNotIn('Ankfn1', searchTextItems, 'Gene Ankfn1 is being returned!') 
        
        
        
        
        
    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'TestGXDQF.testName']
    unittest.main()                