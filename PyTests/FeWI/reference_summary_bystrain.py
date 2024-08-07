"""
Created on May 18, 2018
@author: jeffc
Verify that all the reference results are correct when you have a strain with both normal references and curator added references
"""

import os.path
import sys
import tracemalloc
import unittest
import config

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate
from util.table import Table

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../..', )
)

# Tests
tracemalloc.start()


class TestReferenceSummaryStrain(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/reference")
        self.driver.implicitly_wait(10)

    def test_ref_summary_both_reftype(self):
        """
        @status: Tests that all the reference results are correct when you have a strain with both normal references and curator added references
        @note: ref-sum-bystrain-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/reference")
        idsearchbox = driver.find_element(By.ID, 'id')
        # Enter your J number in the searchbox
        idsearchbox.send_keys("J:24637")
        idsearchbox.submit()
        # find the link beside the word Strains in the Curated Data column and click it
        self.driver.find_element(By.LINK_TEXT, '2').click()
        # locates the strain summary table, find all the rows of data and print it to the console
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        straindata = strain_table.get_rows()
        print(iterate.getTextAsList(straindata))
        idsreturned = iterate.getTextAsList(straindata)
        # asserts that the 2 rows of data are correct
        self.assertEqual(['Strain/Stock Name Synonyms Attributes IDs References',
                          'BUB/BnJ BUB/BnJ-Pde6brd1\ninbred strain\nMGI:2159907\nJAX:000653\nMPD:24\n120',
                          'SF/CamEiJ San Franciscan\ninbred strain\nwild-derived\nMGI:2159978\nJAX:000280\nMPD:159\n22'],
                         idsreturned)
        # The reason we brought back all the rows of data is because we needed to make sure the reference counts were correct and it did not bring back duplicate J numbers
        # example BUB/BnJ shows 67 references, in the EI it shows 69 between the two reference tables. The 2 extra references are because both EI tables have J:6844 and J:17601,
        # duplicate J numbers are not displayed in the FEWI strain summary for reference page.

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestReferenceSummaryStrain))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
