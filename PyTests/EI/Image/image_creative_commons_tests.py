'''
Created on Jun 6, 2019

@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import HTMLTestRunner
import json
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table




# Tests

class TestImgCCSearch(unittest.TestCase):
    """
    @status Test Image Creative Commons display
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/imageGxd")
    
    def tearDown(self):
        self.driver.close()
        
    def testImageCCActaDsp(self):
        """
        @Status tests that the Creative commons display is present for Acta Biochim Biophys Sin (Shanghai)
        @see pwi-image-cc-1
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('152235')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"
    
    def testImageCCBrainDsp(self):
        """
        @Status tests that the Creative commons display is present for Brain
        @see pwi-image-cc-2
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('164634')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

    def testImageCCCarcDsp(self):
        """
        @Status tests that the Creative commons display is present for Carcinogenesis
        @see pwi-image-cc-3
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('206523')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

    def testImageCCCardioDsp(self):
        """
        @Status tests that the Creative commons display is present for Cardiovasc Res
        @see pwi-image-cc-4
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('260813')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

    def testImageCCCerebDsp(self):
        """
        @Status tests that the Creative commons display is present for Cereb Cortex
        @see pwi-image-cc-5
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('174477')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

    def testImageCCChemDsp(self):
        """
        @Status tests that the Creative commons display is present for Chem Senses
        @see pwi-image-cc-6
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('72149')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

    def testImageCCGlyDsp(self):
        """
        @Status tests that the Creative commons display is present for Glycobiology
        @see pwi-image-cc-7
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('91517')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

    def testImageCCHumMolDsp(self):
        """
        @Status tests that the Creative commons display is present for Hum Mol Genet
        @see pwi-image-cc-8
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('260788')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

    def testImageCCHumReDsp(self):
        """
        @Status tests that the Creative commons display is present for Hum Reprod
        @see pwi-image-cc-9
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('59030')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

    def testImageCCJGerDsp(self):
        """
        @Status tests that the Creative commons display is present for J Gerontol A Biol Sci Med Sci
        @see pwi-image-cc-10
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('70181')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

    def testImageCCMolBioDsp(self):
        """
        @Status tests that the Creative commons display is present for Mol Biol Evol
        @see pwi-image-cc-11
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('80848')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

    def testImageCCToxDsp(self):
        """
        @Status tests that the Creative commons display is present for Toxicol Sci
        @see pwi-image-cc-12
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('55992')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

    def testImageCCEmboDsp(self):
        """
        @Status tests that the Creative commons display is present for EMBO J
        @see pwi-image-cc-13
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('54310')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

    def testImageCCJInvDsp(self):
        """
        @Status tests that the Creative commons display is present for J Invest Dermatol
        @see pwi-image-cc-14
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('258432')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

    def testImageCCMolPDsp(self):
        """
        @Status tests that the Creative commons display is present for Mol Psychiatry
        @see pwi-image-cc-15
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('103960')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

    def testImageCCCellCycDsp(self):
        """
        @Status tests that the Creative commons display is present for Cell Cycle
        @see pwi-image-cc-16
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('97898')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert the Creative Commons display is present
        element = self.driver.find_element_by_id('creativeCommonsWarning')
        if element.is_displayed():
            print "Creative Commons warning  is displayed"
        else:
            print "Creative Commons warning is not displaying!"

'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestImgSearch))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main()