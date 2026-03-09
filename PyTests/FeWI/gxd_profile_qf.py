"""
Created on Jul 20, 2022
These tests check the functionality of the the GXD Profile query form
@author: jeffc
Verify that searching by a single anatomical structure & detected return the correct in classical mode
Verify that searching by a single anatomical structure & detected return the correct in RNA-Seq mode
Verify that searching by two anatomical structures & detected return the correct in classical mode
Verify that searching by two anatomical structures & detected return the correct in RNA-Seq mode
Verify that searching by 1 structure & detected and no where else return the correct in classical mode
Verify that query for detected in "A", Not detected in "B", where "A" and "B" are in different anatomical systems
       in classical mode
Verify that wild type results(broad definition) are excluded in classical mode.(assays which are not associated with any allele pairs,
        or In Situ reporter(knock-in) assays associated with a single allele pair which is heterozygous wild type for the assayed gene)
Verify that query for detected in "A", Not detected in "B", where "A" and "B" are in different anatomical systems in classical mode
Verify that query for detected in "A", Not detected in "B", where "A" is a parent of "B" in the same anatomical system in classical mode
Verify that query for detected in "A", Not detected in "B", where "A" is a parent of "B" in the same anatomical system in RNA-Seq mode
Verify that query for detected in "A", Not detected in "B", Not detected in "C" in classical mode
Verify that query for detected in "A", detected in  "B", Not detected in "c" in classical mode
Verify that query for detected in "A", detected in  "B", Not detected in "c", Not detected in "d" in RNA-Seq mode
verify that query for detected in "A", Not detected in "B", where a gene has both "expressed" and "not expressed" results for "A"
        and has no results and/or "not expressed" results for "B" should return the gene in classical mode

"""
import os.path
import sys
import time
import tracemalloc
import unittest
import config

from util import iterate
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../..', )
)

# Tests
tracemalloc.start()


class TestGxdProfileQF(unittest.TestCase):

    def setUp(self):
        browser = getattr(config, "BROWSER", "chrome").lower()
        if browser == "chrome":
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "firefox":
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == "edge":
            self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        self.driver.set_window_size(1500, 1000)

    def test_prof_single_results(self):
        """
        @status: Tests that searching by a single anatomical structure & detected return the correct classical results
        @note: GXD-Profile-1 CRM-82
        @attention: the time sleeps need to be replaced by expected conditions code. passed 11/14/2024
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/profile')
        # Click the Classical Assays option
        self.driver.find_element(By.ID, 'profileModeC').click()
        self.driver.find_element(By.ID, 'detectedRadio0').is_selected()
        struct1 = self.driver.find_element(By.ID, 'profileStructure0')
        # Enter your structure
        struct1.send_keys("molar root")
        time.sleep(2)
        struct1.send_keys(Keys.RETURN)
        struct1.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.ID, 'resultstab').click()
        time.sleep(2)
        # locates the structure column and lists the structures found
        structurelist = self.driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = structurelist.find_elements(By.CLASS_NAME, 'yui-dt-col-structure')
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        # assert that this gene is not returned since it is associated to a normal phenotype
        self.assertIn('TS28: molar root', searchtextitems, 'TS28: tongue anterior part is not being returned!')

    def test_prof_single_results_rna(self):
        """
        @status: Tests that searching by a single anatomical structure & detected return the correct RNA-Seq results
        @note: GXD-Profile-1 CRM-82
        @attention: the time sleeps need to be replaced by expected conditions code. passed 11/26/2024
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/profile')
        # Click the RNA-Seq option
        self.driver.find_element(By.ID, 'profileModeR').click()
        self.driver.find_element(By.ID, 'detectedRadio0').is_selected()
        struct1 = self.driver.find_element(By.ID, 'profileStructure0')
        # Enter your structure
        struct1.send_keys("heart ventricle")
        time.sleep(2)
        struct1.send_keys(Keys.RETURN)
        struct1.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.ID, 'stagegridtab').click()
        time.sleep(2)
        # find the ts grid box for TS26 for heart ventricle
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col0 > rect.blue5')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue5')
        # find the ts grid box for TS27 for heart ventricle
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col1 > rect.blue5')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue5')
        # find the ts grid box for TS28 for heart ventricle
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col2 > rect.blue5')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue5')


    def test_prof_double_results(self):
        """
        @status: Tests that searching by two anatomical structures & detected return the correct classical results
        @note: GXD-Profile-2 CRM-82
        @attention: the time sleeps need to be replaced by expected conditions code. Passed 11/14/2024
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/profile')
        # Click the Classical Assays option
        self.driver.find_element(By.ID, 'profileModeC').click()
        self.driver.find_element(By.ID, 'detectedRadio0').is_selected()
        struct1 = self.driver.find_element(By.ID, 'profileStructure0')
        # Enter your structure
        struct1.send_keys("tooth root")
        time.sleep(2)
        struct1.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'detectedRadio1').click()
        struct2 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct2.send_keys("molar root")
        time.sleep(2)
        struct2.send_keys(Keys.RETURN)
        struct2.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.ID, 'resultstab').click()
        time.sleep(2)
        # locates the structure column and lists the structures found
        structurelist = self.driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = structurelist.find_elements(By.CLASS_NAME, 'yui-dt-col-structure')
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        # assert that this gene is not returned since it is associated to a normal phenotype
        self.assertIn('TS28: molar root', searchtextitems, 'TS28: tongue anterior part is not being returned!')

    def test_prof_double_results_rna(self):
        """
        @status: Tests that searching by two anatomical structures & detected return the correct RNA-Seq results
        @note: GXD-Profile-2 CRM-82
        @attention: the time sleeps need to be replaced by expected conditions code. passed 11/26/2024
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/profile')
        #driver.get(config.TEST_URL + '/gxd')
        # Click the RNA-Seq option
        self.driver.find_element(By.ID, 'profileModeR').click()
        self.driver.find_element(By.ID, 'detectedRadio0').is_selected()
        struct1 = self.driver.find_element(By.ID, 'profileStructure0')
        # Enter your structure
        struct1.send_keys("leg mu")
        time.sleep(1)
        auto_list = self.driver.find_element(By.CLASS_NAME, "yui-ac-bd").find_element(By.TAG_NAME, 'ul')
        items = auto_list.find_elements(By.TAG_NAME, "li")
        for item in items:
            text = item.text
            print(text)
        time.sleep(2)
        struct1.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'detectedRadio1').click()
        # Enter your structure
        struct2 = self.driver.find_element(By.ID, 'profileStructure1')
        struct2.send_keys("triceps su")
        time.sleep(2)
        struct2.send_keys(Keys.RETURN)
        struct2.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.ID, 'stagegridtab').click()
        time.sleep(2)
        # find the ts grid box for TS28 for femur diaphysis
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col0 > rect.blue5')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue3
        self.assertEqual(rightclass, 'blue5')
        # find the ts grid box for TS28 for femur metaphysis
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row1.col0 > rect.blue5')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue3
        self.assertEqual(rightclass, 'blue5')

    def test_profile_nowhereelse(self):
        """
        @status: Tests that searching by 1 structure & detected and no where else return the correct classical results
        @note: GXD-Profile-3 CRM-82
        @attention: the time sleeps need to be replaced by expected conditions code. Passed 11/14/2024
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/profile')
        #driver.get(config.TEST_URL + '/gxd')
        # Click the Classical Assays option
        self.driver.find_element(By.ID, 'profileModeC').click()
        self.driver.find_element(By.ID, 'detectedRadio0').is_selected()
        struct1 = self.driver.find_element(By.ID, 'profileStructure0')
        # Enter your structure
        struct1.send_keys("blood island")
        time.sleep(2)
        struct1.send_keys(Keys.RETURN)
        struct1.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.ID, 'profileNowhereElseCheckbox').is_selected()
        time.sleep(2)
        self.driver.find_element(By.ID, 'resultstab').click()
        time.sleep(2)
        # locates the structure column and lists the structures found
        structurelist = self.driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = structurelist.find_elements(By.CLASS_NAME, 'yui-dt-col-structure')
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        # assert that this gene is not returned since it is associated to a normal phenotype
        self.assertIn('TS13: blood island', searchtextitems, 'TS13: blood island is not being returned!')

    def test_profile_D_notD_systems(self):
        """
        @status: Tests that query for detected in "A", Not detected in "B", where "A" and "B" are in different anatomical systems for classical results
        @note: GXD-Profile-4 CRM-82
        @attention: the time sleeps need to be replaced by expected conditions code!! passed 11/14/2024
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/profile')
        #driver.get(config.TEST_URL + '/gxd')
        # Click the Classical Assays option
        self.driver.find_element(By.ID, 'profileModeC').click()
        self.driver.find_element(By.ID, 'detectedRadio0').is_selected()
        struct1 = self.driver.find_element(By.ID, 'profileStructure0')
        # Enter your structure
        struct1.send_keys("tongue anterior part")
        time.sleep(2)
        struct1.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'notdetectedRadio1').click()
        struct2 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct2.send_keys("tongue extrinsic muscle TS22-28")
        time.sleep(2)
        struct2.send_keys(Keys.RETURN)
        #struct2.send_keys(Keys.ENTER)
        time.sleep(2)
        # find and click the assay results tab
        self.driver.find_element(By.ID, 'resultstab').click()
        time.sleep(2)
        # locates the structure column and lists the structures found
        structurelist = self.driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = structurelist.find_elements(By.CLASS_NAME, 'yui-dt-col-structure')
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        # assert that this gene is not returned since it is associated to a normal phenotype
        self.assertIn('TS28: tongue anterior part', searchtextitems,
                      'TS28: tongue anterior part is not being returned!')
        # assert that this gene is not returned since it has no expression annotations
        self.assertNotIn('TS23: tongue extrinsic muscle', searchtextitems,
                         'TS23: tongue extrinsic muscle is being returned!')

    """def test_profile_all_no(self):
        
        @status: Tests that searching by 3 not detected structures return the correct results
        @note: GXD-Profile-5 Test no longer valid! 6/28/2023
        
        driver = self.driver
        #driver.get(config.TEST_URL + '/gxd/profile')
        driver.get(config.TEST_URL + '/gxd')
        self.driver.find_element(By.CSS_SELECTOR, '#expressionSearch > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1) > em:nth-child(1)').click()
        #time.sleep(2)
        struct1 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct1.send_keys("???")
        time.sleep(2)
        self.driver.find_element(By.ID, 'profileDetected1').is_selected()
        struct1.send_keys(Keys.RETURN)
        time.sleep(2)
        struct2 = self.driver.find_element(By.ID, 'profileStructure2')
        # Enter your structure
        struct2.send_keys("???")
        time.sleep(2)
        self.driver.find_element(By.ID, 'profileNotDetected2').click()
        struct2.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'resultstab').click()
        time.sleep(2)
        #locates the structure column and lists the structures found
        structurelist = self.driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = structurelist.find_elements(By.CLASS_NAME, 'yui-dt-col-structure')
        searchTextItems = iterate.getTextAsList(items)        
        print(searchTextItems)
        #assert that this gene is not returned since it is associated to a normal phenotype
        self.assertIn('TS28: tongue anterior part', searchTextItems, 'TS28: tongue anterior part is not being returned!')   
        #assert that this gene is not returned since it has no expression annotations
        self.assertNotIn('TS23: tongue extrinsic muscle', searchTextItems, 'TS23: tongue extrinsic muscle is being returned!') 
     """
    def test_diff_wt_results(self):
        """
        @status: Tests that wild type results(broad definition) are excluded in classical results.(assays which are not associated with any allele pairs,
        or In Situ reporter(knock-in) assays associated with a single allele pair which is heterozygous wild type for the assayed gene)
        @note: GXD-Diff-2 passed 11/19/2024
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/profile')
        # Click the RNA-Seq option
        self.driver.find_element(By.ID, 'profileModeC').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'detectedRadio0').is_selected()
        struct1 = self.driver.find_element(By.ID, 'profileStructure0')
        # Enter your structure
        struct1.send_keys("bladder")
        time.sleep(2)
        struct1.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'notdetectedRadio1').click()
        struct2 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct2.send_keys("adventitia of bladder")
        time.sleep(2)
        struct2.send_keys(Keys.RETURN)
        struct2.send_keys(Keys.ENTER)
        time.sleep(2)
        #self.driver.find_element(By.ID, 'genegridtab')
        #time.sleep(2)
        #self.driver.find_element(By.ID, 'genegridtab')
        # find the Genes column
        self.driver.find_element(By.ID, 'colGroup')
        genelist = driver.find_element(By.ID, 'colGroupInner')
        items = genelist.find_elements(By.TAG_NAME, "text")
        searchtextitems = iterate.getTextAsList(items)
        # print(searchtextitems)
        self.assertIn('Abcc6', searchtextitems)
        self.assertIn('Acaa2', searchtextitems)
        # find the tissue grid box for bladder for marker Abcc6
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col17 > rect.blue2')
        rightclass = item.get_attribute('class')
        # now we assert the class name of the gridbox matches the class name of blue2
        self.assertEqual(rightclass, 'blue2')
        # find the Anatomical Systems column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchtextitems = iterate.getTextAsList(items)
        # print(searchTextItems)
        # Now assert that these 2 systems are returned in the first column of the grid
        self.assertIn('bladder', searchtextitems)
        self.assertIn('adventitia of bladder', searchtextitems)

    def test_diff_systems(self):
        """
        @status: Tests that query for detected in "A", Not detected in "B", where "A" and "B" are in different anatomical systems for classical results
        @note: GXD-Diff-3(partial test)
        @attention: the time sleeps need to be replaced by expected conditions code. passed 11/19/2024
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/profile')
        # Click the Classical Assays option
        self.driver.find_element(By.ID, 'profileModeC').click()
        self.driver.find_element(By.ID, 'detectedRadio0').is_selected()
        struct1 = self.driver.find_element(By.ID, 'profileStructure0')
        # Enter your structure
        struct1.send_keys("pulmonary valve")
        time.sleep(2)
        struct1.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'notdetectedRadio1').click()
        struct2 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct2.send_keys("aortic valve")
        time.sleep(2)
        struct2.send_keys(Keys.RETURN)
        struct2.send_keys(Keys.ENTER)
        time.sleep(2)
        # find the results table
        self.driver.find_element(By.ID, 'genegridtab').click()
        time.sleep(2)
        # locates the gene column and lists the structures found
        # find the Genes column
        self.driver.find_element(By.ID, 'colGroup')
        genelist = driver.find_element(By.ID, 'colGroupInner')
        items = genelist.find_elements(By.TAG_NAME, "text")
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        # assert the correct genes are returned
        self.assertIn('Bmp2', searchtextitems)
        self.assertIn('Col11a1', searchtextitems)
        self.assertIn('Crip2', searchtextitems)
        self.assertIn('Evc', searchtextitems)
        self.assertIn('Evc2', searchtextitems)
        self.assertIn('Foxc2', searchtextitems)
        self.assertIn('Hand1', searchtextitems)
        self.assertIn('Hapln1', searchtextitems)
        self.assertIn('Itga6', searchtextitems)
        self.assertIn('Matr3', searchtextitems)
        self.assertIn('Mki67', searchtextitems)
        self.assertIn('Notch2', searchtextitems)
        # click the tissue by gene tab
        # find the tissue grid box for bladder for marker Matr3
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col9 > rect.blue1')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue1')
        # find the Anatomical Systems column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        # Now assert that only this system is returned in the grid
        self.assertIn('pulmonary valve', searchtextitems)

    def test_same_parent(self):
        """
        @status: Tests that query for detected in "A", Not detected in "B", where "A" is a parent of "B" in the same anatomical system for classical results
        @note: GXD-Diff-4(partial test) passed 11/19/2024
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/profile')
        # Click the Classical Assays option
        self.driver.find_element(By.ID, 'profileModeC').click()
        self.driver.find_element(By.ID, 'detectedRadio0').is_selected()
        struct1 = self.driver.find_element(By.ID, 'profileStructure0')
        # Enter your structure
        struct1.send_keys("pulmonary valve")
        time.sleep(2)
        struct1.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'notdetectedRadio1').click()
        struct2 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct2.send_keys("pulmonary valve leaflet")
        time.sleep(2)
        struct2.send_keys(Keys.RETURN)
        struct2.send_keys(Keys.ENTER)
        time.sleep(2)
        # find the results table
        self.driver.find_element(By.ID, 'genegridtab').click()
        time.sleep(2)
        # find the Genes column
        self.driver.find_element(By.ID, 'colGroup')
        genelist = driver.find_element(By.ID, 'colGroupInner')
        items = genelist.find_elements(By.TAG_NAME, "text")
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        # self.assertIn('Adgrb2', searchTextItems)
        self.assertIn('Acta2', searchtextitems)
        self.assertIn('Casp3', searchtextitems)
        self.assertIn('Col11a1', searchtextitems)
        self.assertIn('Crip2', searchtextitems)
        self.assertIn('Evc', searchtextitems)
        self.assertIn('Evc2', searchtextitems)
        self.assertIn('Foxc2', searchtextitems)
        self.assertIn('Gnb4', searchtextitems)
        self.assertIn('Hand1', searchtextitems)
        self.assertIn('Itga6', searchtextitems)
        self.assertIn('Itgb1', searchtextitems)
        self.assertIn('Mki67', searchtextitems)
        self.assertIn('Mxra8', searchtextitems)
        self.assertIn('Npas3', searchtextitems)
        self.assertIn('Postn', searchtextitems)
        self.assertIn('Tnmd', searchtextitems)

        # find the tissue grid box for bladder for marker Agtr2
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col12 > rect.blue1')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue1')
        # find the Anatomical Systems column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        # Now assert that only this system is returned in the grid
        self.assertIn('pulmonary valve', searchtextitems)

    def test_same_parent_rna(self):
        """
        @status: Tests that query for detected in "A", Not detected in "B", where "A" is a parent of "B" in the same anatomical system for RNA-Seq results
        @note: GXD-Diff-4(partial test) passed 11/26/2024
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/profile')
        # Click the RNA-Seq option
        self.driver.find_element(By.ID, 'profileModeR').click()
        self.driver.find_element(By.ID, 'detectedRadio0').is_selected()
        struct1 = self.driver.find_element(By.ID, 'profileStructure0')
        # Enter your structure
        struct1.send_keys("femur dia")
        time.sleep(2)
        auto_list = self.driver.find_element(By.CLASS_NAME, "yui-ac-bd").find_element(By.TAG_NAME, 'ul')
        items = auto_list.find_elements(By.TAG_NAME, "li")
        for item in items:
            text = item.text
            print(text)
        time.sleep(2)
        struct1.send_keys(Keys.RETURN)
        #struct1.send_keys(Keys.TAB)
        time.sleep(2)
        self.driver.find_element(By.ID, 'notdetectedRadio1').click()
        struct2 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct2.send_keys("femur meta")
        time.sleep(2)
        struct2.send_keys(Keys.RETURN)
        struct2.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.ID, 'stagegridtab').click()
        time.sleep(2)
        # find the ts grid box for TS28 for femur diaphysis
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col0 > rect.blue4')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue4
        self.assertEqual(rightclass, 'blue4')
        # find the ts grid box for TS28 for femur metaphysis
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row1.col0 > rect.red4')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of red4
        self.assertEqual(rightclass, 'red4')


    def test_multi_nots(self):
        """
        @status: Tests that query for detected in "A", Not detected in "B", Not detected in "C" in classical results
        @note: GXD-Diff-4(partial test) Passed 11/19/2024
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/profile')
        # Click the Classical Expression option
        self.driver.find_element(By.ID, 'profileModeC').click()
        self.driver.find_element(By.ID, 'detectedRadio0').is_selected()
        struct1 = self.driver.find_element(By.ID, 'profileStructure0')
        # Enter your structure
        struct1.send_keys("hair")
        time.sleep(2)
        struct1.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'notdetectedRadio1').click()
        struct2 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct2.send_keys("hair follicle")
        time.sleep(2)
        struct2.send_keys(Keys.RETURN)
        self.driver.find_element(By.ID, 'notdetectedRadio2').click()
        struct2 = self.driver.find_element(By.ID, 'profileStructure2')
        # Enter your structure
        struct2.send_keys("hair follicle isthmus")
        time.sleep(2)
        struct2.send_keys(Keys.RETURN)
        struct2.send_keys(Keys.ENTER)
        time.sleep(2)
        # find the results table
        #self.driver.find_element(By.ID, 'resultstab').click()
        self.driver.find_element(By.ID, 'genegridtab').click()
        time.sleep(2)
        # find the Genes column
        self.driver.find_element(By.ID, 'colGroup')
        genelist = driver.find_element(By.ID, 'colGroupInner')
        items = genelist.find_elements(By.TAG_NAME, "text")
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        # self.assertIn('Adgrb2', searchTextItems)
        self.assertIn('Alk', searchtextitems)
        self.assertIn('Ceacam1', searchtextitems)
        self.assertIn('Frat2', searchtextitems)
        self.assertIn('Krt32', searchtextitems)
        self.assertIn('Krt82', searchtextitems)
        self.assertIn('Krt86', searchtextitems)
        self.assertIn('Naa20', searchtextitems)
        self.assertIn('Naa25', searchtextitems)
        self.assertIn('Pcdh19', searchtextitems)
        self.assertIn('Pcx', searchtextitems)
        self.assertIn('Pde11a', searchtextitems)
        self.assertIn('Rufy3', searchtextitems)

        # find the tissue grid box for hair follicle for marker Ceacam1
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.row1:nth-child(13) > rect.red2')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'red2')
        # find the Anatomical Systems column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        # Now assert that only this system is returned in the grid
        self.assertIn('hair follicle', searchtextitems)

    def test_multi_detect_multi_nots(self):
        """
        @status: Tests that query for detected in "A", detected in  "B", Not detected in "c" in classical results
        @note: GXD-Diff-4(partial test) this test is unstable sometimes selecting the wrong  auto select  for  the first term!
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/profile')
        # Click the Classical Assays option
        self.driver.find_element(By.ID, 'profileModeC').click()
        # click add structure button
        self.driver.find_element(By.ID, 'addDetected').click()
        self.driver.find_element(By.ID, 'detectedRadio0').is_selected()
        struct1 = self.driver.find_element(By.ID, 'profileStructure0')
        # Enter your structure
        struct1.send_keys("1st branchial")
        time.sleep(2)
        struct1.send_keys(Keys.RETURN)
        self.driver.find_element(By.ID, 'detectedRadio1').click()
        struct2 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct2.send_keys("cerebral cortex")
        time.sleep(2)
        struct2.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'notdetectedRadio2').click()
        struct3 = self.driver.find_element(By.ID, 'profileStructure2')
        # Enter your structure
        struct3.send_keys("white fat")
        time.sleep(2)
        struct3.send_keys(Keys.RETURN)
        self.driver.find_element(By.ID, 'notdetectedRadio3').click()
        struct4 = self.driver.find_element(By.ID, 'profileStructure3')
        # Enter your structure
        struct4.send_keys("yolk sac")
        time.sleep(2)
        struct4.send_keys(Keys.RETURN)
        struct4.send_keys(Keys.ENTER)
        time.sleep(2)
        # find the results table
        #self.driver.find_element(By.ID, 'resultstab').click()
        self.driver.find_element(By.ID, 'genegridtab').click()
        time.sleep(2)
        # find the Genes column
        self.driver.find_element(By.ID, 'colGroup')
        genelist = driver.find_element(By.ID, 'colGroupInner')
        items = genelist.find_elements(By.TAG_NAME, "text")
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        self.assertIn('Frzb', searchtextitems)

        # find the tissue grid box for intestine wall for marker Pygl
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col20 > rect.blue1')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue1')
        # find the tissue grid box for large intestine for marker Mybph
        boxlist1 = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item1 = boxlist1.find_element(By.CSS_SELECTOR, 'g.cell.row2.col20 > rect.red1')
        rightclass = item1.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'red1')
        # find the Anatomical Systems column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        # Now assert that only these systems are returned in the grid
        self.assertIn('white fat', searchtextitems)

    def test_multi_detect_multi_nots_RNA(self):
        """
        @status: Tests that query for detected in "A", detected in  "B", Not detected in "c", Not detected in "d"
        using the RNA-Seq option
        @note: GXD-Diff-4(partial test) passed 11/26/2024
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/profile')
        # Click the RNA-Seq option
        self.driver.find_element(By.ID, 'profileModeR').click()
        # click add structure button
        self.driver.find_element(By.ID, 'addDetected').click()
        self.driver.find_element(By.ID, 'detectedRadio0').is_selected()
        struct1 = self.driver.find_element(By.ID, 'profileStructure0')
        # Enter your structure
        struct1.send_keys("intestine wall")
        time.sleep(2)
        struct1.send_keys(Keys.RETURN)
        self.driver.find_element(By.ID, 'detectedRadio1').click()
        struct2 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct2.send_keys("brown fat")
        time.sleep(2)
        struct2.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'notdetectedRadio2').click()
        struct3 = self.driver.find_element(By.ID, 'profileStructure2')
        # Enter your structure
        struct3.send_keys("large intestine")
        time.sleep(2)
        struct3.send_keys(Keys.RETURN)
        self.driver.find_element(By.ID, 'notdetectedRadio3').click()
        struct4 = self.driver.find_element(By.ID, 'profileStructure3')
        # Enter your structure
        struct4.send_keys("small intestine")
        time.sleep(2)
        struct4.send_keys(Keys.RETURN)
        struct4.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.ID, 'stagegridtab').click()
        time.sleep(2)
        # find the ts grid box for TS28 for intestine wall
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col1 > rect.blue3')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue3
        self.assertEqual(rightclass, 'blue3')
        # find the ts grid box for TS28 for brown fat
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row1.col1 > rect.blue3')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue3
        self.assertEqual(rightclass, 'blue3')
        # find the ts grid box for TS22 for large intestine
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row2.col0 > rect.red3')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of red3
        self.assertEqual(rightclass, 'red3')
        # find the ts grid box for TS28 for small intestine
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row3.col1 > rect.red3')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of red3
        self.assertEqual(rightclass, 'red3')


    def test_diff_exp_notexp(self):
        """
        @status: Tests that query for detected in "A", Not detected in "B", where a gene has both "expressed" and "not expressed" results for "A"
        and has no results and/or "not expressed" results for "B" should return the gene in classical mode.
        @note: GXD-Diff-6
        @attention:  This test needs to be fixed once we go to lucene indexing OR find an example with less results!!
        passed 11/22/2024
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/profile')
        # Click the Classical Assays option
        self.driver.find_element(By.ID, 'profileModeC').click()
        self.driver.find_element(By.ID, 'detectedRadio0').is_selected()
        struct1 = self.driver.find_element(By.ID, 'profileStructure0')
        # Enter your structure
        struct1.send_keys("liver")
        time.sleep(2)
        struct1.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element(By.ID, 'notdetectedRadio1').click()
        struct2 = self.driver.find_element(By.ID, 'profileStructure1')
        # Enter your structure
        struct2.send_keys("spleen")
        time.sleep(2)
        struct2.send_keys(Keys.RETURN)
        struct2.send_keys(Keys.ENTER)
        time.sleep(2)
        # find the results table
        self.driver.find_element(By.ID, 'genegridtab').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'genegridtab')
        time.sleep(5)
        # find the Genes column
        self.driver.find_element(By.ID, 'colGroup')
        genelist = driver.find_element(By.ID, 'colGroupInner')
        items = genelist.find_elements(By.TAG_NAME, "text")
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        self.assertIn('A2m', searchtextitems)
        self.assertIn('Aard', searchtextitems)
        self.assertIn('Abca1', searchtextitems)
        # self.assertIn('Bckdk', searchTextItems)
        # self.assertIn('Pkm', searchTextItems)
        # find the tissue grid box for liver for marker A2m
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col19 > rect')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue1')
        # find the Anatomical Systems column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        # Now assert that both systems are returned in the grid
        self.assertIn('liver', searchtextitems)
        self.assertIn('spleen', searchtextitems)



    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxdProfileQF))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\\WebdriverTests'))
