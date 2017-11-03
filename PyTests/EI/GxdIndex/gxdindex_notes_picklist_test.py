
'''
Created on Oct 24, 2016

@author: jeffc
@attention: These tests must only be run against a development environment!!!
Test uses for notes picklist items
'''

import unittest
import time
from selenium import webdriver
import HTMLTestRunner
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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

class TestNotes(unittest.TestCase):
    """
    @status Test GXD Index browser for ability to modify marker and notes data, later will need to verify created and modified by/dates
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/gxdindex") 
        username = self.driver.find_element_by_name('user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = self.driver.find_element_by_name('password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = self.driver.find_element_by_name("submit") #Find the Login button
        submit.click() #click the login button
        
    def tearDown(self):
        self.driver.close()    
        

    def testSelectedNotes(self):
        """
        @Status tests that when you select an option for the notes field the correct option is added/displayed in the notes field, all options are tested
        
        """
        driver = self.driver
        form = self.form
        
        form.enter_value('jnumid', '225216')
        # click the Tab key
        form.press_tab()
        form.enter_value('marker_symbol', 'Bmp4')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print marker_symbol
        self.assertEqual(marker_symbol, 'Bmp4')
        form.click_search()
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Activated")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "The antibody used recognizes the activated form of the protein.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Cleaved")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "The antibody used recognizes the cleaved form of the protein.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Phosphorylated")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "The antibody used recognizes the phosphorylated form of the protein.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Ab/probe spec.")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "The specificity of the antibody/probe used was not detailed; both/all family members have been annotated.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Ab/probe spec. MGI ID")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "The antibody/probe specificity was not detailed and may recognize a related gene; (MGI:) has also been annotated.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("microRNA")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "The mature microRNA is encoded at multiple sites in the genome.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Supplementary")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "Results are in the supplementary material.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Section or WM")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "Reference does not indicate whether specimen is a section or whole mount.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Range")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "Authors state that expression was examined on dpc *-*; not all stages are detailed.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Primer spec")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "Primer specificity was not detailed and may amplify a related gene; several/all family members have been annotated.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Primer spec MGI ID")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "Primer specificity was not detailed and may amplify a related gene; (MGI:) has also been annotated.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Immunoprecipitated")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "The protein was immunoprecipitated prior to Western blotting.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Dot Blot")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "Northern data was obtained from a dot blot.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Enzymatic act")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "Enzymatic activity was used to detect gene expression.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Discrepancies")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "There are discrepancies between the text and the figure legend as to the age of the tissue/embryo.")
        
        form.get_value("comments")
        driver.find_element_by_id("clearNotesButton").click()
        Select(driver.find_element_by_id("noteSelect")).select_by_visible_text("Fractionated")
        notefield = form.get_value('comments')
        self.assertEqual(notefield, "The material used in the Western blot was fractionated.")
        
        
    def testAgeNotSpecified(self):
        """
        @Status tests that the notes field adds proper text when Age Not Specified button is clicked
        """
        driver = self.driver
        form = self.form
        
        form.enter_value('jnumid', '225216')
        # click the Tab key
        form.press_tab()
        #finds the marker field
        form.enter_value('marker_symbol', 'Bmp2')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print marker_symbol
        self.assertEqual(marker_symbol, 'Bmp2')
        form.click_search()
        self.driver.find_element_by_id('comments').clear()#clears the notes field
        self.driver.find_element_by_id("ageNotSpecifiedButton").click()
        agenote = form.get_value('comments')#Get what text is in the notes field
        self.assertEqual(agenote, "Age of embryo at noon of plug day not specified in reference.", "The note is incorrect")
        
    def testAgeNormalized(self):
        """
        @Status tests that the notes field adds proper text when Age Normalized button is clicked
        """
        driver = self.driver
        form = self.form
        
        form.enter_value('jnumid', '225216')
        # click the Tab key
        form.press_tab()
        #finds the marker field
        form.enter_value('marker_symbol', 'Bmp2')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print marker_symbol
        self.assertEqual(marker_symbol, 'Bmp2')
        form.click_search()
        self.driver.find_element_by_id('comments').clear()#clears the notes field
        self.driver.find_element_by_id("ageNormalizedButton").click()
        agenote = form.get_value('comments')#Get what text is in the notes field
        self.assertEqual(agenote, "Age normalized so that noon of plug day = E0.5.", "The note is incorrect")
        
    def testAgeAssigned(self):
        """
        @Status tests that the notes field properly adds text when Age Assigned button is clicked
        """
        driver = self.driver
        form = self.form
        
        form.enter_value('jnumid', '225216')
        # click the Tab key
        form.press_tab()
        #finds the marker field
        form.enter_value('marker_symbol', 'Bmp2')
        marker_symbol = form.get_value('marker_symbol')
        form.press_tab()
        print marker_symbol
        self.assertEqual(marker_symbol, 'Bmp2')
        form.click_search()
        self.driver.find_element_by_id('comments').clear()#clears the notes field
        self.driver.find_element_by_id("ageAssignedButton").click()
        agenote = form.get_value('comments')#Get what text is in the notes field
        self.assertEqual(agenote, "Age assigned by curator based on morphological criteria supplied by authors.", "The note is incorrect")
        

    
       
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestNotes))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main() 