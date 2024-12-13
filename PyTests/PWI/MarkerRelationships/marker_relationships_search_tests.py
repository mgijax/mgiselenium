'''
Created on Oct 9, 2024

@author: jeffc
'''
import unittest
import time
import tracemalloc
import json
import config
import sys, os.path

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from test.test_base64 import BaseXYTestCase
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests
tracemalloc.start()


class TestEIMarkerRelationshipsSearch(unittest.TestCase):
    """
    @status Test Marker Relationships searching, etc
    """

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/markerfear/")

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

    def testEIMarkerRelationshipsMGI_IDSearch(self):
        """
        @Status tests that a basic MGI ID search works
        @see pwi-marker-rel-search-1 passed 10/11/2024
        """
        driver = self.driver
        # finds the Marker Relationships MGI ID field and enter the ID, tabs out of the field then clicks the Search button
        self.driver.find_element(By.ID, "markerAccID").send_keys('MGI:5905757')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Ces1'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct antigen is returned
        self.assertEqual(result1, ['Ces1'])

    def testEIMarkerRelationshipsMarkerSymbolSearch(self):
        """
        @Status tests that a basic marker relationship Marker symbol search works
        @see pwi-marker-rel-search-2 passed 10/11/2024
        """
        driver = self.driver
        # finds the Marker Relationship Marker field and enters a marker symbol, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys('Mirc1')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Mirc1'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct relationship is returned
        self.assertEqual(result1, ['Mirc1'])

    def testEIMarkerRelationshipsMarkerSymbolWildSearch(self):
        """
        @Status tests that a basic marker symbol using wildcard search works
        @see pwi-marker-rel-search-2 passed 10/11/2024
        """
        driver = self.driver
        # finds the marker symbol field and enters a partial symbol with wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys('Mirc%')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Mirc10'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
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
        # Assert the correct relationships are returned
        self.assertEqual(result1, ['Mirc1'])
        self.assertEqual(result2, ['Mirc10'])
        self.assertEqual(result3, ['Mirc11'])
        self.assertEqual(result4, ['Mirc12'])
        self.assertEqual(result5, ['Mirc13'])
        self.assertEqual(result6, ['Mirc14'])

    def testEIMarkerRelationshipsTypeSearch(self):
        """
        @Status tests that a basic marker relationships type search works
        @see pwi-marker-rel-search-3 passed 10/11/2024
        """
        driver = self.driver
        # finds the Relationship Type field and select option cluster_has_member(string:12438344), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "CMrelationshipTerm-0")).select_by_value('string:12438344')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Cyp2j'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        print(result1)
        # Assert the correct relationships are returned
        self.assertEqual(result1, ['Ces1'])
        self.assertEqual(result2, ['Cyp2j'])
        self.assertEqual(result3, ['Mirc1'])

    def testEIMarkerRelationshipsCMJnumSearch(self):
        """
        @Status tests that a basic marker relationships cluster has member J# search works
        @see pwi-marker-rel-search-4 passed on 10/11/2024
        """
        driver = self.driver
        # finds the cluster has member J number field and enter the J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "CMjnumID-0").send_keys('J:229199')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Rhox'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct relationships are returned
        self.assertEqual(result1, ['Rhox'])


    def testEIMarkerRelationshipCMmrkAccIDSearch(self):
        """
        @Status tests that a basic marker relationships cluster has member marker Acc ID search works
        @see pwi-marker-rel-search-5 passed 10/11/2024
        """
        driver = self.driver
        # finds the mutation involves marker acc ID field and enters an MGI ID, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "CMmarkerAccID2-0").send_keys('MGI:3580237')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Rhox'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct relationshipss are returned(first 5)
        self.assertEqual(result1, ['Rhox'])


    def testEIMarkerRelationshipsCMMrkSearch(self):
        """
        @Status tests that a basic marker relationships cluster has member marker search works
        @see pwi-marker-rel-search-6 passed 10/11/2024
        """
        driver = self.driver
        # finds the muation involves marker field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "CMmarkerSymbol2-0").send_keys('Ly6a')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Ly6'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct relationships are returned(first 5)
        self.assertEqual(result1, ['Ly6'])


    def testEIMarkerRelationshipsCMNoteSearch(self):
        """
        @Status tests that a basic marker relationships cluster has member note search  works
        @see pwi-marker-rel-search-7 passed 10/11/2024
        """
        driver = self.driver
        # finds the mutated involves note field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "CMnote-0").send_keys('strain specific marker')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Hbb'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct relationships are returned
        self.assertEqual(result1, ['Hbb'])

    def testEIMarkerRelationshipsCMModifySearch(self):
        """
        @Status tests that a basic marker relationships cluster has member modify search  works
        @see pwi-marker-rel-search-? passed 10/11/2024
        """
        driver = self.driver
        # finds the mutated involves note field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "CMmodifiedBy-0").send_keys('mmh')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Mirc40'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        print(result1)
        # Assert the correct relationships are returned
        self.assertEqual(result1, ['Mirc37'])
        self.assertEqual(result2, ['Mirc38'])
        self.assertEqual(result3, ['Mirc39'])
        self.assertEqual(result4, ['Mirc40'])
        self.assertEqual(result5, ['Mirc41'])

    def testEIMarkerRelationshipsCMModifyDateSearch(self):
        """
        @Status tests that a basic marker relationships cluster has member modify date search  works
        @see pwi-marker-rel-search-? passed 10/11/2024
        """
        driver = self.driver
        # finds the mutated involves note field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "CMmodifiedDate-0").send_keys('2015-09-12')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Mirc40'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        print(result1)
        # Assert the correct relationships are returned
        self.assertEqual(result1, ['Mirc39'])
        self.assertEqual(result2, ['Mirc40'])
        self.assertEqual(result3, ['Mirc41'])
        self.assertEqual(result4, ['Mirc42'])
        self.assertEqual(result5, ['Mirc43'])

    def testEIMarkerRelationshipsREJnumSearch(self):
        """
        @Status tests that a basic marker relationships regulates expression J number search works
        @see pwi-marker-rel-search-8 passed 10/10/2024
        """
        driver = self.driver
        # finds the Expresses component Relationship Type field and select option mouse(string:1), tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "REjnumID-0").send_keys('J:320178')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Rr93'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        print(result1)
        # Assert the correct relationships are returned
        self.assertEqual(result1, ['Rr113'])
        self.assertEqual(result2, ['Rr114'])
        self.assertEqual(result3, ['Rr93'])

    def testEIMarkerRelationshipsREAccIDSearch(self):
        """
        @Status tests that a basic marker relationships regulates expression marker acc ID search works
        @see pwi-marker-rel-search-9 passed 10/10/2024
        """
        driver = self.driver
        # finds the expresses component J number field and enter the J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "REmarkerAccID2-0").send_keys('MGI:98297')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Rr120'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        print(result1)
        # Assert the correct relationships is returned
        self.assertEqual(result1, ['Rr113'])
        self.assertEqual(result2, ['Rr114'])
        self.assertEqual(result3, ['Rr115'])

    def testEIMarkerRelationshipREMarkerSearch(self):
        """
        @Status tests that a basic marker relationships regulates expression marker search works
        @see pwi-marker-rel-search-10 passed 10/10/2024
        """
        driver = self.driver
        # finds the expresses component marker acc ID field and enters an MGI ID, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "REmarkerSymbol2-0").send_keys('Shh')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Rr121'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct relationshipss are returned
        self.assertEqual(result1, ['Rr113'])

    def testEIMarkerRelationshipRENoteSearch(self):
        """
        @Status tests that a basic marker relationships regulates expression note search works
        @see pwi-marker-rel-search-11 passed 10/10/2024
        """
        driver = self.driver
        # finds the expresses component marker field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "REnote-0").send_keys('super-enhancer')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Rr547'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        print(result1)
        # Assert the correct relationships are returned(first 5)
        self.assertEqual(result1, ['Rr147456'])
        self.assertEqual(result2, ['Rr547'])

    def testEIMarkerRelationshipsREModifySearch(self):
        """
        @Status tests that a basic marker relationships regulates expression modify search  works
        @see pwi-marker-rel-search-? passed 10/11/2024
        """
        driver = self.driver
        # finds the mutated involves note field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "REmodifiedBy-0").send_keys('wilmil')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Rr110'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        print(result1)
        # Assert the correct relationships are returned
        self.assertEqual(result1, ['Rr100'])
        self.assertEqual(result2, ['Rr102'])
        self.assertEqual(result3, ['Rr103'])
        self.assertEqual(result4, ['Rr104'])
        self.assertEqual(result5, ['Rr105'])

    def testEIMarkerRelationshipsREModifyDateSearch(self):
        """
        @Status tests that a basic marker relationships regulates expression modify date search  works
        @see pwi-marker-rel-search-? passed 10/11/2024
        """
        driver = self.driver
        # finds the mutated involves note field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "REmodifiedDate-0").send_keys('2024-10-08')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Rr110'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        print(result1)
        # Assert the correct relationships are returned
        self.assertEqual(result1, ['Rr100'])
        self.assertEqual(result2, ['Rr102'])
        self.assertEqual(result3, ['Rr103'])
        self.assertEqual(result4, ['Rr104'])
        self.assertEqual(result5, ['Rr105'])

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEIMarkerRelationshipsSearch))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))