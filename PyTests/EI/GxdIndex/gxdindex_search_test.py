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
from util.form import ModuleForm




# Tests

class TestSearch(unittest.TestCase):
    """
    @status Test GXD Index browser search using J number, marker symbol, ???
    """

    def setUp(self):
        self.driver = webdriver.Firefox() 
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.PWI_URL + "/edit/gxdindex")
    
    def tearDown(self):
        self.driver.close()
        

    def testJnumSearch(self):
        """
        @Status tests that a basic J number search works
        @bug: test needs to capture user and dates
        """
        driver = self.driver
        form = self.form
        
        form.enter_value('jnumid', '173543')
        form.click_search()
        
        #finds the citation field
        citation = form.get_value('citation')
        
        print citation
        self.assertEqual(citation, 'Harper J, Proc Natl Acad Sci U S A 2011 Jun 28;108(26):10585-90')

        #finds the marker field
        marker_symbol = form.get_value('marker_symbol')
        
        print marker_symbol
        self.assertEqual(marker_symbol, '1810065E05Rik')

        #finds the coded? field
        is_coded = form.get_value('is_coded')
        
        print is_coded
        self.assertEqual(is_coded, 'false')

        #finds the priority field
        priority = form.get_selected_text('_priority_key')
        
        print priority
        self.assertEqual(priority, 'High')
        

        #finds the conditional mutants field
        conditional = form.get_selected_text('_conditionalmutants_key')
        
        print conditional
        self.assertEqual(conditional, 'Conditional')

        #finds the priority field
        created_user = driver.find_element_by_id('createdby_login')
        
        print created_user
        self.assertEqual(created_user.text, 'jx')
        
        
    def testInvalidJnumSearch(self):
        """
        @Status tests that an invalid J number search gives an error
        @bug test needs to be written
        """
        form = self.form
        form.enter_value('jnumid', "99999999")
        form.press_tab()
        
        error = form.get_error_message()
        
        self.assertEqual("No Reference for J Number=J:99999999", error)
        
        
    def testMarkerSearch(self):
        """
        @Status Tests that a marker symbol search works
        @bug: test needs to capture user and dates
        """
        driver = self.driver
        form = self.form
        
        form.enter_value('marker_symbol', 'Pax6')
        form.click_search()
        
        #finds the J number field
        jnumid = form.get_value('jnumid')
        
        print jnumid
        self.assertEqual(jnumid, 'J:193837')
        

        #finds the citation field
        citation = form.get_value('citation')
        
        print citation
        self.assertEqual(citation, 'Abdelhamed ZA, Hum Mol Genet 2013 Apr 1;22(7):1358-72')

        #finds the coded? field
        is_coded = form.get_value('is_coded')
        
        print is_coded
        self.assertEqual(is_coded, 'false')
 
        #finds the priority field
        priority = form.get_selected_text('_priority_key')
        
        print priority
        self.assertEqual(priority, 'Medium')
        
 
        #finds the conditional field
        conditional = form.get_selected_text('_conditionalmutants_key')
        
        print conditional
        self.assertEqual(conditional, 'Not Applicable')
 
        
    def testWildcardSearch(self):
        """
        @Status tests that a wildcard search for a marker works
        @bug test needs to be written
        """
        
    def testWithdrawnMrkSearch(self):
        """
        @Status tests that a search for a withdrawn marker gives an error
        @bug test needs to be written
        """
        
    def testInvalidMrkSearch(self):
        """
        @Status tests that an error message is displayed when invalid marker symbol entered
        @bug test needs to be written
        """
        
    def testQTLErrorMsg(self):
        """
        @Status tests that an error message is displayed when selecting a heritable phenotypic marker or QTL
        @bug test needs to be written
        """
        
    def testMultipleMrkSearch(self):
        """
        @Status tests that a multiple marker search works
        @bug test needs to be written
        """
    


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSearch))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()