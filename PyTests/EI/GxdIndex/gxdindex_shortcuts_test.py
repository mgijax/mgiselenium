'''
Created on Oct 25, 2016

@author: jeffc
this test was created to verify the proper operation of the shortcut key options
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import HtmlTestRunner
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table
from util.TestResultUtility import Report


# Tests

class TestEiGxdIndexShortcuts(unittest.TestCase):
    """
    @status Test GXD Index browser for the correct fields being cleared
    @attention: This will only work on the Chrome browser. Only contains 2 shortcut tests, others can be added later as time permits
    """

    def setUp(self):
        self.report = Report()
        self.report.WriteReportHeader()
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/gxdindex") 
        username = self.driver.find_element(By.NAME, 'user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = self.driver.find_element(By.NAME, 'password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = self.driver.find_element(By.NAME, "submit") #Find the Login button
        submit.click() #click the login button
        

    def testCtrlAltc(self):
        """
        @Status tests that when an index record is cleared using Ctrl+Alt+c the correct fields are cleared
        
        """
        driver = self.driver
        form = self.form
        time.sleep(2)
        action = ActionChains(self.driver)
        form.enter_value('jnumID','74162')
        # click the Tab key
        form.press_tab()
        #finds the citation field
        citation = form.get_value('short_citation')
        print(citation)
        try:
            self.assertEqual(citation, 'Abdelwahid E, Cell Tissue Res 2001 Jul;305(1):67-78')
            self.report.AppendToReport("gxdIdx1-0", "testctrrlaltc", "citation text displays", "correct citation text displays", citation, "Pass", "")
        except Exception:
            self.report.AppendToReport("gxdIdx1-0", "testctrrlaltc", "citation text displays", "correct citation text displays", citation, "Fail", "")
        #finds the marker field
        form.enter_value('markerSymbol', 'Bmp2')
        marker_symbol = form.get_value('markerSymbol')
        form.press_tab()
        print(marker_symbol)
        try:
            self.assertEqual(marker_symbol, 'Bmp2')
            self.report.AppendToReport("gxdIdx1-1", "testctrrlaltc", "marker symbol displays", "correct marker symbol displays", "symbol is ", "Pass", "")
        except Exception:
            self.report.AppendToReport("gxdIdx1-1", "testctrrlaltc", "marker symbol displays", "correct marker symbol displays", "symbol is ", "Fail", "")
        form.click_search()
        time.sleep(2)
        action.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('c').key_up(Keys.CONTROL).key_up(Keys.ALT).perform()
        time.sleep(5)
        #finds the citation field
        citation = form.get_value('short_citation')
        print(citation)
        self.assertEqual(citation, '')
        #finds the marker field
        marker_symbol = form.get_value('markerSymbol')
        print(marker_symbol)
        self.assertEqual(marker_symbol, '')
        #finds the coded? field
        is_coded = form.get_value('isFullCoded')
        
        print(is_coded)
        self.assertEqual(is_coded, '')
        #finds the priority field
        priority = form.get_selected_text('priority') 
        print(priority)
        self.assertEqual(priority, 'Search All')
        #finds the conditional mutants field
        conditional = form.get_selected_text('conditional')
        print(conditional)
        self.assertEqual(conditional, 'Search All')
        #finds the created by field
        created_user = form.get_value('createdBy')
        print(created_user)
        self.assertEqual(created_user, '')
        #finds the modified by field
        modified_user = form.get_value('modifiedBy')#.find_element_by_css_selector('td')
        print(modified_user)
        self.assertEqual(modified_user, '')
        #finds the created by date field
        created_date = form.get_value('creationDate')
        print(created_date)
        self.assertEqual(created_date, '')
        #finds the created by date field
        modified_date = form.get_value('modificationDate')
        print(modified_date)
        self.assertEqual(modified_date, '')
        #find the table field to check
        table_element = driver.find_element(By.ID, "indexGrid")
        table = Table(table_element)
        #verifies there is no X in the RNA-sxn by age 10.5 box
        cell = table.get_cell(2, 21)
        #cell.click()
        wait.forAngular(driver)
        self.assertEqual(cell.text, '', "the cell is checked")
        
    def testCtrlAlts(self):
        """
        @Status tests that when a reference is entered then Ctrl+Alt+s is pressed the correct results are returned
        
        """
        driver = self.driver
        form = self.form
        time.sleep(2)
        actions = ActionChains(self.driver)
        form.enter_value('jnumID', '124809')
        # click the Tab key
        form.press_tab()
        #finds the citation field
        citation = form.get_value('short_citation')
        print(citation)
        try:
            self.assertEqual(citation, 'Cheong N, J Biol Chem 2007 Aug 17;282(33):23811-7')
            self.report.AppendToReport("gxdIdx1-2", "testctrrlalts", "Citation is displayed", "correct citation displays", "citation is ", "Pass", "")
        except Exception:
            self.report.AppendToReport("gxdIdx1-2", "testctrrlalts", "Citation is displayed", "correct citation displays", "citation is ", "Fail", "")
        actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('s').key_up(Keys.CONTROL).key_up(Keys.ALT).perform()
        time.sleep(5)
        #finds the citation field
        citation = form.get_value('short_citation')
        print(citation)
        self.assertEqual(citation, 'Cheong N, J Biol Chem 2007 Aug 17;282(33):23811-7')
        #finds the marker field
        marker_symbol = form.get_value('markerSymbol')
        print(marker_symbol)
        self.assertEqual(marker_symbol, 'Abca3')
        #finds the coded? field
        is_coded = form.get_value('isFullCoded')        
        print(is_coded)
        self.assertEqual(is_coded, 'string:0')#No option
        #finds the priority field
        priority = form.get_selected_text('priority') 
        print(priority)
        self.assertEqual(priority, 'Medium')
        #finds the conditional mutants field
        conditional = form.get_selected_text('conditional')
        print(conditional)
        self.assertEqual(conditional, 'Not Specified')
        #finds the created by field
        created_user = form.get_value('createdBy')
        print(created_user)
        self.assertEqual(created_user, 'terryh')
        #finds the modified by field
        modified_user = form.get_value('modifiedBy')#.find_element_by_css_selector('td')
        print(modified_user)
        self.assertEqual(modified_user, 'terryh')
        #finds the created by date field
        created_date = form.get_value('creationDate')
        print(created_date)
        self.assertEqual(created_date, '2007-10-01')
        #finds the created by date field
        modified_date = form.get_value('modificationDate')
        print(modified_date)
        self.assertEqual(modified_date, '2007-10-01')
        #find the table field to check
        table_element = driver.find_element(By.ID, "indexGrid")
        table = Table(table_element)
        #verifies there is an X in the Prot-sxn by age 18.5 box
        cell = table.get_cell(1, 37)
        wait.forAngular(driver)
        self.assertEqual(cell.text, 'X', "the cell is checked")   

    def tearDown(self):

        self.report.WriteReportFooter()
        self.report.WriteToFile("GXDIndexEITestResults.html")
        self.driver.quit()
       
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiGxdIndexShortcuts))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests')) 