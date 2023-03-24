'''
Created on Jul 31, 2020
TESTS HAVE NOT YET BEEN REWRITTEN FOR ANTIBODIES MODULE!!!!!!!
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
from test.test_base64 import BaseXYTestCase
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests

class TestEIAntibodySearch(unittest.TestCase):
    """
    @status Test Antibody searching, etc
    """

    def setUp(self):
        self.driver = webdriver.Firefox() 
        #self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/antibody")
    
    def tearDown(self):
        self.driver.close()

    def testAntibodyNameSearch(self):
        """
        @Status tests that a basic antibody name search works
        @see pwi-antibody-search-1
        """
        driver = self.driver
        #finds the Antibody Name field and enters an antibody name, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antibodyName").send_keys('anti-uvomorulin ')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibody is returned
        self.assertEqual(symbol1, ['anti-uvomorulin'])

    def testAntibodyName2Search(self):
        """
        @Status tests that a basic antibody name w/wildcard search works
        @see pwi-antibody-search-1
        """
        driver = self.driver
        #finds the Antibody Name field and enters an antibody name w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antibodyName").send_keys('anti-Dkk%')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibody is returned
        self.assertEqual(symbol1, ['anti-Dkk-1'])

    def testAntibodyTypeSearch(self):
        """
        @Status tests that a basic antibody type search works
        @see pwi-antibody-search-2
        """
        driver = self.driver
        #finds the antibody type field and selects the option 'Monoclonal' (value=string:107367161), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "antibodyType")).select_by_value('string:107367161')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        symbol3 = iterate.getTextAsList(cell3)
        print(symbol1)
        #Assert the correct antibody is returned
        self.assertEqual(symbol1, ['11C7'])
        self.assertEqual(symbol2, ['121'])
        self.assertEqual(symbol3, ['12/21/1-C-6'])
        
    def testAntibodyClassSearch(self):
        """
        @Status tests that a basic Antibody class search works 
        @see pwi-antigen-search-3
        """
        driver = self.driver
        #finds the antibody class field and selects the option 'IgG2c' (value=string:107080512), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "antibodyClass")).select_by_value('string:107080512')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibody is returned
        self.assertEqual(symbol1, ['AIRE Monoclonal Antibody (5H12), eFluor 660'])
        
    def testAntibodyOrganismSearch(self):
        """
        @Status tests that a basic antibody organism search works 
        @see pwi-antigen-search-4
        """
        driver = self.driver
        #finds the antibody organism field and selects the option 'monkey' (value=string:72), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "antibodyOrganism")).select_by_value('string:72')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(5)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['anti-GH'])
        self.assertEqual(symbol2, ['Anti-GH'])
        
    def testAntigenAccIDSearch(self):
        """
        @Status tests that a basic antigen accession ID search works 
        @see pwi-antibody-search-5
        """
        driver = self.driver
        #finds the antigen accession ID field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antigenAcc").send_keys('MGI:2684475')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['Gli3ab1'])

    def testAntigenNameSearch(self):
        """
        @Status tests that a basic antigen name search works 
        @see pwi-antibody-search-6
        """
        driver = self.driver
        #finds the antigen name field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antigenName").send_keys('uvomorulin')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['anti-uvomorulin'])
 
    def testAntigenName2Search(self):
        """
        @Status tests that a basic antigen name with wildcard search works 
        @see pwi-antibody-search-6
        """
        driver = self.driver
        #finds the antigen name field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antigenName").send_keys('CDEBP%')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['Ab61']) 
        
    def testAntibodyRegionSearch(self):
        """
        @Status tests that a basic region covered search works
        @see pwi-antibody-search-7
        """
        driver = self.driver
        #finds the antibody region covered field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "regionCovered").send_keys('carboxyl-terminal domain ')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibody is returned
        self.assertEqual(symbol1, ['anti-GLUT1'])               
        
    def testAntibodyRegion2Search(self):
        """
        @Status tests that a basic region covered search with wildcard works
        @see pwi-antibody-search-7
        """
        driver = self.driver
        #finds the region covered field and enters text, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "regionCovered").send_keys('histidyl-tagged%')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibody is returned
        self.assertEqual(symbol1, ['ANTI-myosin VIIA'])
        
    def testAntigenNotesSearch(self):
        """
        @Status tests that a basic antigens notes works
        @see pwi-antibody-search-8
        """
        driver = self.driver
        #finds the antigen notes field and enters text, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antigenNote").send_keys('fused to GST')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['anti-ATF4'])
        self.assertEqual(symbol2, ['anti-mHSF1J'])    
        
    def testAntigenNotes2Search(self):
        """
        @Status tests that a basic antigens notes with wildcard works
        @see pwi-antibody-search-8
        """
        driver = self.driver
        #finds the antigen notes field and enters text, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antigenNote").send_keys('%describe%')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        symbol3 = iterate.getTextAsList(cell3)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['anti-c-ErbB2/c-Neu (ab-3)'])
        self.assertEqual(symbol2, ['anti-Dnmt antibody'])  
        self.assertEqual(symbol3, ['anti-Syk'])   

    def testAntigenOrganismSearch(self):
        """
        @Status tests that a basic antigen organism search works
        @see pwi-antibody-search-9
        """
        driver = self.driver
        #finds the organism(antigen) field and select the option 'Carp', tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "antigenOrganism")).select_by_value('string:62')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['parvalbumin antibody 235'])

    def testAntigenStrainSearch(self):
        """
        @Status tests that a basic antibody antigen strain search  works
        @see pwi-antibody-search-10
        """
        driver = self.driver
        #finds the antibody antigen strain field and enters text, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "strain").send_keys('BALB/c')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
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
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['12F11 antibody'])
        self.assertEqual(symbol2, ['2A7'])
        self.assertEqual(symbol3, ['346-11A'])
        self.assertEqual(symbol4, ['72B9'])
        self.assertEqual(symbol5, ['Anti-CD31 (ER-MP12; #MCA23388)'])

    def testAntigenStrain2Search(self):
        """
        @Status tests that a basic antibody antigen strain search with wildcard works
        @see pwi-antibody-search-10
        """
        driver = self.driver
        #finds the antibody antigen strain field and enters text, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "strain").send_keys('129')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['anti-CD34 (MEC 14.7; sc-18917)'])
        
    def testAntigenTissueSearch(self):
        """
        @Status tests that a basic tissue search works
        @see pwi-antibody-search-11
        """
        driver = self.driver
        #finds the tissue field and enters a tissue, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "tissue").send_keys('thymus')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        cell6 = table.get_row_cells(5)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        symbol3 = iterate.getTextAsList(cell3)
        symbol4 = iterate.getTextAsList(cell4)
        symbol5 = iterate.getTextAsList(cell5)
        symbol6 = iterate.getTextAsList(cell6)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['1D4'])
        self.assertEqual(symbol2, ['Anti-CD4 (RM4-5; 100548)'])
        self.assertEqual(symbol3, ['anti-PARP1 (556362)'])
        self.assertEqual(symbol4, ['anti-TdT serum'])
        self.assertEqual(symbol5, ['H202-407-6-3'])
        self.assertEqual(symbol6, ['HS9 antibody'])
        
    """def testAntigenTissue1Search(self):
        
        @Status tests that a basic tissue search w/wildcard works
        @see pwi-antibody-search-11 (no longer valid test as wildcard not used for Tissue field 2/16/2023)
        
        driver = self.driver
        #finds the tissue field and enters a tissue w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "tissue").send_keys('endo%')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(6)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['anti-CD34 (MEC 14.7; sc-18917)'])
        self.assertEqual(symbol2, ['EA-1'])    
        """
    def testAntigenTissueDescSearch(self):
        """
        @Status tests that a basic tissue description search works
        @see pwi-antibody-search-12
        """
        driver = self.driver
        #finds the tissue description field and enters a description, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "description").send_keys('mast cell')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibody is returned
        self.assertEqual(symbol1, ['PS-2'])
        
    """def testAntigenTissueDesc1Search(self):
        
        @Status tests that a basic tissue description search w/wildcard works
        @see pwi-antigen-search-12 (No longer a valid test as wildcards no longer work 2/16/23)
        
        driver = self.driver
        #finds the tissue Description field and enters a description w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "description").send_keys('%tectal proteins')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antigens are returned(first 3)
        self.assertEqual(symbol1, ['3CB2'])
        """
    def testAntigenCelllineSearch(self):
        """
        @Status tests that a basic cell line search works
        @see pwi-antibody-search-13
        """
        driver = self.driver
        #finds the cell line field and enter a cell line, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "cellLine").send_keys('MC/9')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['9C10'])
        self.assertEqual(symbol2, ['Integrin alpha5 antibody (5H10-27 (MFR5))'])
        
    def testAntigenCellline1Search(self):
        """
        @Status tests that a basic cell line search w/wildcard works
        @see pwi-antibody-search-13
        """
        driver = self.driver
        #finds the cell line field and enters a description, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "cellLine").send_keys('PCC4 Aza RI')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['anti-uvomorulin'])
        self.assertEqual(symbol2, ['anti-uvomorulin/E-Cadherin (DECMA-1), rat'])    
        
    def testAntigenAgePrefixSearch(self):
        """
        @Status tests that a basic age prefix search works
        @see pwi-antibody-search-14
        """
        driver = self.driver
        #finds the age prefix field and select the option 'postnatal day', tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "age")).select_by_value('string:postnatal year')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        print(symbol1)
        #Assert the correct antigen is returned
        self.assertEqual(symbol1, ['A4.840'])
        self.assertEqual(symbol2, ['clone A4.74'])    
        
    def testAntigenAgeStageSearch(self):
        """
        @Status tests that a basic age stage search works
        @see pwi-antibody-search-15
        """
        driver = self.driver
        #finds the age stage field and enters an age range, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "ageStage").send_keys('11.5')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['mouse anti-ICD'])   

    def testAntigenAgeStage2Search(self):
        """
        @Status tests that a basic age stage search with wildcard works
        @see pwi-antibody-search-15
        """
        driver = self.driver
        #finds the age stage field and enters an age stage, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "ageStage").send_keys('12%')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['mAb 13A4'])  
        
    def testAntigenGenderSearch(self):
        """
        @Status tests that a basic gender search works
        @see pwi-antibody-search-16
        """
        driver = self.driver
        #finds the gender field and enter the option 'female'(string:315164, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "gender")).select_by_value('string:315164')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['serum 231'])
        
    def testAntibodyRefJnumberSearch(self):
        """
        @Status tests that a basic antibody reference J number search works
        @see pwi-antibody-search-18
        """
        driver = self.driver
        #finds the antibody reference J# field and enter a J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "jnumid_ref-0").send_keys('J:147857')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibody is returned
        self.assertEqual(symbol1, ['14-1'])

    def testAntibodyRefJnumWildSearch(self):
        """
        @Status tests that a basic antibody reference J number with wildcard search works
        @see pwi-antibody-search-18
        """
        driver = self.driver
        #finds the antibody reference J# field and enter a J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "jnumid_ref-0").send_keys('J:14789%')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
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
        #Assert the correct antibody is returned(first 4)
        self.assertEqual(symbol1, ['anti-Ge-1 serum IC6'])
        self.assertEqual(symbol2, ['anti-GP15 MILI'])
        self.assertEqual(symbol3, ['anti-PLZF clone 2A9'])
        self.assertEqual(symbol4, ['eiF3a antibody'])
        self.assertEqual(symbol5, ['eiF4GII antibody'])
        
    def testAntibodyRefCiteSearch(self):
        """
        @Status tests that a basic antibody reference citation search works
        @see pwi-antibody-search-19
        """
        driver = self.driver
        #finds the antibody reference citation field and enters text, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "short_citation-0").send_keys('Jubb AM, J Pathol 2012 Jan;226(1):50-60')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        symbol3 = iterate.getTextAsList(cell3)
        symbol4 = iterate.getTextAsList(cell4)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['7130 antibody'])
        self.assertEqual(symbol2, ['anti-CD31 (2H8 MAB1398Z)'])
        self.assertEqual(symbol3, ['anti-LYVE1 (AF2125)'])
        self.assertEqual(symbol4, ['clone MECA-32'])
        

    def testAntibodyAliasSearch(self):
        """
        @Status tests that a basic antibody alias search works
        @see pwi-antibody-search-20
        """
        driver = self.driver
        #finds the antibody alias field and enters text, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "alias-0").send_keys('anti-CD117')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['Anti-c-kit'])
        
    def testAntibodyAlias2Search(self):
        """
        @Status tests that a basic antibody alias search with wildcard works
        @see pwi-antibody-search-20
        """
        driver = self.driver
        #finds the antibody alias field and enters text, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "alias-0").send_keys('anti-CD%')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        symbol3 = iterate.getTextAsList(cell3)
        symbol4 = iterate.getTextAsList(cell4)
        print(symbol1)
        #Assert the correct antibodies are returned(first 4)
        self.assertEqual(symbol1, ['3E2'])
        self.assertEqual(symbol2, ['anti-alpha6 integrin (GoH3)'])
        self.assertEqual(symbol3, ['Anti-c-kit'])
        self.assertEqual(symbol4, ['anti-mouse Pdgfrb (APB5; #14-1402-82)'])

    def testAntibodyAliasJnumSearch(self):
        """
        @Status tests that a basic antibody alias J number search works
        @see pwi-antibody-search-21
        """
        driver = self.driver
        #finds the antibody alias J number field and enters a J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "jnumid-0").send_keys('J:37016')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['MJ7/18'])

    def testAntibodyAliasCiteSearch(self):
        """
        @Status tests that a basic antibody alias citation search works
        @see pwi-antibody-search-22
        """
        driver = self.driver
        #finds the antibody alias J number field and enters a J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "short_citation-0").send_keys('Velling T, Dev Dyn 1996 Dec;207(4):355-71')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(6)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['MJ7/18'])

    def testAntibodyNotesSearch(self):
        """
        @Status tests that a basic antibody notes using wildcards search works
        @see pwi-antibody-search-23
        """
        driver = self.driver
        #finds the antibody alias J number field and enters a J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "antibodyNote").send_keys('%reduction in fluorescence% ')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['1310'])

    def testAntibodyMarkerSearch(self):
        """
        @Status tests that a basic antibody Marker search works
        @see pwi-antibody-search-24
        """
        driver = self.driver
        #finds the antibody marker field and enters text, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "markerSymbol-0").send_keys('sfpq')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['anti-PSF (clone B92)'])
        self.assertEqual(symbol2, ['anti-SFPQ'])

    def testAntibodyMarkerWildSearch(self):
        """
        @Status tests that a basic antibody marker using wildcards search works
        @see pwi-antibody-search-24
        """
        driver = self.driver
        #finds the antibody alias J number field and enters a J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "markerSymbol-0").send_keys('Sfp%')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        print(symbol1)
        #Assert the correct antibodies are returned
        self.assertEqual(symbol1, ['anti-PSF (clone B92)'])
        self.assertEqual(symbol2, ['anti-SFPQ'])

    def testAntibodyChrSearch(self):
        """
        @Status tests that a basic antibody chromosome search works
        @see pwi-antibody-search-25
        """
        driver = self.driver
        #finds the antibody chromosome field and enters text, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "chromosome-0").send_keys('Y')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(4)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        cell2 = table.get_row_cells(1)
        cell3 = table.get_row_cells(2)
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        cell6 = table.get_row_cells(5)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        symbol3 = iterate.getTextAsList(cell3)
        symbol4 = iterate.getTextAsList(cell4)
        symbol5 = iterate.getTextAsList(cell5)
        symbol6 = iterate.getTextAsList(cell6)
        print(symbol1)
        #Assert the correct antibodies are returned(first 6)
        self.assertEqual(symbol1, ['anti-Dby'])
        self.assertEqual(symbol2, ['anti-H-Y'])
        self.assertEqual(symbol3, ['anti-Sry'])
        self.assertEqual(symbol4, ['anti-SRY'])
        self.assertEqual(symbol5, ['Anti-Sry'])
        self.assertEqual(symbol6, ['anti-SRY (Mab #15)'])
                                                            
    def testAntibodyCreateBySearch(self):
        """
        @Status tests that an antibody search using the Created By field returns correct data
        @see pwi-antibody-date-search-1
        """
        driver = self.driver
        #find the Created By field and enter the name
        driver.find_element(By.ID, "createdBy").send_keys("jx")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), '5-HTT'))
        #find the Created by field
        create_by = driver.find_element(By.ID, 'createdBy').get_attribute('value')
        print(create_by)
        #Assert the  Created By field returned is correct 
        self.assertEqual(create_by, 'jx')
        #find the Creation Date field
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '2020-06-18')

    def testAntibodyModBySearch(self):
        """
        @Status tests that an antibody search using the Modified By field returns correct data
        @see pwi-antibody-date-search-2
        """
        driver = self.driver
        #find the Modified by field and enter the name
        driver.find_element(By.ID, "modifiedBy").send_keys("jx")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), '281-2'))
        #find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        #Assert the  Modified By field returned is correct 
        self.assertEqual(mod_by, 'jx')
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '2020-06-18')

    def testAntibodyCreateDateSearch(self):
        """
        @Status tests that an antibody search using the Creation Date field returns correct data
        @see pwi-antibody-date-search-3
        """
        driver = self.driver
        #find the Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("2013-01-23")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Anti-M-cadherin'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '2013-01-23')

    def testAntibodyModDateSearch(self):
        """
        @Status tests that an antibody search using the Modified By field returns correct data
        @see pwi-antibody-date-search-4
        """
        driver = self.driver
        #find the Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("2013-01-02")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'EphA4 antibody'))
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '2013-01-02')

    def testAntibodyModDateLessSearch(self):
        """
        @Status tests that an antibody search using the Modified By field and less than returns correct data
        @see pwi-antigen-date-search-7
        """
        driver = self.driver
        #find the antigen Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("<1998-09-14")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'anti-p107'))
        #find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        time.sleep(2)
        print(mod_by)
        #Assert the  Modified By field returned is correct 
        self.assertEqual(mod_by, 'dbo')
        time.sleep(2)
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '1998-08-04')

    def testAntibodyModDateLessEqualSearch(self):
        """
        @Status tests that an antibody search using the Modified By field and less than or equal to returns correct data
        @see pwi-antibody-date-search-8
        """
        driver = self.driver
        #find the Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("<=1998-09-14")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'anti-p107'))
        #find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        time.sleep(2)
        print(mod_by)
        #Assert the  Modified By field returned is correct 
        self.assertEqual(mod_by, 'dbo')
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '1998-09-14')

    def testAntibodyModDateBetweenSearch(self):
        """
        @Status tests that an antibody search using the Modified By field and between dates returns correct data
        @see pwi-antibody-date-search-9
        """
        driver = self.driver
        #find the Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("1998-08-04..1998-08-10")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'anti-p107'))
        #find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        time.sleep(2)
        print(mod_by)
        #Assert the  Modified By field returned is correct 
        self.assertEqual(mod_by, 'dbo')
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '1998-08-04')

    def testAntibodyCreateDateLessSearch(self):
        """
        @Status tests that an antibody search using the Creation Date field and Less than returns correct data
        @see pwi-antibody-date-search-12
        """
        driver = self.driver
        #find the Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("<1998-06-23")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'anti-GLUT1'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        time.sleep(2)
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '1998-06-22')

    def testAntibodyCreateDateLessEqualSearch(self):
        """
        @Status tests that an antibody search using the Creation Date field and Less than, equals to returns correct data
        @see pwi-antibody-date-search-13
        """
        driver = self.driver
        #find the Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("<=1998-06-23")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'anti-GLUT1'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '1998-06-22')

    def testAntibodyCreateDateBetweenSearch(self):
        """
        @Status tests that an antibody search using the Creation Date field and Between dates returns correct data
        @see pwi-antibody-date-search-14
        """
        driver = self.driver
        #find the antibody Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("1998-06-22..1998-07-09")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'anti-GLUT1'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '1998-06-22')



        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEIAntibodySearch))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))      