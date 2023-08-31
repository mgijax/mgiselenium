'''
Created on Jan 28, 2016
This test verifies correct functioning of the clip board features within the EmapA module
@author: jeffc
Verify trying to add a duplicate term/stage to the clip board
Verify adding a single stage to the clipboard
Verify adding stages to the clipboard separated by commas
Verify adding stages to the clip board separated by a dash
Verify adding all stages to clip board using a *
Verify trying to add a stage to the clip board using a non-numeric number
Verify trying to add stages to the clipboard using an invalid range
Verify you can delete one item from the clipboard
Verify you can delete multiple items from the clipboard
Verify that a basic sort works by displaying the clip board results in smart alpha order
Verify confirm the shortcut keys(CTRL + ALT + k) resets the clipboard input box
'''
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config

from util import iterate, wait
from util.form import ModuleForm
from util.table import Table
import time
# Tests

class TestEiEmapaClipboard(unittest.TestCase):
    """
    Tests various features connected with the clipboard.
    """

    def setUp(self):
        self.driver = webdriver.Firefox() 
        #self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/emapaBrowser")        
        # logging in for all tests
        username = self.driver.find_element(By.NAME, 'user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        time.sleep(4)
        passwd = self.driver.find_element(By.NAME, 'password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        time.sleep(4)
        submit = self.driver.find_element(By.NAME, "submit") #Find the Login button
        submit.click() #click the login button
        time.sleep(1)
   
    def tearDown(self):
        self.driver.close()        

    """def testOutRangeStage(self):        
        
        @status adding a stage that is out of range for a selected term.
        this test no longer works because no error message gets displayed just nothing placed  in clipboard
                
        wait.forAngular(self.driver)
        #find the "Term Search" box and enter the term brain 
        self.driver.find_element(By.ID, "termSearch").send_keys('brain')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        result = self.driver.find_element(By.ID, "termResultList").find_element(By.CSS_SELECTOR, "mark")
        result.click()
        wait.forAngular(self.driver)
        
        clear = self.driver.find_element(By.ID, "clipboardFunctions").find_element(By.ID, "clipboardClear")
        clear.click()
        
        wait.forAngular(self.driver)
        
        clipbox = self.driver.find_element(By.ID, "clipboardInput")
        clipbox.send_keys("16")
        clipbox.send_keys(Keys.RETURN)
        #Click the 'Add to Clipboard' button
        self.driver.find_element(By.ID, 'addClipboardButton').click()
        wait.forAngular(self.driver)
        
        errdisplay = self.driver.find_element(By.ID, "errorMessage")
        self.assertTrue(errdisplay.is_displayed(), "Error message not displaying")
        """ 
    def testDuplicateStage(self):        
        """
        @status trying to add a duplicate term/stage to the clip board.
        """
        #find the "Term Search" box and enter the term brain 
        self.driver.find_element(By.ID, "termSearch").send_keys('brain')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        result = self.driver.find_element(By.ID, "termResultList").find_element(By.CSS_SELECTOR, "mark")
        result.click()
        wait.forAngular(self.driver)
        
        clear = self.driver.find_element(By.ID, "clipboardFunctions").find_element(By.ID, "clipboardClear")
        clear.click()
        wait.forAngular(self.driver)
        
        clipbox = self.driver.find_element(By.ID, "clipboardInput")
        clipbox.send_keys("18,19,20,20,21,22,23,24,25")
        self.driver.find_element(By.ID, 'addClipboardButton').click()
        #clipbox.send_keys(Keys.RETURN) 
        wait.forAngular(self.driver)
        
        clipsort = self.driver.find_element(By.ID, "emapClipBoardContent").find_element(By.ID, "clipboard")       
        items = clipsort.find_elements(By.CSS_SELECTOR, "li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS18; brain", "TS19; brain", "TS20; brain", "TS21; brain", "TS22; brain", "TS23; brain", "TS24; brain", "TS25; brain"], searchTreeItems)
        
    def testSingleStage(self):   
        """
        @status adding a single stage to the clipboard.
        """
        #find the "Term Search" box and enter the term tail 
        self.driver.find_element(By.ID, "termSearch").send_keys('tail')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)        
        result = self.driver.find_element(By.ID, "termResultList").find_element(By.CSS_SELECTOR, "mark")
        result.click()
        wait.forAngular(self.driver)
        
        clear = self.driver.find_element(By.ID, "clipboardFunctions").find_element(By.ID, "clipboardClear")
        clear.click()
        wait.forAngular(self.driver)
        
        clipbox = self.driver.find_element(By.ID, "clipboardInput")
        clipbox.send_keys("18")
        clipbox.send_keys(Keys.RETURN)
        wait.forAngular(self.driver)
        
        clipsort = self.driver.find_element(By.ID, "emapClipBoardContent").find_element(By.ID, "clipboard")
        items = clipsort.find_elements(By.CSS_SELECTOR, "li")
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS18; tail"], searchTreeItems)
        
    def testCommaStages(self):    
        """
        @status adding stages to the clipboard separated by commas.
        """
        #find the "Term Search" box and enter the term epithelium 
        self.driver.find_element(By.ID, "termSearch").send_keys('epithelium')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        result = self.driver.find_element(By.ID, "termResultList").find_element(By.CSS_SELECTOR, "mark")
        result.click()
        wait.forAngular(self.driver)
        
        clear = self.driver.find_element(By.ID, "clipboardFunctions").find_element(By.ID, "clipboardClear")
        clear.click()
        wait.forAngular(self.driver)
        
        clipbox = self.driver.find_element(By.ID, "clipboardInput")
        clipbox.send_keys("15,16,17,19")
        clipbox.send_keys(Keys.RETURN) 
        wait.forAngular(self.driver)
        
        clipsort = self.driver.find_element(By.ID, "emapClipBoardContent").find_element(By.ID, "clipboard")       
        items = clipsort.find_elements(By.CSS_SELECTOR, "li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS15; epithelium", "TS16; epithelium", "TS17; epithelium", "TS19; epithelium"], searchTreeItems)
        
    def testDashStages(self):   
        """
        @status adding stages to the clip board separated by a dash.
        """
        #find the "Term Search" box and enter the term neck 
        self.driver.find_element(By.ID, "termSearch").send_keys('neck')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        result = self.driver.find_element(By.ID, "termResultList").find_element(By.CSS_SELECTOR, "mark")
        result.click()
        wait.forAngular(self.driver)
        
        clear = self.driver.find_element(By.ID, "clipboardFunctions").find_element(By.ID, "clipboardClear")
        clear.click()
        wait.forAngular(self.driver)
        
        clipbox = self.driver.find_element(By.ID, "clipboardInput")
        clipbox.send_keys("22-25")
        clipbox.send_keys(Keys.RETURN) 
        wait.forAngular(self.driver)
        
        clipsort = self.driver.find_element(By.ID, "emapClipBoardContent").find_element(By.ID, "clipboard")       
        items = clipsort.find_elements(By.CSS_SELECTOR, "li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS22; neck", "TS23; neck", "TS24; neck", "TS25; neck"], searchTreeItems)
        
    def testWildcardStage(self):   
        """
        @status adding all stages to clip board using a *.
        """
        #find the "Term Search" box and enter the term epiblast 
        self.driver.find_element(By.ID, "termSearch").send_keys('epiblast')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        result = self.driver.find_element(By.ID, "termResultList").find_element(By.CSS_SELECTOR, "mark")
        result.click()
        wait.forAngular(self.driver)
        
        clear = self.driver.find_element(By.ID, "clipboardFunctions").find_element(By.ID, "clipboardClear")
        clear.click()
        wait.forAngular(self.driver)
        
        clipbox = self.driver.find_element(By.ID, "clipboardInput")
        clipbox.send_keys("*")
        clipbox.send_keys(Keys.RETURN)
        wait.forAngular(self.driver)
        
        clipsort = self.driver.find_element(By.ID, "emapClipBoardContent").find_element(By.ID, "clipboard")       
        items = clipsort.find_elements(By.CSS_SELECTOR, "li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS6; epiblast", "TS7; epiblast", "TS8; epiblast"], searchTreeItems)
        
    def testNonNumberStage(self):
        """
        @status trying to add a stage to the clip board using a non-numeric number.
        """
        #find the "Term Search" box and enter the term brain 
        self.driver.find_element(By.ID, "termSearch").send_keys('epiblast')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        result = self.driver.find_element(By.ID, "termResultList").find_element(By.CSS_SELECTOR, "mark")
        result.click()   
        clipbox = self.driver.find_element(By.ID, "clipboardInput")
        clipbox.send_keys("seven")
        clipbox.send_keys(Keys.RETURN)
        wait.forAngular(self.driver)
        
        errdisplay = self.driver.find_element(By.ID, "errorMessage")
        self.assertTrue(errdisplay.is_displayed(), "Error message not displaying")
        
    def testInvalidRange(self):   
        """
        @status trying to add stages to the clipboard using an invalid range.
        """
        #find the "Term Search" box and enter the term epiblast 
        self.driver.find_element(By.ID, "termSearch").send_keys('epiblast')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        result = self.driver.find_element(By.ID, "termResultList").find_element(By.CSS_SELECTOR, "mark")
        result.click()
        wait.forAngular(self.driver)
        
        clipbox = self.driver.find_element(By.ID, "clipboardInput")
        clipbox.send_keys("8-6")
        clipbox.send_keys(Keys.RETURN)
        wait.forAngular(self.driver)

        errdisplay = self.driver.find_element(By.ID, "errorMessage")
        self.assertTrue(errdisplay.is_displayed(), "Error message not displaying")
        
    def testdeleteoneclipboard(self):   
        """
        @status tests you can delete one item from the clipboard.
        """
        #find the "Term Search" box and enter the term emb% 
        self.driver.find_element(By.ID, "termSearch").send_keys('emb%')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        result = self.driver.find_element(By.ID, "termResultList").find_elements(By.LINK_TEXT, "embryo")
        clear = self.driver.find_element(By.ID, "clipboardFunctions").find_element(By.ID, "clipboardClear")
        clear.click()
        wait.forAngular(self.driver)
        
        clipbox = self.driver.find_element(By.ID, "clipboardInput")
        clipbox.send_keys("4-5")
        clipbox.send_keys(Keys.RETURN)
        wait.forAngular(self.driver)
        
        clipsort = self.driver.find_element(By.ID, "emapClipBoardContent").find_element(By.ID, "clipboard")
        items = clipsort.find_elements(By.CSS_SELECTOR, "li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        
        self.assertEqual(["TS4; embryo", "TS5; embryo"], searchTreeItems)
        items[1].click()
        wait.forAngular(self.driver)
        
        self.driver.find_element(By.XPATH, "//*[@id='clipboard']/li[2]/img").click()
        wait.forAngular(self.driver)
        
        clipsort = self.driver.find_element(By.ID, "emapClipBoardContent").find_element(By.ID, "clipboard")
        items = clipsort.find_elements(By.CSS_SELECTOR, "li")
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS4; embryo"], searchTreeItems)
        
    def testDeleteMultClipboard(self):    
        """
        @status tests you can delete multiple items from the clipboard.
        """
        #find the "Term Search" box and enter the term neck 
        self.driver.find_element(By.ID, "termSearch").send_keys('neck')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        clear = self.driver.find_element(By.ID, "clipboardFunctions").find_element(By.ID, "clipboardClear")
        clear.click()
        wait.forAngular(self.driver)
        
        clipbox = self.driver.find_element(By.ID, "clipboardInput")
        clipbox.send_keys("23-27")
        clipbox.send_keys(Keys.RETURN)
        wait.forAngular(self.driver)
        
        clipsort = self.driver.find_element(By.ID, "emapClipBoardContent").find_element(By.ID, "clipboard")
        items = clipsort.find_elements(By.CSS_SELECTOR, "li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS23; neck","TS24; neck","TS25; neck","TS26; neck","TS27; neck"], searchTreeItems)
        
        # TS24; neck
        self.driver.find_element(By.XPATH, "//*[@id='clipboard']/li[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id='clipboard']/li[2]/img").click()
        wait.forAngular(self.driver)
        # TS25; neck
        self.driver.find_element(By.XPATH, "//*[@id='clipboard']/li[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id='clipboard']/li[2]/img").click()
        wait.forAngular(self.driver)
        # TS26; neck
        self.driver.find_element(By.XPATH, "//*[@id='clipboard']/li[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id='clipboard']/li[2]/img").click()
        wait.forAngular(self.driver)
        
        clipsort = self.driver.find_element(By.ID, "emapClipBoardContent").find_element(By.ID, "clipboard")
        items = clipsort.find_elements(By.CSS_SELECTOR, "li")
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS23; neck","TS27; neck"], searchTreeItems)
        

    def testClipboardBasicSort(self):
        """
        @status tests that a basic sort works by displaying the clip board results in smart alpha order.
        """
        #find the "Term Search" box and enter the term emb% 
        self.driver.find_element(By.ID, "termSearch").send_keys('emb%')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        result = self.driver.find_element(By.ID, "termResultList").find_elements(By.LINK_TEXT, "embryo")
        clear = self.driver.find_element(By.ID, "clipboardFunctions").find_element(By.ID, "clipboardClear")
        clear.click()
        wait.forAngular(self.driver)
        
        clipbox = self.driver.find_element(By.ID, "clipboardInput")
        clipbox.send_keys("5-7")
        clipbox.send_keys(Keys.RETURN)
        wait.forAngular(self.driver)
        
        clipsort = self.driver.find_element(By.ID, "emapClipBoardContent").find_element(By.ID, "clipboard")
        items = clipsort.find_elements(By.CSS_SELECTOR, "li")
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)

        self.assertEqual(["TS5; embryo","TS6; embryo","TS7; embryo"], searchTreeItems)
        clipbox.clear()
        #find the Clear button and click it to clear the form
        self.driver.find_element(By.ID, "formClear").click()
        # do a new search for endoderm
        #find the "Term Search" box and enter the term endoderm 
        self.driver.find_element(By.ID, "termSearch").send_keys('endoderm')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        result = self.driver.find_element(By.ID, "termResultList").find_elements(By.LINK_TEXT, "endoderm")

        clipbox = self.driver.find_element(By.ID, "clipboardInput")
        clipbox.send_keys("6-8")
        clipbox.send_keys(Keys.RETURN)
        wait.forAngular(self.driver)
        
        clipsort = self.driver.find_element(By.ID, "emapClipBoardContent").find_element(By.ID, "clipboard")
        items = clipsort.find_elements(By.CSS_SELECTOR, "li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS5; embryo","TS6; embryo","TS7; embryo","TS6; endoderm","TS7; endoderm","TS8; endoderm"], searchTreeItems)
        sort = self.driver.find_element(By.ID, "clipboardFunctions").find_element(By.ID, "clipboardSort")
        sort.click()
        wait.forAngular(self.driver)
        
        clipsort = self.driver.find_element(By.ID, "emapClipBoardContent").find_element(By.ID, "clipboard")
        items = clipsort.find_elements(By.CSS_SELECTOR, "li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["TS5; embryo","TS6; embryo","TS6; endoderm","TS7; embryo","TS7; endoderm","TS8; endoderm"], searchTreeItems)
        
    def testClipboardShortcut(self):   
        """
        @status confirm the shortcut keys(CTRL + ALT + k) resets the clipboard input box
        """
        actions = ActionChains(self.driver)
        #find the "Term Search" box and enter the term tail 
        self.driver.find_element(By.ID, "termSearch").send_keys('tail')
        time.sleep(2)
        #find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        wait.forAngular(self.driver)
        result = self.driver.find_element(By.ID, "termResultList").find_element(By.CSS_SELECTOR, "mark")
        result.click()
        wait.forAngular(self.driver)
        #clear all items in the clipboard
        clear = self.driver.find_element(By.ID, "clipboardFunctions").find_element(By.ID, "clipboardClear")
        clear.click()
        #Add 18 into the add to clipboard field
        clipbox = self.driver.find_element(By.ID, "clipboardInput")
        clipbox.send_keys("18")
        clipbox.send_keys(Keys.RETURN)
        time.sleep(2)
        clipdata = self.driver.find_element(By.ID, "emapClipBoardContent").find_element(By.ID, "clipboard")
        items = clipdata.find_elements(By.CSS_SELECTOR, "li")
        searchTreeItems = iterate.getTextAsList(items)
        #assert that TS18 tail is displayed in the clipboard
        self.assertEqual(["TS18; tail"], searchTreeItems)
        #clear the clipboard using the shortcut keys
        actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('k').key_up(Keys.CONTROL).key_up(Keys.ALT).perform()
        time.sleep(5)
         
        clipdata = self.driver.find_element(By.ID, "emapClipBoardContent")
        items = clipdata.find_elements(By.CSS_SELECTOR, "li")
        searchTreeItems = iterate.getTextAsList(items)
        #Assert that the clipboard is empty
        self.assertEqual([], searchTreeItems)
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiEmapaClipboard))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
