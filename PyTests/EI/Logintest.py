'''
Created on Feb 4, 2016

@author: jeffc
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def testLoginNoPwd(self):#verifies entering no password gives error
        driver = self.driver
        driver.get(config.PWI_URL)#get the P-WI main page
        self.assertIn("P-WI", driver.page_source)#verifies your on the correct page
        username = driver.find_element_by_name('user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        submit = driver.find_element_by_name("submit") #Find the Login button
        submit.click() #click the login button
        self.assertIn("user or password is invalid", self.driver.page_source)
    
    def testLoginNoUser(self):#verifies entering no user name gives error
        driver = self.driver
        driver.get(config.PWI_URL)#get the P-WI main page
        self.assertIn("P-WI", driver.page_source)#verifies your on the correct page
        passwd = driver.find_element_by_name('password')#finds the password box
        passwd.send_keys("test") #enters a bogus password
        submit = driver.find_element_by_name("submit") #Find the Login button
        submit.click() #click the login button
        self.assertIn("user or password is invalid", self.driver.page_source)    

    def testLoginPass(self):#verifies entering a user name and password logs you in to the system
        driver = self.driver
        driver.get(config.PWI_URL)#get the P-WI main page
        self.assertIn("P-WI", driver.page_source)#verifies your on the correct page
        username = driver.find_element_by_name('user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = driver.find_element_by_name('password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = driver.find_element_by_name("submit") #Find the Login button
        submit.click() #click the login button
        self.assertIn("MGI Production WI Index", self.driver.page_source)    

    def testLogoutPass(self):#verifies entering a user name and password logs you in to the system
        driver = self.driver
        driver.get(config.PWI_URL)#get the P-WI main page
        self.assertIn("P-WI", driver.page_source)#verifies your on the correct page
        username = driver.find_element_by_name('user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = driver.find_element_by_name('password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = driver.find_element_by_name("submit") #Find the Login button
        submit.click() #click the login button
        self.assertIn("MGI Production WI Index", self.driver.page_source) 
        logoutlink = driver.find_element_by_id("headerLogout")#find the logout link
        logoutlink.click() #click the logout link   
        self.assertIn("Login", self.driver.page_source) #verify the login button now exists

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLoginNoUser']
    unittest.main()