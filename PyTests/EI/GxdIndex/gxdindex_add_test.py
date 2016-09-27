'''
Created on Sep 20, 2016

@author: jeffc
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

class TestAdd(unittest.TestCase):
    """
    @status Test GXD Index browser for ability to add an index
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
        

    def testAddIndex(self):
        """
        @Status tests that an index record can be added
        
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
        #find the table field to check
        table_element = driver.find_element_by_id("indexGrid")
        table = Table(table_element)
        #puts an X in the Prot-sxn by age 7.5 box
        cell = table.get_cell("prot-sxn", "7.5")
        cell.click()
        wait.forAngular(driver)
        self.assertEqual(cell.text, 'X', "the cell is not checked")

        
    def testJnumMrkErrMsgs(self):
        """
        @Status tests that the correct error messages are displayed when entering an invalid J number and when entering an invalid Marker
        
        """
        driver = self.driver
        form = self.form
        form.enter_value('jnumid', '000000')
        # click the Tab key
        form.press_tab()
        #Get the error message that is displayed
        jnum_error = form.get_error_message()
        self.assertEqual(jnum_error, "No Reference for J Number=J:000000", 'error message not displayed')
        #finds the marker field
        form.enter_value('marker_symbol', 'ffffff')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print marker_symbol
        #Get the error message that is displayed
        mrk_error = form.get_error_message()
        self.assertEqual(mrk_error, 'Invalid marker symbol')

    def testPriorityErrMsg(self):
        """
        @Status tests that the correct error message is displayed when not selecting a priority
        
        """
        driver = self.driver
        form = self.form
        wait.forAngular(driver)
        form.enter_value('jnumid', '144307')
        # click the Tab key
        form.press_tab()
        #finds the marker field
        form.enter_value('marker_symbol', 'zyx')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print marker_symbol
        #press the enter key
        driver.find_element_by_id("addButton").click()
        wait.forAngular(driver)
        #Get the error message that is displayed
        priority_error = form.get_error_message()
        print priority_error
        self.assertEqual(priority_error, '(psycopg2.InternalError) Priority Required')

    def testStageErrMsg(self):
        """
        @Status tests that the correct error message is displayed when not selecting any stage
        
        """
        driver = self.driver
        form = self.form
        wait.forAngular(driver, '5')
        form.enter_value('jnumid', '225216')
        # click the Tab key
        form.press_tab()
        #finds the marker field
        form.enter_value('marker_symbol', 'Bmp2')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print marker_symbol
        #finds the marker field
        form.enter_value('_priority_key', 'Low')
        priority_option = form.get_value('_priority_key')
        form.press_tab()
        print priority_option
        self.assertEqual(priority_option, '74716')
        #press the enter key
        driver.find_element_by_id("addButton").click()
        wait.forAngular(driver, '5')
        #Get the error message that is displayed
        stage_error = form.get_error_message()
        print stage_error
        self.assertEqual(stage_error, 'No stages have been selected for this record')    
        

    
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
       
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAdd))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main() 