'''
Created on Mar 17, 2022

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
class TestEIAlleleRelationshipsSearch(unittest.TestCase):
    """
    @status Test Allele Relationships searching, etc
    """

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/allelefear/")

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

    def testEIAlleleRelationshipsMGI_IDSearch(self):
        """
        @Status tests that a basic MGI ID search works
        @see pwi-allele-rel-search-1
        """
        driver = self.driver
        # finds the Allele Relationships MGI ID field and enter the ID, tabs out of the field then clicks the Search button
        self.driver.find_element(By.ID, "alleleAccID").send_keys('MGI:6430734')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Gpc5<C57BL/6J>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct antigen is returned
        self.assertEqual(result1, ['Gpc5<C57BL/6J>'])

    def testEIAlleleRelationshipsAlleleSymbolSearch(self):
        """
        @Status tests that a basic allele relationship Allele symbol search works
        @see pwi-allele-rel-search-2
        """
        driver = self.driver
        # finds the Allele Relationship Allele field and enters an allele symbol, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "alleleSymbol").send_keys('Gpc5<DBA/2J>')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Gpc5<DBA/2J>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct relationship is returned
        self.assertEqual(result1, ['Gpc5<DBA/2J>'])

    def testEIAlleleRelationshipsAlleleSymbolwildSearch(self):
        """
        @Status tests that a basic allele symbol using wilcard search works
        @see pwi-allele-rel-search-2
        """
        driver = self.driver
        # finds the allele symbol field and enters a partial symbol with wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "alleleSymbol").send_keys('Gpc5%')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Gpc5<DBA/2J>'))
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
        self.assertEqual(result1, ['Gpc5<C57BL/6J>'])
        self.assertEqual(result2, ['Gpc5<DBA/2J>'])
        self.assertEqual(result3, ['Gpc5<em1Gpt>'])
        self.assertEqual(result4, ['Gpc5<em1Smoc>'])
        self.assertEqual(result5, ['Gpc5<Gt(IST13574F4)Tigm>'])
        self.assertEqual(result6, ['Gpc5<tm1.1Mrl>'])

    def testEIAlleleRelationshipsMITypeSearch(self):
        """
        @Status tests that a basic allele relationships mutation involved type search works with wildcard
        @see pwi-allele-rel-search-3
        """
        driver = self.driver
        # finds the Relationship Type field and select option normal(string:12438362), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "MIrelationshipTerm-0")).select_by_value('string:12438362')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Gpc5<DBA/2J>'))
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
        self.assertEqual(result1, ['Gpc5<C57BL/6J>'])
        self.assertEqual(result2, ['Gpc5<DBA/2J>'])
        self.assertEqual(result3, ['Grm7<rs3723352-G>'])

    def testEIAlleleRelationshipsMIJnumSearch(self):
        """
        @Status tests that a basic allele relationships Mutation Involves J# search works
        @see pwi-allele-rel-search-4
        """
        driver = self.driver
        # finds the mutation involves J number field and enter the J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "MIjnumID-0").send_keys('J:257336')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Dp(13Spock1)1Tac'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct relationships is returned
        self.assertEqual(result1, ['Dp(13Spock1)1Tac'])

    def testEIAlleleRelationshipMImrkAccIDSearch(self):
        """
        @Status tests that a basic allele relationships mutation involves marker Acc ID search works
        @see pwi-allele-rel-search-5
        """
        driver = self.driver
        # finds the mutation involves marker acc ID field and enters an MGI ID, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "MImarkerAccID-0").send_keys('MGI:96677')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'In(5)30Rk'))
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
        # Assert the correct relationshipss are returned(first 5)
        self.assertEqual(result1, ['Del(5Kit-Cep135)1Utr'])
        self.assertEqual(result2, ['In(5)30Rk'])
        self.assertEqual(result3, ['In(5)33Rk'])
        self.assertEqual(result4, ['In(5)9Rk'])
        self.assertEqual(result5, ['Kit<W-19H>'])

    def testEIAlleleRelationshipsMIMrkSearch(self):
        """
        @Status tests that a basic allele relationships mutation involves marker search works
        @see pwi-allele-rel-search-6
        """
        driver = self.driver
        # finds the muation involves marker field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "MImarkerSymbol-0").send_keys('Clock')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'In(5)30Rk'))
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
        # Assert the correct relationships are returned(first 5)
        self.assertEqual(result1, ['Del(5Kit-Cep135)1Utr'])
        self.assertEqual(result2, ['Del(5Kit-Nmu)2Utr'])
        self.assertEqual(result3, ['In(5)30Rk'])
        self.assertEqual(result4, ['In(5)33Rk'])
        self.assertEqual(result5, ['In(5)9Rk'])

    def testEIAlleleRelationshipsMINoteSearch(self):
        """
        @Status tests that a basic allele relationships Mutated Involves note search  works
        @see pwi-allele-der-search-7
        """
        driver = self.driver
        # finds the mutated involves note field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "MInote-0").send_keys('translocation or duplication of exon 1')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Tg(SNCA*A53T)2Nbm'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct relationships are returned
        self.assertEqual(result1, ['Tg(SNCA*A53T)2Nbm'])

    def testEIAlleleRelationshipsECTypeSearch(self):
        """
        @Status tests that a basic allele relationships expresses component type search works
        @see pwi-allele-rel-search-8
        """
        driver = self.driver
        # finds the Expresses component Relationship Type field and select option mouse(string:1), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "ECorganism-0")).select_by_value('string:1')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Actb<tm3.1(Sirt1)Npa>'))
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
        self.assertEqual(result1, ['2500002B13Rik<tm1(CAG-2500002B13Rik)Yo>'])
        self.assertEqual(result2, ['Actb<tm3.1(Sirt1)Npa>'])
        self.assertEqual(result3, ['Actb<tm3(Kras*)Arge>'])

    def testEIAlleleRelationshipsECJnumSearch(self):
        """
        @Status tests that a basic allele relationships Expresses Component J# search works
        @see pwi-allele-rel-search-9
        """
        driver = self.driver
        # finds the expresses component J number field and enter the J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "ECjnumID-0").send_keys('J:246645')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Sox3<em1(Sox2)Pqt>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct relationships is returned
        self.assertEqual(result1, ['Sox3<em1(Sox2)Pqt>'])

    def testEIAlleleRelationshipECmrkAccIDSearch(self):
        """
        @Status tests that a basic allele relationships expresses component marker Acc ID search works
        @see pwi-allele-rel-search-10
        """
        driver = self.driver
        # finds the expresses component marker acc ID field and enters an MGI ID, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "ECmarkerAccID-0").send_keys('MGI:96163')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Ak7<Tg(tetO-Hmox1)67Sami>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct relationshipss are returned
        self.assertEqual(result1, ['Ak7<Tg(tetO-Hmox1)67Sami>'])

    def testEIAlleleRelationshipsECMrkSearch(self):
        """
        @Status tests that a basic allele relationships expresses component marker search works
        @see pwi-allele-rel-search-11
        """
        driver = self.driver
        # finds the expresses component marker field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "ECmarkerSymbol-0").send_keys('Gata2')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Gt(ROSA)26Sor<tm10(Gata2)Jhai>'))
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
        self.assertEqual(result1, ['Gata2<tm2(Gata2)Jeng>'])
        self.assertEqual(result2, ['Gt(ROSA)26Sor<tm10(Gata2)Jhai>'])

    def testEIAlleleRelationshipsECNoteSearch(self):
        """
        @Status tests that a basic allele relationships expresses component note search  works
        @see pwi-allele-der-search-12
        """
        driver = self.driver
        # finds the mutated involves note field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "ECnote-0").send_keys('HBEGF/GFP fusion')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Aire<tm5.1(HBEGF/GFP)Mmat>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct relationships are returned
        self.assertEqual(result1, ['Aire<tm5.1(HBEGF/GFP)Mmat>'])

    def testEIAlleleRelationshipsOrganismSearch(self):
        """
        @Status tests that a basic allele relationships Driver Component Organism Pick List search  works
        @see pwi-allele-der-search-13
        """
        driver = self.driver
        # finds the Driver Component Organism pick list field and select  the option zebrafish('string:84') , then click the Search button
        Select(driver.find_element(By.ID, "DCorganism-0")).select_by_value('string:84')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Tg(dlx5a-cre)1Mekk'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct relationships are returned
        self.assertEqual(result1, ['Tg(dlx5a-cre)1Mekk'])

    """def testEIAlleleRelationshipsPropertySearch(self):
        
        @Status tests that a basic allele relationships property search  works
        @see pwi-allele-der-search-14!!!!! (this test is no longer valid. All tests need review to fix the changes made for this form)
        
        driver = self.driver
        # finds the Property list field and select the option Non-mouse_organism , set value to zebrafish and then click the Search button
        Select(driver.find_element(By.ID, "propertyName-0")).select_by_value('string:12948290')
        driver.find_element(By.ID, "value-0").send_keys("zebrafish")
        time.sleep(2)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        print(result1)
        # Assert the correct relationships are returned
        self.assertEqual(result1, ['Mesp2<tm7.1(mespb)Ysa>'])
        self.assertEqual(result2, ['Mesp2<tm7(mespb)Ysa>'])
        self.assertEqual(result3, ['Tg(MMTV-Catnb)3Pac'])
        self.assertEqual(result4, ['Tg(MMTV-Catnb)5Pac'])"""

    def testEIAlleleRelationshipsMrkRegionToolSearch(self):
        """
        @Status tests that a basic allele relationships Marker Region Tool search  works
        @see pwi-allele-der-search-15
        """
        driver = self.driver
        # finds the Allele field and enters text, the Chr,start coordinate, stop coordinate and lastly Relationship Type fields to enter data. tabs out of the fields then clicks the Search button
        driver.find_element(By.ID, "alleleSymbol").send_keys('Qki<qk-v>')
        Select(driver.find_element(By.ID, "chromsome")).select_by_value('string:17')
        driver.find_element(By.ID, "startCoordinate").send_keys('10425400')
        driver.find_element(By.ID, "endCoordinate").send_keys('12282248')
        Select(driver.find_element(By.ID, "relationshipTerm")).select_by_value('string:12438350')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Qki<qk-v>'))
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        # Assert the correct relationships are returned
        self.assertEqual(result1, ['Qki<qk-v>'])


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEIAlleleRelationshipsSearch))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))