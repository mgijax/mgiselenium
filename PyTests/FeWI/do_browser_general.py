'''
Created on Jan 18, 2017
These tests are for verifying the correct data get returned for the heading section, along with default sorts and settings for the data returned.
The default tab to be displayed is the Term tab.
@author: jeffc
Verify term details
Verify alternate IDs for OMIM, EFO, KEGG, MESH and ORDO
Verify synonym data is displayed correctly when multiple synonyms exist
Verify alternate IDs are sorted correctly
'''
import unittest
import time
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys,os.path
from selenium.webdriver import firefox
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

tracemalloc.start()
class TestDoBrowserGeneral(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL)
        #self.driver.get("http://scrumdogdev.informatics.jax.org")
        self.driver.implicitly_wait(10)
        
    def test_dobrowser_header(self):
        '''
        @status this test verifies the term line in the header section on the DO browser page is correct.
        '''
        print ("BEGIN test_dobrowser_header")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:14330")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, "Parkinson's disease").click()
        #switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        header = self.driver.find_element(By.ID, 'diseaseNameID')#identifies the header section of the DO Browser page
        print(header.text)
        
        self.assertEqual(header.text, "Parkinson's disease (DOID:14330)")
        syn = self.driver.find_element(By.ID, 'diseaseSynonym')#identifies the synonym line in the header section of the DO Browser page
        print(syn.text)
        
        self.assertEqual(syn.text, "paralysis agitans; Parkinson disease")
        alt_id = self.driver.find_element(By.ID, 'diseaseSecondaryIDs')#identifies the alternate IDs line of the header section of the DO Browser page
        print(alt_id.text)
        
        self.assertIn(alt_id.text, "OMIM:607688, OMIM:610297, OMIM:613643, OMIM:614251, EFO:0002508, ICD10CM:G20, ICD9CM:332, ICD9CM:332.0, KEGG:05012, MESH:D010300, NCI:C26845, OMIM:PS168600, ORDO:2828, UMLS_CUI:C0030567")

        #locates and verifies the definition
        definition = self.driver.find_element(By.ID, 'diseaseDefinition')#identifies the Definition line of the header section of the DO Browser page
        print(definition.text)
        
        self.assertEqual(definition.text, "A synucleinopathy that has_material_basis_in degeneration of the central nervous system that often impairs motor skills, speech, and other functions.")
        
    def test_dobrowser_altIDs_links(self):
        '''
        @status this test verifies the alt IDs for OMIM, EFO, KEGG, MESH and ORDO are correct.
        '''
        print ("BEGIN test_dobrowser_altIDs_links")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:14330")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, "Parkinson's disease").click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'titleBarMainTitle'))):
            print('page loaded')
        header = self.driver.find_element(By.CSS_SELECTOR, '#diseaseNameID')#identifies the header section of the DO Browser page
        print(header.text)
        self.assertEqual(header.text, "Parkinson's disease (DOID:14330)")
        syn = self.driver.find_element(By.ID, 'diseaseSynonym')#identifies the synonym line in the header section of the DO Browser page
        print(syn.text)
        self.assertEqual(syn.text, "paralysis agitans; Parkinson disease")
        alt_id = self.driver.find_element(By.ID, 'diseaseSecondaryIDs')#identifies the alternate IDs line of the header section of the DO Browser page
        print(alt_id.text)
        self.assertIn(alt_id.text, "EFO:0002508, ICD10CM:G20, ICD9CM:332, ICD9CM:332.0, KEGG:05012, MESH:D010300, NCI:C26845, OMIM:PS168600, ORDO:2828, UMLS_CUI:C0030567 ")

        self.driver.find_element(By.LINK_TEXT, 'OMIM:PS168600').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'mimHeader'))):
            print('OMIM page loaded')
        print((self.driver.current_url))
        self.assertEqual(self.driver.current_url, 'https://www.omim.org/phenotypicSeries/PS168600', 'The OMIM link is broken!')
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'titleBarMainTitle'))):
            print('DO Browser page loaded')

        self.driver.find_element(By.LINK_TEXT, 'EFO:0002508').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        if WebDriverWait(self.driver, 4).until(EC.text_to_be_present_in_element((By.ID, 'TERM_ID'), 'EFO:0002508')):
            print('ebi page loaded')
        print((self.driver.current_url))
        self.assertEqual(self.driver.current_url, 'https://www.ebi.ac.uk/ols/ontologies/efo/terms?short_form=EFO_0002508', 'The EFO link is broken!')
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'titleBarMainTitle'))):
            print('DO Browser page loaded')

        self.driver.find_element(By.LINK_TEXT, 'KEGG:05012').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        if WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.ID, 'form1'))):
            print('kegg page loaded')
        print((self.driver.current_url))
        self.assertEqual(self.driver.current_url, 'https://www.genome.jp/dbget-bin/www_bget?map05012', 'The KEGG link is broken!')
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'titleBarMainTitle'))):
            print('DO Browser page loaded')
        
        self.driver.find_element(By.LINK_TEXT, 'MESH:D010300').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        if WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.ID, 'universal_header'))):
            print('Mesh page loaded')
        print((self.driver.current_url))
        self.assertEqual(self.driver.current_url, 'https://www.ncbi.nlm.nih.gov/mesh/D010300', 'The MESH link is broken!')
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'titleBarMainTitle'))):
            print('DO Browser page loaded')

        self.driver.find_element(By.LINK_TEXT, 'ORDO:2828').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        if WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.ID, 'introduction'))):
            print('ordo page loaded')
        print((self.driver.current_url))
        self.assertEqual(self.driver.current_url, 'https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=2828', 'The ORDO link is broken!')
        
    def test_dobrowser_mult_syn(self):
        '''
        @status this test verifies the synonym data is correctly displayed when multiple synonyms exist
        '''
        print ("BEGIN test_dobrowser_mult_syn")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:1700")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'X-linked ichthyosis').click()
        #switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        syn = self.driver.find_element(By.ID, 'diseaseSynonym')#identifies the synonym line in the header section of the DO Browser page
        print(syn.text)
        self.assertEqual(syn.text, "X-linked ichthyosis with steryl-sulphatase deficiency; X-linked placental steryl-sulphatase deficiency; X-linked recessive ichthyosis")
        
    def test_dobrowser_id_sort(self):
        '''
        @status this test verifies that the alternate IDs are sorted correctly. Rule is OMIM ids come first followed by all other in smart alpha order.
        '''
        print ("BEGIN test_dobrowser_id_sort")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:1700")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'X-linked ichthyosis').click()
        #switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        alt_id = self.driver.find_element(By.ID, 'diseaseSecondaryIDs')#identifies the alternate IDs line of the header section of the DO Browser page
        print(alt_id.text)
        self.assertEqual(alt_id.text, "OMIM:308100, ICD10CM:Q80.1, MESH:D016114, NCI:C84779, UMLS_CUI:C0079588")
        

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()
       
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDoBrowserGeneral))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
