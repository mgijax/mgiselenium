'''
Created on Feb 1, 2019
Tests the update and delete features for the Marker History table(none of these tests are ready to use right now!!!!)
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
import sys, os.path

# from builtins import True
# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table


# Tests

class TestEiMrkUpdateDeleteHistory(unittest.TestCase):
    """
    @status Test Marker History update and delete fields
    """

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/marker")
        username = self.driver.find_element(By.NAME, 'user')  # finds the user login box
        username.send_keys(config.PWI_LOGIN)  # enters the username
        passwd = self.driver.find_element(By.NAME, 'password')  # finds the password box
        passwd.send_keys(config.PWI_PASSWORD)  # enters a valid password
        submit = self.driver.find_element(By.NAME, "submit")  # Find the Login button
        submit.click()  # click the login button

    def tearDown(self):
        self.driver.close()

    #    def testSymbolHistoryAdd(self):
    #        """
    #        @Status tests that marker history add feature works
    #        @see pwi-mrk-det-hist-add-1 broken!!!!3/20/2020
    #        """
    #        driver = self.driver
    # finds the history symbol field and enters a symbol
    #        driver.find_element(By.ID, "historySymbol-0").send_keys('Shh')
    #        driver.find_element(By.ID, 'searchButton').click()
    # waits until the element is located or 10 seconds
    #        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'historyName-1')))
    #        time.sleep(2)
    # get the data for the Symbol column for certain rows
    #        hist_sym = driver.find_element(By.ID, 'historySymbol-0').get_attribute('value')
    #        hist_sym8 = driver.find_element(By.ID, 'historySymbol-8').get_attribute('value')
    #        print(hist_sym)
    #        print(hist_sym8)
    # Assert the second synonym date returned(row2) is correct
    #        self.assertEqual(hist_sym, 'Hhg1')
    #        self.assertEqual(hist_sym8, 'Hxl3')
    # Find and click the History Add button
    #        driver.find_element(By.ID, "addHistoryButton").click()
    #        time.sleep(2)
    # find the Event pulldown list
    #        Select(driver.find_element(By.ID, 'historyEvent'))
    #
    #        driver.find_element(By.ID, 'historySymbol-9').clear()
    #        time.sleep(2)
    # find the add history Symbol field and enter your symbol
    #        driver.find_element(By.ID, 'historySymbol-9').send_keys('Dsh')
    # find the add history Name field and enter your name
    #        driver.find_element(By.ID, 'historyName-8').send_keys('test')
    #        driver.find_element(By.ID, 'historyJnum-9').clear()
    # find the add history J number field and enter your J number
    #        driver.find_element(By.ID, 'historyJnum-9').send_keys('J:2300')
    # find the Event field and select assigned
    #        Select(driver.find_element(By.ID, 'historyEvent')).select_by_visible_text('assigned')
    # find the Reason field and select Not Specified
    #        Select(driver.find_element(By.ID, 'historyEventReason')).select_by_visible_text('Not Specified')
    #        time.sleep(5)
    # Find and click the modify button
    #        driver.find_element(By.ID, 'updateMarkerButton').click()
    #        time.sleep(5)
    # get the data for the Symbol column for certain rows
    #        hist_sym = driver.find_element(By.ID, 'historySymbol-0').get_attribute('value')
    #        hist_sym9 = driver.find_element(By.ID, 'historySymbol-9').get_attribute('value')
    #        print(hist_sym)
    #        print(hist_sym9)
    #        #Assert the second synonym date returned(row2) is correct
    #        self.assertEqual(hist_sym, 'Hhg1')
    #        self.assertEqual(hist_sym9, 'Dsh')
    #        #now lets put the symbol back to it's original.
    #        driver.find_element(By.ID, 'deleteRow-9').click()
    #        time.sleep(2)
    # find all the history symbols in the history table and print to screen
    #        i=0
    #        while True:
    #            try:
    #                ele = self.driver.find_element(By.ID, 'historySymbol-' + str(i))
    #                print(ele.get_attribute('value'))
    #                i += 1
    #            except:
    #                break
    #        #find the Modify button and click it
    #        driver.find_element(By.ID, 'updateMarkerButton').click()

    def testSymbolHistoryUpdate(self):
        """
        @Status tests that marker history symbol can be modified
        @see pwi-mrk-det-hist-update-1

        """
        driver = self.driver
        # finds the history symbol field and enters a symbol
        driver.find_element(By.ID, "historySymbol-0").send_keys('Dsh')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)

        # find all the history symbols in the history table and print to screen
        i = 0
        while True:
            try:
                ele = self.driver.find_element(By.ID, 'historySymbol-' + str(i))
                print(ele.get_attribute('value'))
                i += 1
            except:
                break
        # find the last(9th) row symbol and change it from Hxl3 to Hx
        driver.find_element(By.ID, 'historySymbol-8').clear()
        time.sleep(2)
        driver.find_element(By.ID, 'historySymbol-8').send_keys('Hx')
        driver.find_element(By.ID, 'historySymbol-8').send_keys(Keys.TAB)
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()
        time.sleep(2)
        # find the symbol column for the last(9th) symbol and verify it is now Hx
        last_sym = driver.find_element(By.ID, 'historySymbol-8').get_attribute('value')
        # waits until the element is located or 10 seconds
        # WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value((By.ID, 'historySymbol-8', 'Hx')))
        self.assertEqual(last_sym, 'Hx')
        # now lets put the symbol back to it's original.
        driver.find_element(By.ID, 'historySymbol-8').clear()
        time.sleep(2)
        driver.find_element(By.ID, 'historySymbol-8').send_keys('Hxl3')
        driver.find_element(By.ID, 'historySymbol-8').send_keys(Keys.TAB)
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()

    def testNameHistoryModify(self):
        """
        @Status tests that a basic Marker History Name can be modified
        @see pwi-mrk-det-hist-update-3
        """
        driver = self.driver
        # finds the history name field and enters a name
        driver.find_element(By.ID, "historyName-0").send_keys('sonic hedgehog')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # find the symbol column of the history table for the first 9 results
        symname1 = driver.find_element(By.ID, 'historyName-0').get_attribute('value')
        symname2 = driver.find_element(By.ID, 'historyName-1').get_attribute('value')
        symname3 = driver.find_element(By.ID, 'historyName-2').get_attribute('value')
        symname4 = driver.find_element(By.ID, 'historyName-3').get_attribute('value')
        symname5 = driver.find_element(By.ID, 'historyName-4').get_attribute('value')
        symname6 = driver.find_element(By.ID, 'historyName-5').get_attribute('value')
        symname7 = driver.find_element(By.ID, 'historyName-6').get_attribute('value')
        symname8 = driver.find_element(By.ID, 'historyName-7').get_attribute('value')
        symname9 = driver.find_element(By.ID, 'historyName-8').get_attribute('value')
        # assert that the symbols are correct and in the correct order
        self.assertEqual(symname1, 'hedgehog gene 1')
        self.assertEqual(symname2, 'hedgehog gene 1')
        self.assertEqual(symname3, 'sonic hedgehog')
        self.assertEqual(symname4, 'short digits')
        self.assertEqual(symname5, 'short digits')
        self.assertEqual(symname6, 'hemimelic extra toes')
        self.assertEqual(symname7, 'hemimelic extra toes')
        self.assertEqual(symname8, 'hemimelic extratoes like 3')
        self.assertEqual(symname9, 'hemimelic extratoes like 3')
        # find the fourth row symbol name and change it from short digits to short digits testing
        driver.find_element(By.ID, 'historyName-3').clear()
        time.sleep(2)
        driver.find_element(By.ID, 'historyName-3').send_keys('short digits testing')
        driver.find_element(By.ID, 'historyName-3').send_keys(Keys.TAB)
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()
        time.sleep(2)
        # find the symbol name column for the 4th symbol and verify it is now short digits testing
        symname4 = driver.find_element(By.ID, 'historyName-3').get_attribute('value')
        # waits until the element is located or 10 seconds
        # WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value((By.ID, 'historySymbol-8', 'Hx')))
        self.assertEqual(symname4, 'short digits testing')
        # now lets put the symbol name back to it's original.
        driver.find_element(By.ID, 'historyName-3').clear()
        time.sleep(2)
        driver.find_element(By.ID, 'historyName-3').send_keys('short digits')
        driver.find_element(By.ID, 'historyName-3').send_keys(Keys.TAB)
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()

    def testDateHistoryModify(self):
        """
        @Status tests that a basic Marker History Date can be modified
        @see pwi-mrk-det-hist-update-4
        """
        driver = self.driver
        # finds the history symbol field and enters a symbol
        driver.find_element(By.ID, "historyName-0").send_keys('splotch-like%')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # find the symbol name column of the history table for the first 7 results
        symname1 = driver.find_element(By.ID, 'historyName-0').get_attribute('value')
        symname2 = driver.find_element(By.ID, 'historyName-1').get_attribute('value')
        symname3 = driver.find_element(By.ID, 'historyName-2').get_attribute('value')
        symname4 = driver.find_element(By.ID, 'historyName-3').get_attribute('value')
        symname5 = driver.find_element(By.ID, 'historyName-4').get_attribute('value')
        symname6 = driver.find_element(By.ID, 'historyName-5').get_attribute('value')
        symname7 = driver.find_element(By.ID, 'historyName-6').get_attribute('value')
        # assert that the symbols are correct and in the correct order
        self.assertEqual(symname1, 'paired box 3')
        self.assertEqual(symname2, 'paired box 3')
        self.assertEqual(symname3, 'paired box 3')
        self.assertEqual(symname4, 'splotch')
        self.assertEqual(symname5, 'splotch')
        self.assertEqual(symname6, 'splotch-like 2')
        self.assertEqual(symname7, 'splotch-like 2')
        # find the fourth row date and change it from 1947-01-01 to 2019-11-19
        driver.find_element(By.ID, 'historyEventDate-3').clear()
        time.sleep(2)
        driver.find_element(By.ID, 'historyEventDate-3').send_keys('2019-11-19')
        driver.find_element(By.ID, 'historyEventDate-3').send_keys(Keys.TAB)
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()
        time.sleep(2)
        # find the date column for the 4th symbol and verify it is now 2019-11-19
        symdate4 = driver.find_element(By.ID, 'historyEventDate-3').get_attribute('value')
        # waits until the element is located or 10 seconds
        # WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value((By.ID, 'historySymbol-8', 'Hx')))
        self.assertEqual(symdate4, '2019-11-19')
        # now lets put the date back to it's original.
        driver.find_element(By.ID, 'historyEventDate-3').clear()
        time.sleep(2)
        driver.find_element(By.ID, 'historyEventDate-3').send_keys('1947-01-01')
        driver.find_element(By.ID, 'historyEventDate-3').send_keys(Keys.TAB)
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()

    def testJnumHistoryModify(self):
        """
        @Status tests that a basic Marker History J# can be modified
        @see pwi-mrk-det-hist-update-5
        """
        driver = self.driver
        # finds the history name field and enters a symbol
        driver.find_element(By.ID, "historyName-0").send_keys('splotch-like%')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # find the J number column of the history table for the first 7 results
        jnumber1 = driver.find_element(By.ID, 'historyJnum-0').get_attribute('value')
        jnumber2 = driver.find_element(By.ID, 'historyJnum-1').get_attribute('value')
        jnumber3 = driver.find_element(By.ID, 'historyJnum-2').get_attribute('value')
        jnumber4 = driver.find_element(By.ID, 'historyJnum-3').get_attribute('value')
        jnumber5 = driver.find_element(By.ID, 'historyJnum-4').get_attribute('value')
        jnumber6 = driver.find_element(By.ID, 'historyJnum-5').get_attribute('value')
        jnumber7 = driver.find_element(By.ID, 'historyJnum-6').get_attribute('value')
        # assert that the symbols are correct and in the correct order
        self.assertEqual(jnumber1, 'J:14224')
        self.assertEqual(jnumber2, 'J:15839')
        self.assertEqual(jnumber3, 'J:15839')
        self.assertEqual(jnumber4, 'J:12957')
        self.assertEqual(jnumber5, 'J:2944')
        self.assertEqual(jnumber6, 'J:162227')
        self.assertEqual(jnumber7, 'J:222308')
        # find the fourth row J# and change it from J:12957 to J:23000
        driver.find_element(By.ID, 'historyJnum-3').clear()
        time.sleep(2)
        driver.find_element(By.ID, 'historyJnum-3').send_keys('J:23000')
        driver.find_element(By.ID, 'historyJnum-3').send_keys(Keys.TAB)
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()
        time.sleep(2)
        # find the J# column for the 4th symbol and verify it is now J:23000
        jnumber4 = driver.find_element(By.ID, 'historyJnum-3').get_attribute('value')
        # waits until the element is located or 10 seconds
        # WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value((By.ID, 'historySymbol-8', 'Hx')))
        self.assertEqual(jnumber4, 'J:23000')
        # now lets put the J# back to it's original.
        driver.find_element(By.ID, 'historyJnum-3').clear()
        time.sleep(2)
        driver.find_element(By.ID, 'historyJnum-3').send_keys('J:12957')
        driver.find_element(By.ID, 'historyJnum-3').send_keys(Keys.TAB)
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()

    def testJnumHistoryValid(self):
        """
        @Status tests that a basic Marker History J number update verifies
        @see pwi-mrk-det-hist-update-6 *might need to verify this test is actually testing the right thing*
        """
        driver = self.driver
        # finds the J# field and enters a J number
        driver.find_element(By.ID, "historyJnum-0").send_keys('J:2944')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # find the J number column of the history table for the first 7 results
        jnumber1 = driver.find_element(By.ID, 'historyJnum-0').get_attribute('value')
        jnumber2 = driver.find_element(By.ID, 'historyJnum-1').get_attribute('value')
        jnumber3 = driver.find_element(By.ID, 'historyJnum-2').get_attribute('value')
        jnumber4 = driver.find_element(By.ID, 'historyJnum-3').get_attribute('value')
        jnumber5 = driver.find_element(By.ID, 'historyJnum-4').get_attribute('value')
        jnumber6 = driver.find_element(By.ID, 'historyJnum-5').get_attribute('value')
        jnumber7 = driver.find_element(By.ID, 'historyJnum-6').get_attribute('value')
        # assert that the symbols are correct and in the correct order
        self.assertEqual(jnumber1, 'J:14224')
        self.assertEqual(jnumber2, 'J:15839')
        self.assertEqual(jnumber3, 'J:15839')
        self.assertEqual(jnumber4, 'J:12957')
        self.assertEqual(jnumber5, 'J:2944')
        self.assertEqual(jnumber6, 'J:162227')
        self.assertEqual(jnumber7, 'J:222308')
        # find the fourth row J# and change it from J:12957 to J:23000
        driver.find_element(By.ID, 'historyJnum-3').clear()
        time.sleep(2)
        driver.find_element(By.ID, 'historyJnum-3').send_keys('J:23000')
        driver.find_element(By.ID, 'historyJnum-3').send_keys(Keys.TAB)
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()
        time.sleep(2)
        # find the J# column for the 4th symbol and verify it is now J:23000
        jnumber4 = driver.find_element(By.ID, 'historyJnum-3').get_attribute('value')
        # waits until the element is located or 10 seconds
        # WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value((By.ID, 'historySymbol-8', 'Hx')))
        self.assertEqual(jnumber4, 'J:23000')
        # now lets put the J# back to it's original.
        driver.find_element(By.ID, 'historyJnum-3').clear()
        time.sleep(2)
        driver.find_element(By.ID, 'historyJnum-3').send_keys('J:12957')
        driver.find_element(By.ID, 'historyJnum-3').send_keys(Keys.TAB)
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()

    def testEventHistoryModify(self):
        """
        @Status tests that a basic Marker History Event can be modified
        @see pwi-mrk-det-hist-search-8
        """
        driver = self.driver
        # finds the history symbol field and enters a symbol
        driver.find_element(By.ID, "historySymbol-0").send_keys('Pax1')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # find the Event column of the history table for the first 9 results
        vent1 = driver.find_element(By.ID, 'historyEvent-0').get_attribute('value')
        vent2 = driver.find_element(By.ID, 'historyEvent-1').get_attribute('value')
        vent3 = driver.find_element(By.ID, 'historyEvent-2').get_attribute('value')
        vent4 = driver.find_element(By.ID, 'historyEvent-3').get_attribute('value')
        vent5 = driver.find_element(By.ID, 'historyEvent-4').get_attribute('value')
        vent6 = driver.find_element(By.ID, 'historyEvent-5').get_attribute('value')
        vent7 = driver.find_element(By.ID, 'historyEvent-6').get_attribute('value')
        vent8 = driver.find_element(By.ID, 'historyEvent-7').get_attribute('value')
        vent9 = driver.find_element(By.ID, 'historyEvent-8').get_attribute('value')
        # assert that the symbols are correct and in the correct order
        self.assertEqual(vent1, 'string:1')  # string:1 equals assigned
        self.assertEqual(vent2, 'string:4')  # string:4 equals allele of
        self.assertEqual(vent3, 'string:1')
        self.assertEqual(vent4, 'string:4')
        self.assertEqual(vent5, 'string:1')
        self.assertEqual(vent6, 'string:4')
        self.assertEqual(vent7, 'string:1')
        self.assertEqual(vent8, 'string:2')  # string:2 equals rename
        self.assertEqual(vent9, 'string:1')
        # find the seventh row Event and change it from rename to assigned
        time.sleep(2)
        my_select = driver.find_element(By.ID, 'historyEvent-7')
        for option in my_select.find_elements_by_tag_name('option'):
            if option.text == "assigned":
                option.click()
                break
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()
        time.sleep(2)
        # find the Event column for the 7th row and verify it is now Assigned
        vent8 = driver.find_element(By.ID, 'historyEvent-7').get_attribute('value')
        # waits until the element is located or 10 seconds
        # WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value((By.ID, 'historySymbol-8', 'Hx')))
        self.assertEqual(vent8, 'string:1')
        # now lets put the Event back to it's original of rename.
        time.sleep(2)
        my_select = driver.find_element(By.ID, 'historyEvent-7')
        for option in my_select.find_elements(By.TAG_NAME, 'option'):
            if option.text == "rename":
                option.click()
                break
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()

    def testEventReasonHistoryModify(self):
        """
        @Status tests that a basic Marker History Event Reason can be modified
        @see pwi-mrk-det-hist-search-9
        """
        driver = self.driver
        # finds the history symbol field and enters a symbol
        driver.find_element(By.ID, "historySymbol-0").send_keys('Ang2')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # find the Reason column of the history table for the first 3 results
        vreason1 = driver.find_element(By.ID, 'historyEventReason-0').get_attribute('value')
        vreason2 = driver.find_element(By.ID, 'historyEventReason-1').get_attribute('value')
        vreason3 = driver.find_element(By.ID, 'historyEventReason-2').get_attribute('value')

        # assert that the reasons are correct and in the correct order
        self.assertEqual(vreason1, 'string:-1')  # string:-1 equals Not Specified
        self.assertEqual(vreason2, 'string:3')  # string:3 equals personal comm w/authors
        self.assertEqual(vreason3, 'string:3')

        # find the second row Reason and change it from personal comm w/authors to per gene family revision
        time.sleep(2)
        my_select = driver.find_element(By.ID, 'historyEventReason-1')
        for option in my_select.find_elements(By.TAG_NAME, 'option'):
            if option.text == "per gene family revision":
                option.click()
                break
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()
        time.sleep(2)
        # find the Reason column for the 2nd row and verify it is now string:2 (per gene family)
        vreason2 = driver.find_element(By.ID, 'historyEvent-1').get_attribute('value')
        # waits until the element is located or 10 seconds
        # WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value((By.ID, 'historySymbol-8', 'Hx')))
        self.assertEqual(vreason2, 'string:2')
        # now lets put the Event back to it's original of rename.
        time.sleep(2)
        my_select = driver.find_element(By.ID, 'historyEventReason-1')
        for option in my_select.find_elements(By.TAG_NAME, 'option'):
            if option.text == "personal comm w/authors":
                option.click()
                break
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()

    def testHistoryDeleteConfirm(self):
        """
        @Status tests that a basic Marker History row deletion gives a validation popup confirmation and the row gets highlighted.
        @see pwi-mrk-det-hist-update-12 **Under Construction**
        """
        driver = self.driver
        # finds the history symbol field and enters a symbol
        driver.find_element(By.ID, "historySymbol-0").send_keys('Gata-1')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # find the symbol column of the history table for the first 9 results
        sym1 = driver.find_element(By.ID, 'historySymbol-0').get_attribute('value')
        sym2 = driver.find_element(By.ID, 'historySymbol-1').get_attribute('value')
        sym3 = driver.find_element(By.ID, 'historySymbol-2').get_attribute('value')
        sym4 = driver.find_element(By.ID, 'historySymbol-3').get_attribute('value')
        sym5 = driver.find_element(By.ID, 'historySymbol-4').get_attribute('value')
        # assert that the symbols are correct and in the correct order
        self.assertEqual(sym1, 'Gf-1')
        self.assertEqual(sym2, 'Gf-1')
        self.assertEqual(sym3, 'Gata-1')
        self.assertEqual(sym4, 'Gata-1')
        self.assertEqual(sym5, 'Gata1')
        # find the delete x for row 5 of the history table and click it
        driver.find_element(By.ID, 'deleteRow-4').click()
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()
        time.sleep(2)
        # now lets add  this row back
        # find the add Row button for the history table and click it
        driver.find_element(By.ID, 'addHistoryButton').click()
        # find the add history Symbol field and enter your symbol
        driver.find_element(By.ID, 'historySymbol-4').send_keys('Gata1')
        # find the add history Name field and enter your name
        driver.find_element(By.ID, 'historyName-4').send_keys('GATA binding protein 1')
        # find the add history Date field and enter the date
        driver.find_element(By.ID, 'historyEventDate-4').send_keys('1993-11-01')
        # find the add history J number field and enter your J number
        driver.find_element(By.ID, 'historyJnum-4').send_keys('J:15839')
        driver.find_element(By.ID, 'historyJnum-4').send_keys(Keys.TAB)
        # find the Event field and select assigned
        Select(driver.find_element(By.ID, 'historyEvent-4')).select_by_visible_text('assigned')
        # find the Reason field and select Not Specified
        Select(driver.find_element(By.ID, 'historyEventReason-4')).select_by_visible_text('Not Specified')
        time.sleep(2)
        # find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()
        time.sleep(2)
        # Find the 5th row and verify the symbol is correct
        sym5 = driver.find_element(By.ID, 'historySymbol-4').get_attribute('value')
        # assert that the symbol for the 5th row is correct
        self.assertEqual(sym5, 'Gata1')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiMrkUpdateDeleteHistory))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
