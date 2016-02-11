'''
Created on Jan 5, 2016

@author: jeffc
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test_private_allele(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def test_private(self):
        driver = self.driver
        driver.get("http://www.informatics.jax.org")
        self.assertIn("Informatics", driver.title)
        querytext = driver.find_element_by_name('query')
        querytext.send_keys("Brca1") #put your marker symbol
        querytext.send_keys(Keys.RETURN) #click the submit button
        brcalink = driver.find_element_by_link_text("Brca1") #Find the Brca1 link and click it
        brcalink.click() #Find the all alleles and mutations link and click it
        allallelelink = driver.find_element_by_link_text("89")
        allallelelink.click() #assert that there is no link for Brca1<test1>#testallele = driver.find_element_by_link_text('Brca1<sup>test1</sup>')
        noallelelink = driver.find_element_by_partial_link_text("ash")
        #self.assertFalse(noallelelink.is_displayed(), "allele link exists!")
        self.assertTrue(noallelelink.is_displayed())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":

    unittest.main()