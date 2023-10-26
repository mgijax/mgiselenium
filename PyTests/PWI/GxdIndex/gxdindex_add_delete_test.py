'''
Created on Sep 20, 2016

@author: jeffc
@attention: These tests must only be run against a development environment!!
@bug: since selenium 4 getting errors for popups(lines 153 and 184), need to find out why!!!!
'''
import unittest
import time
import tracemalloc
import config
import sys, os.path
# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests
tracemalloc.start()
class TestEiGxdIndexAddDelete(unittest.TestCase):
    """
    @status Test GXD Index browser for ability to add an index
    """

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1800, 1000)
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/gxdindex")
        username = self.driver.find_element(By.NAME, 'user')  # finds the user login box
        username.send_keys(config.PWI_LOGIN)  # enters the username
        passwd = self.driver.find_element(By.NAME, 'password')  # finds the password box
        passwd.send_keys(config.PWI_PASSWORD)  # enters a valid password
        submit = self.driver.find_element(By.NAME, "submit")  # Find the Login button
        submit.click()  # click the login button

    def testAddDeleteIndex(self):
        """
        @Status tests that an index record can be added

        """
        driver = self.driver
        form = self.form
        time.sleep(2)
        print("BEGIN testAddIndex")
        form.enter_value('jnumid', '225216')
        # click the Tab key
        form.press_tab()
        # finds the citation field
        citation = form.get_value('citation')
        print(citation)
        self.assertEqual(citation, 'Alvarez-Saavedra M, Nat Commun 2014;5():4181')
        # finds the marker field
        form.enter_value('marker_symbol', 'Bmp2')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print(marker_symbol)
        self.assertEqual(marker_symbol, 'Bmp2')
        # find the table field to check
        table_element = driver.find_element(By.ID, "indexGrid")
        table = Table(table_element)
        # puts an X in the first assay/age cell
        cell = table.get_cell(1, 1)
        cell.click()
        wait.forAngular(driver)
        self.assertEqual(cell.text, 'X', "the cell is not checked")
        form.click_add()  # click the add button
        print("Index record added - now delete it")

        form.click_clear()  # clear the form and start over for delete
        driver = self.driver
        form = self.form

        form.enter_value('jnumid', '225216')
        # click the Tab key
        form.press_tab()
        # finds the citation field
        citation = form.get_value('citation')
        print(citation)
        self.assertEqual(citation, 'Alvarez-Saavedra M, Nat Commun 2014;5():4181')
        # finds the marker field
        form.enter_value('marker_symbol', 'Bmp2')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print(marker_symbol)
        self.assertEqual(marker_symbol, 'Bmp2')
        # find the table field to check
        table_element = driver.find_element(By.ID, "indexGrid")
        table = Table(table_element)
        # puts an X in the first assay/age cell
        cell = table.get_cell(1, 1)
        cell.click()
        wait.forAngular(driver)
        self.assertEqual(cell.text, 'X', "the cell is not checked")
        form.click_search()  # get the record
        form.click_delete()  # click the delete button
        print("Index record deleted")

    def testJnumMrkErrMsgs(self):
        """
        @Status tests that the correct error messages are displayed when entering an invalid J number and when entering an invalid Marker

        """
        driver = self.driver
        form = self.form
        time.sleep(2)
        form.enter_value('jnumid', '000000')
        # click the Tab key
        form.press_tab()
        # Get the error message that is displayed
        jnum_error = form.get_error_message()
        self.assertEqual(jnum_error, "No Reference for J Number=J:000000", 'error message not displayed')
        # finds the marker field
        form.enter_value('marker_symbol', 'ffffff')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print(marker_symbol)
        # Get the error message that is displayed
        mrk_error = form.get_error_message()
        self.assertEqual(mrk_error, 'Invalid marker symbol ffffff')

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
        # finds the marker field
        form.enter_value('marker_symbol', 'zyx')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print(marker_symbol)
        # press the enter key
        driver.find_element(By.ID, "addButton").click()
        wait.forAngular(driver)
        # Get the error message that is displayed
        priority_error = form.get_error_message()
        print(priority_error)
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
        # finds the marker field
        form.enter_value('marker_symbol', 'Gata1')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print(marker_symbol)
        # finds the marker field
        form.enter_value('_priority_key', 'Low')
        priority_option = form.get_value('_priority_key')
        form.press_tab()
        print(priority_option)
        # self.assertEqual(priority_option, '74716')
        # press the enter key
        form.click_add()

        # Get the error message that is displayed
        stage_error = form.get_error_message()
        print(stage_error)
        self.assertEqual(stage_error, 'No stages have been selected for this record')

        table = driver.find_element(By.ID, "resultsTable")
        table.find_elements(By.TAG_NAME, "tr")[1].click()
        wait.forAngular(driver)
        form.click_delete()

    def tearDown(self):
        driver = self.driver
        form = self.form
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiGxdIndexAddDelete))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
