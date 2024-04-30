"""
Created on Jan 5, 2016
@author: jeffc
Verify that private alleles are not displaying on allele summary page
Verify that the dummy private allele Brca1<test1> does not display on public if queried by the quick search tool
"""
import os.path
import sys
import tracemalloc
import unittest
import config

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import wait

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../config', )
)

# Tests
tracemalloc.start()


class TestPrivateAllele(unittest.TestCase):
    """
    @status: Tests that the dummy private allele Brca1<test1> does not display on public if queried by the quick search tool
    """

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.PUBLIC_URL)
        self.driver.implicitly_wait(10)

    def test_private(self):
        """
        Teste that private alleles are not displaying on allele summary page
        """
        driver = self.driver
        self.assertIn("Informatics", driver.title)
        querytext = driver.find_element(By.NAME, 'query')
        querytext.clear()
        querytext.send_keys("Brca1")  # put your marker symbol
        querytext.send_keys(Keys.RETURN)  # click the submit button
        brcalink = driver.find_element(By.LINK_TEXT, "Brca1")  # Find the Brca1 link and click it
        brcalink.click()
        # switch to the new tab that opens
        self.driver.switch_to.window(self.driver.window_handles[1])
        # Find the all alleles and mutations link and click it
        allallelelink = driver.find_element(By.ID, "phenoMutationLink")
        allallelelink.click()  # assert that there is no link for Brca1<test1>
        # assert that there is no link for Brca1<test1>
        self.assertNotIn("test1", self.driver.page_source, "Test1 allele is displaying!")

    def test_hide_private_marker(self):
        """
        @status: Tests that the dummy private allele Brca1<test1> does not display on public if queried by the quick search tool
        """
        driver = self.driver
        self.assertIn("Informatics", driver.title)
        querytext = driver.find_element(By.NAME, 'query')
        querytext.clear()
        querytext.send_keys("Brca1<test1>")  # put your marker symbol
        querytext.send_keys(Keys.RETURN)  # click the submit button
        wait.forAjax(self.driver, 2)
        self.assertNotIn(self.driver.page_source, 'Braca1<test1>')

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPrivateAllele))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
