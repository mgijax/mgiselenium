'''
Created on Nov 21, 2018

@author: jeffc
'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import HtmlTestRunner
import json
import sys, os.path
from select import select

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table


# Tests

class TestEiMrkAddDelete(unittest.TestCase):
    """
    @status Tests you can add and delete markers of various types and statuses
    @see:
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
        submit.click()

    def tearDown(self):
        self.driver.close()

    def testTypeGeneAdd(self):
        """
        @Status tests that you can add a marker of type Gene
        @see pwi-mrk-create-mrk-1
        @note: remove time sleeps later when time permits! tested 2/10/2020
        """
        driver = self.driver
        # finds the marker type pulldown list and selects "Pseudogene"
        Select(driver.find_element(By.ID, "markerType")).select_by_value('string:7')
        time.sleep(2)
        # finds the marker status pulldown and selects "Official"
        Select(driver.find_element(By.ID, "markerStatus")).select_by_value('string:1')
        time.sleep(2)
        # Finds the Chromosome pulldown list and selects Chromosome "2"
        driver.find_element(By.ID, 'chromosome').clear();
        driver.find_element(By.ID, 'chromosome').send_keys("2");
        # Select(driver.find_element(By.ID, "browser")).select_by_value('2')
        time.sleep(2)
        # Finds the Symbol field and enters a new symbol
        driver.find_element(By.ID, "markerSymbol").send_keys('jeffcmarker')
        time.sleep(2)
        # Finds the Name field and enters a new name
        driver.find_element(By.ID, "markerName").send_keys('jeffc test marker')
        time.sleep(2)
        # Finds the J# field in the History section and enter a valid J number
        driver.find_element(By.ID, "historyJnum-0").send_keys('28000')
        actionChains = ActionChains(driver)
        actionChains.send_keys(Keys.TAB)
        actionChains.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'createMarkerButton').click()
        time.sleep(2)
        # find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print(symbol1)
        # Assert the correct marker symbol and marker type is returned
        self.assertEqual(symbol1, ['jeffcmarker'])
        # since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element(By.ID, 'markerType').get_attribute('value')
        self.assertEqual(mrktype, 'string:7')  # 1 equals "Gene"

    def testTypeGeneRef(self):
        """
        @Status tests that you can add a reference to a marker of type Gene
        @see pwi-mrk-det-ref-add-1, 5 tested 2/10/2020
        """
        driver = self.driver
        # finds the Symbol field and enters the text
        driver.find_element(By.ID, "markerSymbol").send_keys('saal1')
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # click on the References Tab
        driver.find_element(By.ID, 'refsTabButton').click()
        time.sleep(2)
        # find the Reference Add button and click it
        driver.find_element(By.ID, 'addReferenceButton').click()
        # find the Type field and select "General" as the option
        Select(driver.find_element(By.ID, 'refAssocType')).select_by_value('string:1018')
        # find the J# field and enter the J# into it then tabout for validation check
        driver.find_element(By.ID, 'refjnumID-0').send_keys('28000')
        actionChains = ActionChains(driver)
        actionChains.send_keys(Keys.TAB)
        actionChains.perform()
        # find and click the "Modify" button
        driver.find_element(By.ID, 'updateMarkerButton').click()
        time.sleep(5)
        # find the Type field, ref jnum field, citation field of row 1 of the Reference tab and print them
        typ = driver.find_element(By.ID, 'refAssocType').get_attribute('value')
        refjn = driver.find_element(By.ID, 'refjnumID-0').get_attribute('value')
        cit = driver.find_element(By.ID, 'refAssocCitation-0').get_attribute('value')
        print(typ)
        print(refjn)
        print(cit)
        # assert the row of Reference data(first 3 fields)
        self.assertEqual(typ, 'string:1018')
        self.assertEqual(refjn, 'J:28000')
        self.assertEqual(cit, 'Novotny MV, Experientia 1995 Jul 14;51(7):738-43')

    def testGeneFeatureAdd(self):
        """
        @Status tests that you can add a feature type to a Marker Type Gene
        @see pwi-mrk-det-feature-add-1
        @note: remove time sleeps later when time permits! tested 2/10/2020
        """
        driver = self.driver
        # finds the Symbol field . Enter jeff% and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("jeff%")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # click the add row button for Feature Type
        driver.find_element(By.ID, 'addFeatureTypeButton').click()
        # Find the feature type pulldown and select "gene segment"
        Select(driver.find_element(By.ID, "featureID")).select_by_value('string:7313348')
        time.sleep(2)
        # find the Feature Type field and print it
        feat = driver.find_element(By.ID, 'featureID').get_attribute('value')
        print(feat)
        # assert the feature type is correct for this marker
        self.assertEqual(feat, 'string:7313348')

    def testDnaSegFeatureAdd(self):
        """
        @Status tests that you can't add a feature type to a Marker Type DNA Segment Marker
        @see pwi-mrk-det-feature-add-2
        @note: remove time sleeps later when time permits! tested 2/10/2020
        """
        driver = self.driver
        # finds the Symbol field . Enter 123B5b and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("123B5b")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)

        # Assert there is no Add Feature type pulldown list
        def test_element_does_not_exist(self):
            with self.assertRaises(NoSuchElementException):
                driver.find_element(By.ID, "featureID")

    def testCytoMrkFeatureAdd(self):
        """
        @Status tests that you can add a feature type to a Marker Type Cytogenetic Marker
        @see pwi-mrk-det-feature-add-3
        @note: remove time sleeps later when time permits! tested 2/10/2020
        """
        driver = self.driver
        # finds the Symbol field . Enter 123B5b and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("Del(8)7H")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # Find the feature type pulldown and select "Robertsonian fusion"
        Select(driver.find_element(By.ID, "featureID")).select_by_value('string:7196771')
        time.sleep(2)
        # Now let's click the Modify button!
        driver.find_element(By.ID, 'updateMarkerButton').click()
        time.sleep(2)
        # find the Feature Type field and print it
        feat = driver.find_element(By.ID, 'featureID').get_attribute('value')
        print(feat)
        # assert the feature type is correct for this marker
        self.assertEqual(feat, 'string:7196771')

    def testQtlFeatureAdd(self):
        """
        @Status tests that you can't add a feature type to a Marker Type QTL
        @see pwi-mrk-det-feature-add-4
        @note: remove time sleeps later when time permits! tested 2/10/2020
        """
        driver = self.driver
        # finds the Symbol field . Enter Aec1 and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("Aec1")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)

        # Assert there is no Add Feature type pulldown list
        def test_element_does_not_exist(self):
            with self.assertRaises(NoSuchElementException):
                driver.find_element(By.ID, "tdcAddList")

    def testPseudoFeatureAdd(self):
        """
        @Status tests that you can add a feature type to a Marker Type Pseudogene Marker
        @see pwi-mrk-det-feature-add-5
        @note: remove time sleeps later when time permits! tested 2/11/2020
        """
        driver = self.driver
        # finds the Symbol field . Enter Clec7a and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("Clec7a")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # Find the feature type pulldown and select "Pseudogenic region"
        Select(driver.find_element(By.ID, "featureID")).select_by_value('string:7288448')
        time.sleep(2)
        # Find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()
        time.sleep(2)
        # find the Feature Type field and print it
        feat = driver.find_element(By.ID, 'featureID').get_attribute('value')
        print(feat)
        # assert the feature type is correct for this marker
        self.assertEqual(feat, 'string:7288448')

    def testBacYacFeatureAdd(self):
        """
        @Status tests that you can't add a feature type to a Marker Type BAC/YAC end
        @see pwi-mrk-det-feature-add-6
        @note: remove time sleeps later when time permits! tested 2/11/2020
        """
        driver = self.driver
        # finds the Symbol field . Enter 52H9 and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("52H9")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)

        # Assert there is no Add Feature type pulldown list
        def test_element_does_not_exist(self):
            with self.assertRaises(NoSuchElementException):
                driver.find_element(By.ID, "featureID")

    def testOtherGenomeFeatureAdd(self):
        """
        @Status tests that you can add a feature type to a Marker Type Other Genome Feature
        @see pwi-mrk-det-feature-add-7
        @note: remove time sleeps later when time permits! tested 2/11/2020
        """
        driver = self.driver
        # finds the Symbol field . Enter Cpgi% and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("Cpgi10")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # Find the feature type pulldown and select "unclassified other genome feature"
        Select(driver.find_element(By.ID, "featureID")).select_by_value('string:7648969')
        time.sleep(2)
        # Find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()
        time.sleep(2)
        # find the Feature Type field and print it
        feat = driver.find_element(By.ID, 'featureID').get_attribute('value')
        print(feat)
        # assert the feature type is correct for this marker
        self.assertEqual(feat, 'string:7648969')

    def testComplexFeatureAdd(self):
        """
        @Status tests that you can't add a feature type to a Marker Type Complex/Cluster/Region
        @see pwi-mrk-det-feature-add-8
        @note: remove time sleeps later when time permits! tested 2/11/2020
        """
        driver = self.driver
        # finds the Symbol field . Enter Amy and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("Amy")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)

        # Assert there is no Add Feature type pulldown list
        def test_element_does_not_exist(self):
            with self.assertRaises(NoSuchElementException):
                driver.find_element(By.ID, "featureID")

    def testTransgeneFeatureAdd(self):
        """
        @Status tests that you can't add a feature type to a Marker Type Transgene
        @see pwi-mrk-det-feature-add-9
        @note: remove time sleeps later when time permits! tested 2/11/2020
        """
        driver = self.driver
        # finds the Symbol field . Enter Tg(Hbb-b1)83Clo and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("Tg(Hbb-b1)83Clo")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)

        # Assert there is no Add Feature type pulldown list
        def test_element_does_not_exist(self):
            with self.assertRaises(NoSuchElementException):
                driver.find_element(By.ID, "featureID")

    def testMultipleFeatureAdd(self):
        """
        @Status tests that you can add multiple feature types to a Marker
        @see pwi-mrk-det-feature-add-10
        @note: remove time sleeps later when time permits! tested 02/25/2020
        """
        driver = self.driver
        # finds the Symbol field . Enter Cpgi% and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("Cpgi1")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # Find the feature types "Add" button and click it
        driver.find_element(By.ID, 'addFeatureTypeButton').click()
        time.sleep(2)
        driver.find_element(By.ID, 'addFeatureTypeButton').click()
        # gets you focused in the second row of Feature Type
        row2 = driver.find_element(By.ID, "featureTypeTable").find_element(By.CSS_SELECTOR, 'tr:nth-child(2)')
        row2.click()
        time.sleep(2)
        # Find the feature type pulldown and select "unclassified other genome feature"
        Select(row2.find_element(By.ID, "featureID")).select_by_value('string:7648969')
        time.sleep(2)
        # gets you focused in the third row of Feature Type
        row3 = driver.find_element(By.ID, "featureTypeTable").find_element(By.CSS_SELECTOR, 'tr:nth-child(3)')
        row3.click()
        time.sleep(2)
        # Find the feature type pulldown and select "minisatellite"
        Select(row3.find_element(By.ID, "featureID")).select_by_value('string:7648968')
        time.sleep(2)
        # Find the Modify button and click it
        driver.find_element(By.ID, 'updateMarkerButton').click()
        time.sleep(2)
        # This gets and then verifies that the first feature type is CpG island(string:15406205)
        feat1 = driver.find_element(By.ID, 'featureID').get_attribute('value')
        print(feat1)
        self.assertEqual(feat1, 'string:15406205')
        # This gets and then verifies that the second feature type is minisatellite(string:7648968)
        # even though this was entered third once the adds are modified the feature type resorts by alpha
        row2 = driver.find_element(By.ID, "featureTypeTable").find_element(By.CSS_SELECTOR, 'tr:nth-child(2)')
        feat2 = row2.find_element_by_id('featureID').get_attribute('value')
        self.assertEqual(feat2, 'string:7648968')
        # This gets and then verifies that the third feature type is unclassified other genome featyre(string:7648969)
        # even though this was entered second once the adds are modified the feature type resorts by alpha
        row3 = driver.find_element(By.ID, "featureTypeTable").find_element(By.CSS_SELECTOR, 'tr:nth-child(3)')
        feat3 = row3.find_element(By.ID, 'featureID').get_attribute('value')
        self.assertEqual(feat3, 'string:7648969')

    def testBadMrkTypeFeatureAdd(self):
        """
        @Status tests that you get an error when you try to change the Marker type for an incompatible feature type
        @see pwi-mrk-det-feature-update-1
        @note: remove time sleeps later when time permits! tested 02/25/2020
        """
        driver = self.driver
        # finds the Symbol field . Enter Hc3 and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("Hc3")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # find the Marker Type pulldown and try to change it from Cytogenetic Marker to Other Genome Feature
        Select(driver.find_element(By.ID, "markerType")).select_by_value('string:9')
        time.sleep(2)
        # capture the javascript alert and press it's OK button
        alertObj = driver.switch_to.alert()
        print(alertObj.text)
        time.sleep(2)
        # Assert the alert text returned is correct
        self.assertEqual(alertObj.text, 'Invalid Marker Type/Feature Type combination. ')
        alertObj.accept()

    def testBadFeatureTypeMarkerAdd(self):
        """
        @Status tests that you get an error when you try to change the Feature type for an incompatible Marker type
        @see pwi-mrk-det-feature-update-2
        @note: remove time sleeps later when time permits! tested 02/25/2020
        """
        driver = self.driver
        # finds the Symbol field . Enter Hc3 and click the Search button
        driver.find_element(By.ID, "markerSymbol").send_keys("Hc3")
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(2)
        # find the Feature Type pulldown and try to change it from unclassified cytogenetic marker to pseudogene
        Select(driver.find_element(By.ID, "featureID")).select_by_value('string:7313348')
        time.sleep(2)
        # capture the javascript alert and press it's OK button
        alertObj = driver.switch_to.alert
        print(alertObj.text)
        time.sleep(2)
        # Assert the alert text returned is correct
        self.assertEqual(alertObj.text, 'Invalid Marker Type/Feature Type combination. ')
        alertObj.accept()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiMrkAddDelete))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
