'''
Created on Jul 20, 2022
These tests check the functionality of the the GXD Profile query form
@author: jeffc
Verify that searching by a single anatomical structure & detected return the correct results
Verify that searching by two anatomical structures & detected return the correct results
Verify that searching by 1 structure & detected and no where else return the correct results
Verify that query for detected in "A", Not detected in "B", where "A" and "B" are in different anatomical systems
'''
import unittest
import time
import tracemalloc
import config
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate, wait

#Tests
tracemalloc.start()
class TestGxdProfileQF(unittest.TestCase):


    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)

    def test_prof_single_results(self):
        """
        @status: Tests that searching by a single anatomical structure & detected return the correct results
        @note: GXD-Profile-1 CRM-82
        @attention: the time sleeps need to be replaced by expected conditions code
        """
        driver = self.driver
        #driver.get(config.TEST_URL + '/gxd/profile')
        driver.get(config.TEST_URL + '/gxd')
        self.driver.find_element(By.CSS_SELECTOR, '#expressionSearch > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1) > em:nth-child(1)').click()
        struct1 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct1.send_keys("molar root")
        time.sleep(2)
        self.driver.find_element(By.ID, 'profileDetected1').is_selected()
        struct1.send_keys(Keys.TAB)
        struct2 = self.driver.find_element(By.ID, 'profileStructure2')
        struct2.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'resultstab').click()
        #locates the structure column and lists the structures found
        structurelist = self.driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = structurelist.find_elements(By.CLASS_NAME, 'yui-dt-col-structure')
        searchTextItems = iterate.getTextAsList(items)        
        print(searchTextItems)
        #assert that this gene is not returned since it is associated to a normal phenotype
        self.assertIn('TS28: molar root', searchTextItems, 'TS28: tongue anterior part is not being returned!')   
        

    def test_prof_double_results(self):
        """
        @status: Tests that searching by two anatomical structures & detected return the correct results
        @note: GXD-Profile-2 CRM-82
        @attention: the time sleeps need to be replaced by expected conditions code
        """
        driver = self.driver
        #driver.get(config.TEST_URL + '/gxd/profile')
        driver.get(config.TEST_URL + '/gxd')
        self.driver.find_element(By.CSS_SELECTOR, '#expressionSearch > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1) > em:nth-child(1)').click()
        struct1 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct1.send_keys("tooth root")
        time.sleep(2)
        self.driver.find_element(By.ID, 'profileDetected1').is_selected()
        struct1.send_keys(Keys.RETURN)
        time.sleep(2)
        struct2 = self.driver.find_element(By.ID, 'profileStructure2')
        # Enter your structure
        struct2.send_keys("molar root")
        time.sleep(2)
        self.driver.find_element(By.ID, 'profileDetected2').click()
        struct2.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'resultstab').click()
        #locates the structure column and lists the structures found
        structurelist = self.driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = structurelist.find_elements(By.CLASS_NAME, 'yui-dt-col-structure')
        searchTextItems = iterate.getTextAsList(items)        
        print(searchTextItems)
        #assert that this gene is not returned since it is associated to a normal phenotype
        self.assertIn('TS28: molar root', searchTextItems, 'TS28: tongue anterior part is not being returned!')   
        

    def test_profile_nowhereelse(self):
        """
        @status: Tests that searching by 1 structure & detected and no where else return the correct results
        @note: GXD-Profile-3 CRM-82
        @attention: the time sleeps need to be replaced by expected conditions code
        """
        driver = self.driver
        #driver.get(config.TEST_URL + '/gxd/profile')
        driver.get(config.TEST_URL + '/gxd')
        self.driver.find_element(By.CSS_SELECTOR, '#expressionSearch > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1) > em:nth-child(1)').click()
        struct1 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct1.send_keys("blood island")
        time.sleep(2)
        self.driver.find_element(By.ID, 'profileDetected1').click()
        struct1.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'profileNowhereElseCheckbox').is_selected()
        self.driver.find_element(By.ID, 'resultstab').click()
        #locates the structure column and lists the structures found
        structurelist = self.driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = structurelist.find_elements(By.CLASS_NAME, 'yui-dt-col-structure')
        searchTextItems = iterate.getTextAsList(items)        
        print(searchTextItems)
        #assert that this gene is not returned since it is associated to a normal phenotype
        self.assertIn('TS13: blood island', searchTextItems, 'TS13: blood island is not being returned!')   


    def test_profile_D_notD_systems(self):
        """
        @status: Tests that query for detected in "A", Not detected in "B", where "A" and "B" are in different anatomical systems
        @note: GXD-Profile-4 CRM-82
        @attention: the time sleeps need to be replaced by expected conditions code!!
        """
        driver = self.driver
        #driver.get(config.TEST_URL + '/gxd/profile')
        driver.get(config.TEST_URL + '/gxd')
        self.driver.find_element(By.CSS_SELECTOR, '#expressionSearch > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1) > em:nth-child(1)').click()
        struct1 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct1.send_keys("tongue anterior part")
        time.sleep(2)
        self.driver.find_element(By.ID, 'profileDetected1').is_selected()
        struct1.send_keys(Keys.RETURN)
        time.sleep(2)
        struct2 = self.driver.find_element(By.ID, 'profileStructure2')
        # Enter your structure
        struct2.send_keys("tongue extrinsic muscle")
        time.sleep(2)
        self.driver.find_element(By.ID, 'profileNotDetected2').click()
        struct2.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'resultstab').click()
        time.sleep(2)
        #locates the structure column and lists the structures found
        structurelist = self.driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = structurelist.find_elements(By.CLASS_NAME, 'yui-dt-col-structure')
        searchTextItems = iterate.getTextAsList(items)        
        print(searchTextItems)
        #assert that this gene is not returned since it is associated to a normal phenotype
        self.assertIn('TS28: tongue anterior part', searchTextItems, 'TS28: tongue anterior part is not being returned!')   
        #assert that this gene is not returned since it has no expression annotations
        self.assertNotIn('TS23: tongue extrinsic muscle', searchTextItems, 'TS23: tongue extrinsic muscle is being returned!') 

        
    """def test_profile_all_no(self):
        
        @status: Tests that searching by 3 not detected structures return the correct results
        @note: GXD-Profile-5 Test no longer valid! 6/28/2023
        
        driver = self.driver
        #driver.get(config.TEST_URL + '/gxd/profile')
        driver.get(config.TEST_URL + '/gxd')
        self.driver.find_element(By.CSS_SELECTOR, '#expressionSearch > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1) > em:nth-child(1)').click()
        #time.sleep(2)
        struct1 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct1.send_keys("???")
        time.sleep(2)
        self.driver.find_element(By.ID, 'profileDetected1').is_selected()
        struct1.send_keys(Keys.RETURN)
        time.sleep(2)
        struct2 = self.driver.find_element(By.ID, 'profileStructure2')
        # Enter your structure
        struct2.send_keys("???")
        time.sleep(2)
        self.driver.find_element(By.ID, 'profileNotDetected2').click()
        struct2.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'resultstab').click()
        time.sleep(2)
        #locates the structure column and lists the structures found
        structurelist = self.driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = structurelist.find_elements(By.CLASS_NAME, 'yui-dt-col-structure')
        searchTextItems = iterate.getTextAsList(items)        
        print(searchTextItems)
        #assert that this gene is not returned since it is associated to a normal phenotype
        self.assertIn('TS28: tongue anterior part', searchTextItems, 'TS28: tongue anterior part is not being returned!')   
        #assert that this gene is not returned since it has no expression annotations
        self.assertNotIn('TS23: tongue extrinsic muscle', searchTextItems, 'TS23: tongue extrinsic muscle is being returned!') 
     """
                
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxdProfileQF))
    return suite
        
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
    