'''
Created on Oct 4, 2016

@author: jeffc
this test was created to verify the proper field are cleared when hitting the Clear button
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

class TestModify(unittest.TestCase):
    """
    @status Test GXD Index browser for the correct fields being cleared
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.PWI_URL + "/edit/gxdindex") 
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
        
        form.enter_value('jnumid', '225216')
        # click the Tab key
        form.press_tab()
        #finds the citation field
        citation = form.get_value('citation')
        print citation
        self.assertEqual(citation, 'Alvarez-Saavedra M, Nat Commun 2014;5():4181')
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
        self.assertEqual(priority, 'Low')
        
        #finds the conditional mutants field
        conditional = form.get_selected_text('_conditionalmutants_key')
        
        print conditional
        self.assertEqual(conditional, 'Conditional')

        #finds the created by field
        created_user = driver.find_element_by_id('createdby_login')
        
        print created_user
        self.assertEqual(created_user.text, 'jfinger')

        
        #finds the modified by field
        modified_user = driver.find_element_by_id('modifiedby_login')#.find_element_by_css_selector('td')
        
        print modified_user
        self.assertEqual(modified_user.text, 'jeffc')
        
        #finds the created by date field
        created_date = form.get_value('creation_date')
        
        print created_date
        self.assertEqual(created_date, '12/11/2015')
        
        #finds the created by date field
        modified_date = form.get_value('modification_date')
        
        print modified_date
        self.assertEqual(modified_date, '10/04/2016')
        
        #find the table field to check
        table_element = driver.find_element_by_id("indexGrid")
        table = Table(table_element)
        #puts an X in the Prot-sxn by age 7.5 box
        cell = table.get_cell("RT-PCR", "A")
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
        created_user = driver.find_element_by_id('createdby_login')
        
        print created_user
        self.assertEqual(created_user.text, '')
        
        #finds the modified by field
        modified_user = driver.find_element_by_id('modifiedby_login')#.find_element_by_css_selector('td')
        
        print modified_user
        self.assertEqual(modified_user.text, '')
        
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
        #puts an X in the Prot-sxn by age 7.5 box
        cell = table.get_cell("RT-PCR", "A")
        #cell.click()
        wait.forAngular(driver)
        self.assertNotEqual(cell.text, 'X', "the cell is not checked")

    def tearDown(self):
        driver = self.driver
        form = self.form
        form.click_clear()
        form.enter_value('jnumid', '225216')
        form.press_tab()
        form.enter_value('marker_symbol', 'Bmp2')
        form.press_tab()
        form.click_search()
        form.click_delete()
        self.driver.close()
       
'''
These tests should NEVER!!!! be run against a production system!!
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAdd))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main() 