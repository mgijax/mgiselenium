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

class TestImgPaneSearch(unittest.TestCase):
    """
    @status Test Image Pane searching, etc
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
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
        driver.find_element_by_id("imagePaneLabel").send_keys('A heart WT')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the Pane Labels results table
        pane_table = self.driver.find_element_by_id("imagePaneTable")
        table = Table(pane_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(1)
        cell2 = table.get_row_cells(2)
        cell3 = table.get_row_cells(3)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        print result1
        #Assert the correct details are returned
        self.assertEquals(result1, ['A heart Paxx-/-', '144, 131, 97, 95'])
        self.assertEquals(result2, ['A heart Paxx-/-;Xlf-/-', '337, 131, 101, 95'])
        self.assertEquals(result3, ['A heart WT', '47, 131, 97, 95'])

    def testImagePaneSearchWild(self):
        """
        @Status tests that a basic Image Pane Label search using a wildcard works
        @see pwi-image-pane-search-2
        """
        driver = self.driver
        #finds the Image Pane Label field and enters text then clicks the Search button
        driver.find_element_by_id("imagePaneLabel").send_keys('%liver Paxx%')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the Pane Labels results table
        pane_table = self.driver.find_element_by_id("imagePaneTable")
        table = Table(pane_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(1)
        cell2 = table.get_row_cells(2)
        cell3 = table.get_row_cells(3)
        cell4 = table.get_row_cells(4)
        cell5 = table.get_row_cells(5)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        print result5
        #Assert the correct details are returned
        self.assertEquals(result1, ['A heart Paxx-/-', '144, 131, 97, 95'])
        self.assertEquals(result2, ['A heart Paxx-/-;Xlf-/-', '337, 131, 101, 95'])
        self.assertEquals(result3, ['A heart WT', '47, 131, 97, 95'])
        self.assertEquals(result4, ['A heart Xlf-/-', '241, 131, 96, 95'])
        self.assertEquals(result5, ['A liver Paxx-/-', '144, 226, 97, 95'])

    def testImagePaneSearchSpecChr(self):
        """
        @Status tests that a basic Image Pane Label search for a label with a special character works
        @see pwi-image-pane-search-3
        """
        driver = self.driver
        #finds the Image Pane Label field and enters text then clicks the Search button
        driver.find_element_by_id("imagePaneLabel").send_keys("k/k'")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the Pane Labels results table
        pane_table = self.driver.find_element_by_id("imagePaneTable")
        table = Table(pane_table)
        #Iterate and print the search results, checking the 14th and 15th result
        cell14 = table.get_row_cells(14)
        cell15 = table.get_row_cells(15)
        result14 = iterate.getTextAsList(cell14)
        result15 = iterate.getTextAsList(cell15)
        print result14
        #Assert the correct details are returned
        self.assertEquals(result14, ["k/k'", ''])
        self.assertEquals(result15, ["l/l'", ''])

    def testImagePaneSearchlong(self):
        """
        @Status tests that a basic Image Pane Label search for a label that is extremely long works
        @see pwi-image-pane-search-4
        """
        driver = self.driver
        #finds the Image Pane Label field and enters text then clicks the Search button
        driver.find_element_by_id("imagePaneLabel").send_keys("C merge (EFGP and choline acetyltransferase immunoreactivity)")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the Pane Labels results table
        pane_table = self.driver.find_element_by_id("imagePaneTable")
        table = Table(pane_table)
        #Iterate and print the search results, checking the 8th and 9th result
        cell8 = table.get_row_cells(8)
        cell9 = table.get_row_cells(9)
        result8 = iterate.getTextAsList(cell8)
        result9 = iterate.getTextAsList(cell9)
        print result8
        print result9
        #Assert the correct details are returned
        self.assertEquals(result8, ['Ci (expanded boxed region in B)', ''])
        self.assertEquals(result9, ['C merge (EFGP and choline acetyltransferase immunoreactivity)', ''])

    def testImagePaneNoLabelSearch(self):
        """
        @Status tests that a basic Image Pane Label search for a label is blanl(no label) works
        @see pwi-image-pane-search-5
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('73')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the Pane Labels results table
        pane_table = self.driver.find_element_by_id("imagePaneTable")
        table = Table(pane_table)
        #Iterate and print the search results, checking the 1st result
        cell1 = table.get_row_cells(1)
        result1 = iterate.getTextAsList(cell1)
        print result1
        #Assert the correct details are returned
        self.assertEquals(result1, ['', '0, 0, 350, 534'])
        
    def testImagePaneUnderscoreSearch(self):
        """
        @Status tests a pane label display that starts with an underscore
        @see pwi-image-pane-search-6
        """
        driver = self.driver
        #finds the Image Pane Label field and enters text then clicks the Search button
        driver.find_element_by_id("imagePaneLabel").send_keys("_Hox-4-4")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the Pane Labels results table
        pane_table = self.driver.find_element_by_id("imagePaneTable")
        table = Table(pane_table)
        #Iterate and print the search results, checking the 1st result
        cell1 = table.get_row_cells(1)
        result1 = iterate.getTextAsList(cell1)
        print result1
        #Assert the correct details are returned
        self.assertEquals(result1, ['_Hox-4-4', ''])

    def testImagePaneSortSearch(self):
        """
        @Status tests that a basic Image Pane Label search has the correct alpha sort of the pane labels
        @see pwi-image-pane-search-7
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('38389')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the Pane Labels results table
        pane_table = self.driver.find_element_by_id("imagePaneTable")
        table = Table(pane_table)
        #Iterate and print the search results, checking the 1st result
        cell1 = table.get_row_cells(1)
        cell2 = table.get_row_cells(2)
        cell3 = table.get_row_cells(3)
        cell4 = table.get_row_cells(4)
        cell5 = table.get_row_cells(5)
        cell6 = table.get_row_cells(6)
        cell7 = table.get_row_cells(7)
        cell8 = table.get_row_cells(8)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        result6 = iterate.getTextAsList(cell6)
        result7 = iterate.getTextAsList(cell7)
        result8 = iterate.getTextAsList(cell8)
        print result1
        #Assert the correct details are returned
        self.assertEquals(result1, ['_ptc E14.5', '253, 32, 241, 159'])
        self.assertEquals(result2, ['_ptc E17', '253, 196, 241, 144'])
        self.assertEquals(result3, ['_ptc P14', '253, 540, 241, 194'])
        self.assertEquals(result4, ['_ptc P7', '253, 344, 241, 191'])
        self.assertEquals(result5, ['_Shh E14.5', '55, 32, 192, 159'])
        self.assertEquals(result6, ['_Shh E17', '55, 196, 192, 144'])
        self.assertEquals(result7, ['_Shh P14', '55, 540, 192, 194'])
        self.assertEquals(result8, ['_Shh P7', '55, 344, 192, 191'])

'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestImgSearch))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main()
    