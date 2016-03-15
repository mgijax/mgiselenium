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
  os.path.join(os.path.dirname(__file__), '../../../config',)
)
import config

# Constants
BROWSER_URL = config.PWI_URL + "/edit/emapBrowser"

# Tests

class ClipboardTest(unittest.TestCase):
    """
    Tests various features connected with the clipboard.
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(config.PWI_URL)
        self.driver.implicitly_wait(10)
        
        # logging in for all tests
        username = self.driver.find_element_by_name('user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = self.driver.find_element_by_name('password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = self.driver.find_element_by_name("submit") #Find the Login button
        submit.click() #click the login button
        
        self.driver.get(BROWSER_URL)

    def testOutRangeStage(self):        
        """adding a stage that is out of range for a selected term. This test works!
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("brain")
        searchbox.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        time.sleep(5)
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("16")
        clipbox.send_keys(Keys.RETURN)
        time.sleep(5)
        errdisplay = self.driver.find_element_by_id("clipboardError")
        self.assertTrue(errdisplay.is_displayed(), "Error message not displaying")
        
    def testDuplicateStage(self):        
        """trying to add a duplicate term/stage to the clip board, this test is working!
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("brain")
        searchbox.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        time.sleep(5)
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("18,19,20,20,21,22,23,24,25")
        clipbox.send_keys(Keys.RETURN) 
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")       
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(items)
        print items
        self.assertEqual(["TS18; brain", "TS19; brain", "TS20; brain", "TS21; brain", "TS22; brain", "TS23; brain", "TS24; brain", "TS25; brain"], searchTreeItems)
        
    def testSingleStage(self):   
        """adding a single stage to the clipboard, this test works
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("tail")
        searchbox.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        time.sleep(5)
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("18")
        clipbox.send_keys(Keys.RETURN)
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(items)
        print items
        self.assertEqual(["TS18; tail"], searchTreeItems)
        
    def testCommaStages(self):    
        """adding stages to the clipboard separated by commas, this test works
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("epithelium")
        searchbox.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        time.sleep(5)
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("15,16,17,19")
        clipbox.send_keys(Keys.RETURN) 
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")       
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(items)
        print items
        self.assertEqual(["TS15; epithelium", "TS16; epithelium", "TS17; epithelium", "TS19; epithelium"], searchTreeItems)
        
    def testDashStages(self):   
        """adding stages to the clip board separated by a dash, this test works!
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("neck")
        searchbox.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        time.sleep(5)
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("22-25")
        clipbox.send_keys(Keys.RETURN) 
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")       
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(items)
        print items
        self.assertEqual(["TS22; neck", "TS23; neck", "TS24; neck", "TS25; neck"], searchTreeItems)
        
    def testWildcardStage(self):   
        """adding all stages to clip board using a *, this test works!
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("epiblast")
        searchbox.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        time.sleep(5)
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("*")
        clipbox.send_keys(Keys.RETURN)
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")       
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(items)
        print items
        time.sleep(5)
        self.assertEqual(["TS6; epiblast", "TS7; epiblast", "TS8; epiblast"], searchTreeItems)
        
    def testNonNumberStage(self):
        """trying to add a stage to the clip board using a non-numeric number, test works!
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("epiblast")
        searchbox.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()   
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("seven")
        clipbox.send_keys(Keys.RETURN)
        time.sleep(5)
        errdisplay = self.driver.find_element_by_id("clipboardError")
        self.assertTrue(errdisplay.is_displayed(), "Error message not displaying")
        
    def testInvalidRange(self):   
        """trying to add stages to the clipboard using an invalid range, test works!
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("epiblast")
        searchbox.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_id("termResultList").find_element_by_css_selector("mark")
        result.click()
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("8-6")
        clipbox.send_keys(Keys.RETURN)
        time.sleep(10)
        errdisplay = self.driver.find_element_by_id("clipboardError")
        self.assertTrue(errdisplay.is_displayed(), "Error message not displaying")
        
    def testdeleteoneclipboard(self):   
        """tests you can delete one item from the clipboard, test is working!
        """
        
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("emb%")
        searchbox.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_id("termResultList").find_elements_by_link_text("embryo")
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        time.sleep(5)
        print result
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("4-5")
        clipbox.send_keys(Keys.RETURN)
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(items)
        print items
        time.sleep(5)
        self.assertEqual(["TS4; embryo", "TS5; embryo"], searchTreeItems)
        items[1].click()
        self.driver.find_element_by_xpath("//*[@id='clipboard']/li[2]/img").click()
        time.sleep(5)
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        searchTreeItems = self.getSearchTextAsList(items)
        print items
        self.assertEqual(["TS4; embryo"], searchTreeItems)
        
    def testdeletemultclipboard(self):    
        """tests you can delete multiple items from the clipboard, test is working!
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("neck")
        searchbox.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_id("termResultList").find_elements_by_link_text("embryo")
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        time.sleep(5)
        print result
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("23-27")
        clipbox.send_keys(Keys.RETURN)
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(items)
        print items
        time.sleep(5)
        self.assertEqual(["TS23; neck","TS24; neck","TS25; neck","TS26; neck","TS27; neck"], searchTreeItems)
        items[1].click()
        self.driver.find_element_by_xpath("//*[@id='clipboard']/li[2]/img").click()
        items[2].click()
        self.driver.find_element_by_xpath("//*[@id='clipboard']/li[3]/img").click()
        items[3].click()
        self.driver.find_element_by_xpath("//*[@id='clipboard']/li[4]/img").click()
        time.sleep(5)
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        searchTreeItems = self.getSearchTextAsList(items)
        print items
        self.assertEqual(["TS23; neck","TS27; neck"], searchTreeItems)
        

    def testClpboardBasicSort(self):
        """
        tests that a basic sort works by displaying the clip board results in smart alpha order, test works
        """
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("emb%")
        searchbox.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_id("termResultList").find_elements_by_link_text("embryo")
        clear = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardClear")
        clear.click()
        time.sleep(5)
        print result
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("5-7")
        clipbox.send_keys(Keys.RETURN)
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(items)
        print items
        time.sleep(5)
        self.assertEqual(["TS5; embryo","TS6; embryo","TS7; embryo"], searchTreeItems)
        searchbox.clear()
        clipbox.clear()
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("endoderm")
        searchbox.send_keys(Keys.RETURN)
        result = self.driver.find_element_by_id("termResultList").find_elements_by_link_text("embryo")
        time.sleep(5)
        print result
        clipbox = self.driver.find_element_by_id("clipboardInput")
        clipbox.send_keys("6-8")
        clipbox.send_keys(Keys.RETURN)
        time.sleep(5)
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(items)
        print items
        time.sleep(5)
        self.assertEqual(["TS5; embryo","TS6; embryo","TS7; embryo","TS6; endoderm","TS7; endoderm","TS8; endoderm"], searchTreeItems)
        sort = self.driver.find_element_by_id("clipboardFunctions").find_element_by_id("clipboardSort")
        sort.click()
        time.sleep(5)
        clipsort = self.driver.find_element_by_id("emapClipBoardContent").find_element_by_id("clipboard")
        items = clipsort.find_elements_by_css_selector("li")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = self.getSearchTextAsList(items)
        print items
        time.sleep(5)
        self.assertEqual(["TS5; embryo","TS6; embryo","TS6; endoderm","TS7; embryo","TS7; endoderm","TS8; endoderm"], searchTreeItems)
        

    def getSearchTextAsList(self, liItems):
        """
        Take all found li tags in liItems
            and return a list of all the text values
            for each li tag
        """
        searchTextItems = []
        for item in liItems:
            text = item.text
            searchTextItems.append(item.text)
            
        print "li text = %s" % searchTextItems
        return searchTextItems
        
            
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()