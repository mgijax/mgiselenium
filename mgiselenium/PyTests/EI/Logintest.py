'''
Created on Feb 4, 2016

@author: jeffc
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get()

    def testLoginNoPwd(self):
        driver = self.driver
        driver.get("http://scrumdog.informatics.jax.org/pwi/")
        self.assertIn("P-WI", driver.title)
        username = driver.find_element_by_name('user')
        username.send_keys("jeffc") #put your marker symbol
        #querytext.send_keys(Keys.RETURN) #click the submit button
        submit = driver.find_element(by, "Login") #Find the Login button
        submit.click() #click the login button
        allallelelink = driver.find_element_by_link_text("89")
        allallelelink.click() #assert that there is no link for Brca1<test1>#testallele = driver.find_element_by_link_text('Brca1<sup>test1</sup>')
        noallelelink = driver.find_element_by_partial_link_text("ash")
        #self.assertFalse(noallelelink.is_displayed(), "allele link exists!")
        self.assertTrue(noallelelink.is_displayed())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLoginNoUser']
    unittest.main()