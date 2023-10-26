'''
Created on Jan 4, 2016
@Attention: This file does not have tests yet. Need to add them
@author: jeffc
Verify
'''
import unittest
import tracemalloc
import config
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#Tests
tracemalloc.start()
class TestGxd(unittest.TestCase):


    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
    def test_gxd_Name(self):
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'titleBarMainTitleGxd')))  # waits until the page loads
        self.assertIn("Mouse Gene Expression", driver.title, "page not found")

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxd))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
