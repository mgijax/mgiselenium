"""
Created on Jan 23, 2017
These test are for verifying the functionality of the Term detail tab of the DO Browser
@author: jeffc
Verify DO browser heading information
Verify DO browser terms with siblings display properly
Verify DO browser top level terms also display their siblings
Verify DO browser displays proper terms, siblings and children
Verify Do browser displays proper terms, siblings and many children
Verify DO browser display when a term has no OMIM ID/no annotations
Verify DO browser display when verifies that when a child term has children it's followed by a + sign
"""
import os.path
import sys
import time
import tracemalloc
import unittest

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config import TEST_URL
from util import iterate

# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)

# Tests
tracemalloc.start()
class TestDoBrowserTermTab(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(TEST_URL)
        self.driver.implicitly_wait(10)
        
    def test_dobrowser_header(self):
        """
        @status this test verifies the term line in the header section on the DO browser page is correct.
        """
        print("BEGIN test_dobrowser_header")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:1324")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'lung cancer').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'genesTabButton'))):
            print('page loaded')
        header = self.driver.find_element(By.ID, 'diseaseNameID')  # identifies the header section of the DO Browser page
        print(header.text)
        
        self.assertEqual(header.text, "lung cancer (DOID:1324)")
        syn = self.driver.find_element(By.ID, 'diseaseSynonym')  # identifies the synonym line in the header section of the DO Browser page
        print(syn.text)
        
        self.assertEqual(syn.text, "lung neoplasm")
        alt_id = self.driver.find_element(By.ID, 'diseaseSecondaryIDs')  # identifies the alternate IDs line of the header section of the DO Browser page
        print(alt_id.text)
        
        self.assertEqual(alt_id.text, "OMIM:211980, OMIM:608935, OMIM:612571, OMIM:612593, OMIM:614210, DOID:13075, DOID:1322, DOID:9881, ICD10CM:C34.1, ICD10CM:C34.2, ICD10CM:C34.3, ICD9CM:162.3, ICD9CM:162.4, ICD9CM:162.5, ICD9CM:162.8, UMLS_CUI:C0024624, UMLS_CUI:C0153491, UMLS_CUI:C0153492, UMLS_CUI:C0153493")
        # locates and verifies the definition
        definition = self.driver.find_element(By.ID, 'diseaseDefinition')  # identifies the Definition line of the header section of the DO Browser page
        print(definition.text)
        
        self.assertEqual(definition.text, "A respiratory system cancer that is located_in the lung.")
        
    def test_dobrowser_siblings(self):
        """
        @status this test verifies the correct Parent Terms and Siblings are returned for this query. This test example has no children
        """
        print("BEGIN test_dobrowser_siblings")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:12217")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'Lewy body dementia').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'genesTabButton'))):
            print('page loaded')
        # locate the Parent Term box
        parent = self.driver.find_elements(By.ID, 'termTabParentWrapper')  # identifies all the parents found in the Parents term box
        searchtermitems = iterate.getTextAsList(parent)
        self.assertEqual(searchtermitems[0], "dementia +")
        print(searchtermitems)
        # locate the sublings terms box
        siblings = self.driver.find_elements(By.ID, 'termTabTermWrapper')
        searchtermitems = iterate.getTextAsList(siblings)
        self.assertEqual(searchtermitems[0], "Lewy body dementia\n\nfrontotemporal dementia +\nvascular dementia", 'correct siblings are not being returned')
        
    def test_dobrowser_toplevel_siblings(self):
        """
        @status this test verifies the correct Parent Term and Siblings are returned for this query. This test example verifies that when searching a top level term it's siblings are all returned.
        """
        print("BEGIN test_dobrowser_toplevel_siblings")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:225")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(5)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'syndrome').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'genesTabButton'))):
            print('page loaded')
        # locate the Parent Term box
        parent = self.driver.find_elements(By.ID, 'termTabParentWrapper')  # identifies all the parents found in the Parents term box
        searchtermitems = iterate.getTextAsList(parent)
        self.assertEqual(searchtermitems[0], "disease +")
        print(searchtermitems)
        # locate the sublings terms box
        siblings = self.driver.find_elements(By.ID, 'termTabTermWrapper')
        searchtermitems = iterate.getTextAsList(siblings)
        self.assertEqual(searchtermitems[0], "syndrome +\n\ndisease by infectious agent +\ndisease of anatomical entity +\ndisease of cellular proliferation +\ndisease of mental health +\ndisease of metabolism +\ngenetic disease +\nphysical disorder +", 'correct siblings are not being returned')
                
        
    def test_dobrowser_children(self):
        """
        @status this test verifies the correct Parent Terms, Siblings, and Children are returned for this query. This test example has children
        """
        print("BEGIN test_dobrowser_children")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:12365")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'malaria').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'genesTabButton'))):
            print('page loaded')
        # locate the Parent Term box
        parent = self.driver.find_elements(By.ID, 'termTabParentWrapper')  # identifies all the parents found in the Parents term box
        searchtermitems = iterate.getTextAsList(parent)
        self.assertEqual(searchtermitems[0], "parasitic protozoa infectious disease +")
        print(searchtermitems)
        # locate the siblings terms box
        siblings = self.driver.find_elements(By.ID, 'termTabTermWrapper')
        searchtermitems = iterate.getTextAsList(siblings)
        self.assertEqual(searchtermitems[0], "malaria +\n\namebiasis\nbabesiosis\nbalantidiasis\ncoccidiosis +\ndientamoebiasis\ngiardiasis\nleishmaniasis +\nprimary amebic meningoencephalitis +\ntheileriasis\ntrichomoniasis +\ntrypanosomiasis +")
        print(searchtermitems)
        # locate the children terms box
        children = self.driver.find_elements(By.ID, 'termTabChildWrapper')
        searchtermitems = iterate.getTextAsList(children)
        self.assertEqual(searchtermitems[0], "blackwater fever\ncerebral malaria\nmixed malaria\nPlasmodium falciparum malaria\nPlasmodium malariae malaria\nPlasmodium ovale malaria\nPlasmodium vivax malaria")
        print(searchtermitems)

    def test_dobrowser_many_children(self):
        """
        @status this test verifies the correct Parent Terms, Siblings, and Children are returned for this query. This test example has many children(shows no rollup used)
        @bug: fails because sort order of children terms is no longer smart alpha!!!!!! temporarily fixed(10/21/2020)
        """
        print("BEGIN test_dobrowser_many_children")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:9562")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'primary ciliary dyskinesia').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'genesTabButton'))):
            print('page loaded')
        # locate the Parent Term box
        parent = self.driver.find_elements(By.ID, 'termTabParentWrapper')  # identifies all the parents found in the Parents term box
        searchtermitems = iterate.getTextAsList(parent)
        self.assertEqual(searchtermitems[0], "ciliopathy +")
        print(searchtermitems)
        # locate the siblings terms box
        siblings = self.driver.find_elements(By.ID, 'termTabTermWrapper')
        searchtermitems = iterate.getTextAsList(siblings)
        self.assertEqual(searchtermitems[0], "primary ciliary dyskinesia +\n\nJoubert syndrome +\nMeckel syndrome +")
        print(searchtermitems)
        # locate the children terms box
        children = self.driver.find_elements(By.ID, 'termTabChildWrapper')
        searchtermitems = iterate.getTextAsList(children)
        self.assertEqual(searchtermitems[0], "Kartagener syndrome\nprimary ciliary dyskinesia 1\nprimary ciliary dyskinesia 10\nprimary ciliary dyskinesia 11\nprimary ciliary dyskinesia 12\nprimary ciliary dyskinesia 13\nprimary ciliary dyskinesia 14\nprimary ciliary dyskinesia 15\nprimary ciliary dyskinesia 16\nprimary ciliary dyskinesia 17\nprimary ciliary dyskinesia 18\nprimary ciliary dyskinesia 19\nprimary ciliary dyskinesia 2\nprimary ciliary dyskinesia 20\nprimary ciliary dyskinesia 21\nprimary ciliary dyskinesia 22\nprimary ciliary dyskinesia 23\nprimary ciliary dyskinesia 24\nprimary ciliary dyskinesia 25\nprimary ciliary dyskinesia 26\nprimary ciliary dyskinesia 27\nprimary ciliary dyskinesia 28\nprimary ciliary dyskinesia 29\nprimary ciliary dyskinesia 3\nprimary ciliary dyskinesia 30\nprimary ciliary dyskinesia 32\nprimary ciliary dyskinesia 33\nprimary ciliary dyskinesia 34\nprimary ciliary dyskinesia 35\nprimary ciliary dyskinesia 36\nprimary ciliary dyskinesia 37\nprimary ciliary dyskinesia 38\nprimary ciliary dyskinesia 39\nprimary ciliary dyskinesia 4\nprimary ciliary dyskinesia 40\nprimary ciliary dyskinesia 41\nprimary ciliary dyskinesia 42\nprimary ciliary dyskinesia 43\nprimary ciliary dyskinesia 44\nprimary ciliary dyskinesia 45\nprimary ciliary dyskinesia 5\nprimary ciliary dyskinesia 6\nprimary ciliary dyskinesia 7\nprimary ciliary dyskinesia 8\nprimary ciliary dyskinesia 9\nStromme syndrome")
        print(searchtermitems)

    def test_dobrowser_noomim(self):
        """
        @status this test verifies the correct Parent Terms and Siblings are returned for this query. This test example has no children because it has no OMIM
        and no annotations
        """
        print("BEGIN test_dobrowser_noomim")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:14332")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'postencephalitic Parkinson disease').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'genesTabButton'))):
            print('page loaded')
        # locate the Parent Term box
        parent = self.driver.find_elements(By.ID, 'termTabParentWrapper')  # identifies all the parents found in the Parents term box
        searchtermitems = iterate.getTextAsList(parent)
        self.assertEqual(searchtermitems[0], "secondary Parkinson disease +")
        print(searchtermitems)
        # locate the siblings terms box
        siblings = self.driver.find_elements(By.ID, 'termTabTermWrapper')
        searchtermitems = iterate.getTextAsList(siblings)
        self.assertEqual(searchtermitems[0], "postencephalitic Parkinson disease")
        print(searchtermitems)

    def test_dobrowser_child_of_children(self):
        """
        @status this test verifies the correct Parent Terms, Siblings, and Children are returned for this query. This test example verifies
        that when a child term has children it's followed by a + sign
        """
        print("BEGIN test_dobrowser_child_of_children")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:680")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'tauopathy').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'genesTabButton'))):
            print('page loaded')
        # locate the Parent Term box
        parent = self.driver.find_elements(By.ID, 'termTabParentWrapper')  # identifies all the parents found in the Parents term box
        searchtermitems = iterate.getTextAsList(parent)
        self.assertEqual(searchtermitems[0], "neurodegenerative disease +")
        print(searchtermitems)
        # locate the siblings terms box
        siblings = self.driver.find_elements(By.ID, 'termTabTermWrapper')
        searchtermitems = iterate.getTextAsList(siblings)
        self.assertIn(searchtermitems[0], "tauopathy +\n\nagenesis of the corpus callosum with peripheral neuropathy\namyotrophic lateral sclerosis-parkinsonism/dementia complex 1\nchildhood-onset neurodegeneration with brain atrophy\nfamilial encephalopathy with neuroserpin inclusion bodies\nhereditary ataxia +\nHuntington's disease\nHuntington's disease-like 2\ninfantile cerebellar-retinal degeneration\nmotor neuron disease +\nmyoclonic cerebellar dyssynergia\nneuroacanthocytosis +\nneurodegeneration with ataxia, dystonia, and gaze palsy, childhood-onset\nneurodegeneration with brain iron accumulation +\nneurodevelopmental disorder with regression, abnormal movements, loss of speech, and seizures\nneuronal intranuclear inclusion disease\nolivopontocerebellar atrophy\nPick's disease\nplexopathy\npontocerebellar hypoplasia +\nprimary cerebellar degeneration\nsecondary Parkinson disease +\nSPOAN syndrome\nstress-induced childhood-onset neurodegeneration with variable ataxia and seizures\nsynucleinopathy +")
        print(searchtermitems)
        # locate the children terms box
        children = self.driver.find_elements(By.ID, 'termTabChildWrapper')
        searchtermitems = iterate.getTextAsList(children)
        self.assertEqual(searchtermitems[0], "Alzheimer's disease +\nchronic traumatic encephalopathy")
        print(searchtermitems)
            
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDoBrowserTermTab))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
