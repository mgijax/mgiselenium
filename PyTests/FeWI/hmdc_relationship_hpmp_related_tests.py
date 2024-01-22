'''
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
'''
import unittest
import time
import tracemalloc
import config
import sys, os.path

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests
tracemalloc.start()


class TestHmdcRelationshipHpRelated(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        self.driver.implicitly_wait(10)


    def test_rel_related_hp_standard(self):
        '''
        @status these tests verify a relationship that is a standard related HP standard
        @see: HMDC-rel-hpmp-1
        '''
        print("BEGIN test_rel_related_hp_standard")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0002666")  #identifies the input field and enters an MP ID
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
        # Verify the Search Term table columns(row 1)
        self.assertEqual(sterm1.text, '(HP:0002666)\nPheochromocytoma')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0002050)\nincreased pheochromocytoma incidence')
        self.assertEqual(termsyn1.text, 'increased phaeochromocytoma incidence | phaeochromocytoma | pheochromocytoma')

    def test_rel_over_man_match1(self):
        '''
        @status these tests verify a relationship that is overridden by manual match
        @see: HMDC-rel-hpmp-2
        '''
        print("BEGIN test_rel_over_man_match1")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0009792")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0009792)\nTeratoma')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0002627)\nincreased teratoma incidence')
        self.assertEqual(termsyn1.text, 'teratoma')

    def test_rel_over_man_match2(self):
        '''
        @status these tests verify a relationship that is overridden by manual match (2)
        @see: HMDC-rel-hpmp-3
        '''
        print("BEGIN test_rel_over_man_match2")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0001028")  #identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click() #find the Search  for related terms button and click it
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
        # Verify the Search table columns (row 1)
        self.assertEqual(sterm.text, '(HP:0001028)\nHemangioma')
        self.assertEqual(mmethod.text, 'manual')
        self.assertEqual(mtype.text, 'related')
        self.assertEqual(mterm.text, '(MP:0002947)\nincreased hemangioma incidence')
        self.assertEqual(termsyn.text, 'angioma | haemangioma | hemangioma | increased angiomoma incidence | increased haemangioma incidence')

    def test_rel_over_man_match3(self):
        '''
        @status these tests verify a relationship that is overridden by manual switch 3
        @see: HMDC-rel-hpmp-4
        '''
        print("BEGIN test_rel_over_man_match3")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0000093")  #identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click() #find the Search  for related terms button and click it
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
        # Verify the Search table columns (row 1)
        self.assertEqual(sterm1.text, '(HP:0000093)\nProteinuria')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0002962)\nincreased urine protein level')
        self.assertEqual(termsyn1.text, 'increased protein excretion | proteinuria')

    def test_rel_related_hp_standard2(self):
        '''
        @status these tests verify a relationship that has a basic result(related)(standard result)
        @see: HMDC-rel-hpmp-5
        '''
        print("BEGIN test_rel_hp_standard2")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0002486")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0002486)\nMyotonia')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0003157)\nimpaired muscle relaxation')
        self.assertEqual(termsyn1.text, 'myotonia')

    def test_rel_add_man_match(self):
        '''
        @status these tests verify a relationship that has additional manual match
        @see: HMDC-rel-hpmp-6
        '''
        print("BEGIN test_rel_add_man_match")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0100256")  #identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click() #find the Search  for related terms button and click it
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
        # Verify the Search table columns(row 1 & 2)
        self.assertEqual(sterm1.text, '(HP:0100256)\nSenile plaques')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0003329)\namyloid beta deposits')
        self.assertEqual(termsyn1.text, 'amyloid beta plaques | increased amyloid beta deposition')
        self.assertEqual(sterm2.text, '(HP:0100256)\nSenile plaques')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'related')
        self.assertEqual(mterm2.text, '(MP:0003214)\nneurofibrillary tangles')
        self.assertEqual(termsyn2.text, 'neuritic plaques | senile plaques')

    def test_rel_related_hp_standard3(self):
        '''
        @status these tests verify a relationship that is a standard related HP standard(3)
        @see: HMDC-rel-hpmp-7
        '''
        print("BEGIN test_related_hp_standard3")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0410267")  #identifies the input field and enters an MP ID
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
        # Verify the Search table column(row 1)
        self.assertEqual(sterm1.text, '(HP:0410267)\nIntestinal hemangioma')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0003287)\nincreased intestinal hemangioma incidence')
        self.assertEqual(termsyn1.text, 'increased intestinal haemangioma incidence | intestinal angioma | intestinal haemangioma | intestinal hemangioma')

    def test_rel_related_hp_standard4(self):
        '''
        @status these tests verify a relationship that is a standard related HP standard(4)
        @see: HMDC-rel-hpmp-8
        '''
        print("BEGIN test_rel_related_hp_standard4")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0002586")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0002586)\nPeritonitis')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0003303)\nperitoneal inflammation')
        self.assertEqual(termsyn1.text, 'peritoneum inflammation | peritonitis')

    def test_rel_related_hp_standard5(self):
        '''
        @status these tests verify a relationship that is a standard related HP standard(5)
        @see: HMDC-rel-hpmp-9
        '''
        print("BEGIN test_rel_related_hp_standard5")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0001402")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0001402)\nHepatocellular carcinoma')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0003331)\nincreased hepatocellular carcinoma incidence')
        self.assertEqual(termsyn1.text, 'HCC | hepatocellular carcinoma | liver neoplasia | liver neoplasm | malignant hepatoma | neoplastic liver')

    def test_rel_related_hp_standard6(self):
        '''
        @status these tests verify a relationship that is a standard related HP standard(6)
        @see: HMDC-rel-hpmp-10
        '''
        print("BEGIN test_rel_related_hp_standard6")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0008208")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0008208)\nParathyroid hyperplasia')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0003493)\nparathyroid gland hyperplasia')
        self.assertEqual(termsyn1.text, 'hyperplastic parathyroid gland | parathyroid hyperplasia')

    def test_rel_add_logical_match(self):
        '''
        @status these tests verify a relationship that has additional logical match
        @see: HMDC-rel-hpmp-11
        '''
        print("BEGIN test_rel_add_logical_match")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0008249")  #identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click() #find the Search  for related terms button and click it
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
        self.assertEqual(sterm1.text, '(HP:0008249)\nThyroid hyperplasia')
        self.assertEqual(mmethod1.text, 'logical')
        self.assertEqual(mtype1.text, 'close')
        self.assertEqual(mterm1.text, '(MP:0005355)\nenlarged thyroid gland')
        self.assertEqual(termsyn1.text, 'goiter | increased thyroid gland size')
        self.assertEqual(sterm2.text, '(HP:0008249)\nThyroid hyperplasia')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'related')
        self.assertEqual(mterm2.text, '(MP:0003498)\nthyroid gland hyperplasia')
        self.assertEqual(termsyn2.text, 'hyperplastic thyroid | thyroid hyperplasia')

    def test_rel_related_hp_standard7(self):
        '''
        @status these tests verify a relationship that is a standard related HP standard(7)
        @see: HMDC-rel-hpmp-12
        '''
        print("BEGIN test_rel_related_hp_standard7")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0100718")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0100718)\nUterine rupture')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0003571)\nuterus rupture')
        self.assertEqual(termsyn1.text, 'metral rupture | metra rupture | rupture of uterus | uterine rupture')

    def test_rel_related_hp_standard8(self):
        '''
        @status these tests verify a relationship that is a standard related HP standard(8)
        @see: HMDC-rel-hpmp-13
        '''
        print("BEGIN test_rel_related_hp_standard8")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0025464")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0025464)\nIncreased reactive oxygen species production')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0003674)\noxidative stress')
        self.assertEqual(termsyn1.text, 'increased reactive oxygen species production | increased ROS production')

    def test_rel_over_by_man_mapping(self):
        '''
        @status these tests verify a relationship that is overridden by manual mapping
        @see: HMDC-rel-hpmp-14
        '''
        print("BEGIN test_over_by_man_mapping")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0000268")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0000268)\nDolichocephaly')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0003742)\nnarrow head')
        self.assertEqual(termsyn1.text, 'dolichocephaly')

    def test_rel_add_man_mapping(self):
        '''
        @status these tests verify a relationship that has additional manual mapping
        @see: HMDC-rel-hpmp-15
        '''
        print("BEGIN test_rel_add_man_mapping")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click()  # find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0002860")  # identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click()  # find the Search  for related terms button and click it
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
        self.assertEqual(sterm1.text, '(HP:0002860)\nSquamous cell carcinoma')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0009704)\nincreased skin squamous cell carcinoma incidence')
        self.assertEqual(termsyn1.text, 'skin squamous cell carcinoma')
        self.assertEqual(sterm2.text, '(HP:0002860)\nSquamous cell carcinoma')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'related')
        self.assertEqual(mterm2.text, '(MP:0004207)\nincreased squamous cell carcinoma incidence')
        self.assertEqual(termsyn2.text, 'SCC | squamous cell carcinoma')

    def test_rel_add_man_mapping2(self):
        '''
        @status these tests verify a relationship that has additional manual mapping
        @see: HMDC-rel-hpmp-16
        '''
        print("BEGIN test_add_man_mapping2")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0006267")  #identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click() #find the Search  for related terms button and click it
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
        self.assertEqual(sterm1.text, '(HP:0006267)\nLarge placenta')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'broad')
        self.assertEqual(mterm1.text, '(MP:0004920)\nincreased placenta weight')
        self.assertEqual(termsyn1.text, '')
        self.assertEqual(sterm2.text, '(HP:0006267)\nLarge placenta')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'related')
        self.assertEqual(mterm2.text, '(MP:0004260)\nenlarged placenta')
        self.assertEqual(termsyn2.text, 'increased size of placenta | large placenta | placentomegaly')

    def test_rel_man_match_another_term(self):
        '''
        @status these tests verify a relationship that in list search or single search only showing manual match to another term
        @see: HMDC-rel-hpmp-17
        '''
        print("BEGIN test_rel_man_match_another_term")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0002375")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0002375)\nHypokinesia')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0005156)\nbradykinesia')
        self.assertEqual(termsyn1.text, 'bradycinesia | hypokinesia | reduced spontaneous movement')

    def test_rel_additional_man_mapping(self):
        '''
        @status these tests verify a relationship that has additional manual match
        @see: HMDC-rel-hpmp-18
        '''
        print("BEGIN test_rel_additional_man_mapping")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0002140")  #identifies the input field and enters an MP ID
        self.driver.find_element(By.XPATH, '/html/body/form/div[4]/input[1]').click() #find the Search  for related terms button and click it
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
        # Verify the Search table columns(row 1 & 2)
        self.assertEqual(sterm1.text, '(HP:0002140)\nIschemic stroke')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0003076)\nincreased susceptibility to ischemic brain injury')
        self.assertEqual(termsyn1.text, 'decreased resistance to ischaemic brain injury | decreased resistance to ischemic brain injury | increased CNS stroke | increased susceptibility to ischaemic brain injury | increased susceptibility to spontaneous CNS ischaemia | increased susceptibility to spontaneous CNS ischemia')
        self.assertEqual(sterm2.text, '(HP:0002140)\nIschemic stroke')
        self.assertEqual(mmethod2.text, 'lexical')
        self.assertEqual(mtype2.text, 'related')
        self.assertEqual(mterm2.text, '(MP:0006080)\nbrain ischemia')
        self.assertEqual(termsyn2.text, 'brain ischaemia | cerebral ischaemia | cerebral ischemia | ischaemic stroke | ischemic stroke')

    def test_rel_over_man_mapping3(self):
        '''
        @status these tests verify a relationship that is overridden by manual mapping
        @see: HMDC-rel-hpmp-19
        '''
        print("BEGIN test_rel_over_man_mapping3")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0100545")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0100545)\nArterial stenosis')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0006135)\nartery stenosis')
        self.assertEqual(termsyn1.text, 'arterial stenosis')

    def test_rel_over_man_mapping4(self):
        '''
        @status these tests verify a relationship that is overridden by manual mapping
        @see: HMDC-rel-hpmp-20
        '''
        print("BEGIN test_rel_over_man_mapping4")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0012226")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0012226)\nOvarian teratoma')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0009442)\nincreased ovarian teratoma incidence')
        self.assertEqual(termsyn1.text, 'ovarian dermoid cyst | ovarian teratoma')

    def test_rel_over_by_lex_exact(self):
        '''
        @status these tests verify a relationship that is overridden by lexical exact
        @see: HMDC-rel-hpmp-21
        '''
        print("BEGIN test_over_by_lex_exact")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0006690")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0006690)\nMyocardial calcification')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0010534)\ncalcified myocardium')
        self.assertEqual(termsyn1.text, 'myocardial calcification')

    def test_rel_over_man_mapping5(self):
        '''
        @status these tests verify a relationship that is overridden by manual mapping
        @see: HMDC-rel-hpmp-22
        '''
        print("BEGIN test_rel_over_man_mapping5")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0002039")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0002039)\nAnorexia')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0011940)\ndecreased food intake')
        self.assertEqual(termsyn1.text, 'anorexia | hypophagia | loss of appetite | reduced food intake')

    def test_rel_over_by_lex_exact2(self):
        '''
        @status these tests verify a relationship that is overridden by lexical exact
        @see: HMDC-rel-hpmp-23
        '''
        print("BEGIN test_rel_over_by_lex_exact2")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0000215")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0000215)\nThick upper lip vermilion')
        self.assertEqual(mmethod1.text, 'lexical')
        self.assertEqual(mtype1.text, 'exact')
        self.assertEqual(mterm1.text, '(MP:0030169)\nthick upper lip')
        self.assertEqual(termsyn1.text, 'fleshy top lip | fleshy upper lip | full top lip | full upper lip | prominent top lip | prominent upper lip | thick top lip | thick top lip vermilion | thick upper lip vermilion')

    def test_rel_over_man_mapping6(self):
        '''
        @status these tests verify a relationship that is overridden by manual mapping
        @see: HMDC-rel-hpmp-24
        '''
        print("BEGIN test_rel_over_man_mapping6")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0030038")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0030038)\nEnchondroma')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0031283)\nincreased enchondroma incidence')
        self.assertEqual(termsyn1.text, 'enchondroma')

    def test_rel_over_man_mapping7(self):
        '''
        @status these tests verify a relationship that is overridden by manual mapping
        @see: HMDC-rel-hpmp-25
        '''
        print("BEGIN test_rel_over_man_mapping7")
        my_select = self.driver.find_element(By.XPATH,"//select[starts-with(@id, 'field_0_')]")  #identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Disease or Phenotype ID(s)':
                option.click()
                break

        self.driver.find_element(By.CSS_SELECTOR, ".btn-mybtn").click() #find and click the 'Add related phenotype terms by ID' button
        # switch focus to the new tab for HP-MP Search
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        self.driver.find_element(By.ID, "hpmpInput").send_keys("HP:0000329")  #identifies the input field and enters an MP ID
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
        self.assertEqual(sterm1.text, '(HP:0000329)\nFacial hemangioma')
        self.assertEqual(mmethod1.text, 'manual')
        self.assertEqual(mtype1.text, 'related')
        self.assertEqual(mterm1.text, '(MP:0031292)\nincreased facial hemangioma incidence')
        self.assertEqual(termsyn1.text, 'facial angioma | facial haemangioma | facial hemangioma | increased facial angiomoma incidence | increased facial haemangioma incidence')


    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHmdcRelationshipHpRelated))
    return suite
