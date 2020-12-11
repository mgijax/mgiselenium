'''
Created on Sep 14, 2016
This test is for searches using the quick search feature of the WI
@author: jeffc

'''

import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util import wait, iterate
from util.table import Table
#from config.config import TEST_URL
# adjust the path to find config
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)

import config
#from config import TEST_URL

class TestSearchTool(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.get("http://www.informatics.jax.org")
        #self.driver.get("http://bluebob.informatics.jax.org")
        self.driver.get(config.TEST_URL) 
        #print (config)

    def test_gene_id(self):
        """
        @status: Tests that a Gene ID-primary search brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("MGI:87895")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        #time.sleep(2)
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)

        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI:87895')
        #wait.forAjax(driver)
        
    def test_ref_id(self):
        """
        @status: Tests that a Reference ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Reference ID in the quick search box
        searchbox.send_keys("J:14135")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page
        #find the results(this case third table) table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Reference: J:14135')       
        

    def test_go_id(self):
        """
        @status: Tests that an GO ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your GO ID in the quick search box
        searchbox.send_keys("GO:0005892")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b2Table')))#waits until the results are displayed on the page
        #find the results table
        #time.sleep(2)
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: GO:0005892')
        

    def test_old_gene_id(self):
        """
        @status: Tests that an Old Gene ID-secondary search brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Old Gene ID in the quick search box
        searchbox.send_keys("MGD-MRK-1672")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'MGI: MGD-MRK-1672')    

    def test_genetrap_id(self):
        """
        @status: Tests that a Gene Trap ID search brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene Trap ID in the quick search box
        searchbox.send_keys("FHCRC-GT-S15-11C1")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence: FHCRC-GT-S15-11C1')    
        
        
    def test_gene_assay_id(self):
        """
        @status: Tests that a Gene Assay ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene Assay ID in the quick search box
        searchbox.send_keys("MGI:1339505")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Assay: MGI:1339505') 

    def test_entrezgene_id(self):
        """
        @status: Tests that an Entrezgene(NCBI) ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your EntrezGene(NCBI) ID in the quick search box
        searchbox.send_keys("11539")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Entrez Gene: 11539') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[2].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[2].text, 'Sequence: 11539') 

    def test_ncbi_id(self):
        """
        @status: Tests that a NCBI ID brings back the proper information
        @bug: sort is different each time on new QS
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCBI ID in the quick search box
        searchbox.send_keys("20423")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        print(all_cells[5].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'HomoloGene: 20423')
        self.assertEqual(all_cells[2].text, 'Entrez Gene: 20423')
        self.assertEqual(all_cells[3].text, 'Name: CpG island 20423')
        self.assertEqual(all_cells[4].text, 'Name: predicted gene 20423')
        self.assertEqual(all_cells[5].text, 'Name: transcription start site region 20423')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        print(all_cells[3].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Reference: J:20423')
        self.assertEqual(all_cells[2].text, 'Homology Class: 20423') 
        self.assertEqual(all_cells[3].text, 'Sequence: 20423')
                
    def test_ensembl_id(self):
        """
        @status: Tests that an Ensembl Gene Model ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Ensembl ID in the quick search box
        searchbox.send_keys("ENSMUSG00000005672")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Ensembl Gene Model: ENSMUSG00000005672') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence: ENSMUSG00000005672') 

    def test_ensembl_t_id(self):
        """
        @status: Tests that an Ensembl Transcript ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Ensembl ID in the quick search box
        searchbox.send_keys("ENSMUST00000033380")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Ensembl Transcript: ENSMUST00000033380') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence: ENSMUST00000033380')         

    def test_ensembl_p_id(self):
        """
        @status: Tests that an Ensembl Protein ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Ensembl ID in the quick search box
        searchbox.send_keys("ENSMUSP00000102131")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Ensembl Protein: ENSMUSP00000102131') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence: ENSMUSP00000102131')   

    def test_refseq_p_id(self):
        """
        @status: Tests that a RefSeq-primary ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your RegSeq ID in the quick search box
        searchbox.send_keys("NM_023876")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'RefSeq: NM_023876') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence: NM_023876')

    def test_refseq_s_id(self):
        """
        @status: Tests that a RefSeq-secondary ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your RegSeq ID in the quick search box
        searchbox.send_keys("XP_001477707")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'RefSeq: XP_001477707') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence: NP_937813')

    def test_SeqDB_p_id(self):
        '''
        @status: Tests that a Sequence DB primary ID brings back the proper information
        '''
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your RegSeq ID in the quick search box
        searchbox.send_keys("AK145957")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence DB: AK145957') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence: AK145957')

    def test_SeqDB_s_id(self):
        '''
        @status: Tests that a Sequence DB secondary ID brings back the proper information
        '''
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your RegSeq ID in the quick search box
        searchbox.send_keys("D87828")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence DB: D87828') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence: D87831')        

    """def test_unigene_id(self):
        
        @status: Tests that an Ensembl ID brings back the proper information
        @attention: Unigene has been retired!!!
        
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your UniGene ID in the quick search box
        searchbox.send_keys("181490")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[0].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : 181490 (UniGene)   and more detail...')
        wait.forAjax(driver) 
        """
        
    def test_swissprot_p_id(self):
        """
        @status: Tests that an swissprot primary ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your UniProt ID in the quick search box
        searchbox.send_keys("Q9ER73")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'SWISS-PROT: Q9ER73') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence: Q9ER73')
        
    def test_swissprot_s_id(self):
        """
        @status: Tests that an swissprot secondary ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your UniProt ID in the quick search box
        searchbox.send_keys("Q91YT1")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'SWISS-PROT: Q91YT1') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence: Q3UPH1')
        
    def test_trembl_p_id(self):
        """
        @status: Tests that an trembl primary ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your UniProt ID in the quick search box
        searchbox.send_keys("B8JK67")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'TrEMBL: B8JK67') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence: B8JK67')
                
    def test_homologene_id(self):
        """
        @status: Tests that an HomoloGene ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your HomoloGene ID in the quick search box
        searchbox.send_keys("20151")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'HomoloGene: 20151') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[2].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[2].text, 'Homology Class: 20151')
 
    def test_consensus_CDS_id(self):
        """
        @status: Tests that a Consensus CDS Project ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your HomoloGene ID in the quick search box
        searchbox.send_keys("CCDS28624.1")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Consensus CDS Project: CCDS28624.1') 

    def test_Unigene_id(self):
        """
        @status: Tests that an UniGene ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your HomoloGene ID in the quick search box
        searchbox.send_keys("8122")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'UniGene: 8122') 
        self.assertEqual(all_cells[2].text, 'HomoloGene: 8122') 
        self.assertEqual(all_cells[3].text, 'Name: CpG island 8122') 
        self.assertEqual(all_cells[4].text, 'Name: predicted gene 8122') 
        self.assertEqual(all_cells[5].text, 'Name: transcription start site region 8122') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[2].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Reference: J:8122')
        self.assertEqual(all_cells[2].text, 'Homology Class: 8122') 

    def test_protein_ont_id(self):
        """
        @status: Tests that an Protein Ontology ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your HomoloGene ID in the quick search box
        searchbox.send_keys("PR:000008517")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Protein Ontology: PR:000008517') 

    def test_ec_id(self):
        """
        @status: Tests that a EC ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your EC ID in the quick search box
        searchbox.send_keys("3.4.21.6")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'EC: 3.4.21.6')

    def test_pdb_id(self):
        """
        @status: Tests that a PDB ID brings back the proper information
        @attention: does not now identify it's a pdb ID
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your PDB ID in the quick search box
        searchbox.send_keys("1HU8")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'PDB: 1HU8') 
        
    def test_mirbase_id(self):
        """
        @status: Tests that a miRBase ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your mirBasee ID in the quick search box
        searchbox.send_keys("MI0000248")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'miRBase: MI0000248')        
        
    def test_qtl_archive_id(self):
        """
        @status: Tests that a QTL Archive ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your PDB ID in the quick search box
        searchbox.send_keys("Brich1")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Download data from the QTL Archive: Brich1') 

    def test_ncbi_gme_id(self):
        """
        @status: Tests that an NCBI Gene Model Evidence ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your HomoloGene ID in the quick search box
        searchbox.send_keys("NT_187055")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'NCBI Gene Model Evidence: NT_187055') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[2].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[2].text, 'Sequence: NT_187055')

    def test_affy1_st_id(self):
        """
        @status: Tests that an Affy 1.0 ST ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your HomoloGene ID in the quick search box
        searchbox.send_keys("10388707")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Affy 1.0 ST: 10388707') 

    def test_affy430_2_id(self):
        """
        @status: Tests that an Affy 430 2.0 ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your HomoloGene ID in the quick search box
        searchbox.send_keys("1416346_at")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Affy 430 2.0: 1416346_at') 
 
    def test_affy_U74_id(self):
        """
        @status: Tests that an Affy U74 ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your HomoloGene ID in the quick search box
        searchbox.send_keys("107044_at")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Affy U74: 107044_at') 
                        
    def test_omim_id(self):
        """
        @status: Tests that an OMIM ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your OMIM ID in the quick search box
        searchbox.send_keys("OMIM:168600")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b2Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'OMIM: OMIM:168600') 
        #find the results table
        #results_table = self.driver.find_element(By.ID, 'b3Table')
        #table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        #all_cells = table.get_column_cells('Why did this match?')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        #self.assertEqual(all_cells[1].text, 'OMIM:: OMIM:168600')

    def test_omim_id_no_pre(self):
        """
        @status: Tests that an OMIM ID without the prefix of OMIM: brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your OMIM ID in the quick search box
        searchbox.send_keys("168600")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b2Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'OMIM: 168600') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Reference: J:168600')
        
    def test_omim_gene_id(self):
        """
        @status: Tests that an OMIM ID for a gene(human) brings back the proper information
        @attention: Does not work in new quick search. bug?
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your OMIM ID in the quick search box
        searchbox.send_keys("OMIM:191170")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        wait.forAjax(driver)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID : OMIM:191170 (OMIM - Human)')
        wait.forAjax(driver) 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID : OMIM:191170 (OMIM - Human)')
        

    def test_omim_gene_id_no_pre(self):
        """
        @status: Tests that an OMIM ID for a gene(human) without the prefix of OMIM: brings back the proper information
        @attention: does not work in new quick search Bug?
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your OMIM ID in the quick search box
        searchbox.send_keys("191170")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[2].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : 191170 (OMIM - Human)')
        wait.forAjax(driver)                 

    def test_hgnc_id(self):
        """
        @status: Tests that an HGNC ID brings back the proper information
        @attention: not working in new quick search.
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your HGNC ID in the quick search box
        searchbox.send_keys("HGNC:28837")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[0].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : HGNC:28837 (HGNC - Human)   and more detail...')
        wait.forAjax(driver) 


    def test_atcc_clone_id(self):
        """
        @status: Tests that an ATCC clone ID brings back the proper information
        @attention: Not working in new quick search 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your ATCC clone ID in the quick search box
        searchbox.send_keys("719230")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[2].find_elements(By.CLASS_NAME, 'qsBucketRow1')[1].find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : 719230 (ATCC)') 

    def test_image_clone_id(self):
        """
        @status: Tests that an Image clone ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Image clone ID in the quick search box
        searchbox.send_keys("MGI:200469")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first 2 rows of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        print(all_cells[2].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Probe/Clone: MGI:200469') 
        self.assertEqual(all_cells[2].text, 'Sequence: W09270')

    def test_mgc_id(self):
        """
        @status: Tests that an MGC ID brings back the proper information
        @note: does not tell you the ID is MGC
        @attention: Not finding  probe/clone or RNA sequences in bucket 3 of new quick search
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your MGC ID in the quick search box
        searchbox.send_keys("14049")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: 14049') 
        self.assertEqual(all_cells[2].text, 'Sequence: W09270')
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first 3 rows of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        print(all_cells[2].text)
        print(all_cells[3].text)
        print(all_cells[4].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Probe/Clone: MGI:200469') 
        self.assertEqual(all_cells[2].text, 'Sequence: 14049')
        self.assertEqual(all_cells[3].text, 'Sequence: 14049')
        self.assertEqual(all_cells[4].text, 'Sequence: 14049')

    def test_riken_clone_id(self):
        """
        @status: Tests that a RIKEN clone ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your RIKEN clone ID in the quick search box
        searchbox.send_keys("MGI:2420147")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Probe/Clone: MGI:2420147')

    def test_rpci_id(self):
        """
        @status: Tests that an RPCI ID brings back the proper information
        @attention: not working correctly in new quick search
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your RPCI ID in the quick search box
        searchbox.send_keys("RP23-100A23")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page)
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[2].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : RP23-100A23 (RPCI-23)')
        wait.forAjax(driver) 

    def test_interpro_id(self):
        """
        @status: Tests that an Interpro ID brings back the proper information 
        @note: 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your InterPro ID in the quick search box
        searchbox.send_keys("IPR003599")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, "Protein Domain: Immunoglobulin subtype (IPR003599)") 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'InterPro: IPR003599') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'InterPro Domains: IPR003599')

    def test_pirsf_id(self):
        """
        @status: Tests that a PIRSF ID brings back the proper information
        @attention: new quick search not bringing back the protein coding genes in table 1
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your PIRSF ID in the quick search box
        searchbox.send_keys("PIRSF038195")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        print(all_cells[2].text)
        print(all_cells[3].text)
        print(all_cells[4].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: PIRSF038195') 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: PIRSF038195') 

    def test_pubmed_id(self):
        """
        @status: Tests that a PubMed ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your PubMed ID in the quick search box
        searchbox.send_keys("8825637")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Reference: J:30580') 

    def test_mgi_reference_id(self):
        """
        @status: Tests that an MGI Reference ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your MGI Reference ID in the quick search box
        searchbox.send_keys("MGI:3716133")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Reference: J:122989') 

    def test_dbsnp_id(self):
        """
        @status: Tests that a dbSNP ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your dbSNP ID in the quick search box
        searchbox.send_keys("rs3021544")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'SNP: rs3021544') 

    def test_genbank_id(self):
        """
        @status: Tests that a GenBank ID brings back the proper information
        @attention: new QS brings back 2 sequence details but why match is first ID not one searched for.
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Genbank ID in the quick search box
        searchbox.send_keys("S40294")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: S40294')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'protein coding gene: MGI:96677') 

    def test_allele_id(self):
        """
        @status: Tests that an allele ID(knockout) brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Allele ID in the quick search box
        searchbox.send_keys("MGI:2156651")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b1Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI:2156651')

    def test_escellline_igtc_id(self):
        """
        @status: Tests that an ES Cell Line ID(IGTC) brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your ES Cell Line ID in the quick search box
        searchbox.send_keys("BGB069")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Name: gene trap BGB069, BayGenomics')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence: BGB069')

    def test_escellline_lexicon_id(self):
        """
        @status: Tests that an ES Cell Line ID(Lexicon) brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your ES Cell Line ID in the quick search box
        searchbox.send_keys("OST2298")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Symbol: Slc9a3r2Gt(OST2298)Lex')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence: OST2298')

    def test_probe_id(self):
        """
        @status: Tests that a Probe ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Probe ID in the quick search box
        searchbox.send_keys("MGI:10980")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Probe/Clone: MGI:10980')
        
    def test_mgc_clone_id(self):
        """
        @status: Tests that an MGC Clone ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your MGC clone ID in the quick search box
        searchbox.send_keys("MGI:1414340")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        print(all_cells[1].text)
        print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Probe/Clone: MGI:1414340')
        self.assertEqual(all_cells[2].text, 'Sequence: BC005448')
        self.assertEqual(all_cells[3].text, 'Sequence: BE380449')

    def test_map_exp_id(self):
        """
        @status: Tests that a Mapping Experiment ID brings back the proper information
        @attention: Not working in new quick search!
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Mapping Experiment ID in the quick search box
        searchbox.send_keys("MGD-CREX-2835")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[2].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : MGD-CREX-2835')
        wait.forAjax(driver) 

    def test_mouse_anat_id(self):
        """
        @status: Tests that an Adult Mouse Anatomy ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Adult Mouse Anatomy ID in the quick search box
        searchbox.send_keys("MA:0000168")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MA:0000168')

    def test_mp_id(self):
        """
        @status: Tests that an MP ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your MP ID in the quick search box
        searchbox.send_keys("MP:0002089")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b2Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the first row of data to find the best match column of the table
        all_cells = table.get_column_cells('Best match')
        print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Mammalian Phenotype: MP:0002089')

    def test_antibody_id(self):
        """
        @status: Tests that an Antibody ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Antibody ID in the quick search box
        searchbox.send_keys("MGI:4438078")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Antibody: MGI:4438078')

    def test_proteoform_id(self):
        """
        @status: Tests that a Proteoform ID brings back the proper information
        @attention: new QS this test is broken.
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Proteoform ID in the quick search box
        searchbox.send_keys("PR:Q80YE4-2")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'PR:: PR:Q80YE4-2') 
        
    def test_do_id(self):
        """
        @status: Tests that a Disease Ontology ID brings back the proper information
        @attention: data is different from old QS form
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Proteoform ID in the quick search box
        searchbox.send_keys("DOID:1700")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b2Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Disease Ontology: DOID:1700')
        

    def test_strain_id(self):
        """
        @status: Tests that a Strain ID search brings back the proper information
        @note: Strain-qs-id-1 
        @attention: has result in different bucket than old QS form.
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Strain ID in the quick search box
        searchbox.send_keys("MGI:2159854")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Strain: MGI:2159854')

    def test_strain_alt_id(self):
        """
        @status: Tests that a Strain Alternate ID search brings back the proper information
         @note: Strain-qs-id-2
         @attention: not working yet in new quick search form
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Strain ID in the quick search box
        searchbox.send_keys("MGI:2164529")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : MGI:2164529')
        wait.forAjax(driver)

    def test_strain_jax_id(self):
        """
        @status: Tests that a JAX ID search brings back the proper information
         @note: Strain-qs-id-3
         @attention: does not work yet in new quick search page
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your JAX ID in the quick search box
        searchbox.send_keys("000651")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : 000651')
        wait.forAjax(driver)

    def test_strain_mmrrc_id(self):
        """
        @status: Tests that a MMRCC ID search brings back the proper information
         @note: Strain-qs-id-4
         @attention: does not work in new quick search page
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Strain ID in the quick search box
        searchbox.send_keys("mmrrc:029868")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : MMRRC:029868')
        wait.forAjax(driver)

    def test_strain_apb_id(self):
        """
        @status: Tests that a APB ID search brings back the proper information
         @note: Strain-qs-id-5
         @attention: does not work yet on new quick search page
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your APB ID in the quick search box
        searchbox.send_keys("APB:629")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : APB:629')
        wait.forAjax(driver)

    def test_strain_arc_id(self):
        """
        @status: Tests that a ARC ID search brings back the proper information
         @note: Strain-qs-id-6
         @attention: does not work yet on new quick search page
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your ARC ID in the quick search box
        searchbox.send_keys("ARC:B6")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : ARC:B6')
        wait.forAjax(driver)

    def test_strain_card_id(self):
        """
        @status: Tests that a CARD ID search brings back the proper information
         @note: Strain-qs-id-8
         @attention: does not work yet on new quick search page
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your CARD ID in the quick search box
        searchbox.send_keys("242")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : 242')
        wait.forAjax(driver)

    def test_strain_cmmr_id(self):
        """
        @status: Tests that a CMMR ID search brings back the proper information
         @note: Strain-qs-id-10
         @attention: does not work yet on new quick search page
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your CMMR ID in the quick search box
        searchbox.send_keys("0076")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : 0076')
        wait.forAjax(driver)

    def test_strain_emma_id(self):
        """
        @status: Tests that a EMMA ID search brings back the proper information
         @note: Strain-qs-id-12
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your EMMA ID in the quick search box
        searchbox.send_keys("EM:05001")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : EM:05001')
        wait.forAjax(driver)

    def test_strain_ems_id(self):
        """
        @status: Tests that a EMS ID search brings back the proper information
         @note: Strain-qs-id-13
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your EMS ID in the quick search box
        searchbox.send_keys("pacEMS1D")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : pacEMS1D')
        wait.forAjax(driver)

    def test_strain_harwell_id(self):
        """
        @status: Tests that a Harwell ID search brings back the proper information
         @note: Strain-qs-id-15
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Harwell ID in the quick search box
        searchbox.send_keys("FESA:03299")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : FESA:03299')
        wait.forAjax(driver)

    def test_strain_jpga_id(self):
        """
        @status: Tests that a JPGA ID search brings back the proper information
         @note: Strain-qs-id-16
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your JPGA ID in the quick search box
        searchbox.send_keys("11473")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : 11473')
        wait.forAjax(driver)

    def test_strain_ncimr_id(self):
        """
        @status: Tests that a NCIMR ID search brings back the proper information
         @note: Strain-qs-id-19
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("01XH9")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : 01XH9')
        wait.forAjax(driver)

    def test_strain_mpd_id(self):
        """
        @status: Tests that a MPD ID search brings back the proper information
         @note: Strain-qs-id-20
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your MPD ID in the quick search box
        searchbox.send_keys("3")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : 3')
        wait.forAjax(driver)

    def test_strain_mugen_id(self):
        """
        @status: Tests that a MUGEN ID search brings back the proper information
         @note: Strain-qs-id-22
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your MUGEN ID in the quick search box
        searchbox.send_keys("M193046")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : M193046')
        wait.forAjax(driver)

    def test_strain_nig_id(self):
        """
        @status: Tests that a NIG ID search brings back the proper information
         @note: Strain-qs-id-23
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NIG ID in the quick search box
        searchbox.send_keys("229")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : 229')
        wait.forAjax(driver)

    def test_strain_nmice_id(self):
        """
        @status: Tests that a NMICE ID search brings back the proper information
         @note: Strain-qs-id-24
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NMICE ID in the quick search box
        searchbox.send_keys("MGI:1861634")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : MGI:1861634')
        wait.forAjax(driver)

    def test_strain_obs_id(self):
        """
        @status: Tests that a OBS ID search brings back the proper information
         @note: Strain-qs-id-25
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your OBS ID in the quick search box
        searchbox.send_keys("OBS:27")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : OBS:27')
        wait.forAjax(driver)

    def test_strain_ornl_id(self):
        """
        @status: Tests that a ORNL ID search brings back the proper information
         @note: Strain-qs-id-26
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your OBS ID in the quick search box
        searchbox.send_keys("ORNL:47BS")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : ORNL:47BS')
        wait.forAjax(driver)

    def test_strain_riken_brc_id(self):
        """
        @status: Tests that a RIKEN BRC ID search brings back the proper information
         @note: Strain-qs-id-27
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your RIKEN BRC ID in the quick search box
        searchbox.send_keys("RBRC00222")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : RBRC00222')
        wait.forAjax(driver)

    def test_strain_tac_id(self):
        """
        @status: Tests that a TAC ID search brings back the proper information
         @note: Strain-qs-id-29 can also use the ID 1334
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your TAC ID in the quick search box
        searchbox.send_keys("TAC:rag2")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : TAC:rag2')
        wait.forAjax(driver)

    def test_strain_rmrc_nlac_id(self):
        """
        @status: Tests that a RMRC NLAC ID search brings back the proper information
         @note: Strain-qs-id-31 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your RMRC-NLAC ID in the quick search box
        searchbox.send_keys("RMRC11005")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : RMRC11005')
        wait.forAjax(driver)

    def test_strain_name(self):
        """
        @status: Tests that a strain name search brings back the proper information
         @note: Strain-qs-name-1 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your strain name in the quick search box
        searchbox.send_keys("CD-1/crl")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'Name : Crl:CD-1')
        wait.forAjax(driver)

    def test_strain_syn(self):
        """
        @status: Tests that a strain synonym search brings back the proper information
         @note: Strain-qs-name-2 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your strain synonym in the quick search box
        searchbox.send_keys("APPSWE")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[1].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'Synonym : APPSWE')
        wait.forAjax(driver)

    def test_mgp_id(self):
        """
        @status: Tests that an MGP ID search that has a canonical gene brings back the proper information
         @note: Strain-qs-id-33
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("MGP_DBA2J_G0024137")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Genome Features Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[0].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : MGP_DBA2J_G0024137 (Mouse Genome Project)   and more detail...')
        #finds the Other Results By ID Why did this match? information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match3_info = buckets[2].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems3 = iterate.getTextAsList(match3_info)
        wait.forAjax(driver)
        print(searchTextItems3)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(searchTextItems3[2], 'ID : MGP_DBA2J_G0024137 (Mouse Genome Project)')
        wait.forAjax(driver)

    def test_mgp_id_no(self):
        """
        @status: Tests that an MGP ID search that has no canonical gene brings back the proper information
         @note: Strain-qs-id-??
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("MGP_129S1SvlmJ_G0020756")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Genome Features Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[0].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'Symbol : Mgp   and 6 more...')
        wait.forAjax(driver)
                  
    def test_mgi_gene_model_id(self):
        """
        @status: Tests that an MGI Gene Model ID search brings back the proper information
         @note: Strain-qs-id-34
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("MGI_C57BL6J_95661")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'qsBucket')))#waits until the results are displayed on the page
        #finds the Genome Features Best Match information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match_info = buckets[0].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print(searchTextItems)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : MGI_C57BL6J_95661 (MGI Strain Gene)   and more detail...')
        #finds the Other Results By ID Why did this match? information
        buckets = driver.find_elements(By.CLASS_NAME, 'qsBucket')
        match3_info = buckets[2].find_element(By.CLASS_NAME, 'qsBucketRow1').find_elements(By.TAG_NAME, 'td')
        searchTextItems3 = iterate.getTextAsList(match3_info)
        wait.forAjax(driver)
        print(searchTextItems3)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(searchTextItems3[2], 'ID : MGI_C57BL6J_95661 (MGI Strain Gene)')
        wait.forAjax(driver)

    def test_rs_id(self):
        """
        @status: Tests that an rs ID brings back the proper information
        @note 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your rs ID in the quick search box
        searchbox.send_keys("rs49528167")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the results table
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'SNP: rs49528167')
           
    def tearDown(self):
        self.driver.quit()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSearchTool))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))