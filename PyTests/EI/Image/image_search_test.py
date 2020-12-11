'''
Created on May 17, 2019
These are tests that check the searching options of the Image module
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

class TestEiImageSearch(unittest.TestCase):
    """
    @status Test Image searching, etc
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/imageGxd")
    
    def tearDown(self):
        self.driver.close()
        
    def testImageMgiIdThumbSearch(self):
        """
        @Status tests that a basic Image MGI ID thumbnail search works
        @see pwi-image-search-1
        """
        driver = self.driver
        #finds the Image Class pulldown and selects "Search all" option then click the Search button
        Select(driver.find_element_by_id("imageClassID")).select_by_value('')
        #finds the MGI ID field and enters am MGI ID then clicks the Search button
        driver.find_element_by_id("objectAccId").send_keys('MGI:3717589')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct J number detail is returned
        self.assertEqual(result1, ['J:20443; Thumbnail; 1'])

    def testImageMgiIdFullSearch(self):
        """
        @Status tests that a basic Image MGI ID full image search works
        @see pwi-image-search-2
        """
        driver = self.driver
        #finds the MGI ID field and enters am MGI ID then clicks the Search button
        driver.find_element_by_id("objectAccId").send_keys('MGI:5442068')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct J number detail is returned
        self.assertEqual(result1, ['J:148; Full Size; 10'])

    def testImageJnumAllSearch(self):
        """
        @Status tests that a basic Image J number Search All image search works
        @see pwi-image-search-3
        """
        driver = self.driver
        #finds the Image Class pulldown and selects "Search all" option then click the Search button
        Select(driver.find_element_by_id("imageClassID")).select_by_value('')
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('139510')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        cell6 = table.get_row_cells(5)
        cell7 = table.get_row_cells(6)
        cell8 = table.get_row_cells(7)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        result6 = iterate.getTextAsList(cell6)
        result7 = iterate.getTextAsList(cell7)
        result8 = iterate.getTextAsList(cell8)
        print(result1)
        #Assert the correct J number details are returned
        self.assertEqual(result1, ['J:139510; Full Size; 1'])
        self.assertEqual(result2, ['J:139510; Full Size; 1aleft'])
        self.assertEqual(result3, ['J:139510; Thumbnail; 1aleft'])        
        self.assertEqual(result4, ['J:139510; Full Size; 1aright'])
        self.assertEqual(result5, ['J:139510; Thumbnail; 1aright'])
        self.assertEqual(result6, ['J:139510; Full Size; 1b'])
        self.assertEqual(result7, ['J:139510; Thumbnail; 1b'])
        self.assertEqual(result8, ['J:139510; Full Size; S1'])     

    def testImageJnumExpSearch(self):
        """
        @Status tests that a basic Image J number Expression image search works
        @note: this also tests sort order!
        @see pwi-image-search-4
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('1503')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        cell6 = table.get_row_cells(5)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        result6 = iterate.getTextAsList(cell6)
        print(result1)
        #Assert the correct J number details are returned
        self.assertEqual(result1, ['J:1503; Full Size; 4'])
        self.assertEqual(result2, ['J:1503; Full Size; 5'])
        self.assertEqual(result3, ['J:1503; Full Size; 6'])
        self.assertEqual(result4, ['J:1503; Full Size; 7'])
        self.assertEqual(result5, ['J:1503; Full Size; 8'])
        self.assertEqual(result6, ['J:1503; Full Size; 9'])

    def testImageJnumPhenoSearch(self):
        """
        @Status tests that a basic Image J number Phenotype image search works
        @note: this also tests sort order!
        @see pwi-image-search-5
        """
        driver = self.driver
        #finds the Image Class pulldown and selects "Phenotypes" option then click the Search button
        Select(driver.find_element_by_id("imageClassID")).select_by_value('6481782')
        #finds the J# field and enter a J Number for a phenotype image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('6708')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        cell6 = table.get_row_cells(5)
        cell7 = table.get_row_cells(6)
        cell8 = table.get_row_cells(7)
        cell9 = table.get_row_cells(8)
        cell10 = table.get_row_cells(9)
        cell17 = table.get_row_cells(16)
        cell18 = table.get_row_cells(17)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        result6 = iterate.getTextAsList(cell6)
        result7 = iterate.getTextAsList(cell7)
        result8 = iterate.getTextAsList(cell8)
        result9 = iterate.getTextAsList(cell9)
        result10 = iterate.getTextAsList(cell10)
        result17 = iterate.getTextAsList(cell17)
        result18 = iterate.getTextAsList(cell18)
        print(result1)
        #Assert the correct J number details are returned(for the first 12 results)
        self.assertEqual(result1, ['J:6708; Full Size; 1'])
        self.assertEqual(result2, ['J:6708; Thumbnail; 1'])
        self.assertEqual(result3, ['J:6708; Full Size; 2'])
        self.assertEqual(result4, ['J:6708; Thumbnail; 2'])
        self.assertEqual(result5, ['J:6708; Full Size; 3'])
        self.assertEqual(result6, ['J:6708; Thumbnail; 3'])
        self.assertEqual(result7, ['J:6708; Full Size; 5'])
        self.assertEqual(result8, ['J:6708; Thumbnail; 5'])
        self.assertEqual(result9, ['J:6708; Full Size; 6'])
        self.assertEqual(result10, ['J:6708; Thumbnail; 6'])
        self.assertEqual(result17, ['J:6708; Full Size; 10'])
        self.assertEqual(result18, ['J:6708; Thumbnail; 10'])

    def testImageJnumMoleSearch(self):
        """
        @Status tests that a basic Image J number Molecular image search works
        @see pwi-image-search-6
        """
        driver = self.driver
        #finds the Image Class pulldown and selects "Molecular" option then click the Search button
        Select(driver.find_element_by_id("imageClassID")).select_by_value('6481783')
        #finds the J# field and enter a J Number for a molecular image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('42811')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        
        print(result1)
        #Assert the correct J number details are returned(for the first 6 results)
        self.assertEqual(result1, ['J:42811; Full Size; 1'])
        self.assertEqual(result2, ['J:42811; Thumbnail; 1'])

    def testImageFigLabelSearch(self):
        """
        @Status tests that a basic Image Figure Label search works
        @see pwi-image-search-7
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("figureLabelID").send_keys('5A')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        print(result1)
        #Assert the correct J number details are returned(for the first 6 results)
        self.assertEqual(result1, ['J:81846; Full Size; 5A'])
        self.assertEqual(result2, ['J:241606; Full Size; 5A'])

    def testImageCiteWildSearch(self):
        """
        @Status tests that a basic Image Citation w/wildcard search works
        @see pwi-image-search-8
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("citationID").send_keys('Zakin%')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        cell6 = table.get_row_cells(5)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        result6 = iterate.getTextAsList(cell6)
        print(result1)
        #Assert the correct J number details are returned(for the first 6 results)
        self.assertEqual(result1, ['J:47698; Full Size; 3'])
        self.assertEqual(result2, ['J:47698; Full Size; 4'])
        self.assertEqual(result3, ['J:47698; Full Size; 5'])
        self.assertEqual(result4, ['J:66476; Full Size; 1'])
        self.assertEqual(result5, ['J:66476; Full Size; 2'])
        self.assertEqual(result6, ['J:66476; Full Size; 3'])

    def testImageClassExpSearch(self):
        """
        @Status tests that a basic Image Class Expression search works
        @note: This will check sorting  of results as well(Jnum, Label, Image Type)
        @attention: The EC webdriverwait code needs to be worked on/fixed when time allows
        @see pwi-image-search-9
        """
        driver = self.driver
        #finds the Image Class pulldown and selects "Expression" option then click the Search button
        Select(driver.find_element_by_id("imageClassID")).select_by_value('6481781')
        driver.find_element_by_id('searchButton').click()
        time.sleep(15)
        #WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.ID, "resultsCount")))
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        time.sleep(2)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        cell6 = table.get_row_cells(5)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        result6 = iterate.getTextAsList(cell6)        
        print(result1)
        #Assert the correct J number details are returned(for the first 6 results)
        self.assertEqual(result1, ['J:25; Full Size; 1'])
        self.assertEqual(result2, ['J:25; Full Size; 2'])
        self.assertEqual(result3, ['J:47; Full Size; 1'])
        self.assertEqual(result4, ['J:47; Full Size; 2'])
        self.assertEqual(result5, ['J:47; Full Size; 3'])
        self.assertEqual(result6, ['J:47; Full Size; 4'])

    def testImageClassPhenoSearch(self):
        """
        @Status tests that a basic Image Class Phenotypes search works
        @note: This will check sorting  of results as well(Jnum, Label, Image Type)
        @attention: The EC webdriverwait code needs to be worked on/fixed when time allows
        @see pwi-image-search-10
        """
        driver = self.driver
        #finds the Image Class pulldown and selects "Phenotypes" option then click the Search button
        Select(driver.find_element_by_id("imageClassID")).select_by_value('6481782')
        driver.find_element_by_id('searchButton').click()
        time.sleep(5)
        #WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.ID, "resultsCount")))
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        cell6 = table.get_row_cells(5)
        cell7 = table.get_row_cells(6)
        cell8 = table.get_row_cells(7)
        cell9 = table.get_row_cells(8)
        cell10 = table.get_row_cells(9)
        cell21 = table.get_row_cells(20)
        cell22 = table.get_row_cells(21)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        result6 = iterate.getTextAsList(cell6)
        result7 = iterate.getTextAsList(cell7)
        result8 = iterate.getTextAsList(cell8)
        result9 = iterate.getTextAsList(cell9)
        result10 = iterate.getTextAsList(cell10)  
        result21 = iterate.getTextAsList(cell21)
        result22 = iterate.getTextAsList(cell22)            
        print(result1)
        #Assert the correct J number details are returned(for the first 10 results, plus result for image 10)
        self.assertEqual(result1, ['J:4348; Full Size; 1'])
        self.assertEqual(result2, ['J:4348; Thumbnail; 1'])
        self.assertEqual(result3, ['J:4348; Full Size; 2'])
        self.assertEqual(result4, ['J:4348; Thumbnail; 2'])
        self.assertEqual(result5, ['J:6708; Full Size; 1'])
        self.assertEqual(result6, ['J:6708; Thumbnail; 1'])
        self.assertEqual(result7, ['J:6708; Full Size; 2'])
        self.assertEqual(result8, ['J:6708; Thumbnail; 2'])
        self.assertEqual(result9, ['J:6708; Full Size; 3'])
        self.assertEqual(result10, ['J:6708; Thumbnail; 3'])
        self.assertEqual(result21, ['J:6708; Full Size; 10'])
        self.assertEqual(result22, ['J:6708; Thumbnail; 10'])

    def testImageClassMolecularSearch(self):
        """
        @Status tests that a basic Image Class Molecular search works
        @note: This will check sorting  of results as well(Jnum, Label, Image Type)
        @attention: The EC webdriverwait code needs to be worked on/fixed when time allows
        @see pwi-image-search-11
        """
        driver = self.driver
        #finds the Image Class pulldown and selects "Molecular" option then click the Search button
        Select(driver.find_element_by_id("imageClassID")).select_by_value('6481783')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.ID, "resultsCount")))
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        cell6 = table.get_row_cells(5)
        cell7 = table.get_row_cells(6)
        cell8 = table.get_row_cells(7)
        cell9 = table.get_row_cells(8)
        cell10 = table.get_row_cells(9)
        cell11 = table.get_row_cells(10)
        cell12 = table.get_row_cells(11)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        result6 = iterate.getTextAsList(cell6)
        result7 = iterate.getTextAsList(cell7)
        result8 = iterate.getTextAsList(cell8)
        result9 = iterate.getTextAsList(cell9)
        result10 = iterate.getTextAsList(cell10)
        result11 = iterate.getTextAsList(cell11)
        result12 = iterate.getTextAsList(cell12)        
        print(result1)
        #Assert the correct J number details are returned(for the first 12 results)
        self.assertEqual(result1, ['J:42811; Full Size; 1'])
        self.assertEqual(result2, ['J:42811; Thumbnail; 1'])
        self.assertEqual(result3, ['J:52722; Full Size; 3'])
        self.assertEqual(result4, ['J:52722; Thumbnail; 3'])
        self.assertEqual(result5, ['J:77213; Full Size; 1'])
        self.assertEqual(result6, ['J:77213; Thumbnail; 1'])
        self.assertEqual(result7, ['J:80319; Full Size; 1a'])
        self.assertEqual(result8, ['J:80319; Thumbnail; 1a'])
        self.assertEqual(result9, ['J:80963; Full Size; 1'])
        self.assertEqual(result10, ['J:80963; Thumbnail; 1'])
        self.assertEqual(result11, ['J:83279; Full Size; 1B'])
        self.assertEqual(result12, ['J:83279; Thumbnail; 1B'])

    def testImageCaptionWildSearch(self):
        """
        @Status tests that a basic Image Caption w/wildcard search works
        @see pwi-image-search-12
        """
        driver = self.driver
        #find the J# filed and enter the J number
        driver.find_element_by_id("JNumID").send_keys('J:47')
        #finds the caption field and enter a wildcard search term then click the Search button
        driver.find_element_by_id("captionID").send_keys('%Magnification, 291 X%')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "resultsCount")))
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct J number details are returned
        self.assertEqual(result1, ['J:47; Full Size; 1'])
        
    def testImageCopyrightWildSearch(self):
        """
        @Status tests that a basic Image Copyright w/wildcard search works
        @note J:190949; Full Size; 3 should come before J:190949; Full Size; S1 but sort is not perfect, known issue. Leave it as is for now.
        @see pwi-image-search-14
        """
        driver = self.driver
        #find the J# filed and enter the J number
        driver.find_element_by_id("JNumID").send_keys('J:190949')
        #finds the Copyright field and enter a wildcard term then click the Search button
        driver.find_element_by_id("copyrightID").send_keys('%vasc cell%')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        print(result1)
        #Assert the correct J number details are returned
        self.assertEqual(result1, ['J:190949; Full Size; S1'])
        self.assertEqual(result2, ['J:190949; Full Size; 3'])

    def testImageJnumNoCopyrightSearch(self):
        """
        @Status tests that a basic Image J number Search that has no copyright will not display a copyright and not fail search works
        @see pwi-image-search-15
        """
        driver = self.driver
        #finds the J# field and enter a J Number for an expression image then click the Search button
        driver.find_element_by_id("JNumID").send_keys('2250')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the Copyright Field
        cpy = driver.find_element_by_id('copyrightID')
        print(cpy.text)
        #Assert the copyright field is clear of text
        self.assertEqual(cpy.text, '', 'The copyright field is not empty')
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        print(result1)
        #Assert the correct J number details are returned
        self.assertEqual(result1, ['J:2250; Full Size; 4'])
        self.assertEqual(result2, ['J:2250; Full Size; 5'])
        self.assertEqual(result3, ['J:2250; Full Size; 6'])
        self.assertEqual(result4, ['J:2250; Full Size; 7'])
        
        
        #*************************************************************************************************************

    def testImageCreateBySearch(self):
        """
        @Status tests that an image search using the Created By field returns correct data
        @see pwi-image-date-search-1
        """
        driver = self.driver
        #find the Modified By field and enter the user name
        driver.find_element_by_id("objectCreatedBy").send_keys("jx")
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #wait until the Reference table is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows of results
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        cell2 = table.get_row(2)
        cell3 = table.get_row(3)
        cell4 = table.get_row(4)
        cell5 = table.get_row(5)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'J:25; Full Size; 1')
        self.assertEqual(cell1.text, 'J:25; Full Size; 2')
        self.assertEqual(cell2.text, 'J:779; Full Size; 2')
        self.assertEqual(cell3.text, 'J:779; Full Size; 3')
        self.assertEqual(cell4.text, 'J:779; Full Size; 4')
        self.assertEqual(cell5.text, 'J:779; Full Size; 5')
        #Assert the correct Creation Name is returned in the Created By field
        createuser = driver.find_element_by_id('objectCreatedBy').get_attribute('value')
        self.assertEqual(createuser, 'jx')    

    def testImageModBySearch(self):
        """
        @Status tests that an image search using the Modified By field returns correct data
        @see pwi-image-date-search-2
        """
        driver = self.driver
        #find the Modified By field and enter the user name
        driver.find_element_by_id("objectModifiedBy").send_keys("ijm")
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #wait until the Reference table is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows of results
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        cell2 = table.get_row(2)
        cell3 = table.get_row(3)
        cell4 = table.get_row(4)
        cell5 = table.get_row(5)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'J:706; Full Size; 1')
        self.assertEqual(cell1.text, 'J:706; Full Size; 3')
        self.assertEqual(cell2.text, 'J:706; Full Size; 5')
        self.assertEqual(cell3.text, 'J:706; Full Size; 7')
        self.assertEqual(cell4.text, 'J:821; Full Size; 1')
        self.assertEqual(cell5.text, 'J:906; Full Size; 5')
        #Assert the correct Modified By Name is returned in the Modified By field
        moduser = driver.find_element_by_id('objectModifiedBy').get_attribute('value')
        self.assertEqual(moduser, 'ijm')        

    def testCreateDateSearch(self):
        """
        @Status tests that a basic Creation Date search works
        @see pwi-image-date-search-3
        """
        driver = self.driver
        #finds the Creation Date field, enters a Date
        driver.find_element_by_id("objectCreationDate").send_keys("2009-09-03")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows of results
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        cell2 = table.get_row(2)
        cell3 = table.get_row(3)
        cell4 = table.get_row(4)
        cell5 = table.get_row(5)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'J:91438; Full Size; 1')
        self.assertEqual(cell1.text, 'J:91438; Full Size; 2')
        self.assertEqual(cell2.text, 'J:91438; Full Size; 3')
        self.assertEqual(cell3.text, 'J:91438; Full Size; 4')
        self.assertEqual(cell4.text, 'J:91438; Full Size; 5')
        self.assertEqual(cell5.text, 'J:91438; Full Size; 6')
        #Assert the correct Creation Name is returned in the Creation Date field
        createdate = driver.find_element_by_id('objectCreationDate').get_attribute('value')
        self.assertEqual(createdate, '2009-09-03')        
             
    def testModifyDateSearch(self):
        """
        @Status tests that a basic Modification Date search works
        @see pwi-image-date-search-4
        """
        driver = self.driver
        #finds the Modification Date field, enters a Date
        driver.find_element_by_id("objectModificationDate").send_keys("2013-02-08")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        cell2 = table.get_row(2)
        cell3 = table.get_row(3)
        cell4 = table.get_row(4)
        cell5 = table.get_row(5)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'J:2959; Full Size; 3')
        self.assertEqual(cell1.text, 'J:2959; Full Size; 4')
        self.assertEqual(cell2.text, 'J:2959; Full Size; 5')
        self.assertEqual(cell3.text, 'J:2959; Full Size; 7')
        self.assertEqual(cell4.text, 'J:2959; Full Size; 8')
        self.assertEqual(cell5.text, 'J:2959; Full Size; 9')
        #Assert the correct Creation Name is returned in the Creation Date field
        modifydate = driver.find_element_by_id('objectModificationDate').get_attribute('value')
        self.assertEqual(modifydate, '2013-02-08')        
        
    def testModifyDateLessSearch(self):
        """
        @Status tests that a basic Modification Date by less than works
        @see pwi-image-date-search-7
        """
        driver = self.driver
        #finds the Modification Date field, enters a Date with less than symbol
        driver.find_element_by_id("objectModificationDate").send_keys('<2005-09-16')
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'J:47; Full Size; 1')
        self.assertEqual(cell1.text, 'J:886; Full Size; 1')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('objectModificationDate').get_attribute('value')
        self.assertEqual(modifydate, '1999-03-04')        

    def testModifyDateLessEqualSearch(self):
        """
        @Status tests that a basic Modification Date by less than equals works
        @see pwi-image-date-search-8
        """
        driver = self.driver
        #finds the Modification Date field, enters a Date with less than symbol
        driver.find_element_by_id("objectModificationDate").send_keys('<=2009-09-14')
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'J:47; Full Size; 1')
        self.assertEqual(cell1.text, 'J:767; Full Size; 2')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('objectModificationDate').get_attribute('value')
        self.assertEqual(modifydate, '1999-03-04')        
      
    def testModifyDateRangeSearch(self):
        """
        @Status tests that a basic Modification Date by range search works
        @see pwi-image-date-search-9
        """
        driver = self.driver
        #finds the Modification Date field, enters a range of Dates
        driver.find_element_by_id("objectModificationDate").send_keys("2019-05-08..2019-05-09")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'J:77376; Full Size; 3')
        self.assertEqual(cell1.text, 'J:77376; Full Size; 4')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('objectModificationDate').get_attribute('value')
        self.assertEqual(modifydate, '2019-05-09')  
              

        
    def testCreateDateLessSearch(self):
        """
        @Status tests that a basic Creation Date by less than works
        @see pwi-image-date-search-12
        """
        driver = self.driver
        #finds the Creation Date field, enters a Date with less than symbol
        driver.find_element_by_id("objectCreationDate").send_keys('<2005-09-13')
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'J:47; Full Size; 1')
        self.assertEqual(cell1.text, 'J:47; Full Size; 2')
        #Assert the correct Creation Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('objectCreationDate').get_attribute('value')
        self.assertEqual(modifydate, '1999-03-04')        

    def testCreateDateLessEqualSearch(self):
        """
        @Status tests that a basic Creation Date by less than equals works
        @see pwi-image-date-search-13
        """
        driver = self.driver
        #finds the Creation Date field, enters a Date with less than symbol
        driver.find_element_by_id("objectCreationDate").send_keys('<=1998-06-22')
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbol has been returned in the results table
        self.assertEqual(cell0.text, 'J:1309; Full Size; 1')
        self.assertEqual(cell1.text, 'J:19231; Full Size; 1')
        #Assert the correct Creation Date is returned in the Creation Date field
        createdate = driver.find_element_by_id('objectCreationDate').get_attribute('value')
        self.assertEqual(createdate, '1998-06-22')        
      
    def testCreateDateRangeSearch(self):
        """
        @Status tests that a basic Modification Date by range search works
        @see pwi-image-date-search-14
        """
        driver = self.driver
        #finds the Creation Date field, enters a range of Dates
        driver.find_element_by_id("objectCreationDate").send_keys("1998-06-22..1998-07-16")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbols has been returned in the results table
        self.assertEqual(cell0.text, 'J:1309; Full Size; 1')
        self.assertEqual(cell1.text, 'J:9556; Full Size; 2')
        #Assert the correct Creation Date is returned in the Creation Date field
        createdate = driver.find_element_by_id('objectCreationDate').get_attribute('value')
        self.assertEqual(createdate, '1998-06-22')        

    def testImgJnumNoCopySearch(self):
        """
        @Status tests that a J number search that has no copyright does not fail but works
        @see pwi-image-date-search-15
        """
        driver = self.driver
        #finds the J# field and enters a J number
        driver.find_element_by_id("JNumID").send_keys("J:2250")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct symbols has been returned in the results table
        self.assertEqual(cell0.text, 'J:2250; Full Size; 4')
        #Assert the copyright field is blank
        copyrgt = driver.find_element_by_id('copyrightID')
        self.assertEqual(copyrgt.text, "                                ")         

    def testAccTypePaintSearch(self):
        """
        @Status tests that a basic Image Accession Type GenePaint search works
        @attention: The EC webdriverwait code needs to be worked on/fixed when time allows
        @see pwi-image-search-27 **Test passes but is very very slow now! 3/20/2020
        """
        driver = self.driver
        #finds the Image Other Accession Ids pulldown and selects "GenePaint" option, find the Other Accession ID field and enter a genepaint ID, then click the Search button
        Select(driver.find_element_by_id("accidTypeID")).select_by_value('105')
        driver.find_element_by_id('otherAccId').send_keys('%DA,-A82,-Asetstart,%')
        driver.find_element_by_id('searchButton').click()
        time.sleep(90)
        #WebDriverWait(driver, 90).until(EC.text_to_be_present_in_element((By.ID, "resultsCount")))
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        cell6 = table.get_row_cells(5)
        cell7 = table.get_row_cells(6)
        cell8 = table.get_row_cells(7)
        cell9 = table.get_row_cells(8)
        cell10 = table.get_row_cells(9)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        result6 = iterate.getTextAsList(cell6)
        result7 = iterate.getTextAsList(cell7)
        result8 = iterate.getTextAsList(cell8)
        result9 = iterate.getTextAsList(cell9)
        result10 = iterate.getTextAsList(cell10)        
        print(result1)
        #Assert the correct J number details are returned(for the first 10 results)
        self.assertEqual(result1, ['J:122989; Full Size; Embryo_DA4_8_1A'])
        self.assertEqual(result2, ['J:122989; Full Size; Embryo_DA4_8_1B'])
        self.assertEqual(result3, ['J:122989; Full Size; Embryo_DA4_8_1D'])
        self.assertEqual(result4, ['J:122989; Full Size; Embryo_DA4_8_2B'])
        self.assertEqual(result5, ['J:122989; Full Size; Embryo_DA4_8_3A'])
        self.assertEqual(result6, ['J:122989; Full Size; Embryo_DA4_8_3B'])
        self.assertEqual(result7, ['J:122989; Full Size; Embryo_DA4_8_3C'])
        self.assertEqual(result8, ['J:122989; Full Size; Embryo_DA4_8_4A'])
        self.assertEqual(result9, ['J:122989; Full Size; Embryo_DA4_8_4B'])
        self.assertEqual(result10, ['J:122989; Full Size; Embryo_DA4_8_5B'])
        #find the Other Accession Ids table
        accid_table = self.driver.find_element_by_id("otherAccIdTable")
        table = Table(accid_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct Acc ID result details are returned
        self.assertEqual(result1, ['GenePaint', 'DA,-A82,-Asetstart,-A1'])
       
    def testAccTypeGudmapSearch(self):
        """
        @Status tests that a basic Image Accession Type Gudmap search works
        @attention: The EC webdriverwait code needs to be worked on/fixed when time allows
        @see pwi-image-search-28
        """
        driver = self.driver
        #finds the Image Other Accession Ids pulldown and selects "Gudmap" option then click the Search button
        Select(driver.find_element_by_id("accidTypeID")).select_by_value('163')
        driver.find_element_by_id('searchButton').click()
        time.sleep(10)
        #WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.ID, "resultsCount")))
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        cell6 = table.get_row_cells(5)
        cell7 = table.get_row_cells(6)
        cell8 = table.get_row_cells(7)
        cell9 = table.get_row_cells(8)
        cell10 = table.get_row_cells(9)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        result6 = iterate.getTextAsList(cell6)
        result7 = iterate.getTextAsList(cell7)
        result8 = iterate.getTextAsList(cell8)
        result9 = iterate.getTextAsList(cell9)
        result10 = iterate.getTextAsList(cell10)        
        print(result1)
        #Assert the correct J number details are returned(for the first 10 results)
        self.assertEqual(result1, ['J:171409; Full Size; GUDMAP:3'])
        self.assertEqual(result2, ['J:171409; Full Size; GUDMAP:4'])
        self.assertEqual(result3, ['J:171409; Full Size; GUDMAP:5'])
        self.assertEqual(result4, ['J:171409; Full Size; GUDMAP:9'])
        self.assertEqual(result5, ['J:171409; Full Size; GUDMAP:10'])
        self.assertEqual(result6, ['J:171409; Full Size; GUDMAP:15'])
        self.assertEqual(result7, ['J:171409; Full Size; GUDMAP:16'])
        self.assertEqual(result8, ['J:171409; Full Size; GUDMAP:22'])
        self.assertEqual(result9, ['J:171409; Full Size; GUDMAP:23'])
        self.assertEqual(result10, ['J:171409; Full Size; GUDMAP:26'])
        #find the Other Accession Ids table
        accid_table = self.driver.find_element_by_id("otherAccIdTable")
        table = Table(accid_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct Acc ID result details are returned
        self.assertEqual(result1, ['GUDMAP', 'GUDMAP:3'])
       
    def testAccTypeEurexpressSearch(self):
        """
        @Status tests that a basic Image Accession Type Eurexpress search works
        @attention: The EC webdriverwait code needs to be worked on/fixed when time allows
        @see pwi-image-search-30
        """
        driver = self.driver
        #finds the Image Other Accession Ids pulldown and selects "Eurpexpress" option then click the Search button
        Select(driver.find_element_by_id("accidTypeID")).select_by_value('148')
        driver.find_element_by_id('searchButton').click()
        time.sleep(15)
        #wait = WebDriverWait(driver, 20)
        #element = wait.until(EC.text_to_be_present_in_element((By.ID, "resultsTable")));
        #element.view()
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        cell6 = table.get_row_cells(5)
        cell7 = table.get_row_cells(6)
        cell8 = table.get_row_cells(7)
        cell9 = table.get_row_cells(8)
        cell10 = table.get_row_cells(9)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        result6 = iterate.getTextAsList(cell6)
        result7 = iterate.getTextAsList(cell7)
        result8 = iterate.getTextAsList(cell8)
        result9 = iterate.getTextAsList(cell9)
        result10 = iterate.getTextAsList(cell10)        
        print(result1)
        #Assert the correct J number details are returned(for the first 10 results)
        self.assertEqual(result1, ['J:153498; Full Size; euxassay_000001_01'])
        self.assertEqual(result2, ['J:153498; Full Size; euxassay_000001_02'])
        self.assertEqual(result3, ['J:153498; Full Size; euxassay_000001_03'])
        self.assertEqual(result4, ['J:153498; Full Size; euxassay_000001_04'])
        self.assertEqual(result5, ['J:153498; Full Size; euxassay_000001_05'])
        self.assertEqual(result6, ['J:153498; Full Size; euxassay_000001_06'])
        self.assertEqual(result7, ['J:153498; Full Size; euxassay_000001_07'])
        self.assertEqual(result8, ['J:153498; Full Size; euxassay_000001_08'])
        self.assertEqual(result9, ['J:153498; Full Size; euxassay_000001_09'])
        self.assertEqual(result10, ['J:153498; Full Size; euxassay_000001_10'])
        #find the Other Accession Ids table
        accid_table = self.driver.find_element_by_id("otherAccIdTable")
        table = Table(accid_table)
        #Iterate and print the search results
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct Acc ID result details are returned
        self.assertEqual(result1, ['Eurexpress', 'euxassay_000001_01'])             


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiImageSearch))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
    