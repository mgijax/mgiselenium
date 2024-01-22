'''
Created on Feb 4, 2016
verified working on Scrum 6/6/2023
@author: jeffc
'''
import unittest
import tracemalloc
import config
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#Tests
tracemalloc.start()
class TestLogintest(unittest.TestCase):


    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1800, 1000)

    def testLoginNoPwd(self):#verifies entering no password gives error
        driver = self.driver
        driver.get(config.TEST_PWI_URL)#get the P-WI main page
        self.assertIn("P-WI", driver.page_source)#verifies your on the correct page
        username = driver.find_element(By.NAME, 'user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        submit = driver.find_element(By.NAME, "submit") #Find the Login button
        submit.click() #click the login button
        self.assertIn("user or password is invalid", self.driver.page_source)
    
    def testLoginNoUser(self):#verifies entering no user name gives error
        driver = self.driver
        driver.get(config.TEST_PWI_URL)#get the P-WI main page
        self.assertIn("P-WI", driver.page_source)#verifies your on the correct page
        passwd = driver.find_element(By.NAME, 'password')#finds the password box
        passwd.send_keys("test") #enters a bogus password
        submit = driver.find_element(By.NAME, "submit") #Find the Login button
        submit.click() #click the login button
        self.assertIn("*user or password is invalid", self.driver.page_source)

    def testLoginPass(self):#verifies entering a user name and password logs you in to the system
        driver = self.driver
        driver.get(config.TEST_PWI_URL)#get the P-WI main page
        self.assertIn("P-WI", driver.page_source)#verifies your on the correct page
        username = driver.find_element(By.NAME, 'user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = driver.find_element(By.NAME, 'password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = driver.find_element(By.NAME, "submit") #Find the Login button
        submit.click() #click the login button
        self.assertIn("P-WI", self.driver.page_source)    

    def testLogoutPass(self):#verifies entering a user name and password logs you in to the system
        driver = self.driver
        driver.get(config.TEST_PWI_URL)#get the P-WI main page
        self.assertIn("P-WI", driver.page_source)#verifies your on the correct page
        username = driver.find_element(By.NAME, 'user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = driver.find_element(By.NAME, 'password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = driver.find_element(By.NAME, "submit") #Find the Login button
        submit.click() #click the login button
        self.assertIn("P-WI", self.driver.page_source) 
        logoutlink = driver.find_element(By.ID, "headerLogout")#find the logout link
        logoutlink.click() #click the logout link   
        self.assertIn("Login", self.driver.page_source) #verify the login button now exists

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLogintest))
    return suite

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLoginNoUser']
    unittest.main()
