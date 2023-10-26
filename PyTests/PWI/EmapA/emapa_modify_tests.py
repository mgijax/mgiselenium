'''
Created on Jan 28, 2016
@attention: Needs tests added as time permits!!!!!!
@attention: Needs tests added as time permits!!!!!!
@attention: Needs tests added as time permits!!!!!!
@author: jeffc
'''
import unittest
import tracemalloc
import time
import config
import sys, os.path
# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..')
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

#Tests
tracemalloc.start()
class TestEiEmapaModify(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/emapaBrowser")
        # logging in for all tests
        username = self.driver.find_element(By.NAME, 'user')  # finds the user login box
        username.send_keys(config.PWI_LOGIN)  # enters the username
        passwd = self.driver.find_element(By.NAME, 'password')  # finds the password box
        passwd.send_keys(config.PWI_PASSWORD)  # enters a valid password
        submit = self.driver.find_element(By.NAME, "submit")  # Find the Login button
        submit.click()  # click the login button

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiEmapaModify))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))