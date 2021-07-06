'''
Created on Sep 14, 2016
This test is for searches using the quick search feature of the WI
@author: jeffc

'''

import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select
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
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        #self.driver.get("http://www.informatics.jax.org")
        self.driver.get("http://bluebob.informatics.jax.org")
        #self.driver.get(config.TEST_URL) 
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Gene ID primary is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Genome Feature ID: MGI:87895')
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Reference ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: J:14135')       
        

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the vocabulary terms tab table
        driver.find_element(By.ID, 'ui-id-3').click()
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The GO ID is:", all_cells[1].text)
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Genome Feature ID: MGD-MRK-1672')    

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Gene Trap ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: FHCRC-GT-S15-11C1 (IGTC)')    
        
        
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Gene Assay ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI:1339505') 

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Entrez Gene ID: 11539') 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The EntrezGene(NCBI) ID is:", all_cells[2].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[2].text, 'ID: 11539 (MGC)') 

    def test_ncbi_id(self):
        """
        @status: Tests that a NCBI Gene Model ID brings back the proper information
        @bug: 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCBI ID in the quick search box
        searchbox.send_keys("20423")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #print(all_cells[5].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'HomoloGene ID: 20423')
        self.assertEqual(all_cells[2].text, 'Entrez Gene ID: 20423')
        self.assertEqual(all_cells[3].text, 'Name: CpG island 20423')
        self.assertEqual(all_cells[4].text, 'Name: predicted gene 20423')
        self.assertEqual(all_cells[5].text, 'Name: transcription start site region 20423')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b3Table')))#waits until the results are displayed on the page 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The NCBI Gene Model ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: 20423 (NCBI Gene Model)')
                
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Ensembl Gene Model ID: ENSMUSG00000005672') 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Ensembl Gene Model ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: ENSMUSG00000005672 (Ensembl Gene Model)') 

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Ensembl Transcript ID: ENSMUST00000033380') 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Ensembl Transcript ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: ENSMUST00000033380 (Ensembl Transcript)')         

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Ensembl Protein ID: ENSMUSP00000102131') 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Ensembl Protein ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: ENSMUSP00000102131 (Ensembl Protein)')   

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Refseq primary ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'RefSeq ID: NM_023876') 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: NM_023876 (RefSeq)')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Refseq secondary ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'RefSeq ID: XP_001477707') 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: XP_001477707 (RefSeq)')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence DB ID: AK145957') 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Sequence DB primary ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: AK145957 (Sequence DB)')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence DB ID: D87828') 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Sequence DB secondary ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: D87828 (Sequence DB)')        
        
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'SWISS-PROT ID: Q9ER73') 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The SwissProt primary ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: Q9ER73 (SWISS-PROT)')
        
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'SWISS-PROT ID: Q91YT1') 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The SwissProt secondary ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: Q91YT1 (SWISS-PROT)')
        
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'TrEMBL ID: B8JK67') 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Trembl primary ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: B8JK67 (TrEMBL)')
                
    def test_homologene_id(self):
        """
        @status: Tests that an HomoloGene ID brings back the proper information
        @attention: this ID will go away in the next few months 05/28/2021
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your HomoloGene ID in the quick search box
        searchbox.send_keys("20151")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'HomoloGene ID: 20151') 
        self.assertEqual(all_cells[2].text, 'Name: CpG island 20151') 
        self.assertEqual(all_cells[3].text, 'Name: transcription start site region 20151') 
        self.assertEqual(all_cells[4].text, 'Synonym: mm_20151.1') 
        
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Consensus CDS Project ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Consensus CDS Project ID: CCDS28624.1') 

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Unigene ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'UniGene ID: 8122') 
        self.assertEqual(all_cells[2].text, 'HomoloGene ID: 8122') 
        self.assertEqual(all_cells[3].text, 'Name: CpG island 8122') 
        self.assertEqual(all_cells[4].text, 'Name: predicted gene 8122') 
        self.assertEqual(all_cells[5].text, 'Name: transcription start site region 8122') 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print(all_cells[2].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: 8122 (MGC)')
        self.assertEqual(all_cells[2].text, 'ID: 8122 (MGC)') 

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Protein Ontology ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Protein Ontology ID: PR:000008517') 

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The EC ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'EC ID: 3.4.21.6')

    def test_pdb_id(self):
        """
        @status: Tests that a PDB ID brings back the proper information
        @attention: 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your PDB ID in the quick search box
        searchbox.send_keys("1HU8")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The PDB ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'PDB ID: 1HU8') 
        
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The miRBase ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'miRBase ID: MI0000248')        
        
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The QTL Archive ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Download data from the QTL Archive ID: Brich1') 

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The NCBI Gene Model ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'NCBI Gene Model Evidence ID: NT_187055') 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: NT_187055 (RefSeq)')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Affy 1.0 ST ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Affy 1.0 ST ID: 10388707') 

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Affy 430 2.0 ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Affy 430 2.0 ID: 1416346_at') 
 
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Affy U74 ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Affy U74 ID: 107044_at') 
                        
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, "Disease Ortholog: late onset Parkinson's disease (OMIM:168600)") 
        #find the vocabulary terms tab table
        driver.find_element(By.ID, 'ui-id-3').click()
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The OMIM ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: OMIM:168600') 
        #find the alleles tab table
        driver.find_element(By.ID, 'ui-id-2').click()
        results_table = self.driver.find_element(By.ID, 'b5Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, "Disease Model: Parkinson's disease 1 (subterm of late onset Parkinson's disease, with ID OMIM:168600)")

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the vocabulary terms tab table
        driver.find_element(By.ID, 'ui-id-3').click()
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The OMIM ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'OMIM: 168600') 
        
    def test_omim_gene_id(self):
        """
        @status: Tests that an OMIM ID for a gene(human) brings back the proper information
        @attention: 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your OMIM ID in the quick search box
        searchbox.send_keys("OMIM:191170")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        wait.forAjax(driver)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'OMIM ID: OMIM:191170 (human)')
        wait.forAjax(driver) 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The OMIM ID (human) is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: OMIM:191170 (OMIM - human)')
        

    def test_omim_gene_id_no_pre(self):
        """
        @status: Tests that an OMIM ID for a gene(human) without the prefix of OMIM: brings back the proper information
        @note: passed test 12/23/2020
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your OMIM ID in the quick search box
        searchbox.send_keys("191170")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        wait.forAjax(driver)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'OMIM ID: 191170 (human)')
        wait.forAjax(driver)
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The OMIM ID (human) is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: 191170 (OMIM - human)')                 

    def test_hgnc_id(self):
        """
        @status: Tests that an HGNC ID brings back the proper information
        @note: passed test 12/23/2020
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your HGNC ID in the quick search box
        searchbox.send_keys("HGNC:28837")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        wait.forAjax(driver)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'HGNC ID: HGNC:28837 (human)')
        wait.forAjax(driver)
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The HGNC ID (human) is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: HGNC:28837 (HGNC - human)') 
        wait.forAjax(driver) 


    def test_atcc_clone_id(self):
        """
        @status: Tests that an ATCC clone ID brings back the proper information
        @attention: 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your ATCC clone ID in the quick search box
        searchbox.send_keys("719230")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The ATCC clone ID is:", all_cells[1].text)
        wait.forAjax(driver)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: 719230 (ATCC)')
        self.assertEqual(all_cells[2].text, 'ID: 719230 (ATCC)')
        wait.forAjax(driver) 

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first 2 rows of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Image clone ID is:", all_cells[1].text)
        #print(all_cells[2].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI:200469') 
        self.assertEqual(all_cells[2].text, 'ID: MGI:200469')

    def test_mgc_id(self):
        """
        @status: Tests that an MGC ID brings back the proper information
        @note:
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your MGC ID in the quick search box
        searchbox.send_keys("14049")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Entrez Gene ID: 14049') 
        self.assertEqual(all_cells[2].text, 'Name: CpG island 14049')
        self.assertEqual(all_cells[3].text, 'Name: predicted gene 14049') 
        self.assertEqual(all_cells[4].text, 'Name: transcription start site region 14049')
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first 3 rows of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        #print(all_cells[1].text)
        print("The MGC ID is:", all_cells[2].text)
        #print(all_cells[3].text)
        #print(all_cells[4].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: 14049 (NCBI Gene Model)') 
        self.assertEqual(all_cells[2].text, 'ID: 14049 (MGC)')
        self.assertEqual(all_cells[3].text, 'ID: 14049 (MGC)')
        self.assertEqual(all_cells[4].text, 'ID: 14049 (MGC)')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Riken clone ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI:2420147')

    def test_rpci_id(self):
        """
        @status: Tests that an RPCI ID brings back the proper information
        @attention: 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your RPCI ID in the quick search box
        searchbox.send_keys("RP23-100A23")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The RPCI ID is:", all_cells[1].text)
        wait.forAjax(driver)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: RP23-100A23 (RPCI-23)')
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, "Protein Domain: Immunoglobulin subtype (IPR003599)") 
        self.assertEqual(all_cells[2].text, "Protein Domain: Immunoglobulin subtype (IPR003599)") 
        self.assertEqual(all_cells[3].text, "Protein Domain: Immunoglobulin subtype (IPR003599)") 
        self.assertEqual(all_cells[4].text, "Protein Domain: Immunoglobulin subtype (IPR003599)") 
        self.assertEqual(all_cells[5].text, "Protein Domain: Immunoglobulin subtype (IPR003599)") 
        #find the vocabulary terms tab table
        driver.find_element(By.ID, 'ui-id-3').click()
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Interpro ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: IPR003599') 
        

    def test_pirsf_id(self):
        """
        @status: Tests that a PIRSF ID brings back the proper information
        @note: 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your PIRSF ID in the quick search box
        searchbox.send_keys("PIRSF038195")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #print(all_cells[2].text)
        #print(all_cells[3].text)
        #print(all_cells[4].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Protein Family: paired box protein PAX (PIRSF038195)')
        self.assertEqual(all_cells[2].text, 'Protein Family: paired box protein PAX (PIRSF038195)')
        self.assertEqual(all_cells[3].text, 'Protein Family: paired box protein PAX (PIRSF038195)')
        self.assertEqual(all_cells[4].text, 'Protein Family: paired box protein PAX (PIRSF038195)')
        self.assertEqual(all_cells[5].text, 'Protein Family: paired box protein PAX (PIRSF038195)')
        self.assertEqual(all_cells[6].text, 'Protein Family: paired box protein PAX (PIRSF038195)')
        self.assertEqual(all_cells[7].text, 'Protein Family: paired box protein PAX (PIRSF038195)')
        self.assertEqual(all_cells[8].text, 'Protein Family: paired box protein PAX (PIRSF038195)')
        self.assertEqual(all_cells[9].text, 'Protein Family: paired box protein PAX (PIRSF038195)') 
        #find the vocabulary terms tab table
        driver.find_element(By.ID, 'ui-id-3').click()
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The PIRSF ID is:", all_cells[1].text)
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Pubmed ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: 8825637') 

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The MGI Reference ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI:3716133') 

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The dbSNP ID is:", all_cells[1].text)
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Sequence DB ID: S40294')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Genbank(sequence DB) ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: S40294 (Sequence DB)') 
        self.assertEqual(all_cells[1].text, 'ID: S40294 (Sequence DB)')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the alleles tab table
        driver.find_element(By.ID, 'ui-id-2').click()
        results_table = self.driver.find_element(By.ID, 'b5Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Allele(knockout) ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Allele ID: MGI:2156651')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the alleles tab table
        driver.find_element(By.ID, 'ui-id-2').click()
        results_table = self.driver.find_element(By.ID, 'b5Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Cell Line ID: BGB069 (BayGenomics)')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The ES celline(IGTC) ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: BGB069 (IGTC)')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the alleles tab table
        driver.find_element(By.ID, 'ui-id-2').click()
        results_table = self.driver.find_element(By.ID, 'b5Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Cell Line ID: OST2298 (Lexicon)')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the stocks and strains tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best match')
        #print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Name: FVB.129-Slc9a3r2Gt(OST2298)Lex')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The ES celline(Lexicon) ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: OST2298 (Lexicon Genetics)')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Probe ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI:10980')
        
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The MGC clone ID is:", all_cells[1].text)
        #print(all_cells[2].text)
        #print(all_cells[3].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI:1414340')
        self.assertEqual(all_cells[2].text, 'ID: MGI:1414340')
        self.assertEqual(all_cells[3].text, 'ID: MGI:1414340')

    def test_map_exp_id(self):
        """
        @status: Tests that a Mapping Experiment ID brings back the proper information
        @attention: 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Mapping Experiment ID in the quick search box
        searchbox.send_keys("MGD-CREX-2835")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Map Experiment ID is:", all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGD-CREX-2835 (MGI)')
        

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Adult Mouse Anatomy ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MA:0000168 (Adult Mouse Anatomy)')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the vocabulary terms tab table
        driver.find_element(By.ID, 'ui-id-3').click()
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the first row of data to find the best match column of the table
        all_cells = table.get_column_cells('Best match')
        print("The MP ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MP:0002089')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Antibody ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI:4438078')

    def test_proteoform_id(self):
        """
        @status: Tests that a Proteoform ID brings back the proper information
        @attention: Passed 12/23/2020 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Proteoform ID in the quick search box
        searchbox.send_keys("PR:Q80YE4-2")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Proteoform ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Proteoform: mAATK/iso:2 (PR:Q80YE4-2)') 
        
    def test_do_id(self):
        """
        @status: Tests that a Disease Ontology ID brings back the proper information
        @note: passed test 12/23/2020
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Proteoform ID in the quick search box
        searchbox.send_keys("DOID:1700")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Disease Ortholog: X-linked ichthyosis (DOID:1700)')
        #find the vocabulary terms tab table
        driver.find_element(By.ID, 'ui-id-3').click()
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Disease Ontology ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: DOID:1700')
        

    def test_strain_id(self):
        """
        @status: Tests that a Strain ID search brings back the proper information
        @note: Strain-qs-id-1 passed 12/23/2020
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Strain ID in the quick search box
        searchbox.send_keys("MGI:2159854")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI:2159854')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Strain Alternate ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI:2164529')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The JAX strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: 000651')

    def test_strain_mmrrc_id(self):
        """
        @status: Tests that a MMRCC ID search brings back the proper information
         @note: Strain-qs-id-4
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Strain ID in the quick search box
        searchbox.send_keys("mmrrc:029868")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The MMRRC strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'MMRRC: MMRRC:029868')

    def test_strain_apb_id(self):
        """
        @status: Tests that a APB ID search brings back the proper information
         @note: Strain-qs-id-5
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your APB ID in the quick search box
        searchbox.send_keys("APB:629")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The APB strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'APB: APB:629')

    def test_strain_arc_id(self):
        """
        @status: Tests that a ARC ID search brings back the proper information
         @note: Strain-qs-id-6
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your ARC ID in the quick search box
        searchbox.send_keys("ARC:B6")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The ARC strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ARC: ARC:B6')

    def test_strain_card_id(self):
        """
        @status: Tests that a CARD ID search brings back the proper information
         @note: Strain-qs-id-8
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your CARD ID in the quick search box
        searchbox.send_keys("242")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The CARD strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'CARD: 242')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The CMMR strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'CMMR: 0076')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The EMMA strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'EMMA: EM:05001')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The EMS strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'EMS: pacEMS1D')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Harwell strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Harwell: FESA:03299')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The JPGA strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'JPGA: 11473')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The NCIMR strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'NCIMR: 01XH9')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The MPD strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'MPD: 3')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The MUGEN strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'MUGEN: M193046')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The NIG strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'MPD: 229')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The NMICE strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'NMICE: MGI:1861634')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The OBS strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'OBS: OBS:27')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The ORNL strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ORNL: ORNL:47BS')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Riken BRC strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'RIKEN BRC: RBRC00222')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The TAC strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'TAC: TAC:rag2')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The RMRC-NLAC strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'RMRC-NLAC: RMRC11005')

    def test_strain_name(self):
        """
        @status: Tests that a strain name search brings back the proper information
         @note: Strain-qs-name-1 this is a BUG that will get fixed!!
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your strain name in the quick search box
        searchbox.send_keys("CD-1/crl")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The strain name is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: Crl:CD-1')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the alleles tab table
        driver.find_element(By.ID, 'ui-id-2').click()
        results_table = self.driver.find_element(By.ID, 'b5Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The strain synonym is:", all_cells[1].text)
        #asserts that the Best match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Synonym: APPswe')
        #find the strains and sticks tab table
        self.driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best match column of the table
        all_cells = table.get_column_cells('Best Match')
        print(all_cells[1].text)
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Name: 129S6.Cg-Tg(APPSWE)2576Kha/Tac')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the genome features tab table
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the best match? column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Strain Gene ID: MGP_DBA2J_G0024137 (Mouse Genome Project)')
        #find the Alleles tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The MGP strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGP_DBA2J_G0024137 (Mouse Genome Project)')

    def test_bcbc_id(self):
        """
        @status: Tests that a beta cell biology consortium ID search brings back the proper information
         @note: Strain-qs-id-??
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("RES180")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the sticks and strains tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The BCBC strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'BCBC: RES180')

    def test_crl_id(self):
        """
        @status: Tests that a Charles River Labs ID search brings back the proper information
         @note: Strain-qs-id-??
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("CRL:476")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the stocks and strains tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The CRL strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'CRL: CRL:476')

    def test_cwr_id(self):
        """
        @status: Tests that a Case Western Reserve ID search brings back the proper information
         @note: Strain-qs-id-??
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("CWR:S")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the stocks and strains tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The CWR strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'CWR: CWR:S')

    def test_envigo_id(self):
        """
        @status: Tests that an Envigo ID search brings back the proper information
         @note: Strain-qs-id-??
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("118")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the stocks and strains tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The Envigo strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ENVIGO: 118')

    def test_geno_id(self):
        """
        @status: Tests that a geno ID search brings back the proper information
         @note: Strain-qs-id-??
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("GENO:ICP3")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the Strains and stock tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The genOway ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'genOway: GENO:ICP3')

    def test_genphar_id(self):
        """
        @status: Tests that a GenPharmatech ID search brings back the proper information
         @note: Strain-qs-id-??
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("GPT:D000274")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stock tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The GPD ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'GPT: GPT:D000274')

    def test_mgus_id(self):
        """
        @status: Tests that a mammalian genome unit stocklist ID search brings back the proper information
         @note: Strain-qs-id-??
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("FESA:001731")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stock tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The mammalian genome unit stocklist ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Harwell: FESA:001731')

    def test_rgd_id(self):
        """
        @status: Tests that an RGD ID search brings back the proper information
         @note: 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("RGD:1307977")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the best match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Rat Genome Database ID: RGD:1307977 (rat)')
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The RGD ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: RGD:1307977 (Rat Genome Database - rat)')

    def test_kmpc_id(self):
        """
        @status: Tests that a korea mouse phenotyping center ID search brings back the proper information
         @note: Strain-qs-id-??
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("mop1904190")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The KMPC strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'KMPC: MOP1904190')

    def test_zfin_id(self):
        """
        @status: Tests that a ZFIN ID search brings back the proper information
         @note: 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("ZDB-GENE-130530-570")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the best match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Zebrafish Model Organism Database ID: ZDB-GENE-130530-570 (zebrafish)')
        #find the other results by ID tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The ZFIN ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: ZDB-GENE-130530-570 (Zebrafish Model Organism Database - zebrafish)')

    def test_genotype_id(self):
        """
        @status: Tests that a genotype ID(with phenotype data) search brings back the proper information
         @note: 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("MGI:3521824")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Genotype ID(with pheno data) is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI:3521824')

    def test_phenoimage_id(self):
        """
        @status: Tests that a phenotype image ID search brings back the proper information
         @note: 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("MGI:4353158")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The Phenotype Image ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI:4353158')

    def test_gxdimage_id(self):
        """
        @status: Tests that a GXD Image ID search brings back the proper information
         @note: 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("MGI:5292760")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The GXD Image ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI:5292760')

    def test_rmrc_id(self):
        """
        @status: Tests that a national applied Research lab ID search brings back the proper information
         @note: Strain-qs-id-??
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("RMRC13006")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The RMRC-NLAC ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'RMRC-NLAC: RMRC13006')

    def test_smoc_id(self):
        """
        @status: Tests that a shanghai model organism center ID search brings back the proper information
         @note: Strain-qs-id-??
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("NM-NSG-006")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The SMOC ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'SMOC: NM-NSG-006')

    def test_unc_id(self):
        """
        @status: Tests that a university of north carolina ID search brings back the proper information
         @note: Strain-qs-id-??
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("UNC:119")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The UNC ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'UNC: UNC:119')

    def test_vcmr_id(self):
        """
        @status: Tests that a vanderbilt cryopreserved mouse repository ID search brings back the proper information
         @note: Strain-qs-id-??
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("VCMR:5522")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the strains and stocks tab table
        driver.find_element(By.ID, 'ui-id-4').click()
        results_table = self.driver.find_element(By.ID, 'b4Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Best Match')
        print("The VCMR ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'VCMR: VCMR:5522')

    def test_mgp_id_no(self):
        """
        @status: Tests that an MGP ID search that has no canonical gene brings back the proper information
         @note: Strain-qs-id-??
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your NCIMR ID in the quick search box
        searchbox.send_keys("MGP_AJ_G0020403")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Strain Gene ID: MGP_AJ_G0020403 (Mouse Genome Project)')
        #find the other results tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The MGP strain ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGP_AJ_G0020403 (Mouse Genome Project)')
                  
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the Best match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Strain Gene ID: MGI_C57BL6J_95661 (MGI Strain Gene)')
        #find the other results tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The MGI strain gene ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: MGI_C57BL6J_95661 (MGI Strain Gene)')

    def test_mygene_id(self):
        """
        @status: Tests that a My Gene ID brings back the proper information, especially homolog
        @note passed last 6/2/2021
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your rs ID in the quick search box
        searchbox.send_keys("PSEN1")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the best match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the best match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Symbol: Psen1')
        #find the other results tab table
        driver.find_element(By.ID, 'ui-id-5').click()
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Why did this match? column of the table
        all_cells = table.get_column_cells('Why did this match?')
        print("The MyGene ID is:", all_cells[1].text)
        #asserts that the Why did this match? data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'ID: PSEN1 (MyGene - human)')

    def test_mouse_coord_search(self):
        """
        @status: Tests that a search by Mouse Coordinates brings back the proper information, especially homolog
        @note passed last 7/5/2021
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        #Select(self.driver.find_element(By.ID, 'queryType')).select_by_value('mouse location')#finds the query type list and select the 'mouse location' option
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your rs ID in the quick search box
        searchbox.send_keys("Chr5:28661838-28672099")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page 
        #find the genome features tab table
        driver.find_element(By.ID, 'ui-id-1').click()
        time.sleep(2)
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the best match column of the table
        all_cells = table.get_column_cells('Best Match')
        #print(all_cells[1].text)
        #asserts that the best match data is correct for the ID searched
        self.assertEqual(all_cells[1].text, 'Overlaps specified coordinate range: Location')
        #find the alleles tab table
        driver.find_element(By.ID, 'ui-id-2').click()
        time.sleep(2)
        results_table = self.driver.find_element(By.ID, 'b5Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Best Match column of the table
        all_cells = table.get_column_cells('Best match')
        #asserts that the Best Match data is correct for the searched coordinates
        self.assertEqual(all_cells[1].text, 'Overlaps specified coordinate range: Location')
           
    def tearDown(self):
        self.driver.quit()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSearchTool))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))