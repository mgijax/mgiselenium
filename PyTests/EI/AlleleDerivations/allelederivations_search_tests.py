'''
Created on Jul 31, 2020

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

class TestEIAlleleDerivationSearch(unittest.TestCase):
    """
    @status Test Allele Derivation searching, etc
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/allelederivation")
    
    def tearDown(self):
        self.driver.close()

    def testAlleleDerivationTypeSearch(self):
        """
        @Status tests that a basic Derivation Type search works
        @see pwi-allele-der-search-1
        """
        driver = self.driver
        #finds the Allele Derivation Type field and select the option Endonuclease-mediated(string:11927650), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "derivationType")).select_by_value('string:11927650')
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
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct antigen is returned
        self.assertEqual(result1, ['Not Applicable Endonuclease-mediated Library E14TG2a 129P2/OlaHsd Not Specified'])

    def testAlleleDerivationjnumSearch(self):
        """
        @Status tests that a basic allele derivation J number search works
        @see pwi-allele-der-search-2
        """
        driver = self.driver
        #finds the Allele Derivation J number field and enters a J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "jnumID").send_keys('J:14927')
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
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct derivation is returned
        self.assertEqual(result1, ['Achim Gossler Gene trapped Library D3 129S2/SvPas p6LSN'])

    def testAlleleDerivationJnumwildSearch(self):
        """
        @Status tests that a basic allele derivation J number using wilcard search works
        @see pwi-allele-der-search-2
        """
        driver = self.driver
        #finds the J number field and enters a partial J number with wilcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "jnumID").send_keys('J:14%')
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
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        print(result1)
        #Assert the correct derivations are returned
        self.assertEqual(result1, ['Achim Gossler Gene trapped Library D3 129S2/SvPas p6LSN'])
        self.assertEqual(result2, ['Elizabeth Simpson Targeted Library E14TG2a 129P2/OlaHsd Not Specified'])
        self.assertEqual(result3, ['Elizabeth Simpson Targeted Library mEMS1202 (B6.129P2-Hprt<b-m3>/J x 129S-Gt(ROSA)26Sor<tm1Sor>/J)F1 Not Specified'])
        
    def testAlleleDerivationCiteWildSearch(self):
        """
        @Status tests that a basic Citation search works with wildcard
        @see pwi-allele-der-search-3
        """
        driver = self.driver
        #finds the citation field and enters an citation name w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "citation").send_keys('Mitchell%')
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
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct derivation is returned
        self.assertEqual(result1, ['BayGenomics Gene Trap Library pGT0,1,2'])
        
    def testAlleleDerivationCreatorSearch(self):
        """
        @Status tests that a basic Creator search works 
        @see pwi-allele-der-search-4
        """
        driver = self.driver
        #finds the creator field and select the option Achim Gossler(string:4788779), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "creator")).select_by_value('string:4788779')
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
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct derivation is returned
        self.assertEqual(result1, ['Achim Gossler Gene trapped Library D3 129S2/SvPas p6LSN'])
        
        
    def testAlleleDerivationPclWildSearch(self):
        """
        @Status tests that a basic Parent Cell Line search w/wildcard works 
        @see pwi-allele-der-search-5
        """
        driver = self.driver
        #finds the parent cell line field and enters text w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "parentCellLine").send_keys('mEMS%')
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
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        print(result1)
        #Assert the correct derivations are returned(first 5)
        self.assertEqual(result1, ['Elizabeth Simpson Targeted Library mEMS1202 (B6.129P2-Hprt<b-m3>/J x 129S-Gt(ROSA)26Sor<tm1Sor>/J)F1 Not Specified'])
        self.assertEqual(result2, ['Elizabeth Simpson Targeted Library mEMS1204 (B6.129P2-Hprt<b-m3>/J x 129S-Gt(ROSA)26Sor<tm1Sor>/J)F1 Not Specified'])
        self.assertEqual(result3, ['Elizabeth Simpson Targeted Library mEMS1217 (B6.129P2-Hprt<b-m3>/J x 129S-Gt(ROSA)26Sor<tm1Sor>/J)F1 Not Specified'])
        self.assertEqual(result4, ['Elizabeth Simpson Targeted Library mEMS1218 (B6.129P2-Hprt<b-m3>/J x 129S-Gt(ROSA)26Sor<tm1Sor>/J)F1 Not Specified'])
        self.assertEqual(result5, ['Elizabeth Simpson Targeted Library mEMS1254 B6.129P2-Hprt<b-m3>/J Not Specified'])
        
    def testAlleleDerivationPclSearch(self):
        """
        @Status tests that a basic parent cell line search works
        @see pwi-allele-der-search-5
        """
        driver = self.driver
        #finds the parent cell line field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "parentCellLine").send_keys('D3')
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
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        print(result1)
        #Assert the correct derivations are returned(first 5)
        self.assertEqual(result1, ['Achim Gossler Gene trapped Library D3 129S2/SvPas p6LSN'])
        self.assertEqual(result2, ['Harald von Melchner Gene trapped Library D3 129S2/SvPas ppgklxneoLacZ'])
        self.assertEqual(result3, ['Not Specified Chemically and radiation induced Library D3 129S2/SvPas Not Specified'])
        self.assertEqual(result4, ['Not Specified Chemically induced (ENU) Library D3 129S2/SvPas Not Specified'])
        self.assertEqual(result5, ['Not Specified Chemically induced (other) Library D3 129S2/SvPas Not Specified'])            
        
    def testAlleleDerivationPclStrainWildSearch(self):
        """
        @Status tests that a basic Parent Cell Line strain search w/wildcard works 
        @see pwi-allele-der-search-6
        """
        driver = self.driver
        #finds the parent cell line strain field and enters text w/wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "parentCellLineStrain").send_keys('129S7%')
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
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        print(result1)
        #Assert the correct derivations are returned(first 5)
        self.assertEqual(result1, ['FHCRC Gene Trap Library ROSABetageo'])
        self.assertEqual(result2, ['FHCRC Gene Trap Library SABetageo'])
        self.assertEqual(result3, ['Helmholtz Zentrum Muenchen GmbH Targeted Library AB2.2 129S7/SvEvBrd-Hprt<b-m2> L1L2_Bact_P'])
        self.assertEqual(result4, ['Helmholtz Zentrum Muenchen GmbH Targeted Library AB2.2 129S7/SvEvBrd-Hprt<b-m2> L1L2_gt0'])
        self.assertEqual(result5, ['Helmholtz Zentrum Muenchen GmbH Targeted Library AB2.2 129S7/SvEvBrd-Hprt<b-m2> L1L2_gt1'])
        
    def testAlleleDerivationPclStrainSearch(self):
        """
        @Status tests that a basic parent cell line search works
        @see pwi-allele-der-search-6
        """
        driver = self.driver
        #finds the parent cell line strain field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "parentCellLineStrain").send_keys('129S2/SvPas')
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
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        print(result1)
        #Assert the correct derivations are returned(first 5)
        self.assertEqual(result1, ['Achim Gossler Gene trapped Library D3 129S2/SvPas p6LSN'])
        self.assertEqual(result2, ['ESDB Gene Trap Library MICB1'])
        self.assertEqual(result3, ['GGTC Gene Trap Library GV02C04'])
        self.assertEqual(result4, ['GGTC Gene Trap Library GV03C04'])
        self.assertEqual(result5, ['GGTC Gene Trap Library GV04C04'])            
              
    def testAlleleDerivationCellLineTypeSearch(self):
        """
        @Status tests that a basic Cell Line Type search works
        @see pwi-allele-der-search-7
        """
        driver = self.driver
        #finds the Cell line Type field and select the option 'Spermatogonial Stem Cell'(string:3982970), tabs out of the field then clicks the Search button
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
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct derivation is returned
        self.assertEqual(result1, ['Not Specified Gene trapped Library Not Specified Not Specified ROSABetageo'])
        
    def testAlleleDerivationVectorNameWildSearch(self):
        """
        @Status tests that a basic vector name using a wilcard search works
        @see pwi-allele-der-search-8
        """
        driver = self.driver
        #finds the vector name field and enters some text with wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "vector").send_keys('U3N%')
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
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        print(result1)
        #Assert the correct derivations are returned
        self.assertEqual(result1, ['ESDB Gene Trap Library MICB1'])
        self.assertEqual(result2, ['ESDB Gene Trap Library MICB2']) 
        self.assertEqual(result3, ['H Earl Ruley Gene trapped Library D3H 129S2/SvPas U3neo']) 
        self.assertEqual(result4, ['H Earl Ruley Gene trapped Library D3H 129S2/SvPas U3NeoSV1']) 
        self.assertEqual(result5, ['H Earl Ruley Gene trapped Library D3H 129S2/SvPas U3NeoSV2']) 
        
    def testAlleleDerivationVectorNameSearch(self):
        """
        @Status tests that a basic vector name search works
        @see pwi-allele-der-search-8
        """
        driver = self.driver
        #finds the vector name field and enters some text, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "vector").send_keys('ROSANBeta-geo')
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
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        print(result1)
        #Assert the correct derivations are returned
        self.assertEqual(result1, ['Masahide Asano Gene trapped Library E14.1 129P2/OlaHsd ROSANBeta-geo'])
        self.assertEqual(result2, ['Yoichiro Iwakura Gene trapped Library R1 (129X1/SvJ x 129S1/Sv)F1-Kitl<+> ROSANBeta-geo']) 

        
    def testAlleleDerivationVevtorTypeSearch(self):
        """
        @Status tests that a basic vector type search works
        @see pwi-allele-der-search-9
        """
        driver = self.driver
        #finds the vector type field and enter the option 'poly-A trap'(string:3982975, tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "vectorType")).select_by_value('string:3982975')
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
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        print(result1)
        #Assert the correct derivations are returned
        self.assertEqual(result1, ['Peter Gruss Gene trapped Library MPI-II 129/Sv IRESbetagalNeo(-pA)'])  
        self.assertEqual(result2, ['Peter Gruss Gene trapped Library R1 (129X1/SvJ x 129S1/Sv)F1-Kitl<+> IRESbetagalNeo(-pA)'])
        
    def testAlleleDerivationNoteWildSearch(self):
        """
        @Status tests that a basic note with wildcard search works
        @see pwi-allele-der-search-10
        """
        driver = self.driver
        #finds the note field and enter test with wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "generalNote").send_keys('%Lexicon%')
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
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct antigens are returned
        self.assertEqual(result1, ['Lexicon Genetics Gene Trap Library 129S5/SvEvBrd'])
                                                            
    def testAlleleDerivationCreateBySearch(self):
        """
        @Status tests that an allele derivation search using the Created By field returns correct data
        @see pwi-allele-der-date-search-1
        """
        driver = self.driver
        #find the derivation Created By field and enter the name
        driver.find_element(By.ID, "createdBy").send_keys("smb")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Not Specified Gene trapped Library Not Specified Not Specified ROSABetageo'))
        #find the Created by field
        create_by = driver.find_element(By.ID, 'createdBy').get_attribute('value')
        print(create_by)
        #Assert the  Created By field returned is correct 
        self.assertEqual(create_by, 'smb')
        #find the Creation Date field
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '2009-08-12')

    def testAlleleDerivationModBySearch(self):
        """
        @Status tests that a derivation search using the Modified By field returns correct data
        @see pwi-allele-der-date-search-2
        """
        driver = self.driver
        #find the derivation Modified by field and enter the name
        driver.find_element(By.ID, "modifiedBy").send_keys("smb")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Not Specified Gene trapped Library Not Specified Not Specified ROSABetageo'))
        #find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        #Assert the  Modified By field returned is correct 
        self.assertEqual(mod_by, 'smb')
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '2009-09-02')

    def testAlleleDerivationCreateDateSearch(self):
        """
        @Status tests that a derivation search using the Creation Date field returns correct data
        @see pwi-allele-der-date-search-3
        """
        driver = self.driver
        #find the antigen Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("2018-09-04")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Not Applicable Endonuclease-mediated Library TC1/TC-1 129S6/SvEvTac Not Specified'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '2018-09-04')

    def testAlleleDerivationModDateSearch(self):
        """
        @Status tests that a derivation search using the Modified By field returns correct data
        @see pwi-antigen-date-search-4
        """
        driver = self.driver
        #find the derivation Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("2009-09-02")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Not Specified Gene trapped Library Not Specified Not Specified ROSABetageo'))
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '2009-09-02')

    def testAlleleDerivationModDateLessSearch(self):
        """
        @Status tests that a derivation search using the Modified By field and less than returns correct data
        @see pwi-allele-der-date-search-7
        """
        driver = self.driver
        #find the derivation Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("<2009-08-12")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'BayGenomics Gene Trap Library pGT0,1,2'))
        #find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        #Assert the  Modified By field returned is correct 
        self.assertEqual(mod_by, 'derivationload')
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '2009-08-11')

    def testAlleleDerivationModDateLessEqualSearch(self):
        """
        @Status tests that a derivation search using the Modified By field and less than or equal to returns correct data
        @see pwi-antigen-date-search-8
        """
        driver = self.driver
        #find the derivation Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("<=2009-08-14")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Achim Gossler Gene trapped Library D3 129S2/SvPas p6LSN'))
        #find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        #Assert the  Modified By field returned is correct 
        self.assertEqual(mod_by, 'mnk')
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '2009-08-14')

    def testAlleleDerivationModDateBetweenSearch(self):
        """
        @Status tests that a derivation search using the Modified By field and between dates returns correct data
        @see pwi-antigen-date-search-9
        """
        driver = self.driver
        #find the derivation Modification Date field and enter a date
        driver.find_element(By.ID, "modificationDate").send_keys("2009-08-14..2009-08-17")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Achim Gossler Gene trapped Library D3 129S2/SvPas p6LSN'))
        #find the Modified by field
        mod_by = driver.find_element(By.ID, 'modifiedBy').get_attribute('value')
        print(mod_by)
        #Assert the  Modified By field returned is correct 
        self.assertEqual(mod_by, 'mnk')
        #find the Modification Date field
        mod_date = driver.find_element(By.ID, 'modificationDate').get_attribute('value')
        print(mod_date)
        #Assert the Modification Date field returned is correct 
        self.assertEqual(mod_date, '2009-08-14')

    def testAlleleDerivationCreateDateLessSearch(self):
        """
        @Status tests that a derivation search using the Creation Date field and Less than returns correct data
        @see pwi-allele-der-date-search-12
        """
        driver = self.driver
        #find the derivation Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("<2009-08-18")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Achim Gossler Gene trapped Library D3 129S2/SvPas p6LSN'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '2009-08-14')

    def testAlleleDerivationCreateDateLessEqualSearch(self):
        """
        @Status tests that a derivation search using the Creation Date field and Less than, equals to returns correct data
        @see pwi-antigen-date-search-13
        """
        driver = self.driver
        #find the derivation Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("<=2009-08-17")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Achim Gossler Gene trapped Library D3 129S2/SvPas p6LSN'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '2009-08-14')

    def testAlleleDerivationCreateDateBetweenSearch(self):
        """
        @Status tests that a derivation search using the Creation Date field and Between dates returns correct data
        @see pwi-antigen-date-search-14
        """
        driver = self.driver
        #find the derivation Creation Date field and enter a date
        driver.find_element(By.ID, "creationDate").send_keys("2009-08-17..2009-08-18")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.ID, 'resultsTable'), 'Harald von Melchner Gene trapped Library D3 129S2/SvPas ppgklxneoLacZ'))
        create_date = driver.find_element(By.ID, 'creationDate').get_attribute('value')
        print(create_date)
        #Assert the  Creation Date field returned is correct 
        self.assertEqual(create_date, '2009-08-17')



        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEIAlleleDerivationSearch))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))                                     