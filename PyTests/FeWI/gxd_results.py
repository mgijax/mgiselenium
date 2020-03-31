'''
Created on Aug 16, 2019
This set of tests verifies results you might get from the GXD query form, it covers all the Tabs
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from util.table import Table
from util.form import ModuleForm
import sys,os.path
from genericpath import exists
#from test.test_support import get_attribute
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
import config
from config import TEST_URL

class TestGXDResults(unittest.TestCase):


    def setUp(self):
    
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/gxd/")
        self.driver.implicitly_wait(10)
        self.form = ModuleForm(self.driver)
        
     
    def test_gene_tab_do_filter_list(self):
        """
        @status: Tests that the disease list used on the GXD results page Disease  filter is correct.
        @note: GXD-do-filter-1 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        phenobox = driver.find_element(By.ID, 'vocabTerm')
        # Enter your disease in the pheno box, in this case we leave the field empty to return  the entire disease list
        phenobox.send_keys("")
        time.sleep(2)
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        self.driver.find_element_by_id('doFilter').click()
        time.sleep(2)
        #capture the diseases listed in the disease filter popup list
        diseaseElts = self.driver.find_elements_by_name('doFilter')
        diseases = [e.get_attribute('value') for e in diseaseElts]            
        print(diseases)
        #assert the list returned is correct.
        self.assertEqual(diseases, ['benign neoplasm', 'cancer', 'cardiovascular system disease', 'central nervous system disease', 'chromosomal disease', 'disease by infectious agent', 'disease of mental health', 'disease of metabolism', 'endocrine system disease', 'gastrointestinal system disease', 'hematopoietic system disease', 'immune system disease', 'integumentary system disease', 'monogenic disease', 'musculoskeletal system disease', 'nervous system disease', 'peripheral nervous system disease', 'physical disorder', 'polygenic disease', 'reproductive system disease', 'respiratory system disease', 'sensory system disease', 'syndrome', 'thoracic disease', 'urinary system disease', 'bar'], 'The list is not correct')

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
        time.sleep(2)
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        self.driver.find_element_by_id('doFilter').click()
        time.sleep(2)        
        #select the filter option 'disease by infectious agent'
        self.driver.find_elements_by_name('doFilter')[5].click()
        #click the Filter button found on the filter by disease button
        self.driver.find_element_by_id('yui-gen0-button').click()
        #locate the Genes tab and click it
        self.driver.find_element_by_id('genestab').click()
        #locates the genes column and lists the genes found
        genelist = driver.find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-symbol')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        time.sleep(2)
        #assert that the genes returned are correct, should be 9 genes as of 8/29/2019
        self.assertEqual(searchTextItems, ['Ank1', 'Aqp4', 'Cebpb', 'Fcgr2b', 'Hmox1', 'Icam1', 'Ifng', 'Pklr', 'Zeb1'], 'the list of genes is not correct!')   
        
    def test_gene_tab_do_filter_no_genes(self):
        """
        @status: Tests that the Disease filter is correctly return the right genes for disease by infectious agent.
        @note: GXD-do-filter-3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.ID, 'nomenclature')
        # Enter your gene in the nomenclature box
        genebox.send_keys("Rn7sk")
        time.sleep(2)
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        self.driver.find_element_by_id('doFilter').click()
        time.sleep(2)
        eventmsg = self.driver.find_element_by_id('command').text
        print(eventmsg)
        #asserts that the event msg for no genes with ontology associations is properly displayed
        self.assertEqual(eventmsg, 'No genes found with ontology associations.', 'the no genes found text is not displaying')

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
        time.sleep(2)
        phenobox.send_keys(Keys.ENTER)
        #time.sleep(2)
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        self.driver.find_element_by_id('goMfFilter').click()
        time.sleep(2)
        #capture the molecular functions listed in the molecular function filter popup list
        molefuncElts = self.driver.find_elements_by_name('goMfFilter')
        molecular = [e.get_attribute('value') for e in molefuncElts]            
        print(molecular)
        #assert the list returned is correct.
        self.assertEqual(molecular, ['carbohydrate derivative binding', 'cytoskeletal protein binding', 'DNA binding', 'enzyme regulator', 'hydrolase', 'ligase', 'lipid binding', 'oxidoreductase', 'RNA binding', 'signaling receptor activity', 'signaling receptor binding', 'transcription', 'transferase', 'transporter', 'bar'])

    def test_gene_tab_go_molecular_filter_gene_result(self):
        """
        @status: Tests that the GO molecular filter is correctly returning the right genes for molecular function ligase.
        @note: GXD-go-molec-filter-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        phenobox = driver.find_element(By.ID, 'vocabTerm')
        # Enter your molecular function in the pheno box, (cell-cell signaling)
        phenobox.send_keys("cell-cell signaling")
        time.sleep(2)
        phenobox.send_keys(Keys.ENTER)
        #time.sleep(2)
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        self.driver.find_element_by_id('goMfFilter').click()
        time.sleep(2)        
        #select the filter option 'ligase'
        self.driver.find_elements_by_name('goMfFilter')[5].click()
        #click the Filter button found on the filter by Molecular Function button
        self.driver.find_element_by_id('yui-gen0-button').click()
        time.sleep(2)
        #locate the Genes tab and click it
        self.driver.find_element_by_id('genestab').click()
        time.sleep(2)
        #locates the genes column and lists the genes found
        genelist = driver.find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-symbol')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        time.sleep(5)
        #assert that the genes returned are correct, should be 3 genes as of 8/29/2019
        self.assertEqual(searchTextItems, ['Aacs', 'Acsl4', 'Atg7', 'Glul', 'Ifnar1', 'Kars'], 'the list of genes is not correct!')   
        
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
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        self.driver.find_element_by_id('goMfFilter').click()
        time.sleep(2)
        eventmsg = self.driver.find_element_by_id('command').text
        print(eventmsg)
        #asserts that the event msg for no genes with ontology associations is properly displayed
        self.assertEqual(eventmsg, 'No genes found with ontology associations.', 'the no genes found text is not displaying')

    def test_gene_tab_go_biological_filter_list(self):
        """
        @status: Tests that the GO biological process list used on the GXD results page Biological Process filter is correct.
        @note: GXD-go-biol-filter-1 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        phenobox = driver.find_element(By.ID, 'vocabTerm')
        # Enter your molecular finction in the pheno box, (cell-cell signaling)
        phenobox.send_keys("cell-cell signaling")
        time.sleep(2)
        phenobox.send_keys(Keys.ENTER)
        #time.sleep(2)
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        self.driver.find_element_by_id('goBpFilter').click()
        time.sleep(2)
        #capture the Biological Processes listed in the biological process filter popup list
        biologicElts = self.driver.find_elements_by_name('goBpFilter')
        biologic = [e.get_attribute('value') for e in biologicElts]            
        print(biologic)
        #assert the list returned is correct.
        self.assertEqual(biologic, ['carbohydrate derivative metabolism', 'cell death', 'cell differentiation', 'cell population proliferation', 'cellular component organization', 'establishment of localization', 'homeostatic process', 'immune system process', 'lipid metabolic process', 'nucleic acid-templated transcription', 'protein metabolic process', 'response to stimulus', 'signaling', 'system development', 'bar'])

    def test_gene_tab_go_biological_filter_gene_result(self):
        """
        @status: Tests that the GO biological process filter is correctly returning the right genes for biological process ??????.
        @note: GXD-go-biol-filter-2 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        phenobox = driver.find_element(By.ID, 'vocabTerm')
        # Enter your biological Process in the pheno box, (redox signal response)
        phenobox.send_keys("redox signal response")
        time.sleep(2)
        phenobox.send_keys(Keys.ENTER)
        #time.sleep(2)
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        self.driver.find_element_by_id('goBpFilter').click()
        time.sleep(2)        
        #select the filter option 'establishment of localization'
        self.driver.find_elements_by_name('goBpFilter')[5].click()
        #click the Filter button found on the filter by Biological Process button
        self.driver.find_element_by_id('yui-gen0-button').click()
        time.sleep(2)
        #locate the Genes tab and click it
        self.driver.find_element_by_id('genestab').click()
        time.sleep(2)
        #locates the genes column and lists the genes found
        genelist = driver.find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-symbol')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        time.sleep(2)
        #assert that the genes returned are correct, should be 7 genes as of 8/29/2019
        self.assertEqual(searchTextItems, ['Arntl', 'Clock', 'Fkbp1b', 'Ryr2', 'Selenos', 'Slc7a11', 'Smpd3'], 'the list of genes is not correct!')   
        
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
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        self.driver.find_element_by_id('goBpFilter').click()
        time.sleep(2)
        eventmsg = self.driver.find_element_by_id('command').text
        print(eventmsg)
        #asserts that the event msg for no genes with ontology associations is properly displayed
        self.assertEqual(eventmsg, 'No genes found with ontology associations.', 'the no genes found text is not displaying')

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
        #time.sleep(2)
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        self.driver.find_element_by_id('goCcFilter').click()
        time.sleep(2)
        #capture the Cellular Components listed in the cellular component filter popup list
        cellularElts = self.driver.find_elements_by_name('goCcFilter')
        cellular = [e.get_attribute('value') for e in cellularElts]            
        print(cellular)
        #assert the list returned is correct.
        self.assertEqual(cellular, ['cell projection', 'cytoplasmic vesicle', 'cytoskeleton', 'cytosol', 'endoplasmic reticulum', 'endosome', 'extracellular region', 'Golgi apparatus', 'mitochondrion', 'non-membrane-bounded organelle', 'nucleus', 'organelle envelope', 'organelle lumen', 'plasma membrane', 'synapse', 'vacuole', 'bar'])

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
        #time.sleep(2)
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        self.driver.find_element_by_id('goCcFilter').click()
        time.sleep(2)        
        #select the filter option 'vacuole'
        self.driver.find_elements_by_name('goCcFilter')[0].click()
        #click the Filter button found on the filter by Cellular Component button
        self.driver.find_element_by_id('yui-gen0-button').click()
        time.sleep(2)
        #locate the Genes tab and click it
        self.driver.find_element_by_id('genestab').click()
        time.sleep(2)
        #locates the genes column and lists the genes found
        genelist = driver.find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-symbol')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        time.sleep(2)
        #assert that the genes returned are correct, should be 2 genes as of 9/10/2019
        self.assertEqual(searchTextItems, ['Siae'], 'the list of genes is not correct!')   
        
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
        self.driver.find_element_by_id('submit1').click()
        time.sleep(2)
        self.driver.find_element_by_id('goCcFilter').click()
        time.sleep(2)
        eventmsg = self.driver.find_element_by_id('command').text
        print(eventmsg)
        #asserts that the event msg for no genes with ontology associations is properly displayed
        self.assertEqual(eventmsg, 'No genes found with ontology associations.', 'the no genes found text is not displaying')
        
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
        #find the Mutated in option, check it and use the gene Wt1
        mutate = driver.find_element(By.ID, 'mutatedIn')
        # Enter your gene
        mutate.send_keys("Wt1")
        #find the InSitu assays and Blot assays check boxes and uncheck them
        driver.find_element(By.CLASS_NAME, 'allInSitu').click()
        driver.find_element(By.ID, 'blotAll').click()
        #find the Whole Genome assays check box and click it
        driver.find_element(By.ID, 'wholeGenomeAll').click()
        #find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        #Defaults to Assays Tab so no tab click required
        #locates the Results Detail column and lists the data found
        genelist = driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-assayID')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        #assert that "data" link goes to the correct experiment page.Test result for E-MTAB-5772
        links = self.driver.find_element_by_link_text('data')
        exturl = links.get_attribute('href')
        #assert that the link url is correct
        self.assertEqual(exturl, 'https://www.ebi.ac.uk/gxa/experiments/E-MTAB-5772/Results')   
        
    def test_assay_results_tab_ref_exp_id(self):
        """
        @status: Tests that the ID link in the Reference column goes to the correct website and experiment page.
        @note: GXD-aresults-3, 4 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # Enter your gene
        genebox.send_keys("shh")
        time.sleep(2)
        #find the Mutated in option, check it and use the gene Wt1
        mutate = driver.find_element(By.ID, 'mutatedIn')
        # Enter your gene
        mutate.send_keys("Wt1")
        #find the InSitu assays and Blot assays check boxes and uncheck them
        driver.find_element(By.CLASS_NAME, 'allInSitu').click()
        driver.find_element(By.ID, 'blotAll').click()
        #find the Whole Genome assays check box and click it
        driver.find_element(By.ID, 'wholeGenomeAll').click()
        #find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        #Defaults to Assays Tab so no tab click required
        #locates the Reference column and finds the ID link to click
        genelist = driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-reference')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        #assert that ID link goes to the correct experiment page.Test result for E-MTAB-5772
        links = self.driver.find_element_by_link_text('E-MTAB-5772')
        inturl = links.get_attribute('href')
        #assert that the link url is correct
        self.assertEqual(inturl, 'http://test.informatics.jax.org/gxd/htexp_index/summary?arrayExpressID=E-MTAB-5772')           
   
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
        Select(self.driver.find_element(By.ID, 'theilerStage')).deselect_by_value('0')#deselect the default option
        Select(self.driver.find_element(By.ID, 'theilerStage')).select_by_value('28')#finds the theiler stage list and select the TS 28 option
        time.sleep(2)
        #find the InSitu assays and Blot assays check boxes and uncheck them
        driver.find_element(By.CLASS_NAME, 'allInSitu').click()
        driver.find_element(By.ID, 'blotAll').click()
        #find the Whole Genome assays check box and click it
        driver.find_element(By.ID, 'wholeGenomeAll').click()
        #find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        #Defaults to Assays Results Tab so no tab click required
        #locates the TPM Level column and finds all the data in the column?
        genelist = driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-tpmLevel')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        #assert that the TPM column results are displaying  the 4 different options
        self.assertIn('Below Cutoff', searchTextItems, 'Below Cutoff is not being found!') 
        self.assertIn('Low', searchTextItems, 'Low is not being found!')
        self.assertIn('Medium', searchTextItems, 'Medium is not being found!') 
        self.assertIn('High', searchTextItems, 'High is not being found!')         

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
        time.sleep(2)
        #find the InSitu assays and Blot assays check boxes and uncheck them
        driver.find_element(By.CLASS_NAME, 'allInSitu').click()
        driver.find_element(By.ID, 'blotAll').click()
        #find the Whole Genome assays check box and click it
        driver.find_element(By.ID, 'wholeGenomeAll').click()
        #find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        #Defaults to Assays Results Tab so no tab click required
        #click the Show/Hide Additional Sample Data box
        driver.find_element(By.ID, 'showHide').click()
        time.sleep(2)
        #locates the table column headings and verify the order of the columns
        cols = driver.find_elements_by_xpath('.//span[@class = "yui-dt-label"]')
        head = iterate.getTextAsList(cols)
        print(head)
        time.sleep(1)
        #assert that the columns are in the correct order
        self.assertEqual(head, ['Gene','Result Details','Assay Type','Age','Structure','Detected?','TPM Level\n(RNA-Seq)','Biological Replicates\n(RNA-Seq)','Images','Mutant Allele(s)','Strain','Sex','Notes\n(RNA-Seq)','Reference',''])
       
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
        #find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        #Defaults to Assays Results Tab so no tab click required
        #locates the table column headings and verify the order of the columns
        cols = driver.find_elements_by_xpath('.//span[@class = "yui-dt-label"]')
        head = iterate.getTextAsList(cols)
        print(head)
        time.sleep(1)
        #assert that the columns are in the correct order
        self.assertEqual(head, ['Gene','Result Details','Assay Type','Age','Structure','Detected?','TPM Level\n(RNA-Seq)','','Images','Mutant Allele(s)','','','','Reference',''])
        
    def test_assay_results_tab_assay_type_col_sort(self):
        """
        @status: Tests that the assay type column is sorted correctly.
        @note: GXD-aresults-9 sort order is Immunohistochemistry, RNA in situ, In situ reporter (knock in), Northern blot, Western blot, RT-PCR, RNase protection, Nuclease S, RNA-Seq
        !!!!this trest breaks! need to change TS28 to TS25 & 26 to limit results"""
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        genebox = driver.find_element(By.NAME, 'nomenclature')
        # Enter your gene
        genebox.send_keys("Afp")
        time.sleep(2)
        Select(self.driver.find_element(By.ID, 'theilerStage')).deselect_by_value('0')#deselect the default option
        Select(self.driver.find_element(By.ID, 'theilerStage')).select_by_value('28')#finds the theiler stage list and select the TS 28 option
        time.sleep(2)
        #find the Wild Type specimens only button and click it
        self.driver.find_element_by_id('isWildType').click()
        #find the Whole Genome assays check box and click it
        driver.find_element(By.ID, 'wholeGenomeAll').click()
        #find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        #Defaults to Assays Results Tab so no tab click required
        #locates the Assay Type column and finds all the data in the column?
        genelist = driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-assayType')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        #assert that the TPM column results are displaying  the 4 different options
        self.assertEqual(searchTextItems, ['Immunohistochemistry', 'Immunohistochemistry', 'Immunohistochemistry', 'Immunohistochemistry', 'Immunohistochemistry', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'RNA in situ', 'In situ reporter (knock in)', 'In situ reporter (knock in)', 'In situ reporter (knock in)', 'In situ reporter (knock in)', 'Northern blot', 'Northern blot', 'Western blot', 'Western blot', 'Western blot', 'Western blot', 'Western blot', 'Western blot', 'Western blot', 'Western blot', 'Western blot', 'Western blot', 'Western blot', 'Western blot', 'Western blot', 'Western blot', 'Western blot', 'Western blot', 'Western blot', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'RT-PCR', 'Nuclease S1', 'Nuclease S1', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq', 'RNA-Seq']) 
                         
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
        Select(self.driver.find_element(By.ID, 'theilerStage')).deselect_by_value('0')#deselect the default option
        Select(self.driver.find_element(By.ID, 'theilerStage')).select_by_value('28')#finds the theiler stage list and select the TS 28 option
        time.sleep(2)
        #find the In Situ Assays check box and unchecks it
        self.driver.find_element_by_id('inSituAll').click()
        #find the Blot Assays check box and unchecks it
        self.driver.find_element_by_id('blotAll').click()
        #find the Whole Genome assays check box and click it
        driver.find_element(By.ID, 'wholeGenomeAll').click()
        #find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        #Click the Show/Hide Additional Sample Data box to display other columns
        driver.find_element_by_id('showHide').click()
        #Defaults to Assays Results Tab so no tab click required
        #locates the Notes(RNA-Seq) column and finds all the data in the column?
        genelist = driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = genelist.find_elements(By.CLASS_NAME, 'yui-dt-col-notes')
        searchTextItems = iterate.getTextAsList(items)
        time.sleep(2)
        print(searchTextItems[0] + '  line0')
        print(searchTextItems[1] + '  line1')
        print(searchTextItems[2] + '  line2')
        print(searchTextItems[3] + '  line3')
        print(searchTextItems[4] + '  line4')
        print(searchTextItems[5] + '  line5')
        print(searchTextItems[6] + '  line6')
        print(searchTextItems[7] + '  line7')
        print(searchTextItems[8] + '  line8')
        print(searchTextItems[9] + '  line9')
        print(searchTextItems[10] + '  line10')
        print(searchTextItems[11] + '  line11')
        print(searchTextItems[12] + '  line12')
        #assert that the TPM column results are displaying  the 4 different options
        self.assertEqual(searchTextItems[6], 'Conditional mutant. day 6 of pregnancy') 
        self.assertEqual(searchTextItems[11], 'Conditional mutant. day of parturition (within 12 hours after delivery)')      
        self.assertEqual(searchTextItems[40], 'Conditional mutant.') 
        self.assertEqual(searchTextItems[42], 'Conditional mutant.')

    def test_assay_results_filter_by_exp(self):
        """
        @status: Tests that the filter by experiment option on the assays tab Assays Detail column works as expected.
        @note: GXD-aresults-11 !!broken, can't click filter icon until given an ID or class.
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/gxd")
        anat_struct = driver.find_element(By.ID, 'structure')
        # Enter your anatomical structure
        anat_struct.send_keys("liver")
        time.sleep(2)
        anat_struct.send_keys(Keys.TAB)
        time.sleep(2)
        #find the In Situ Assays check box and uncheck it
        self.driver.find_element_by_id('inSituAll').click()
        #find the Blot Assays check box and uncheck it
        self.driver.find_element_by_id('blotAll').click()
        #find the Whole Genome assays check box and check it
        driver.find_element(By.ID, 'wholeGenomeAll').click()
        #find the search button and click it
        driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        #Defaults to Assays Results Tab, so find and click the Assays tab
        #locate the Assays tab and click it
        self.driver.find_element_by_id('assaystab').click()
        time.sleep(2)
        flink = driver.find_elements_by_class_name('rsFilterLink')
        flink[0].click()
        time.sleep(4)
        #locates the Reference column and finds all the data in the column
        reflist = driver.find_element(By.ID, 'resultsdata').find_element(By.CLASS_NAME, 'yui-dt-data')
        items = reflist.find_elements(By.CLASS_NAME, 'yui-dt-col-reference')
        searchTextItems = iterate.getTextAsList(items)
        time.sleep(2)
        print(searchTextItems[2])
        #assert that the reference ID E-MTAB-599 exists in each row checked
        self.assertIn('E-GEOD-33979 Novel roles for Klf1 in regulating the erythroid transcriptome revealed by mRNA-seq', searchTextItems[1]) 
        self.assertIn('E-GEOD-45684 Transcription profiling by high throughput sequencing of a Diversity Outbred mice population and the eight founder strains: A/J, 129S1/SvImJ, C57BL/6J, NOD/ShiLtJ, NZO/HlLtJ, CAST/EiJ, PWK/PhJ, and WSB/EiJ', searchTextItems[2]) 
        self.assertIn('E-GEOD-70484 Transcription profiling by high throughput sequencing of different tissues from mouse to detect maternal or paternal allele expression biases at the tissue level', searchTextItems[3]) 
        self.assertIn('E-GEOD-72491 Transcription profiling by RNA-seq of fetal liver from poly(C) binding protein 2 (Pcbp2) knockout mice', searchTextItems[4]) 
        self.assertIn('E-GEOD-74747 RNA-seq of 9 tissues from an adult male C57BL/6 mouse', searchTextItems[5]) 
        self.assertIn('E-MTAB-599 RNA-seq of mouse DBA/2J x C57BL/6J heart, hippocampus, liver, lung, spleen and thymus', searchTextItems[6]) 
        self.assertIn('E-MTAB-2328 Transcription profiling by high throughput sequencing of liver and brain during mouse organ development', searchTextItems[7]) 
        self.assertIn('E-MTAB-2801 Strand-specific RNA-seq of nine mouse tissues', searchTextItems[8]) 
        self.assertIn('E-MTAB-3662 Pilot KOMP knockout mouse strains', searchTextItems[9]) 
    
    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'TestGXDQF.testName']
    unittest.main()                