'''
Created on Jul 24, 2018
These tests start out using the Marker form to display and test Marker Details
@attention: All these tests need to be rewritten using the new Marker module!!!!!!!
@attention: All these tests need to be rewritten using the new Marker module!!!!!!!
@attention: All these tests need to be rewritten using the new Marker module!!!!!!!
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
import sys,os.path
from util import wait, iterate
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import TEST_PWI_URL

class TestPwiMrkDetail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() 

    def test_mrk_det_type_gene(self):
        """
        @status: Tests that a search by Marker Type Gene basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-1
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/')  
        time.sleep(2)
        #find the Symbol field and enter the text      
        driver.find_element(By.ID, 'markerSymbol').send_keys('Kit')
        # Finf the search button and click it.
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(3)
        #wait until the delete column of the history table is present
        #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'deleteIconColumn')))
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'deleteIconColumn')))
        mrk_symbol = driver.find_element(By.ID, 'markerSymbol')#finds the marker symbol
        print (mrk_symbol.text)   
        mrk_id = driver.find_element(By.ID, 'accIdQuery')#finds the marker ID
        print (mrk_id.text)
        mrk_status = driver.find_element(By.ID, 'markerStatus')#finds the Marker status
        print (mrk_status.text)
        mrk_name = driver.find_element(By.ID, 'markerName')#finds the Current Name
        print (mrk_name.text)
        mrk_type = driver.find_element(By.ID, 'markerType')#finds the Marker Type
        print (mrk_type.text)
        mrk_feature = driver.find_element(By.ID, 'featureTypeTable')#finds the Feature Type
        print (mrk_feature.text)
        mrk_chrom = driver.find_element(By.ID, 'chromosome')#finds the Chromosome
        print (mrk_chrom.text)
        mrk_band = driver.find_element(By.ID, 'cytogeneticOffset')#finds the Cytogenetic band
        print (mrk_band.text)
        mrk_posit = driver.find_element(By.ID, 'cmOffset')#finds the Marker Detail cM position
        print (mrk_posit.text)    
        #Verifies that the returned data is all correct for the 11 fields
        #self.assertEqual(mrk_symbol.text, 'Kit', 'The Symbol is not correct!')
        self.assertEqual(mrk_id.text, 'MGI:96677', 'The MGI ID is not correct!')
        self.assertEqual(mrk_status.text, 'Official', 'The Marker Status is not correct!')
        self.assertEqual(mrk_name.text, 'KIT proto-oncogene receptor tyrosine kinase', 'The Current Name is not correct!')
        self.assertEqual(mrk_type.text, 'Gene', 'The Marker Type is not correct!')
        self.assertEqual(mrk_feature.text, 'protein coding gene', 'The Marker Feature Type is not correct!')
        self.assertEqual(mrk_chrom.text, '5', 'The Chromosome is not correct!')
        self.assertEqual(mrk_band.text, 'C', 'The Cytogenetic band is not correct!')
        self.assertEqual(mrk_posit.text, '39.55', 'The cM Position is not correct!')
        
    def test_mrk_det_type_herit(self):
        """
        @status: Tests that a search by Marker Type Heritable Phenotype Marker basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-2
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/MGI:87996')        
        #nomenbox = driver.find_element(By.ID, 'nomen')
        # put your marker symbol in the box
        #nomenbox.send_keys("pax6")
        #nomenbox.send_keys(Keys.RETURN)
        #time.sleep(3)
        #finds the marker link and clicks it
        #driver.find_element(By.LINK_TEXT, "Pax6").click()
        #time.sleep(10)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Alleles')))#waits until the results are displayed on the page by looking for the MGI ID to be displayed
        mrk_symbol = driver.find_element(By.ID, 'mrkDetail_Symbol')#finds the marker symbol
        print (mrk_symbol.text)    
        mrk_id = driver.find_element(By.ID, 'mrkDetail_ID')#finds the marker ID
        print (mrk_id.text)
        mrk_sec = driver.find_element(By.ID, 'mrkDetail_secondaryIDs')#finds the secondary IDs
        print (mrk_sec.text)
        mrk_status = driver.find_element(By.ID, 'mrkDetail_status')#finds the Marker status
        print (mrk_status.text)
        mrk_name = driver.find_element(By.ID, 'mrkDetail_name')#finds the Current Name
        print (mrk_name.text)
        mrk_syn = driver.find_element(By.ID, 'mrkDetail_synonyms')#finds the Synonymns
        print (mrk_syn.text)
        mrk_type = driver.find_element(By.ID, 'mrkDetail_mrkType')#finds the Marker Type
        print (mrk_type.text)
        mrk_feature = driver.find_element(By.ID, 'mrkDetail_featureType')#finds the Feature Type
        print (mrk_feature.text)
        mrk_biotype = driver.find_element(By.ID, 'mrkDetail_biotypes')#finds the Biotypes
        print (mrk_biotype.text)
        mrk_location = driver.find_element(By.ID, 'mrkDetail_location')#finds the Location
        print (mrk_location.text)
        mrk_clip = driver.find_element(By.ID, 'mrkDetail_clip')#finds the Marker Detail Clip
        print (mrk_clip.text)    
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(mrk_symbol.text, 'Alm - Public Alm Page', 'The Symbol is not correct!')
        self.assertEqual(mrk_id.text, 'MGI:87996', 'The MGI ID is not correct!')
        self.assertEqual(mrk_sec.text, '', 'The secondary IDs are not correct!')
        self.assertEqual(mrk_status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(mrk_name.text, 'anterior lenticonus with microphthalmia', 'The Current Name is not correct!')
        self.assertEqual(mrk_syn.text, '', 'The Marker Synonyms are not correct!')
        self.assertEqual(mrk_type.text, 'Gene', 'The Marker Type is not correct!')
        self.assertEqual(mrk_feature.text, 'heritable phenotypic marker', 'The Marker Feature Type is not correct!')
        self.assertEqual(mrk_biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(mrk_location.text, 'ChrUN', 'The Marker Location is not correct!')
        self.assertEqual(mrk_clip.text, 'Homozygous mutation of this gene results in embryonic lethality. Heterozygous mutants exhibit reduced body size, white belly spot, cataracts, cornea/iris dysmorphology, and microphthalmia.', 'The Marker Detail Clip is not correct!')
              
    def test_mrk_det_type_qtl(self):
        """
        @status: Tests that a search by Marker Type QTL basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-3
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/MGI:5002524')        
        #nomenbox = driver.find_element(By.ID, 'nomen')
        # put your marker symbol in the box
        #nomenbox.send_keys("pax6")
        #nomenbox.send_keys(Keys.RETURN)
        #time.sleep(3)
        #finds the marker link and clicks it
        #driver.find_element(By.LINK_TEXT, "Pax6").click()
        #time.sleep(10)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Alleles')))#waits until the results are displayed on the page by looking for the MGI ID to be displayed
        mrk_symbol = driver.find_element(By.ID, 'mrkDetail_Symbol')#finds the marker symbol
        print (mrk_symbol.text)    
        mrk_id = driver.find_element(By.ID, 'mrkDetail_ID')#finds the marker ID
        print (mrk_id.text)
        mrk_sec = driver.find_element(By.ID, 'mrkDetail_secondaryIDs')#finds the secondary IDs
        print (mrk_sec.text)
        mrk_status = driver.find_element(By.ID, 'mrkDetail_status')#finds the Marker status
        print (mrk_status.text)
        mrk_name = driver.find_element(By.ID, 'mrkDetail_name')#finds the Current Name
        print (mrk_name.text)
        mrk_syn = driver.find_element(By.ID, 'mrkDetail_synonyms')#finds the Synonymns
        print (mrk_syn.text)
        mrk_type = driver.find_element(By.ID, 'mrkDetail_mrkType')#finds the Marker Type
        print (mrk_type.text)
        mrk_feature = driver.find_element(By.ID, 'mrkDetail_featureType')#finds the Feature Type
        print (mrk_feature.text)
        mrk_biotype = driver.find_element(By.ID, 'mrkDetail_biotypes')#finds the Biotypes
        print (mrk_biotype.text)
        mrk_location = driver.find_element(By.ID, 'mrkDetail_location')#finds the Location
        print (mrk_location.text)
        mrk_clip = driver.find_element(By.ID, 'mrkDetail_clip')#finds the Marker Detail Clip
        print (mrk_clip.text)    
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(mrk_symbol.text, 'Aanq1 - Public Aanq1 Page', 'The Symbol is not correct!')
        self.assertEqual(mrk_id.text, 'MGI:5002524', 'The MGI ID is not correct!')
        self.assertEqual(mrk_sec.text, '', 'The secondary IDs are not correct!')
        self.assertEqual(mrk_status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(mrk_name.text, 'aristolochic acid nephrotoxicity QTL 1', 'The Current Name is not correct!')
        self.assertEqual(mrk_syn.text, '', 'The Marker Synonyms are not correct!')
        self.assertEqual(mrk_type.text, 'QTL', 'The Marker Type is not correct!')
        self.assertEqual(mrk_feature.text, 'QTL', 'The Marker Feature Type is not correct!')
        self.assertEqual(mrk_biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(mrk_location.text, 'Chr4:63685589-63685589 bp, null strand From MGI annotation of GRCm38', 'The Marker Location is not correct!')
        self.assertEqual(mrk_clip.text, '', 'The Marker Detail Clip is not correct!')

    def test_mrk_det_type_transgene(self):
        """
        @status: Tests that a search by Marker Type Transgene basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-4
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/MGI:3852242')        
        #nomenbox = driver.find_element(By.ID, 'nomen')
        # put your marker symbol in the box
        #nomenbox.send_keys("pax6")
        #nomenbox.send_keys(Keys.RETURN)
        #time.sleep(3)
        #finds the marker link and clicks it
        #driver.find_element(By.LINK_TEXT, "Pax6").click()
        #time.sleep(10)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Alleles')))#waits until the results are displayed on the page by looking for the MGI ID to be displayed
        mrk_symbol = driver.find_element(By.ID, 'mrkDetail_Symbol')#finds the marker symbol
        print (mrk_symbol.text)    
        mrk_id = driver.find_element(By.ID, 'mrkDetail_ID')#finds the marker ID
        print (mrk_id.text)
        mrk_sec = driver.find_element(By.ID, 'mrkDetail_secondaryIDs')#finds the secondary IDs
        print (mrk_sec.text)
        mrk_status = driver.find_element(By.ID, 'mrkDetail_status')#finds the Marker status
        print (mrk_status.text)
        mrk_name = driver.find_element(By.ID, 'mrkDetail_name')#finds the Current Name
        print (mrk_name.text)
        mrk_syn = driver.find_element(By.ID, 'mrkDetail_synonyms')#finds the Synonymns
        print (mrk_syn.text)
        mrk_type = driver.find_element(By.ID, 'mrkDetail_mrkType')#finds the Marker Type
        print (mrk_type.text)
        mrk_feature = driver.find_element(By.ID, 'mrkDetail_featureType')#finds the Feature Type
        print (mrk_feature.text)
        mrk_biotype = driver.find_element(By.ID, 'mrkDetail_biotypes')#finds the Biotypes
        print (mrk_biotype.text)
        mrk_location = driver.find_element(By.ID, 'mrkDetail_location')#finds the Location
        print (mrk_location.text)
        mrk_clip = driver.find_element(By.ID, 'mrkDetail_clip')#finds the Marker Detail Clip
        print (mrk_clip.text)    
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(mrk_symbol.text, 'Et(cre/ERT2)8131Rdav - Public Et(cre/ERT2)8131Rdav Page', 'The Symbol is not correct!')
        self.assertEqual(mrk_id.text, 'MGI:3852242', 'The MGI ID is not correct!')
        self.assertEqual(mrk_sec.text, '', 'The secondary IDs are not correct!')
        self.assertEqual(mrk_status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(mrk_name.text, 'enhancer trap 8131, Ron Davis', 'The Current Name is not correct!')
        self.assertEqual(mrk_syn.text, '', 'The Marker Synonyms are not correct!')
        self.assertEqual(mrk_type.text, 'Transgene', 'The Marker Type is not correct!')
        self.assertEqual(mrk_feature.text, 'transgene', 'The Marker Feature Type is not correct!')
        self.assertEqual(mrk_biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(mrk_location.text, 'ChrUN', 'The Marker Location is not correct!')
        self.assertEqual(mrk_clip.text, '', 'The Marker Detail Clip is not correct!')

    def test_mrk_det_type_Complex(self):
        """
        @status: Tests that a search by Marker Type Complex/Cluster/Region basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-5
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/MGI:88539')        
        #nomenbox = driver.find_element(By.ID, 'nomen')
        # put your marker symbol in the box
        #nomenbox.send_keys("pax6")
        #nomenbox.send_keys(Keys.RETURN)
        #time.sleep(3)
        #finds the marker link and clicks it
        #driver.find_element(By.LINK_TEXT, "Pax6").click()
        #time.sleep(10)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Alleles')))#waits until the results are displayed on the page by looking for the MGI ID to be displayed
        mrk_symbol = driver.find_element(By.ID, 'mrkDetail_Symbol')#finds the marker symbol
        print (mrk_symbol.text)    
        mrk_id = driver.find_element(By.ID, 'mrkDetail_ID')#finds the marker ID
        print (mrk_id.text)
        mrk_sec = driver.find_element(By.ID, 'mrkDetail_secondaryIDs')#finds the secondary IDs
        print (mrk_sec.text)
        mrk_status = driver.find_element(By.ID, 'mrkDetail_status')#finds the Marker status
        print (mrk_status.text)
        mrk_name = driver.find_element(By.ID, 'mrkDetail_name')#finds the Current Name
        print (mrk_name.text)
        mrk_syn = driver.find_element(By.ID, 'mrkDetail_synonyms')#finds the Synonymns
        print (mrk_syn.text)
        mrk_type = driver.find_element(By.ID, 'mrkDetail_mrkType')#finds the Marker Type
        print (mrk_type.text)
        mrk_feature = driver.find_element(By.ID, 'mrkDetail_featureType')#finds the Feature Type
        print (mrk_feature.text)
        mrk_biotype = driver.find_element(By.ID, 'mrkDetail_biotypes')#finds the Biotypes
        print (mrk_biotype.text)
        mrk_location = driver.find_element(By.ID, 'mrkDetail_location')#finds the Location
        print (mrk_location.text)
        mrk_clip = driver.find_element(By.ID, 'mrkDetail_clip')#finds the Marker Detail Clip
        print (mrk_clip.text)    
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(mrk_symbol.text, 'Csn - Public Csn Page', 'The Symbol is not correct!')
        self.assertEqual(mrk_id.text, 'MGI:88539', 'The MGI ID is not correct!')
        self.assertEqual(mrk_sec.text, '', 'The secondary IDs are not correct!')
        self.assertEqual(mrk_status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(mrk_name.text, 'casein gene family, alpha, beta, gamma, delta/epsilon, kappa', 'The Current Name is not correct!')
        self.assertEqual(mrk_syn.text, '', 'The Marker Synonyms are not correct!')
        self.assertEqual(mrk_type.text, 'Complex/Cluster/Region', 'The Marker Type is not correct!')
        self.assertEqual(mrk_feature.text, 'complex/cluster/region', 'The Marker Feature Type is not correct!')
        self.assertEqual(mrk_biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(mrk_location.text, 'Chr5', 'The Marker Location is not correct!')
        self.assertEqual(mrk_clip.text, '', 'The Marker Detail Clip is not correct!')

    def test_mrk_det_type_Cytogenetic(self):
        """
        @status: Tests that a search by Marker Type Cytogenetic Marker basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-6
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/MGI:6156853')        
        #nomenbox = driver.find_element(By.ID, 'nomen')
        # put your marker symbol in the box
        #nomenbox.send_keys("pax6")
        #nomenbox.send_keys(Keys.RETURN)
        #time.sleep(3)
        #finds the marker link and clicks it
        #driver.find_element(By.LINK_TEXT, "Pax6").click()
        #time.sleep(10)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Alleles')))#waits until the results are displayed on the page by looking for the MGI ID to be displayed
        mrk_symbol = driver.find_element(By.ID, 'mrkDetail_Symbol')#finds the marker symbol
        print (mrk_symbol.text)    
        mrk_id = driver.find_element(By.ID, 'mrkDetail_ID')#finds the marker ID
        print (mrk_id.text)
        mrk_sec = driver.find_element(By.ID, 'mrkDetail_secondaryIDs')#finds the secondary IDs
        print (mrk_sec.text)
        mrk_status = driver.find_element(By.ID, 'mrkDetail_status')#finds the Marker status
        print (mrk_status.text)
        mrk_name = driver.find_element(By.ID, 'mrkDetail_name')#finds the Current Name
        print (mrk_name.text)
        mrk_syn = driver.find_element(By.ID, 'mrkDetail_synonyms')#finds the Synonymns
        print (mrk_syn.text)
        mrk_type = driver.find_element(By.ID, 'mrkDetail_mrkType')#finds the Marker Type
        print (mrk_type.text)
        mrk_feature = driver.find_element(By.ID, 'mrkDetail_featureType')#finds the Feature Type
        print (mrk_feature.text)
        mrk_biotype = driver.find_element(By.ID, 'mrkDetail_biotypes')#finds the Biotypes
        print (mrk_biotype.text)
        mrk_location = driver.find_element(By.ID, 'mrkDetail_location')#finds the Location
        print (mrk_location.text)
        mrk_clip = driver.find_element(By.ID, 'mrkDetail_clip')#finds the Marker Detail Clip
        print (mrk_clip.text)    
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(mrk_symbol.text, 'Del(Y)1Tac - Public Del(Y)1Tac Page', 'The Symbol is not correct!')
        self.assertEqual(mrk_id.text, 'MGI:6156853', 'The MGI ID is not correct!')
        self.assertEqual(mrk_sec.text, '', 'The secondary IDs are not correct!')
        self.assertEqual(mrk_status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(mrk_name.text, 'deletion, Chr Y, Taconic 1', 'The Current Name is not correct!')
        self.assertEqual(mrk_syn.text, '', 'The Marker Synonyms are not correct!')
        self.assertEqual(mrk_type.text, 'Cytogenetic Marker', 'The Marker Type is not correct!')
        self.assertEqual(mrk_feature.text, 'cytogenetic marker', 'The Marker Feature Type is not correct!')
        self.assertEqual(mrk_biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(mrk_location.text, 'ChrY', 'The Marker Location is not correct!')
        self.assertEqual(mrk_clip.text, '', 'The Marker Detail Clip is not correct!')

    def test_mrk_det_type_bacyac(self):
        """
        @status: Tests that a search by Marker Type Bac/Yac basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-7
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/MGI:1336996')        
        #nomenbox = driver.find_element(By.ID, 'nomen')
        # put your marker symbol in the box
        #nomenbox.send_keys("pax6")
        #nomenbox.send_keys(Keys.RETURN)
        #time.sleep(3)
        #finds the marker link and clicks it
        #driver.find_element(By.LINK_TEXT, "Pax6").click()
        #time.sleep(10)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Alleles')))#waits until the results are displayed on the page by looking for the MGI ID to be displayed
        mrk_symbol = driver.find_element(By.ID, 'mrkDetail_Symbol')#finds the marker symbol
        print (mrk_symbol.text)    
        mrk_id = driver.find_element(By.ID, 'mrkDetail_ID')#finds the marker ID
        print (mrk_id.text)
        mrk_sec = driver.find_element(By.ID, 'mrkDetail_secondaryIDs')#finds the secondary IDs
        print (mrk_sec.text)
        mrk_status = driver.find_element(By.ID, 'mrkDetail_status')#finds the Marker status
        print (mrk_status.text)
        mrk_name = driver.find_element(By.ID, 'mrkDetail_name')#finds the Current Name
        print (mrk_name.text)
        mrk_syn = driver.find_element(By.ID, 'mrkDetail_synonyms')#finds the Synonymns
        print (mrk_syn.text)
        mrk_type = driver.find_element(By.ID, 'mrkDetail_mrkType')#finds the Marker Type
        print (mrk_type.text)
        mrk_feature = driver.find_element(By.ID, 'mrkDetail_featureType')#finds the Feature Type
        print (mrk_feature.text)
        mrk_biotype = driver.find_element(By.ID, 'mrkDetail_biotypes')#finds the Biotypes
        print (mrk_biotype.text)
        mrk_location = driver.find_element(By.ID, 'mrkDetail_location')#finds the Location
        print (mrk_location.text)
        mrk_clip = driver.find_element(By.ID, 'mrkDetail_clip')#finds the Marker Detail Clip
        print (mrk_clip.text)    
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(mrk_symbol.text, '10S - Public 10S Page', 'The Symbol is not correct!')
        self.assertEqual(mrk_id.text, 'MGI:1336996', 'The MGI ID is not correct!')
        self.assertEqual(mrk_sec.text, '', 'The secondary IDs are not correct!')
        self.assertEqual(mrk_status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(mrk_name.text, 'DNA segment, 10S', 'The Current Name is not correct!')
        self.assertEqual(mrk_syn.text, '', 'The Marker Synonyms are not correct!')
        self.assertEqual(mrk_type.text, 'BAC/YAC end', 'The Marker Type is not correct!')
        self.assertEqual(mrk_feature.text, 'BAC/YAC end', 'The Marker Feature Type is not correct!')
        self.assertEqual(mrk_biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(mrk_location.text, 'Chr17', 'The Marker Location is not correct!')
        self.assertEqual(mrk_clip.text, '', 'The Marker Detail Clip is not correct!')

    def test_mrk_det_type_pseudo(self):
        """
        @status: Tests that a search by Marker Type Pseudogene basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-8
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/MGI:3035137')        
        #nomenbox = driver.find_element(By.ID, 'nomen')
        # put your marker symbol in the box
        #nomenbox.send_keys("pax6")
        #nomenbox.send_keys(Keys.RETURN)
        #time.sleep(3)
        #finds the marker link and clicks it
        #driver.find_element(By.LINK_TEXT, "Pax6").click()
        #time.sleep(10)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Alleles')))#waits until the results are displayed on the page by looking for the MGI ID to be displayed
        mrk_symbol = driver.find_element(By.ID, 'mrkDetail_Symbol')#finds the marker symbol
        print (mrk_symbol.text)    
        mrk_id = driver.find_element(By.ID, 'mrkDetail_ID')#finds the marker ID
        print (mrk_id.text)
        mrk_sec = driver.find_element(By.ID, 'mrkDetail_secondaryIDs')#finds the secondary IDs
        print (mrk_sec.text)
        mrk_status = driver.find_element(By.ID, 'mrkDetail_status')#finds the Marker status
        print (mrk_status.text)
        mrk_name = driver.find_element(By.ID, 'mrkDetail_name')#finds the Current Name
        print (mrk_name.text)
        mrk_syn = driver.find_element(By.ID, 'mrkDetail_synonyms')#finds the Synonymns
        print (mrk_syn.text)
        mrk_type = driver.find_element(By.ID, 'mrkDetail_mrkType')#finds the Marker Type
        print (mrk_type.text)
        mrk_feature = driver.find_element(By.ID, 'mrkDetail_featureType')#finds the Feature Type
        print (mrk_feature.text)
        mrk_biotype = driver.find_element(By.ID, 'mrkDetail_biotypes')#finds the Biotypes
        print (mrk_biotype.text)
        mrk_location = driver.find_element(By.ID, 'mrkDetail_location')#finds the Location
        print (mrk_location.text)
        mrk_clip = driver.find_element(By.ID, 'mrkDetail_clip')#finds the Marker Detail Clip
        print (mrk_clip.text)    
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(mrk_symbol.text, 'AA414768 - Public AA414768 Page', 'The Symbol is not correct!')
        self.assertEqual(mrk_id.text, 'MGI:3035137', 'The MGI ID is not correct!')
        self.assertEqual(mrk_sec.text, 'MGI:3705633', 'The secondary IDs are not correct!')
        self.assertEqual(mrk_status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(mrk_name.text, 'expressed sequence AA414768', 'The Current Name is not correct!')
        self.assertEqual(mrk_syn.text, 'OTTMUSG00000017000', 'The Marker Synonyms are not correct!')
        self.assertEqual(mrk_type.text, 'Pseudogene', 'The Marker Type is not correct!')
        self.assertEqual(mrk_feature.text, 'pseudogenic region', 'The Marker Feature Type is not correct!')
        self.assertEqual(mrk_biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(mrk_location.text, 'ChrX:12936872-12938128 bp, + strand From Ensembl annotation of GRCm38', 'The Marker Location is not correct!')
        self.assertEqual(mrk_clip.text, '', 'The Marker Detail Clip is not correct!')

    def test_mrk_det_type_other(self):
        """
        @status: Tests that a search by Marker Type Other Genome Feature basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-8
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/MGI:87875')        
        #nomenbox = driver.find_element(By.ID, 'nomen')
        # put your marker symbol in the box
        #nomenbox.send_keys("pax6")
        #nomenbox.send_keys(Keys.RETURN)
        #time.sleep(3)
        #finds the marker link and clicks it
        #driver.find_element(By.LINK_TEXT, "Pax6").click()
        #time.sleep(10)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Alleles')))#waits until the results are displayed on the page by looking for the MGI ID to be displayed
        mrk_symbol = driver.find_element(By.ID, 'mrkDetail_Symbol')#finds the marker symbol
        print (mrk_symbol.text)    
        mrk_id = driver.find_element(By.ID, 'mrkDetail_ID')#finds the marker ID
        print (mrk_id.text)
        mrk_sec = driver.find_element(By.ID, 'mrkDetail_secondaryIDs')#finds the secondary IDs
        print (mrk_sec.text)
        mrk_status = driver.find_element(By.ID, 'mrkDetail_status')#finds the Marker status
        print (mrk_status.text)
        mrk_name = driver.find_element(By.ID, 'mrkDetail_name')#finds the Current Name
        print (mrk_name.text)
        mrk_syn = driver.find_element(By.ID, 'mrkDetail_synonyms')#finds the Synonymns
        print (mrk_syn.text)
        mrk_type = driver.find_element(By.ID, 'mrkDetail_mrkType')#finds the Marker Type
        print (mrk_type.text)
        mrk_feature = driver.find_element(By.ID, 'mrkDetail_featureType')#finds the Feature Type
        print (mrk_feature.text)
        mrk_biotype = driver.find_element(By.ID, 'mrkDetail_biotypes')#finds the Biotypes
        print (mrk_biotype.text)
        mrk_location = driver.find_element(By.ID, 'mrkDetail_location')#finds the Location
        print (mrk_location.text)
        mrk_clip = driver.find_element(By.ID, 'mrkDetail_clip')#finds the Marker Detail Clip
        print (mrk_clip.text)    
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(mrk_symbol.text, 'Acf1 - Public Acf1 Page', 'The Symbol is not correct!')
        self.assertEqual(mrk_id.text, 'MGI:87875', 'The MGI ID is not correct!')
        self.assertEqual(mrk_sec.text, '', 'The secondary IDs are not correct!')
        self.assertEqual(mrk_status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(mrk_name.text, 'albumin conformation factor 1', 'The Current Name is not correct!')
        self.assertEqual(mrk_syn.text, 'Acf-1', 'The Marker Synonyms are not correct!')
        self.assertEqual(mrk_type.text, 'Other Genome Feature', 'The Marker Type is not correct!')
        self.assertEqual(mrk_feature.text, 'unclassified other genome feature', 'The Marker Feature Type is not correct!')
        self.assertEqual(mrk_biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(mrk_location.text, 'Chr1', 'The Marker Location is not correct!')
        self.assertEqual(mrk_clip.text, '', 'The Marker Detail Clip is not correct!')
        
    def test_mrk_det_withdrawn_mrk(self):
        """
        @status: Tests that a withdrawn marker returns correctly
        @note pwi-mrk-det-search-10
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/key/155768')  
        #opens the PWI marker form
        #driver.get(TEST_PWI_URL + '/#markerForm')        
        #nomenbox = driver.find_element(By.ID, 'nomen')
        # put your marker symbol in the box
        #nomenbox.send_keys("gata1")
        #nomenbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Public Ccm1 Page')))#waits until the Gata1 link is displayed on the page
        mrk_symbol = driver.find_element(By.ID, 'mrkDetail_Symbol')#finds the marker symbol
        print (mrk_symbol.text)    
        mrk_id = driver.find_element(By.ID, 'mrkDetail_ID')#finds the marker ID
        print (mrk_id.text)
        mrk_sec = driver.find_element(By.ID, 'mrkDetail_secondaryIDs')#finds the secondary IDs
        print (mrk_sec.text)
        mrk_status = driver.find_element(By.ID, 'mrkDetail_status')#finds the Marker status
        print (mrk_status.text)
        mrk_name = driver.find_element(By.ID, 'mrkDetail_name')#finds the Current Name
        print (mrk_name.text)
        mrk_syn = driver.find_element(By.ID, 'mrkDetail_synonyms')#finds the Synonymns
        print (mrk_syn.text)
        mrk_type = driver.find_element(By.ID, 'mrkDetail_mrkType')#finds the Marker Type
        print (mrk_type.text)
        mrk_feature = driver.find_element(By.ID, 'mrkDetail_featureType')#finds the Feature Type
        print (mrk_feature.text)
        mrk_biotype = driver.find_element(By.ID, 'mrkDetail_biotypes')#finds the Biotypes
        print (mrk_biotype.text)
        mrk_location = driver.find_element(By.ID, 'mrkDetail_location')#finds the Location
        print (mrk_location.text)
        mrk_clip = driver.find_element(By.ID, 'mrkDetail_clip')#finds the Marker Detail Clip
        print (mrk_clip.text)    
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(mrk_symbol.text, 'Ccm1 - Public Ccm1 Page', 'The Symbol is not correct!')
        self.assertEqual(mrk_id.text, '', 'The MGI ID is not correct!')
        self.assertEqual(mrk_sec.text, '', 'The secondary IDs are not correct!')
        self.assertEqual(mrk_status.text, 'withdrawn', 'The Marker Status is not correct!')
        self.assertEqual(mrk_name.text, 'withdrawn, = Krit1', 'The Current Name is not correct!')
        self.assertEqual(mrk_syn.text, '', 'The Marker Synonyms are not correct!')
        self.assertEqual(mrk_type.text, 'Gene', 'The Marker Type is not correct!')
        self.assertEqual(mrk_feature.text, '', 'The Marker Feature Type is not correct!')
        self.assertEqual(mrk_biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(mrk_location.text, 'Chr5', 'The Marker Location is not correct!')
        self.assertEqual(mrk_clip.text, '', 'The Marker Detail Clip is not correct!')
        

    def tearDown(self):
        self.driver.close()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPwiMrkDetail))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))