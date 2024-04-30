"""
Created on Dec 11, 2023

This file contains the tests for Hmdc relationships for HP to MP Broad searches that are entered via the Hmdc search form.
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

    def test_rel_broad_hp_standard(self):
        """
        @status these tests verify a relationship that is a standard broad HP standard
        @see: HMDC-rel-hpmp-1
        """
        print("BEGIN test_rel_broad_hp_standard")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys(
            "HP:0025144")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH,
                                 '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for rows 1
        sterm1 = table.get_cell(1, 0)
        print(sterm1.text)
        mmethod1 = table.get_cell(1, 2)
        print(mmethod1.text)
        mtype1 = table.get_cell(1, 3)
        print(mtype1.text)
        mterm1 = table.get_cell(1, 4)
        print(mterm1.text)
        termsyn1 = table.get_cell(1, 5)
        print(termsyn1.text)
        # Verify the Search Term table columns(rows 1), match method, match type and Matched term are correct.
        self.assertEqual(sterm1.text, '(HP:0025144)\nShivering')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0000745)\ntremors')
        self.assertEqual(termsyn1.text, 'quivering | shaking | shivering | trembling | tremor')

    def test_rel_broad_hp_standard2(self):
        """
        @status these tests verify a relationship that is a standard broad HP standard
        @see: HMDC-rel-hpmp-2
        """
        print("BEGIN test_rel_broad_hp_standard2")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys(
            "HP:0003560")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH,
                                 '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for rows 1
        sterm1 = table.get_cell(1, 0)
        print(sterm1.text)
        mmethod1 = table.get_cell(1, 2)
        print(mmethod1.text)
        mtype1 = table.get_cell(1, 3)
        print(mtype1.text)
        mterm1 = table.get_cell(1, 4)
        print(mterm1.text)
        termsyn1 = table.get_cell(1, 5)
        print(termsyn1.text)
        # Verify the Search Term table columns(rows 1), match method, match type and Matched term are correct.
        self.assertEqual(sterm1.text, '(HP:0003560)\nMuscular dystrophy')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0000752)\ndystrophic muscle')
        self.assertEqual(termsyn1.text, 'muscular dystrophy')

    def test_rel_hp_add_man_match(self):
        """
        @status these tests verify a relationship that is additional manual match
        @see: HMDC-rel-hpmp-3
        """
        print("BEGIN test_rel_hp_add_man_match")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys(
            "HP:0002414")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH,
                                 '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table row 1 & 2
        sterm1 = table.get_cell(1, 0)
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
        # Verify the table rows 1 & 2
        self.assertEqual(sterm1.text, '(HP:0002414)\nSpina bifida')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0003054)\nspina bifida')
        self.assertEqual(termsyn1.text, 'spinal dysraphism')
        self.assertEqual(sterm2.text, '(HP:0002414)\nSpina bifida')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'broad')
        self.assertEqual(mterm2.text, '(MP:0000929)\nopen neural tube')
        self.assertEqual(termsyn2.text,
                         'failure of neural tube closure | hydrocele spinalis | schistorrhachis | spina bifida')

    def test_rel_hp_add_lex_match(self):
        """
        @status these tests verify a relationship that is additional lexical match
        @see: HMDC-rel-hpmp-4
        """
        print("BEGIN test_rel_hp_add_lex_match")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys(
            "HP:0012535")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH,
                                 '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table rows 1 through 8
        sterm1 = table.get_cell(1, 0)
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
        mmethod2 = table.get_cell(2, 2)
        mtype2 = table.get_cell(2, 3)
        mterm2 = table.get_cell(2, 4)
        termsyn2 = table.get_cell(2, 5)
        sterm3 = table.get_cell(3, 0)
        mmethod3 = table.get_cell(3, 2)
        mtype3 = table.get_cell(3, 3)
        mterm3 = table.get_cell(3, 4)
        termsyn3 = table.get_cell(3, 5)
        sterm4 = table.get_cell(4, 0)
        mmethod4 = table.get_cell(4, 2)
        mtype4 = table.get_cell(4, 3)
        mterm4 = table.get_cell(4, 4)
        termsyn4 = table.get_cell(4, 5)
        sterm5 = table.get_cell(5, 0)
        mmethod5 = table.get_cell(5, 2)
        mtype5 = table.get_cell(5, 3)
        mterm5 = table.get_cell(5, 4)
        termsyn5 = table.get_cell(5, 5)
        sterm6 = table.get_cell(6, 0)
        mmethod6 = table.get_cell(6, 2)
        mtype6 = table.get_cell(6, 3)
        mterm6 = table.get_cell(6, 4)
        termsyn6 = table.get_cell(6, 5)
        sterm7 = table.get_cell(7, 0)
        mmethod7 = table.get_cell(7, 2)
        mtype7 = table.get_cell(7, 3)
        mterm7 = table.get_cell(7, 4)
        termsyn7 = table.get_cell(7, 5)
        sterm8 = table.get_cell(8, 0)
        mmethod8 = table.get_cell(8, 2)
        mtype8 = table.get_cell(8, 3)
        mterm8 = table.get_cell(8, 4)
        termsyn8 = table.get_cell(8, 5)
        # Verify table row 1
        self.assertEqual(sterm1.text, '(HP:0012535)\nAbnormal synaptic transmission')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0004807)\nabnormal paired-pulse inhibition')
        self.assertEqual(termsyn1.text,
                         'abnormal paired pulse depression | abnormal paired-pulse depression | abnormal paired pulse inhibition | abnormal PPD | abnormal PPI')
        # Verify table row 2
        self.assertEqual(sterm2.text, '(HP:0012535)\nAbnormal synaptic transmission')
        self.assertEqual(mmethod2.text, 'manual')
        self.assertEqual(mtype2.text, 'broad')
        self.assertEqual(mterm2.text, '(MP:0004008)\nabnormal GABA-mediated receptor currents')
        self.assertEqual(termsyn2.text, 'abnormal gamma-amino-n-butyric acid receptor currents')
        # Verify table row 3
        self.assertEqual(sterm3.text, '(HP:0012535)\nAbnormal synaptic transmission')
        self.assertEqual(mmethod3.text, 'manual')
        self.assertEqual(mtype3.text, 'broad')
        self.assertEqual(mterm3.text, '(MP:0003008)\nenhanced long-term potentiation')
        self.assertEqual(termsyn3.text, 'enhanced long term potentiation | enhanced LTP')
        # Verify table row 4
        self.assertEqual(sterm4.text, '(HP:0012535)\nAbnormal synaptic transmission')
        self.assertEqual(mmethod4.text, 'manual')
        self.assertEqual(mtype4.text, 'broad')
        self.assertEqual(mterm4.text, '(MP:0001898)\nabnormal long-term depression')
        self.assertEqual(termsyn4.text, 'abnormal long term depression | abnormal LTD')
        # verify table row 5
        self.assertEqual(sterm5.text, '(HP:0012535)\nAbnormal synaptic transmission')
        self.assertEqual(mmethod5.text, 'manual')
        self.assertEqual(mtype5.text, 'broad')
        self.assertEqual(mterm5.text, '(MP:0001473)\nreduced long-term potentiation')
        self.assertEqual(termsyn5.text,
                         'deficient long term potentiation | deficient LTP | reduced long term potentiation')
        # Verify table row 6
        self.assertEqual(sterm6.text, '(HP:0012535)\nAbnormal synaptic transmission')
        self.assertEqual(mmethod6.text, 'manual')
        self.assertEqual(mtype6.text, 'broad')
        self.assertEqual(mterm6.text, '(MP:0001475)\nreduced long-term depression')
        self.assertEqual(termsyn6.text, 'deficient long term depression | deficient LTD | reduced long term depression')
        # Verify table row 7
        self.assertEqual(sterm7.text, '(HP:0012535)\nAbnormal synaptic transmission')
        self.assertEqual(mmethod7.text, 'lexical')
        self.assertEqual(mtype7.text, 'exact')
        self.assertEqual(mterm7.text, '(MP:0003635)\nabnormal synaptic transmission')
        self.assertEqual(termsyn7.text, 'abnormal neurotransmission')
        # Verify table row 8
        self.assertEqual(sterm8.text, '(HP:0012535)\nAbnormal synaptic transmission')
        self.assertEqual(mmethod8.text, 'lexical')
        self.assertEqual(mtype8.text, 'broad')
        self.assertEqual(mterm8.text, '(MP:0002206)\nabnormal CNS synaptic transmission')
        self.assertEqual(termsyn8.text, 'abnormal CNS neurotransmission | abnormal synaptic transmission')

    def test_rel_hp_add_man_match2(self):
        """
        @status these tests verify a relationship that is additional manual match
        @see: HMDC-rel-hpmp-5  !!!need a new example as the data for this example has changed!!!!
        """
        print("BEGIN test_rel_hp_add_man_match2")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys(
            "HP:0000045")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH,
                                 '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table row 1
        sterm1 = table.get_cell(1, 0)
        print(sterm1.text)
        mmethod1 = table.get_cell(1, 2)
        print(mmethod1.text)
        mtype1 = table.get_cell(1, 3)
        print(mtype1.text)
        mterm1 = table.get_cell(1, 4)
        print(mterm1.text)
        termsyn1 = table.get_cell(1, 5)
        print(termsyn1.text)
        # Verify the table row 1
        self.assertEqual(sterm1.text, '(HP:0000045)\nAbnormal scrotum morphology')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0002669)\nabnormal scrotum morphology')
        self.assertEqual(termsyn1.text, 'abnormality of the scrotum | scrotum dysplasia')

    def test_rel_hp_over_man_match(self):
        """
        @status these tests verify a relationship that overridden by manual exact
        @see: HMDC-rel-hpmp-6
        """
        print("BEGIN test_rel_hp_over_man_match")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys(
            "HP:0000083")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH,
                                 '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for rows 1
        sterm1 = table.get_cell(1, 0)
        print(sterm1.text)
        mmethod1 = table.get_cell(1, 2)
        print(mmethod1.text)
        mtype1 = table.get_cell(1, 3)
        print(mtype1.text)
        mterm1 = table.get_cell(1, 4)
        print(mterm1.text)
        termsyn1 = table.get_cell(1, 5)
        print(termsyn1.text)
        # Verify table (rows 1)
        self.assertEqual(sterm1.text, '(HP:0000083)\nRenal insufficiency')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0003606)\nkidney failure')
        self.assertEqual(termsyn1.text, 'renal failure | renal insufficiency')

    def test_rel_hp_add_man_broad(self):
        """
        @status these tests verify a relationship that overridden by manual broad
        @see: HMDC-rel-hpmp-7
        """
        print("BEGIN test_rel_hp_add_man_broad")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys(
            "HP:0410030")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH,
                                 '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for row 1
        sterm1 = table.get_cell(1, 0)
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
        self.assertEqual(sterm1.text, '(HP:0410030)\nCleft lip')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0005170)\ncleft upper lip')
        self.assertEqual(termsyn1.text, 'cheiloschisis | cleft lip | harelip')

    def test_rel_hp_over_lex_exact(self):
        """
        @status these tests verify a relationship that overridden by lexical exact
        @see: HMDC-rel-hpmp-8
        """
        print("BEGIN test_rel_hp_over_lex_exact")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys(
            "HP:0030160")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH,
                                 '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for row 1
        sterm1 = table.get_cell(1, 0)
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
        self.assertEqual(sterm1.text, '(HP:0030160)\nCervicitis')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0009228)\nuterine cervix inflammation')
        self.assertEqual(termsyn1.text,
                         'canalis cervicis uteri inflammation | caudal segment of uterus inflammation | cervical canal inflammation | cervical canal of uterus inflammation | cervical inflammation | cervicitis | cervix inflammation | cervix uteri inflammation | neck of uterus inflammation')

    def test_rel_hp_add_lex_match2(self):
        """
        @status these tests verify a relationship that is additional lexical match
        @see: HMDC-rel-hpmp-9
        """
        print("BEGIN test_rel_hp_add_lex_exact2")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys(
            "HP:0011040")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH,
                                 '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for rows 1 & 2
        sterm1 = table.get_cell(1, 0)
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
        # Verify the Search Term table columns(rows 1 & 2)
        self.assertEqual(sterm1.text, '(HP:0011040)\nAbnormal intrahepatic bile duct morphology')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0009497)\nabnormal intrahepatic bile duct morphology')
        self.assertEqual(termsyn1.text, 'abnormal intrahepatic biliary system morphology')
        self.assertEqual(sterm2.text, '(HP:0011040)\nAbnormal intrahepatic bile duct morphology')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'broad')
        self.assertEqual(mterm2.text, '(MP:0009494)\nabnormal biliary ductule morphology')
        self.assertEqual(termsyn2.text,
                         'abnormal cannalicular ductule morphology | abnormal ductuli biliferi | abnormal intrahepatic bile duct morphology')

    def test_rel_hp_add_man_match3(self):
        """
        @status these tests verify a relationship that is additional manual match
        @see: HMDC-rel-hpmp-10
        """
        print("BEGIN test_rel_hp_add_man_match3")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys(
            "HP:0005262")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH,
                                 '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for rows 1 & 2
        sterm1 = table.get_cell(1, 0)
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
        # Verify the Search Term table columns(rows 1 & 2)
        self.assertEqual(sterm1.text, '(HP:0005262)\nAbnormal synovial membrane morphology')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0008148)\nabnormal sternocostal joint morphology')
        self.assertEqual(termsyn1.text, 'abnormal rib-sternum attachment')
        self.assertEqual(sterm2.text, '(HP:0005262)\nAbnormal synovial membrane morphology')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'broad')
        self.assertEqual(mterm2.text, '(MP:0030866)\nabnormal synovial joint membrane morphology')
        self.assertEqual(termsyn2.text,
                         'abnormal stratum synoviale morphology | abnormal synovial joint lining morphology | abnormal synovial layer of articular capsule morphology | abnormal synovial membrane morphology | abnormal synovial membrane of synovial joint morphology | abnormal synovium morphology')

    def test_rel_hp_over_lex_exact(self):
        """
        @status these tests verify a relationship that is overridden by lexical exact match
        @see: HMDC-rel-hpmp-11
        """
        print("BEGIN test_rel_hp_over_lex_exact")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys(
            "HP:0000062")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH,
                                 '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for rows 1
        sterm1 = table.get_cell(1, 0)
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
        # Verify the Search Term table columns(rows 1)
        self.assertEqual(sterm1.text, '(HP:0000062)\nAmbiguous genitalia')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0031377)\nambiguous external genitalia')
        self.assertEqual(termsyn1.text, 'ambiguous genitalia | indeterminate external genitalia')

    def test_rel_add_man_match_over_lex_exact(self):
        """
        @status these tests verify a relationship that has additional manual match overridden by lexical exact match
        @see: HMDC-rel-hpmp-12
        """
        print("BEGIN test_rel_add_man_match_over_lex_exact")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys(
            "HP:0100333")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH,
                                 '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for row 1 & 2
        sterm1 = table.get_cell(1, 0)
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
        # Verify the Search Term table columns(row 1 & 2)
        self.assertEqual(sterm1.text, '(HP:0100333)\nUnilateral cleft lip')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0005170)\ncleft upper lip')
        self.assertEqual(termsyn1.text, 'cheiloschisis | cleft lip | harelip')
        self.assertEqual(sterm2.text, '(HP:0100333)\nUnilateral cleft lip')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'exact')
        self.assertEqual(mterm2.text, '(MP:0031447)\nunilateral cleft upper lip')
        self.assertEqual(termsyn2.text,
                         'one sided cleft upper lip | one-sided cleft upper lip | unilateral cheiloschisis | unilateral cleft lip')

    def test_rel_add_man_match4(self):
        """
        @status these tests verify a relationship that is additional manual match
        @see: HMDC-rel-hpmp-13
        """
        print("BEGIN test_rel_add_man_match4")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys(
            "HP:0100336")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH,
                                 '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
        mphp_table = self.driver.find_element(By.ID, 'hmdcTermSearchTable')
        table = Table(mphp_table)
        # Iterate the table columns for row 1 & 2
        sterm1 = table.get_cell(1, 0)
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
        # Verify the Search Term table columns(rows 1 & 2)
        self.assertEqual(sterm1.text, '(HP:0100336)\nBilateral cleft lip')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'narrow')
        self.assertEqual(mterm1.text, '(MP:0005170)\ncleft upper lip')
        self.assertEqual(termsyn1.text, 'cheiloschisis | cleft lip | harelip')
        self.assertEqual(sterm2.text, '(HP:0100336)\nBilateral cleft lip')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'broad')
        self.assertEqual(mterm2.text, '(MP:0031448)\nbilateral cleft upper lip')
        self.assertEqual(termsyn2.text, 'bilateral cheiloschisis | bilateral cleft lip')

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHmdcGenesSearch))
    return suite
