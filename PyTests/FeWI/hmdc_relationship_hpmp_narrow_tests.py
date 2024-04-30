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

    def test_rel_narrow_hp_add_lex_match(self):
        """
        @status these tests verify a relationship that is a additional lexical match
        @see: HMDC-rel-hpmp-1
        """
        print("BEGIN test_rel_narrow_hp_add_lex_match")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0032120")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for rows 1
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
        # Verify the Search Term table columns(rows 1)
        self.assertEqual(sterm1.text, '(HP:0032120)\nAbnormal peripheral nervous system physiology')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0003633)\nabnormal nervous system physiology')
        self.assertEqual(termsyn1.text, 'abnormal brain function | abnormal central nervous system physiology | abnormal peripheral nervous system physiology | central nervous system functional abnormalities | central nervous system: other functional anomalies | peripheral nervous system: functional anomalies')

    def test_rel_narrow_hp_over_man_exact(self):
        """
        @status these tests verify a relationship that is an overridden by manual exact
        @see: HMDC-rel-hpmp-2
        """
        print("BEGIN test_rel_narrow_hp_over_man_exact")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0002094")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for rows 1
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
        # Verify the Search Term table columns(rows 1)
        self.assertEqual(sterm1.text, '(HP:0002094)\nDyspnea')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0001954)\nrespiratory distress')
        self.assertEqual(termsyn1.text, 'dyspnea | dyspnoea | gasping | labored breathing | laboured breathing | shortness of breath')

    def test_rel_narrow_hp_standard_match(self):
        """
        @status these tests verify a relationship that is a standard narrow match
        @see: HMDC-rel-hpmp-3
        """
        print("BEGIN test_rel_narrow_hp_standard_match")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0003189")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table row 1
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
        # Verify the table columns row 1
        self.assertEqual(sterm1.text, '(HP:0003189)\nLong nose')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0000446)\nlong snout')
        self.assertEqual(termsyn1.text, 'increased snout length | long nose')

    def test_rel_narrow_add_man_match(self):
        """
        @status these tests verify a relationship that is additional manual matches
        @see: HMDC-rel-hpmp-4  !!!need to find a new example!!!!
        """
        print("BEGIN test_rel_narrow_add_man_match")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0001760")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns row1
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
        # Verify the table columns row1
        self.assertEqual(sterm1.text, '(HP:0001760)\nAbnormal foot morphology')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0000572)\nabnormal autopod morphology')
        self.assertEqual(termsyn1.text, 'abnormal foot morphology | abnormal hand morphology | abnormal paw/hand/foot morphology | abnormal paw morphology | abnormal paws | hand and/or foot anomaly | paw abnormalities | paw/hand/foot dysplasia')

    def test_rel_narrow_add_man_match2(self):
        """
        @status these tests verify a relationship that is additional manual matches
        @see: HMDC-rel-hpmp-5
        """
        print("BEGIN test_rel_narrow_add_man_match2")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0005922")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns row 1
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
        # Verify the table columns row1
        self.assertEqual(sterm1.text, '(HP:0005922)\nAbnormal hand morphology')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0000572)\nabnormal autopod morphology')
        self.assertEqual(termsyn1.text, 'abnormal foot morphology | abnormal hand morphology | abnormal paw/hand/foot morphology | abnormal paw morphology | abnormal paws | hand and/or foot anomaly | paw abnormalities | paw/hand/foot dysplasia')

    def test_rel_narrow_hp_over_man(self):
        """
        @status these tests verify a relationship that is overridden manual narrow match
        @see: HMDC-rel-hpmp-6
        """
        print("BEGIN test_rel_narrow_hp_over_man")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0000776")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for rows 1
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
        # Verify the Search table columns(rows 1)
        self.assertEqual(sterm1.text, '(HP:0000776)\nCongenital diaphragmatic hernia')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0003924)\ndiaphragmatic hernia')
        self.assertEqual(termsyn1.text, 'congenital diaphragmatic hernia | herniated diaphragm')

    def test_rel_narrow_hp_standard_match2(self):
        """
        @status these tests verify a relationship that a standard narrow search
        @see: HMDC-rel-hpmp-7
        """
        print("BEGIN test_rel_narrow_hp_standard_match2")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0001167")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for rows 1
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
        # Verify the Search table columns(row 1 & 2)
        self.assertEqual(sterm1.text, '(HP:0001167)\nAbnormal finger morphology')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0002110)\nabnormal digit morphology')
        self.assertEqual(termsyn1.text, 'abnormal finger morphology | abnormal toe morphology | digit abnormalities | digit dysplasia | extremities: digit dysmorphology')

    def test_rel_narrow_hp_over_man2(self):
        """
        @status these tests verify a relationship that is overridden manual narrow match
        @see: HMDC-rel-hpmp-8
        """
        print("BEGIN test_rel_narrow_hp_over_man2")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0001780")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for rows 1
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
        self.assertEqual(sterm1.text, '(HP:0001780)\nAbnormal toe morphology')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0002110)\nabnormal digit morphology')
        self.assertEqual(termsyn1.text, 'abnormal finger morphology | abnormal toe morphology | digit abnormalities | digit dysplasia | extremities: digit dysmorphology')

    def test_rel_narrow_over_man_broad(self):
        """
        @status these tests verify a relationship that is overridden by manual broad
        @see: HMDC-rel-hpmp-9
        """
        print("BEGIN test_rel_narrow_over_man_broad")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0033031")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for rows 1 & 2
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
        # Verify the Search table columns(rows 1)
        self.assertEqual(sterm1.text, '(HP:0033031)\nHyperpyrexia')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0011016)\nincreased core body temperature')
        self.assertEqual(termsyn1.text, 'hyperpyrexia')

    def test_rel_narrow_over_man_related(self):
        """
        @status these tests verify a relationship that is overridden by manual related
        @see: HMDC-rel-hpmp-10
        """
        print("BEGIN test_rel_narrow_over_man_related")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0003196")  # identifies the input field and enters an MP ID
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
        # Verify the Search table columns(rows 1)
        self.assertEqual(sterm1.text, '(HP:0003196)\nShort nose')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0000445)\nshort snout')
        self.assertEqual(termsyn1.text, 'decreased snout length | short nasal dorsum | short nasal ridge | short nose | short nose ridge')

    def test_rel_narrow_hp_over_man3(self):
        """
        @status these tests verify a relationship that is overridden by manual narrow
        @see: HMDC-rel-hpmp-11
        """
        print("BEGIN test_rel_narrow_hp_over_man3")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0000003")  # identifies the input field and enters an MP ID
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
        # Iterate the table row2 columns
        termsyn1 = table.get_cell(1, 5)
        print(termsyn1.text)
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm1.text, '(HP:0000003)\nMulticystic kidney dysplasia')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0008528)\npolycystic kidney')
        self.assertEqual(termsyn1.text, 'multicystic kidney dysplasia | multiple renal cysts | polycystic kidney disease | polycystic kidneys')


    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHmdcGenesSearch))
    return suite
