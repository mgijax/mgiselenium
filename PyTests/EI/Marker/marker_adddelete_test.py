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
import HTMLTestRunner
import json
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

class TestMrkAddDelete(unittest.TestCase):
    """
    @status Tests you can add and delete markers of various types and statuses
    @see: 
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/marker")
        username = self.driver.find_element_by_name('user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = self.driver.find_element_by_name('password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = self.driver.find_element_by_name("submit") #Find the Login button
        submit.click()
    
    def tearDown(self):
        self.driver.close()
        
    def testTypeGeneAdd(self):
        """
        @Status tests that you can add a marker of type Gene
        @see pwi-mrk-create-mrk-1
        @note: remove time sleeps later when time permits!
        """
        driver = self.driver
        #finds the marker type pulldown list and selects "Pseudogene"
        Select(driver.find_element_by_id("markerType")).select_by_value('7')
        time.sleep(2)
        #finds the marker status pulldown and selects "Official"
        Select(driver.find_element_by_id("markerStatus")).select_by_value('1')
        time.sleep(2)
        #Finds the Chromosome pulldown list and selects Chromosome "2"
        Select(driver.find_element_by_id("chromosome")).select_by_value('2')
        time.sleep(2)
        #Finds the Symbol field and enters a new symbol
        driver.find_element_by_id("markerSymbol").send_keys('jeffcmarker')
        time.sleep(2)
        #Finds the Name field and enters a new name
        driver.find_element_by_id("markerName").send_keys('jeffc test marker')
        time.sleep(2)
        #Finds the J# field in the History section and enter a valid J number
        driver.find_element_by_id("markerHistoryJNumID").send_keys('28000')
        actionChains = ActionChains(driver)
        actionChains.send_keys(Keys.TAB)
        actionChains.perform()
        time.sleep(2)
        driver.find_element_by_id('createMarkerButton').click()
        time.sleep(2)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTableHeader")
        table = Table(results_table)
        #Iterate and print the search results headers
        cell1 = table.get_row_cells(0)
        symbol1 = iterate.getTextAsList(cell1)
        print symbol1
        #Assert the correct marker symbol and marker type is returned
        self.assertEquals(symbol1, ['jeffcmarker'])
        #since we search for a particular marker type verify the correct type is displayed
        mrktype = driver.find_element_by_id('markerType').get_attribute('value')
        self.assertEqual(mrktype, '7')#1 equals "Gene"

    def testTypeGeneAddRef(self):
        """
        @Status tests that you can add a reference to a marker of type Gene
        @see pwi-mrk-det-ref-add-1, 5 
        """
        driver = self.driver
        #finds the Symbol field and enters the text
        driver.find_element_by_id("markerSymbol").send_keys('saal1')
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #click on the References Tab
        driver.find_element_by_id('refsTabButton').click()
        time.sleep(2)
        #find the Reference Add button and click it
        driver.find_element_by_id('addReferenceButton').click()
        #find the J# field and enter the J# into it then tabout for validation check
        driver.find_element_by_id('addMarkerRefJnumID').send_keys('28000')
        actionChains = ActionChains(driver)
        actionChains.send_keys(Keys.TAB)
        actionChains.perform()
        #find and click the "Commit Row" button
        driver.find_element_by_id('addMarkerRefCommitID').click()
        time.sleep(10)
        #find the reference row that has the correct J number
        refs_table = self.driver.find_element_by_id("refsTable")
        table = Table(refs_table)
        #Iterate and get the correct row of reference data
        cells = table.get_row_cells(1)
        row1 = iterate.getTextAsList(cells)
        print row1
        #assert the row of Reference data, Note we never actually modify the marker so this reference never gets saved.
        self.assertEqual(row1, [u'', u'General', u'28000', u'Novotny MV, Experientia 1995 Jul 14;51(7):738-43', u'', u''])
    
    def testGeneFeatureAdd(self):
        """
        @Status tests that you can add a feature type to a Marker Type Gene
        @see pwi-mrk-det-feature-add-1
        @note: remove time sleeps later when time permits!
        """
        driver = self.driver
        #finds the Symbol field . Enter jeff% and click the Search button
        driver.find_element_by_id("markerSymbol").send_keys("jeff%")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Find the feature type pulldown and select "gene segment"
        Select(driver.find_element_by_id("tdcAddList")).select_by_value('6238171')
        time.sleep(2)
        #Find the feature types "Add" button and click it
        driver.find_element_by_id('addFeatureTypeButton').click()
        time.sleep(2)
        #NOTE: we never actually save this feature type!
        #find the feature types table
        feature_table = self.driver.find_element_by_id("featureTypeTable")
        table = Table(feature_table)
        #Iterate and print the feature type results
        cell1 = table.get_row_cells(1)
        item1 = iterate.getTextAsList(cell1)
        print item1
        #Assert the correct feature type is returned
        self.assertEquals(item1, ['', 'gene segment'])  

    def testDnaSegFeatureAdd(self):
        """
        @Status tests that you can't add a feature type to a Marker Type DNA Segment Marker
        @see pwi-mrk-det-feature-add-2
        @note: remove time sleeps later when time permits!
        """
        driver = self.driver
        #finds the Symbol field . Enter 123B5b and click the Search button
        driver.find_element_by_id("markerSymbol").send_keys("123B5b")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert there is no Add Feature type pulldown list
        def test_element_does_not_exist(self):
            with self.assertRaises(NoSuchElementException):
                driver.find_element_by_id("tdcAddList")

    def testCytoMrkFeatureAdd(self):
        """
        @Status tests that you can add a feature type to a Marker Type Cytogenetic Marker
        @see pwi-mrk-det-feature-add-3
        @note: remove time sleeps later when time permits!
        """
        driver = self.driver
        #finds the Symbol field . Enter jeffc% and click the Search button
        driver.find_element_by_id("markerSymbol").send_keys("jeffc%")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Find the feature type pulldown and select "Robertsonian fusion"
        Select(driver.find_element_by_id("tdcAddList")).select_by_value('7196771')
        time.sleep(2)
        #Find the feature types "Add" button and click it
        driver.find_element_by_id('addFeatureTypeButton').click()
        time.sleep(2)
        #NOTE: we never actually save this feature type!
        #find the feature types table
        feature_table = self.driver.find_element_by_id("featureTypeTable")
        table = Table(feature_table)
        #Iterate and print the feature type results
        cell1 = table.get_row_cells(1)
        item1 = iterate.getTextAsList(cell1)
        print item1
        #Assert the correct feature type is returned
        self.assertEquals(item1, ['', 'Robertsonian fusion'])  

    def testQtlFeatureAdd(self):
        """
        @Status tests that you can't add a feature type to a Marker Type QTL
        @see pwi-mrk-det-feature-add-4
        @note: remove time sleeps later when time permits!
        """
        driver = self.driver
        #finds the Symbol field . Enter Aec1 and click the Search button
        driver.find_element_by_id("markerSymbol").send_keys("Aec1")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert there is no Add Feature type pulldown list
        def test_element_does_not_exist(self):
            with self.assertRaises(NoSuchElementException):
                driver.find_element_by_id("tdcAddList")

    def testPseudoFeatureAdd(self):
        """
        @Status tests that you can add a feature type to a Marker Type Pseudogene Marker
        @see pwi-mrk-det-feature-add-5
        @note: remove time sleeps later when time permits!
        """
        driver = self.driver
        #finds the Symbol field . Enter Clec7a and click the Search button
        driver.find_element_by_id("markerSymbol").send_keys("Clec7a")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Find the feature type pulldown and select "Pseudogenic region"
        Select(driver.find_element_by_id("tdcAddList")).select_by_value('7288448')
        time.sleep(2)
        #Find the feature types "Add" button and click it
        driver.find_element_by_id('addFeatureTypeButton').click()
        time.sleep(2)
        #NOTE: we never actually save this feature type!
        #find the feature types table
        feature_table = self.driver.find_element_by_id("featureTypeTable")
        table = Table(feature_table)
        #Iterate and print the feature type results
        cell1 = table.get_row_cells(1)
        item1 = iterate.getTextAsList(cell1)
        print item1
        #Assert the correct feature type is returned
        self.assertEquals(item1, ['', 'pseudogenic region'])  

    def testBacYacFeatureAdd(self):
        """
        @Status tests that you can't add a feature type to a Marker Type BAC/YAC end
        @see pwi-mrk-det-feature-add-6
        @note: remove time sleeps later when time permits!
        """
        driver = self.driver
        #finds the Symbol field . Enter 52H9 and click the Search button
        driver.find_element_by_id("markerSymbol").send_keys("52H9")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert there is no Add Feature type pulldown list
        def test_element_does_not_exist(self):
            with self.assertRaises(NoSuchElementException):
                driver.find_element_by_id("tdcAddList")

    def testOtherGenomeFeatureAdd(self):
        """
        @Status tests that you can add a feature type to a Marker Type Other Genome Feature
        @see pwi-mrk-det-feature-add-7
        @note: remove time sleeps later when time permits!
        """
        driver = self.driver
        #finds the Symbol field . Enter Cpgi% and click the Search button
        driver.find_element_by_id("markerSymbol").send_keys("Cpgi%")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Find the feature type pulldown and select "unclassified other genome feature"
        Select(driver.find_element_by_id("tdcAddList")).select_by_value('7648969')
        time.sleep(2)
        #Find the feature types "Add" button and click it
        driver.find_element_by_id('addFeatureTypeButton').click()
        time.sleep(2)
        #NOTE: we never actually save this feature type!
        #find the feature types table
        feature_table = self.driver.find_element_by_id("featureTypeTable")
        table = Table(feature_table)
        #Iterate and print the feature type results
        cell1 = table.get_row_cells(1)
        item1 = iterate.getTextAsList(cell1)
        print item1
        #Assert the correct feature type is returned
        self.assertEquals(item1, ['', 'unclassified other genome feature'])
        
    def testComplexFeatureAdd(self):
        """
        @Status tests that you can't add a feature type to a Marker Type Complex/Cluster/Region
        @see pwi-mrk-det-feature-add-8
        @note: remove time sleeps later when time permits!
        """
        driver = self.driver
        #finds the Symbol field . Enter Amy and click the Search button
        driver.find_element_by_id("markerSymbol").send_keys("Amy")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert there is no Add Feature type pulldown list
        def test_element_does_not_exist(self):
            with self.assertRaises(NoSuchElementException):
                driver.find_element_by_id("tdcAddList")          

    def testTransgeneFeatureAdd(self):
        """
        @Status tests that you can't add a feature type to a Marker Type Transgene
        @see pwi-mrk-det-feature-add-9
        @note: remove time sleeps later when time permits!
        """
        driver = self.driver
        #finds the Symbol field . Enter Tg(Hbb-b1)83Clo and click the Search button
        driver.find_element_by_id("markerSymbol").send_keys("Tg(Hbb-b1)83Clo")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Assert there is no Add Feature type pulldown list
        def test_element_does_not_exist(self):
            with self.assertRaises(NoSuchElementException):
                driver.find_element_by_id("tdcAddList")

    def testMultipleFeatureAdd(self):
        """
        @Status tests that you can add multiple feature types to a Marker
        @see pwi-mrk-det-feature-add-10
        @note: remove time sleeps later when time permits!
        """
        driver = self.driver
        #finds the Symbol field . Enter Cpgi% and click the Search button
        driver.find_element_by_id("markerSymbol").send_keys("Cpgi%")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #Find the feature type pulldown and select "unclassified other genome feature"
        Select(driver.find_element_by_id("tdcAddList")).select_by_value('7648969')
        time.sleep(2)
        #Find the feature types "Add" button and click it
        driver.find_element_by_id('addFeatureTypeButton').click()
        time.sleep(2)
        #Find the feature type pulldown and select "minisatellite"
        Select(driver.find_element_by_id("tdcAddList")).select_by_value('7648968')
        time.sleep(2)
        #Find the feature types "Add" button and click it
        driver.find_element_by_id('addFeatureTypeButton').click()
        time.sleep(2)
        #NOTE: we never actually save this feature type!
        #find the feature types table
        feature_table = self.driver.find_element_by_id("featureTypeTable")
        table = Table(feature_table)
        #Iterate and print the feature type results
        cell1 = table.get_row_cells(1)
        item1 = iterate.getTextAsList(cell1)
        print item1
        cell2 = table.get_row_cells(2)
        item2 = iterate.getTextAsList(cell2)
        print item2
        cell3 = table.get_row_cells(3)
        item3 = iterate.getTextAsList(cell3)
        print item3
        #Assert the correct feature types are returned
        self.assertEquals(item1, ['', 'minisatellite']) 
        self.assertEquals(item2, ['', 'unclassified other genome feature'])
        self.assertEquals(item3, ['', 'CpG island']) 

    def testBadMrkTypeFeatureAdd(self):
        """
        @Status tests that you get an error when you try to change the Marker type for an imcompatible feature type
        @see pwi-mrk-det-feature-update-1
        @note: remove time sleeps later when time permits!
        """
        driver = self.driver
        #finds the Symbol field . Enter Hc3 and click the Search button
        driver.find_element_by_id("markerSymbol").send_keys("Hc3")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the Marker Type pulldown and try to change it from Cytogenetic Marker to Other Genome Feature
        Select(driver.find_element_by_id("markerType")).select_by_value('9')
        time.sleep(2)
        #capture the javascript alert and press it's OK button
        alertObj = driver.switch_to.alert
        print alertObj.text
        time.sleep(2)
        #Assert the alert text returned is correct
        self.assertEquals(alertObj.text, 'Invalid Marker Type/Feature Type combination. ')
        alertObj.accept()
        
    def testBadFeatureTypeMarkerAdd(self):
        """
        @Status tests that you get an error when you try to change the Feature type for an imcompatible Marker type
        @see pwi-mrk-det-feature-update-2
        @note: remove time sleeps later when time permits!
        """
        driver = self.driver
        #finds the Symbol field . Enter Hc3 and click the Search button
        driver.find_element_by_id("markerSymbol").send_keys("Hc3")
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the Feature Type pulldown and try to change it from unclassified cytogenetic marker to pseudogene
        Select(driver.find_element_by_id("tdcAddList")).select_by_value('7313348')
        time.sleep(2)
        #Find the feature types "Add" button and click it
        driver.find_element_by_id('addFeatureTypeButton').click()
        time.sleep(2)
        #capture the javascript alert and press it's OK button
        alertObj = driver.switch_to.alert
        print alertObj.text
        time.sleep(2)
        #Assert the alert text returned is correct
        self.assertEquals(alertObj.text, 'Invalid Marker Type/Feature Type combination. ')
        alertObj.accept()






            
'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMrkSearch))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main()
    