'''
Created on Dec 22, 2015
This test suite checks that private alleles and private markers are not displayed on Public.
@author: jeffc
'''
import unittest
import tracemalloc
import time
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
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.select import Select
from util import wait

#Tests
tracemalloc.start()
class TestPrivateData(unittest.TestCase): 
    

    def setUp(self):
        #self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.PUBLIC_URL)
        self.driver.implicitly_wait(4)

    def test_hide_private_allele(self):
        """
        @status: Tests that the dummy private allele Brca1<test1> does not display on public
        """
        print ("BEGIN test_hide_private_allele")
        driver = self.driver
        querytext = driver.find_element(By.NAME,'query')
        querytext.clear()
        querytext.send_keys("Brca1")# put your marker symbol
        querytext.send_keys(Keys.RETURN)  # click the submit button
        brcalink = driver.find_element(By.LINK_TEXT, 'Brca1')# Find the Brca1 link and click it
        brcalink.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'phenoMutationLink')))  # waits until the All Mutations and Alleles link is displayed on the page
        #allallelelink = driver.find_element(By.LINK_TEXT, '93')# Find the all alleles and mutations link and click it
        allallelelink = driver.find_element(By.ID, 'phenoMutationLink')# Find the all alleles and mutations link and click it
        allallelelink.click()
        # assert that there is no link for Brca1<test1>
        bodytext = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertFalse('Brca1<sup>test1</sup>' in bodytext)
        
    def test_hide_private_marker(self):
        """
        @status: Tests that the dummy private allele Brca1<test1> does not display on public
        """
        print ("BEGIN test_hide_private_marker")
        driver = self.driver
        querytext = driver.find_element(By.NAME, 'query')
        querytext.clear()
        querytext.send_keys("Agit")# put your marker symbol
        querytext.send_keys(Keys.RETURN)  # clicks the return/enter button
        wait.forAjax(driver)
        #missng = driver.find_element(By.CLASS_NAME,'redText').is_displayed()
        missng = driver.find_element(By.ID,'fCount')
        #verifies that the Genome Features tab is displaying (0) results
        self.assertTrue(missng, '(0)')
    

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPrivateData))
    return suite
        
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
