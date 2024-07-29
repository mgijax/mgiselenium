"""
Created on Dec 15, 2023

This file contains the tests for Hmdc relationships for MP to HP Related searches looking at synonym to synonym.
Tests are organized based off of a google spreadsheet found here: https://docs.google.com/spreadsheets/d/1QiOx12b_9sXVOZslGlTAdex6oETLWRHn_jQhElotkX4/edit#gid=0
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


class TestHmdcSynToSynSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)

    def test_rel_syn_to_syn1(self):
        """
        @status these tests verify a relationship that has a synonym match for Abdominal distention
        @see: HMDC-syn_to_syn-1
        """
        print("BEGIN test_rel_syn_to_syn1")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0003270")  # identifies the input field and enters an MP ID
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
        # Iterate the table columns for row 2
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype2.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        termsyn2 = table.get_cell(2, 5)
        print(termsyn2.text)
        # Verify the Search table columns row 1
        self.assertEqual(sterm.text, '(HP:0003270)\nAbdominal distention')
        self.assertEqual(mmethod.text, 'manual')
        self.assertEqual(mtype.text, 'exact')
        self.assertEqual(mterm.text, '(MP:0001270)\ndistended abdomen')
        self.assertEqual(termsyn.text, 'bulging abdomen | protruding abdomen')
        # Verify the Search table columns row 2
        self.assertEqual(sterm2.text, '(HP:0003270)\nAbdominal distention')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'exact')
        self.assertEqual(mterm2.text, '(MP:0009247)\nmeteorism')
        self.assertEqual(termsyn2.text, 'bloating | gastrointestinal bloating | tympania | tympanism | tympanites')

    def test_rel_syn_to_syn2(self):
        """
        @status these tests verify a relationship that has a synonym  match for Abnormal situs inversus
        @see: HMDC-syn_to_syn-2
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
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0003363")  # identifies the input field and enters an MP ID
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
        # Iterate the table columns for row 2
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype2.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        termsyn2 = table.get_cell(2, 5)
        print(termsyn2.text)
        # Verify the Search Term table columns(row 1)
        self.assertEqual(sterm1.text, '(HP:0003363)\nAbdominal situs inversus')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0002766)\nsitus inversus')
        self.assertEqual(termsyn1.text, 'situs inversus viscerum | visceral inversion')
        # Verify the Search Term table columns(row 2)
        self.assertEqual(sterm2.text, '(HP:0003363)\nAbdominal situs inversus')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'exact')
        self.assertEqual(mterm2.text, '(MP:0011249)\nabdominal situs inversus')
        self.assertEqual(termsyn2.text, '')

    def test_rel_syn_to_syn3(self):
        """
        @status these tests verify a relationship that has a synonym match for Abnormal emotion
        @see: HMDC-syn-syn-3
        """
        print("BEGIN test_rel_syn_to_syn3")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0100851")  # identifies the input field and enters an MP ID
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
        # Iterate the table columns for row 2
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype2.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        termsyn2 = table.get_cell(2, 5)
        print(termsyn2.text)
        # Verify the Search Term table columns(row 1)
        self.assertEqual(sterm1.text, '(HP:0100851)\nAbnormal emotion')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0003461)\nabnormal response to novel object')
        self.assertEqual(termsyn1.text, '')
        # Verify the Search Term table columns(row 2)
        self.assertEqual(sterm2.text, '(HP:0100851)\nAbnormal emotion')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'exact')
        self.assertEqual(mterm2.text, '(MP:0002572)\nabnormal emotion/affect behavior')
        self.assertEqual(termsyn2.text, 'abnormal emotion/affect behaviour | neurological/behavioral: emotion/affect abnormalities | neurological/behavioural: emotion/affect abnormalities')

    def test_rel_syn_to_syn4(self):
        """
        @status these tests verify a relationship that has a synonym match to Abnormal cardiomyocyte morphology
        @see: HMDC-syn-to-syn-4
        """
        print("BEGIN test_rel_syn_to_syn4")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0031331")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0031331)\nAbnormal cardiomyocyte morphology')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0000278)\nabnormal myocardial fiber morphology')
        self.assertEqual(termsyn1.text, 'abnormal adult cardiomyocyte morphology | abnormal cardiac muscle cell morphology | abnormal myocardial cell morphology | abnormal myocardial fibers | abnormal myocardial fibre morphology | abnormal myocardial fibres | myocardial fiber dysplasia | myocardial fibers abnormalities | myocardial fibre dysplasia | myocardial fibres abnormalities')

    def test_rel_syn_to_syn5(self):
        """
        @status these tests verify a relationship that has a synonym match to Abnormal of the forehead
        @see: HMDC-syn-to-syn-5
        """
        print("BEGIN test_rel_syn_to_syn5")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0000290")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0000290)\nAbnormality of the forehead')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0030031)\nabnormal forehead morphology')
        self.assertEqual(termsyn1.text, 'abnormality of the frontal region of the face | deformity of the forehead | forehead anomaly | malformation of the forehead')
    def test_rel_syn_to_syn6(self):
        """
        @status these tests verify a relationship that has a synonym match to Abnormal cerebral morphology
        @see: HMDC-syn-to-syn-6
        """
        print("BEGIN test_rel_syn_to_syn6")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0002060")  # identifies the input field and enters an MP ID
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
        # Iterate the table columns for row 2
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype2.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        termsyn2 = table.get_cell(2, 5)
        print(termsyn2.text)
        # Iterate the table columns for row 3
        sterm3 = table.get_cell(3, 0)
        print(sterm3.text)
        mmethod3 = table.get_cell(3, 2)
        print(mmethod3.text)
        mtype3 = table.get_cell(3, 3)
        print(mtype3.text)
        mterm3 = table.get_cell(3, 4)
        print(mterm3.text)
        termsyn3 = table.get_cell(3, 5)
        print(termsyn3.text)
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm1.text, '(HP:0002060)\nAbnormal cerebral morphology')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0000787)\nabnormal telencephalon morphology')
        self.assertEqual(termsyn1.text, 'telencephalon dysplasia')
        # Verify the Search table columns(row 2)
        self.assertEqual(sterm2.text, '(HP:0002060)\nAbnormal cerebral morphology')
        self.assertEqual(mmethod2.text, 'manual')
        self.assertEqual(mtype2.text, 'broad')
        self.assertEqual(mterm2.text, '(MP:0000794)\nabnormal parietal lobe morphology')
        self.assertEqual(termsyn2.text, 'parietal lobe dysplasia')
        # Verify the Search table columns(row 3)
        self.assertEqual(sterm3.text, '(HP:0002060)\nAbnormal cerebral morphology')
        self.assertEqual(mmethod3.text, 'lexical')
        self.assertEqual(mtype3.text, 'narrow')
        self.assertEqual(mterm3.text, '(MP:0021002)\nbrain lesion')
        self.assertEqual(termsyn3.text, 'cerebral lesion')

    def test_rel_syn_to_syn7(self):
        """
        @status these tests verify a relationship that has a synonym match to Abnormality of the calcaneus
        @see: HMDC-syn-to-syn-7
        """
        print("BEGIN test_rel_syn_to_syn7")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0008364")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0008364)\nAbnormality of the calcaneus')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0009728)\nabnormal calcaneum morphology')
        self.assertEqual(termsyn1.text, 'abnormal calcaneal bone morphology | abnormal calcaneus morphology | abnormal fibulare morphology | abnormal fibular tarsal bone | abnormal heel bone | abnormal hock bone | abnormal os calcis')

    def test_rel_syn_to_syn8(self):
        """
        @status these tests verify a relationship that has a synonym match to Aplasia of the fingers
        @see: HMDC-syn-to-syn-8
        """
        print("BEGIN test_rel_syn_to_syn8")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0009380")  # identifies the input field and enters an MP ID
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
        # Iterate the table columns for row 2
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype2.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        termsyn2 = table.get_cell(2, 5)
        print(termsyn2.text)
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm1.text, '(HP:0009380)\nFinger aplasia')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0000565)\noligodactyly')
        self.assertEqual(termsyn1.text, 'hypodactyly')
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm2.text, '(HP:0009380)\nFinger aplasia')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'narrow')
        self.assertEqual(mterm2.text, '(MP:0000561)\nadactyly')
        self.assertEqual(termsyn2.text, 'absence of digits | absent fingers | absent toes')

    def test_rel_syn_to_syn9(self):
        """
        @status these tests verify a relationship that has a synonym match for Abnormality of the liver
        @see: HMDC-syn_to_syn-9
        """
        print("BEGIN test_rel_syn_to_syn9")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0001392")  # identifies the input field and enters an MP ID
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
        # Iterate the table columns for row 2
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype2.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        termsyn2 = table.get_cell(2, 5)
        print(termsyn2.text)
        # Verify the Search table columns row 1
        self.assertEqual(sterm.text, '(HP:0001392)\nAbnormality of the liver')
        self.assertEqual(mmethod.text, 'logical')
        self.assertEqual(mtype.text, 'close')
        self.assertEqual(mterm.text, '(MP:0004847)\nabnormal liver weight')
        self.assertEqual(termsyn.text, 'abnormal hepatic weight')
        # Verify the Search table columns row 2
        self.assertEqual(sterm2.text, '(HP:0001392)\nAbnormality of the liver')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'broad')
        self.assertEqual(mterm2.text, '(MP:0000598)\nabnormal liver morphology')
        self.assertEqual(termsyn2.text, 'abnormal hepatic morphology | abnormal liver | liver dysplasia')

    def test_rel_syn_to_syn10(self):
        """
        @status these tests verify a relationship that has a synonym  match for abnormal circulating albumin concentration
        @see: HMDC-syn_to_syn-10
        """
        print("BEGIN test_rel_broad_standard_match10")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0012116")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0012116)\nAbnormal circulating albumin concentration')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0000199)\nabnormal circulating serum albumin level')
        self.assertEqual(termsyn1.text, 'abnormal albumin level')

    def test_rel_syn_to_syn11(self):
        """
        @status these tests verify a relationship that has a synonym match for Aplasia of the vestibule
        @see: HMDC-syn-syn-11
        """
        print("BEGIN test_rel_syn_to_syn11")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0011377")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0011377)\nAplasia of the vestibule')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0004314)\nabsent inner ear vestibule')
        self.assertEqual(termsyn1.text, 'absent vestibule')

    def test_rel_syn_to_syn12(self):
        """
        @status these tests verify a relationship that has a synonym match to abnormal albumin level
        @see: HMDC-syn-to-syn-12 BROKEN (maybe not valid now both HP/MP is exact)
        """
        print("BEGIN test_rel_syn_to_syn12")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0012116")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0012116)\nAbnormal circulating albumin concentration')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0000199)\nabnormal circulating serum albumin level')
        self.assertEqual(termsyn1.text, 'abnormal albumin level')

    def test_rel_syn_to_syn13(self):
        """
        @status these tests verify a relationship that has a synonym match to Sparse hair
        @see: HMDC-syn-to-syn-13
        """
        print("BEGIN test_rel_syn_to_syn13")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0008070")  # identifies the input field and enters an MP ID
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
        # Iterate the table columns for row 2
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype2.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        termsyn2 = table.get_cell(2, 5)
        print(termsyn2.text)
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm1.text, '(HP:0008070)\nSparse hair')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0000416)\nsparse hair')
        self.assertEqual(termsyn1.text, 'hypotrichosis | partial hair loss | sparse fur | thin coat | thin hair')
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm2.text, '(HP:0008070)\nSparse hair')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'related')
        self.assertEqual(mterm2.text, '(MP:0003815)\nhairless')
        self.assertEqual(termsyn2.text,'absent hair | bald | hypotrichosis | naked | nude')

    def test_rel_syn_to_syn14(self):
        """
        @status these tests verify a relationship that has a synonym match to Recurrent infections
        @see: HMDC-syn-to-syn-14
        """
        print("BEGIN test_rel_syn_to_syn14")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0002719")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0002719)\nRecurrent infections')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0002406)\nincreased susceptibility to infection')
        self.assertEqual(termsyn1.text, 'decreased resistance to infection | susceptibility to infection')

    def test_rel_syn_to_syn15(self):
        """
        @status these tests verify a relationship that has a synonym match to Stillbirth
        @see: HMDC-syn-to-syn-15
        """
        print("BEGIN test_rel_syn_to_syn15")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0003826")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0003826)\nStillbirth')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0002081)\nperinatal lethality')
        self.assertEqual(termsyn1.text, 'perinatal death | stillborn | survival: perinatal lethality')

    def test_rel_syn_to_syn16(self):
        """
        @status these tests verify a relationship that has a synonym match to Subcutaneous calcification
        @see: HMDC-syn-to-syn-16
        """
        print("BEGIN test_rel_syn_to_syn16")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0007618")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0007618)\nSubcutaneous calcification')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0003196)\ncalcified skin')
        self.assertEqual(termsyn1.text, 'skin calcification')

    def test_rel_syn_to_syn17(self):
        """
        @status these tests verify a relationship that has a synonym match to Abnormal circulating free fatty acid concentration
        @see: HMDC-syn-to-syn-17
        """
        print("BEGIN test_rel_syn_to_syn17")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0040300")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0040300)\nAbnormal circulating free fatty acid concentration')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0001553)\nabnormal circulating free fatty acids level')
        self.assertEqual(termsyn1.text, 'abnormal circulating free fatty acid level | abnormal circulating non-esterified fatty acids level | abnormal FFA level | abnormal NEFA level | abnormal UFA level | abnormal unesterified fatty acids level')

    def test_rel_syn_to_syn18(self):
        """
        @status these tests verify a relationship that has a synonym match to Aortic valve stenosis
        @see: HMDC-syn-to-syn-18
        """
        print("BEGIN test_rel_syn_to_syn18")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0001650")  # identifies the input field and enters an MP ID
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
        # Iterate the table columns for row 2
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype2.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        termsyn2 = table.get_cell(2, 5)
        print(termsyn2.text)
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm1.text, '(HP:0001650)\nAortic valve stenosis')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0006117)\naortic valve stenosis')
        self.assertEqual(termsyn1.text, 'aortic semi-lunar valve stenosis | aortic semilunar valve stenosis | aortic stenosis | aortic valvar stenosis | left arterial valve stenosis | left semi-lunar valve stenosis | left semilunar valve stenosis | left ventriculoarterial junction stenosis')
        # Verify the Search table columns(row 2)
        self.assertEqual(sterm2.text, '(HP:0001650)\nAortic valve stenosis')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'related')
        self.assertEqual(mterm2.text, '(MP:0010463)\naorta stenosis')
        self.assertEqual(termsyn2.text, 'aortic stenosis')

    def test_rel_syn_to_syn19(self):
        """
        @status these tests verify a relationship that has a synonym match to Broad skull
        @see: HMDC-syn-to-syn-19
        """
        print("BEGIN test_rel_syn_to_syn19")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0002682")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0002682)\nBroad skull')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0000441)\nincreased cranium width')
        self.assertEqual(termsyn1.text, 'increased skull width | wide skull')

    def test_rel_syn_to_syn20(self):
        """
        @status these tests verify a relationship that has a synonym match to fine hair
        @see: HMDC-syn-to-syn-20 BROKEN (maybe no longer valid as both HP/MP now exact)
        """
        print("BEGIN test_rel_syn_to_syn20")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0002213")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0002213)\nFine hair')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0009930)\nfuzzy hair')
        self.assertEqual(termsyn1.text, 'fine hair')

    def test_rel_syn_to_syn21(self):
        """
        @status these tests verify a relationship that has a synonym match to Loss of consciousness
        @see: HMDC-syn-to-syn-21
        """
        print("BEGIN test_rel_syn_to_syn21")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0007185")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0007185)\nLoss of consciousness')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0031302)\nsyncope')
        self.assertEqual(termsyn1.text, 'fainting | fainting spell')

    def test_rel_syn_to_syn22(self):
        """
        @status these tests verify a relationship that has a synonym match to Pulmonic stenosis
        @see: HMDC-syn-to-syn-22
        """
        print("BEGIN test_rel_syn_to_syn22")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0001642")  # identifies the input field and enters an MP ID
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
        # Iterate the table columns for row 2
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype1.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        termsyn2 = table.get_cell(2, 5)
        print(termsyn2.text)
        # Iterate the table columns for row 3
        sterm3 = table.get_cell(3, 0)
        print(sterm3.text)
        mmethod3 = table.get_cell(3, 2)
        print(mmethod3.text)
        mtype3 = table.get_cell(3, 3)
        print(mtype3.text)
        mterm3 = table.get_cell(3, 4)
        print(mterm3.text)
        termsyn3 = table.get_cell(3, 5)
        print(termsyn3.text)
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm1.text, '(HP:0001642)\nPulmonic stenosis')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0010449)\nheart right ventricle outflow tract stenosis')
        self.assertEqual(termsyn1.text, 'arterial cone stenosis | conus arteriosus stenosis | heart right ventricle outflow tract obstruction | infundibular pulmonary stenosis | infundibular pulmonic stenosis | infundibulum of right ventricle stenosis | infundibulum of the heart stenosis | pulmonary cone stenosis | pulmonary conus stenosis | right ventricle infundibulum stenosis | right ventricle pulmonary outflow tract stenosis | RVOTO | subpulmonary stenosis | subpulmonic stenosis')
        # Verify the Search table columns(row 2)
        self.assertEqual(sterm2.text, '(HP:0001642)\nPulmonic stenosis')
        self.assertEqual(mmethod2.text, 'manual')
        self.assertEqual(mtype2.text, 'broad')
        self.assertEqual(mterm2.text, '(MP:0006128)\npulmonary valve stenosis')
        self.assertEqual(termsyn2.text, 'pulmonary stenosis | pulmonary stenosis, valvar | pulmonary valvar stenosis | pulmonic valve stenosis | right arterial valve stenosis | right semi-lunar valve stenosis | right semilunar valve stenosis')
        # Verify the Search table columns(row 3)
        self.assertEqual(sterm3.text, '(HP:0001642)\nPulmonic stenosis')
        self.assertEqual(mmethod3.text, 'lexical')
        self.assertEqual(mtype3.text, 'related')
        self.assertEqual(mterm3.text, '(MP:0010457)\npulmonary artery stenosis')
        self.assertEqual(termsyn3.text, 'pulmonary arterial stenosis | pulmonary stenosis')

    def test_rel_syn_to_syn23(self):
        """
        @status these tests verify a relationship that has a synonym match to Transposition of the great arteries
        @see: HMDC-syn-to-syn-23
        """
        print("BEGIN test_rel_syn_to_syn23")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0001669")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0001669)\nTransposition of the great arteries')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0004110)\ntransposition of great arteries')
        self.assertEqual(termsyn1.text, 'discordant VA connections | TGA | transposition of great vessels')

    def test_rel_syn_to_syn24(self):
        """
        @status these tests verify a relationship that has a synonym match to Glomerular sclerosis
        @see: HMDC-syn-to-syn-24
        """
        print("BEGIN test_rel_syn_to_syn24")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0000096")  # identifies the input field and enters an MP ID
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
        # Iterate the table columns for row 2
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype2.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        termsyn2 = table.get_cell(2, 5)
        print(termsyn2.text)
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm1.text, '(HP:0000096)\nGlomerular sclerosis')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0005264)\nglomerulosclerosis')
        self.assertEqual(termsyn1.text, 'glomerular sclerosis')
        # Verify the Search table columns(row 2)
        self.assertEqual(sterm2.text, '(HP:0000096)\nGlomerular sclerosis')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'narrow')
        self.assertEqual(mterm2.text, '(MP:0011377)\nrenal glomerulus fibrosis')
        self.assertEqual(termsyn2.text, 'fibrotic glomerular capillaries | fibrotic glomeruli | kidney glomerular fibrosis | kidney glomerulus fibrosis | renal glomerular fibrosis')

    def test_rel_syn_to_syn25(self):
        """
        @status these tests verify a relationship that has a synonym match to Neoplasm of the pancreas
        @see: HMDC-syn-to-syn-25
        """
        print("BEGIN test_rel_syn_to_syn25")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0002894")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0002894)\nNeoplasm of the pancreas')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0009153)\nincreased pancreas tumor incidence')
        self.assertEqual(termsyn1.text, 'increased pancreas tumour incidence | pancreas cancer | pancreas neoplasms | pancreatic cancer | pancreatic neoplasms | pancreatic tumor | pancreatic tumour')

    def test_rel_syn_to_syn26(self):
        """
        @status these tests verify a relationship that has a synonym match to Atrophy of alveolar ridges
        @see: HMDC-syn-to-syn-26
        """
        print("BEGIN test_rel_syn_to_syn26")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0006308")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0006308)\nAtrophy of alveolar ridges')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0030466)\nalveolar process atrophy')
        self.assertEqual(termsyn1.text, 'alveolar bone atrophy | alveolar bone loss | alveolar bone resorption | alveolar ridge atrophy')

    def test_rel_syn_to_syn27(self):
        """
        @status these tests verify a relationship that has a synonym match to Agenesis of incisor
        @see: HMDC-syn-to-syn-27
        """
        print("BEGIN test_rel_syn_to_syn27")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0006485")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0006485)\nAgenesis of incisor')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0000125)\nabsent incisors')
        self.assertEqual(termsyn1.text, 'absence of incisors')

    def test_rel_syn_to_syn28(self):
        """
        @status these tests verify a relationship that has a synonym match to Enamel hypoplasia
        @see: HMDC-syn-to-syn-28
        """
        print("BEGIN test_rel_syn_to_syn28")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0006297")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0006297)\nEnamel hypoplasia')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0002576)\nabnormal enamel morphology')
        self.assertEqual(termsyn1.text, 'enamel dysplasia')

    def test_rel_syn_to_syn29(self):
        """
        @status these tests verify a relationship that has a synonym match to Hypertension
        @see: HMDC-syn-to-syn-29
        """
        print("BEGIN test_rel_syn_to_syn29")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0000822")  # identifies the input field and enters an MP ID
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
        # Iterate the table columns for row 2
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype2.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        termsyn2 = table.get_cell(2, 5)
        print(termsyn2.text)
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm1.text, '(HP:0000822)\nHypertension')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0000231)\nhypertension')
        self.assertEqual(termsyn1.text, '')
        # Verify the Search table columns(row 2)
        self.assertEqual(sterm2.text, '(HP:0000822)\nHypertension')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'related')
        self.assertEqual(mterm2.text, '(MP:0002842)\nincreased systemic arterial blood pressure')
        self.assertEqual(termsyn2.text, 'high blood pressure')

    def test_rel_syn_to_syn30(self):
        """
        @status these tests verify a relationship that has a synonym match to Hypoplasia of the fallopian tube
        @see: HMDC-syn-to-syn-30
        """
        print("BEGIN test_rel_syn_to_syn30")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0008697")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0008697)\nHypoplasia of the fallopian tube')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0003576)\noviduct hypoplasia')
        self.assertEqual(termsyn1.text, 'fallopian tube hypoplasia | hypoplastic oviduct | rudimentary fallopian tubes | rudimentary oviduct | rudimentary salpinges | rudimentary salpinx | rudimentary salpinx uterina | rudimentary tuba fallopiana | rudimentary tuba fallopii | rudimentary tuba uterina | rudimentary uterine tube | salpinges hypoplasia | salpinx hypoplasia | salpinx uterina hypoplasia | tuba fallopiana hypoplasia | tuba fallopii hypoplasia | tuba uterina hypoplasia | uterine tube hypoplasia')

    def test_rel_syn_to_syn31(self):
        """
        @status these tests verify a relationship that has a synonym match to Hypoplasia of the ovary
        @see: HMDC-syn-to-syn-31
        """
        print("BEGIN test_rel_syn_to_syn31")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0008724")  # identifies the input field and enters an MP ID
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
        # Iterate the table columns for row 2
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype2.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        termsyn2 = table.get_cell(2, 5)
        print(termsyn2.text)
        # Iterate the table columns for row 3
        sterm3 = table.get_cell(3, 0)
        print(sterm3.text)
        mmethod3 = table.get_cell(3, 2)
        print(mmethod3.text)
        mtype3 = table.get_cell(3, 3)
        print(mtype3.text)
        mterm3 = table.get_cell(3, 4)
        print(mterm3.text)
        termsyn3 = table.get_cell(3, 5)
        print(termsyn3.text)
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm1.text, '(HP:0008724)\nHypoplasia of the ovary')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0001127)\nsmall ovary')
        self.assertEqual(termsyn1.text, 'decreased ovary size | reduced ovary size | small ovaries')
        # Verify the Search table columns(row 2)
        self.assertEqual(sterm2.text, '(HP:0008724)\nHypoplasia of the ovary')
        self.assertEqual(mmethod2.text, 'manual')
        self.assertEqual(mtype2.text, 'broad')
        self.assertEqual(mterm2.text, '(MP:0004856)\ndecreased ovary weight')
        self.assertEqual(termsyn2.text, 'reduced ovary weight')
        # Verify the Search table columns(row 3)
        self.assertEqual(sterm3.text, '(HP:0008724)\nHypoplasia of the ovary')
        self.assertEqual(mmethod3.text, 'lexical')
        self.assertEqual(mtype3.text, 'exact')
        self.assertEqual(mterm3.text, '(MP:0005158)\novary hypoplasia')
        self.assertEqual(termsyn3.text, 'hypoplastic ovaries | hypoplastic ovary | ovarian hypoplasia | rudimentary ovary')

    def test_rel_syn_to_syn32(self):
        """
        @status these tests verify a relationship that has a synonym match to Hypoplasia of the vagina
        @see: HMDC-syn-to-syn-32
        """
        print("BEGIN test_rel_syn_to_syn32")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0008726")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0008726)\nHypoplasia of the vagina')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0008984)\nvagina hypoplasia')
        self.assertEqual(termsyn1.text, 'hypoplastic vagina | rudimentary vagina | vaginal hypoplasia')

    def test_rel_syn_to_syn33(self):
        """
        @status these tests verify a relationship that has a synonym match to Intestinal polyp
        @see: HMDC-syn-to-syn-33
        """
        print("BEGIN test_rel_syn_to_syn33")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0005266")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0005266)\nIntestinal polyp')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0008011)\nintestine polyps')
        self.assertEqual(termsyn1.text, 'intestinal polyposis | intestinal polyps')

    def test_rel_syn_to_syn34(self):
        """
        @status these tests verify a relationship that has a synonym match to Lower limb muscle weakness
        @see: HMDC-syn-to-syn-34
        """
        print("BEGIN test_rel_syn_to_syn34")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0007340")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0007340)\nLower limb muscle weakness')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0031204)\nhindlimb paresis')
        self.assertEqual(termsyn1.text, 'hind limb paresis | hind limb weakness | hindlimb weakness | lameness | leg weakness')

    def test_rel_syn_to_syn35(self):
        """
        @status these tests verify a relationship that has a synonym match to Absent toe
        @see: HMDC-syn-to-syn-35
        """
        print("BEGIN test_rel_syn_to_syn35")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0010760")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0010760)\nAbsent toe')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0000561)\nadactyly')
        self.assertEqual(termsyn1.text, 'absence of digits | absent fingers | absent toes')

    def test_rel_syn_to_syn36(self):
        """
        @status these tests verify a relationship that has a synonym match to short nose
        @see: HMDC-syn-to-syn-36
        """
        print("BEGIN test_rel_syn_to_syn36")
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
        # Iterate the table columns for row 2
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype2.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        termsyn2 = table.get_cell(2, 5)
        print(termsyn2.text)
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm1.text, '(HP:0003196)\nShort nose')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0000445)\nshort snout')
        self.assertEqual(termsyn1.text, 'decreased snout length | short nasal dorsum | short nasal ridge | short nose | short nose ridge')
        # Verify the Search table columns(row 2)
        self.assertEqual(sterm2.text, '(HP:0003196)\nShort nose')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'related')
        self.assertEqual(mterm2.text, '(MP:0030190)\nsmall snout')
        self.assertEqual(termsyn2.text, 'decreased muzzle size | decreased nose size | decreased snout size | reduced muzzle size | reduced nose size | reduced snout size | small muzzle | small nose')

    '''def test_rel_syn_to_syn38(self):
        
        @status these tests verify a relationship that has a synonym match to Pterygium (should not find a match)
        @see: HMDC-syn-to-syn-38
        
        print("BEGIN test_rel_syn_to_syn38")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0001059")  #identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click() #find the Search  for related terms button and click it
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
        self.assertEqual(sterm1.text, '(MP:0003664)\nocular pterygium')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(HP:0002617)\nVascular dilatation')
        self.assertEqual(termsyn1.text, 'Aneurysm | Aneurysmal dilatation | Aneurysmal disease | Aneurysms | Wider than typical opening or gap')
        '''
    '''def test_rel_syn_to_syn39(self):
        
        @status these tests verify a relationship that has a synonym match to Hearing impairment
        @see: HMDC-syn-to-syn-39
        
        print("BEGIN test_rel_syn_to_syn39")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0000365")  #identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click() #find the Search  for related terms button and click it
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
        self.assertEqual(sterm1.text, '(MP:0006325)\nimpaired hearing')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(HP:0002617)\nVascular dilatation')
        self.assertEqual(termsyn1.text, 'Aneurysm | Aneurysmal dilatation | Aneurysmal disease | Aneurysms | Wider than typical opening or gap')
'''
    '''def test_rel_syn_to_syn40(self):
        
        @status these tests verify a relationship that has a synonym match to Polycystic kidney dysplasia
        @see: HMDC-syn-to-syn-40
        
        print("BEGIN test_rel_syn_to_syn40")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0000113")  #identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click() #find the Search  for related terms button and click it
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
        self.assertEqual(sterm1.text, '(MP:0008528)\npolycystic kidney')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(HP:0002617)\nVascular dilatation')
        self.assertEqual(termsyn1.text, 'Aneurysm | Aneurysmal dilatation | Aneurysmal disease | Aneurysms | Wider than typical opening or gap')
'''
    def test_rel_syn_to_syn41(self):
        """
        @status these tests verify a relationship that has a synonym match to Retrognathia
        @see: HMDC-syn-to-syn-41
        """
        print("BEGIN test_rel_syn_to_syn41")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0000278")  # identifies the input field and enters an MP ID
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
        # Iterate the table columns for row 2
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype2.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        termsyn2 = table.get_cell(2, 5)
        print(termsyn2.text)
        # Iterate the table columns for row 3
        sterm3 = table.get_cell(3, 0)
        print(sterm3.text)
        mmethod3 = table.get_cell(3, 2)
        print(mmethod3.text)
        mtype3 = table.get_cell(3, 3)
        print(mtype3.text)
        mterm3 = table.get_cell(3, 4)
        print(mterm3.text)
        termsyn3 = table.get_cell(3, 5)
        print(termsyn3.text)
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm1.text, '(HP:0000278)\nRetrognathia')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0030273)\nmandibular retrognathia')
        self.assertEqual(termsyn1.text, 'mandibular retrognathism | mandibular retroposition | receding lower jaw | receding mandible | retrognathia of lower jaw')
        # Verify the Search table columns(row 2)
        self.assertEqual(sterm2.text, '(HP:0000278)\nRetrognathia')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'exact')
        self.assertEqual(mterm2.text, '(MP:0004282)\nretrognathia')
        self.assertEqual(termsyn2.text, 'jaw retroposition | receding jaw | recessed jaw | retrognathism')
        # Verify the Search table columns(row 3)
        self.assertEqual(sterm3.text, '(HP:0000278)\nRetrognathia')
        self.assertEqual(mmethod3.text, 'lexical')
        self.assertEqual(mtype3.text, 'broad')
        self.assertEqual(mterm3.text, '(MP:0030270)\nretrogenia')
        self.assertEqual(termsyn3.text, 'receding chin | recessed chin')

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHmdcSynToSynSearch))
    return suite
