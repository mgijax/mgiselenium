'''
Created on Sep 14, 2016
This test is for searches using the quick search feature of the WI
@author: jeffc

'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,os.path
from util import wait, iterate
from config.config import TEST_URL
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import TEST_URL

class TestSearchTool(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.get("http://www.informatics.jax.org")
        self.driver.get(TEST_URL) 

    def test_gene_id(self):
        """
        @status: Tests that a Gene ID search brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("MGI:87895")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : MGI:87895   and more detail...')
        wait.forAjax(driver)
        
    def test_ref_id(self):
        """
        @status: Tests that a Reference ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Reference ID in the quick search box
        searchbox.send_keys("J:14135")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : J:14135')
        wait.forAjax(driver)       
        

    def test_go_id(self):
        """
        @status: Tests that an GO ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your GO ID in the quick search box
        searchbox.send_keys("GO:0005892")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'Function : acetylcholine-gated channel complex (GO:0005892)   and more detail...')
        wait.forAjax(driver) 

    def test_old_gene_id(self):
        """
        @status: Tests that an Old Gene ID search brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Old Gene ID in the quick search box
        searchbox.send_keys("MGD-MRK-1672")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : MGD-MRK-1672   and more detail...')
        wait.forAjax(driver)
        

    def test_genetrap_id(self):
        """
        @status: Tests that a Gene Trap ID search brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Gene Trap ID in the quick search box
        searchbox.send_keys("FHCRC-GT-S15-11C1")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : FHCRC-GT-S15-11C1 (IGTC)   and more detail...')
        wait.forAjax(driver)
        
    def test_gene_assay_id(self):
        """
        @status: Tests that a Gene Assay ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Gene Assay ID in the quick search box
        searchbox.send_keys("MGI:1339505")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : MGI:1339505')
        wait.forAjax(driver) 

    def test_ensembl_id(self):
        """
        @status: Tests that an Ensembl ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Ensembl ID in the quick search box
        searchbox.send_keys("ENSMUSG00000005672")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : ENSMUSG00000005672 (Ensembl Gene Model)   and more detail...')
        wait.forAjax(driver) 

    def test_entrezgene_id(self):
        """
        @status: Tests that an Entrezgene ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your EntrezGene ID in the quick search box
        searchbox.send_keys("11539")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : 11539 (Entrez Gene)   and more detail...')
        wait.forAjax(driver) 

    def test_unigene_id(self):
        """
        @status: Tests that an Ensembl ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your UniGene ID in the quick search box
        searchbox.send_keys("181490")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : 181490 (UniGene)   and more detail...')
        wait.forAjax(driver) 
        
    def test_uniprot_id(self):
        """
        @status: Tests that an Ensembl ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your UniProt ID in the quick search box
        searchbox.send_keys("Q9ER73")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : Q9ER73 (UniProt, EBI)   and more detail...')
        wait.forAjax(driver) 

    def test_unists_id(self):
        """
        @status: Tests that an Ensembl ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your UniSTS ID in the quick search box
        searchbox.send_keys("125993")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : 125993 (UniSTS)')
        wait.forAjax(driver) 

    def test_vega_id(self):
        """
        @status: Tests that an Ensembl ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your VEGA ID in the quick search box
        searchbox.send_keys("OTTMUSG00000010935")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : OTTMUSG00000010935 (VEGA Gene Model)   and more detail...')
        wait.forAjax(driver) 

    def test_omim_id(self):
        """
        @status: Tests that an OMIM ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your OMIM ID in the quick search box
        searchbox.send_keys("168600")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[1].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : 168600 (OMIM)')
        wait.forAjax(driver) 

    def test_homologene_id(self):
        """
        @status: Tests that an HomoloGene ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your HomoloGene ID in the quick search box
        searchbox.send_keys("20151")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : 20151 (HomoloGene)   and more detail...')
        wait.forAjax(driver) 

    def test_hgnc_id(self):
        """
        @status: Tests that an HGNC ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your HGNC ID in the quick search box
        searchbox.send_keys("HGNC:28837")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : HGNC:28837 (HGNC - Human)   and more detail...')
        wait.forAjax(driver) 

    def test_refseq_id(self):
        """
        @status: Tests that a RefSeq ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your RegSeq ID in the quick search box
        searchbox.send_keys("NM_023876")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : NM_023876 (RefSeq)   and more detail...')
        wait.forAjax(driver) 

    def test_pdb_id(self):
        """
        @status: Tests that a PDB ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your PDB ID in the quick search box
        searchbox.send_keys("1HU8")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : 1HU8 (PDB)   and more detail...')
        wait.forAjax(driver) 

    def test_atcc_clone_id(self):
        """
        @status: Tests that an ATCC clone ID brings back the proper information 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your ATCC clone ID in the quick search box
        searchbox.send_keys("719230")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_elements_by_class_name("qsBucketRow1")[1].find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : 719230 (ATCC)')
        wait.forAjax(driver) 

    def test_image_clone_id(self):
        """
        @status: Tests that an Image clone ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Image clone ID in the quick search box
        searchbox.send_keys("MGI:200469")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : MGI:200469')
        wait.forAjax(driver) 

    def test_mgc_id(self):
        """
        @status: Tests that an MGC ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your MGC ID in the quick search box
        searchbox.send_keys("14049")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : 14049 (MGC)')
        wait.forAjax(driver) 

    def test_riken_clone_id(self):
        """
        @status: Tests that a RIKEN clone ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your RIKEN clone ID in the quick search box
        searchbox.send_keys("MGI:2420147")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow2").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : MGI:2420147')
        wait.forAjax(driver) 

    def test_rpci_id(self):
        """
        @status: Tests that an RPCI ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your RPCI ID in the quick search box
        searchbox.send_keys("RP23-100A23")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : RP23-100A23 (RPCI-23)')
        wait.forAjax(driver) 

    def test_interpro_id(self):
        """
        @status: Tests that an Interpro ID brings back the proper information 
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your InterPro ID in the quick search box
        searchbox.send_keys("IPR003599")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[1].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : IPR003599')
        wait.forAjax(driver) 

    def test_pirsf_id(self):
        """
        @status: Tests that a PIRSF ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your PIRSF ID in the quick search box
        searchbox.send_keys("PIRSF038195")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[1].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : PIRSF038195')
        wait.forAjax(driver) 

    def test_pubmed_id(self):
        """
        @status: Tests that a PubMed ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your PubMed ID in the quick search box
        searchbox.send_keys("8825637")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : 8825637 (PubMed)')
        wait.forAjax(driver) 

    def test_mgi_reference_id(self):
        """
        @status: Tests that an MGI Reference ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your MGI Reference ID in the quick search box
        searchbox.send_keys("MGI:3716133")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : MGI:3716133')
        wait.forAjax(driver) 

    def test_dbsnp_id(self):
        """
        @status: Tests that a dbSNP ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your dbSNP ID in the quick search box
        searchbox.send_keys("rs3021544")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : rs3021544 (RefSNP)')
        wait.forAjax(driver) 

    def test_genbank_id(self):
        """
        @status: Tests that a GenBank ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Genbank ID in the quick search box
        searchbox.send_keys("S40294")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : S40294 (GenBank, EMBL, DDBJ)')
        wait.forAjax(driver) 

    def test_ec_id(self):
        """
        @status: Tests that a EC ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your EC ID in the quick search box
        searchbox.send_keys("3.4.21.6")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : 3.4.21.6 (EC)   and more detail...')
        wait.forAjax(driver) 

    def test_mirbase_id(self):
        """
        @status: Tests that a miRBase ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your mirBasee ID in the quick search box
        searchbox.send_keys("MI0000248")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'ID : MI0000248 (miRBase)   and more detail...')
        wait.forAjax(driver) 

    def test_allele_id(self):
        """
        @status: Tests that an allele ID(knockout) brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Allele ID in the quick search box
        searchbox.send_keys("MGI:2156651")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'Allele ID : MGI:2156651   and more detail...')
        wait.forAjax(driver) 

    def test_escellline_igtc_id(self):
        """
        @status: Tests that an ES Cell Line ID(IGTC) brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your ES Cell Line ID in the quick search box
        searchbox.send_keys("BGB069")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'Cell Line ID : BGB069 (BayGenomics)   and 2 more...')
        wait.forAjax(driver) 

    def test_escellline_lexicon_id(self):
        """
        @status: Tests that an ES Cell Line ID(Lexicon) brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your ES Cell Line ID in the quick search box
        searchbox.send_keys("OST2298")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'Cell Line ID : OST2298 (Lexicon)   and 2 more...')
        wait.forAjax(driver) 

    def test_ncbi_id(self):
        """
        @status: Tests that a NCBI ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your NCBI ID in the quick search box
        searchbox.send_keys("20423")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_elements_by_class_name("qsBucketRow2")[0].find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : 20423 (NCBI Gene Model)')
        wait.forAjax(driver) 

    def test_probe_id(self):
        """
        @status: Tests that a Probe ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Probe ID in the quick search box
        searchbox.send_keys("MGI:10980")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : MGI:10980')
        wait.forAjax(driver) 

    def test_mgc_clone_id(self):
        """
        @status: Tests that an MGC Clone ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your MGC clone ID in the quick search box
        searchbox.send_keys("MGI:1414340")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_elements_by_class_name("qsBucketRow2")[0].find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : MGI:1414340')
        wait.forAjax(driver) 

    def test_map_exp_id(self):
        """
        @status: Tests that a Mapping Experiment ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Mapping Experiment ID in the quick search box
        searchbox.send_keys("MGD-CREX-2835")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : MGD-CREX-2835')
        wait.forAjax(driver) 

    def test_mouse_anat_id(self):
        """
        @status: Tests that an Adult Mouse Anatomy ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Adult Mouse Anatomy ID in the quick search box
        searchbox.send_keys("MA:0000168")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : MA:0000168 (Adult Mouse Anatomy)')
        wait.forAjax(driver) 

    def test_mp_id(self):
        """
        @status: Tests that an MP ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your MP ID in the quick search box
        searchbox.send_keys("MP:0002089")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[1].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : MP:0002089')
        wait.forAjax(driver) 

    def test_antibody_id(self):
        """
        @status: Tests that an Antibody ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Antibody ID in the quick search box
        searchbox.send_keys("MGI:4438078")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[2].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[2], 'ID : MGI:4438078')
        wait.forAjax(driver) 

    def test_proteoform_id(self):
        """
        @status: Tests that a Proteoform ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Proteoform ID in the quick search box
        searchbox.send_keys("PR:Q80YE4-2")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[0].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[7], 'Proteoform : mAATK/iso:2 (PR:Q80YE4-2)   and more detail...')
        wait.forAjax(driver) 
        
    def test_do_id(self):
        """
        @status: Tests that a Disease Ontology ID brings back the proper information
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element_by_id('searchToolTextArea')
        # put your Proteoform ID in the quick search box
        searchbox.send_keys("DOID:1700")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the Best Match information
        buckets = driver.find_elements_by_class_name("qsBucket")
        match_info = buckets[1].find_element_by_class_name("qsBucketRow1").find_elements_by_tag_name("td")
        searchTextItems = iterate.getTextAsList(match_info)
        wait.forAjax(driver)
        print searchTextItems
        #asserts that the Best Match data is correct for the ID searched
        self.assertEqual(searchTextItems[3], 'ID : DOID:1700')
        wait.forAjax(driver) 
                
        
    def tearDown(self):
        self.driver.quit()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSearchTool))
    return suite

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSpecSumByRef']
    unittest.main()