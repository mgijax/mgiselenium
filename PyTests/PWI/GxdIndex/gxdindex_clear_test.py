'''
Created on Oct 4, 2016
@author: jeffc
this test was created to verify the proper fields are cleared when hitting the Clear button
this test was verified to work on 6/9/2023
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
class TestEiGxdIndexClear(unittest.TestCase):
    """
    @status Test GXD Index browser for the correct fields being cleared
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

    def testClearFields(self):
        """
        @Status tests that when an index record is cleared the correct fields get cleared

        """
        driver = self.driver
        form = self.form
        time.sleep(2)
        form.enter_value('jnumID', '74162')
        # click the Tab key
        form.press_tab()
        # finds the citation field
        citation = form.get_value('short_citation')
        print(citation)
        self.assertEqual(citation, 'Abdelwahid E, Cell Tissue Res 2001 Jul;305(1):67-78')
        # finds the marker field
        form.enter_value('markerSymbol', 'Bmp2')
        marker_symbol = form.get_value('markerSymbol')
        form.press_tab()
        print(marker_symbol)
        self.assertEqual(marker_symbol, 'Bmp2')
        form.click_search()

        # finds the coded? field
        is_coded = form.get_value('isFullCoded')

        print(is_coded)
        self.assertEqual(is_coded, 'string:1')

        # finds the priority field
        priority = form.get_selected_text('priority')

        print(priority)
        self.assertEqual(priority, 'High')

        # finds the conditional mutants field
        conditional = form.get_selected_text('conditional')

        print(conditional)
        self.assertEqual(conditional, 'Not Specified')

        # finds the created by field
        created_user = form.get_value('createdBy')

        print(created_user)
        self.assertEqual(created_user, 'MGI_2.97')

        # finds the modified by field
        modified_user = form.get_value('modifiedBy')  # .find_element_by_css_selector('td')

        print(modified_user)
        self.assertEqual(modified_user, 'MGI_2.97')

        # finds the created by date field
        created_date = form.get_value('creationDate')

        print(created_date)
        self.assertEqual(created_date, '2002-04-23')

        # finds the created by date field
        modified_date = form.get_value('modificationDate')

        print(modified_date)
        self.assertEqual(modified_date, '2002-04-23')

        # find the table field to check
        table_element = driver.find_element(By.ID, "indexGrid")
        table = Table(table_element)
        # get a cell that has been selected for this index record(RNA-sxn/10.5)
        cell = table.get_cell(2, 21)
        # cell.click()
        wait.forAngular(driver)
        self.assertEqual(cell.text, 'X', "the cell is not checked")

        form.click_clear()  # press the clear button
        # finds the citation field
        citation = form.get_value('short_citation')
        print(citation)
        self.assertEqual(citation, '')
        # finds the marker field
        marker_symbol = form.get_value('markerSymbol')
        print(marker_symbol)
        self.assertEqual(marker_symbol, '')
        # finds the coded? field
        is_coded = form.get_value('isFullCoded')
        print(is_coded)
        self.assertEqual(is_coded, '')

        # finds the priority field
        priority = form.get_selected_text('priority')

        print(priority)
        self.assertEqual(priority, 'Search All')

        # finds the conditional mutants field
        conditional = form.get_selected_text('conditional')

        print(conditional)
        self.assertEqual(conditional, 'Search All')

        # finds the created by field
        created_user = form.get_value('createdBy')

        print(created_user)
        self.assertEqual(created_user, '')

        # finds the modified by field
        modified_user = form.get_value('modifiedBy')  # .find_element_by_css_selector('td')

        print(modified_user)
        self.assertEqual(modified_user, '')

        # finds the created by date field
        created_date = form.get_value('creationDate')

        print(created_date)
        self.assertEqual(created_date, '')

        # finds the created by date field
        modified_date = form.get_value('modificationDate')

        print(modified_date)
        self.assertEqual(modified_date, '')

        # find the table field to check
        table_element = driver.find_element(By.ID, "indexGrid")
        table = Table(table_element)
        # look for an X in the first assay/age cell
        cell = table.get_cell(2, 21)

        wait.forAngular(driver)
        self.assertEqual(cell.text, '', "the cell is checked - clear didn't work")

    def tearDown(self):
        driver = self.driver
        driver.quit()
        tracemalloc.stop()


'''
These tests should NEVER!!!! be run against a production system!!'''


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiGxdIndexClear))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))