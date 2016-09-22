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




# Tests

class TestAdd(unittest.TestCase):
    """
    @status Test GXD Index browser for ability to add an index
    """

    def setUp(self):
        self.driver = webdriver.Firefox() 
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.PWI_URL + "/edit/gxdindex")

    def testAddIndex(self):
        """
        @Status tests that an index record can be added
        @bug: test under construction
        """
        driver = self.driver
        form = self.form
        
        form.enter_value('jnumid', '173543')
        # click the Tab key
        form.press_tab()
        
        #finds the citation field
        citation = form.get_value('citation')
        
        print citation
        self.assertEqual(citation, 'Harper J, Proc Natl Acad Sci U S A 2011 Jun 28;108(26):10585-90')

        #finds the marker field
        form.enter_value('marker_symbol', 'gata1')
        marker_symbol = form.get_value('marker_symbol')
        
        form.press_tab()
        print marker_symbol
        self.assertEqual(marker_symbol, 'gata1')

        #finds the coded? field
        #is_coded = form.get_value('is_coded')
        
        #print is_coded
        #self.assertEqual(is_coded, 'false')

        #finds the priority field
        #priority = form.get_selected_text('_priority_key')
        
        #print priority
        #self.assertEqual(priority, 'High')
        

        #finds the conditional mutants field
        #conditional = form.get_selected_text('_conditionalmutants_key')
        
        #print conditional
        #self.assertEqual(conditional, 'Conditional')

        #finds the created by field
        #created_user = driver.find_element_by_id('createdby_login')
        
        #print created_user
        #self.assertEqual(created_user.text, 'jx')

        
        #finds the modified by field
        #modified_user = driver.find_element_by_id('modifiedby_login')#.find_element_by_css_selector('td')
        
        #print modified_user
        #self.assertEqual(modified_user.text, 'jx')
        
        #finds the created by date field
        #created_date = form.get_value('creation_date')
        
        #print created_date
        #self.assertEqual(created_date, '07/26/2011')
        
        #finds the created by date field
        #modified_date = form.get_value('modification_date')
        
        #print modified_date
        #self.assertEqual(modified_date, '12/12/2011')
        

    
    def tearDown(self):
        self.driver.close()
       
       
       
       
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAdd))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main() 