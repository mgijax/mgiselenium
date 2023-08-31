
'''
Created on Oct 24, 2016
@author: jeffc
@attention: These tests must only be run against a development environment!!!
Test uses for notes picklist items
Verify that Pick List options for the notes field are all correct by verifying each option's text
Verify that the notes field adds proper text when Age Not Specified button is clicked
Verify that the notes field adds proper text when Age Normalized button is clicked
Verify that the notes field properly adds text when Age Assigned button is clicked
'''

import unittest
import time
from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
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

class TestEiGxdIndexNotesPicklist(unittest.TestCase):
    """
    @status Test GXD Index browser for ability to modify marker and notes data, later will need to verify created and modified by/dates
    """

    def setUp(self):
        self.driver = webdriver.Firefox() 
        #self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/gxdindex") 
        username = self.driver.find_element(By.NAME, 'user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = self.driver.find_element(By.NAME, 'password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = self.driver.find_element(By.NAME, "submit") #Find the Login button
        submit.click() #click the login button
        
    def tearDown(self):
        self.driver.close()    
        

    def testSelectedNotes(self):
        """
        @Status tests that Pick List options for the notes field are all correct by verifying each option's text
        
        """
        driver = self.driver
        form = self.form
        time.sleep(2)
        form.enter_value('jnumID', 'J:320934')
        # click the Tab key
        form.press_tab()
        form.enter_value('markerSymbol', 'Pax3')
        marker_symbol = form.get_value('markerSymbol')
        form.press_tab()
        print(marker_symbol)
        self.assertEqual(marker_symbol, 'Pax3')
        form.click_search()
        form.get_value("note")
        #identify the pick list dropdown list
        pick_list = self.driver.find_element(By.ID, "notePickList")
        items = pick_list.find_elements(By.TAG_NAME, "option")
        for item in items:
            text = item.text
            print(text)
        self.assertEqual(items[1].text, "Activated", "Term 1 is not visible!")
        self.assertEqual(items[2].text, "Cleaved", "Term 2 is not visible!")
        self.assertEqual(items[3].text, "Phosphorylated", "Term 3 is not visible!")
        self.assertEqual(items[4].text, "Ab/probe spec.", "Term 4 is not visible!")
        self.assertEqual(items[5].text, "Ab/probe spec. MGI ID", "Term 5 is not visible!")
        self.assertEqual(items[6].text, "microRNA", "Term 6 is not visible!")
        self.assertEqual(items[7].text, "Supplementary", "Term 7 is not visible!")
        self.assertEqual(items[8].text, "Section or WM", "Term 8 is not visible!")
        self.assertEqual(items[9].text, "Range", "Term 9 is not visible!")
        self.assertEqual(items[10].text, "Primer spec", "Term 10 is not visible!")
        self.assertEqual(items[11].text, "Primer spec MGI ID", "Term 11 is not visible!")
        self.assertEqual(items[12].text, "Immunoprecipitated", "Term 12 is not visible!")
        self.assertEqual(items[13].text, "Dot Blot", "Term 13 is not visible!")
        self.assertEqual(items[14].text, "Enzymatic act", "Term 14 is not visible!")
        self.assertEqual(items[15].text, "Discrepancies", "Term 15 is not visible!")
        self.assertEqual(items[16].text, "Fractionated", "Term 16 is not visible!")        
        
        
    def testAgeNotSpecified(self):
        """
        @Status tests that the notes field adds proper text when Age Not Specified button is clicked
        """
        driver = self.driver
        form = self.form
        time.sleep(2)
        form.enter_value('jnumID', '225216')
        # click the Tab key
        form.press_tab()
        #finds the marker field
        form.enter_value('markerSymbol', 'Bmp2')
        marker_symbol = form.get_value('markerSymbol')
        form.press_tab()
        print(marker_symbol)
        self.assertEqual(marker_symbol, 'Bmp2')
        form.click_search()
        self.driver.find_element(By.ID, 'note').clear()#clears the notes field
        self.driver.find_element(By.ID, "ageNotSpecifiedButton").click()
        agenote = form.get_value('note')#Get what text is in the notes field
        self.assertEqual(agenote, "Age of embryo at noon of plug day not specified in reference.", "The note is incorrect")
        
    def testAgeNormalized(self):    
        """
        @Status tests that the notes field adds proper text when Age Normalized button is clicked
        """
        driver = self.driver
        form = self.form
        time.sleep(2)
        form.enter_value('jnumID', '225216')
        # click the Tab key
        form.press_tab()
        #finds the marker field
        form.enter_value('markerSymbol', 'Bmp2')
        marker_symbol = form.get_value('markerSymbol')
        form.press_tab()
        print(marker_symbol)
        self.assertEqual(marker_symbol, 'Bmp2')
        form.click_search()
        self.driver.find_element(By.ID, 'note').clear()#clears the notes field
        self.driver.find_element(By.ID, "ageNormalizedButton").click()
        agenote = form.get_value('note')#Get what text is in the notes field
        self.assertEqual(agenote, "Age normalized so that noon of plug day = E0.5.", "The note is incorrect")
        
    def testAgeAssigned(self):
        """
        @Status tests that the notes field properly adds text when Age Assigned button is clicked
        """
        driver = self.driver
        form = self.form
        time.sleep(2)
        form.enter_value('jnumID', '225216')
        # click the Tab key
        form.press_tab()
        #finds the marker field
        form.enter_value('markerSymbol', 'Bmp2')
        marker_symbol = form.get_value('markerSymbol')
        form.press_tab()
        print(marker_symbol)
        self.assertEqual(marker_symbol, 'Bmp2')
        form.click_search()
        self.driver.find_element(By.ID, 'note').clear()#clears the notes field
        self.driver.find_element(By.ID, "ageAssignedButton").click()
        agenote = form.get_value('note')#Get what text is in the notes field
        self.assertEqual(agenote, "Age assigned by curator based on morphological criteria supplied by authors.", "The note is incorrect")

       
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiGxdIndexNotesPicklist))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests')) 