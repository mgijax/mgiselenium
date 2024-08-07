"""
Created on Oct 21, 2016
These tests were created to verify details on the Genotype detail pages(genoview) and all Genotype page(allgenoviews)
@author: jeffc
Verify the Genotype heading details except 'find mice' information
Verify the Genetic Background link is correct
Verify the Genetic Background strain is not a link when it has 'involves'
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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)

# Tests
tracemalloc.start()


class TestGenotypeDetail(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/allele/")
        self.driver.implicitly_wait(10)

    def test_genotype_header(self):
        """
        @status this test verifies the Genotype heading details except 'find mice' information.
        @note
        """
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        plnk = self.driver.find_element(By.PARTIAL_LINK_TEXT, '132-14Neu')
        self.driver.execute_script("arguments[0].click();", plnk)
        self.driver.find_element(By.LINK_TEXT, 'hm1').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'genoID'))):
            print('Phenotypes Associated with This Genotype page loaded')
        mgiid = self.driver.find_element(By.CLASS_NAME, 'genoID')
        self.assertEqual(mgiid.text, "MGI:3707321",
                         "This is not the correct MGI ID")  # verifies we have the correct MGI ID
        hmid = self.driver.find_element(By.CLASS_NAME, 'hmGeno')
        self.assertEqual(hmid.text, "hm1",
                         "This is not the correct hm ID")  # verifies we are bringing the hm1 data back
        gt = self.driver.find_element(By.CLASS_NAME, 'genotypeCombo')
        print(gt.text)
        self.assertEqual(gt.text, "Pax6132-14Neu/Pax6132-14Neu",
                         "This is not the correct genotype combo")  # verifies the Allelic Composition is correct

        link = self.driver.find_element(By.LINK_TEXT, 'C3.Cg-Pax6132-14Neu')
        self.assertEqual(link.text, 'C3.Cg-Pax6132-14Neu',
                         'This is not the correct Genetic Background!')  # verifies the Genetic Background is correct

    def test_genotype_gb_link(self):
        """
        @status this test verifies the Genetic Background link is correct.
        @note genodetail-1
        """
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        plnk = self.driver.find_element(By.PARTIAL_LINK_TEXT, '132-14Neu')
        self.driver.execute_script("arguments[0].click();", plnk)
        self.driver.find_element(By.LINK_TEXT, 'hm1').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'genoID'))):
            print('Phenotypes Associated with This Genotype page loaded')
        # click the Genetic Background link
        self.driver.find_element(By.LINK_TEXT, 'C3.Cg-Pax6132-14Neu').click()
        self.driver.switch_to.window(self.driver.window_handles[2])
        ptitle = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        # Assert the page title is for the correct strain name
        self.assertEqual(ptitle.text, "C3.Cg-Pax6132-14Neu")

    def test_genotype_gb_nolink(self):
        """
        @status this test verifies the Genetic Background strain is not a link when it has 'involves'.
        @note genodetail-2
        """
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Pax62Neu').click()
        # self.driver.find_element(By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()
        self.driver.find_element(By.LINK_TEXT, 'hm1').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'genoID'))):
            print('Phenotypes Associated with This Genotype page loaded')
        # click the Genetic Background link
        strain_link = self.driver.find_element(By.CSS_SELECTOR,
                                               '.detail > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)')
        if strain_link.tag_name == 'a':  # validating the element
            print('element is link')
        else:
            print('element is text')

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGenotypeDetail))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
