"""
Created on Aug 16, 2019
This set of tests verifies results you might get from the GXD query form, it covers all the Tabs
@author: jeffc
Verify that the disease list used on the GXD results page Disease filter is correct
Verify that the Disease filter is correctly return the right genes for disease by infectious agent
Verify that the Disease filter is correctly return no genes for disease by infectious agent
Verify that the GO molecular function list used on the GXD results page Molecular Function filter is correct
Verify that the GO molecular filter is correctly returning the right genes for molecular function ligase
Verify that the Molecular Function filter is correctly returning the right message when there are no Molecular Function filtered results
Verify that the GO biological process list used on the GXD results page Biological Process filter is correct
Verify that the GO biological process filter is correctly returning the right genes for biological process ??????
Verify that the Biological Process filter is correctly returning the right message when there are no Biological Process filtered results
Verify that the GO cellular component list used on the GXD results page Cellular Component filter is correct
Verify that the GO cellular component filter is correctly returning the right genes for cellular component ??????
Verify that the Cellular Component filter is correctly returning the right message when there are no Cellular Component filtered results
Verify that the "data" link in the Results Detail column goes to the correct website and experiment page
Verify that the ID link in the Reference column goes to the correct website and experiment page
Verify that the TPM Level (RNA-Seq) column is displayed and data is correct
Verify that the columns display in correct order when Additional Sample Data is displayed
Verify that the columns display in correct order when Additional Sample Data is not displayed
Verify that the assay type column is sorted correctly
Verify that the text Conditional Mutant get displayed in the Notes(RNA-Seq) column when appropriate. Always come first in the notes field
Verify that the filter by assay type option on the assays tab Assays Detail column works as expected
"""
import os.path
import sys
import time
import tracemalloc
import unittest
import config

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate
from util.form import ModuleForm

# from test.test_support import get_attribute
# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../..', )
)

# Test
tracemalloc.start()


class TestGxdResults(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/gxd/")
        self.driver.implicitly_wait(10)
        self.form = ModuleForm(self.driver)
        # wait = WebDriverWait(driver, 10)

    def test_gene_tab_do_filter_list(self):
        """
        @status: Tests that the disease list used on the GXD results page Disease filter is correct.
        @note: GXD-do-filter-1 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        phenobox = driver.find_element(By.ID, 'vocabTerm')
        # Enter your disease in the pheno box, in this case we leave the field empty to return  the entire disease list
        phenobox.send_keys("")
        self.driver.find_element(By.ID, 'submit1').click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'yui-dt-data'))):
            print('data now displayed')
        ele = driver.find_element(By.ID, 'doFilter')
        driver.execute_script("arguments[0].click()", ele)
        # capture the diseases listed in the disease filter popup list
        diseaseelts = self.driver.find_elements(By.NAME, 'doFilter')
        diseases = [e.get_attribute('value') for e in diseaseelts]
        print(diseases)
        # assert the list returned is correct.
        self.assertEqual(diseases, ['benign neoplasm', 'cancer', 'cardiovascular system disease',
                                    'central nervous system disease', 'chromosomal disease',
                                    'disease by infectious agent', 'disease of mental health', 'disease of metabolism',
                                    'endocrine system disease', 'gastrointestinal system disease',
                                    'hematopoietic system disease', 'immune system disease',
                                    'integumentary system disease', 'monogenic disease',
                                    'musculoskeletal system disease', 'nervous system disease',
                                    'peripheral nervous system disease', 'physical disorder', 'polygenic disease',
                                    'reproductive system disease', 'respiratory system disease',
                                    'sensory system disease', 'syndrome', 'thoracic disease', 'urinary system disease',
                                    'bar'], 'The list is not correct')

    def test_gene_tab_do_filter_gene_result(self):
        """
        @status: Tests that the Disease filter is correctly return the right genes for disease by infectious agent.
        @note: GXD-do-filter-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        phenobox = driver.find_element(By.ID, 'vocabTerm')
        # Enter your disease in the pheno box, in this case we leave the field empty to return  the entire disease list
        phenobox.send_keys("")
        self.driver.find_element(By.ID, 'submit1').click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'yui-dt-data'))):
            print('data now displayed')
        ele = driver.find_element(By.ID, 'doFilter')
        driver.execute_script("arguments[0].click()", ele)
        # select the filter option 'benign neoplasm'
        dfil = self.driver.find_elements(By.NAME, 'doFilter')[0]
        driver.execute_script("arguments[0].click();", dfil)
        # click the Filter button found on the filter by disease button
        filter = self.driver.find_element(By.ID, 'yui-gen0-button')
        driver.execute_script("arguments[0].click();", filter)
        # locate the Genes tab and click it
        ele1 = driver.find_element(By.ID, 'genestab')
        driver.execute_script("arguments[0].click()", ele1)
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'yui-dt-data'))):
            print('data now displayed')
        # locates the genes column and lists the genes found
        genelist = driver.find_element(By.ID, 'genesdata')
        time.sleep(2)
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-symbol')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        # assert that the genes returned are correct, should be 12 genes as of 9/11/2020
        self.assertEqual(searchTextItems,
                         ['Gene', 'Acvrl1', 'Eng', 'Foxo3', 'Kras', 'Men1', 'Notch4', 'Pdgfrb', 'Ptpn11', 'Ret', 'Sdhc', 'Sdhd', 'Tsc2',
                          'Vhl'], 'the list of genes is not correct!')

    def test_gene_tab_do_filter_no_genes(self):
        """
        @status: Tests that the Disease filter is correctly return no genes for disease by infectious agent.
        @note: GXD-do-filter-3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.ID, 'nomenclature')
        # Enter your gene in the nomenclature box
        genebox.send_keys("Rn7sk")
        self.driver.find_element(By.ID, 'submit1').click()
        ele = driver.find_element(By.ID, 'doFilter')
        driver.execute_script("arguments[0].click()", ele)
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'command'))):
            print('Filter by Biological Process popup displayed')
        time.sleep(2)
        eventmsg = self.driver.find_element(By.ID, 'command').text
        print(eventmsg)
        # asserts that the event msg for no genes with ontology associations is properly displayed
        self.assertEqual(eventmsg, 'No genes found with ontology associations.',
                         'the no genes found text is not displaying')

    def test_gene_tab_go_molecular_filter_list(self):
        """
        @status: Tests that the GO molecular function list used on the GXD results page Molecular Function filter is correct.
        @note: GXD-go-molec-filter-1 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        phenobox = driver.find_element(By.ID, 'vocabTerm')
        # Enter your molecular finction in the pheno box, (cell-cell signaling)
        phenobox.send_keys("cell-cell signaling")
        phenobox.send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, 'submit1').click()
        ele = driver.find_element(By.ID, 'goMfFilter')
        driver.execute_script("arguments[0].click()", ele)
        # self.driver.find_element(By.ID, 'goMfFilter').click()
        # capture the molecular functions listed in the molecular function filter popup list
        molefuncelts = self.driver.find_elements(By.NAME, 'goMfFilter')
        molecular = [e.get_attribute('value') for e in molefuncelts]
        print(molecular)
        # assert the list returned is correct.
        self.assertEqual(molecular, ['carbohydrate derivative binding', 'cytoskeletal protein binding', 'DNA binding',
                                     'enzyme regulator', 'hydrolase', 'ligase', 'lipid binding', 'oxidoreductase',
                                     'RNA binding', 'signaling receptor activity', 'signaling receptor binding',
                                     'transcription', 'transferase', 'transporter', 'bar'])

    def test_gene_tab_go_molecular_filter_gene_result(self):
        """
        @status: Tests that the GO molecular filter is correctly returning the right genes for molecular function ligase.
        @note: GXD-go-molec-filter-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        phenobox = driver.find_element(By.ID, 'vocabTerm')
        # Enter your molecular function in the pheno box, (cell-cell signaling)
        phenobox.send_keys("upregulation of cell blebbing")
        time.sleep(2)
        phenobox.send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, 'submit1').click()
        ele = driver.find_element(By.ID, 'goMfFilter')
        driver.execute_script("arguments[0].click()", ele)
        # select the filter option 'cytoskeletal protein binding'
        mffilter = self.driver.find_elements(By.NAME, 'goMfFilter')[1]
        driver.execute_script("arguments[0].click();", mffilter)
        # click the Filter button found on the filter by Molecular Function button
        filter = self.driver.find_element(By.ID, 'yui-gen0-button')
        driver.execute_script("arguments[0].click();", filter)
        if WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.CLASS_NAME, 'yui-dt-data'))):
            print('data now displayed')
        # locate the Genes tab and click it
        ele1 = driver.find_element(By.ID, 'genestab')
        driver.execute_script("arguments[0].click()", ele1)
        if WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.CLASS_NAME, 'yui-dt-data'))):
            print('data now displayed')
        # locates the genes column and lists the genes found
        genelist = driver.find_element(By.ID, 'genesdata')
        time.sleep(2)
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-symbol')
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        time.sleep(4)
        # assert that the genes returned are correct, should be 3 genes as of 8/29/2019
        self.assertEqual(searchtextitems, ['Gene', 'Anln'], 'the list of genes is not correct!')

    def test_gene_tab_go_molecular_filter_no_genes(self):
        """
        @status: Tests that the Molecular Function filter is correctly returning the right message when there are no Molecular Function filtered results.
        @note: GXD-go-molec-filter-3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.ID, 'nomenclature')
        # Enter your gene in the nomenclature box
        genebox.send_keys("Mir7-1")
        time.sleep(2)
        self.driver.find_element(By.ID, 'submit1').click()
        ele = driver.find_element(By.ID, 'goMfFilter')
        driver.execute_script("arguments[0].click()", ele)
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'command'))):
            print('Filter by Biological Process popup displayed')
        time.sleep(2)
        eventmsg = self.driver.find_element(By.ID, 'command').text
        print(eventmsg)
        # asserts that the event msg for no genes with ontology associations is properly displayed
        self.assertEqual(eventmsg, 'No genes found with ontology associations.',
                         'the no genes found text is not displaying')

    def test_gene_tab_go_biological_filter_list(self):
        """
        @status: Tests that the GO biological process list used on the GXD results page Biological Process filter is correct.
        @note: GXD-go-biol-filter-1 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        phenobox = driver.find_element(By.ID, 'vocabTerm')
        # Enter your molecular function in the pheno box, (cell-cell signaling)
        phenobox.send_keys("cell-cell signaling")
        phenobox.send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, 'submit1').click()
        self.driver.find_element(By.ID, 'goBpFilter').click()
        # capture the Biological Processes listed in the biological process filter popup list
        biologicelts = self.driver.find_elements(By.NAME, 'goBpFilter')
        biologic = [e.get_attribute('value') for e in biologicelts]
        print(biologic)
        # assert the list returned is correct.
        self.assertEqual(biologic,
                         ['carbohydrate derivative metabolism', 'cell differentiation', 'cell population proliferation',
                          'cellular component organization', 'DNA-templated transcription',
                          'establishment of localization', 'homeostatic process', 'immune system process',
                          'lipid metabolic process', 'programmed cell death', 'protein metabolic process',
                          'response to stimulus', 'signaling', 'system development', 'bar'])

    def test_gene_tab_go_biological_filter_gene_result(self):
        """
        @status: Tests that the GO biological process filter is correctly returning the right genes for biological process ??????.
        @note: GXD-go-biol-filter-2 !!this test is unstable, works sometimes and does not others.
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        phenobox = driver.find_element(By.ID, 'vocabTerm')
        # Enter your biological Process in the pheno box, (redox signal response)
        phenobox.send_keys("redox signal response")
        time.sleep(2)
        phenobox.send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, 'submit1').click()
        ele = driver.find_element(By.ID, 'goBpFilter')
        driver.execute_script("arguments[0].click()", ele)
        # select the filter option 'establishment of localization'
        bpfilter = self.driver.find_elements(By.NAME, 'goBpFilter')[5]
        driver.execute_script("arguments[0].click();", bpfilter)
        # click the Filter button found on the filter by Biological Process button
        filter = self.driver.find_element(By.ID, 'yui-gen0-button')
        driver.execute_script("arguments[0].click();", filter)
        time.sleep(2)
        # locate the Genes tab and click it
        ele1 = driver.find_element(By.ID, 'genestab')
        driver.execute_script("arguments[0].click()", ele1)
        time.sleep(3)
        # locates the genes column and lists the genes found
        genelist = driver.find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-symbol')
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        time.sleep(5)
        # assert that the genes returned are correct, should be 7 genes as of 8/29/2019
        self.assertEqual(searchtextitems, ['Bmal1', 'Clock', 'Fkbp1b', 'Ryr2', 'Selenos', 'Slc7a11', 'Smpd3'],
                         'the list of genes is not correct!')

    def test_gene_tab_go_biological_filter_no_genes(self):
        """
        @status: Tests that the Biological Process filter is correctly returning the right message when there are no Biological Process filtered results.
        @note: GXD-go-biol-filter-3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.ID, 'nomenclature')
        # Enter your gene in the nomenclature box
        genebox.send_keys("Ass-ps1")
        time.sleep(2)
        self.driver.find_element(By.ID, 'submit1').click()
        ele = driver.find_element(By.ID, 'goBpFilter')
        driver.execute_script("arguments[0].click()", ele)
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'command'))):
            print('Filter by Biological Process popup displayed')
        time.sleep(2)
        eventmsg = self.driver.find_element(By.ID, 'command').text
        print(eventmsg)
        # asserts that the event msg for no genes with ontology associations is properly displayed
        self.assertEqual(eventmsg, 'No genes found with ontology associations.',
                         'the no genes found text is not displaying')

    def test_gene_tab_go_cellular_filter_list(self):
        """
        @status: Tests that the GO cellular component list used on the GXD results page Cellular Component filter is correct.
        @note: GXD-go-cellular-filter-1 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        phenobox = driver.find_element(By.ID, 'vocabTerm')
        # Enter your cellular component in the pheno box, (cell-cell signaling)
        phenobox.send_keys("cell-cell signaling")
        time.sleep(2)
        phenobox.send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, 'submit1').click()
        ele = driver.find_element(By.ID, 'goCcFilter')
        driver.execute_script("arguments[0].click()", ele)
        # capture the Cellular Components listed in the cellular component filter popup list
        cellularelts = self.driver.find_elements(By.NAME, 'goCcFilter')
        cellular = [e.get_attribute('value') for e in cellularelts]
        print(cellular)
        # assert the list returned is correct.
        self.assertEqual(cellular,
                         ['cell projection', 'cytoplasmic vesicle', 'cytoskeleton', 'cytosol', 'endoplasmic reticulum',
                          'endosome', 'extracellular region', 'Golgi apparatus', 'mitochondrion',
                          'non-membrane-bounded organelle', 'nucleus', 'organelle envelope', 'organelle lumen',
                          'plasma membrane', 'protein-containing complex', 'synapse', 'vacuole', 'bar'])

    def test_gene_tab_go_cellular_filter_gene_result(self):
        """
        @status: Tests that the GO cellular component filter is correctly returning the right genes for cellular component ??????.
        @note: GXD-go-cellular-filter-2 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        anatstructurebox = driver.find_element(By.ID, 'structure')
        # Enter your anatomical structure in the anatomical structure box, (abdominal fat pad)
        anatstructurebox.send_keys("abdominal fat pad")
        time.sleep(2)
        anatstructurebox.send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, 'submit1').click()
        ele = driver.find_element(By.ID, 'goCcFilter')
        driver.execute_script("arguments[0].click()", ele)
        # select the filter option 'vacuole'
        ccfilter = self.driver.find_elements(By.NAME, 'goCcFilter')[0]
        driver.execute_script("arguments[0].click();", ccfilter)
        # click the Filter button found on the filter by Cellular Component button
        filter = self.driver.find_element(By.ID, 'yui-gen0-button')
        driver.execute_script("arguments[0].click();", filter)
        # locate the Genes tab and click it
        ele = driver.find_element(By.ID, 'genestab')
        driver.execute_script("arguments[0].click()", ele)
        time.sleep(2)
        # locates the genes column and lists the genes found
        genelist = driver.find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-symbol')
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        time.sleep(2)
        # assert that the genes returned are correct, should be 2 genes as of 9/10/2019
        self.assertEqual(searchtextitems, ['Siae'], 'the list of genes is not correct!')

    def test_gene_tab_go_cellular_filter_no_genes(self):
        """
        @status: Tests that the Cellular Component filter is correctly returning the right message when there are no Cellular Component filtered results.
        @note: GXD-go-cellular-filter-3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.ID, 'nomenclature')
        # Enter your gene in the nomenclature box
        genebox.send_keys("Ass-ps2")
        time.sleep(2)
        self.driver.find_element(By.ID, 'submit1').click()
        ele = driver.find_element(By.ID, 'goCcFilter')
        driver.execute_script("arguments[0].click()", ele)
        time.sleep(2)
        eventmsg = self.driver.find_element(By.ID, 'command').text
        print(eventmsg)
        # asserts that the event msg for no genes with ontology associations is properly displayed
        self.assertEqual(eventmsg, 'No genes found with ontology associations.',
                         'the no genes found text is not displaying')

    def test_assay_results_tab_data_link(self):
        """
        @status: Tests that the "data" link in the Results Detail column goes to the correct website and experiment page.
        @note: GXD-aresults-1, 2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # Enter your gene
        genebox.send_keys("shh")
        time.sleep(2)
        # find the Mutated in option, check it and use the gene Wt1
        mutate = driver.find_element(By.ID, 'mutatedIn')
        # Enter your gene
        mutate.send_keys("Nrg1")
        # find the InSitu assays and Blot assays check boxes and uncheck them
        allin = driver.find_element(By.CLASS_NAME, 'allInSitu')
        driver.execute_script("arguments[0].click();", allin)
        ball = driver.find_element(By.ID, 'blotAll')
        driver.execute_script("arguments[0].click();", ball)
        # find the Whole Genome assays check box and click it
        wgenall = driver.find_element(By.ID, 'wholeGenomeAll')
        driver.execute_script("arguments[0].click();", wgenall)
        # find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        # Defaults to Assays Tab so no tab click required
        # locates the Results Detail column and lists the data found
        genelist = driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-assayID')
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        # assert that "data" link goes to the correct experiment page.Test result for E-MTAB-5772
        links = self.driver.find_element(By.LINK_TEXT, 'data')
        exturl = links.get_attribute('href')
        # assert that the link url is correct
        self.assertEqual(exturl, 'https://www.ebi.ac.uk/gxa/experiments/E-MTAB-5772/Results')

    def test_assay_results_tab_ref_exp_id(self):
        """
        @status: Tests that the ID link in the Reference column goes to the correct website and experiment page.
        @note: GXD-aresults-3, 4 
        @note: this test will fail unless run against test machine due to assert result.
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # Enter your gene
        genebox.send_keys("shh")
        time.sleep(2)
        # find the Mutated in option, check it and use the gene Wt1
        mutate = driver.find_element(By.ID, 'mutatedIn')
        # Enter your gene
        mutate.send_keys("Nrg1")
        # find the InSitu assays and Blot assays check boxes and uncheck them
        allin = driver.find_element(By.CLASS_NAME, 'allInSitu')
        driver.execute_script("arguments[0].click();", allin)
        ball = driver.find_element(By.ID, 'blotAll')
        driver.execute_script("arguments[0].click();", ball)
        # find the Whole Genome assays check box and click it
        wgenall = driver.find_element(By.ID, 'wholeGenomeAll')
        driver.execute_script("arguments[0].click();", wgenall)
        # find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        # Defaults to Assays Tab so no tab click required
        # locates the Reference column and finds the ID link to click
        genelist = driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-reference')
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        # assert that ID link goes to the correct experiment page.Test result for E-MTAB-5772
        links = self.driver.find_element(By.LINK_TEXT, 'E-MTAB-5772')
        inturl = links.get_attribute('href')
        # assert that the link url is correct
        self.assertEqual(inturl, 'https://test.informatics.jax.org/gxd/htexp_index/summary?arrayExpressID=E-MTAB-5772')

    def test_assay_results_tab_tpm_column(self):
        """
        @status: Tests that the TPM Level (RNA-Seq) column is displayed and data is correct.
        @note: GXD-aresults-5 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # Enter your gene
        genebox.send_keys("Cela2a,Gna12,Cdc45,Btn1a1")
        time.sleep(2)
        Select(self.driver.find_element(By.ID, 'theilerStage')).deselect_by_value('0')  # deselect the default option
        Select(self.driver.find_element(By.ID, 'theilerStage')).select_by_value(
            '28')  # finds the theiler stage list and select the TS 28 option
        # find the InSitu assays and Blot assays check boxes and uncheck them
        allin = driver.find_element(By.CLASS_NAME, 'allInSitu')
        driver.execute_script("arguments[0].click();", allin)
        ball = driver.find_element(By.ID, 'blotAll')
        driver.execute_script("arguments[0].click();", ball)
        # find the Whole Genome assays check box and click it
        wgenall = driver.find_element(By.ID, 'wholeGenomeAll')
        driver.execute_script("arguments[0].click();", wgenall)
        # find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        # Defaults to Assays Results Tab so no tab click required
        # locates the TPM Level column and finds all the data in the column?
        genelist = driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-tpmLevel')
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        # assert that the TPM column results are displaying  the 4 different options
        self.assertIn('Below Cutoff', searchtextitems, 'Below Cutoff is not being found!')
        self.assertIn('Low', searchtextitems, 'Low is not being found!')
        self.assertIn('Medium', searchtextitems, 'Medium is not being found!')
        self.assertIn('High', searchtextitems, 'High is not being found!')

    def test_assay_results_tab_add_sample_data_on(self):
        """
        @status: Tests that the columns display in correct order when Additional Sample Data is displayed.
        @note: GXD-aresults-6,7
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # Enter your gene
        genebox.send_keys("shh")
        # find the InSitu assays and Blot assays check boxes and uncheck them
        allin = driver.find_element(By.CLASS_NAME, 'allInSitu')
        driver.execute_script("arguments[0].click();", allin)
        ball = driver.find_element(By.ID, 'blotAll')
        driver.execute_script("arguments[0].click();", ball)
        # find the Whole Genome assays check box and click it
        wgenall = driver.find_element(By.ID, 'wholeGenomeAll')
        driver.execute_script("arguments[0].click();", wgenall)
        # find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        # Defaults to Assays Results Tab so no tab click required
        # click the Show/Hide Additional Sample Data box
        driver.find_element(By.ID, 'showHide').click()
        time.sleep(2)
        # locates the table column headings and verify the order of the columns
        cols = driver.find_elements(By.XPATH, './/span[@class = "yui-dt-label"]')
        head = iterate.getTextAsList(cols)
        print(head)
        # assert that the columns are in the correct order
        self.assertEqual(head, ['Gene', 'Result Details', 'Assay Type', 'Age', 'Structure', 'Cell\nType', 'Detected?',
                                'TPM Level\n(RNA-Seq)', 'Biological Replicates\n(RNA-Seq)', 'Images',
                                'Mutant Allele(s)', 'Strain', 'Sex', 'Notes\n(RNA-Seq)', 'Reference', ''])

    def test_assay_results_tab_column_headings(self):
        """
        @status: Tests that the columns display in correct order when Additional Sample Data is not displayed.
        @note: GXD-aresults-8
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # Enter your gene
        genebox.send_keys("shh")
        time.sleep(2)
        # find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        # Defaults to Assays Results Tab so no tab click required
        # locates the table column headings and verify the order of the columns
        cols = driver.find_elements(By.XPATH, './/span[@class = "yui-dt-label"]')
        head = iterate.getTextAsList(cols)
        print(head)
        # assert that the columns are in the correct order
        self.assertEqual(head, ['Gene', 'Result Details', 'Assay Type', 'Age', 'Structure', 'Cell\nType', 'Detected?',
                                'TPM Level\n(RNA-Seq)', '', 'Images', 'Mutant Allele(s)', '', '', '', 'Reference', ''])

    def test_assay_results_tab_assay_type_col_sort(self):
        """
        @status: Tests that the assay type column is sorted correctly.
        @note: GXD-aresults-9 sort order is Immunohistochemistry, RNA in situ, In situ reporter (knock in), Northern blot, Western blot, RT-PCR, RNase protection, Nuclease S, RNA-Seq
        @attention: better to find an example that has all assay types with few results
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # Enter your gene
        genebox.send_keys("Afp")
        time.sleep(2)
        Select(self.driver.find_element(By.ID, 'theilerStage')).deselect_by_value('0')  # deselect the default option
        Select(self.driver.find_element(By.ID, 'theilerStage')).select_by_value(
            '25')  # finds the theiler stage list and select the TS 28 option
        # find the Wild Type specimens only button and click it
        iwild = self.driver.find_element(By.ID, 'isWildType')
        driver.execute_script("arguments[0].click();", iwild)
        # find the Whole Genome assays check box and click it
        wgenall = driver.find_element(By.ID, 'wholeGenomeAll')
        driver.execute_script("arguments[0].click();", wgenall)
        # find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        # Defaults to Assays Results Tab so no tab click required
        # locates the Assay Type column and finds all the data in the column?
        genelist = driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-assayType')
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems)
        # assert that the TPM column results are displaying  the 4 different options
        self.assertEqual(searchtextitems,
                         ['Immunohistochemistry', 'Immunohistochemistry', 'Western blot', 'Western blot', 'RT-PCR',
                          'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq',
                          'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq'])

    def test_assay_results_tab_cond_mutant(self):
        """
        @status: Tests that the text Conditional Mutant get displayed in the Notes(RNA-Seq) column when appropriate. Always come first in the notes field.
        @note: GXD-aresults-10  
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # Enter your gene
        genebox.send_keys("Abca15")
        time.sleep(2)
        Select(self.driver.find_element(By.ID, 'theilerStage')).deselect_by_value('0')  # deselect the default option
        Select(self.driver.find_element(By.ID, 'theilerStage')).select_by_value(
            '28')  # finds the theiler stage list and select the TS 28 option
        # find the In Situ Assays check box and unchecks it
        isall = self.driver.find_element(By.ID, 'inSituAll')
        driver.execute_script("arguments[0].click();", isall)
        # find the Blot Assays check box and unchecks it
        ball = self.driver.find_element(By.ID, 'blotAll')
        driver.execute_script("arguments[0].click();", ball)
        # find the Whole Genome assays check box and click it
        wgenall = driver.find_element(By.ID, 'wholeGenomeAll')
        driver.execute_script("arguments[0].click();", wgenall)
        # find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        # Click the Show/Hide Additional Sample Data box to display other columns
        driver.find_element(By.ID, 'showHide').click()
        # Defaults to Assays Results Tab so no tab click required
        # locates the Notes(RNA-Seq) column and finds all the data in the column?
        genelist = driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-notes')
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems[0] + '  line0')
        print(searchtextitems[1] + '  line1')
        print(searchtextitems[2] + '  line2')
        print(searchtextitems[3] + '  line3')
        print(searchtextitems[4] + '  line4')
        print(searchtextitems[5] + '  line5')
        print(searchtextitems[6] + '  line6')
        print(searchtextitems[7] + '  line7')
        print(searchtextitems[8] + '  line8')
        print(searchtextitems[9] + '  line9')
        print(searchtextitems[10] + '  line10')
        print(searchtextitems[11] + '  line11')
        print(searchtextitems[12] + '  line12')
        # assert that the TPM column results are displaying  the 4 different options
        self.assertEqual(searchtextitems[0], 'wild type')
        self.assertEqual(searchtextitems[5], 'day of parturition (within 12 hours after delivery)')
        self.assertEqual(searchtextitems[6], 'Conditional mutant. day 6 of pregnancy')
        self.assertEqual(searchtextitems[7], 'day 6 of pregnancy')

    def test_assay_results_filter_by_assay_type(self):
        """
        @status: Tests that the filter by assay type option on the assays tab Assays Detail column works as expected.
        @note: GXD-aresults-11
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        anat_struct = driver.find_element(By.ID, 'structure')
        # Enter your anatomical structure
        anat_struct.send_keys("liver")
        time.sleep(2)
        anat_struct.send_keys(Keys.TAB)
        # find the Whole Genome assays check box and check it
        wgenall = driver.find_element(By.ID, 'wholeGenomeAll')
        driver.execute_script("arguments[0].click();", wgenall)
        # find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        # Defaults to Assays Results Tab, so find and click the Assays tab
        # locate the Assays tab and click it
        ele = driver.find_element(By.ID, 'assaystab')
        driver.execute_script("arguments[0].click()", ele)
        # self.driver.find_element(By.ID, 'assaystab').click()
        # finds the Filter by Assay Type popup and selects "RNA-Seq".
        ele1 = driver.find_element(By.ID, 'assayTypeFilter')
        driver.execute_script("arguments[0].click()", ele1)
        # driver.find_element(By.ID, 'assayTypeFilter').click()
        driver.find_element(By.CSS_SELECTOR, '#command > label:nth-child(11) > input:nth-child(1)').click()
        driver.find_element(By.ID, 'yui-gen0-button').click()
        time.sleep(2)
        # locates the Reference column and finds all the data in the column
        reflist = driver.find_element(By.ID, 'assaysdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = reflist.find_elements(By.CLASS_NAME, 'yui-dt-col-reference')
        searchtextitems = iterate.getTextAsList(items)
        print(searchtextitems[0] + '  line0')
        print(searchtextitems[1] + '  line1')
        print(searchtextitems[2] + '  line2')
        print(searchtextitems[3] + '  line3')
        print(searchtextitems[4] + '  line4')
        print(searchtextitems[5] + '  line5')
        print(searchtextitems[6] + '  line6')
        print(searchtextitems[7] + '  line7')
        print(searchtextitems[8] + '  line8')
        print(searchtextitems[9] + '  line9')
        print(searchtextitems[10] + '  line10')
        print(searchtextitems[11] + '  line11')
        print(searchtextitems[12] + '  line12')
        time.sleep(2)
        # assert that the reference ID E-MTAB-599 exists in each row checked
        self.assertIn(
            "E-GEOD-33979 Novel roles for Klf1 in regulating the erythroid transcriptome revealed by mRNA-seq",
            searchtextitems[0])
        self.assertIn(
            'E-GEOD-45684 Transcription profiling by high throughput sequencing of a Diversity Outbred mice population and the eight founder strains: A/J, 129S1/SvImJ, C57BL/6J, NOD/ShiLtJ, NZO/HlLtJ, CAST/EiJ, PWK/PhJ, and WSB/EiJ',
            searchtextitems[1])
        self.assertIn(
            'E-GEOD-70484 Transcription profiling by high throughput sequencing of different tissues from mouse to detect maternal or paternal allele expression biases at the tissue level',
            searchtextitems[2])
        self.assertIn(
            'E-GEOD-72491 Transcription profiling by RNA-seq of fetal liver from poly(C) binding protein 2 (Pcbp2) knockout mice',
            searchtextitems[3])
        self.assertIn('E-GEOD-74747 RNA-seq of 9 tissues from an adult male C57BL/6 mouse', searchtextitems[4])
        self.assertIn(
            'E-MTAB-599 RNA-seq of mouse DBA/2J x C57BL/6J heart, hippocampus, liver, lung, spleen and thymus',
            searchtextitems[5])
        self.assertIn(
            'E-MTAB-2328 Transcription profiling by high throughput sequencing of liver and brain during mouse organ development',
            searchtextitems[6])
        self.assertIn('E-MTAB-2801 Strand-specific RNA-seq of nine mouse tissues', searchtextitems[7])
        self.assertIn('E-MTAB-3662 Pilot KOMP knockout mouse strains', searchtextitems[8])

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxdResults))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
