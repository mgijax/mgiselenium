"""
Created on Dec 11, 2023

This file contains the tests for Hmdc relationships for MP to HP Related searches that are entered via the Hmdc search form.
Tests are organized based off of a google spreadsheet found here: https://docs.google.com/spreadsheets/d/1QDnGDC3QNv_XUyBKN4rpNqzSnNOG-D0WVNixESeej9A/edit?pli=1#gid=0
@author: jeffc
Verify
Verify
Verify
Verify
Verify
Verify
Verify
Verify
Verify
Verify
Verify
Verify
Verify
Verify
Verify
Verify
Verify
Verify
Verify
Verify
"""
import os.path
import sys
import tracemalloc
import unittest
import config

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import wait
from util.table import Table
# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)

# Tests
tracemalloc.start()


class TestHmdcGenesSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)

    def test_rel_manual_2lex(self):
        """
        @status these tests verify a relationship that one manual and 2 lexical (broad and exact)
        @see: HMDC-broad-mphp-1
        """
        print("BEGIN test_rel_manual_2lex")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0030270")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for row 1
        sterm = table.get_cell(1,0)
        print(sterm.text)
        mmethod = table.get_cell(1, 2)
        print(mmethod.text)
        mtype = table.get_cell(1, 3)
        print(mtype.text)
        mterm = table.get_cell(1, 4)
        print(mterm.text)
        termsyn = table.get_cell(1, 5)
        print(termsyn.text)
        # Verify the Search table columns row 1
        self.assertEqual(sterm.text, '(MP:0030270)\nretrogenia')
        self.assertEqual(mmethod.text, 'lexical')
        self.assertEqual(mtype.text, 'broad')
        self.assertEqual(mterm.text, '(HP:0000278)\nRetrognathia')
        self.assertEqual(termsyn.text, 'Lower jaw retrognathia | Receding chin | Receding lower jaw | Receding mandible | Retrogenia | Retrognathia of lower jaw | Weak chin | Weak jaw')

    def test_rel_broad_standard_match1(self):
        """
        @status these tests verify a relationship that has a basic result(broad)(standard result)(1)
        @see: HMDC-broad-mphp-2
        """
        print("BEGIN test_rel_broad_standard_match1")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0010421")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for row 1
        sterm1 = table.get_cell(1,0)
        print(sterm1.text)
        mmethod1 = table.get_cell(1, 2)
        print(mmethod1.text)
        mtype1 = table.get_cell(1, 3)
        print(mtype1.text)
        mterm1 = table.get_cell(1, 4)
        print(mterm1.text)
        termsyn1 = table.get_cell(1, 5)
        print(termsyn1.text)
        # Verify the Search table columns row 1
        self.assertEqual(sterm1.text, '(MP:0010421)\nventricular aneurysm')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(HP:0006698)\nDilatation of the ventricular cavity')
        self.assertEqual(termsyn1.text, 'Ventricular aneurysm')

    def test_rel_lex_broad_basic2(self):
        """
        @status these tests verify a relationship that has a basic result(broad)(standard result)(2)
        @see: HMDC-nar-mphp-3
        """
        print("BEGIN test_rel_lex_broad_basic2")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0010450")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for row 1
        sterm1 = table.get_cell(1,0)
        print(sterm1.text)
        mmethod1 = table.get_cell(1, 2)
        print(mmethod1.text)
        mtype1 = table.get_cell(1, 3)
        print(mtype1.text)
        mterm1 = table.get_cell(1, 4)
        print(mterm1.text)
        termsyn1 = table.get_cell(1, 5)
        print(termsyn1.text)
        # Verify the Search Term table columns(row 1)
        self.assertEqual(sterm1.text, '(MP:0010450)\natrial septal aneurysm')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(HP:0011995)\nAtrial septal dilatation')
        self.assertEqual(termsyn1.text, 'Atrial septal aneurysm')


    def test_rel_lex_broad_basic3(self):
        """
        @status these tests verify a relationship that has a basic result(broad)(standard result)(3)
        @see: HMDC-nar-mphp-4
        """
        print("BEGIN test_rel_lex_broad_basic3")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0003279")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for row 1
        sterm1 = table.get_cell(1,0)
        print(sterm1.text)
        mmethod1 = table.get_cell(1, 2)
        print(mmethod1.text)
        mtype1 = table.get_cell(1, 3)
        print(mtype1.text)
        mterm1 = table.get_cell(1, 4)
        print(mterm1.text)
        termsyn1 = table.get_cell(1, 5)
        print(termsyn1.text)
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm1.text, '(MP:0003279)\naneurysm')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(HP:0002617)\nVascular dilatation')
        self.assertEqual(termsyn1.text, 'Aneurysm | Aneurysmal dilatation | Aneurysmal disease | Aneurysms | Wider than typical opening or gap')



    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHmdcGenesSearch))
    return suite
