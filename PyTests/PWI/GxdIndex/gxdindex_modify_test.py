'''
Created on Oct 4, 2016

@author: jeffc
@attention: These tests must only be run against a development environment!!!
'''

import unittest
import time
import tracemalloc
from jd_HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import HtmlTestRunner

import sys, os.path

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table


# Tests
tracemalloc.start()
class TestEiGxdIndexModify(unittest.TestCase):
    """
    @status Test GXD Index browser for ability to modify marker and notes data, later will need to verify created and modified by/dates
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/gxdindex")
        username = self.driver.find_element(By.NAME, 'user')  # finds the user login box
        username.send_keys(config.PWI_LOGIN)  # enters the username
        passwd = self.driver.find_element(By.NAME, 'password')  # finds the password box
        passwd.send_keys(config.PWI_PASSWORD)  # enters a valid password
        submit = self.driver.find_element(By.NAME, "submit")  # Find the Login button
        submit.click()  # click the login button

    def testModMrk(self):
        """
        @Status tests that an index record Marker symbol can be modified

        """
        driver = self.driver
        form = self.form
        time.sleep(2)
        form.enter_value('jnumid', '186289')
        # click the Tab key
        form.press_tab()
        # finds the citation field
        citation = form.get_value('citation')
        print(citation)
        self.assertIn('Brahmaraju', citation)
        # finds the marker field
        form.enter_value('marker_symbol', 'Aire')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print(marker_symbol)
        form.click_search()

        table_element = driver.find_element(By.ID, "indexGrid")
        table = Table(table_element)
        # puts an X in the first assay/second age cell
        cell = table.get_cell(1, 2)
        cell.click()
        wait.forAngular(driver)
        self.assertEqual(cell.text, 'X', "the cell is not checked")
        wait.forAngular(driver)
        # Modify record to add another age
        form.click_modify()
        print("MODIFY worked - now modify again to remove so the test works the next time")

        form.click_clear()
        form.enter_value('jnumid', '186289')
        # click the Tab key
        form.press_tab()
        # finds the citation field
        citation = form.get_value('citation')
        print(citation)
        self.assertIn('Brahmaraju', citation)
        # finds the marker field
        form.enter_value('marker_symbol', 'Aire')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print(marker_symbol)
        form.click_search()

        # removes an X in the first assay/second age cell
        cell = table.get_cell(1, 2)
        cell.click()
        wait.forAngular(driver)
        self.assertEqual(cell.text, '', "the cell is checked - expecting it to be empty")
        wait.forAngular(driver)
        # Modify record to add another age
        form.click_modify()
        print("2nd MODIFY done - to remove change added")

    def testModNotes(self):
        """
        @Status tests that the notes field can be modified

        """
        driver = self.driver
        form = self.form
        time.sleep(2)
        form.enter_value('jnumid', '225216')
        # click the Tab key
        form.press_tab()
        # finds the citation field
        citation = form.get_value('citation')
        print(citation)
        self.assertEqual(citation, 'Alvarez-Saavedra M, Nat Commun 2014;5():4181')
        # finds the marker field
        form.enter_value('marker_symbol', 'Atoh1')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print(marker_symbol)
        self.assertEqual(marker_symbol, 'Atoh1')
        form.click_search()
        self.driver.find_element(By.ID, 'comments').clear()  # clears the notes field
        form.enter_value('comments', 'A test Comment')  # Enter a note in the notes field
        marker_symbol = form.get_value('comments')
        form.press_tab()

        form.click_modify()

    def tearDown(self):
        self.driver.quit()


'''
These tests should NEVER!!!! be run against a production system!!'''


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiGxdIndexModify))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))