"""
Created on Apr 6, 2018
@author: jeffc
Verify that the parent terms are correctly identified, In this case parent term should be is-a
Verify that the terms are correctly sorted. The default sort for the tree view is smart alpha
Verify that searching by an HP term that has 'of the' in the name correctly returns results
"""

import os.path
import sys
import time
import tracemalloc
import unittest
import config

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../', )
)

# Tests
tracemalloc.start()


class TestHPOBrowser(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)

    def test_parent_data(self):
        """
        @status: Tests that the parent terms are correctly identified
        In this case parent term should be is-a
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/hp_ontology/HP:0000118")
        # identifies the table tags that  contain  parent terms
        parent = driver.find_element(By.ID, 'termPaneDetails').find_elements(By.TAG_NAME, 'td')
        print([x.text for x in parent])

        # verifies that the returned part terms are correct
        self.assertEqual(parent[3].text, "is-a All")

    def test_default_sort_treeview(self):
        """
        @status: Tests that the terms are correctly sorted
        The default sort for the tree view is smart alpha
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/hp_ontology/HP:0000005")
        time.sleep(1)
        termList = driver.find_elements(By.CLASS_NAME, 'jstree-anchor')
        terms = iterate.getTextAsList(termList)
        print([x.text for x in termList])

        # Mode of inheritance should not be before the 10th item in the list
        self.assertGreater(terms.index('Mode of inheritance'), 3)

    def test_term_w_ofthe(self):
        """
        @status: Tests that searching by an HP term that has 'of the' in the name correctly returns results
        @note: 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/hp_ontology/")
        searchbox = driver.find_element(By.ID, 'searchTerm')
        # put your HPO search term in the search box
        searchbox.send_keys("Abnormality of the chin")
        searchbox.send_keys(Keys.RETURN)
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('results loaded')
        searchlist = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchlist)
        print([x.text for x in searchlist])

        # This term should be returned in the HPO search results
        self.assertIn('Abnormality of the chin', terms)

    def tearDown(self):
        pass
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHPOBrowser))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
