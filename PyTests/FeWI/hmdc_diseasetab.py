"""
Created on Nov 15, 2016
This test should check the column headers for correct display and order. It currently verifies the returned diseases and their order
and the DO IDs in correct order, tests for the other columns need to be added later.
Updated: July 2017 (jlewis) - updates to make Disease Tab tests more tolerant to changes in annotations.  e.g. removing counts
@author: jeffc
Verify the column headings on the Disease Tab are correct and in the correct order
Verify the correct diseases are returned for this query
Verify the correct diseases are returned for this query. This query uses search option Phenotype or Disease
    Name for a query by an MP term name.
Verify This query uses search option Gene Symbol(s) or ID(s).  Verified disease returned due to a Mouse, Human, and Mouse/Human annotations
Verify the correct DO IDs are returned for this query. This query uses search option Phenotype or Disease ID(s)
        this ID  should bring back the disease "Carney complex"
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
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate, wait
from util.table import Table

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)

# Test
tracemalloc.start()


class TestHmdcDiseaseTab(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)

    def test_diseases_tab_headers(self):
        """
        @status This test verifies the column headings on the Disease Tab are correct and in the correct order.  Updated July 2017 to be
                more tolerant of data changes by removing disease count.
        @see HMDC-disease-17 (column headings on Diseases Tab)
        """
        print("BEGIN test_diseases_tab_headers")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Gata1")  # identifies the input field and enters gata1
        # wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()

        # identify the Disease Tab and click on it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR, "li.uib-tab:nth-child(3) > a:nth-child(1)")
        print(disease_tab.text)
        disease_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.ID, 'diseaseTable'))):
            print('HMDC disease tab data loaded')
        time.sleep(3)
        #capture, print and assert the disease tab headers are correct
        head1 = self.driver.find_element(By.XPATH, "//th[contains(@st-sort,'term')]")
        print(head1.text)
        self.assertEqual(head1.text, "Disease")
        head2 = self.driver.find_element(By.XPATH, "//th[contains(@st-sort,'primaryId')]")
        print(head2.text)
        self.assertEqual(head2.text, "DO ID")
        head3 = self.driver.find_element(By.XPATH, "//th[contains(@st-sort,'omimIds')]")
        print(head3.text)
        self.assertEqual(head3.text, "OMIM ID(s)")
        head4 = self.driver.find_element(By.XPATH, "//th[contains(@st-sort,'diseaseModelCount')]")
        print(head4.text)
        self.assertEqual(head4.text, "Mouse Models")
        head5 = self.driver.find_element(By.XPATH, "//th[contains(@st-sort,'diseaseMouseMarkers')]")
        print(head5.text)
        self.assertEqual(head5.text, "Associated Genes from Mouse Models")
        head6 = self.driver.find_element(By.XPATH, "//th[contains(@st-sort,'diseaseHumanMarkers')]")
        print(head6.text)
        self.assertEqual(head6.text, "Associated Human Genes (Source)")
        head7 = self.driver.find_element(By.XPATH, "//th[contains(@st-sort,'diseaseRefCount')]")
        print(head7.text)
        self.assertEqual(head7.text, "References using\nMouse Models")


    def test_diseases_tab_diseases(self):
        """
        @status This test verifies the correct diseases are returned for this query as-of July 2017. This query uses search option
                Gene Symbol(s) or ID(s).  Verified disease returned due to a Mouse, Human, and Mouse/Human annotations.
        @see HMDC-GQ-1 (gene symbol query); HMDC-disease-9 (return diseases for a gene search)
        """
        print("BEGIN test_diseases_tab_diseases")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Gata1")  # identifies the input field and enters gata1
        self.driver.find_element(By.ID, "searchButton").click()
        # identify the Disease tab and verify the tab's text
        disease_tab = self.driver.find_element(By.CSS_SELECTOR,
                                               "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print(disease_tab.text)
        disease_tab.click()
        time.sleep(4)
        disease_table = Table(self.driver.find_element(By.ID, "diseaseTable"))
        cells = disease_table.get_column_cells("Disease")
        print(iterate.getTextAsList(cells))

        diseasenamesreturned = iterate.getTextAsList(cells)

        # asserts that the following diseases are returned
        self.assertIn('depressive disorder', diseasenamesreturned)  # Human GATA1 annotation
        self.assertIn('myelofibrosis', diseasenamesreturned)  # Mouse Gata1 annotation
        self.assertIn('thrombocytopenia', diseasenamesreturned)  # Human and Mouse GATA1/Gata1 annotations

    def test_diseases_tab_diseases2(self):
        """
        @status this test verifies the correct diseases are returned for this query. This query uses search option Phenotype or Disease Name for a
                query by an MP term name.
        @see HMDC-PQ-1 (single token MP term); HMDC-disease-11 (return diseases due to association to genocluster returned)
        """
        print("BEGIN test_diseases_tab_diseases2")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype Name':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_autocomplete_input_0").send_keys(
            "phototoxicity")  # selects phototoxicity from the autocomplete list
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Genes tab and verify the tab's text
        disease_tab = self.driver.find_element(By.CSS_SELECTOR,
                                               "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print(disease_tab.text)
        disease_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                               '#diseaseTable > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2) > a:nth-child(1)'))):
            print('HMDC disease tab data loaded')
        disease_table = Table(self.driver.find_element(By.ID, "diseaseTable"))
        cells = disease_table.get_column_cells("Disease")
        print(iterate.getTextAsList(cells))

        diseasenamesreturned = iterate.getTextAsList(cells)
        # asserts that the correct genes in the correct order are returned
        self.assertIn('erythropoietic protoporphyria', diseasenamesreturned)
        self.assertIn('xeroderma pigmentosum group G', diseasenamesreturned)

    def test_diseases_tab_doids(self):
        """
        @status this test verifies the correct DO IDs are returned for this query. This query uses search option Phenotype or Disease ID(s)
        this ID  should bring back the disease "Carney complex".  Updated July 2017 to make more tolerant to new annotations.  Count removed and
        modified assertEqual to assertIn.
        @see HMDC-DQ-9 (primary DOID query), HMDC-disease-10 (query by DOID, return diseases by DOID)
        """
        print("BEGIN test_diseases_tab_doids")

        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "DOID:0050471")  # identifies the input field and enters ID for "Carney complex"
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Disease Tab and click on it
        disease_tab = self.driver.find_element(By.CSS_SELECTOR,
                                               "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(3) > a.nav-link.ng-binding")
        print(disease_tab.text)
        disease_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                               '#diseaseTable > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(2) > a:nth-child(1)'))):
            print('HMDC disease tab data loaded')
        disease_table = Table(self.driver.find_element(By.ID, "diseaseTable"))
        cells = disease_table.get_column_cells("DO ID")
        print(iterate.getTextAsList(cells))
        diseaseidsreturned = iterate.getTextAsList(cells)
        self.assertIn('DOID:0050471', diseaseidsreturned)  # verify DOID entered is returned in Disease Tab

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHmdcDiseaseTab))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
