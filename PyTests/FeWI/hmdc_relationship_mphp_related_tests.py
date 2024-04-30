"""
Created on Jan 6, 2017
Updated: July 2017 (jlewis).  Updates to be more tolerant of data changes.  Cross-reference requirements with test cases.
Remove assertions in tests that are outside scope of requirement being tested.

This file contains the tests for Gene nomenclature searches (mouse and human) that are entered via the Gene Symbol(s)/ID(s)
query field and/or the Gene Name query fields.
Tests are organized in this order in the file:  Negative tests; gene symbol tests, gene name tests, and multiple field tests
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

from HTMLTestRunner import HTMLTestRunner
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


class TestHmdcRelationshipMPRelatedSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)

    def test_rel_man_narrow_dif_term_and_lex(self):
        """
        @status these tests verify a relationship that has manual narrow to a different term and lexical
        @see: HMDC-rl-mphp-1
        """
        print("BEGIN test_rel_man_narrow_dif_term_and_lex")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0010718")  # identifies the input field and enters an MP ID
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
        # Verify the Search table columns for (row 1)
        self.assertEqual(sterm.text, '(MP:0010718)\nchoroid coloboma')
        self.assertEqual(mmethod.text, 'lexical')
        self.assertEqual(mtype.text, 'related')
        self.assertEqual(mterm.text, '(HP:0000567)\nChorioretinal coloboma')

    def test_rel_man_override_same_term(self):
        """
        @status these tests verify a relationship that overridden by a manual match to the same term
        @see: HMDC-rl-mphp-2
        """
        print("BEGIN test_rel_man_override_same_term")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0002626")  # identifies the input field and enters an MP ID
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
        # Verify the Search table columns (row 1)
        self.assertEqual(sterm.text, '(MP:0002626)\nincreased heart rate')
        self.assertEqual(mmethod.text, 'manual')
        self.assertEqual(mtype.text, 'exact')
        self.assertEqual(mterm.text, '(HP:0001649)\nTachycardia')

    def test_rel_lex_related_basic(self):
        """
        @status these tests verify a relationship that has a basic result(standard result)
        @see: HMDC-rl-mphp-3
        """
        print("BEGIN test_rel_lex_related_basic")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0006156")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(MP:0006156)\nabnormal visual pursuit')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(HP:0007772)\nImpaired smooth pursuit')
        self.assertEqual(termsyn1.text, 'Abnormality of visual tracking | Abnormal visual pursuit | Impairment of visual pursuit')


    def test_rel_lex_exact_related_2_mp(self):
        """
        @status these tests verify a relationship that has lexical exact and related to 2 different MP terms
        @see: HMDC-rl-mphp-4
        """
        print("BEGIN test_rel_lex_exact_related_2_mp")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0001194")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(MP:0001194)\ndermatitis')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(HP:0011123)\nInflammatory abnormality of the skin')
        self.assertEqual(termsyn1.text, 'Abnormal tendency to infections of the skin | Dermatitis | Inflammatory abnormality of the skin | Inflammatory skin disease | Skin inflammation')

    def test_rel_man_lex_2_mp(self):
        """
        @status these tests verify a relationship that has manual & lexical to 2 different MP terms
        @see: HMDC-rl-mphp-5
        """
        print("BEGIN test_rel_man_lex_2_mp")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0011676")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(MP:0011676)\naortic arch obstruction')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(HP:0011611)\nInterrupted aortic arch')
        self.assertEqual(termsyn1.text, 'Aortic arch obstruction | Atretic transverse aortic arch')

    def test_rel_lex_close_2_mp(self):
        """
        @status these tests verify a relationship that has lexical close and related to different terms
        @see: HMDC-rl-mphp-6
        """
        print("BEGIN test_rel_lex_close_2_mp")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0001211")  # identifies the input field and enters an MP ID
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
        # Iterate the table row2 columns
        sterm2 = table.get_cell(2, 0)
        print(sterm2.text)
        mmethod2 = table.get_cell(2, 2)
        print(mmethod2.text)
        mtype2 = table.get_cell(2, 3)
        print(mtype2.text)
        mterm2 = table.get_cell(2, 4)
        print(mterm2.text)
        # Verify the Search table columns(rows 1 & 2)
        self.assertEqual(sterm1.text, '(MP:0001211)\nwrinkled skin')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'close')
        self.assertEqual(mterm1.text, '(HP:0007392)\nExcessive wrinkled skin')
        self.assertEqual(sterm2.text, '(MP:0001211)\nwrinkled skin')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'related')
        self.assertEqual(mterm2.text, '(HP:0100678)\nPremature skin wrinkling')

    def test_rel_over_lex_broad(self):
        """
        @status these tests verify a relationship that over-ridden by lexical broad
        @see: HMDC-rl-mphp-7
        """
        print("BEGIN test_rel_over_lex_broad")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0003290")  # identifies the input field and enters an MP ID
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
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm1.text, '(MP:0003290)\nintestinal hypoperistalsis')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(HP:0100771)\nHypoperistalsis')

    def test_rel_man_lex_2dif_mp(self):
        """
        @status these tests verify a relationship that has manual and lexical to 2 different MP terms
        @see: HMDC-rl-mphp-8
        """
        print("BEGIN test_rel_man_lex_2dif_mp")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0004143")  # identifies the input field and enters an MP ID
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
        # Verify the Search table columns(row 1)
        self.assertEqual(sterm1.text, '(MP:0004143)\nmuscle hypertonia')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(HP:0001257)\nSpasticity')
        self.assertEqual(termsyn1.text, 'Involuntary muscle stiffness, contraction, or spasm | Muscle spasticity | Muscular spasticity')
        # Verify the Search table columns(row 2)
        self.assertEqual(sterm2.text, '(MP:0004143)\nmuscle hypertonia')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'related')
        self.assertEqual(mterm2.text, '(HP:0001276)\nHypertonia')
        self.assertEqual(termsyn2.text,'Hypertonicity | Increased muscle tone | Muscle hypertonia | Spasticity and rigidity of muscles')

    def test_rel_lex_man_dif_term(self):
        """
        @status these tests verify a relationship that has both lexical and manual to a different term
        @see: HMDC-rl-mphp-9
        """
        print("BEGIN test_lex_man_dif_term")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0002766")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(MP:0002766)\nsitus inversus')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(HP:0001696)\nSitus inversus totalis')
        self.assertEqual(termsyn1.text, 'All organs on wrong side of body | Situs inversus | situs oppositus | situs transversus')

    def test_rel_lex_rel_exact_2dif_mp(self):
        """
        @status these tests verify a relationship that has both lexical related and exact to 2 different MP terms
        @see: HMDC-rl-mphp-10
        """
        print("BEGIN test_lex_rel_exact_2dif_mp")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0011418")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(MP:0011418)\nleukocyturia')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(HP:0012085)\nPyuria')
        self.assertEqual(termsyn1.text, 'High urine neutrophil count | Leukocyturia')

    def test_rel_lex_man_dif_term(self):
        """
        @status these tests verify a relationship that has both lexical and manual to a different term
        @see: HMDC-rl-mphp-11
        """
        print("BEGIN test_rel_lex_man_dif_term")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0004634")  # identifies the input field and enters an MP ID
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
        # Verify the Search table columns(rows 1 & 2)
        self.assertEqual(sterm1.text, '(MP:0004634)\nshort metacarpal bones')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(HP:0010034)\nShort 1st metacarpal')
        self.assertEqual(termsyn1.text, 'First metacarpal hypoplasia | First metacarpals hypoplastic | Hypoplastic 1st metacarpal | Shortened 1st long bone of hand | Short first metacarpal | Short first metacarpals')
        self.assertEqual(sterm2.text, '(MP:0004634)\nshort metacarpal bones')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'related')
        self.assertEqual(mterm2.text, '(HP:0010049)\nShort metacarpal')
        self.assertEqual(termsyn2.text, 'Brachymetacarpalia | Hypoplastic metacarpal | Metacarpal hypoplasia | Shortened long bone of hand | Shortened long bones of hand | Shortened metacarpals | Shortening of metacarpals | Short metacarpal bones | Short metacarpals')

    def test_rel_over_man_exact_same_term(self):
        """
        @status these tests verify a relationship that overridden by a manual match to the same term, HP term also has additional manual mappings
        @see: HMDC-rl-mphp-12
        """
        print("BEGIN test_over_man_exact_same_term")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0005039")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(MP:0005039)\nhypoxia')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(HP:0012418)\nHypoxemia')
        self.assertEqual(termsyn1.text, 'Hypoxia | Low blood oxygen level')

    def test_rel_lex_exact_relate_2dif_term(self):
        """
        @status these tests verify a relationship that has lexical exact and related to 2 different MP terms
        @see: HMDC-rl-mphp-12
        """
        print("BEGIN test_lex_exact_relate_2dif_term")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("MP:0001222")  # identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(MP:0001222)\nepidermal hyperplasia')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(HP:0025092)\nEpidermal acanthosis')
        self.assertEqual(termsyn1.text, 'Acanthosis | Acanthotic epidermis | Epidermal hyperplasia | Thickening of upper layer of skin')


    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHmdcRelationshipMPRelatedSearch))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))