'''
Created on Jan 28, 2016
This test verifies correct functioning of the clip board features within the EmapA module
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

from base_class import EmapaBaseClass

# Tests

class ClipboardTest(unittest.TestCase, EmapaBaseClass):
    """
    Tests various features connected with the clipboard.
    """

    def setUp(self):
        self.init()
        
        # logging in for all tests
        username = self.driver.find_element_by_name('user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = self.driver.find_element_by_name('password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = self.driver.find_element_by_name("submit") #Find the Login button
        submit.click() #click the login button
        

    def testOutRangeStage(self):        
        """
        @status adding a stage that is out of range for a selected term.
        """
        self.performSearch(term="brain")
        
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()
        
        wait.forAjax(self.driver)
        
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        
        wait.forAjax(self.driver)
        
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("16")
        clipbox.send_keys(Keys.RETURN)
        
        wait.forAjax(self.driver)
        
        errdisplay = self.driver.find_element_by_id("clipboardError")
        self.assertTrue(errdisplay.is_displayed(), "Error message not displaying")
        
    def testDuplicateStage(self):        
        """
        @status trying to add a duplicate term/stage to the clip board.
        """
        self.performSearch(term="brain")
        
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()
        wait.forAjax(self.driver)
        
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        wait.forAjax(self.driver)
        
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("18,19,20,20,21,22,23,24,25")
        clipbox.send_keys(Keys.RETURN) 
        wait.forAjax(self.driver)
        
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")       
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS18; brain", "TS19; brain", "TS20; brain", "TS21; brain", "TS22; brain", "TS23; brain", "TS24; brain", "TS25; brain"], searchTreeItems)
        
    def testSingleStage(self):   
        """
        @status adding a single stage to the clipboard.
        """
        self.performSearch(term="tail")
        
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()
        wait.forAjax(self.driver)
        
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        wait.forAjax(self.driver)
        
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("18")
        clipbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS18; tail"], searchTreeItems)
        
    def testCommaStages(self):    
        """
        @status adding stages to the clipboard separated by commas.
        """
        self.performSearch(term="epithelium")
        
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()
        wait.forAjax(self.driver)
        
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        wait.forAjax(self.driver)
        
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("15,16,17,19")
        clipbox.send_keys(Keys.RETURN) 
        wait.forAjax(self.driver)
        
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")       
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS15; epithelium", "TS16; epithelium", "TS17; epithelium", "TS19; epithelium"], searchTreeItems)
        
    def testDashStages(self):   
        """
        @status adding stages to the clip board separated by a dash.
        """
        self.performSearch(term="neck")
        
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()
        wait.forAjax(self.driver)
        
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        wait.forAjax(self.driver)
        
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("22-25")
        clipbox.send_keys(Keys.RETURN) 
        wait.forAjax(self.driver)
        
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")       
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS22; neck", "TS23; neck", "TS24; neck", "TS25; neck"], searchTreeItems)
        
    def testWildcardStage(self):   
        """
        @status adding all stages to clip board using a *.
        """
        self.performSearch(term="epiblast")
        
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()
        wait.forAjax(self.driver)
        
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        wait.forAjax(self.driver)
        
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("*")
        clipbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")       
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS6; epiblast", "TS7; epiblast", "TS8; epiblast"], searchTreeItems)
        
    def testNonNumberStage(self):
        """
        @status trying to add a stage to the clip board using a non-numeric number.
        """
        self.performSearch(term="epiblast")
        
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()   
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("seven")
        clipbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        errdisplay = self.driver.find_element_by_id("clipboardError")
        self.assertTrue(errdisplay.is_displayed(), "Error message not displaying")
        
    def testInvalidRange(self):   
        """
        @status trying to add stages to the clipboard using an invalid range.
        """
        self.performSearch(term="epiblast")
        
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()
        wait.forAjax(self.driver)
        
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("8-6")
        clipbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)

        errdisplay = self.driver.find_element_by_id("clipboardError")
        self.assertTrue(errdisplay.is_displayed(), "Error message not displaying")
        
    def testdeleteoneclipboard(self):   
        """
        @status tests you can delete one item from the clipboard.
        """
        self.performSearch(term="emb%")
        
        result = self.driver.find_element_by_id("termResultList").find_elements_by_link_text("embryo")
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        wait.forAjax(self.driver)
        
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("4-5")
        clipbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        
        self.assertEqual(["TS4; embryo", "TS5; embryo"], searchTreeItems)
        items[1].click()
        wait.forAjax(self.driver)
        
        self.driver.find_element_by_xpath("//*[@id='clipboard']/li[2]/img").click()
        wait.forAjax(self.driver)
        
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS4; embryo"], searchTreeItems)
        
    def testdeletemultclipboard(self):    
        """
        @status tests you can delete multiple items from the clipboard.
        """
        self.performSearch(term="neck")
        
        result = self.driver.find_element_by_id("termResultList").find_elements_by_link_text("embryo")
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        wait.forAjax(self.driver)
        
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("23-27")
        clipbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        
        self.assertEqual(["TS23; neck","TS24; neck","TS25; neck","TS26; neck","TS27; neck"], searchTreeItems)
        items[1].click()
        self.driver.find_element_by_xpath("//*[@id='clipboard']/li[2]/img").click()
        items[2].click()
        self.driver.find_element_by_xpath("//*[@id='clipboard']/li[3]/img").click()
        items[3].click()
        self.driver.find_element_by_xpath("//*[@id='clipboard']/li[4]/img").click()
        wait.forAjax(self.driver)
        
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS23; neck","TS27; neck"], searchTreeItems)
        

    def testClpboardBasicSort(self):
        """
        @status tests that a basic sort works by displaying the clip board results in smart alpha order.
        """
        self.performSearch(term="emb%")
        
        result = self.driver.find_element_by_id("termResultList").find_elements_by_link_text("embryo")
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        wait.forAjax(self.driver)
        
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("5-7")
        clipbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)

        self.assertEqual(["TS5; embryo","TS6; embryo","TS7; embryo"], searchTreeItems)
        clipbox.clear()
        
        # do a new search for endoderm
        self.performSearch(term="endoderm")
        
        result = self.driver.find_element_by_id("termResultList").find_elements_by_link_text("embryo")

        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("6-8")
        clipbox.send_keys(Keys.RETURN)
        wait.forAjax(self.driver)
        
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS5; embryo","TS6; embryo","TS7; embryo","TS6; endoderm","TS7; endoderm","TS8; endoderm"], searchTreeItems)
        sort = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardSort")
        sort.click()
        wait.forAjax(self.driver)
        
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS5; embryo","TS6; embryo","TS6; endoderm","TS7; embryo","TS7; endoderm","TS8; endoderm"], searchTreeItems)
        
            
    def tearDown(self):
        self.closeAllWindows()
        
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ClipboardTest))
    return suite


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
