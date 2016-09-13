'''
Created on Sep 7, 2016

This test verifies searching within the EmapA module, Both a term search and a stage search

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




# Tests

class TestSearch(unittest.TestCase):
    """
    @status Test GXD Index browser search using J number, marker symbol, ???
    """

    def setUp(self):
        self.driver = webdriver.Firefox() 

    def testJnumSearch(self):
        """
        @Status tests that a basic J number search works
        @bug: test needs to capture user and dates
        """
        driver = self.driver
        driver.get(config.PWI_URL + "/edit/gxdindex")
        wait.forAjax(driver)
        time.sleep(1)
        jnumbox = driver.find_element_by_id('jnumid')
        # put your j number
        jnumbox.send_keys("173543")
        jnumbox.send_keys(Keys.RETURN)
        driver.find_element_by_id('searchButton').click()
        time.sleep(1)
        #finds the citation field
        cite_result = driver.find_element_by_id('citation').get_attribute('value')
        
        print cite_result
        self.assertEqual(cite_result, 'Harper J, Proc Natl Acad Sci U S A 2011 Jun 28;108(26):10585-90')
        time.sleep(1)
        #finds the marker field
        mrk_result = driver.find_element_by_id('marker_symbol').get_attribute('value')
        
        print mrk_result
        self.assertEqual(mrk_result, '1810065E05Rik')
        time.sleep(1)
        #finds the coded? field
        coded_result = driver.find_element_by_id('is_coded').get_attribute('value')
        
        print coded_result
        self.assertEqual(coded_result, 'false')
        time.sleep(1)
        #finds the priority field
        priority_result = driver.find_element_by_id('_priority_key').find_element_by_css_selector('#_priority_key option:checked')
        
        print priority_result
        self.assertEqual(priority_result.text, 'High')
        
        time.sleep(1)
        #finds the priority field
        condition_result = driver.find_element_by_id('_conditionalmutants_key').find_element_by_css_selector('#_conditionalmutants_key option:checked')
        
        print condition_result
        self.assertEqual(condition_result.text, 'Conditional')
        time.sleep(1)
        #finds the priority field
        created_user = driver.find_element_by_class_name('ng-binding')#.find_element_by_css_selector('td')
        
        print created_user
        self.assertEqual(created_user.text, 'jx')
        #term_result = self.driver.find_element_by_id("termResultList")
        #items = term_result.find_elements_by_tag_name("li")
        
        # add all li text to a list for "assertIn" test
        #searchTextItems = iterate.getTextAsList(items)
        
        #self.assertIn('brain TS17-28', searchTextItems)
        
    def testMarkerSearch(self):
        """
        @Status Tests that a marker symbol search works
        @bug: test needs to capture user and dates
        """
        driver = self.driver
        driver.get(config.PWI_URL + "/edit/gxdindex")
        wait.forAjax(driver)
        time.sleep(1)
        mrk_field = driver.find_element_by_id('marker_symbol')
        
        # put your marker symbol
        mrk_field.send_keys("Pax6")
        #mrk_field.send_keys(Keys.RETURN)
        driver.find_element_by_id('searchButton').click()     
        time.sleep(4)
        #finds the J number field
        jnum_result = driver.find_element_by_id('jnumid').get_attribute('value')
        
        print jnum_result
        self.assertEqual(jnum_result, 'J:193837')
        
        time.sleep(1)
        #finds the citation field
        cite_result = driver.find_element_by_id('citation').get_attribute('value')
        
        print cite_result
        self.assertEqual(cite_result, 'Abdelhamed ZA, Hum Mol Genet 2013 Apr 1;22(7):1358-72')
        time.sleep(1)
        time.sleep(1)
        #finds the coded? field
        coded_result = driver.find_element_by_id('is_coded').get_attribute('value')
        
        print coded_result
        self.assertEqual(coded_result, 'false')
        time.sleep(1)
        #finds the priority field
        priority_result = driver.find_element_by_id('_priority_key').find_element_by_css_selector('#_priority_key option:checked')
        
        print priority_result
        self.assertEqual(priority_result.text, 'Medium')
        
        time.sleep(1)
        #finds the priority field
        condition_result = driver.find_element_by_id('_conditionalmutants_key').find_element_by_css_selector('#_conditionalmutants_key option:checked')
        
        print condition_result
        self.assertEqual(condition_result.text, 'Not Applicable')
        time.sleep(1)
        
    def testWildcardSearch(self):
        """
        @Status tests that a wildcard  search works
        @bug test needs to be written
        """
        
        
    def closeAllWindows(self):
        """
        close all open windows for the current driver
        """
        for window_handle in self.driver.window_handles:
            self.driver.switch_to_window(window_handle)
            self.driver.close()
                
            
    def tearDown(self):
        self.closeAllWindows()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSearch))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()