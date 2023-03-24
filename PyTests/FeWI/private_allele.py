'''
Created on Jan 5, 2016

@author: jeffc
'''
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import PUBLIC_URL
from util import wait
import time

class TestPrivateAllele(unittest.TestCase):
    """
    @status: Tests that the dummy private allele Brca1<test1> does not display on public
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get(config.PUBLIC_URL)
        self.driver.implicitly_wait(10)

    def test_private(self):
        driver = self.driver
        self.assertIn("Informatics", driver.title)
        querytext = driver.find_element(By.NAME, 'query')
        querytext.clear()
        querytext.send_keys("Brca1")  # put your marker symbol
        querytext.send_keys(Keys.RETURN)  # click the submit button
        brcalink = driver.find_element(By.LINK_TEXT, "Brca1")# Find the Brca1 link and click it
        brcalink.click()
        #switch to the new tab that opens
        self.driver.switch_to.window(self.driver.window_handles[1])
        # Find the all alleles and mutations link and click it
        allallelelink = driver.find_element(By.ID, "phenoMutationLink")
        time.sleep(2)
        allallelelink.click()  # assert that there is no link for Brca1<test1>
        time.sleep(.5)
        # assert that there is no link for Brca1<test1>
        self.assertNotIn("test1", self.driver.page_source,"Test1 allele is displaying!")
        
    def test_hide_private_marker(self):
        """
        @status: Tests that the dummy private allele Brca1<test1> does not display on public
        @bug: this test no longer works !!!!!
        """
        driver = self.driver
        self.assertIn("Informatics", driver.title)
        querytext = driver.find_element(By.NAME, 'query')
        querytext.clear()
        querytext.send_keys("Brca1<test1>")# put your marker symbol
        querytext.send_keys(Keys.RETURN)  # click the submit button
        wait.forAjax(driver)
        missng = driver.find_element(By.CLASS_NAME, 'redText').is_displayed()#verifies that the warning Could not find the independent term(s): is displaying
        self.assertTrue(missng, 'oops, is not displaying warning message!')
    
    def tearDown(self):
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPrivateAllele))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
