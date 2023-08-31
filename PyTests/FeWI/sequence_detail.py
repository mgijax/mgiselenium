'''
Created on Jun 26, 2018
These tests are for verifying functionality of a Sequence Detail page
@author: jeffc
Verify that an MGP sequence detail displays the correct sequence ID and that the version  is correct
Verify that an MGI(B6) sequence detail displays the correct sequence ID and that the version is correct
Verify that an MGP sequence detail has a link to Ensembl in the ID ribbon and this link goes to the correct page
Verify that an MGP sequence detail displays the correct sequence description
Verify that an MGI sequence detail displays the correct sequence description
Verify that an MGP sequence detail displays the correct sequence provider
Verify that an MGI sequence detail displays the correct sequence provider
Verify that an MGP sequence can be downloaded for FASTA
Verify that an MGP sequence can be sent to NCBI Blast
Verify that an MGI gene model sequence can be downloaded for FASTA
Verify that an MGI gene model sequence can be sent to NCBI Blast
Verify that an MGP sequence detail displays the correct sequence base pair
Verify that an MGI sequence detail displays the correct sequence base pair
Verify that an MGP sequence detail displays the correct sequence base pair
Verify that an MGI sequence detail displays the correct sequence base pair
Verify that an MGP sequence detail displays the correct chromosome
Verify that an MGI sequence detail displays the correct chromosome
Verify that an MGP sequence detail displays the correct associated genes and markers data
Verify that an MGI sequence detail displays the correct associated genes and markers data
'''
import unittest
import time
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.form import ModuleForm
from util.table import Table
import sys,os.path
from util import wait, iterate
#from config.config import TEST_URL
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import TEST_URL

#Test
tracemalloc.start()
class TestSequenceDetail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        #self.driver.get("http://www.informatics.jax.org")
        #self.driver.get("http://bluebob.informatics.jax.org")
        self.form = ModuleForm(self.driver)
        self.driver.get(TEST_URL) 

    def test_mgp_id(self):
        """
        @status: Tests that an MGP sequence detail displays the correct sequence ID and that the version  is correct
        @note: seqdetail-id-1, 4, 5
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGP_AKRJ_G0023142')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #waits until the sequence ID table is  displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'detailStructureTable'))):
            print('sequence detail page loaded')
        #find the sequence ID in the ID/Version ribbon
        #locates the first row of the Sequence table
        seq_table = Table(self.driver.find_element(By.CLASS_NAME, "detailStructureTable"))
        cells = seq_table.get_row(0)
        print(cells.text)
        #asserts the ID ribbon data is correct
        self.assertEqual("ID/Version\nMGP_AKRJ_G0023142 (Ensembl) Multiple Genome Viewer (MGV) Version: MGP_AKRJ_G0023142.Ensembl Release 92", cells.text)
        
    def test_mgi_b6_id(self):
        """
        @status: Tests that an MGI(B6) sequence detail displays the correct sequence ID and that the version is correct
        @note: seqdetail-id-2, 4, 6
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGI_C57BL6J_5804994')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the sequence ID table is  displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'seqIdTable'))):
            print('Sequence Table loaded')
        #find the sequence ID in the ID/Version ribbon
        #locates the first row of the sequence table
        seq_table = Table(self.driver.find_element(By.ID, "seqIdTable"))
        cells = seq_table.get_row(0)
        print(cells.text)
        #asserts the ID ribbon data is correct
        self.assertEqual('MGI_C57BL6J_5804994 Multiple Genome Viewer (MGV) Version: MGI_C57BL6J_5804994.GRCm39', cells.text)          
        
    def test_mgp_ensembl_link(self):
        """
        @status: Tests that an MGP sequence detail has a link to Ensembl in the ID ribbon and this link goes to the correct page.
        @note: seqdetail-id-3
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGP_AKRJ_G0023142')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the results are  displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Ensembl'))):
            print('Ensembl link loaded')
        #locates the Ensembl link and clicks it
        self.driver.find_element(By.LINK_TEXT, 'Ensembl').click()
        page_title = self.driver.find_element(By.CLASS_NAME, 'species')
        print(page_title.text)
        #Asserts that the emsembl page is for the correct strain
        sum_head = self.driver.find_element(By.CLASS_NAME, 'summary-heading')
        print(sum_head.text)   
        self.assertEqual('Gene: Vmn2r106 MGP_AKRJ_G0023142', sum_head.text) 

    def test_mgp_seq_desc(self):
        """
        @status: Tests that an MGP sequence detail displays the correct sequence description
        @note: seqdetail-desc-1
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGP_CAROLIEiJ_G0022151')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the sequence ID table is  displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'seqIdTable'))):
            print('Sequence Table loaded')
        #find the sequence description in the sequence description ribbon
        #locates the second row of the Sequence table
        seq_table = Table(self.driver.find_element(By.CLASS_NAME, 'detailStructureTable'))
        cells = seq_table.get_cell(2, 1)
        print(cells.text)
        #asserts the sequence description ribbon data is correct
        self.assertEqual("chr18:34262022-34436126, + strand. Annotation of mouse strain CAROLI/EiJ genome assembly provided by the University of California Santa Cruz (UCSC) Genome Browser Group and the Wellcome Sanger Institute's Mouse Genomes Project (MGP). Distributed via Ensembl Release 103. Gene type: protein coding gene; Gene Name: Pcdha9.", cells.text)         

    def test_mgi_seq_desc(self):
        """
        @status: Tests that an MGI sequence detail displays the correct sequence description
        @note: seqdetail-desc-2
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGI_C57BL6J_95661')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the sequence ID table is  displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'seqIdTable'))):
            print('Sequence Table loaded')
        #find the sequence description in the sequence description ribbon
        #locates the second row of the Sequence table
        seq_table = Table(self.driver.find_element(By.CLASS_NAME, 'detailStructureTable'))
        cells = seq_table.get_cell(2, 1)
        print(cells.text)
        #asserts the sequence description ribbon data is correct
        self.assertEqual('ChrX:7825499-7844310, - strand. MGI derived this sequence for the C57BL/6J strain version of Gene: Gata1, Gene type: protein coding gene, from outermost boundary coordinates of combined annotations to mouse reference assembly GRCm39 provided by: ENSEMBL:ENSMUSG00000031162,NCBI_Gene:14460. Note that the source annotations for this representation of the C57BL/6J gene model sequence can derive from different assembly patches (J:262996).', cells.text)

    def test_mgp_seq_provider(self):
        """
        @status: Tests that an MGP sequence detail displays the correct sequence provider
        @note: seqdetail-prvder-1
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGP_CAROLIEiJ_G0022151')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the sequence ID table is  displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'seqIdTable'))):
            print('Sequence Table loaded')
        #find the sequence provider in the Provider ribbon
        #locates the third row, second cell of the Sequence table
        seq_table = Table(self.driver.find_element(By.CLASS_NAME, 'detailStructureTable'))
        cells = seq_table.get_cell(3, 1)
        print(cells.text)
        #asserts the provider ribbon data is correct
        self.assertEqual("Wellcome Sanger Institute's Mouse Genomes Project (MGP) Strain Gene Model", cells.text)         

    def test_mgi_seq_provider(self):
        """
        @status: Tests that an MGI sequence detail displays the correct sequence provider
        @note: seqdetail-prvder-2
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGI_C57BL6J_95661')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the sequence ID table is  displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'seqIdTable'))):
            print('Sequence Table loaded')
        #find the sequence provider in the Provider ribbon
        #locates the third row, second cell of the Sequence table
        seq_table = Table(self.driver.find_element(By.CLASS_NAME, 'detailStructureTable'))
        cells = seq_table.get_cell(3, 1)
        print(cells.text)
        #asserts the Provider ribbon data is correct
        self.assertEqual('MGI C57BL/6J Strain Gene Model', cells.text)         


    def test_mgp_fasta(self):
        """
        @status: Tests that an MGP sequence can be downloaded for FASTA
        @note: seqdetail-seq-1
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGP_AKRJ_G0020754')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the GO button for FASTA download is displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Go']"))):
            print('FASTA download GO button loaded')
        #find the GO button beside FASTA download and click it
        driver.find_element(By.XPATH, "//input[@value='Go']").click()
        #asserts that the correct sequence data is returned from FASTA
        assert "MGP_AKRJ_G0020754 13:94228187-94249372" in self.driver.page_source
   
    def test_mgp_ncbi_blast(self):
        """
        @status: Tests that an MGP sequence can be sent to NCBI Blast
        @note: seqdetail-seq-2
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGP_AKRJ_G0020754')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the sequence pulldown form is displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.NAME, 'seqPullDownForm'))):
            print('Sequence pull down form loaded')
        #find the sequence list and select the "forward to NCBI Blast" option
        self.driver.find_element(By.NAME, 'seqPullDownForm')
        Select(driver.find_element(By.NAME, 'seqPullDown')).select_by_visible_text('forward to NCBI BLAST')
        # waits until the GO button for forward to NCBI Blast is displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Go']"))):
            print('forward to NCBI Blast GO button loaded')
        #find the GO button beside FASTA download and click it
        driver.find_element(By.XPATH, "//input[@value='Go']").click()
        #asserts that the correct blast page is returned by NCBI
        #switch focus to the new tab for strain detail page
        driver.switch_to.window(self.driver.window_handles[-1])
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'pageTitle'))):
            print('forward to NCBI Blast page loaded')
        #Identify the page title
        page_header = self.driver.find_element(By.CLASS_NAME, 'pageTitle')
        #asserts that the Page header is correct
        self.assertEqual('Standard Nucleotide BLAST', page_header.text)

    def test_mgi_gm_fasta(self):
        """
        @status: Tests that an MGI gene model sequence can be downloaded for FASTA
        @note: seqdetail-seq-3
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGI_C57BL6J_98660')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the GO button for FASTA download is displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Go']"))):
            print('forward to NCBI Blast GO button loaded')
        #find the GO button beside FASTA download and click it
        driver.find_element(By.XPATH, "//input[@value='Go']").click()
        #asserts that the correct sequence data is returned from FASTA
        assert "MGI_C57BL6J_98660 Y:2662471-2663658" in self.driver.page_source 

    def test_mgi_gm_ncbi_blast(self):
        """
        @status: Tests that an MGI gene model sequence can be sent to NCBI Blast
        @note: seqdetail-seq-4
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGI_C57BL6J_98660')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the sequence pulldown form is displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.NAME, 'seqPullDownForm'))):
            print('Sequence pull down form loaded')
        #find the sequence list and select the "forward to NCBI Blast" option
        self.driver.find_element(By.NAME, 'seqPullDownForm')
        Select(driver.find_element(By.NAME, 'seqPullDown')).select_by_visible_text('forward to NCBI BLAST')
        # waits until the GO button for forward to NCBI Blast is displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Go']"))):
            print('forward to NCBI Blast GO button loaded')
        #find the GO button beside FASTA download and click it
        driver.find_element(By.XPATH, "//input[@value='Go']").click()
        #asserts that the correct blast page is returned by NCBI
        #switch focus to the new tab for strain detail page
        driver.switch_to.window(self.driver.window_handles[-1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'pageTitle'))):
            print('forward to NCBI Blast page loaded')
        #Identify the page title
        page_header = self.driver.find_element(By.CLASS_NAME, 'pageTitle')
        #asserts that the Page header is correct
        self.assertEqual('Standard Nucleotide BLAST', page_header.text)

    def test_mgp_seq_bp(self):
        """
        @status: Tests that an MGP sequence detail displays the correct sequence base pair
        @note: seqdetail-seq-5
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGP_CAROLIEiJ_G0022151')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the sequence ID table is  displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'seqIdTable'))):
            print('Sequence Table loaded')
        #find the sequence in the Sequence ribbon
        #locates the fourth row, second cell of the Sequence table
        seq_info = self.driver.find_element(By.CSS_SELECTOR, '.detailStructureTable > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > div:nth-child(1)')
        print(seq_info.text)
        #asserts the Sequence ribbon data is correct
        self.assertTrue(seq_info.text, 'DNA 174105 bp')         

    def test_mgi_seq_bp(self):
        """
        @status: Tests that an MGI sequence detail displays the correct sequence base pair
        @note: seqdetail-seq-6
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGI_C57BL6J_98660')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the sequence ID table is  displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'seqIdTable'))):
            print('Sequence Table loaded')
        #find the sequence in the Sequence ribbon
        #locates the fourth row, second cell of the Sequence table
        seq_table = Table(self.driver.find_element(By.CLASS_NAME, 'detailStructureTable'))
        cells = seq_table.get_cell(4, 1)
        print(cells.text)
        #asserts the Sequence ribbon data is correct
        self.assertIn('DNA 1188 bp', cells.text)         

    def test_mgp_source_data(self):
        """
        @status: Tests that an MGP sequence detail displays the correct sequence base pair
        @note: seqdetail-source-1
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGP_CASTEiJ_G0006926')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence')))#waits until the results are displayed on the page
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the source table is displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'sourceTable'))):
            print('Source Table loaded')
        #find the source data in the Source ribbon
        #locates the Source table
        src_table = Table(self.driver.find_element(By.ID, 'sourceTable'))
        #find the source name cell, print it and assert it to be correct
        cell1 = src_table.get_cell(1, 1)
        print(cell1.text)
        self.assertIn('Sequenced Mouse Inbred Strain Genome Meta-data', cell1.text)          
        #find the organism cell, print it and assert it to be correct
        cell2 = src_table.get_cell(2, 1)
        print(cell2.text)
        self.assertIn('mouse', cell2.text)
        #find the Strain/Species cell, print it and assert it to be correct
        cell3 = src_table.get_cell(3, 1)
        print(cell3.text)
        self.assertIn('CAST/EiJ', cell3.text)   
        #find the sex cell, print it and assert it to be correct
        cell4 = src_table.get_cell(4, 1)
        print(cell4.text)
        self.assertIn('Not Applicable', cell4.text)  
        #locates the Inner Source table
        in_src_table = Table(self.driver.find_element(By.ID, 'sourceTableInner2'))
        #find the Age cell, print it and assert it to be correct
        cell5 = in_src_table.get_cell(0, 1)
        print(cell5.text)
        self.assertIn('Not Specified', cell5.text)          
        #find the Tissue cell, print it and assert it to be correct
        cell6 = in_src_table.get_cell(1, 1)
        print(cell6.text)
        self.assertIn('Not Specified', cell6.text)
        #find the Cell Line cell, print it and assert it to be correct
        cell7 = in_src_table.get_cell(2, 1)
        print(cell7.text)
        self.assertIn('Not Applicable', cell7.text)    
              

    def test_mgi_source_data(self):
        """
        @status: Tests that an MGI sequence detail displays the correct sequence base pair
        @note: seqdetail-source-2
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGI_C57BL6J_98660')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the source table is displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'sourceTable'))):
            print('Source Table loaded')
        #find the source data in the Source ribbon
        #locates the Source table
        src_table = Table(self.driver.find_element(By.ID, 'sourceTable'))
        #find the source name cell, print it and assert it to be correct
        cell1 = src_table.get_cell(1, 1)
        print(cell1.text)
        self.assertIn('Sequenced Mouse Strain C57BL/6J Genome Meta-data', cell1.text)          
        #find the organism cell, print it and assert it to be correct
        cell2 = src_table.get_cell(2, 1)
        print(cell2.text)
        self.assertIn('mouse', cell2.text)
        #find the Strain/Species cell, print it and assert it to be correct
        cell3 = src_table.get_cell(3, 1)
        print(cell3.text)
        self.assertIn('C57BL/6J', cell3.text)   
        #find the sex cell, print it and assert it to be correct
        cell4 = src_table.get_cell(4, 1)
        print(cell4.text)
        self.assertIn('Not Applicable', cell4.text)  
        #locates the Inner Source table
        in_src_table = Table(self.driver.find_element(By.ID, 'sourceTableInner2'))
        #find the Age cell, print it and assert it to be correct
        cell5 = in_src_table.get_cell(0, 1)
        print(cell5.text)
        self.assertIn('Not Specified', cell5.text)          
        #find the Tissue cell, print it and assert it to be correct
        cell6 = in_src_table.get_cell(1, 1)
        print(cell6.text)
        self.assertIn('Not Specified', cell6.text)
        #find the Cell Line cell, print it and assert it to be correct
        cell7 = in_src_table.get_cell(2, 1)
        print(cell7.text)
        self.assertIn('Not Applicable', cell7.text)     

    def test_mgp_chr_data(self):
        """
        @status: Tests that an MGP sequence detail displays the correct chromosome
        @note: seqdetail-chr-1
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGP_CASTEiJ_G0006926')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the sequence ID table is  displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'seqIdTable'))):
            print('Sequence Table loaded')
        #find the chromosome data in the Chromosome ribbon
        chromo = self.driver.find_element(By.CSS_SELECTOR, '.detailStructureTable > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2)')
        print(chromo.text)
        self.assertEqual('6', chromo.text)

    def test_mgi_chr_data(self):
        """
        @status: Tests that an MGI sequence detail displays the correct chromosome
        @note: seqdetail-chr-2
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGI_C57BL6J_98660')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the sequence ID table is  displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'seqIdTable'))):
            print('Sequence Table loaded')
        #find the chromosome data in the Chromosome ribbon
        chromo = self.driver.find_element(By.CSS_SELECTOR, '.detailStructureTable > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2)')
        print(chromo.text)
        self.assertEqual('Y', chromo.text)

    def test_mgp_assoc_gene(self):
        """
        @status: Tests that an MGP sequence detail displays the correct associated genes and markers data
        @note: seqdetail-assoc-gene-1
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGP_CASTEiJ_G0006926')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the Annotated genes and markers table is displayed on the page
        if WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'markerTable'))):
            print('annotated genes and markers table displayed')
        #locates the Source table
        mrk_table = Table(self.driver.find_element(By.ID, 'markerTable'))
        #find the Type cell, print it and assert it to be correct
        cell1 = mrk_table.get_cell(1, 0)
        print(cell1.text)
        self.assertIn('Gene', cell1.text)     
        #find the Symbol cell, print it and assert it to be correct
        cell1 = mrk_table.get_cell(1, 1)
        print(cell1.text)
        self.assertIn('Gm17216', cell1.text) 
        #find the Name cell, print it and assert it to be correct
        cell1 = mrk_table.get_cell(1, 2)
        print(cell1.text)
        self.assertIn('predicted gene 17216', cell1.text) 
        #find the GO Terms cell, print it and assert it to be correct
        cell1 = mrk_table.get_cell(1, 3)
        print(cell1.text)
        self.assertIn('0', cell1.text) 
        #find the Expression Assays cell, print it and assert it to be correct
        cell1 = mrk_table.get_cell(1, 4)
        print(cell1.text)
        self.assertIn('96', cell1.text) 
        #find the Orthologs cell, print it and assert it to be correct
        cell1 = mrk_table.get_cell(1, 5)
        print(cell1.text)
        self.assertIn('0', cell1.text) 
        #find the Phenotypic Alleles cell, print it and assert it to be correct
        cell1 = mrk_table.get_cell(1, 6)
        print(cell1.text)
        self.assertIn('0', cell1.text) 

    def test_mgi_assoc_gene(self):
        """
        @status: Tests that an MGI sequence detail displays the correct associated genes and markers data
        @note: seqdetail-cassoc-gene-2
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('MGI_C57BL6J_98660')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.find_element(By.ID, 'oLink').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence'))):
            print('Sequence link loaded')
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sequence')))#waits until the results are displayed on the page
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        #switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # waits until the Annotated genes and markers table is displayed on the page
        if WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'markerTable'))):
            print('annotated genes and markers table displayed')
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'markerTable')))#waits until the source table is displayed on the page
        #locates the Source table
        mrk_table = Table(self.driver.find_element(By.ID, 'markerTable'))
        #find the Type cell, print it and assert it to be correct
        cell1 = mrk_table.get_cell(1, 0)
        print(cell1.text)
        self.assertIn('Gene', cell1.text)     
        #find the Symbol cell, print it and assert it to be correct
        cell1 = mrk_table.get_cell(1, 1)
        print(cell1.text)
        self.assertIn('Sry', cell1.text) 
        #find the Name cell, print it and assert it to be correct
        cell1 = mrk_table.get_cell(1, 2)
        print(cell1.text)
        self.assertIn('sex determining region of Chr Y', cell1.text) 
        #find the GO Terms cell, print it and assert it to be correct
        cell1 = mrk_table.get_cell(1, 3)
        print(cell1.text)
        self.assertIn('38', cell1.text)
        #find the Expression Assays cell, print it and assert it to be correct
        cell1 = mrk_table.get_cell(1, 4)
        print(cell1.text)
        self.assertIn('196', cell1.text)
        #find the Orthologs cell, print it and assert it to be correct
        cell1 = mrk_table.get_cell(1, 5)
        print(cell1.text)
        self.assertIn('3', cell1.text) 
        #find the Phenotypic Alleles cell, print it and assert it to be correct
        cell1 = mrk_table.get_cell(1, 6)
        print(cell1.text)
        self.assertIn('41', cell1.text) 
        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSequenceDetail))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))