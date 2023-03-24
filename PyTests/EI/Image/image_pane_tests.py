'''
Created on Jun 4, 2019
These are Image Pane tests for searching, displaying, adding and editing. 
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
import HtmlTestRunner
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

class TestEiImagePaneSearch(unittest.TestCase):
    """
    @status Test Image Pane searching, etc
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        #self.driver.get(config.TEST_PWI_URL + "/edit/imageGxd")
        self.form.get_module(config.TEST_PWI_URL + "/edit/imageGxd")
    
    def tearDown(self):
        self.driver.close()
        
    def testImagePaneSearch(self):
        """
        @Status tests that a basic Image Pane Label search works
        @see pwi-image-pane-search-1 
        """
        driver = self.driver
        #finds the Image Pane Label field and enters text then clicks the Search button
        driver.find_element(By.ID, "paneLabelID").send_keys('A heart WT')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the Pane Labels results table
        pane_table = self.driver.find_element(By.ID, "imagePaneTable")
        time.sleep(2)
        
        third_row = self.driver.find_element(By.ID, "paneLabelID480566").get_attribute("value")
        time.sleep(2)
        print(third_row)
        #Assert the correct details are returned, the third Pane Label should be 'A heart WT
        self.assertEqual(third_row, 'A heart WT')

    def testImagePaneSearchWild(self):
        """
        @Status tests that a basic Image Pane Label search using a wildcard works
        @see pwi-image-pane-search-2 broken??? 2/16/2023
        """
        driver = self.driver
        #finds the Image Pane Label field and enters text then clicks the Search button
        driver.find_element(By.ID, "paneLabelID").send_keys('%liver Paxx%')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the Pane Labels results table
        pane_table = self.driver.find_element(By.ID, "imagePaneTable")
        table = Table(pane_table)
        time.sleep(2)
        row1 = self.driver.find_element(By.ID, "paneLabelID480567").get_attribute("value")
        row2 = self.driver.find_element(By.ID, "paneLabelID480569").get_attribute("value")
        row3 = self.driver.find_element(By.ID, "paneLabelID480566").get_attribute("value")
        row4 = self.driver.find_element(By.ID, "paneLabelID480568").get_attribute("value")
        row5 = self.driver.find_element(By.ID, "paneLabelID480571").get_attribute("value")
        time.sleep(2)
        print(row1)
        print(row2)
        print(row3)
        print(row4)
        print(row5)
        #Assert the correct details are returned
        self.assertEqual(row1, 'A heart Paxx-/-')
        self.assertEqual(row2, 'A heart Paxx-/-;Xlf-/-')
        self.assertEqual(row3, 'A heart WT')
        self.assertEqual(row4, 'A heart Xlf-/-')
        self.assertEqual(row5, 'A liver Paxx-/-')

    def testImagePaneSearchSpecChr(self):
        """
        @Status tests that a basic Image Pane Label search for a label with a special character works
        @see pwi-image-pane-search-3
        """
        driver = self.driver
        #finds the Image Pane Label field and enters text then clicks the Search button
        driver.find_element(By.ID, "paneLabelID").send_keys("k/k'")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the Pane Labels results table
        pane_table = self.driver.find_element(By.ID, "imagePaneTable")
        table = Table(pane_table)
        time.sleep(2)
        row14 = self.driver.find_element(By.ID, "paneLabelID480840").get_attribute("value")
        row15 = self.driver.find_element(By.ID, "paneLabelID480847").get_attribute("value")
        time.sleep(2)
        print(row14)
        #Assert the correct details are returned
        self.assertEqual(row14, "k/k'")
        self.assertEqual(row15, "l/l'")

    def testImagePaneLabelSearch(self):
        """
        @Status tests that a basic Image Pane Label search for a label that is extremely long works
        @see pwi-image-pane-search-4
        """
        driver = self.driver
        #finds the Image Pane Label field and enters text then clicks the Search button
        driver.find_element(By.ID, "paneLabelID").send_keys("C merge (EFGP and choline acetyltransferase immunoreactivity)")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the Pane Labels results table
        pane_table = self.driver.find_element(By.ID, "imagePaneTable")
        table = Table(pane_table)
        time.sleep(2)
        row8 = self.driver.find_element(By.ID, "paneLabelID313902").get_attribute("value")
        row9 = self.driver.find_element(By.ID, "paneLabelID313901").get_attribute("value")
        time.sleep(5)
        print(row8)
        #Assert the correct details are returned
        self.assertEqual(row8, 'C merge (EFGP and choline acetyltransferase immunoreactivity)')
        self.assertEqual(row9, "Ci (expanded boxed region in B)")

    def testImagePaneNoLabelSearch(self):
        """
        @Status tests that a basic Image Pane Label search for a label is blank(no label) works
        @see pwi-image-pane-search-5 
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element(By.ID, "JNumID").send_keys('73')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the Pane Labels results table
        pane_row1 = self.driver.find_element(By.ID, "paneLabelID6895").get_attribute("value")
        #prints the pane label for row 1(should be blank)
        print(pane_row1)
        #Assert the correct details are returned
        self.assertEqual(pane_row1, '')
        
    def testImagePaneUnderscoreSearch(self):
        """
        @Status tests a pane label display that starts with an underscore
        @see pwi-image-pane-search-6 
        """
        driver = self.driver
        #finds the Image Pane Label field and enters text then clicks the Search button
        driver.find_element(By.ID, "paneLabelID").send_keys("_Hox-4-4")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the Pane Labels results table
        pane_row1 = self.driver.find_element(By.ID, "paneLabelID472753").get_attribute('value')
        pane_row2 = self.driver.find_element(By.ID, "paneLabelID472754").get_attribute('value')
        #prints the pane label for row 1(should be blank)
        print(pane_row1)
        print(pane_row2)
        #Assert the correct details are returned
        self.assertEqual(pane_row1, '_Hox-4-4')
        self.assertEqual(pane_row2, '_Hox-4-5')

    def testImagePaneSortSearch(self):
        """
        @Status tests that a basic Image Pane Label search has the correct alpha sort of the pane labels
        @see pwi-image-pane-search-7 !currently broken, same issue as search 5
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element(By.ID, "JNumID").send_keys('38389')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the Pane Labels results table
        pane_row1 = self.driver.find_element(By.ID, "paneLabelID465633").get_attribute('value')
        pane_row2 = self.driver.find_element(By.ID, "paneLabelID465634").get_attribute('value')
        pane_row3 = self.driver.find_element(By.ID, "paneLabelID465636").get_attribute('value')
        pane_row4 = self.driver.find_element(By.ID, "paneLabelID465635").get_attribute('value')
        pane_row5 = self.driver.find_element(By.ID, "paneLabelID465629").get_attribute('value')
        pane_row6 = self.driver.find_element(By.ID, "paneLabelID465630").get_attribute('value')
        pane_row7 = self.driver.find_element(By.ID, "paneLabelID465632").get_attribute('value')
        pane_row8 = self.driver.find_element(By.ID, "paneLabelID465631").get_attribute('value')
        #Iterate and print the search results, checking the 1st result
        print(pane_row1)
        print(pane_row2)
        #Assert the correct details are returned
        self.assertEqual(pane_row1, '_ptc E14.5')
        self.assertEqual(pane_row2, '_ptc E17')
        self.assertEqual(pane_row3, '_ptc P14')
        self.assertEqual(pane_row4, '_ptc P7')
        self.assertEqual(pane_row5, '_Shh E14.5')
        self.assertEqual(pane_row6, '_Shh E17')
        self.assertEqual(pane_row7, '_Shh P14')
        self.assertEqual(pane_row8, '_Shh P7')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiImagePaneSearch))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
    