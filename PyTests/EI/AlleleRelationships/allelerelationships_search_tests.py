'''
Created on Mar 17, 2022

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

class TestEIAlleleRelationshipsSearch(unittest.TestCase):
    """
    @status Test Allele Relationships searching, etc
    """

    def setUp(self):
        self.driver = webdriver.Firefox() 
        #self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/allelefear/")
    
    def tearDown(self):
        self.driver.close()

    def testEIAlleleRelationshipsMGI_IDSearch(self):
        """
        @Status tests that a basic MGI ID search works
        @see pwi-allele-rel-search-1
        """
        driver = self.driver
        #finds the Allele Relationships MGI ID field and enter the ID, tabs out of the field then clicks the Search button
        self.driver.find_element(By.ID, "alleleAccID").send_keys('MGI:6430734')
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
        self.assertEqual(result1, ['Gpc5<C57BL/6J>'])

    def testEIAlleleRelationshipsAlleleSymbolSearch(self):
        """
        @Status tests that a basic allele relationship Allele symbol search works
        @see pwi-allele-rel-search-2
        """
        driver = self.driver
        #finds the Allele Relationship Allele field and enters an allele symbol, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "alleleSymbol").send_keys('Gpc5<DBA/2J>')
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
        #Assert the correct relationship is returned
        self.assertEqual(result1, ['Gpc5<DBA/2J>'])

    def testEIAlleleRelationshipsAlleleSymbolwildSearch(self):
        """
        @Status tests that a basic allele symbol using wilcard search works
        @see pwi-allele-rel-search-2
        """
        driver = self.driver
        #finds the allele symbol field and enters a partial symbol with wildcard, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "alleleSymbol").send_keys('Gpc5%')
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
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        result5 = iterate.getTextAsList(cell5)
        result6 = iterate.getTextAsList(cell6)
        print(result1)
        #Assert the correct relationships are returned
        self.assertEqual(result1, ['Gpc5<C57BL/6J>'])
        self.assertEqual(result2, ['Gpc5<DBA/2J>'])
        self.assertEqual(result3, ['Gpc5<Gt(IST13574F4)Tigm>'])
        self.assertEqual(result4, ['Gpc5<tm1.1Mrl>'])
        self.assertEqual(result5, ['Gpc5<tm1a(KOMP)Wtsi>'])
        self.assertEqual(result6, ['Gpc5<tm1e(KOMP)Wtsi>'])
        
    def testEIAlleleRelationshipsMITypeSearch(self):
        """
        @Status tests that a basic allele relationships mutation involved type search works with wildcard
        @see pwi-allele-rel-search-3
        """
        driver = self.driver
        #finds the Relationship Type field and select option normal(string:12438362), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "MIrelationshipTerm-0")).select_by_value('string:12438362')
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
        #Assert the correct relationships are returned
        self.assertEqual(result1, ['Gpc5<C57BL/6J>'])
        self.assertEqual(result2, ['Gpc5<DBA/2J>'])
        self.assertEqual(result3, ['Grm7<rs3723352-G>'])
        
    def testEIAlleleRelationshipsMIJnumSearch(self):
        """
        @Status tests that a basic allele relationships Mutation Involves J# search works 
        @see pwi-allele-rel-search-4
        """
        driver = self.driver
        #finds the mutation involves J number field and enter the J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "MIjnumID-0").send_keys('J:257336')
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
        #Assert the correct relationships is returned
        self.assertEqual(result1, ['Dp(13Spock1)1Tac'])
        
        
    def testEIAlleleRelationshipMImrkAccIDSearch(self):
        """
        @Status tests that a basic allele relationships mutation involves marker Acc ID search works 
        @see pwi-allele-rel-search-5
        """
        driver = self.driver
        #finds the mutation involves marker acc ID field and enters an MGI ID, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "MImarkerAccID-0").send_keys('MGI:96677')
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
        #Assert the correct relationshipss are returned(first 5)
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
        #finds the muation involves marker field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "MImarkerSymbol-0").send_keys('Clock')
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
        #Assert the correct relationships are returned(first 5)
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
        #finds the mutated involves note field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "MInote-0").send_keys('Exon 2 was inverted.')
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
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct relationships are returned
        self.assertEqual(result1, ['Ext1<tm1.2Vcs>'])
        
    def testEIAlleleRelationshipsECTypeSearch(self):
        """
        @Status tests that a basic allele relationships expresses component type search works 
        @see pwi-allele-rel-search-8
        """
        driver = self.driver
        #finds the Expresses component Relationship Type field and select option expresses_mouse_gene(string:12965808), tabs out of the field then clicks the Search button
        Select(driver.find_element(By.ID, "ECrelationshipTerm-0")).select_by_value('string:12965808')
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
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        print(result1)
        #Assert the correct relationships are returned
        self.assertEqual(result1, ['2500002B13Rik<tm1(CAG-2500002B13Rik)Yo>'])
        self.assertEqual(result2, ['Actb<tm3.1(Sirt1)Npa>'])
        self.assertEqual(result3, ['Ak7<Tg(tetO-Hmox1)67Sami>'])
        
    def testEIAlleleRelationshipsECJnumSearch(self):
        """
        @Status tests that a basic allele relationships Expresses Component J# search works 
        @see pwi-allele-rel-search-9
        """
        driver = self.driver
        #finds the expresses component J number field and enter the J number, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "ECjnumID-0").send_keys('J:246645')
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
        #Assert the correct relationships is returned
        self.assertEqual(result1, ['Sox3<em1(Sox2)Pqt>'])
        
        
    def testEIAlleleRelationshipECmrkAccIDSearch(self):
        """
        @Status tests that a basic allele relationships expresses component marker Acc ID search works 
        @see pwi-allele-rel-search-10
        """
        driver = self.driver
        #finds the expresses component marker acc ID field and enters an MGI ID, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "ECmarkerAccID-0").send_keys('MGI:104847')
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
        #Assert the correct relationshipss are returned
        self.assertEqual(result1, ['Adora3<tm1(ADORA3)Msth>'])
        
    def testEIAlleleRelationshipsECMrkSearch(self):
        """
        @Status tests that a basic allele relationships expresses component marker search works
        @see pwi-allele-rel-search-11
        """
        driver = self.driver
        #finds the expresses component marker field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "ECmarkerSymbol-0").send_keys('Gata2')
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
        #Assert the correct relationships are returned(first 5)
        self.assertEqual(result1, ['Gata2<tm2(Gata2)Jeng>'])
        self.assertEqual(result2, ['Gt(ROSA)26Sor<tm10(Gata2)Jhai>'])          
        
    def testEIAlleleRelationshipsECNoteSearch(self):
        """
        @Status tests that a basic allele relationships expresses component note search  works 
        @see pwi-allele-der-search-12
        """
        driver = self.driver
        #finds the mutated involves note field and enters text , tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "ECnote-0").send_keys('HBEGF/GFP fusion')
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
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct relationships are returned
        self.assertEqual(result1, ['Aire<tm5.1(HBEGF/GFP)Mmat>'])        

    def testEIAlleleRelationshipsOrganismSearch(self):
        """
        @Status tests that a basic allele relationships Organism Pick List search  works 
        @see pwi-allele-der-search-13
        """
        driver = self.driver
        #finds the Organism pick list field and select  the option zebrafish , then click the Search button
        Select(driver.find_element(By.ID, "organismLookup")).select_by_value('string:zebrafish')
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
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        print(result1)
        #Assert the correct relationships are returned
        self.assertEqual(result1, ['Mesp2<tm7.1(mespb)Ysa>'])        
        self.assertEqual(result2, ['Mesp2<tm7(mespb)Ysa>'])
        self.assertEqual(result3, ['Tg(MMTV-Catnb)3Pac'])   
        self.assertEqual(result4, ['Tg(MMTV-Catnb)5Pac'])
    
    def testEIAlleleRelationshipsPropertySearch(self):
        """
        @Status tests that a basic allele relationships property search  works 
        @see pwi-allele-der-search-14
        """
        driver = self.driver
        #finds the Property list field and select the option Non-mouse_organism , set value to zebrafish and then click the Search button
        Select(driver.find_element(By.ID, "propertyName-0")).select_by_value('string:12948290')
        driver.find_element(By.ID, "value-0").send_keys("zebrafish")
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
        result1 = iterate.getTextAsList(cell1)
        result2 = iterate.getTextAsList(cell2)
        result3 = iterate.getTextAsList(cell3)
        result4 = iterate.getTextAsList(cell4)
        print(result1)
        #Assert the correct relationships are returned
        self.assertEqual(result1, ['Mesp2<tm7.1(mespb)Ysa>'])        
        self.assertEqual(result2, ['Mesp2<tm7(mespb)Ysa>'])
        self.assertEqual(result3, ['Tg(MMTV-Catnb)3Pac'])   
        self.assertEqual(result4, ['Tg(MMTV-Catnb)5Pac'])    

    def testEIAlleleRelationshipsMrkRegionToolSearch(self):
        """
        @Status tests that a basic allele relationships Marker Region Tool search  works 
        @see pwi-allele-der-search-15
        """
        driver = self.driver
        #finds the Allele field and enters text, the Chr,start coordinate, stop coordinate and lastly Relationship Type fields to enter data. tabs out of the fields then clicks the Search button
        driver.find_element(By.ID, "alleleSymbol").send_keys('Qki<qk-v>')
        Select(driver.find_element(By.ID, "chromsome")).select_by_value('string:17')
        driver.find_element(By.ID, "startCoordinate").send_keys('10425400')
        driver.find_element(By.ID, "endCoordinate").send_keys('12282248')
        Select(driver.find_element(By.ID, "relationshipTerm")).select_by_value('string:12438350')
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
        result1 = iterate.getTextAsList(cell1)
        print(result1)
        #Assert the correct relationships are returned
        self.assertEqual(result1, ['Qki<qk-v>'])     

        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEIAlleleRelationshipsSearch))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))                                     