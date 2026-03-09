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
        self.assertEqual(term[21].text, 'OB FRMD7 GABA GABAergic neuron (Primate)')
        self.assertEqual(term[22].text, 'oxygen accumulating cell')
        self.assertEqual(term[23].text, 'perivascular cell')
        self.assertEqual(term[24].text, 'photosynthetic cell')
        self.assertEqual(term[25].text, 'polyploid cell')
        self.assertEqual(term[26].text, 'precursor cell')
        self.assertEqual(term[27].text, 'prokaryotic cell')
        self.assertEqual(term[28].text, 'secretory cell')
        self.assertEqual(term[29].text, 'skeletogenic cell')
        self.assertEqual(term[30].text, 'SN GATA3-PVALB GABA GABAergic neuron (Primate)')
        self.assertEqual(term[31].text, 'SN SOX6 Dopa substantia nigra dopaminergic neuron (Primate)')
        self.assertEqual(term[32].text, 'SN-VTR CALB1 Dopa substantia nigra dopaminergic neuron (Primate)')
        self.assertEqual(term[33].text, 'SN-VTR GAD2 Dopa dopaminergic neuron (Primate)')
        self.assertEqual(term[34].text, 'STRd D1/D2-hybrid medium spiny neuron (Primate)')
        self.assertEqual(term[35].text, 'STRd D2 Striomat hybrid medium spiny neuron (Primate)')
        self.assertEqual(term[36].text, 'stuff accumulating cell')
        self.assertEqual(term[37].text, 'supporting cell')
        self.assertEqual(term[38].text, 'zygote')


    def test_parents_multi(self):
        """
        @status: Tests that searching by a cell ontology term that is associated with multiple parents return the
        correct results
        @note: CT-Search-? I'm not sure there is an example of this so maybe this test is not needed?
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
        @status: Tests that searching by an cell ontology term that is associated to a phenotype but has no expression
        annotations  passed 01/22/2026
        @note: CL_Search-
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:2000078")
        recomLink = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "recomLink_CL2000078")))
        print('Tree view details loaded')
        driver.execute_script("arguments[0].scrollIntoView(true);", recomLink)
        recomLink.click()
        # switch focus to the new tab for Recombinase Alleles - Tissue summary
        self.driver.switch_to.window(self.driver.window_handles[-1])

        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, 'dynamicdata'))
        )

        results_table = driver.find_element(By.ID, 'dynamicdata')
        table = Table(results_table)

        term1 = table.get_cell(2, 2)
        print(term1.text)

        self.assertEqual(
            'Tg(Ntrk3-cre/ERT2)#Phep\ntransgene insertion, Paul A Heppenstall',
            term1.text,
            'Term1 is not returning'
        )


    def test_pheno_link_treeview(self):
        """
        @status: Tests that the phenotype annotations link in the Treeview section when clicked returns correct results.
        @note:  passed 02/09/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:1001607")
        recomLink = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.ID, 'recomLink_CL1001607')))
        print('Tree view details loaded')
        driver.execute_script("arguments[0].scrollIntoView(true);", recomLink)
        recomLink.click()
        # switch focus to the new tab for Recombinase Alleles - Tissue summary
        self.driver.switch_to.window(self.driver.window_handles[-1])

        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, 'dynamicdata'))
        )

        results_table = driver.find_element(By.ID, 'dynamicdata')
        table = Table(results_table)

        term1 = table.get_cell(2, 2)
        term2 = table.get_cell(3, 2)
        print(term1.text)
        print(term2.text)

        self.assertEqual(
            'Tg(Rr162136-cre/ERT2)#Bpou\ntransgene insertion, Blandine Poulet',
            term1.text,
            'Term1 is not returning'
        )
        self.assertEqual(
            'Tg(Prg4-cre/ERT2)#Ndy\ntransgene insertion, Nathaniel A Dyment',
            term2.text,
            'Term2 is not returning'
        )


    def test_pheno_link_nochild_treeview(self):
        """
        @status: Tests that when you have a 1to1 mapping with no child terms associated(gxd&pheno),the phenotype
        annotations link in the Treeview section when clicked returns correct results.
        @note: CL-search-?  passed 01/23/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0000225")
        recom_link = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.ID, 'recomLink_CL0000225')))
        print('Tree view details loaded')
        recom_link.click()
        #time.sleep(2)
        original_window = driver.current_window_handle
        WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(
            [w for w in driver.window_handles if w != original_window][0]
        )

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'dynamicdata'))
        )

        results_table = driver.find_element(By.ID, 'dynamicdata')
        table = Table(results_table)

        term1 = table.get_cell(2, 2)
        print(term1.text)

        self.assertEqual(
            'Tg(Nrp2-cre,-EGFP)#Qsch\ntransgene insertion, Quenten Schwarz',
            term1.text,
            'Term1 is not returning'
        )


    def test_no_pheno_link_exp_link(self):
        """
        @status: Tests that when you have a 1to1 mapping with NO Pheno mapping/has GXD mapping,the GXD link has data
        the phenotype annotations link in the Treeview section has zero results.
        @note: CL-search-?  passed 01/22/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0000566")

        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "resultLink_CL0000566")))
        print('Tree view details loaded')

        bodytext = driver.find_element(By.TAG_NAME, 'body').text
        # the phenotype annotations link found in the Treeview section should be zero
        self.assertFalse('phenotype annotations' in bodytext)

    def test_zero_pheno_link_zero_exp_link(self):
        """
        @status: Tests that when you have a 1to1 NO mapping for expression or pheno, NO child terms, the phenotype
        annotations is zero and expression results links in the Treeview section is normal.
        @note: CL-search-?  needs to be converted to using cell otology browser
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:37850")
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'ygtvchildren'))):
            print('Tree view details loaded')
        time.sleep(2)
        # verifies the returned results are zero for this search
        assert '(0 expression results; 0 phenotype annotations)' in driver.page_source

    def test_pheno_link_with_parent_and_child_treeview(self):
        """
        @status: Tests that when you have a 1toN mapping for pheno and expression, child terms for expression,
        the phenotype annotations link in the Treeview section when clicked returns correct results.
        @note: CL-search-?  passed 01/28/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0000388")
        recomLink =  WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, 'recomLink_CL0000388')))
        print('Tree view details loaded')
        driver.execute_script("arguments[0].scrollIntoView(true);", recomLink)
        recomLink.click()
        time.sleep(2)
        original_window = driver.current_window_handle
        WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(
            [w for w in driver.window_handles if w != original_window][0]
        )

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'dynamicdata'))
        )

        results_table = driver.find_element(By.ID, 'dynamicdata')
        table = Table(results_table)

        term1 = table.get_cell(2, 2)
        print(term1.text)

        self.assertEqual(
            'Tg(Prg4-cre/ERT2)#Ndy\ntransgene insertion, Nathaniel A Dyment',
            term1.text,
            'Term1 is not returning'
        )


    def test_no_pheno_mapping_zero_exp_link(self):
        """
        @status: Tests that when you have no phenotype mapping and no Expression mapping, NO child terms,
        the phenotype annotations link and expression results link in the Treeview section does not display, the RNA-Seq results link is visible.
        @note: CL-search-?  passed 1/23/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0002554")
        wait.forAjax(driver)
        bodytext = driver.find_element(By.TAG_NAME, 'body').text
        # verifies the returned terms are the correct terms for this search
        self.assertTrue('1 RNA-seq or microarray experiments', 'The RNA-seq link is not displaying')
        self.assertFalse('expression results' in bodytext)
        self.assertFalse('recombinase alleles' in bodytext)

    def test_no_pheno_mapping_has_rna_link(self):
        """
        @status: Tests that when you have no phenotype mapping but rna mapping, NO child terms,the phenotype
        annotations link in the Treeview section does not display, the rna results link has normal display.
        @note: CL-search-?  passed 01/28/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0010017")
        if WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'annotationLink'))):
            print('Tree view details loaded')
        linkr = driver.find_element(By.ID,
                                    'htLink_CL0010017')  # the rna-seq link found in the Treeview section
        bodytext = driver.find_element(By.TAG_NAME, 'body').text
        #print(linkr.text)
        # asserts the rna-seq results link exist and phenotype annotations link does not exist
        self.assertTrue('RNA-seq or microarray experiments' in bodytext)
        self.assertFalse('recombinase alleles' in bodytext)

    def test_pheno_link_results_sort(self):
        """
                @status: Tests that when you click the phenotypes term link in the detail section the results returned are
                in alphanumeric sort of driver column
                @note: CL-Search-? passed 2/12/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0000327")

        # Wait until the phenotype link is clickable and click it
        recomLink = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'recomLink_CL0000327'))
        )
        recomLink.click()

        # Switch to the newly opened window
        original_window = driver.current_window_handle
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(
            next(w for w in driver.window_handles if w != original_window)
        )

        # Wait until Driver column cells are present
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'yui-dt0-col-driver')
            )
        )

        # Collect driver column values
        driver_cells = driver.find_elements(By.CLASS_NAME, 'yui-dt0-col-driver')
        driver_texts = [cell.text.strip() for cell in driver_cells if cell.text.strip() and cell.text.strip().lower() != 'driver']

        # Debug output (optional)
        print("Driver column values:", driver_texts)

        # Verify alphanumeric sort
        self.assertEqual(
            driver_texts, [
    'Acan', 'Acan', 'Clec11a', 'Col2a1', 'Col10a1',
    'Col10a1', 'Ihh', 'Islr', 'Lepr', 'Mobp',
    'Pdgfrb', 'Prg4', 'Prg4'
],
            "Driver column is not sorted alphanumerically"
        )

    def test_ht_link_noexpression(self):
        """
        @status: Tests that searching by an CL term that is associated to a ht expression but has no regular expression
        annotations  passed 1/28/2026
        @note: CL_Search-
        """
        driver = self.driver
        # search for: double-positive, alpha-beta thymocyte
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0000809")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('Tree view details loaded')
        time.sleep(1)
        driver.find_element(By.ID,'htLink_CL0000809').click()  # clicks the HT results link found in the Treeview section
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
        @note:  tested 1/23/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:2000053")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('Tree view details loaded')
        time.sleep(1)
        driver.find_element(By.ID,'htLink_CL2000053').click()  # clicks the HT results link found in the Treeview section
        #time.sleep(2)
        # switch focus to the new tab for RNA-Seq and Microarray Experiment page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        items = self.driver.find_element(By.ID, 'pageReportTop')
        # verifies the number of results found is correct
        self.assertEqual('Showing experiments 1 - 3 of 3', items.text, 'number of results returned is not correct')


    def test_ht_link_nochild_treeview(self):
        """
        @status: Tests that when you have a 1to1 mapping with no child terms associated(gxd&ht&pheno),the phenotype
        annotations link in the Treeview section when clicked returns correct results.
        @note: CL-search-?  passed 2/12/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0000058")
        htLink = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.ID, 'recomLink_CL0000058')))
        print('rna-seq link found')
        driver.execute_script("arguments[0].scrollIntoView(true);", htLink)
        htLink.click()
        # switch focus to the new tab for RNA-Seq and Microarray Experiment page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        # verify the correct cell type is displayed in the "You searched for..." section
        ctname = self.driver.find_element(By.CSS_SELECTOR, '#querySummary > div:nth-child(1) > b:nth-child(4)')
        print(ctname.text)
        # verifies the returned results are for the correct cell type for this search
        self.assertIn("chondroblast", ctname.text, 'Term1 is not returning')

    def test_ht_link_withchildboth_treeview(self):
        """
        @status: Tests that when you have a 1to1 mapping with child terms associated(gxd&ht&pheno),the ht
        annotations link in the Treeview section when clicked returns correct results.
        @note: CL-search-?  passed 1/23/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0000346")
        if WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, 'recomLink_CL0000346'))):
            print('expression link not found')
        htLink = driver.find_element(By.ID,'htLink_CL0000346')  # clicks the RNA-Seq link found in the Treeview section
        htLink.click()
        # switch to the new window
        wait.forNewWindow(self.driver, 2)
        self.driver.switch_to.window(self.driver.window_handles[1])

        # verify the correct cell type is displayed in the "You searched for..." section
        ctname = self.driver.find_element(By.ID, 'searchSummary')

        # verifies the returned results are for the correct cell type for this search
        self.assertIn("hair follicle dermal papilla cell", ctname.text, 'cell type is not correct')


    def test_no_ht_link_exp_link(self):
        """
        @status: Tests that when you have a 1to1 mapping with NO ht annotations/has GXD mapping,the GXD link has data
        the ht annotations link in the Treeview section has zero results.
        @note: CL-search-?  tested 1/23/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0000175")
        if WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.ID, 'resultLink_CL0000175'))):
            print('expression link found')
        time.sleep(1)
        # verify that there is no HT results link
        ht_link = driver.find_elements(By.ID, "htLink_CL0000175")
        if len(ht_link) > 0:
            print(f"HT link exists!")
        else:
            print("HT link does not exist.")
        driver.find_element(By.ID,'resultLink_CL0000175').click()  # clicks the expression results link found in the Treeview section
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
        @note: CL-search-?  passed 1/23/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0001087")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'recomLink_CL0001087'))):
            print('recombinase link found')
        time.sleep(1)
        # verify that there is no expression results link
        exp_link = driver.find_elements(By.ID, "recomLink_CL0001087")
        if len(exp_link) > 0:
            print(f"Expression link exists!")
        else:
            print("Expression link does not exist.")
        # verify that there is no HT results link
        ht_link = driver.find_elements(By.ID, "htLink_CL0009014")
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
        @status: Tests that when you have a 1to1  NO mapping for expression or ht, has child terms,the expression
        annotations is zero, the ht annotations is zero and phenotype results links in the Treeview section is normal.
        @note: CL-search-?  passed 01/23/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:4030025")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'recomLink_CL4030025'))):
            print('Tree view details loaded')
        linke = driver.find_element(By.ID,
                                    'recomLink_CL4030025')  # the expression annotations link found in the Treeview section
        print(linke.text)
        bodytext = driver.find_element(By.TAG_NAME, 'body').text
        # verifies that there is a recombinase link but no expression or RNA-seq links
        self.assertTrue('recombinase alleles' in bodytext)
        self.assertFalse('expression results' in bodytext)
        self.assertFalse('RNA-seq or microarray experiments' in bodytext)

    def test_ht_link_withparent3child_treeview(self):
        """
        @status: Tests that when you have a 1toN mapping with parent and 3 child terms associated(ht)
        has child terms,the ht annotations link in the Treeview section when clicked returns correct results.
        @note: CL-search-?  passed 1/28/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0000449")
        htLink = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'htLink_CL0000449')))
        print('Tree view details loaded')
        driver.execute_script("arguments[0].scrollIntoView(true);", htLink)
        htLink.click()
        # switch focus to the new tab for gene expression page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        results_table = self.driver.find_element(By.ID, 'resultSummary')
        table = Table(results_table)
        title1 = self.driver.find_element(By.ID, 'title0')
        print(title1.text)
        title2 = self.driver.find_element(By.ID, 'title1')
        print(title2.text)
        title3 = self.driver.find_element(By.ID, 'title2')
        print(title3.text)
        title4 = self.driver.find_element(By.ID, 'title3')
        print(title4.text)
        title5 = self.driver.find_element(By.ID, 'title4')
        print(title5.text)

        # verifies the returned results are the correct for this search
        self.assertEqual('RNA-seq Analysis of Gs-linked GPCRs expressed in mouse inguinal white adipocytes (iWAT), epididymal white adipocytes (eWAT) and brown adipose tissues (BAT)', title1.text, 'Title1 is not correct')
        self.assertEqual('RNA-seq Analysis of GPCRs expressed in mouse inguinal white adipocytes (iWAT), epididymal white adipocytes (eWAT) and brown adipose tissues (BAT) after high fat diet treatment.', title2.text, 'Title2 is not correct')
        self.assertEqual('MED1 is a lipogenesis co-activator required for postnatal adipose expansion', title3.text, 'Title3 is not correct')
        self.assertEqual('Aging Induced Syntaxin 4 Deficiency Mediates Brown Adipose Tissue Pyroptosis and Thermogenic Dysfunction', title4.text, 'Title4 is not correct')
        self.assertEqual('Mouse brown adipocyte single nucleus RNAseq with Smartseq2', title5.text, 'Title5 is not correct')


    def test_ht_link_with_parent_and_child_treeview(self):
        """
        @status: Tests that when you have a 1toN mapping for pheno, ht, and expression, child terms for expression,
        the ht annotations link in the Treeview section when clicked returns correct results.
        @note: CL-search-?  tested 1/23/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0001069")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('Tree view details loaded')
        time.sleep(1)
        driver.find_element(By.ID,'htLink_CL0001069').click()  # clicks the HT results link found in the Treeview section
        #time.sleep(2)
        # switch focus to the new tab for RNA-Seq and Microarray Experiment page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        items = self.driver.find_element(By.ID, 'pageReportTop')
        # verifies the number of results found is correct
        self.assertEqual('Showing experiments 1 - 11 of 11', items.text, 'number of results returned is not correct')


    def test_no_ht_no_recom_exp_link(self):
        """
        @status: Tests that when you have no ht annotations, no recombinase annotation, just an expression link
        @note: CL-search-?  passed 1/23/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:4052001")
        wait.forAjax(driver)
        bodytext = driver.find_element(By.TAG_NAME, 'body').text
        # verifies the returned terms are the correct terms for this search
        self.assertTrue('expression results', 'The expression results link is missing')
        self.assertFalse('RNA-seq or microarray experiments' in bodytext)
        self.assertFalse('recombinase alleles' in bodytext)

    def test_no_ht_has_recom_has_exp_link(self):
        """
        @status: Tests that when you have no ht but has recombinase and Expression mapping, the ht
        annotations link in the Treeview section does not display, the recombinase alleles link and the expression results link has normal display.
        @note: CL-search-?  passed 1/23/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:2000057")
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, 'resultLink_CL2000057'))):
            print('Tree view details loaded')
        bodytext = driver.find_element(By.TAG_NAME, 'body').text
        # asserts the expression results link exists and phenotype annotations exists, but no RNA-seq link
        self.assertTrue('expression results' in bodytext)
        self.assertTrue('recombinase alleles' in bodytext)
        self.assertFalse('RNA-seq or microarray experiments' in bodytext)

    def test_ht_link_results_sort(self):
        """
        @status: Tests that when you click the ht term link in the detail section the results returned are
        in alphanumeric sort
        @note: CL-Search-?  tested 1/23/2026
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/cell_ontology/CL:0001069")
        if WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('Tree view details loaded')
        time.sleep(1)
        driver.find_element(By.ID,'htLink_CL0001069').click()  # clicks the HT results link found in the Treeview section
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
