"""
Created on Jan 23, 2025
@author: jeffc
Verify parent data is correctly identified
Verify tree view smart alpha sort order
Verify search by CL term that has multiple parents
Verify search by CL term associated with multiple phenotypes
Verify search by EmapA term associated to a single phenotype
Verify search by  EmapA term associated to phenotype but NO expression
Verify the phenotype link treeview returns correct results
Verify 1to1 mapping with NO child terms phenotype link
Verify 1to1 mapping with child terms phenotype link
Verify 1to1 mapping with NO phenotype link but an expression link
Verify 1to1 NO mapping for expression or phenotype
Verify 1to1 NO mapping for expression or phenotype but has children
Verify 1toN mapping with parents and 3 phenotype children
Verify 1toN mapping with parents and expression children
Verify NO phenotype mapping, zero expression, NO children
Verify NO phenotype mapping, has expression mapping, NO children
Verify NO phenotype mapping, NO expression mapping, NO children
Verify the phenotype term link results are alphanumeric sorted
"""
import os.path
import sys
import time
import tracemalloc
import unittest
import config

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from util import wait, iterate
from util.table import Table

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../', )
)

# Tests
tracemalloc.start()


class TestCellTypeBrowser(unittest.TestCase):

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

    def test_parentterm_data(self):
        """
        @status: Tests that the parent terms are correctly identified
        In this case all 3 parent terms should be is-a
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0000540")
        # identifies the table tags that contain parent terms
        parent = driver.find_element(By.ID, 'termPaneDetails').find_elements(By.TAG_NAME, 'td')
        if WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.ID, 'termPaneDetails'))):
            print('Term details loaded')
        print(parent[3].text)
        # verifies that the returned part terms are correct
        self.assertEqual(parent[3].text, "is-a electrically responsive cell\nis-a electrically signaling cell\nis-a neural cell")

    def test_default_sort_treeview(self):
        """
        @status: Tests that the terms are correctly sorted
        The default sort for the tree view is smart alpha
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology")
        time.sleep(2)
        term = driver.find_element(By.ID, 'treeViewContainer').find_elements(By.CLASS_NAME, 'jstree-anchor')
        print(term[1].text)
        print(term[32].text)
        if WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, 'jstree-children'))):
            print('Tree view details loaded')
        # extra embryonic component should not be 2nd item in list
        self.assertEqual(term[0].text, 'cell')
        self.assertEqual(term[1].text, 'abnormal cell')
        self.assertEqual(term[2].text, 'anucleate cell')
        self.assertEqual(term[3].text, 'apoptosis fated cell')
        self.assertEqual(term[4].text, 'cell in vitro')
        self.assertEqual(term[5].text, 'contractile cell')
        self.assertEqual(term[6].text, 'diploid cell')
        self.assertEqual(term[7].text, 'electrically active cell')
        self.assertEqual(term[8].text, 'embryonic cell (metazoa)')
        self.assertEqual(term[9].text, 'eukaryotic cell')
        self.assertEqual(term[10].text, 'excretory cell')
        self.assertEqual(term[11].text, 'foam cell')
        self.assertEqual(term[12].text, 'gamete-nursing cell')
        self.assertEqual(term[13].text, 'germ line cell')
        self.assertEqual(term[14].text, 'haploid cell')
        self.assertEqual(term[15].text, 'hematopoietic cell')
        self.assertEqual(term[16].text, 'inflammatory cell')
        self.assertEqual(term[17].text, 'mitogenic signaling cell')
        self.assertEqual(term[18].text, 'motile cell')
        self.assertEqual(term[19].text, 'nitrogen fixing cell')
        self.assertEqual(term[20].text, 'nucleate cell')
        self.assertEqual(term[21].text, 'oxygen accumulating cell')
        self.assertEqual(term[22].text, 'perivascular cell')
        self.assertEqual(term[23].text, 'photosynthetic cell')
        self.assertEqual(term[24].text, 'polyploid cell')
        self.assertEqual(term[25].text, 'precursor cell')
        self.assertEqual(term[26].text, 'prokaryotic cell')
        self.assertEqual(term[27].text, 'secretory cell')
        self.assertEqual(term[28].text, 'skeletogenic cell')
        self.assertEqual(term[29].text, 'structural cell')
        self.assertEqual(term[30].text, 'stuff accumulating cell')
        self.assertEqual(term[31].text, 'supporting cell')
        self.assertEqual(term[32].text, 'zygote')


    def test_parents_multi(self):
        """
        @status: Tests that searching by a cell ontology term that is associated with multiple parents return the
        correct results
        @note: CT-Search-?
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0000136")
        # identifies the table tags that contain parent terms
        parent = driver.find_element(By.ID, 'termPaneDetails').find_elements(By.TAG_NAME, 'td')
        if WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.ID, 'termPaneDetails'))):
            print('Term details loaded')
        print(parent[3].text)
        # verifies that the returned part terms are correct
        self.assertEqual(parent[3].text,
                         "is-a connective tissue cell\nis-a stuff accumulating cell")

    def test_single_term(self):
        """
        @status: Tests that searching by a cell ontology term that is associated with a single term returns the
        correct results
        @note: CL-Search-?
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0000448")
        time.sleep(2)
        term = driver.find_element(By.ID, 'treeViewContainer').find_elements(By.CLASS_NAME, 'jstree-anchor')
        print(term[0].text)
        print(term[9].text)
        print(term[19].text)
        print(term[20].text)
        print(term[25].text)
        print(term[29].text)
        if WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, 'jstree-children'))):
            print('Tree view details loaded')
        # the first component should always be "cell" and the last 32 should be white adipocyte
        self.assertEqual(term[0].text, 'cell')
        self.assertEqual(term[29].text, 'white adipocyte')

    def test_pheno_link_noexpression(self):
        """
        @status: Tests that searching by an Emapa term that is associated to a phenotype but has no expression
        annotations  !!!under construction, waiting for implementation!!!!!!
        @note: CL_Search-
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology")
        driver.find_element(By.LINK_TEXT, 'phenotype terms').click()
        searchlist = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchlist)
        print([x.text for x in searchlist])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('MP Annotation summary loaded')
        # These 2 terms should be returned in the phenotype search results
        self.assertIn('abnormal blastocoele morphology\nabsent blastocoele', terms, 'these terms are not listed!')

    def test_pheno_link_treeview(self):
        """
        @status: Tests that the phenotype annotations link in the Treeview section when clicked returns correct results.
        @note:  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'phenotypeAnnotationCount'))):
            print('Tree view details loaded')
        driver.find_element(By.CLASS_NAME,
                            'phenotypeAnnotationCount').click()  # clicks the phenotype annotations link found in the Treeview section
        time.sleep(2)
        results_table = self.driver.find_element(By.ID, 'resultsTable')
        table = Table(results_table)
        # gets the 1st,6th,13th,16th rows of the Annotated term column
        term1 = table.get_cell(3, 1)
        term2 = table.get_cell(8, 1)
        term3 = table.get_cell(16, 1)
        term4 = table.get_cell(19, 1)
        print(term1.text)
        print(term2.text)
        print(term3.text)
        print(term4.text)
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'resultsTable'))):
            print('MP Annotation summary loaded')
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('abnormal cerebellum deep nucleus morphology', term1.text, 'Term1 is not returning')
        self.assertEqual('abnormal cerebellum fastigial nucleus morphology', term2.text, 'Term2 is not returning')
        self.assertEqual('abnormal cerebellum dentate nucleus morphology', term3.text, 'Term3 is not returning')
        self.assertEqual('abnormal cerebellum interpositus nucleus morphology', term4.text, 'Term4 is not returning')

    def test_pheno_link_nochild_treeview(self):
        """
        @status: Tests that when you have a 1to1 mapping with no child terms associated(gxd&pheno),the phenotype
        annotations link in the Treeview section when clicked returns correct results.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'phenotypeAnnotationCount'))):
            print('Tree view details loaded')
        driver.find_element(By.CLASS_NAME,
                            'phenotypeAnnotationCount').click()  # clicks the phenotype annotations link found in the Treeview section
        results_table = self.driver.find_element(By.ID, 'resultsTable')
        table = Table(results_table)
        # gets the 1st and only row of the Annotated term column
        term1 = table.get_cell(3, 1)
        print(term1.text)
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'resultsTable'))):
            print('MP Annotation summary loaded')
        # verifies the returned terms are the correct terms for this search
        self.assertEqual("abnormal Peyer's patch epithelium morphology", term1.text, 'Term1 is not returning')

    def test_pheno_link_withchildboth_treeview(self):
        """
        @status: Tests that when you have a 1to1 mapping with child terms associated(gxd&pheno),the phenotype
        annotations link in the Treeview section when clicked returns correct results.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'phenotypeAnnotationCount'))):
            print('Tree view details loaded')
        driver.find_element(By.CLASS_NAME,
                            'phenotypeAnnotationCount').click()  # clicks the phenotype annotations link found in the Treeview section
        time.sleep(2)
        results_table = self.driver.find_element(By.ID, 'resultsTable')
        table = Table(results_table)
        # gets the 1st,2nd rows of the Annotated term column, only 2 rows exist
        term1 = table.get_cell(3, 1)
        term2 = table.get_cell(4, 1)
        print(term1.text)
        print(term2.text)
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'resultsTable'))):
            print('MP Annotation summary loaded')
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('abnormal bulbus cordis morphology', term1.text, 'Term1 is not returning')
        self.assertEqual('abnormal bulbus cordis morphology', term2.text, 'Term2 is not returning')

    def test_no_pheno_link_exp_link(self):
        """
        @status: Tests that when you have a 1to1 mapping with NO Pheno mapping/has GXD mapping,the GXD link has data
        the phenotype annotations link in the Treeview section has zero results.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        # the phenotype annotations link found in the Treeview section should be zero
        assert '0 phenotype annotations' in driver.page_source

    def test_zero_pheno_link_zero_exp_link(self):
        """
        @status: Tests that when you have a 1to1 NO mapping for expression or pheno, NO child terms, the phenotype
        annotations is zero and expression results links in the Treeview section is normal.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:37850")
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'ygtvchildren'))):
            print('Tree view details loaded')
        time.sleep(2)
        # verifies the returned results are zero for this search
        assert '(0 expression results; 0 phenotype annotations)' in driver.page_source

    def test_zero_pheno_link_zero_exp_link_MP_child(self):
        """
        @status: Tests that when you have a 1to1  NO mapping for expression or pheno, has child terms,the phenotype
        annotations is zero and expression results links in the Treeview section is normal.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:16824")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        linke = driver.find_element(By.CLASS_NAME,
                                    'expressionResultCount')  # the expression annotations link found in the Treeview section
        print(linke.text)
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('3', linke.text, 'The 0 expression results link is wrong')
        self.assertIn('0 phenotype annotations', driver.page_source,
                      'The 0 phenotypes annotation link is missing')  # confirms that o phenotype annitations text is displayed when no results

    def test_pheno_link_withparent3child_treeview(self):
        """
        @status: Tests that when you have a 1toN mapping with parent and 3 child terms associated(pheno)
        has child terms,the phenotype annotations link in the Treeview section when clicked returns correct results.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:28373")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        driver.find_element(By.CLASS_NAME,
                            'phenotypeAnnotationCount').click()  # clicks the phenotype annotations link found in the Treeview section
        time.sleep(2)
        results_table = self.driver.find_element(By.ID, 'resultsTable')
        table = Table(results_table)
        # gets the 1st-8th rows of the Annotated term column, only 8 rows exist
        term1 = table.get_cell(3, 1)
        term2 = table.get_cell(4, 1)
        term3 = table.get_cell(5, 1)
        term4 = table.get_cell(6, 1)
        term5 = table.get_cell(7, 1)
        term6 = table.get_cell(8, 1)
        term7 = table.get_cell(9, 1)
        term8 = table.get_cell(10, 1)
        print(term1.text)
        print(term2.text)
        print(term3.text)
        print(term4.text)
        print(term5.text)
        print(term6.text)
        print(term7.text)
        print(term8.text)
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('abnormal renal artery morphology', term1.text, 'Term1 is not returning')
        self.assertEqual('abnormal renal artery morphology', term2.text, 'Term2 is not returning')
        self.assertEqual('abnormal right renal artery morphology', term3.text, 'Term3 is not returning')
        self.assertEqual('abnormal right renal artery morphology', term4.text, 'Term4 is not returning')
        self.assertEqual('abnormal right renal artery morphology', term5.text, 'Term5 is not returning')
        self.assertEqual('abnormal right renal artery morphology', term6.text, 'Term6 is not returning')
        self.assertEqual('abnormal renal artery morphology', term7.text, 'Term7 is not returning')
        self.assertEqual('abnormal right renal artery morphology', term8.text, 'Term8 is not returning')

    def test_pheno_link_with_parent_and_child_treeview(self):
        """
        @status: Tests that when you have a 1toN mapping for pheno and expression, child terms for expression,
        the phenotype annotations link in the Treeview section when clicked returns correct results.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:16075")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        driver.find_element(By.CLASS_NAME,
                            'phenotypeAnnotationCount').click()  # clicks the phenotype annotations link found in the Treeview section
        time.sleep(2)
        results_table = self.driver.find_element(By.ID, 'resultsTable')
        table = Table(results_table)
        # gets the 1st, 2nd, 7th, 8th, and 9th rows of the Annotated term column
        term1 = table.get_cell(3, 1)
        term2 = table.get_cell(4, 1)
        term3 = table.get_cell(10, 1)
        term4 = table.get_cell(11, 1)
        term5 = table.get_cell(12, 1)
        print(term1.text)
        print(term2.text)
        print(term3.text)
        print(term4.text)
        print(term5.text)
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('absent primitive node', term1.text, 'Term1 is not returning')
        self.assertEqual('absent embryonic cilia', term2.text, 'Term2 is not returning')
        self.assertEqual('abnormal primitive node morphology', term3.text, 'Term3 is not returning')
        self.assertEqual('abnormal motile primary cilium morphology', term4.text, 'Term4 is not returning')
        self.assertEqual('decreased embryonic cilium length', term5.text, 'Term5 is not returning')

    def test_no_pheno_mapping_zero_exp_link(self):
        """
        @status: Tests that when you have no phenotype mapping but zero Expression mapping, NO child terms,
        the phenotype annotations link in the Treeview section does not display, the expression results link is zero.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:37425")
        wait.forAjax(driver)
        bodytext = driver.find_element(By.TAG_NAME, 'body').text
        # verifies the returned terms are the correct terms for this search
        self.assertTrue('0 expression results', 'The 0 expression results link is wrong')
        self.assertFalse('phenotype annotations' in bodytext)

    def test_no_pheno_mapping_has_exp_link(self):
        """
        @status: Tests that when you have no phenotype mapping but Expression mapping, NO child terms,the phenotype
        annotations link in the Treeview section does not display, the expression results link has normal display.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:36473")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        linke = driver.find_element(By.CLASS_NAME,
                                    'expressionResultCount')  # the expression annotations link found in the Treeview section
        bodytext = driver.find_element(By.TAG_NAME, 'body').text
        print(linke.text)
        # asserts the expression results link exist and phenotype annotations link does not exist
        self.assertTrue('expression results' in bodytext)
        self.assertFalse('phenotype annotations' in bodytext)

    def test_no_pheno_mapping_zero_exp_link2(self):
        """
        @status: Tests that when you have no phenotype mapping no Expression mapping, NO child terms,the phenotype
        annotations link in the Treeview section does not display, the expression results link has zero results.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:19101")
        wait.forAjax(driver)
        bodytext = driver.find_element(By.TAG_NAME, 'body').text
        # verifies the returned terms are the correct terms for this search
        self.assertTrue('0 expression results', 'The 0 expression results link is wrong')
        self.assertFalse('phenotype annotations' in bodytext)

    def test_pheno_link_results_sort(self):
        """
        @status: Tests that when you click the phenotypes term link in the detail section the results returned are
        in alphanumeric sort
        @note: CL-Search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:16117")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        driver.find_element(By.LINK_TEXT, 'phenotype terms').click()
        searchlist = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchlist)
        print([x.text for x in searchlist])
        print(terms)
        # These terms should be returned in the phenotype search results with the order given
        self.assertIn(
            'abnormal pharyngeal arch morphology\nabsent pharyngeal arches\nectopic pharyngeal arch\nenlarged pharyngeal arch\nfused pharyngeal arches\npharyngeal arch hypoplasia\nsmall pharyngeal arch',
            terms, 'The sort order is not correct')

    def test_ht_link_noexpression(self):
        """
        @status: Tests that searching by an CL term that is associated to a ht expression but has no regular expression
        annotations  tested 9/8/2025
        @note: CL_Search-
        """
        driver = self.driver
        # search for: double-positive, alpha-beta thymocyte
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0000809")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('Tree view details loaded')
        time.sleep(1)
        driver.find_element(By.ID,'htLink_CL:0000809').click()  # clicks the HT results link found in the Treeview section
        #time.sleep(2)
        # switch focus to the new tab for RNA-Seq and Microarray Experiment page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        items = self.driver.find_element(By.ID, 'pageReportTop')
        # verifies the number of results found is correct
        self.assertEqual('Showing experiments 1 - 18 of 18', items.text, 'number of results returned is not correct')


    def test_ht_link_treeview(self):
        """
        @status: Tests that the ht annotations link in the Treeview section when clicked returns correct results.
        @note:  tested 9/8/2025
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:2000053")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('Tree view details loaded')
        time.sleep(1)
        driver.find_element(By.ID,'htLink_CL:2000053').click()  # clicks the HT results link found in the Treeview section
        #time.sleep(2)
        # switch focus to the new tab for RNA-Seq and Microarray Experiment page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        items = self.driver.find_element(By.ID, 'pageReportTop')
        # verifies the number of results found is correct
        self.assertEqual('Showing experiments 1 - 2 of 2', items.text, 'number of results returned is not correct')


    def test_ht_link_nochild_treeview(self):
        """
        @status: Tests that when you have a 1to1 mapping with no child terms associated(gxd&ht&pheno),the phenotype
        annotations link in the Treeview section when clicked returns correct results.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'phenotypeAnnotationCount'))):
            print('Tree view details loaded')
        driver.find_element(By.CLASS_NAME,
                            'phenotypeAnnotationCount').click()  # clicks the phenotype annotations link found in the Treeview section
        results_table = self.driver.find_element(By.ID, 'resultsTable')
        table = Table(results_table)
        # gets the 1st and only row of the Annotated term column
        term1 = table.get_cell(3, 1)
        print(term1.text)
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'resultsTable'))):
            print('MP Annotation summary loaded')
        # verifies the returned terms are the correct terms for this search
        self.assertEqual("abnormal Peyer's patch epithelium morphology", term1.text, 'Term1 is not returning')

    def test_ht_link_withchildboth_treeview(self):
        """
        @status: Tests that when you have a 1to1 mapping with child terms associated(gxd&ht&pheno),the ht
        annotations link in the Treeview section when clicked returns correct results.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'phenotypeAnnotationCount'))):
            print('Tree view details loaded')
        driver.find_element(By.CLASS_NAME,
                            'phenotypeAnnotationCount').click()  # clicks the phenotype annotations link found in the Treeview section
        time.sleep(2)
        results_table = self.driver.find_element(By.ID, 'resultsTable')
        table = Table(results_table)
        # gets the 1st,2nd rows of the Annotated term column, only 2 rows exist
        term1 = table.get_cell(3, 1)
        term2 = table.get_cell(4, 1)
        print(term1.text)
        print(term2.text)
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'resultsTable'))):
            print('MP Annotation summary loaded')
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('abnormal bulbus cordis morphology', term1.text, 'Term1 is not returning')
        self.assertEqual('abnormal bulbus cordis morphology', term2.text, 'Term2 is not returning')

    def test_no_ht_link_exp_link(self):
        """
        @status: Tests that when you have a 1to1 mapping with NO ht annotations/has GXD mapping,the GXD link has data
        the ht annotations link in the Treeview section has zero results.
        @note: CL-search-?  tested 9/09/2025
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0000175")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('Tree view details loaded')
        time.sleep(1)
        # verify that there is no HT results link
        ht_link = driver.find_elements(By.ID, "htLink_CL:0000175")
        if len(ht_link) > 0:
            print(f"HT link exists!")
        else:
            print("HT link does not exist.")
        driver.find_element(By.PARTIAL_LINK_TEXT,'expression results').click()  # clicks the expression results link found in the Treeview section
        # switch focus to the new tab for gene expression page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        items = self.driver.find_element(By.ID, 'yui-pg1-0-page-report')
        # verifies the number of results found is correct
        self.assertEqual('Showing result(s) 1 - 4 of 4', items.text, 'number of results returned is not correct')

    def test_zero_ht_link_zero_exp_link(self):
        """
        @status: Tests that when you have a 1to1 NO mapping for expression or ht or pheno, NO child terms, the phenotype
        annotations is zero, ht annotations, and expression results links in the Treeview section is normal.
        @note: CL-search-?  !!!under construction, still needs the Phenotype link!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0009014")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('Tree view details loaded')
        time.sleep(1)
        # verify that there is no expression results link
        exp_link = driver.find_elements(By.PARTIAL_LINK_TEXT, "expression results")
        if len(exp_link) > 0:
            print(f"Expression link exists!")
        else:
            print("Expression link does not exist.")
        # verify that there is no HT results link
        ht_link = driver.find_elements(By.ID, "htLink_CL:0009014")
        if len(ht_link) > 0:
            print(f"HT link exists!")
        else:
            print("HT link does not exist.")
        # verify that there is no phenotype results link
        exp_link = driver.find_elements(By.PARTIAL_LINK_TEXT, "phenotype results")
        if len(exp_link) > 0:
            print(f"Phenotype link exists!")
        else:
            print("Phenotype link does not exist.")

    def test_zero_ht_link_zero_exp_link_MP_child(self):
        """
        @status: Tests that when you have a 1to1  NO mapping for expression or pheno, has child terms,the phenotype
        annotations is zero, the ht annotations is zero and expression results links in the Treeview section is normal.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:16824")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        linke = driver.find_element(By.CLASS_NAME,
                                    'expressionResultCount')  # the expression annotations link found in the Treeview section
        print(linke.text)
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('3', linke.text, 'The 0 expression results link is wrong')
        self.assertIn('0 phenotype annotations', driver.page_source,
                      'The 0 phenotypes annotation link is missing')  # confirms that o phenotype annitations text is displayed when no results

    def test_ht_link_withparent3child_treeview(self):
        """
        @status: Tests that when you have a 1toN mapping with parent and 3 child terms associated(ht)
        has child terms,the ht annotations link in the Treeview section when clicked returns correct results.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:28373")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        driver.find_element(By.CLASS_NAME,
                            'phenotypeAnnotationCount').click()  # clicks the phenotype annotations link found in the Treeview section
        time.sleep(2)
        results_table = self.driver.find_element(By.ID, 'resultsTable')
        table = Table(results_table)
        # gets the 1st-8th rows of the Annotated term column, only 8 rows exist
        term1 = table.get_cell(3, 1)
        term2 = table.get_cell(4, 1)
        term3 = table.get_cell(5, 1)
        term4 = table.get_cell(6, 1)
        term5 = table.get_cell(7, 1)
        term6 = table.get_cell(8, 1)
        term7 = table.get_cell(9, 1)
        term8 = table.get_cell(10, 1)
        print(term1.text)
        print(term2.text)
        print(term3.text)
        print(term4.text)
        print(term5.text)
        print(term6.text)
        print(term7.text)
        print(term8.text)
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('abnormal renal artery morphology', term1.text, 'Term1 is not returning')
        self.assertEqual('abnormal renal artery morphology', term2.text, 'Term2 is not returning')
        self.assertEqual('abnormal right renal artery morphology', term3.text, 'Term3 is not returning')
        self.assertEqual('abnormal right renal artery morphology', term4.text, 'Term4 is not returning')
        self.assertEqual('abnormal right renal artery morphology', term5.text, 'Term5 is not returning')
        self.assertEqual('abnormal right renal artery morphology', term6.text, 'Term6 is not returning')
        self.assertEqual('abnormal renal artery morphology', term7.text, 'Term7 is not returning')
        self.assertEqual('abnormal right renal artery morphology', term8.text, 'Term8 is not returning')

    def test_ht_link_with_parent_and_child_treeview(self):
        """
        @status: Tests that when you have a 1toN mapping for pheno, ht, and expression, child terms for expression,
        the ht annotations link in the Treeview section when clicked returns correct results.
        @note: CL-search-?  tested 9/09/2025
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0001069")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('Tree view details loaded')
        time.sleep(1)
        driver.find_element(By.ID,'htLink_CL:0001069').click()  # clicks the HT results link found in the Treeview section
        #time.sleep(2)
        # switch focus to the new tab for RNA-Seq and Microarray Experiment page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        items = self.driver.find_element(By.ID, 'pageReportTop')
        # verifies the number of results found is correct
        self.assertEqual('Showing experiments 1 - 9 of 9', items.text, 'number of results returned is not correct')


    def test_no_ht_mapping_zero_exp_link(self):
        """
        @status: Tests that when you have no ht annotations but zero Expression mapping, NO child terms,
        the ht annotations link in the Treeview section does not display, the expression results link is zero.
        @note: CL-search-?  !!!under construction, maybe change this test to where only expression link?!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:37425")
        wait.forAjax(driver)
        bodytext = driver.find_element(By.TAG_NAME, 'body').text
        # verifies the returned terms are the correct terms for this search
        self.assertTrue('0 expression results', 'The 0 expression results link is wrong')
        self.assertFalse('phenotype annotations' in bodytext)

    def test_no_ht_mapping_has_exp_link(self):
        """
        @status: Tests that when you have no ht mapping but Expression mapping, NO child terms,the ht
        annotations link in the Treeview section does not display, the expression results link has normal display.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:36473")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        linke = driver.find_element(By.CLASS_NAME,
                                    'expressionResultCount')  # the expression annotations link found in the Treeview section
        bodytext = driver.find_element(By.TAG_NAME, 'body').text
        print(linke.text)
        # asserts the expression results link exist and phenotype annotations link does not exist
        self.assertTrue('expression results' in bodytext)
        self.assertFalse('phenotype annotations' in bodytext)

    def test_no_ht_mapping_zero_exp_link2(self):
        """
        @status: Tests that when you have no ht mapping no Expression mapping, NO child terms,the ht
        annotations link in the Treeview section does not display, the expression results link has zero results.
        @note: CL-search-?  !!!under construction, waiting for implementation!!!!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:19101")
        wait.forAjax(driver)
        bodytext = driver.find_element(By.TAG_NAME, 'body').text
        # verifies the returned terms are the correct terms for this search
        self.assertTrue('0 expression results', 'The 0 expression results link is wrong')
        self.assertFalse('phenotype annotations' in bodytext)

    def test_ht_link_results_sort(self):
        """
        @status: Tests that when you click the ht term link in the detail section the results returned are
        in alphanumeric sort
        @note: CL-Search-?  tested 9/09/2025
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0001069")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('Tree view details loaded')
        time.sleep(1)
        driver.find_element(By.ID,'htLink_CL:0001069').click()  # clicks the HT results link found in the Treeview section
        # switch focus to the new tab for RNA-Seq and Microarray Experiment page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        title0 = driver.find_element(By.ID, "title0")
        title1 = driver.find_element(By.ID, "title1")
        title2 = driver.find_element(By.ID, "title2")
        title3 = driver.find_element(By.ID, "title3")
        title4 = driver.find_element(By.ID, "title4")
        title5 = driver.find_element(By.ID, "title5")
        title6 = driver.find_element(By.ID, "title6")
        print(title1.text)
        # These terms should be returned in the HT search results with the order given
        self.assertTrue('title0.text','Expression profiling by high throughput sequencing')
        self.assertTrue('title1.text', 'Developmental Acquisition of Regulomes Underlies Innate Lymphoid Cell Functionality')
        self.assertTrue('title2.text', 'ImmGen ULI: Systemwide RNA-seq profiles (#1)')
        self.assertTrue('title3.text', 'Homeostatic leukotrienes, IL-25, and IL-33 signals on intestinal ILC2 status')
        self.assertTrue('title4.text', 'Pulmonary ILC2s differentially depend on epithelial cell- and lymphatic endothelial cell-IL-7 in acute and chronic airway inflammations')
        self.assertTrue('title5.text', 'RNA-Seq of Group 2 innate lymphoid cells (ILC2) from uterine tissue (Virgin, E9.5, E18.5)')
        self.assertTrue('title6.text', 'RNA-Seq of Group 2 innate lymphoid cells (ILC2) from lung and lymph node')

    def tearDown(self):
        pass
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCellTypeBrowser))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\\WebdriverTests'))
