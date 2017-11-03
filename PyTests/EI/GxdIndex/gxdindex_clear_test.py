'''
Created on Oct 4, 2016

@author: jeffc
this test was created to verify the proper field are cleared when hitting the Clear button
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import HTMLTestRunner

import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table



# Tests

class TestClear(unittest.TestCase):
    """
    @status Test GXD Index browser for the correct fields being cleared
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/gxdindex") 
        username = self.driver.find_element_by_name('user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = self.driver.find_element_by_name('password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = self.driver.find_element_by_name("submit") #Find the Login button
        submit.click() #click the login button
        

    def testClearFields(self):
        """
        @Status tests that when an index record is cleared the correct fields get cleared
        
        """
        driver = self.driver
        form = self.form
        
        form.enter_value('jnumid', '74162')
        # click the Tab key
        form.press_tab()
        #finds the citation field
        citation = form.get_value('citation')
        print citation
        self.assertEqual(citation, 'Abdelwahid E, Cell Tissue Res 2001 Jul;305(1):67-78')
        #finds the marker field
        form.enter_value('marker_symbol', 'Bmp2')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print marker_symbol
        self.assertEqual(marker_symbol, 'Bmp2')
        form.click_search()
        
        #finds the coded? field
        is_coded = form.get_value('is_coded')
        
        print is_coded
        self.assertEqual(is_coded, 'false')
        
        #finds the priority field
        priority = form.get_selected_text('_priority_key')
        
        print priority
        self.assertEqual(priority, 'High')
        
        #finds the conditional mutants field
        conditional = form.get_selected_text('_conditionalmutants_key')
        
        print conditional
        self.assertEqual(conditional, 'Not Specified')

        #finds the created by field
        created_user = form.get_value('createdby_login')
        
        print created_user
        self.assertEqual(created_user, 'MGI_2.97')

        
        #finds the modified by field
        modified_user = form.get_value('modifiedby_login')#.find_element_by_css_selector('td')
        
        print modified_user
        self.assertEqual(modified_user, 'MGI_2.97')
        
        #finds the created by date field
        created_date = form.get_value('creation_date')
        
        print created_date
        self.assertEqual(created_date, '04/23/2002')
        
        #finds the created by date field
        modified_date = form.get_value('modification_date')
        
        print modified_date
        self.assertEqual(modified_date, '04/23/2002')
        
        #find the table field to check
        table_element = driver.find_element_by_id("indexGrid")
        table = Table(table_element)
        #get a cell that has been selected for this index record
        cell = table.get_cell(2,21)
        #cell.click()
        wait.forAngular(driver)
        self.assertEqual(cell.text, 'X', "the cell is not checked")
        
        form.click_clear()#press the clear button
        #finds the citation field
        citation = form.get_value('citation')
        print citation
        self.assertEqual(citation, '')
        #finds the marker field
        marker_symbol = form.get_value('marker_symbol')
        print marker_symbol
        self.assertEqual(marker_symbol, '')
        #finds the coded? field
        is_coded = form.get_value('is_coded')
        print is_coded
        self.assertEqual(is_coded, '')
        
        #finds the priority field
        priority = form.get_selected_text('_priority_key')
        
        print priority
        self.assertEqual(priority, 'Search All')
        
        #finds the conditional mutants field
        conditional = form.get_selected_text('_conditionalmutants_key')
        
        print conditional
        self.assertEqual(conditional, 'Search All')

        #finds the created by field
        created_user = form.get_value('createdby_login')
        
        print created_user
        self.assertEqual(created_user, '')
        
        #finds the modified by field
        modified_user = form.get_value('modifiedby_login')#.find_element_by_css_selector('td')
        
        print modified_user
        self.assertEqual(modified_user, '')
        
        #finds the created by date field
        created_date = form.get_value('creation_date')
        
        print created_date
        self.assertEqual(created_date, '')
        
        #finds the created by date field
        modified_date = form.get_value('modification_date')
        
        print modified_date
        self.assertEqual(modified_date, '')
        
        #find the table field to check
        table_element = driver.find_element_by_id("indexGrid")
        table = Table(table_element)
        #look for an X in the first assay/age cell
        cell = table.get_cell(2,21)
  
        wait.forAngular(driver)
        self.assertEqual(cell.text, '', "the cell is checked - clear didn't work")

    def tearDown(self):
        driver = self.driver
        driver.close()
       
'''
These tests should NEVER!!!! be run against a production system!!'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestClear))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main() 