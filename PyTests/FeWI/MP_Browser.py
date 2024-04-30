"""
Created on Dec 7, 2017

@author: jeffc
"""

import os.path
import sys
import time
import tracemalloc
import unittest
import config

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate, wait

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../', )
)

# Tests
tracemalloc.start()


class TestMPBrowser(unittest.TestCase):

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
        driver.get(config.TEST_URL + "/vocab/mp_ontology/MP:0005375")
        # identifies the table tags that  contain  parent terms
        parent = driver.find_element(By.ID, 'termPaneDetails').find_elements(By.TAG_NAME, 'td')
        print([x.text for x in parent])

        # verifies that the returned part terms are correct
        self.assertEqual(parent[2].text, "is-a mammalian phenotype")

    def test_default_sort_treeview(self):
        """
        @status: Tests that the terms are correctly sorted
        The default sort for the tree view is smart alpha
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/mp_ontology/MP:0011614")
        wait.forAjax(self.driver, 2)
        termlist = driver.find_elements(By.CLASS_NAME, 'jstree-anchor')
        terms = iterate.getTextAsList(termlist)
        print([x.text for x in termlist])

        # slow aging should not be before the 18th item in the list
        self.assertGreater(terms.index('slow aging'), 18)

    def test_tissue_link_multi(self):
        """
        @status: Tests that searching by an MP ID that is associated with multiple expressions return the correct results/link
        @note: MP-ID-Search-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/mp_ontology/MP:0002633")
        driver.find_element(By.LINK_TEXT, 'tissues').click()
        wait.forAjax(self.driver, 2)
        searchlist = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchlist)
        print([x.text for x in searchlist])

        # These 2 terms should be returned in the anatomy search results
        self.assertIn('aorta TS23-28\npulmonary artery TS17-28', terms, 'these terms are not listed!')

    def test_tissue_link_single(self):
        """
        @status: Tests that searching by an MP ID that is associated with a single expression returns the correct results/link
        @note: MP-ID-Search-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/mp_ontology/MP:0014185")
        driver.find_element(By.LINK_TEXT, 'tissues').click()
        searchlist = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchlist)
        print([x.text for x in searchlist])
        wait.forAjax(self.driver, 2)
        # This 1 term should be returned in the anatomy search results
        self.assertIn('cerebellum TS21-28', terms, 'this term is not listed!')

    def test_tissue_link_nophenotype(self):
        """
        @status: Tests that searching by an MP term that is associated to an expression but has no phenotype annotations
        @note: MP-ID_Search-4
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/mp_ontology/MP:0030355")
        driver.find_element(By.LINK_TEXT, 'tissues').click()
        wait.forAjax(self.driver, 2)
        searchlist = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchlist)
        print([x.text for x in searchlist])

        # This term should be returned in the anatomy search results
        self.assertIn('lambdoid suture TS24-28', terms, 'this term is not listed!')

    def test_tissue_link_results_sort(self):
        """
        @status: Tests that searching by an MP ID that is associated with multiple expressions return the correct results in alphanumeric sort order
        @note: MP-ID-Search-5 *test passed 4-20-2020
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/mp_ontology/MP:0000914")
        driver.find_element(By.LINK_TEXT, 'tissues').click()
        wait.forAjax(self.driver, 2)
        searchlist = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchlist)
        print([x.text for x in searchlist])

        # These 2 terms should be returned in the anatomy search results
        self.assertIn('brain TS17-28\nconnective tissue TS20-28\ncranium TS20-28', terms, 'these terms are not listed!')

    def test_strain_link_from_summary(self):
        """
        @status: Tests that strains listed in the Genetic Background column of an MP query summary goes to it's strain detail page
        @note: MP-summary-1 *tested 4-20-2020
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/mp/annotations/MP:0006209")
        driver.find_element(By.LINK_TEXT, 'C57BL/6J-Enpp1asj/GrsrJ').click()
        # switch focus to the new tab for Strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        print(page_title.text)
        # Asserts that the strain page is for the correct strain
        self.assertEqual(page_title.text, 'C57BL/6J-Enpp1asj/GrsrJ', 'Page title is not correct!')

    def tearDown(self):
        pass
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMPBrowser))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
