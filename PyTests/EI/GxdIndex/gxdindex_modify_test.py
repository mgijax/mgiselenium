'''
Created on Oct 4, 2016

@author: jeffc
@attention: These tests must only be run against a development environment!!!
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
    @status Test GXD Index browser for ability to modify marker and notes data, later will need to verify created and modified by/dates
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
        

    def testModMrk(self):
        """
        @Status tests that an index record Marker symbol can be modified
        
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
        form.enter_value('marker_symbol', 'Bmp4')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print marker_symbol
        self.assertEqual(marker_symbol, 'Bmp4')
        form.click_search()
        self.driver.find_element_by_id('marker_symbol').clear()#clears the marker field
        form.enter_value('marker_symbol', 'Bmp2')#Enter Bmp2 as the marker
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print marker_symbol
        wait.forAngular(driver)
        form.click_modify()
        marker_symbol = form.get_value('marker_symbol')
        print marker_symbol
        #find the table field to check
        table_element = driver.find_element_by_id("indexGrid")
        table = Table(table_element)
        #puts an X in the Prot-sxn by age 7.5 box
        cell = table.get_cell("prot-sxn", "7.5")
        cell.click()
        wait.forAngular(driver)
        self.assertEqual(cell.text, 'X', "the cell is not checked")

        
    def testModNotes(self):
        """
        @Status tests that the notes field can be modified
        
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
        self.driver.find_element_by_id('comments').clear()#clears the notes field
        form.enter_value('comments', 'A test Comment')#Enter a note in the notes field
        marker_symbol = form.get_value('comments')
        form.press_tab()
        print marker_symbol
        wait.forAngular(driver)
        form.click_modify()
        marker_symbol = form.get_value('comments')
        print marker_symbol
        #find the table field to check
        table_element = driver.find_element_by_id("indexGrid")
        table = Table(table_element)
        #puts an X in the Prot-sxn by age 7.5 box
        cell = table.get_cell("prot-sxn", "7.5")
        cell.click()
        wait.forAngular(driver)
        self.assertEqual(cell.text, 'X', "the cell is not checked")


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
These tests should NEVER!!!! be run against a production system!!'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestModify))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main() 
