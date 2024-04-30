"""
Created on Dec 11, 2023

This file contains the tests for Hmdc relationships for MP to HP Narrow searches that are entered via the Hmdc search form.
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


class TestHmdcRelationshipMPNarrowSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)

    def test_rel_2lex_narrow_2dif_terms(self):
        """
        @status these tests verify a relationship that 2 lexical narrow matches to different MP terms
        @see: HMDC-nar-mphp-1
        """
        print("BEGIN test_rel_2lex_narrow_2dif_terms")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0010479")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns row 1
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
        # Verify the Search table columns for (row 1)
        self.assertEqual(sterm.text, '(MP:0010479)\nbrain aneurysm')
        self.assertEqual(mmethod.text, 'lexical')
        self.assertEqual(mtype.text, 'narrow')
        self.assertEqual(mterm.text, '(HP:0004944)\nDilatation of the cerebral artery')
        self.assertEqual(termsyn.text, 'Brain aneurysm | Cerebral aneurysm | Cerebral artery aneurysm | Intracranial aneurysm')

    def test_rel_narrow_override_man_match(self):
        """
        @status these tests verify a relationship that overridden by manual narrow match
        @see: HMDC-nar-mphp-2
        """
        print("BEGIN test_rel_narrow_override_man_match")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0003605")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns rows 1 & 2
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
        # Verify the Search table columns for (rows 1 & 2)
        self.assertEqual(sterm.text, '(MP:0003605)\nfused kidneys')
        self.assertEqual(mmethod.text, 'manual')
        self.assertEqual(mtype.text, 'narrow')
        self.assertEqual(mterm.text, '(HP:0000085)\nHorseshoe kidney')
        self.assertEqual(termsyn.text, 'Fused kidneys | Horseshoe kidney | Horseshoe kidneys')
        self.assertEqual(sterm2.text, '(MP:0003605)\nfused kidneys')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'narrow')
        self.assertEqual(mterm2.text, '(HP:0034233)\nDisc kidney')
        self.assertEqual(termsyn2.text, 'Type D cross fused renal ectopia')

    def test_rel_lex_narrow_basic(self):
        """
        @status these tests verify a relationship that has a basic result(narrow)(standard result)
        @see: HMDC-nar-mphp-3
        """
        print("BEGIN test_rel_lex_narrow_basic")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0004554")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(MP:0004554)\nsmall pharynx')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(HP:0009555)\nHypoplasia of the pharynx')
        self.assertEqual(termsyn1.text, 'Decreased diameter of pharynx | Decreased length of pharynx | Decreased size of pharynx | Decreased volume of pharynx | Decreased width of pharynx | Hypotrophic pharynx | Small pharynx | Underdevelopment of pharynx')


    def test_rel_override_man_narrow_match(self):
        """
        @status these tests verify a relationship that overridden by manual narrow match
        @see: HMDC-nar-mphp-4
        """
        print("BEGIN test_rel_override_man_narrow_match")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0012174")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(MP:0012174)\nflat head')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(HP:0001357)\nPlagiocephaly')
        self.assertEqual(termsyn1.text, 'Asymmetry of the posterior cranium | Asymmetry of the posterior head | Asymmetry of the posterior skull | Deformational plagiocephaly | Flat head | Flat head syndrome | Flattening of cranial vault | Flattening of cranium | Flattening of head | Flattening of skull | Positional plagiocephaly | Rhomboid shaped cranium | Rhomboid shaped head | Rhomboid shaped skull')

    def test_rel_2lex_narrow_dif_terms(self):
        """
        @status these tests verify a relationship that 2 lexical narrow matches to different MP terms
        @see: HMDC-nar-mphp-5
        """
        print("BEGIN test_rel_2lex_narrow_dif_terms")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0010478")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(MP:0010478)\nintracranial aneurysm')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(HP:0004944)\nDilatation of the cerebral artery')
        self.assertEqual(termsyn1.text, 'Brain aneurysm | Cerebral aneurysm | Cerebral artery aneurysm | Intracranial aneurysm')

    def test_rel_over_man_narrow_match(self):
        """
        @status these tests verify a relationship that overridden by manual narrow match
        @see: HMDC-nar-mphp-6
        """
        print("BEGIN test_rel_over_man_narrow_match")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0003623")  # identifies the input field and enters an MP ID
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
        # Verify the Search Term table columns(row 1)
        self.assertEqual(sterm1.text, '(MP:0003623)\nhydrocele')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(HP:0000034)\nHydrocele testis')
        self.assertEqual(termsyn1.text, 'Hydrocele | Testicular hydrocele')

    def test_rel_lex_exact_narrow_match_diff_terms(self):
        """
        @status these tests verify a relationship that lexical exact and narrow matches to 2 different MP terms
        @see: HMDC-nar-mphp-7
        """
        print("BEGIN test_rel_lex_exact_narrow_match_diff_terms")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0004470")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(MP:0004470)\nsmall nasal bone')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(HP:0004646)\nHypoplasia of the nasal bone')
        self.assertEqual(termsyn1.text, 'Decreased size of nasal bone | Deficiency of nasal bone | Hypotrophic nasal bone | Nasal bone hypoplasia | Small nasal bone | Underdevelopment of nasal bone')

    def test_over_man_close_match(self):
        """
        @status these tests verify a relationship that overridden by manual close match, HP has 3 manual matches
        @see: HMDC-nar-mphp-8
        """
        print("BEGIN test_rel_over_man_close_match")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0009890")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(MP:0009890)\ncleft secondary palate')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(HP:0000175)\nCleft palate')
        self.assertEqual(termsyn1.text, 'Cleft hard and soft palate | Cleft of hard and soft palate | Cleft of palate | Cleft palate | Cleft roof of mouth | Cleft secondary palate | Palatoschisis | Uranostaphyloschisis')

    def test_rel_lex_exact_narrow_match_2term(self):
        """
        @status these tests verify a relationship that lexical exact and narrow matches to 2 different MP terms
        @see: HMDC-nar-mphp-9
        """
        print("BEGIN test_lex_exact_narrow_match_2term")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0030268")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(MP:0030268)\nagnathia')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(HP:0009939)\nMandibular aplasia')
        self.assertEqual(termsyn1.text, 'Absence of lower jaw | Absence of lower jaw bone | Absence of lower jaw bones | Absence of mandible | Absent mandible | Agenesis of the mandible | Agnathia | Aplasia of the lower jaw bone | Failure of development of lower jaw | Failure of development of mandible | Missing lower jaw')

    def test_rel_over_manual_narrow_match(self):
        """
        @status these tests verify a relationship that overridden by manual narrow match
        @see: HMDC-nar-mphp-10
        """
        print("BEGIN test_over_manual_narrow_match")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0005291")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(MP:0005291)\nabnormal glucose tolerance')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(HP:0001952)\nGlucose intolerance')
        self.assertEqual(termsyn1.text, 'Abnormal glucose tolerance | Glucose intolerance')


    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHmdcRelationshipMPNarrowSearch))
    return suite
