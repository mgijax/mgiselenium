'''
Created on Jan 23, 2017
These test are for verifying the functionality of the Term detail tab of the DO Browser
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import HTMLTestRunner
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table



# Tests

class TestDoBrowserTermTab(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL)
        self.driver.implicitly_wait(10)
        
    def test_dobrowser_header(self):
        '''
        @status this test verifies the term line in the header section on the DO browser page is correct.
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:1324")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('lung cancer').click()
        wait.forAjax(self.driver)
        header = self.driver.find_element_by_id('diseaseNameID')#identifies the header section of the DO Browser page
        print header.text
        time.sleep(1)
        self.assertEqual(header.text, "lung cancer (DOID:1324)")
        syn = self.driver.find_element_by_id('diseaseSynonym')#identifies the synonym line in the header section of the DO Browser page
        print syn.text
        time.sleep(1)
        self.assertEqual(syn.text, "lung neoplasm")
        alt_id = self.driver.find_element_by_id('diseaseSecondaryIDs')#identifies the alternate IDs line of the header section of the DO Browser page
        print alt_id.text
        time.sleep(1)
        self.assertEqual(alt_id.text, "OMIM:211980, OMIM:608935, OMIM:612571, OMIM:612593, OMIM:614210, DOID:13075, DOID:1322, DOID:9881, ICD10CM:C34.1, ICD10CM:C34.2, ICD10CM:C34.3, ICD9CM:162.3, ICD9CM:162.4, ICD9CM:162.5, ICD9CM:162.8, UMLS_CUI:C0024624, UMLS_CUI:C0153491, UMLS_CUI:C0153492, UMLS_CUI:C0153493")
        #locates and verifies the definition
        definition = self.driver.find_element_by_id('diseaseDefinition')#identifies the Definition line of the header section of the DO Browser page
        print definition.text
        time.sleep(1)
        self.assertEqual(definition.text, "A respiratory system cancer that is located_in the lung.")
        
    def test_dobrowser_siblings(self):
        '''
        @status this test verifies the correct Parent Terms and Siblings are returned for this query. This test example has no children
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:12217")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('Lewy body dementia').click()
        wait.forAjax(self.driver)
        #locate the Parent Term box
        parent = self.driver.find_elements_by_id("termTabParentWrapper")#identifies all the parents found in the Parents term box
        searchTermItems = iterate.getTextAsList(parent)
        self.assertEqual(searchTermItems[0], "synucleinopathy +\ndementia +")
        print searchTermItems
        #locate the sublings terms box
        siblings = self.driver.find_elements_by_id("termTabTermWrapper")
        searchTermItems = iterate.getTextAsList(siblings)
        self.assertEquals(searchTermItems[0], "Lewy body dementia\n\nfrontotemporal dementia +\nmultiple system atrophy +\nParkinson's disease +\nvascular dementia", 'correct siblings are not being returned')
        
    def test_dobrowser_toplevel_siblings(self):
        '''
        @status this test verifies the correct Parent Term and Siblings are returned for this query. This test example verifies that when searching a top level term it's siblings are all returned.
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:225")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('syndrome').click()
        wait.forAjax(self.driver)
        #locate the Parent Term box
        parent = self.driver.find_elements_by_id("termTabParentWrapper")#identifies all the parents found in the Parents term box
        searchTermItems = iterate.getTextAsList(parent)
        self.assertEqual(searchTermItems[0], "disease +")
        print searchTermItems
        #locate the sublings terms box
        siblings = self.driver.find_elements_by_id("termTabTermWrapper")
        searchTermItems = iterate.getTextAsList(siblings)
        self.assertEquals(searchTermItems[0], "syndrome +\n\ndisease by infectious agent +\ndisease of anatomical entity +\ndisease of cellular proliferation +\ndisease of mental health +\ndisease of metabolism +\ngenetic disease +\nphysical disorder +", 'correct siblings are not being returned')
                
        
    def test_dobrowser_children(self):
        '''
        @status this test verifies the correct Parent Terms, Siblings, and Children are returned for this query. This test example has children
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:12365")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('malaria').click()
        wait.forAjax(self.driver)
        #locate the Parent Term box
        parent = self.driver.find_elements_by_id("termTabParentWrapper")#identifies all the parents found in the Parents term box
        searchTermItems = iterate.getTextAsList(parent)
        self.assertEqual(searchTermItems[0], "parasitic protozoa infectious disease +")
        print searchTermItems
        #locate the siblings terms box
        siblings = self.driver.find_elements_by_id("termTabTermWrapper")
        searchTermItems = iterate.getTextAsList(siblings)
        self.assertEquals(searchTermItems[0], "malaria +\n\namebiasis\nbabesiosis\nbalantidiasis\ncoccidiosis +\ndientamoebiasis\ngiardiasis\ngranulomatous amebic encephalitis\nleishmaniasis +\nprimary amebic meningoencephalitis\ntheileriasis\ntrichomoniasis\ntrypanosomiasis +")
        print searchTermItems
        #locate the children terms box
        children = self.driver.find_elements_by_id("termTabChildWrapper")
        searchTermItems = iterate.getTextAsList(children)
        self.assertEquals(searchTermItems[0], "blackwater fever\ncerebral malaria\nmixed malaria\nPlasmodium falciparum malaria\nPlasmodium malariae malaria\nPlasmodium ovale malaria\nPlasmodium vivax malaria")
        print searchTermItems

    def test_dobrowser_many_children(self):
        '''
        @status this test verifies the correct Parent Terms, Siblings, and Children are returned for this query. This test example has many children(shows no rollup used)
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:9562")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('primary ciliary dyskinesia').click()
        wait.forAjax(self.driver)
        #locate the Parent Term box
        parent = self.driver.find_elements_by_id("termTabParentWrapper")#identifies all the parents found in the Parents term box
        searchTermItems = iterate.getTextAsList(parent)
        self.assertEqual(searchTermItems[0], "ciliopathy +")
        print searchTermItems
        #locate the siblings terms box
        siblings = self.driver.find_elements_by_id("termTabTermWrapper")
        searchTermItems = iterate.getTextAsList(siblings)
        self.assertEquals(searchTermItems[0], "primary ciliary dyskinesia +\n\nJoubert syndrome +\nMeckel syndrome")
        print searchTermItems
        #locate the children terms box
        children = self.driver.find_elements_by_id("termTabChildWrapper")
        searchTermItems = iterate.getTextAsList(children)
        self.assertEquals(searchTermItems[0], "Kartagener syndrome\nprimary ciliary dyskinesia 1\nprimary ciliary dyskinesia 10\nprimary ciliary dyskinesia 11\nprimary ciliary dyskinesia 12\nprimary ciliary dyskinesia 13\nprimary ciliary dyskinesia 14\nprimary ciliary dyskinesia 15\nprimary ciliary dyskinesia 16\nprimary ciliary dyskinesia 17\nprimary ciliary dyskinesia 18\nprimary ciliary dyskinesia 19\nprimary ciliary dyskinesia 2\nprimary ciliary dyskinesia 20\nprimary ciliary dyskinesia 21\nprimary ciliary dyskinesia 22\nprimary ciliary dyskinesia 23\nprimary ciliary dyskinesia 24\nprimary ciliary dyskinesia 25\nprimary ciliary dyskinesia 26\nprimary ciliary dyskinesia 27\nprimary ciliary dyskinesia 28\nprimary ciliary dyskinesia 29\nprimary ciliary dyskinesia 3\nprimary ciliary dyskinesia 30\nprimary ciliary dyskinesia 32\nprimary ciliary dyskinesia 33\nprimary ciliary dyskinesia 34\nprimary ciliary dyskinesia 35\nprimary ciliary dyskinesia 4\nprimary ciliary dyskinesia 5\nprimary ciliary dyskinesia 6\nprimary ciliary dyskinesia 7\nprimary ciliary dyskinesia 8\nprimary ciliary dyskinesia 9\nStromme syndrome")
        print searchTermItems

    def test_dobrowser_noomim(self):
        '''
        @status this test verifies the correct Parent Terms and Siblings are returned for this query. This test example has no children because it has no OMIM
        and no annotations
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:14332")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('postencephalitic Parkinson disease').click()
        wait.forAjax(self.driver)
        #locate the Parent Term box
        parent = self.driver.find_elements_by_id("termTabParentWrapper")#identifies all the parents found in the Parents term box
        searchTermItems = iterate.getTextAsList(parent)
        self.assertEqual(searchTermItems[0], "secondary Parkinson disease +")
        print searchTermItems
        #locate the siblings terms box
        siblings = self.driver.find_elements_by_id("termTabTermWrapper")
        searchTermItems = iterate.getTextAsList(siblings)
        self.assertEquals(searchTermItems[0], "postencephalitic Parkinson disease")
        print searchTermItems

    def test_dobrowser_child_of_children(self):
        '''
        @status this test verifies the correct Parent Terms, Siblings, and Children are returned for this query. This test example verifies
        that when a child term has children it's followed by a + sign
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:680")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('tauopathy').click()
        wait.forAjax(self.driver)
        #locate the Parent Term box
        parent = self.driver.find_elements_by_id("termTabParentWrapper")#identifies all the parents found in the Parents term box
        searchTermItems = iterate.getTextAsList(parent)
        self.assertEqual(searchTermItems[0], "neurodegenerative disease +")
        print searchTermItems
        #locate the siblings terms box
        siblings = self.driver.find_elements_by_id("termTabTermWrapper")
        searchTermItems = iterate.getTextAsList(siblings)
        self.assertEquals(searchTermItems[0], "tauopathy +\n\nagenesis of the corpus callosum with peripheral neuropathy\ndemyelinating disease +\neye degenerative disease +\neyelid degenerative disease +\nfamilial encephalopathy with neuroserpin inclusion bodies\nhereditary ataxia +\nHuntington disease-like 2\nHuntington's disease\ninfantile cerebellar-retinal degeneration\nLafora disease\nmotor neuron disease +\nmyoclonic cerebellar dyssynergia\nneuroacanthocytosis +\nneurodegeneration with brain iron accumulation +\nolivopontocerebellar atrophy\nPick's disease\nplexopathy\npontocerebellar hypoplasia +\nprimary cerebellar degeneration\nsecondary Parkinson disease +\nSPOAN syndrome\nsynucleinopathy +")
        print searchTermItems
        #locate the children terms box
        children = self.driver.find_elements_by_id("termTabChildWrapper")
        searchTermItems = iterate.getTextAsList(children)
        self.assertEquals(searchTermItems[0], "Alzheimer's disease +")
        print searchTermItems
            
        def tearDown(self):
            self.driver.close()
        '''
        def suite():
            suite = unittest.TestSuite()
            suite.addTest(unittest.makeSuite(TestAdd))
            return suite
        '''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main() 
