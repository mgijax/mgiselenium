'''
Created on Jul 13, 2020
These tests verify testing of the search feature for the Antigen EI/PWI module.
@author: jeffc
'''
import unittest
import time
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import json
import sys, os.path
from test.test_base64 import BaseXYTestCase

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table


# Tests
tracemalloc.start()
class TestEIAntigenSearch(unittest.TestCase):
    """
    @status Test Antigen searching, etc
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/antigen")

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

    def testAntigenNameSearch(self):
        """
        @Status tests that a basic antigen name search works
        @see pwi-antigen-search-1
        """
        driver = self.driver
        # finds the Antigen Name field and enters an antigen name, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antigenName").send_keys('Ant-1')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Ant-1'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct antigen is returned
        self.assertEqual(symbol1, ['Ant-1'])

    def testAntigenName2Search(self):
        """
        @Status tests that a basic antigen name search works
        @see pwi-antigen-search-1
        """
        driver = self.driver
        # finds the Antigen Name field and enters an antigen name w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antigenName").send_keys('bre%')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'brevican'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct antigen is returned
        self.assertEqual(symbol1, ['brevican'])

    def testAntigenRegionSearch(self):
        """
        @Status tests that a basic region search works
        @see pwi-antigen-search-2
        """
        driver = self.driver
        # finds the region field and enters an region name, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "regionCovered").send_keys('amino acids 1-76')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), '5-HT-2A-R (N-terminus)'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct antigen is returned
        self.assertEqual(symbol1, ['5-HT-2A-R (N-terminus)'])

    def testAntigenRegion2Search(self):
        """
        @Status tests that a basic region search works with wildcard
        @see pwi-antigen-search-2
        """
        driver = self.driver
        # finds the region field and enters an region name w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "regionCovered").send_keys('GDVES%')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), '2A peptide'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct antigen is returned
        self.assertEqual(symbol1, ['2A peptide'])

    def testAntigenNotesSearch(self):
        """
        @Status tests that a basic notes search works
        @see pwi-antigen-search-3
        """
        driver = self.driver
        # finds the notes field and enters test, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antigenNote").send_keys('recombinant protein')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'AMH'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        symbol3 = iterate.getTextAsList(cell3)
        symbol4 = iterate.getTextAsList(cell4)
        symbol5 = iterate.getTextAsList(cell5)
        print(symbol1)
        # Assert the correct antigens are returned(first 5)
        self.assertEqual(symbol1, ['ACP2'])
        self.assertEqual(symbol2, ['Adiponectin'])
        self.assertEqual(symbol3, ['ALDH1L1'])
        self.assertEqual(symbol4, ['AMH'])
        self.assertEqual(symbol5, ['AML1-b'])

    def testAntigenNotes1Search(self):
        """
        @Status tests that a basic notes search w/wildcard works
        @see pwi-antigen-search-3
        """
        driver = self.driver
        # finds the notes field and enters text w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antigenNote").send_keys('%fragment')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'HAND2'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        symbol3 = iterate.getTextAsList(cell3)
        symbol4 = iterate.getTextAsList(cell4)
        symbol5 = iterate.getTextAsList(cell5)
        print(symbol1)
        # Assert the correct antigens are returned(first 5)
        self.assertEqual(symbol1, ['E-cadherin'])
        self.assertEqual(symbol2, ['EFTUD2'])
        self.assertEqual(symbol3, ['Epha4, C-terminus'])
        self.assertEqual(symbol4, ['FXR2'])
        self.assertEqual(symbol5, ['HAND2'])

    def testAntigenOrganismSearch(self):

        """
        @Status tests that a basic organism search works
        @see pwi-antigen-search-4
        """
        driver = self.driver
        # finds the organism field and selects the option "Carp' (value='string:62), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "organism")).select_by_value('string:62')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'carp-II parvalbumin'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct antigen is returned
        self.assertEqual(symbol1, ['carp-II parvalbumin'])

    def testAntigenStrainSearch(self):
        """
        @Status tests that a basic strain search works
        @see pwi-antigen-search-5
        """
        driver = self.driver
        time.sleep(2)
        # finds the strain field and enters a strain, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "editTabStrain").send_keys('AKR')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'CD49d'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct antigen is returned
        self.assertEqual(symbol1, ['CD49d'])

    def testAntigenStrain1Search(self):
        """
        @Status tests that a basic strain search w/wildcard works
        @see pwi-antigen-search-5
        """
        driver = self.driver
        # finds the strain field and enters a strain w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "editTabStrain").send_keys('C3H%')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'hsc74'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        symbol3 = iterate.getTextAsList(cell3)
        print(symbol1)
        # Assert the correct antigens are returned
        self.assertEqual(symbol1, ['32D leukocyte'])
        self.assertEqual(symbol2, ['hsc74'])
        self.assertEqual(symbol3, ['PECAM1'])

    def testAntigenTissueSearch(self):
        """
        @Status tests that a basic tissue search works
        @see pwi-antigen-search-6
        """
        driver = self.driver
        # finds the tissue field and enters a tissue, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "editTabTissue").send_keys('intestine')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), '28 K CaBP'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct antigen is returned
        self.assertEqual(symbol1, ['28 K CaBP'])

    def testAntigenTissue1Search(self):
        """
        @Status tests that a basic tissue search w/wildcard works
        @see pwi-antigen-search-6
        """
        driver = self.driver
        # finds the tissue field and enters a tissue w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "editTabTissue").send_keys('test%')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Acrogranin'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        symbol3 = iterate.getTextAsList(cell3)
        print(symbol1)
        # Assert the correct antigens are returned(first 3)
        self.assertEqual(symbol1, ['Acrogranin'])
        self.assertEqual(symbol2, ['Clone 4'])
        self.assertEqual(symbol3, ['GENA'])

    def testAntigenTissueDescSearch(self):
        """
        @Status tests that a basic tissue description search works
        @see pwi-antigen-search-7
        """
        driver = self.driver
        # finds the tissue description field and enters a description, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "description").send_keys('cell lysates')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'JLP'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct antigen is returned
        self.assertEqual(symbol1, ['JLP'])

    def testAntigenTissueDesc1Search(self):
        """
        @Status tests that a basic tissue description search w/wildcard works
        @see pwi-antigen-search-7
        """
        driver = self.driver
        # finds the tissue Description field and enters a description w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "description").send_keys('membrane%')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'KCC2'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        symbol3 = iterate.getTextAsList(cell3)
        symbol4 = iterate.getTextAsList(cell4)
        print(symbol1)
        # Assert the correct antigens are returned(first 3)
        self.assertEqual(symbol1, ['alpha-dystroglycan'])
        self.assertEqual(symbol2, ['brain membrane'])
        self.assertEqual(symbol3, ['KCC2'])
        self.assertEqual(symbol4, ['Na+/K+ ATPase alpha-1'])

    def testAntigenCelllineSearch(self):
        """
        @Status tests that a basic cell line search works
        @see pwi-antigen-search-8
        """
        driver = self.driver
        # finds the cell line field and enter a cell line, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "editTabCellLine").send_keys('HEK293T')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'agrin'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct antigen is returned
        self.assertEqual(symbol1, ['agrin'])

    def testAntigenCellline1Search(self):
        """
        @Status tests that a basic cell line search w/wildcard works
        @see pwi-antigen-search-8
        """
        driver = self.driver
        # finds the cell line field and enters a description w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "editTabCellLine").send_keys('%cell Line%')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Cathepsin L'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        symbol3 = iterate.getTextAsList(cell3)
        print(symbol1)
        # Assert the correct antigens are returned(first 3)
        self.assertEqual(symbol1, ['alpha6 integrin'])
        self.assertEqual(symbol2, ['Cathepsin L'])
        self.assertEqual(symbol3, ['CD117/c-kit'])

    def testAntigenAgePrefixSearch(self):
        """
        @Status tests that a basic age prefix search works
        @see pwi-antigen-search-9
        """
        driver = self.driver
        # finds the age prefix field and select the option 'postnatal day', tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "age")).select_by_value('string:postnatal day')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'glycoprotein'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        symbol3 = iterate.getTextAsList(cell3)
        print(symbol1)
        # Assert the correct antigen is returned
        self.assertEqual(symbol1, ['CAII'])
        self.assertEqual(symbol2, ['glycoprotein'])
        self.assertEqual(symbol3, ['L1 antigen'])

    def testAntigenAgeRangeSearch(self):
        """
        @Status tests that a basic age range search works
        @see pwi-antigen-search-9
        """
        driver = self.driver
        # finds the age range field and enters an age range, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "ageStage").send_keys('8-10')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'neural cell adhesion molecule L1'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        print(symbol1)
        # Assert the correct antigens are returned(first 3)
        self.assertEqual(symbol1, ['L1 antigen'])
        self.assertEqual(symbol2, ['neural cell adhesion molecule L1'])

    def testAntigenGenderSearch(self):
        """
        @Status tests that a basic gender search works
        @see pwi-antigen-search-10
        """
        driver = self.driver
        # finds the gender field and enter the option 'female'(string:315164, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "gender")).select_by_value('string:315164')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'p120 CEA-related protein'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct antigens are returned(first 3)
        self.assertEqual(symbol1, ['p120 CEA-related protein'])

    def testAntigenAccIDSearch(self):
        """
        @Status tests that a basic ACC ID search works
        @see pwi-antigen-search-11
        """
        driver = self.driver
        # finds the ACC ID field and enter an ID, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antibodyID-0").send_keys('MGI:3829719')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'thiolase A'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct antigens are returned
        self.assertEqual(symbol1, ['thiolase A'])

    def testAntigenAntibodyNameSearch(self):
        """
        @Status tests that a basic antibody name search works
        @see pwi-antigen-search-12
        """
        driver = self.driver
        # finds the antibody name field and enter a name, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antibodyName-0").send_keys('thiolase A antibody')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'thiolase A'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct antigen is returned
        self.assertEqual(symbol1, ['thiolase A'])

    def testAntigenAntibodyName1Search(self):
        """
        @Status tests that a basic antidoby name search w/wildcard works
        @see pwi-antigen-search-12
        """
        driver = self.driver
        # finds the antibody name field and enters a name w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antibodyName-0").send_keys('TES101%')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'testes'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct antigens are returned
        self.assertEqual(symbol1, ['testes'])

    def testAntigenCreateBySearch(self):
        """
        @Status tests that an antigen search using the Created By field returns correct data
        @see pwi-antigen-date-search-1
        """
        driver = self.driver
        # find the antigen Created By field and enter the name
        driver.find_element(By.ID, "createdBy").send_keys("jx")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), '5-HTT'))
        # find the Created by field
        create_by = driver.find_element(By.ID, 'createdBy').get_attribute('value')
        print(create_by)
        # Assert the  Created By field returned is correct
        self.assertEqual(create_by, 'jx')
        # find the Creation Date field
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        # Assert the  Creation Date field returned is correct
        self.assertEqual(create_date, '2020-06-18')

    def testAntigenModBySearch(self):
        """
        @Status tests that an antigen search using the Modified By field returns correct data
        @see pwi-antigen-date-search-2
        """
        driver = self.driver
        # find the alleles Modified by field and enter the name
        driver.find_element(By.ID, "modifiedBy").send_keys("terryh")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), '921-L'))
        # find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        # Assert the  Modified By field returned is correct
        self.assertEqual(mod_by, 'terryh')
        # find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        # Assert the Modification Date field returned is correct
        self.assertEqual(mod_date, '2022-08-11')

    def testAntigenCreateDateSearch(self):
        """
        @Status tests that an antigen search using the Creation Date field returns correct data
        @see pwi-antigen-date-search-3
        """
        driver = self.driver
        # find the antigen Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("2013-01-23")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'M-cadherin'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        # Assert the  Creation Date field returned is correct
        self.assertEqual(create_date, '2013-01-23')

    def testAntigenModDateSearch(self):
        """
        @Status tests that an antigen search using the Modified By field returns correct data
        @see pwi-antigen-date-search-4
        """
        driver = self.driver
        # find the antigen Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("2013-01-02")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'EphA4'))
        # find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        # Assert the Modification Date field returned is correct
        self.assertEqual(mod_date, '2013-01-02')

    def testAntigenModDateLessSearch(self):
        """
        @Status tests that an antigen search using the Modified By field and less than returns correct data
        @see pwi-antigen-date-search-7
        """
        driver = self.driver
        # find the antigen Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("<1998-09-14")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Syk'))
        # find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        # Assert the  Modified By field returned is correct
        self.assertEqual(mod_by, 'dbo')
        # find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        # Assert the Modification Date field returned is correct
        self.assertEqual(mod_date, '1998-08-10')

    def testAntigenModDateLessEqualSearch(self):
        """
        @Status tests that an antigen search using the Modified By field and less than or equal to returns correct data
        @see pwi-antigen-date-search-8
        """
        driver = self.driver
        # find the antigen Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("<=1998-09-14")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Syk'))
        # find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        # Assert the  Modified By field returned is correct
        self.assertEqual(mod_by, 'dbo')
        # find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        # Assert the Modification Date field returned is correct
        self.assertEqual(mod_date, '1998-09-14')

    def testAntigenModDateBetweenSearch(self):
        """
        @Status tests that an antigen search using the Modified By field and between dates returns correct data
        @see pwi-antigen-date-search-9
        """
        driver = self.driver
        # find the antigen Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("1998-08-04..1998-08-10")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Syk'))
        # find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        # Assert the  Modified By field returned is correct
        self.assertEqual(mod_by, 'dbo')
        # find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        # Assert the Modification Date field returned is correct
        self.assertEqual(mod_date, '1998-08-10')

    def testAntigenCreateDateLessSearch(self):
        """
        @Status tests that an antigen search using the Creation Date field and Less than returns correct data
        @see pwi-antigen-date-search-12
        """
        driver = self.driver
        # find the antigen Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("<1998-06-23")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'uvomorulin'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        # Assert the  Creation Date field returned is correct
        self.assertEqual(create_date, '1998-06-22')

    def testAntigenCreateDateLessEqualSearch(self):
        """
        @Status tests that an antigen search using the Creation Date field and Less than, equals to returns correct data
        @see pwi-antigen-date-search-13
        """
        driver = self.driver
        # find the alleles Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("<=1998-06-23")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'uvomorulin'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        # Assert the  Creation Date field returned is correct
        self.assertEqual(create_date, '1998-06-22')

    def testAntigenCreateDateBetweenSearch(self):
        """
        @Status tests that an antigen search using the Creation Date field and Between dates returns correct data
        @see pwi-antigen-date-search-14
        """
        driver = self.driver
        # find the antigen Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("1998-06-22..1998-07-09")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'uvomorulin'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        # Assert the  Creation Date field returned is correct
        self.assertEqual(create_date, '1998-07-09')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEIAntigenSearch))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))