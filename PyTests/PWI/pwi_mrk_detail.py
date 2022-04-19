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
from selenium.webdriver.support.ui import Select
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
        @note sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-1 passed test 12/7/2020
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/')  
        time.sleep(2)
        #find the Symbol field and enter the text      
        driver.find_element(By.ID, 'markerSymbol').send_keys('Kit')
        # Find the search button and click it.
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(3)
        driver.find_element(By.ID, 'mrkDetailButton').click()
        time.sleep(3)
        driver.switch_to.window(self.driver.window_handles[1])
        symbol = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(2)')
        print("the symbol is: " + symbol.text)
        mrkid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(5)')
        print("the ID is: " + mrkid.text)
        secid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(7)')
        print("the secondary ID is: " + secid.text)
        status = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(9)')
        print("the marker status is: " + status.text)
        name = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(11)')
        print("the current name is: " + name.text)
        syn = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(13)')
        print("the synonym is: " + syn.text)
        mtype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(15)')
        print("the marker type is: " + mtype.text)
        ftype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(17)')
        print("the feature type is: " + ftype.text)
        biotype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(19)')
        print("the biotypes are: " + biotype.text)
        location = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(21)')
        print("the location is: " + location.text)
        mrkclip = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(23)')
        print("the marker detail clip is: " + mrkclip.text)
        #wait until the delete column of the history table is present
        #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'deleteIconColumn')))
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'deleteIconColumn')))
         
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(symbol.text, 'Kit Public Kit Page', 'The Symbol is not correct!')
        self.assertEqual(mrkid.text, 'MGI:96677', 'The MGI ID is not correct!')
        self.assertEqual(secid.text, 'MGI:3530304, MGI:3530312, MGI:3530319', 'The Secondary IDs are not correct!')
        self.assertEqual(status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(name.text, 'KIT proto-oncogene receptor tyrosine kinase', 'The Current Name is not correct!')
        self.assertEqual(syn.text, 'belly-spot, CD117, c-KIT, Dominant white spotting, Gsfsco1, Gsfsco5, Gsfsow3, SCO1, SCO5, SOW3, Steel Factor Receptor, Tr-kit', 'The Synonym is not correct!')
        self.assertEqual(mtype.text, 'Gene', 'The Marker Type is not correct!')
        self.assertEqual(ftype.text, 'protein coding gene', 'The Marker Feature Type is not correct!')
        self.assertEqual(biotype.text, 'Source Biotype Gene ID\nNCBI Gene Model protein-coding 16590\nEnsembl Gene Model protein_coding ENSMUSG00000005672', 'The biotype is not correct!')
        self.assertEqual(location.text, 'Chr5:75735647-75817382 bp, + strand From NCBI annotation of GRCm39', 'The Location is not correct!')
        self.assertEqual(mrkclip.text, 'Mutations at this locus affect migration of embryonic stem cell populations, resulting in mild to severe impairments in hematopoiesis, and pigmentation. Some alleles are homozygous lethal, sterile, or result in the formation of gastrointestinal tumors.', 'The Marker Clip band is not correct!')

        
    def test_mrk_det_type_herit(self):
        """
        @status: Tests that a search by Marker Type Heritable Phenotype Marker basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-2 passed test 12/4/2020
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/')  
        time.sleep(2)
        #find the Symbol field and enter the text      
        driver.find_element(By.ID, 'markerSymbol').send_keys('Alm')
        # Find the search button and click it.
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(3)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mrkDetailButton')))#waits until the results are displayed on the page by looking for the Marker Detail link to be displayed
        #Find the Marker Detail link and click it
        driver.find_element(By.ID, 'mrkDetailButton').click()
        time.sleep(3)
        driver.switch_to.window(self.driver.window_handles[1])
        symbol = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(2)')
        print("the symbol is: " + symbol.text)
        mrkid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(5)')
        print("the ID is: " + mrkid.text)
        secid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(7)')
        print("the secondary ID is: " + secid.text)
        status = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(9)')
        print("the marker status is: " + status.text)
        name = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(11)')
        print("the current name is: " + name.text)
        syn = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(13)')
        print("the synonym is: " + syn.text)
        mtype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(15)')
        print("the marker type is: " + mtype.text)
        ftype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(17)')
        print("the feature type is: " + ftype.text)
        biotype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(19)')
        print("the biotypes are: " + biotype.text)
        location = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(21)')
        print("the location is: " + location.text)
        mrkclip = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(23)')
        print("the marker detail clip is: " + mrkclip.text)
            
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(symbol.text, 'Alm Public Alm Page', 'The Symbol is not correct!')
        self.assertEqual(mrkid.text, 'MGI:87996', 'The MGI ID is not correct!')
        self.assertEqual(secid.text, '[]', 'The secondary IDs are not correct!')
        self.assertEqual(status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(name.text, 'anterior lenticonus with microphthalmia', 'The Current Name is not correct!')
        self.assertEqual(syn.text, '', 'The Marker Synonyms are not correct!')
        self.assertEqual(mtype.text, 'Gene', 'The Marker Type is not correct!')
        self.assertEqual(ftype.text, 'heritable phenotypic marker', 'The Marker Feature Type is not correct!')
        self.assertEqual(biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(location.text, 'ChrUN', 'The Marker Location is not correct!')
        self.assertEqual(mrkclip.text, 'Homozygous mutation of this gene results in embryonic lethality. Heterozygous mutants exhibit reduced body size, white belly spot, cataracts, cornea/iris dysmorphology, and microphthalmia.', 'The Marker Detail Clip is not correct!')
              
    def test_mrk_det_type_qtl(self):
        """
        @status: Tests that a search by Marker Type QTL basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-3 passed 12/07/2020
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/')        
        time.sleep(2)
        #find the Symbol field and enter the text      
        driver.find_element(By.ID, 'markerSymbol').send_keys('Aanq1')
        # Find the search button and click it.
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(3)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mrkDetailButton')))#waits until the results are displayed on the page by looking for the Marker Detail link to be displayed
        #Find the Marker Detail link and click it
        driver.find_element(By.ID, 'mrkDetailButton').click()
        time.sleep(3)
        driver.switch_to.window(self.driver.window_handles[1])
        symbol = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(2)')
        print("the symbol is: " + symbol.text)
        mrkid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(5)')
        print("the ID is: " + mrkid.text)
        secid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(7)')
        print("the secondary ID is: " + secid.text)
        status = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(9)')
        print("the marker status is: " + status.text)
        name = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(11)')
        print("the current name is: " + name.text)
        syn = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(13)')
        print("the synonym is: " + syn.text)
        mtype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(15)')
        print("the marker type is: " + mtype.text)
        ftype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(17)')
        print("the feature type is: " + ftype.text)
        biotype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(19)')
        print("the biotypes are: " + biotype.text)
        location = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(21)')
        print("the location is: " + location.text)
        mrkclip = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(23)')
        print("the marker detail clip is: " + mrkclip.text)
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(symbol.text, 'Aanq1 Public Aanq1 Page', 'The Symbol is not correct!')
        self.assertEqual(mrkid.text, 'MGI:5002524', 'The MGI ID is not correct!')
        self.assertEqual(secid.text, '[]', 'The secondary IDs are not correct!')
        self.assertEqual(status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(name.text, 'aristolochic acid nephrotoxicity QTL 1', 'The Current Name is not correct!')
        self.assertEqual(syn.text, '', 'The Marker Synonyms are not correct!')
        self.assertEqual(mtype.text, 'QTL', 'The Marker Type is not correct!')
        self.assertEqual(ftype.text, 'QTL', 'The Marker Feature Type is not correct!')
        self.assertEqual(biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(location.text, 'Chr4:63603826-63603826 bp, None strand From MGI annotation of GRCm39', 'The Marker Location is not correct!')
        self.assertEqual(mrkclip.text, '', 'The Marker Detail Clip is not correct!')

    def test_mrk_det_type_transgene(self):
        """
        @status: Tests that a search by Marker Type Transgene basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-4 passed 12/07/2020
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/')        
        time.sleep(2)
        #find the Symbol field and enter the text      
        driver.find_element(By.ID, 'markerSymbol').send_keys('Et(cre/ERT2)8131Rdav')
        # Find the search button and click it.
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(3)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mrkDetailButton')))#waits until the results are displayed on the page by looking for the Marker Detail link to be displayed
        #Find the Marker Detail link and click it
        driver.find_element(By.ID, 'mrkDetailButton').click()
        time.sleep(3)
        driver.switch_to.window(self.driver.window_handles[1])
        symbol = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(2)')
        print("the symbol is: " + symbol.text)
        mrkid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(5)')
        print("the ID is: " + mrkid.text)
        secid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(7)')
        print("the secondary ID is: " + secid.text)
        status = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(9)')
        print("the marker status is: " + status.text)
        name = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(11)')
        print("the current name is: " + name.text)
        syn = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(13)')
        print("the synonym is: " + syn.text)
        mtype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(15)')
        print("the marker type is: " + mtype.text)
        ftype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(17)')
        print("the feature type is: " + ftype.text)
        biotype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(19)')
        print("the biotypes are: " + biotype.text)
        location = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(21)')
        print("the location is: " + location.text)
        mrkclip = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(23)')
        print("the marker detail clip is: " + mrkclip.text)
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(symbol.text, 'Et(cre/ERT2)8131Rdav Public Et(cre/ERT2)8131Rdav Page', 'The Symbol is not correct!')
        self.assertEqual(mrkid.text, 'MGI:3852242', 'The MGI ID is not correct!')
        self.assertEqual(secid.text, '[]', 'The secondary IDs are not correct!')
        self.assertEqual(status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(name.text, 'enhancer trap 8131, Ron Davis', 'The Current Name is not correct!')
        self.assertEqual(syn.text, '', 'The Marker Synonyms are not correct!')
        self.assertEqual(mtype.text, 'Transgene', 'The Marker Type is not correct!')
        self.assertEqual(ftype.text, 'transgene', 'The Marker Feature Type is not correct!')
        self.assertEqual(biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(location.text, 'ChrUN', 'The Marker Location is not correct!')
        self.assertEqual(mrkclip.text, '', 'The Marker Detail Clip is not correct!')

    def test_mrk_det_type_Complex(self):
        """
        @status: Tests that a search by Marker Type Complex/Cluster/Region basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-5 passed 12/07/2020
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/')        
        time.sleep(2)
        #find the Symbol field and enter the text      
        driver.find_element(By.ID, 'markerSymbol').send_keys('Csn')
        # Find the search button and click it.
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(3)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mrkDetailButton')))#waits until the results are displayed on the page by looking for the Marker Detail link to be displayed
        #Find the Marker Detail link and click it
        driver.find_element(By.ID, 'mrkDetailButton').click()
        time.sleep(3)
        driver.switch_to.window(self.driver.window_handles[1])
        symbol = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(2)')
        print("the symbol is: " + symbol.text)
        mrkid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(5)')
        print("the ID is: " + mrkid.text)
        secid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(7)')
        print("the secondary ID is: " + secid.text)
        status = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(9)')
        print("the marker status is: " + status.text)
        name = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(11)')
        print("the current name is: " + name.text)
        syn = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(13)')
        print("the synonym is: " + syn.text)
        mtype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(15)')
        print("the marker type is: " + mtype.text)
        ftype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(17)')
        print("the feature type is: " + ftype.text)
        biotype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(19)')
        print("the biotypes are: " + biotype.text)
        location = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(21)')
        print("the location is: " + location.text)
        mrkclip = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(23)')
        print("the marker detail clip is: " + mrkclip.text) 
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(symbol.text, 'Csn Public Csn Page', 'The Symbol is not correct!')
        self.assertEqual(mrkid.text, 'MGI:88539', 'The MGI ID is not correct!')
        self.assertEqual(secid.text, '[]', 'The secondary IDs are not correct!')
        self.assertEqual(status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(name.text, 'casein gene family, alpha, beta, gamma, delta/epsilon, kappa', 'The Current Name is not correct!')
        self.assertEqual(syn.text, '', 'The Marker Synonyms are not correct!')
        self.assertEqual(mtype.text, 'Complex/Cluster/Region', 'The Marker Type is not correct!')
        self.assertEqual(ftype.text, 'complex/cluster/region', 'The Marker Feature Type is not correct!')
        self.assertEqual(biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(location.text, 'Chr5', 'The Marker Location is not correct!')
        self.assertEqual(mrkclip.text, '', 'The Marker Detail Clip is not correct!')

    def test_mrk_det_type_Cytogenetic(self):
        """
        @status: Tests that a search by Marker Type Cytogenetic Marker basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-6 passed 12/07/2020
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/')        
        time.sleep(2)
        #find the Symbol field and enter the text      
        driver.find_element(By.ID, 'markerSymbol').send_keys('Del(Y)1Tac')
        # Find the search button and click it.
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(3)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mrkDetailButton')))#waits until the results are displayed on the page by looking for the Marker Detail link to be displayed
        #Find the Marker Detail link and click it
        driver.find_element(By.ID, 'mrkDetailButton').click()
        time.sleep(3)
        driver.switch_to.window(self.driver.window_handles[1])
        symbol = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(2)')
        print("the symbol is: " + symbol.text)
        mrkid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(5)')
        print("the ID is: " + mrkid.text)
        secid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(7)')
        print("the secondary ID is: " + secid.text)
        status = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(9)')
        print("the marker status is: " + status.text)
        name = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(11)')
        print("the current name is: " + name.text)
        syn = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(13)')
        print("the synonym is: " + syn.text)
        mtype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(15)')
        print("the marker type is: " + mtype.text)
        ftype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(17)')
        print("the feature type is: " + ftype.text)
        biotype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(19)')
        print("the biotypes are: " + biotype.text)
        location = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(21)')
        print("the location is: " + location.text)
        mrkclip = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(23)')
        print("the marker detail clip is: " + mrkclip.text)    
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(symbol.text, 'Del(Y)1Tac Public Del(Y)1Tac Page', 'The Symbol is not correct!')
        self.assertEqual(mrkid.text, 'MGI:6156853', 'The MGI ID is not correct!')
        self.assertEqual(secid.text, '[]', 'The secondary IDs are not correct!')
        self.assertEqual(status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(name.text, 'deletion, Chr Y, Taconic 1', 'The Current Name is not correct!')
        self.assertEqual(syn.text, '', 'The Marker Synonyms are not correct!')
        self.assertEqual(mtype.text, 'Cytogenetic Marker', 'The Marker Type is not correct!')
        self.assertEqual(ftype.text, 'chromosomal deletion', 'The Marker Feature Type is not correct!')
        self.assertEqual(biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(location.text, 'ChrY', 'The Marker Location is not correct!')
        self.assertEqual(mrkclip.text, '', 'The Marker Detail Clip is not correct!')

    def test_mrk_det_type_bacyac(self):
        """
        @status: Tests that a search by Marker Type Bac/Yac basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-7 passed 12/07/2020
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/')        
        time.sleep(2)
        #find the Symbol field and enter the text      
        driver.find_element(By.ID, 'markerSymbol').send_keys('10S')
        # Find the search button and click it.
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(3)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mrkDetailButton')))#waits until the results are displayed on the page by looking for the Marker Detail link to be displayed
        #Find the Marker Detail link and click it
        driver.find_element(By.ID, 'mrkDetailButton').click()
        time.sleep(3)
        driver.switch_to.window(self.driver.window_handles[1])
        symbol = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(2)')
        print("the symbol is: " + symbol.text)
        mrkid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(5)')
        print("the ID is: " + mrkid.text)
        secid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(7)')
        print("the secondary ID is: " + secid.text)
        status = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(9)')
        print("the marker status is: " + status.text)
        name = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(11)')
        print("the current name is: " + name.text)
        syn = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(13)')
        print("the synonym is: " + syn.text)
        mtype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(15)')
        print("the marker type is: " + mtype.text)
        ftype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(17)')
        print("the feature type is: " + ftype.text)
        biotype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(19)')
        print("the biotypes are: " + biotype.text)
        location = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(21)')
        print("the location is: " + location.text)
        mrkclip = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(23)')
        print("the marker detail clip is: " + mrkclip.text)  
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(symbol.text, '10S Public 10S Page', 'The Symbol is not correct!')
        self.assertEqual(mrkid.text, 'MGI:1336996', 'The MGI ID is not correct!')
        self.assertEqual(secid.text, '[]', 'The secondary IDs are not correct!')
        self.assertEqual(status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(name.text, 'DNA segment, 10S', 'The Current Name is not correct!')
        self.assertEqual(syn.text, '', 'The Marker Synonyms are not correct!')
        self.assertEqual(mtype.text, 'BAC/YAC end', 'The Marker Type is not correct!')
        self.assertEqual(ftype.text, 'BAC/YAC end', 'The Marker Feature Type is not correct!')
        self.assertEqual(biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(location.text, 'Chr17', 'The Marker Location is not correct!')
        self.assertEqual(mrkclip.text, '', 'The Marker Detail Clip is not correct!')
 
    def test_mrk_det_type_pseudo(self):
        """
        @status: Tests that a search by Marker Type Pseudogene basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-8 passed 12/07/2020
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/')        
        time.sleep(2)
        #find the Symbol field and enter the text      
        driver.find_element(By.ID, 'markerSymbol').send_keys('AA414768')
        # Find the search button and click it.
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(3)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mrkDetailButton')))#waits until the results are displayed on the page by looking for the Marker Detail link to be displayed
        #Find the Marker Detail link and click it
        driver.find_element(By.ID, 'mrkDetailButton').click()
        time.sleep(3)
        driver.switch_to.window(self.driver.window_handles[1])
        symbol = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(2)')
        print("the symbol is: " + symbol.text)
        mrkid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(5)')
        print("the ID is: " + mrkid.text)
        secid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(7)')
        print("the secondary ID is: " + secid.text)
        status = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(9)')
        print("the marker status is: " + status.text)
        name = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(11)')
        print("the current name is: " + name.text)
        syn = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(13)')
        print("the synonym is: " + syn.text)
        mtype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(15)')
        print("the marker type is: " + mtype.text)
        ftype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(17)')
        print("the feature type is: " + ftype.text)
        biotype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(19)')
        print("the biotypes are: " + biotype.text)
        location = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(21)')
        print("the location is: " + location.text)
        mrkclip = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(23)')
        print("the marker detail clip is: " + mrkclip.text)  
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(symbol.text, 'AA414768 Public AA414768 Page', 'The Symbol is not correct!')
        self.assertEqual(mrkid.text, 'MGI:3035137', 'The MGI ID is not correct!')
        self.assertEqual(secid.text, 'MGI:3705633', 'The secondary IDs are not correct!')
        self.assertEqual(status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(name.text, 'expressed sequence AA414768', 'The Current Name is not correct!')
        self.assertEqual(syn.text, 'OTTMUSG00000017000', 'The Marker Synonyms are not correct!')
        self.assertEqual(mtype.text, 'Pseudogene', 'The Marker Type is not correct!')
        self.assertEqual(ftype.text, 'pseudogene', 'The Marker Feature Type is not correct!')
        self.assertEqual(biotype.text, 'Source Biotype Gene ID\nNCBI Gene Model protein-coding 245350\nEnsembl Gene Model processed_pseudogene ENSMUSG00000083307', 'The Marker Biotype is not correct!')
        self.assertEqual(location.text, 'ChrX:12803111-12804367 bp, + strand From Ensembl annotation of GRCm39', 'The Marker Location is not correct!')
        self.assertEqual(mrkclip.text, '', 'The Marker Detail Clip is not correct!')

    def test_mrk_det_type_other(self):
        """
        @status: Tests that a search by Marker Type Other Genome Feature basic results are returned, IE symbol, ID, Secondary IDs, Marker Status, Current Name, Synonym(s), 
        Marker Type, Feature Type, Biotypes, Location, and Marker Detail Clip
        @bug for right now biotypes are not available !!!, sorting of synonymns is being done by smart alpha with capitals being before lowercase
        @note pwi-mrk-det-search-8 passed 12/07/2020
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/')
        time.sleep(2)
        #find the Symbol field and enter the text      
        driver.find_element(By.ID, 'markerSymbol').send_keys('Acf1')        
        # Find the search button and click it.
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(3)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mrkDetailButton')))#waits until the results are displayed on the page by looking for the Marker Detail link to be displayed
        #Find the Marker Detail link and click it
        driver.find_element(By.ID, 'mrkDetailButton').click()
        time.sleep(3)
        driver.switch_to.window(self.driver.window_handles[1])
        symbol = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(2)')
        print("the symbol is: " + symbol.text)
        mrkid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(5)')
        print("the ID is: " + mrkid.text)
        secid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(7)')
        print("the secondary ID is: " + secid.text)
        status = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(9)')
        print("the marker status is: " + status.text)
        name = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(11)')
        print("the current name is: " + name.text)
        syn = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(13)')
        print("the synonym is: " + syn.text)
        mtype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(15)')
        print("the marker type is: " + mtype.text)
        ftype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(17)')
        print("the feature type is: " + ftype.text)
        biotype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(19)')
        print("the biotypes are: " + biotype.text)
        location = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(21)')
        print("the location is: " + location.text)
        mrkclip = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(23)')
        print("the marker detail clip is: " + mrkclip.text)  
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(symbol.text, 'Acf1 Public Acf1 Page', 'The Symbol is not correct!')
        self.assertEqual(mrkid.text, 'MGI:87875', 'The MGI ID is not correct!')
        self.assertEqual(secid.text, '[]', 'The secondary IDs are not correct!')
        self.assertEqual(status.text, 'official', 'The Marker Status is not correct!')
        self.assertEqual(name.text, 'albumin conformation factor 1', 'The Current Name is not correct!')
        self.assertEqual(syn.text, 'Acf-1', 'The Marker Synonyms are not correct!')
        self.assertEqual(mtype.text, 'Other Genome Feature', 'The Marker Type is not correct!')
        self.assertEqual(ftype.text, 'unclassified other genome feature', 'The Marker Feature Type is not correct!')
        self.assertEqual(biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(location.text, 'Chr1', 'The Marker Location is not correct!')
        self.assertEqual(mrkclip.text, '', 'The Marker Detail Clip is not correct!')
        
    def test_mrk_det_withdrawn_mrk(self):
        """
        @status: Tests that a withdrawn marker returns correctly
        @note pwi-mrk-det-search-10 !!broken because link does not work to marker detail! 12/07/2020
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/edit/marker/')  
        time.sleep(2)
        #find the Symbol field and enter the text      
        driver.find_element(By.ID, 'markerSymbol').send_keys('Ccm1')        
        # Find the search button and click it.
        driver.find_element(By.ID, 'searchButton').click()
        time.sleep(3)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mrkDetailButton')))#waits until the results are displayed on the page by looking for the Marker Detail link to be displayed
        #Find the Marker Detail link and click it
        driver.find_element(By.ID, 'mrkDetailButton').click()
        time.sleep(3)
        driver.switch_to.window(self.driver.window_handles[1])
        symbol = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(2)')
        print("the symbol is: " + symbol.text)
        mrkid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(5)')
        print("the ID is: " + mrkid.text)
        secid = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(7)')
        print("the secondary ID is: " + secid.text)
        status = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(9)')
        print("the marker status is: " + status.text)
        name = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(11)')
        print("the current name is: " + name.text)
        syn = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(13)')
        print("the synonym is: " + syn.text)
        mtype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(15)')
        print("the marker type is: " + mtype.text)
        ftype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(17)')
        print("the feature type is: " + ftype.text)
        biotype = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(19)')
        print("the biotypes are: " + biotype.text)
        location = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(21)')
        print("the location is: " + location.text)
        mrkclip = driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData > dd:nth-child(23)')
        print("the marker detail clip is: " + mrkclip.text)    
        #Verifies that the returned data is all correct for the 11 fields
        self.assertEqual(symbol.text, 'Ccm1 - Public Ccm1 Page', 'The Symbol is not correct!')
        self.assertEqual(mrkid.text, '', 'The MGI ID is not correct!')
        self.assertEqual(secid.text, '', 'The secondary IDs are not correct!')
        self.assertEqual(status.text, 'withdrawn', 'The Marker Status is not correct!')
        self.assertEqual(name.text, 'withdrawn, = Krit1', 'The Current Name is not correct!')
        self.assertEqual(syn.text, '', 'The Marker Synonyms are not correct!')
        self.assertEqual(mtype.text, 'Gene', 'The Marker Type is not correct!')
        self.assertEqual(ftype.text, '', 'The Marker Feature Type is not correct!')
        self.assertEqual(biotype.text, '', 'The Marker Biotype is not correct!')
        self.assertEqual(location.text, 'Chr5', 'The Marker Location is not correct!')
        self.assertEqual(mrkclip.text, '', 'The Marker Detail Clip is not correct!')
        

    def tearDown(self):
        self.driver.close()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPwiMrkDetail))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))