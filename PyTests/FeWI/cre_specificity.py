"""
Created on Jan 16, 2018
This set of tests verifies items found on the Recombinase specificity page
@author: jeffc
Verify a cre allele displays the correct project collection
Verify a cre allele with no project collection
Verify recombinase image links
"""

import os.path
import sys
import tracemalloc
import unittest

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import config
from util.table import Table

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../..', )
)
# Tests
tracemalloc.start()


class TestCreSpecificity(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/home/recombinase")
        self.driver.implicitly_wait(10)

    def test_project_collection(self):
        """
        @status This test verifies that the correct project collection is listed in the Mutation Origin section.
        """
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('MGI:5014205')
        self.driver.find_element(By.NAME, 'submit').click()
        self.driver.find_element(By.ID, 'aLink').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1.1(cre)Mull').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.NAME, 'centeredTitle'), 'Targeted Allele Detail'))
        origin_table = self.driver.find_element(By.ID, 'mutationOriginTable')
        table = Table(origin_table)
        # gets the data found on the Project collection row of the Mutation origin ribbon
        term1 = table.get_cell(3, 0)
        term2 = table.get_cell(3, 1)

        print(term1.text)
        print(term2.text)
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('Project Collection:', term1.text, 'Term1 is not returning')
        self.assertEqual('Neuroscience Blueprint cre', term2.text, "Term2 is incorrect")

    def test_no_project_collection(self):
        """
        @status this test verifies when a cre allele is not assigned to a project collection that row does not display in the Mutation origin ribbon.
        @note test works 4/5/2022
        """
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('MGI:2181632')
        self.driver.find_element(By.NAME, 'submit').click()
        self.driver.find_element(By.ID, 'aLink').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1(CAG-cre)Mnn').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.NAME, 'centeredTitle'), 'Targeted Allele Detail'))
        assert 'Project Collection:' not in self.driver.page_source

    def test_recomb_image_link(self):
        """
        @status this test verifies when a recombinase activity detail page images display and the links go to the correct websites.
        @note fixed and tested 6/7/2022
        """
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('MGI:4365736')
        self.driver.find_element(By.NAME, 'submit').click()
        self.driver.find_element(By.ID, 'aLink').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1(cre)Zjh').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.NAME, 'centeredTitle'), 'Targeted Allele Detail'))
        # toggles open the Recombinase activity table
        self.driver.find_element(By.ID, 'recomRibbonTeaser').click()
        # finds the cell for adipose tissue pre-weaning and clicks it
        self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(1) > td:nth-child(6)').click()
        # switch to the Counts popup
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # click the link "View All result Details and Images" link
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'View All Result').click()
        # verify the cre image is displayed in the Images section
        self.driver.find_element(By.ID, 'creImg429235').is_displayed()

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCreSpecificity))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
