'''
Created on Aug 3, 2020
Tests the search features for the Mutant Cell Lines  EI module
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

class TestEIMCLSearch(unittest.TestCase):
    """
    @status Test Mutant Cell Lines searching, etc
    """

    def setUp(self):
        self.driver = webdriver.Firefox() 
        #self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/mutantcellline")
    
    def tearDown(self):
        self.driver.close()

    def testMclWildSearch(self):
        """
        @Status tests that a basic mutant cell line with wildcard search works
        @see pwi-mcl-search-1
        """
        driver = self.driver
        #finds the Mutant Cell Line field and enters a cell line, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "cellLine").send_keys('CT14%')
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
        #Assert the correct mutant cewll lines are returned
        self.assertEqual(symbol1, ['CT141'])
        self.assertEqual(symbol2, ['CT143'])
        self.assertEqual(symbol3, ['CT146'])

    def testMclSearch(self):
        """
        @Status tests that a basic mutant cell line search works
        @see pwi-mcl-search-1
        """
        driver = self.driver
        #finds the Mutant Cell Line field and enters a mutant cell line, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "cellLine").send_keys('CT45')
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
        #Assert the correct mutant cell line is returned
        self.assertEqual(symbol1, ['CT45'])

    def testMclCreatorSearch(self):
        """
        @Status tests that a basic MCL Creator search works
        @see pwi-mcl-search-2
        """
        driver = self.driver
        #finds the Creator filed and selects the option 'shinichi Aizawa'(string:4811539), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "creator")).select_by_value('string:4811539')
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
        #Assert the correct mutant cell line is returned
        self.assertEqual(symbol1, ['PAT-12'])
        
    def testMclPclSearch(self):
        """
        @Status tests that a basic parent cell line search works 
        @see pwi-mcl-search-3
        """
        driver = self.driver
        #finds the parent cell line field and enters a parent cell line, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "parentCellLine").send_keys('RENKA')
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
        #Assert the correct antigen is returned
        self.assertEqual(symbol1, ['Not Specified'])
        self.assertEqual(symbol2, ['Not Specified'])
        self.assertEqual(symbol3, ['Not Specified'])
        
    def testMclPclStrainSearch(self):
        """
        @Status tests that a basic parent cell line strain search works 
        @see pwi-mcl-search-4
        """
        driver = self.driver
        #finds the notes field and enters test, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "parentCellLineStrain").send_keys('129S7/SvEvBrd-Hprt%')
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
        #Assert the correct mutant cell lines are returned(first 5)
        self.assertEqual(symbol1, ['10C6'])
        self.assertEqual(symbol2, ['6E6'])
        self.assertEqual(symbol3, ['6F11'])
        self.assertEqual(symbol4, ['8A8'])
        self.assertEqual(symbol5, ['8D7'])
        
    def testMclCellLineTypeSearch(self):
        """
        @Status tests that a basic Cell Line Type works 
        @see pwi-mcl-search-5 
        """
        driver = self.driver
        #finds the cell line type field and select the option 'spermatogonial stem cell'(string:3982969), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "cellLineType")).select_by_value('string:3982969')
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
        #Assert the correct antigens are returned(first 5)
        self.assertEqual(symbol1, ['Not Specified'])
        self.assertEqual(symbol2, ['Not Specified'])
        
        
    def testMclDerivationTypeSearch(self):
        """
        @Status tests that a basic derivation type search works
        @see pwi-mcl-search-6
        """
        driver = self.driver
        #finds the derivation type field and selects the option 'transposon induced' (value='string:2327161), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "derivationType")).select_by_value('string:2327161')
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
        #Assert the correct antigen is returned
        self.assertEqual(symbol1, ['Not Specified'])               
        
    def testMclVectorNameSearch(self):
        """
        @Status tests that a basic Vector Name search works
        @see pwi-mcl-search-7
        """
        driver = self.driver
        #finds the vector name field and enters a vector, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "vector").send_keys('pGT0lxf')
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
        cell4 = table.get_row_cells(3)
        cell5 = table.get_row_cells(4)
        symbol1 = iterate.getTextAsList(cell1)
        symbol2 = iterate.getTextAsList(cell2)
        symbol3 = iterate.getTextAsList(cell3)
        symbol4 = iterate.getTextAsList(cell4)
        symbol5 = iterate.getTextAsList(cell5)
        print(symbol1)
        #Assert the correct mutant cell lines are returned(first 5)
        self.assertEqual(symbol1, ['XP0008'])
        self.assertEqual(symbol2, ['XP0009'])
        self.assertEqual(symbol3, ['XP0010'])
        self.assertEqual(symbol4, ['XP0011'])
        self.assertEqual(symbol5, ['XP0012'])
        
    def testMclVectorNameWildSearch(self):
        """
        @Status tests that a basic vector name w/wildcard search works
        @see pwi-mcl-search-7
        """
        driver = self.driver
        #finds the strain field and enters a strain w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "vector").send_keys('ROSANB%')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #Does a webdriver wait until the results table is present so we know the page is loaded
        #if WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, 'resultsCount'))):
            #print('page loaded')
        time.sleep(2)
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
        #Assert the correct mutant cell lines are returned
        self.assertEqual(symbol1, ['10C2'])
        self.assertEqual(symbol2, ['15C3'])    
        self.assertEqual(symbol3, ['5B4'])
        self.assertEqual(symbol4, ['CN3'])
        
    def testMclVectorTypeSearch(self):
        """
        @Status tests that a basic tissue search works
        @see pwi-mcl-search-8
        """
        driver = self.driver
        #finds the vector type field and select the option 'enhancer trap'(string:3982972, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "vectorType")).select_by_value('string:3982972')
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
        #Assert the correct mutant cell lines are returned
        self.assertEqual(symbol1, ['6028'])
        self.assertEqual(symbol2, ['6029'])
        self.assertEqual(symbol3, ['gt216'])
        
    def testMclAlleleSearch(self):
        """
        @Status tests that a basic allele search works
        @see pwi-mcl-search-11
        """
        driver = self.driver
        #finds the allele field and enters an allele, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "alleleSymbols").send_keys('Gata1<tm1Phi>')
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
        #Assert the correct mutant cell lines are returned
        self.assertEqual(symbol1, ['Not Specified'])

        
    def testMclAlleleWildSearch(self):
        """
        @Status tests that a basic allele symbol w/wildcard search works
        @see pwi-antigen-search-11
        """
        driver = self.driver
        #finds the allelesymbols field and enters an allele symbol w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "alleleSymbols").send_keys('Meg3%')
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
        #Assert the correct mutant cell lines are returned
        self.assertEqual(symbol1, ['gt216'])
        self.assertEqual(symbol2, ['Not Specified'])
        self.assertEqual(symbol3, ['Not Specified'])
        self.assertEqual(symbol4, ['Not Specified'])
        self.assertEqual(symbol5, ['Not Specified'])
        
    def testMclLogicaldbSearch(self):
        """
        @Status tests that a basic logical DB search works
        @see pwi-mcl-search-12
        """
        driver = self.driver
        #finds the logical bd field and select the option 'TIGM'(string:97), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "accName")).select_by_value('string:97')
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
        #Assert the correct mutant cell lines are returned
        self.assertEqual(symbol1, ['IST10006D1HMF1'])
        self.assertEqual(symbol2, ['OST489724'])    
        self.assertEqual(symbol3, ['SGT207T1'])
        
    def testMclAccNameSearch(self):
        """
        @Status tests that a basic Acc Name search works
        @see pwi-mcl-search-13
        """
        driver = self.driver
        #finds the Acc Name field and enter a name, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "accName-0").send_keys('E209G12')
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
        #Assert the correct mutant cell line is returned
        self.assertEqual(symbol1, ['E209G12'])
        
    def testMclAccNameWildSearch(self):
        """
        @Status tests that a basic Acc Name search w/wildcard works
        @see pwi-antigen-search-13 
        """
        driver = self.driver
        #finds the cell line field and enters a description w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "accName-0").send_keys('E209G0%')
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
        #Assert the correct mutant cell lines are returned
        self.assertEqual(symbol1, ['E209G01'])
        self.assertEqual(symbol2, ['E209G02'])    
        self.assertEqual(symbol3, ['E209G03'])
        self.assertEqual(symbol4, ['E209G04'])
        self.assertEqual(symbol5, ['E209G06'])
        
    def testMclMultiAllelesSearch(self):
        """
        @Status tests that a basic mutant cell line search works and brings back multiple alles in the Allele Symbol(s) field
        @see pwi-mcl-search-14
        """
        driver = self.driver
        #finds the mutant cell line field and enter a cell line, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "cellLine").send_keys('10226A-A7 ')
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
        #Assert the correct antigen is returned
        self.assertEqual(symbol1, ['10226A-A7'])
        sym = driver.find_element(By.ID, "alleleSymbols").get_attribute('value')
        print(sym)
        self.assertEqual(sym, "Cbln3<tm1(KOMP)Vlcg>,Cbln3<tm1.1(KOMP)Vlcg>")
        
#all the tests after this point need to be rewritten for the mutant cell line module
                                                            
    def testAntigenCreateBySearch(self):
        """
        @Status tests that an antigen search using the Created By field returns correct data
        @see pwi-antigen-date-search-1
        """
        driver = self.driver
        #find the antigen Created By field and enter the name
        driver.find_element(By.ID, "createdBy").send_keys("jx")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Not Specified'))
        #find the Created by field
        create_by = driver.find_element(By.ID, 'createdBy').get_attribute('value')
        print(create_by)
        #Assert the  Created By field returned is correct 
        self.assertEqual(create_by, 'jx')
        #find the Creation Date field
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '2009-10-07')

    def testAntigenModBySearch(self):
        """
        @Status tests that an antigen search using the Modified By field returns correct data
        @see pwi-antigen-date-search-2
        """
        driver = self.driver
        #find the alleles Modified by field and enter the name
        driver.find_element(By.ID, "modifiedBy").send_keys("monikat")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'N01359P1_C_97W_B2'))
        #find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        #Assert the  Modified By field returned is correct 
        self.assertEqual(mod_by, 'monikat')
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '2015-01-07')

    def testAntigenCreateDateSearch(self):
        """
        @Status tests that an antigen search using the Creation Date field returns correct data
        @see pwi-antigen-date-search-3
        """
        driver = self.driver
        #find the antigen Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("2013-01-23")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Not Specified'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '2013-01-23')

    def testAntigenModDateSearch(self):
        """
        @Status tests that an antigen search using the Modified By field returns correct data
        @see pwi-antigen-date-search-4
        """
        driver = self.driver
        #find the antigen Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("2013-01-02")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Not Specified'))
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '2013-01-02')

    def testAntigenModDateLessSearch(self):
        """
        @Status tests that an antigen search using the Modified By field and less than returns correct data
        @see pwi-antigen-date-search-7
        """
        driver = self.driver
        #find the antigen Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("<2006-01-01")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Ex54'))
        #find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        #Assert the  Modified By field returned is correct 
        self.assertEqual(mod_by, 'csmith')
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '2005-06-02')

    def testAntigenModDateLessEqualSearch(self):
        """
        @Status tests that an antigen search using the Modified By field and less than or equal to returns correct data
        @see pwi-antigen-date-search-8
        """
        driver = self.driver
        #find the antigen Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("<=2005-06-02")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Ex54'))
        #find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        #Assert the  Modified By field returned is correct 
        self.assertEqual(mod_by, 'csmith')
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '2005-06-02')

    def testAntigenModDateBetweenSearch(self):
        """
        @Status tests that an antigen search using the Modified By field and between dates returns correct data
        @see pwi-antigen-date-search-9
        """
        driver = self.driver
        #find the antigen Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("2005-05-09..2005-06-02")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Ex54'))
        #find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        #Assert the  Modified By field returned is correct 
        self.assertEqual(mod_by, 'csmith')
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '2005-06-02')

    def testAntigenCreateDateLessSearch(self):
        """
        @Status tests that an antigen search using the Creation Date field and Less than returns correct data
        @see pwi-antigen-date-search-12
        """
        driver = self.driver
        #find the antigen Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("<2005-05-10")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'A006B04'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '2005-05-09')

    def testAntigenCreateDateLessEqualSearch(self):
        """
        @Status tests that an antigen search using the Creation Date field and Less than, equals to returns correct data
        @see pwi-antigen-date-search-13
        """
        driver = self.driver
        #find the alleles Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("<=2005-06-02")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'A006B04'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '2005-05-09')

    def testAntigenCreateDateBetweenSearch(self):
        """
        @Status tests that an antigen search using the Creation Date field and Between dates returns correct data
        @see pwi-antigen-date-search-14
        """
        driver = self.driver
        #find the antigen Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("2005-05-09..2005-06-02")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'A006B04'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '2005-05-09')



        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEIMCLSearch))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))  