'''
Created on Apr 18, 2016
!!these tests might not be valid anymore since the PWI marker form has been replaced by the PWI marker module!!
verified working on Scrum 6/7/2023
@author: jeffc  remove these tests??????
'''

import unittest
import time
import tracemalloc
import config
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import wait, iterate
from config import TEST_PWI_URL

#Tests
tracemalloc.start()
class TestPwiGxdLitIndexByMrk(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1800, 1000)

    def test_table_headers(self):
        """
        @status: Tests that the summaries table headers are correct
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        #locate the symbol field
        symbolbox = driver.find_element(By.ID, 'markerSymbol')
        # put your marker symbol in the box
        symbolbox.send_keys("gata1")
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mrkDetailButton')))  # waits until the marker detail link is displayed on the page
        #finds the marker detail link and clicks it
        driver.find_element(By.ID, "mrkDetailButton").click()
        #switch focus to the marker detail tab
        #WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, 'Lit Index')))#waits until the Lit Index link is displayed on the page
        time.sleep(5)
        handles = driver.window_handles
        size = len(handles)
        for x in range(size):
            if handles[x] != driver.current_window_handle:
                driver.switch_to.window(handles[x])
                print(driver.title)
        driver.find_element(By.LINK_TEXT, "Lit Index").click()
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, 'Public Gata1 Page')))#waits until the Public Gata1 Page link is displayed on the page
        #Locates the summary table and finds the table headings
        headerlist = driver.find_element(By.ID, 'indexRefsTable')
        items = headerlist.find_elements(By.TAG_NAME, "th")
        searchTextItems = iterate.getTextAsList(items)
        #verifies all the table headings are correct and in order
        self.assertEqual(searchTextItems, ['*','Reference','Priority','Conditional'])
        
    def test_page_sort(self):
        """
        @status: Tests that the default page sort is correct
        sort is by no particular order?
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#accessionForm > input:nth-child(2)')))  # waits until the PWI ACC input field is displayed on the page
        # locate the symbol field
        symbolbox = driver.find_element(By.ID, 'markerSymbol')
        # put your marker symbol in the box
        symbolbox.send_keys("gata1")
        driver.find_element(By.ID, 'searchButton').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mrkDetailButton')))  # waits until the marker detail link is displayed on the page
        #finds the marker detail link and clicks it
        driver.find_element(By.ID, "mrkDetailButton").click()
        #switch focus to the marker detail tab
        time.sleep(2)
        handles = driver.window_handles
        size = len(handles)
        for x in range(size):
            if handles[x] != driver.current_window_handle:
                driver.switch_to.window(handles[x])
                print(driver.title)
        driver.find_element(By.LINK_TEXT, "Lit Index").click()
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, 'Public Gata1 Page')))#waits until the Public Gata1 Page link is displayed on the page
        #finds the coded column and then the first 10 items
        refindextable = driver.find_element(By.ID, "indexRefsTable")
        coded = refindextable.find_elements(By.CSS_SELECTOR, 'td:nth-child(1)')
        code1 = coded[0]
        code2 = coded[1]
        code3 = coded[2]
        code4 = coded[3]
        code5 = coded[4]
        code6 = coded[5]
        code7 = coded[6]
        code8 = coded[7]
        code9 = coded[8]
        code10 = coded[9]
        #asserts the first 10 coded labels are correct and in correct order
        self.assertEqual(code1.text, "*")
        self.assertEqual(code2.text, "")
        self.assertEqual(code3.text, "")
        self.assertEqual(code4.text, "*")
        self.assertEqual(code5.text, "*")
        self.assertEqual(code6.text, "")
        self.assertEqual(code7.text, "")
        self.assertEqual(code8.text, "*")
        self.assertEqual(code9.text, "*")
        self.assertEqual(code10.text, "")
        #finds the priority column and then the first 10 items
        refindextable = driver.find_element(By.ID, "indexRefsTable")
        priority = refindextable.find_elements(By.CSS_SELECTOR, 'td:nth-child(3)')
        pri1 = priority[0]
        pri2 = priority[1]
        pri3 = priority[2]
        pri4 = priority[3]
        pri5 = priority[4]
        pri6 = priority[5]
        pri7 = priority[6]
        pri8 = priority[7]
        pri9 = priority[8]
        pri10 = priority[9]
        #asserts the first 10 priority labels are correct and in correct order
        self.assertEqual(pri1.text, "High")
        self.assertEqual(pri2.text, "Low")
        self.assertEqual(pri3.text, "High")
        self.assertEqual(pri4.text, "High")
        self.assertEqual(pri5.text, "High")
        self.assertEqual(pri6.text, "Medium")
        self.assertEqual(pri7.text, "Medium")
        self.assertEqual(pri8.text, "Medium")
        self.assertEqual(pri9.text, "Medium")
        self.assertEqual(pri10.text, "Medium")
        
        #finds the conditional column and then the first 10 items
        refindextable = driver.find_element(By.ID, "indexRefsTable")
        cond = refindextable.find_elements(By.CSS_SELECTOR, 'td:nth-child(4)')
        con1 = cond[0]
        con2 = cond[1]
        con3 = cond[2]
        con4 = cond[3]
        con5 = cond[4]
        con6 = cond[5]
        con7 = cond[6]
        con8 = cond[7]
        con9 = cond[8]
        con10 = cond[9]
        #asserts the first 10 conditional labels are correct and in correct order
        self.assertEqual(con1.text, "Not Specified")
        self.assertEqual(con2.text, "Not Applicable")
        self.assertEqual(con3.text, "Conditional")
        self.assertEqual(con4.text, "Not Applicable")
        self.assertEqual(con5.text, "Conditional")
        self.assertEqual(con6.text, "Not Specified")
        self.assertEqual(con7.text, "Not Specified")
        self.assertEqual(con8.text, "Not Specified")
        self.assertEqual(con9.text, "Not Applicable")
        self.assertEqual(con10.text, "Not Applicable")
        

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPwiGxdLitIndexByMrk))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))