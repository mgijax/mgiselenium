'''
Created on Oct 30, 2018

These tests verify searching within the Marker module.

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
from symbol import sym_name
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table




# Tests

class TestEiMrkSearchHistory(unittest.TestCase):
    """
    @status Test Marker History search fields
    """

    def setUp(self):
        self.driver = webdriver.Firefox() 
        #self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/marker")
    
    def tearDown(self):
        self.driver.close()
        
    def testSymbolHistorySearch(self):
        """
        @Status tests that a basic Marker History Symbol search works
        @see pwi-mrk-det-hist-search-1
        """
        driver = self.driver
        #finds the history symbol field and enters a symbol
        driver.find_element(By.ID, "historySymbol-0").send_keys('Dsh')
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'historySymbol-2')))
        # get the data for the Symbol column for all 9 rows
        hist_sym = driver.find_element(By.ID, 'historySymbol-0').get_attribute('value')  
        hist_sym1 = driver.find_element(By.ID, 'historySymbol-1').get_attribute('value') 
        hist_sym2 = driver.find_element(By.ID, 'historySymbol-2').get_attribute('value') 
        hist_sym3 = driver.find_element(By.ID, 'historySymbol-3').get_attribute('value') 
        hist_sym4 = driver.find_element(By.ID, 'historySymbol-4').get_attribute('value') 
         
        print(hist_sym)
        print(hist_sym4)     
        #Assert the second synonym date returned(row2) is correct
        self.assertEqual(hist_sym, 'Hhg1')      
        self.assertEqual(hist_sym1, 'Hhg1') 
        self.assertEqual(hist_sym2, 'Shh') 
        self.assertEqual(hist_sym3, 'Dsh') 
        self.assertEqual(hist_sym4, 'Dsh') 
        
    def testSymbolHistoryWildSearch(self):
        """
        @Status tests that a basic Marker History Symbol search with a wildcard works
        @see pwi-mrk-det-hist-search-2
        """
        driver = self.driver
        #finds the history symbol field and enters a symbol
        driver.find_element(By.ID, "historySymbol-0").send_keys('Pax%')
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'synonymModification_date-2')))
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
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
        print(cell2.text)
        print(cell3.text)
        print(cell4.text)
        print(cell5.text)
        #Assert the correct genotype has been returned in the results table
        self.assertEqual(cell0.text, 'Pax1')
        self.assertEqual(cell1.text, 'Pax2')
        self.assertEqual(cell2.text, 'Pax3') 
        self.assertEqual(cell3.text, 'Pax4') 
        self.assertEqual(cell4.text, 'Pax5') 
        self.assertEqual(cell5.text, 'Pax6')   
        
    def testNameHistorySearch(self):
        """
        @Status tests that a basic Marker History Name search works
        @see pwi-mrk-det-hist-search-3
        """
        driver = self.driver
        #finds the history name field and enters a name
        driver.find_element(By.ID, "historyName-0").send_keys('sonic hedgehog')
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'historySymbol-2')))
        #time.sleep(2)
        # get the data for the Symbol column for all 9 rows
        hist_sym = driver.find_element(By.ID, 'historySymbol-0').get_attribute('value')  
        hist_sym1 = driver.find_element(By.ID, 'historySymbol-1').get_attribute('value') 
        hist_sym2 = driver.find_element(By.ID, 'historySymbol-2').get_attribute('value') 
        hist_sym3 = driver.find_element(By.ID, 'historySymbol-3').get_attribute('value') 
        hist_sym4 = driver.find_element(By.ID, 'historySymbol-4').get_attribute('value') 
          
        print(hist_sym)
        print(hist_sym4)     
        #Assert the second synonym date returned(row2) is correct
        self.assertEqual(hist_sym, 'Hhg1')      
        self.assertEqual(hist_sym1, 'Hhg1') 
        self.assertEqual(hist_sym2, 'Shh') 
        self.assertEqual(hist_sym3, 'Dsh') 
        self.assertEqual(hist_sym4, 'Dsh') 

        
    def testNameHistoryWildSearch(self):
        """
        @Status tests that a basic Marker History Name search with a wildcard works
        @see pwi-mrk-det-hist-search-4
        """
        driver = self.driver
        #finds the history symbol field and enters a symbol
        driver.find_element(By.ID, "historyName-0").send_keys('splotch-like%')
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'synonymModification_date-1')))
        #time.sleep(2)
        # get the data for the Symbol column for all 9 rows
        hist_sym = driver.find_element(By.ID, 'historySymbol-0').get_attribute('value')  
        hist_sym1 = driver.find_element(By.ID, 'historySymbol-1').get_attribute('value') 
        hist_sym2 = driver.find_element(By.ID, 'historySymbol-2').get_attribute('value') 
        hist_sym3 = driver.find_element(By.ID, 'historySymbol-3').get_attribute('value') 
        hist_sym4 = driver.find_element(By.ID, 'historySymbol-4').get_attribute('value') 
        hist_sym5 = driver.find_element(By.ID, 'historySymbol-5').get_attribute('value') 
        hist_sym6 = driver.find_element(By.ID, 'historySymbol-6').get_attribute('value') 
        print(hist_sym)
        print(hist_sym6)     
        #Assert the second synonym date returned(row2) is correct
        self.assertEqual(hist_sym, 'Pax-3')      
        self.assertEqual(hist_sym1, 'Pax-3') 
        self.assertEqual(hist_sym2, 'Pax3') 
        self.assertEqual(hist_sym3, 'Sp') 
        self.assertEqual(hist_sym4, 'Sp') 
        self.assertEqual(hist_sym5, 'Splchl2') 
        self.assertEqual(hist_sym6, 'Splchl2') 
        
    def testDateHistorySearch(self):
        """
        @Status tests that a basic Marker History Date search works
        @see pwi-mrk-det-hist-search-5
        """
        driver = self.driver
        #finds the history name field and enters a name
        driver.find_element(By.ID, "historyEventDate-0").send_keys('2018-09-20')
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'historyName-0')))
        time.sleep(2)
        #capture the results table rows
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        symbl1 = table.get_row(0)
        symbl2 = table.get_row(1)
        symbl3 = table.get_row(2)
        print(symbl2.text)
        print(symbl3.text)  
        #Assert the first 6 results are correct
        self.assertEqual(symbl1.text, 'Shs')      
        self.assertEqual(symbl2.text, 'Tg(CAG-MYC,-GFP*)#Rugg') 
        self.assertEqual(symbl3.text, 'Tg(Rho-GSTP1)#Psbe') 

    def testJnumHistorySearch(self):
        """
        @Status tests that a basic Marker History J number search works
        @see pwi-mrk-det-hist-search-6
        """
        driver = self.driver
        #finds the J# field and enters a J number
        driver.find_element(By.ID, "historyJnum-0").send_keys('J:2944')
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'historyName-0')))
        time.sleep(2)
        #capture the results table rows
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        symbl1 = table.get_row(0)
        symbl2 = table.get_row(1)
        print(symbl1.text)
        print(symbl2.text)  
        #Assert the first 6 results are correct
        self.assertEqual(symbl1.text, 'Pax3')      
        self.assertEqual(symbl2.text, 'Del(1)3H') 

    def testJnumHistorySearch2(self):
        """
        @Status tests that a basic Marker History J number search works when the J: is not added
        @see pwi-mrk-det-hist-search-6
        """
        driver = self.driver
        #finds the J# field and enters a J number
        driver.find_element(By.ID, "historyJnum-0").send_keys('2944')
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'historyName-0')))
        time.sleep(2)
        #capture the results table rows
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        symbl1 = table.get_row(0)
        symbl2 = table.get_row(1)
        print(symbl1.text)
        print(symbl2.text)  
        #Assert the first 6 results are correct
        self.assertEqual(symbl1.text, 'Pax3')      
        self.assertEqual(symbl2.text, 'Del(1)3H') 

    """def testCitationHistorySearch(self):
        
        @Status tests that a basic Marker History Citation search works
        @see pwi-mrk-det-hist-search-8 Currently can't search by citation 2019-11-15
        
        driver = self.driver
        #finds the Citation field and enters a citation string
        driver.find_element(By.ID, "historyShortCitation-0").send_keys('Balling R, Cell 1988 Nov 4;55(3):531-5')
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'historyName-0')))
        # get the data for the Citation column, print the row 6 result
        cite_row = driver.find_element(By.ID, 'historyShortCitation-5').get_attribute('value')        
        #Assert the sixth citation returned(row6) is correct
        self.assertEqual(cite_row, 'Balling R, Cell 1988 Nov 4;55(3):531-5')      
        #capture the results table row
        symbl1 = driver.find_element(By.XPATH, '/html/body/main/div[1]/div/form/div/div/div[2]/div[5]/div/div[2]/table/tbody/tr[1]/td').get_attribute('innerText')
        print symbl1
        #Assert the first result is correct
        self.assertEqual(symbl1, 'Pax1') """     


    """def testCitationHistoryWildcardSearch(self):
        
        @Status tests that a basic Marker History Citation search with wildcard works
        @see pwi-mrk-det-hist-search-9 Currently can't search by citation 2019-11-15
        
        driver = self.driver
        #finds the Citation field and enters a citation string
        driver.find_element(By.ID, "historyShortCitation-0").send_keys('Selby P%')
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'historyName-0')))
        # get the data for the Citation column, print the row 6 result
        cite_row = driver.find_element(By.ID, 'historyShortCitation-5').get_attribute('value')        
        #Assert the sixth citation returned(row6) is correct
        self.assertEqual(cite_row, 'Selby P, Mouse News Lett 1985;72():123')      
        #capture the results table row
        symbl1 = driver.find_element(By.XPATH, '/html/body/main/div[1]/div/form/div/div/div[2]/div[5]/div/div[2]/table/tbody/tr[1]/td').get_attribute('innerText')
        print symbl1
        #Assert the first result is correct
        self.assertEqual(symbl1, 'Ccd') """

    def testHistoryEventNotSpecifiedSearch(self):
        """
        @Status tests that a basic Marker History Event of Not Specified search works
        @see pwi-mrk-det-hist-search-10
        """
        driver = self.driver
        #finds the Event field and selects the option "Not Specified"
        Select(driver.find_element(By.ID, "historyEvent-0")).select_by_value('string:106563602')#equals "not specified"
        driver.find_element(By.ID, 'searchButton').click() 
        #finds the Event Reason field and selects the option "not specified"
        Select(driver.find_element(By.ID, "historyEventReason-0")).select_by_value('string:106563610')#string:106563610 is option "not specified"       
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'historyName-0')))
        time.sleep(2)
        # get the data for the Event column, print the row 1 result
        evt_row = driver.find_element(By.ID, 'historyEvent-0').get_attribute('value')        
        #Assert the sixth citation returned(row6) is correct
        self.assertEqual(evt_row, 'string:106563602')#string:106563602 equals 'Not Specified'      
        #capture the results table row
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        symbl1 = table.get_row(0)        
        print(symbl1.text)                 
        #Assert the first result is correct
        self.assertEqual(symbl1.text, 'Uqcc5') 

    def testHistoryEventSplitSearch(self):
        """
        @Status tests that a basic Marker History Event of Split search works
        @see pwi-mrk-det-hist-search-11
        """
        driver = self.driver
        #finds the Event field and selects the option "Split"
        Select(driver.find_element(By.ID, "historyEvent-0")).select_by_value('string:106563608')#string:5 is 'split'
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'historyName-0')))
        time.sleep(2)
        # get the data for the Event column, print the row 6 result
        evt_row = driver.find_element(By.ID, 'historyEvent-5').get_attribute('value')        
        #Assert the sixth citation returned(row6) is correct
        self.assertEqual(evt_row, 'string:106563608')#string:106563608 equals 'Split'      

    def testHistoryEventReasonSearch(self):
        """
        @Status tests that a basic Marker History Event Reason search works
        @see pwi-mrk-det-hist-search-12
        """
        driver = self.driver
        #finds the Event Reason field and selects the option "personal comm w/expert"
        Select(driver.find_element(By.ID, "historyEventReason-0")).select_by_value('string:106563618')#string:106563618 is option "personal comm w/expert"
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'historyName-1')))
        time.sleep(2)
        reason_row = driver.find_element(By.ID, 'historyEventReason-2').get_attribute('value')        
        #Assert the third row returned is correct
        self.assertEqual(reason_row, 'string:106563618')#string:106563615 equals 'personal comm w/Expert'  
        #capture the results table row
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        symbl1 = table.get_row(0)
        print(symbl1.text)
        #Assert the first result is correct
        self.assertEqual(symbl1.text, 'Ak6') 
        
    def testHistoryModBySearch(self):
        """
        @Status tests that a basic Marker History Modified by search works
        @see pwi-mrk-det-hist-search-13
        """
        driver = self.driver
        #finds the Modified By field and enters a search name
        driver.find_element(By.ID, "historyModifiedBy-0").send_keys('hjd')
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'historyName-1')))
        time.sleep(2)
        mod_row = driver.find_element(By.ID, 'historyModifiedBy-4').get_attribute('value')        
        #Assert the fifth row returned is correct
        self.assertEqual(mod_row, 'hjd')#string:4 equals 'personal comm w/Expert'  
        #capture the results table row
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        symbl1 = table.get_row(0)
        symbl2 = table.get_row(1)
        symbl3 = table.get_row(2)
        symbl4 = table.get_row(3)
        symbl5 = table.get_row(4)
        print(symbl1.text)
        print(symbl2.text) 
        print(symbl3.text)
        print(symbl4.text) 
        print(symbl5.text)
        #Assert the first result is correct
        self.assertEqual(symbl1.text, 'Cdk12') 
        self.assertEqual(symbl2.text, 'Esd')
        self.assertEqual(symbl3.text, 'Hat1')
        self.assertEqual(symbl4.text, 'Kdm3b')
        self.assertEqual(symbl5.text, 'Kdm6b')
       
    def testHistoryModByWildcardSearch(self):
        """
        @Status tests that a basic Marker History Modified by search with wildcard works
        @see pwi-mrk-det-hist-search-14
        """
        driver = self.driver
        #finds the Modified By field and enters a search name with wildcard
        driver.find_element(By.ID, "historyModifiedBy-0").send_keys('hj%')
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'historyName-1')))
        time.sleep(2)
        mod_row = driver.find_element(By.ID, 'historyModifiedBy-4').get_attribute('value')        
        #Assert the fifth row returned is correct
        self.assertEqual(mod_row, 'hjd')#string:4 equals 'personal comm w/Expert'  
        #capture the results table row
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        symbl1 = table.get_row(0)
        symbl2 = table.get_row(1)
        symbl3 = table.get_row(2)
        symbl4 = table.get_row(3)
        symbl5 = table.get_row(4)
        print(symbl1.text)
        print(symbl2.text) 
        print(symbl3.text)
        print(symbl4.text) 
        print(symbl5.text)
        #Assert the first result is correct
        self.assertEqual(symbl1.text, 'Cdk12') 
        self.assertEqual(symbl2.text, 'Esd')
        self.assertEqual(symbl3.text, 'Hat1')
        self.assertEqual(symbl4.text, 'Kdm3b')
        self.assertEqual(symbl5.text, 'Kdm6b')
        

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiMrkSearchHistory))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
            
