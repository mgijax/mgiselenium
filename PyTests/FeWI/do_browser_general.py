'''
Created on Jan 18, 2017
These tests are for verifying the correct data get returned for the heading section, along with default sorts and settings for the data returned.
The default tab to be displayed is the Term tab.
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


class TestDoBrowserGeneral(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.get(config.TEST_URL)
        self.driver.get("http://scrumdogdev.informatics.jax.org")
        self.driver.implicitly_wait(10)
        
    def test_dobrowser_header(self):
        '''
        @status this test verifies the term line in the header section on the DO browser page is correct.
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:14330")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text("Parkinson's disease").click()
        wait.forAjax(self.driver)
        header = self.driver.find_element_by_id('diseaseNameID')#identifies the header section of the DO Browser page
        print header.text
        time.sleep(1)
        self.assertEqual(header.text, "Parkinson's disease (DOID:14330)")
        syn = self.driver.find_element_by_id('diseaseSynonym')#identifies the synonym line in the header section of the DO Browser page
        print syn.text
        time.sleep(1)
        self.assertEqual(syn.text, "paralysis agitans; Parkinson disease")
        alt_id = self.driver.find_element_by_id('diseaseSecondaryIDs')#identifies the alternate IDs line of the header section of the DO Browser page
        print alt_id.text
        time.sleep(1)
        self.assertEqual(alt_id.text, "OMIM:168600, OMIM:260300, OMIM:300557, OMIM:556500, OMIM:602404, OMIM:605543, OMIM:606324, OMIM:606852, OMIM:607060, OMIM:607688, OMIM:610297, OMIM:612953, OMIM:613164, OMIM:613643, OMIM:614203, OMIM:614251, OMIM:615528, OMIM:615530, EFO:0002508, ICD10CM:G20, ICD9CM:332, ICD9CM:332.0, KEGG:05012, MESH:D010300, NCI:C26845, ORDO:2828, UMLS_CUI:C0030567")

        #locates and verifies the definition
        definition = self.driver.find_element_by_id('diseaseDefinition')#identifies the Definition line of the header section of the DO Browser page
        print definition.text
        time.sleep(1)
        self.assertEqual(definition.text, "A synucleinopathy that has_material_basis_in degeneration of the central nervous system that often impairs motor skills, speech, and other functions.")
        
    def test_dobrowser_altIDs_links(self):
        '''
        @status this test verifies the alt IDs for OMIM, EFO, KEGG, MESH and ORDO are correct.
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:14330")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text("Parkinson's disease").click()
        wait.forAjax(self.driver)
        header = self.driver.find_element_by_id('diseaseNameID')#identifies the header section of the DO Browser page
        print header.text
        time.sleep(1)
        self.assertEqual(header.text, "Parkinson's disease (DOID:14330)")
        syn = self.driver.find_element_by_id('diseaseSynonym')#identifies the synonym line in the header section of the DO Browser page
        print syn.text
        time.sleep(1)
        self.assertEqual(syn.text, "paralysis agitans; Parkinson disease")
        alt_id = self.driver.find_element_by_id('diseaseSecondaryIDs')#identifies the alternate IDs line of the header section of the DO Browser page
        print alt_id.text
        time.sleep(1)
        self.assertEqual(alt_id.text, "OMIM:168600, OMIM:260300, OMIM:300557, OMIM:556500, OMIM:602404, OMIM:605543, OMIM:606324, OMIM:606852, OMIM:607060, OMIM:607688, OMIM:610297, OMIM:612953, OMIM:613164, OMIM:613643, OMIM:614203, OMIM:614251, OMIM:615528, OMIM:615530, EFO:0002508, ICD10CM:G20, ICD9CM:332, ICD9CM:332.0, KEGG:05012, MESH:D010300, NCI:C26845, ORDO:2828, UMLS_CUI:C0030567")
        self.driver.find_element_by_link_text('OMIM:168600').click()
        time.sleep(1)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        print (self.driver.current_url)
        self.assertEqual(self.driver.current_url, 'http://www.omim.org/entry/168600', 'The OMIM link is broken!')
        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(1)
        self.driver.find_element_by_link_text('EFO:0002508').click()
        time.sleep(1)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        print (self.driver.current_url)
        self.assertEqual(self.driver.current_url, 'http://www.ebi.ac.uk/ols/ontologies/efo/terms?short_form=EFO_0002508', 'The EFO link is broken!')
        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(1)
        self.driver.find_element_by_link_text('KEGG:05012').click()
        time.sleep(1)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        print (self.driver.current_url)
        self.assertEqual(self.driver.current_url, 'http://www.genome.jp/dbget-bin/www_bget?map05012', 'The KEGG link is broken!')
        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(1)
        self.driver.find_element_by_link_text('MESH:D010300').click()
        time.sleep(1)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        print (self.driver.current_url)
        self.assertEqual(self.driver.current_url, 'https://www.nlm.nih.gov/cgi/mesh/2011/MB_cgi?exact&field=uid&term=D010300', 'The MESH link is broken!')
        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(1)
        self.driver.find_element_by_link_text('ORDO:2828').click()
        time.sleep(1)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        print (self.driver.current_url)
        self.assertEqual(self.driver.current_url, 'http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=2828', 'The ORDO link is broken!')
        
    def test_dobrowser_mult_syn(self):
        '''
        @status this test verifies the synonym data is correctly displayed when multiple synonyms exist
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:1700")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('X-linked ichthyosis').click()
        wait.forAjax(self.driver)
        syn = self.driver.find_element_by_id('diseaseSynonym')#identifies the synonym line in the header section of the DO Browser page
        print syn.text
        time.sleep(1)
        self.assertEqual(syn.text, "X-linked ichthyosis with steryl-sulphatase deficiency; X-linked placental steryl-sulphatase deficiency; X-linked recessive ichthyosis")
        
    def test_dobrowser_id_sort(self):
        '''
        @status this test verifies that the alternate IDs are sorted correctly. Rule is OMIM ids come first followed by all other in smart alpha order.
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:1700")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('X-linked ichthyosis').click()
        wait.forAjax(self.driver)
        alt_id = self.driver.find_element_by_id('diseaseSecondaryIDs')#identifies the alternate IDs line of the header section of the DO Browser page
        print alt_id.text
        time.sleep(1)
        self.assertEqual(alt_id.text, "OMIM:308100, ICD10CM:Q80.1, MESH:D016114, NCI:C84779, UMLS_CUI:C0079588")
        

    def tearDown(self):
        self.driver.close()
       
        '''
        These tests should NEVER!!!! be run against a production system!!
        def suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(TestAdd))
        return suite
        '''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main() 
