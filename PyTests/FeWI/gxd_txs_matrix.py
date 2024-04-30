"""
Created on Nov 2, 2017
@author: jeffc
@attention: Beginning  test for Tissue X Stage Matrix. Only the first test is valid, all others are copied tests from images tab!!!!
Verify that the high level anatomy terms are displayed in the correct order
Verify the correct anatomy terms and Theiler stages are returned for a simple gene search
Verify the sort order for specimen type using default sort
Verify that the Gene column sort works correctly
Verify that the assay type column sort works correctly
Verify that the specimen type column sort works correctly
"""

import os.path
import sys
import time
import tracemalloc
import unittest

from config import config
from util import wait, iterate
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../..', )
)

# Tests
tracemalloc.start()


class TestGXDTissueStageMatrix(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)

    def test_structure_names_sort(self):
        """
        @status: Tests that the high level anatomy terms are displayed in the correct order
        @attention:
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        # driver.get(config.PUBLIC_URL + "/gxd")
        stagebox = driver.find_element(By.NAME, 'vocabTerm')
        # put your structure term to search in the box
        stagebox.send_keys("mouse")
        stagebox.send_keys(Keys.RETURN)
        driver.find_element(By.ID, 'submit2').click()
        time.sleep(2)
        # find the Tissue x Stage Matrix tab
        tissuestagetab = driver.find_element(By.ID, 'stagegridtab')
        # click the Tissue x Stage Matrix tab
        tissuestagetab.click()
        if WebDriverWait(self.driver, 8).until(EC.presence_of_element_located((By.ID, 'rowGroupInner'))):
            print('tissue x stage tab data loaded')
        # find the Anatomical systems high level terms
        termslist = driver.find_element(By.ID, 'stagegriddata').find_element(By.ID, 'rowGroupInner')
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        self.assertIn('extraembryonic component', searchtextitems)
        self.assertIn('body fluid or substance', searchtextitems)
        self.assertIn('body region', searchtextitems)
        self.assertIn('cavity or lining', searchtextitems)
        self.assertIn('conceptus', searchtextitems)
        self.assertIn('early embryo', searchtextitems)
        self.assertIn('embryo', searchtextitems)
        self.assertIn('germ layer', searchtextitems)
        self.assertIn('organ', searchtextitems)
        self.assertIn('organ system', searchtextitems)
        self.assertIn('tissue', searchtextitems)
        self.assertIn('umbilical or vitelline vessel', searchtextitems)

    def test_anat_terms_results(self):
        """
        @status: Tests the correct anatomy terms and Theiler stages are returned for a simple gene search
        @attention:
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        # driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("Psmb2")
        genebox.send_keys(Keys.RETURN)
        # find the Tissue x Stage Matrix tab and click it
        ele = driver.find_element(By.ID, 'stagegridtab')
        driver.execute_script("arguments[0].click()", ele)
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'rowGroupInner'))):
            print('tissue x stage tab data loaded')
        # find the Anatomical Terms column
        termslist = driver.find_element(By.ID, "stagegriddata").find_element(By.ID, 'rowGroupInner')
        items = termslist.find_elements(By.TAG_NAME, "text")
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        self.assertIn('mouse', searchtextitems)
        self.assertIn('embryo', searchtextitems)
        self.assertIn('extraembryonic component', searchtextitems)
        self.assertIn('organ system', searchtextitems)
        self.assertIn('musculoskeletal system', searchtextitems)
        # find the Anatomical Terms column
        termslist = driver.find_element(By.ID, "stagegriddata").find_element(By.ID, 'colGroupInner')
        items = termslist.find_elements(By.TAG_NAME, "text")
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        self.assertIn('TS11', searchtextitems)
        self.assertIn('TS23', searchtextitems)

    def test_default_sort_specimentype(self):
        """
        @status: Tests the sort order for specimen type using default sort
        sort order is gene first, assay type secondary
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        # driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("Tmem100")
        genebox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Image tab and click it
        ele = driver.find_element(By.ID, 'imagestab')
        driver.execute_script("arguments[0].click()", ele)
        time.sleep(5)
        typelist = driver.find_element(By.ID, "imagesdata").find_elements(By.CSS_SELECTOR,
                                                                          'td.yui-dt-col-hybridization')
        items = typelist[0].find_elements(By.TAG_NAME, "li")
        searchtextitems = iterate.getTextAsList(items)
        # time.sleep(1)
        self.assertEqual(searchtextitems, ["section", "section from whole mount"])

    def test_gene_column_sort(self):
        """
        @status: Tests that the Gene column sort works correctly
        Gene column:
        * sort order is gene, then assay type
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        # driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("shh")
        genebox.send_keys(Keys.RETURN)
        # find the Image tab
        imagetab = driver.find_element(By.ID, "imagestab")
        time.sleep(1)
        # click the image tab
        imagetab.click()
        wait.forAjax(driver)
        time.sleep(1)

        imagesdata = driver.find_element(By.ID, "imagesdata")
        genelist = imagesdata.find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-gene')
        items = genelist[0].find_elements(By.TAG_NAME, "li")
        searchtextitems = iterate.getTextAsList(items)
        self.assertEqual(searchtextitems, ["Arx", "Olig2", "Shh"])
        geneheader = imagesdata.find_element(By.CSS_SELECTOR, 'th.yui-dt-col-gene')
        # click the gene header column to sort
        geneheader.click()
        # wait.forAjax(driver)
        time.sleep(2)
        genelist = driver.find_element(By.ID, "imagesdata").find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-gene')
        time.sleep(2)
        items = genelist[0].find_elements(By.TAG_NAME, "li")
        searchtextitems = iterate.getTextAsList(items)
        self.assertEqual(searchtextitems, ["Ano1", "Cftr", "Shh"])

    def test_assaytype_column_sort(self):
        """
        @status: Tests that the assay type column sort works correctly
        Assay Type column:
        * Not applicable is not shown
        * sort order should be type (with not specified last), followed by assay type and gene
        * reverse order should still leave not specified last
        * blot assays are last by default
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        # driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("pax6")
        genebox.send_keys(Keys.RETURN)
        # find the Image tab
        imagetab = driver.find_element(By.ID, "imagestab")
        time.sleep(1)
        # click the image tab
        imagetab.click()
        wait.forAjax(driver)
        time.sleep(1)
        assaylist = driver.find_element(By.ID, "imagesdata").find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-assayType')
        items = assaylist[0].find_elements(By.TAG_NAME, "li")
        searchtextitems = iterate.getTextAsList(items)
        self.assertEqual(searchtextitems, ["Immunohistochemistry", "Immunohistochemistry"])
        assayheader = driver.find_element(By.ID, "imagesdata").find_element(By.CSS_SELECTOR, 'th.yui-dt-col-assayType')
        # click the gene header column to sort
        assayheader.click()
        wait.forAjax(driver)
        time.sleep(2)
        assaylist = driver.find_element(By.ID, "imagesdata").find_elements(By.CSS_SELECTOR, 'td.yui-dt-col-assayType')
        items = assaylist[2].find_elements(By.TAG_NAME, "li")
        searchtextitems = iterate.getTextAsList(items)
        self.assertEqual(searchtextitems, ["RT-PCR"])

    def test_specimentype_column_sort(self):
        """
        @status: Tests that the specimen type column sort works correctly
        The order for the specimen type sort is the order in the EI menu:
        *whole mount
        *section
        *section from whole mount
        *optical section
        *not specified
        *blots
        
        Reverse would be specified as:
        *optical section
        *section from whole mount
        *section
        *whole mount
        *not specified
        *blots
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        # driver.get(config.PUBLIC_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # put your marker symbol
        genebox.send_keys("hoxa13")
        genebox.send_keys(Keys.RETURN)
        # find the Image tab
        imagetab = driver.find_element(By.ID, "imagestab")
        time.sleep(3)
        # click the image tab
        imagetab.click()
        wait.forAjax(driver)
        time.sleep(3)
        typelist = driver.find_element(By.ID, "imagesdata").find_elements(By.CSS_SELECTOR,
                                                                          'td.yui-dt-col-hybridization')
        items = typelist[0].find_elements(By.TAG_NAME, "li")
        searchtextitems = iterate.getTextAsList(items)
        self.assertEqual(searchtextitems, ["section", "section"])
        specimenheader = driver.find_element(By.ID, "imagesdata").find_element(By.CSS_SELECTOR,
                                                                               'th.yui-dt-col-hybridization')
        # click the gene header column to sort
        specimenheader.click()
        wait.forAjax(driver)
        time.sleep(2)
        assaylist = driver.find_element(By.ID, "imagesdata").find_elements(By.CSS_SELECTOR,
                                                                           'td.yui-dt-col-hybridization')
        items = assaylist[0].find_elements(By.TAG_NAME, "li")
        searchtextitems = iterate.getTextAsList(items)
        self.assertEqual(searchtextitems, ["whole mount"])

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGXDTissueStageMatrix))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
