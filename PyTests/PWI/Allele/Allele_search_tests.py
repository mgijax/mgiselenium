'''
Created on Apr 6, 2020
These are tests that check the searching options of the Allele module
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
class TestEIAlleleSearch(unittest.TestCase):
    """
    @status Test Genotype searching, etc
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/allele")

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

    def testAlleleSymbolSearch(self):
        """
        @Status tests that a basic allele symbol search works
        @see pwi-allele-search-1
        """
        driver = self.driver
        # finds the Strain field and enters a strain w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "symbol").send_keys('Gata1<tm1Sho>')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned
        self.assertEqual(symbol1, ['Gata1<tm1Sho>'])

    def testAlleleNameSearch(self):
        """
        @Status tests that a basic allele name search works
        @see pwi-allele-search-2
        """
        driver = self.driver
        # finds the Strain field and enters a strain w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "name").send_keys('jerker')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned
        self.assertEqual(symbol1, ['Espn<je>'])

    def testAlleleMrkSymbolSearch(self):
        """
        @Status tests that a basic allele marker symbol search works
        @see pwi-allele-search-3
        """
        driver = self.driver
        # finds the Strain field and enters a strain w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "markerSymbol-0").send_keys('Espn')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        print(symbol1)
        print(symbol2)
        # Assert the correct allele symbol is returned
        self.assertEqual(symbol1, ['Espn<+>'])
        self.assertEqual(symbol2, ['Espn<em1Smoc>'])

    def testAlleleMrkJnumSearch(self):
        """
        @Status tests that a basic allele marker symbol J number search works
        @see pwi-allele-search-4
        """
        driver = self.driver
        # finds the Marker J number field and enters a J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "markerjnumID-0").send_keys('J:266040')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned
        self.assertEqual(symbol1, ['Notum<Gt(OST172035)Lex>'])

    def testAlleleMrkStatusSearch(self):
        """
        @Status tests that a basic allele marker symbol status curated search works
        @see pwi-allele-search-5
        """
        driver = self.driver
        # finds the Marker Curated field and select the option 'curated'value=string:4268545, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "markerAlleleStatus")).select_by_value('string:4268545')
        # finds the Created by field and enters the name hdene
        driver.find_element(By.ID, "createdBy").send_keys('hdene')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Gt(ROSA)26Sor<tm1(CAG-GFP)Pec>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is first result of over 4000
        self.assertEqual(symbol1, ['Gt(ROSA)26Sor<tm1(CAG-GFP)Pec>'])

    def testAlleleMrkStatus2Search(self):
        """
        @Status tests that a basic allele marker symbol status search for Curated invalidated works
        @see pwi-allele-search-6
        """
        driver = self.driver
        # finds the Marker status field and select the option 'curated invalidated'value=string:4268546, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "markerAlleleStatus")).select_by_value('string:4268546')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(10)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Adissp<Gt(D053F10)Wrst>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(2)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is first result of over 35
        self.assertEqual(symbol1, ['Adissp<Gt(D053F10)Wrst>'])

    def testAlleleMrkStatus3Search(self):
        """
        @Status tests that a basic allele marker symbol status search for loaded works
        @see pwi-allele-search-7
        """
        driver = self.driver
        # finds the Allele Symbol field and enters a symbol w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "symbol").send_keys('Pax6<Gt%')
        # finds the Marker status field and select the option 'loaded'value=string:4268544, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "markerAlleleStatus")).select_by_value('string:4268544')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(10)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Pax6<Gt(IST14982A1)Tigm>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell5 = table.get_row_cells(4)
        symbol5 = iterate.getTextAsList(cell5)
        print(symbol5)
        # Assert the correct allele symbol is returned, this is first and only result
        self.assertEqual(symbol5, ['Pax6<Gt(IST14982A1)Tigm>'])

    def testAlleleStatusSearch(self):
        """
        @Status tests that a basic allele status search for In Progress works
        @see pwi-allele-search-8
        """
        driver = self.driver
        # finds the Allele Symbol field and enters a symbol w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "symbol").send_keys('Acap1%')
        # finds the Allele status field and select the option 'In Progress'value=string:847111, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "alleleStatus")).select_by_value('string:847111')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(10)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Acap1<crf12.1>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Acap1<crf12.1>'])

    def testAlleleStatus2Search(self):
        """
        @Status tests that a basic allele status search for Reserved works
        @see pwi-allele-search-9
        """
        driver = self.driver
        # finds the Allele Symbol field and enters a symbol w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "symbol").send_keys('Aacs%')
        # finds the Allele status field and select the option 'Reserved'value=string:847113, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "alleleStatus")).select_by_value('string:847113')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(10)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Aacs<Sum13-Jus>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Aacs<Sum13-Jus>'])

    def testAlleleGenerationSearch(self):
        """
        @Status tests that a basic allele generation search for Chemically and Radiation induced works
        @see pwi-allele-search-10
        """
        driver = self.driver
        # finds the Allele Symbol field and enters a symbol w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "symbol").send_keys('and%')
        # finds the Allele generation field and select the option 'Chemically and Radiation induced'value=string:847124, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "alleleType")).select_by_value('string:847124')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(10)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'andra'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['andra'])

    def testAlleleGeneration2Search(self):
        """
        @Status tests that a basic allele generation search for Transposon induced works
        @see pwi-allele-search-11
        """
        driver = self.driver
        # finds the Allele Symbol field and enters a symbol w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "symbol").send_keys('car%')
        # finds the Allele generation field and select the option 'Transposon induced'value=string:2327161, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "alleleType")).select_by_value('string:2327161')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Car12<Tn(sb-T2/GT2/tTA)4563.1Dla>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Car12<Tn(sb-T2/GT2/tTA)4563.1Dla>'])

    def testAlleleInheritanceSearch(self):
        """
        @Status tests that a basic allele Inheritance search for Codorminent works
        @see pwi-allele-search-12
        """
        driver = self.driver
        # finds the Allele inheritance mode field and select the option 'codorminent'value=string:847090, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "inheritance")).select_by_value('string:847090')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Acads<a>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the first result of over 90
        self.assertEqual(symbol1, ['Acads<a>'])

    def testAlleleInheritance2Search(self):
        """
        @Status tests that a basic allele Inheritance search for Semidorminent works
        @see pwi-allele-search-13
        """
        driver = self.driver
        # finds the Allele Symbol field and enters a symbol w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "symbol").send_keys('hal%')
        # finds the Allele inheritance mode field and select the option 'semidorminent'value=string:847091, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "inheritance")).select_by_value('string:847091')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Hal<Ed1>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Hal<Ed1>'])

    def testAlleleGermLineSearch(self):
        """
        @Status tests that a basic allele Germ Line search for Chimeric works
        @see pwi-allele-search-14
        """
        driver = self.driver
        # finds the Allele germ line field and select the option 'chimeric'value=string:3982952, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "transmission")).select_by_value('string:3982952')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Hoxd10<tm1Ipc>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the first result of over 130 results
        self.assertEqual(symbol1, ['Hoxd10<tm1Ipc>'])

    def testAlleleCollectionSearch(self):
        """
        @Status tests that a basic allele collection search for NorCOMM works
        @see pwi-allele-search-15
        """
        driver = self.driver
        # finds the Allele Symbol field and enters a symbol w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "symbol").send_keys('Aat%')
        # finds the Allele collection field and select the option 'NorCOMM'value=string:11025571, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "collection")).select_by_value('string:11025571')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Aatk<tm1(NCOM)Mfgc>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Aatk<tm1(NCOM)Mfgc>'])

    def testAlleleMixedSearch(self):
        """
        @Status tests that a basic allele mixed search for Yes works
        @see pwi-allele-search-16
        """
        driver = self.driver
        # finds the Allele Symbol field and enters a symbol w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "symbol").send_keys('Cnot%')
        # finds the Allele mixed field and select the option 'Yes'value=string:1, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "isMixed")).select_by_value('string:1')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Cnot1<Gt(D045D10)Wrst>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Cnot1<Gt(D045D10)Wrst>'])

    def testAlleleExtinctSearch(self):
        """
        @Status tests that a basic allele Extinct search for Yes works
        @see pwi-allele-search-17
        """
        driver = self.driver
        # finds the Allele Symbol field and enters a symbol w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "symbol").send_keys('Eda%')
        # finds the Allele extinct field and select the option 'Yes'value=string:1, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "isExtinct")).select_by_value('string:1')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Eda<Ta-3J>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Eda<Ta-3J>'])

    def testAlleleRefJnumSearch(self):
        """
        @Status tests that a basic allele Reference J number search works
        @see pwi-allele-search-19
        """
        driver = self.driver
        # finds the Allele J# field, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "refjnumID-0").send_keys('J:181531')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Ednrb<s-163H>-deleted'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Ednrb<s-163H>-deleted'])

    def testAlleleMutantCellLineSearch(self):
        """
        @Status tests that a basic allele Mutant Cell Line search works
        @see pwi-allele-search-20
        """
        driver = self.driver
        # finds the Mutant Cell Line field, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "mutantCellLine-0").send_keys('289B06')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Espn<Gt(289B06)Cmhd>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Espn<Gt(289B06)Cmhd>'])

    def testAlleleMutantCellLineCreateSearch(self):
        """
        @Status tests that a basic allele Muatant Cell Line Creator search works
        @see pwi-allele-search-21
        """
        driver = self.driver
        # finds the Allele Symbol field and enters a symbol w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "symbol").send_keys('Cnot%')
        # finds the Mutant Cell Line Creator field, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "creator-0").send_keys('Velocigene')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Cnot4<tm1(KOMP)Vlcg>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the first result of 2?
        self.assertEqual(symbol1, ['Cnot1<tm1a(EUCOMM)Hmgu>'])

    def testAlleleMutantCellLineModBySearch(self):
        """
        @Status tests that a basic allele Mutant Cell Line Modified by search works
        @see pwi-allele-search-22
        """
        driver = self.driver
        # finds the Allele Symbol field and enters a symbol w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "symbol").send_keys('Air%')
        # finds the Mutant Cell Line Modified By field, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "modifiedBy-0").send_keys('dlb')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Airn<tm3.1Dpb>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Airn<tm3.1Dpb>'])

    def testAlleleMutantCellLineModDateSearch(self):
        """
        @Status tests that a basic allele Mutant Cell Line Modification Date search works
        @see pwi-allele-search-23
        """
        driver = self.driver
        # finds the Mutant Cell Line Modification date field, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "modification_date-0").send_keys('2010-05-21')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Hprt<b-m4>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the first result of about 5
        self.assertEqual(symbol1, ['Hprt<b-m4>'])

    def testAlleleCellLineTypeSearch(self):
        """
        @Status tests that a basic allele cell line type search
        @see pwi-allele-search-24
        """
        driver = self.driver
        # finds the Allele collection field and select the option 'NorCOMM'value=string:11025571, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "cellLineType")).select_by_value('string:3982969')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Ocln<Gt(ROSA)39Tshi>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Ocln<Gt(ROSA)39Tshi>'])

    def testAlleleMGIIDSearch(self):
        """
        @Status tests that a basic allele MGI ID search
        @see pwi-allele-search-25
        """
        driver = self.driver
        # finds the Allele MGI ID field and enters an allele MGI ID, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "accID").send_keys('MGI:3640976')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Ocln<Gt(ROSA)39Tshi>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Ocln<Gt(ROSA)39Tshi>'])

    def testAlleleMrkDetailClipSearch(self):
        """
        @Status tests that a basic allele Marker Detail Clip search
        @see pwi-allele-search-26
        """
        driver = self.driver
        # Find and click the Marker Detail Clip button
        driver.find_element(By.ID, "hideShowDetailClipButton").click()
        # finds the Allele Marker Detail Clip and enters a text string, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "markerDetailClip").send_keys('%extraembryonic membrane and endoderm%')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Smad4<tm2Rob>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the first result of over 45
        self.assertEqual(symbol1, ['Smad4<tm2Rob>'])

    def testAlleleMolecularNoteSearch(self):
        """
        @Status tests that a basic allele Molecular Note search
        @see pwi-allele-search-27
        """
        driver = self.driver
        # Find and click the Molecular button
        driver.find_element(By.ID, "hideShowMolecularNoteButton").click()
        # finds the Allele Molecular Note and enters a text string, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "molecularNote").send_keys('%gene trap vector%')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Bicral<Gt(U3Betageo)1Ruiz>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the first result of over 1000
        self.assertEqual(symbol1, ['Bicral<Gt(U3Betageo)1Ruiz>'])

    def testAlleleGeneralNoteSearch(self):
        """
        @Status tests that a basic allele General Note search
        @see pwi-allele-search-28
        """
        driver = self.driver
        # Find and click the General button
        driver.find_element(By.ID, "hideShowGeneralNoteButton").click()
        # finds the Allele General Note and enters a text string, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "generalNote").send_keys('%electroporated%')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Bicral<Gt(U3Betageo)1Ruiz>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the first result of over 30
        self.assertEqual(symbol1, ['Bicral<Gt(U3Betageo)1Ruiz>'])

    def testAlleleNomenclatureNoteSearch(self):
        """
        @Status tests that a basic allele Nomenclature Note search
        @see pwi-allele-search-29
        """
        driver = self.driver
        # Find and click the Nomenclature button
        driver.find_element(By.ID, "hideShowNomenNoteButton").click()
        # finds the Allele Nomenclature Note and enters a text string, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "nomenNote").send_keys('%parental ES cell line%')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Bicral<Gt(U3Betageo)1Ruiz>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the first result of over 20
        self.assertEqual(symbol1, ['Bicral<Gt(U3Betageo)1Ruiz>'])

    def testAlleleInducibleNoteSearch(self):
        """
        @Status tests that a basic allele Inducible Note search
        @see pwi-allele-search-30
        """
        driver = self.driver
        # Find and click the Inducible button
        driver.find_element(By.ID, "hideShowInducibleNoteButton").click()
        # finds the Allele Inducible Note and enters a text string, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "inducibleNote").send_keys('tamoxifen')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Gt(ROSA)26Sor<tm1(cre/Esr1)Tkp>-deleted'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the first result of over 1000
        self.assertEqual(symbol1, ['Col1a1<tm1.1(CAG-cre/ERT2)Dgk>'])

    def testAlleleUserCreNoteSearch(self):
        """
        @Status tests that a basic allele User(CRE) Note search
        @see pwi-allele-search-31
        """
        driver = self.driver
        # Find and click the User(CRE) button
        driver.find_element(By.ID, "hideShowCreNoteButton").click()
        # finds the Allele User(CRE) Note and enters a text string, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "creNote").send_keys('%donating investigator%')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Cartpt<tm1.1(cre)Hze>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the first result of over 3
        self.assertEqual(symbol1, ['Cartpt<tm1.1(cre)Hze>'])

    def testAlleleIKMCNoteSearch(self):
        """
        @Status tests that a basic allele IKMC Colony Note search
        @see pwi-allele-search-32
        """
        driver = self.driver
        # Find and click the IKMC Colony button
        driver.find_element(By.ID, "hideShowIkmcNoteButton").click()
        # finds the Allele IKMC Allele Colony Note and enters a text string, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "ikmcNote").send_keys('CR10557')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Cartpt<em1(IMPC)Mbp>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the first result
        self.assertEqual(symbol1, ['Cartpt<em1(IMPC)Mbp>'])

    def testAlleleProIDNoteSearch(self):
        """
        @Status tests that a basic allele Pro ID Note search
        @see pwi-allele-search-33
        """
        driver = self.driver
        # Find and click the Associated PRO IDs button
        driver.find_element(By.ID, "hideShowProidNoteButton").click()
        # finds the Allele Associated PRO IDs Note and enters a text string, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "proidNote").send_keys('KBL_Adrb3_01')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Adrb3<em1(IMPC)Krb>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Adrb3<em1(IMPC)Krb>'])

    def testAlleleOtherKompSearch(self):
        """
        @Status tests that an other ACC IDs KOMP Regeneron project search works
        @see pwi-allele-search-35
        """
        driver = self.driver
        # finds the Other ACC IDs pulldown and select the option 'KOMP regeneron project'value=string:125, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "logicaldb-0")).select_by_value('string:125')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # finds the other ACC IDs field IDs and enters an ID, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "otherAcc-0").send_keys('VG19166')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Mb<tm1(KOMP)Vlcg>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Mb<tm1(KOMP)Vlcg>'])

    def testAlleleOtherKompCSDSearch(self):
        """
        @Status tests that an other ACC IDs KOMP CSD project search works
        @see pwi-allele-search-36
        """
        driver = self.driver
        # finds the Other ACC IDs pulldown and select the option 'KOMP CSD project'value=string:126, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "logicaldb-0")).select_by_value('string:126')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # finds the other ACC IDs field IDs and enters an ID, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "otherAcc-0").send_keys('76581')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Auh<tm1a(KOMP)Wtsi>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        symbol2 = iterate.getTextAsList(cell2)
        print(symbol2)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Auh<tm1a(KOMP)Wtsi>'])
        self.assertEqual(symbol2, ['Auh<tm1e(KOMP)Wtsi>'])

    def testAlleleOtherNorcommSearch(self):
        """
        @Status tests that an other ACC IDs NorCOMM project search works
        @see pwi-allele-search-37
        """
        driver = self.driver
        # finds the Other ACC IDs pulldown and select the option 'NorCOMM project'value=string:143, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "logicaldb-0")).select_by_value('string:143')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # finds the other ACC IDs field IDs and enters an ID, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "otherAcc-0").send_keys('71054')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Ace2<tm1(NCOM)Mfgc>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Ace2<tm1(NCOM)Mfgc>'])

    def testAlleleOtherEucommSearch(self):
        """
        @Status tests that an other ACC IDs EUCOMM project search works
        @see pwi-allele-search-38
        """
        driver = self.driver
        # finds the Other ACC IDs pulldown and select the option 'EUCOMM project'value=string:138, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "logicaldb-0")).select_by_value('string:138')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # finds the other ACC IDs field IDs and enters an ID, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "otherAcc-0").send_keys('EUCOMMToolsCre_36168')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Gng7<tm1(EGFP/cre/ERT2)Wtsi>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Gng7<tm1(EGFP/cre/ERT2)Wtsi>'])

    def testAlleleOtherGenentechSearch(self):
        """
        @Status tests that an other ACC IDs EUCOMM project search works
        @see pwi-allele-search-39
        """
        driver = self.driver
        # finds the Other ACC IDs pulldown and select the option 'Genentech'value=string:162, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "logicaldb-0")).select_by_value('string:162')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # finds the other ACC IDs field IDs and enters an ID, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "otherAcc-0").send_keys('36818')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Gng7<tm1(EGFP/cre/ERT2)Wtsi>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Gng7<tm1(EGFP/cre/ERT2)Wtsi>'])

    def testAlleleOtherMirkoSearch(self):
        """
        @Status tests that an other ACC IDs mirKO project search works
        @see pwi-allele-search-40
        """
        driver = self.driver
        # finds the Other ACC IDs pulldown and select the option 'mirKO Project'value=string:166, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "logicaldb-0")).select_by_value('string:166')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # finds the other ACC IDs field IDs and enters an ID, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "otherAcc-0").send_keys('mirKO20845')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Mir700<tm1Wtsi>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Mir700<tm1Wtsi>'])

    def testAlleleMrkJnumValidSearch(self):
        """
        @Status tests that a basic allele marker symbol J number Validation works. If enter incorrect J number should get a popup message
        @see pwi-allele-search-41
        """
        driver = self.driver
        # finds the Marker J number field and enters a J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "markerjnumID-0").send_keys('00000')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # switch to alert
        alert = self.driver.switch_to.alert
        # get the text from the alert
        alert_text = alert.text
        print(alert_text)
        alert.accept()
        # check alert text
        self.assertEqual('Invalid Reference: 00000', alert_text)

    def testAlleleJnumValidSearch(self):
        """
        @Status tests that a basic allele  J number Validation works. If enter incorrect J number should get a popup message
        @see pwi-allele-search-42
        """
        driver = self.driver
        # finds the Allele J number field and enters a J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "refjnumID-0").send_keys('00000')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # switch to alert
        alert = self.driver.switch_to.alert
        # get the text from the alert
        alert_text = alert.text
        print(alert_text)
        alert.accept()
        # check alert text
        self.assertEqual('Invalid Reference: 00000', alert_text)

    def testAlleleMutantcellineValidSearch(self):
        """
        @Status tests that a basic allele Mutant Cell Line Validation works. If enter incorrect should get a popup message
        @see pwi-allele-search-43
        """
        driver = self.driver
        # finds the Allele J number field and enters a J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "mutantCellLine-0").send_keys('test')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # switch to alert
        alert = self.driver.switch_to.alert
        # get the text from the alert
        alert_text = alert.text
        print(alert_text)
        alert.accept()
        # check alert text
        self.assertEqual(alert_text, 'Invalid Mutant Cell Line: test')

    def testAlleleParentcellineValidSearch(self):
        """
        @Status tests that a basic allele Parent Cell Line Validation works. If enter incorrect should get a popup message
        @see pwi-allele-search-44
        """
        driver = self.driver
        # finds the Allele J number field and enters a J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "parentCellLine").send_keys('test')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # switch to alert
        alert = self.driver.switch_to.alert
        # get the text from the alert
        alert_text = alert.text
        print(alert_text)
        alert.accept()
        # check alert text
        self.assertEqual('Invalid Parent Cell Line: test', alert_text)

    def testAlleleSynonymSearch1(self):
        """
        @Status tests that a basic allele Synonym search
        @see pwi-allele-search-45
        """
        driver = self.driver
        # finds the Allele Synonym field and enters a text string, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "synonymName-0").send_keys('NKD')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Atf2<Tg(Gzma-Klra1)7Wum>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Atf2<Tg(Gzma-Klra1)7Wum>'])

    def testAlleleSynonymSearch2(self):
        """
        @Status tests that a basic allele Synonym search
        @see pwi-allele-search-45
        """
        driver = self.driver
        # finds the Allele Synonym field and enters a text string, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "synonymName-0").send_keys('ATF3-KO')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Atf3<tm1Dron>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Atf3<tm1Dron>'])

    def testAlleleAttribEndoSearch(self):
        """
        @Status tests that an Attribute by Endonuclease search works
        @see pwi-allele-search-46
        """
        driver = self.driver
        # finds the Allele Synonym field and enters a text string, tabs out of the field
        driver.find_element(By.ID, "synonymName-0").send_keys('H11<Cas9>')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # finds the Attribute pulldown and select the option 'Endonuclease'value=string:38853195, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "subtype-0")).select_by_value('string:38853195')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(3)
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Igs2<tm1.1(CAG-cas9*)Mmw>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Igs2<tm1.1(CAG-cas9*)Mmw>'])
        # verify the correct option for attribute is selected
        select = Select(driver.find_element(By.ID, 'subtype-0'))
        selected_option = select.first_selected_option
        print(selected_option.text)
        self.assertEqual(selected_option.text, 'Endonuclease')

    def testAlleleAttribTransposaseSearch(self):
        """
        @Status tests that an Attribute by Transposase search works
        @see pwi-allele-search-46
        """
        driver = self.driver
        # finds the Attribute pulldown and select the option 'Transposase'value=string:11025590, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "subtype-0")).select_by_value('string:11025590')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Tg(Prm-sb10)2Tcb'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Tg(Prm-sb10)2Tcb'])
        # verify the correct option for attribute is selected
        select = Select(driver.find_element(By.ID, 'subtype-0'))
        selected_option = select.first_selected_option
        print(selected_option.text)
        self.assertEqual(selected_option.text, 'Transposase')

    def testAlleleMolecularMutNucleotideSearch(self):
        """
        @Status tests that a Molecular Mutations of Nucleotide repeat expansion search works
        @see pwi-allele-search-47 Broken!!!! needs to be fixed
        """
        driver = self.driver
        # finds the Allele Synonym field and enters a text string, tabs out of the field
        driver.find_element(By.ID, "synonymName-0").send_keys('CGG(98)')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # finds the Allele Synonym J number field and enters the correct J number, tabs out of the field
        driver.find_element(By.ID, "synjnumID-0").send_keys('71202')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        # finds the Molecular Mutations pulldown and select the option 'Nucleotide repeat expansion'value=string:847100, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "mutation-0")).select_by_value('string:847100')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        # waits until the element is located or 10 seconds
        #WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Fmr1<tm2Cgr>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Fmr1<tm2Cgr>'])
        # verify the correct option for molecular mutation is selected
        select = Select(driver.find_element(By.ID, 'mutation-0'))
        selected_option = select.first_selected_option
        print(selected_option.text)
        self.assertEqual(selected_option.text, 'Nucleotide repeat expansion')

    def testAlleleMolecularMutViralinsertionSearch(self):
        """
        @Status tests that a Molecular Mutations of Viral insertion search works
        @see pwi-allele-search-47
        """
        driver = self.driver
        # finds the Molecular Mutations pulldown and select the option 'Viral insertion'value=string:847108, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "mutation-0")).select_by_value('string:847108')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Afg3l2<Emv66>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(2)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Afg3l2<Emv66>'])
        # verify the correct option for molecular mutation is selected
        select = Select(driver.find_element(By.ID, 'mutation-0'))
        selected_option = select.first_selected_option
        print(selected_option.text)
        self.assertEqual(selected_option.text, 'Viral insertion')

    def testAlleleDrivergeneBaboonSearch(self):
        """
        @Status tests that a Driver gene of baboon, olive search works
        @see pwi-allele-search-48
        """
        driver = self.driver
        # finds the Driver gene pulldown and select the option 'baboon, olive'value=string:125, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "organism")).select_by_value('string:125')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Tg(CMA1-cre)6Thhe'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the only result
        self.assertEqual(symbol1, ['Tg(CMA1-cre)6Thhe'])
        # verify the correct option  for driver gene is selected
        select = Select(driver.find_element(By.ID, 'organism'))
        selected_option = select.first_selected_option
        print(selected_option.text)
        self.assertEqual(selected_option.text, 'baboon, olive')

    def testAlleleDrivergeneSheepSearch(self):
        """
        @Status tests that a Driver gene of Sheep search works
        @see pwi-allele-search-48
        """
        driver = self.driver
        # finds the Driver gene pulldown and select the option 'sheep'value=string:44, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "organism")).select_by_value('string:44')
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Tg(FSHB-icre)#Kmar'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct allele symbol is returned, this is the first of only 2 results
        self.assertEqual(symbol1, ['Tg(FSHB-icre)#Kmar'])
        # verify the correct option  for driver gene is selected
        select = Select(driver.find_element(By.ID, 'organism'))
        selected_option = select.first_selected_option
        print(selected_option.text)
        self.assertEqual(selected_option.text, 'sheep')

    def testAlleleCreateBySearch(self):
        """
        @Status tests that an allele search using the Created By field returns correct data
        @see pwi-allele-date-search-1
        """
        driver = self.driver
        # find the alleles Created By field and enter the name
        driver.find_element(By.ID, "createdBy").send_keys("hdene")
        # find the alleles Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("2008-12-15")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Smad4<tm2Rob>'))
        # find the Created by field
        create_by = driver.find_element(By.ID, 'createdBy').get_attribute('value')
        print(create_by)
        # Assert the  Created By field returned is correct
        self.assertEqual(create_by, 'hdene')
        # find the Creation Date field
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        # Assert the  Creation Date field returned is correct
        self.assertEqual(create_date, '2008-12-15')

    def testAlleleModBySearch(self):
        """
        @Status tests that an allele search using the Modified By field returns correct data
        @see pwi-allele-date-search-2
        """
        driver = self.driver
        # find the alleles Modified by field and enter the name
        driver.find_element(By.ID, "modifiedBy").send_keys("monikat")
        # find the alleles Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("2018-12-19")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Ucp1<m1Ntam>'))
        # find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        # Assert the  Modified By field returned is correct
        self.assertEqual(mod_by, 'monikat')
        # find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        # Assert the Modification Date field returned is correct
        self.assertEqual(mod_date, '2018-12-19')

    def testAlleleCreateDateSearch(self):
        """
        @Status tests that an allele search using the Creation Date field returns correct data
        @see pwi-allele-date-search-3
        """
        driver = self.driver
        # find the alleles Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("2003-11-26")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Cnga4<tm1Reed>'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        # Assert the  Creation Date field returned is correct
        self.assertEqual(create_date, '2003-11-26')

    def testAlleleModDateSearch(self):
        """
        @Status tests that an allele search using the Modified By field returns correct data
        @see pwi-allele-date-search-4
        """
        driver = self.driver
        # find the alleles Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("2004-11-17")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Lhfpl1<+>'))
        # find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        # Assert the Modification Date field returned is correct
        self.assertEqual(mod_date, '2004-11-17')

    def testAlleleModDateLessSearch(self):
        """
        @Status tests that an allele search using the Modified By field and less than returns correct data
        @see pwi-allele-date-search-7
        """
        driver = self.driver
        # find the alleles Modified by field and enter the name
        driver.find_element(By.ID, "modifiedBy").send_keys("rjc")
        # find the alleles Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("<2003-01-28")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Grm1<+>'))
        # find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        # Assert the  Modified By field returned is correct
        self.assertEqual(mod_by, 'rjc')
        # find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        # Assert the Modification Date field returned is correct
        self.assertEqual(mod_date, '2003-01-24')

    def testAlleleModDateLessEqualSearch(self):
        """
        @Status tests that an allele search using the Modified By field and less than or equal to returns correct data
        @see pwi-allele-date-search-8
        """
        driver = self.driver
        # find the alleles Modified by field and enter the name
        driver.find_element(By.ID, "modifiedBy").send_keys("rjc")
        # find the alleles Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("<=2003-01-28")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Grm1<+>'))
        # find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        # Assert the  Modified By field returned is correct
        self.assertEqual(mod_by, 'rjc')
        # find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        # Assert the Modification Date field returned is correct
        self.assertEqual(mod_date, '2003-01-24')

    def testAlleleModDateBetweenSearch(self):
        """
        @Status tests that an allele search using the Modified By field and between dates returns correct data
        @see pwi-allele-date-search-9
        """
        driver = self.driver
        # find the alleles Modified by field and enter the name
        driver.find_element(By.ID, "modifiedBy").send_keys("rjc")
        # find the alleles Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("2003-01-24..2003-01-28")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Grm1<+>'))
        # find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        # Assert the  Modified By field returned is correct
        self.assertEqual(mod_by, 'rjc')
        # find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        # Assert the Modification Date field returned is correct
        self.assertEqual(mod_date, '2003-01-24')

    def testAlleleCreateDateLessSearch(self):
        """
        @Status tests that an allele search using the Creation Date field and Less than returns correct data
        @see pwi-allele-date-search-12
        """
        driver = self.driver
        # find the alleles Created by field and enter the name
        driver.find_element(By.ID, "createdBy").send_keys("rjc")
        # find the alleles Modification Date field and enter a date
        # find the alleles Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("<2004-02-03")
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'H2-M11<+>'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        # Assert the  Creation Date field returned is correct
        self.assertEqual(create_date, '2004-02-02')

    def testAlleleCreateDateLessEqualSearch(self):
        """
        @Status tests that an allele search using the Creation Date field and Less than, equals to returns correct data
        @see pwi-allele-date-search-13
        """
        driver = self.driver
        # find the alleles Created by field and enter the name
        driver.find_element(By.ID, "createdBy").send_keys("rjc")
        time.sleep(2)
        # find the alleles Modification Date field and enter a date
        # find the alleles Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("<=2004-02-03")
        time.sleep(2)
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        time.sleep(2)
        #WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'H2-M11<+>'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        # Assert the  Creation Date field returned is correct
        self.assertEqual(create_date, '2004-02-03')

    def testAlleleCreateDateBetweenSearch(self):
        """
        @Status tests that an allele search using the Creation Date field and Between dates returns correct data
        @see pwi-allele-date-search-14
        """
        driver = self.driver
        # find the alleles Created by field and enter the name
        driver.find_element(By.ID, "createdBy").send_keys("rjc")
        time.sleep(2)
        # find the alleles Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("2004-01-28..2004-02-03")
        time.sleep(2)
        # find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        # waits until the element is located or 10 seconds
        time.sleep(2)
        #WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'H2-M10.6<+>'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        # Assert the  Creation Date field returned is correct
        self.assertEqual(create_date, '2004-02-03')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEIAlleleSearch))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))