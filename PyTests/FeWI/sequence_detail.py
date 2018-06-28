'''
Created on Jun 26, 2018
These tests are for verifying functionality of a Sequence Detail page
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from util.form import ModuleForm
import sys,os.path
from util import wait, iterate
#from config.config import TEST_URL
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import TEST_URL

class TestSequenceDetail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.get("http://www.informatics.jax.org")
        #self.driver.get("http://bluebob.informatics.jax.org")
        self.form = ModuleForm(self.driver)
        self.driver.get(TEST_URL) 

    def test_mgp_fasta(self):
        """
        @status: Tests that an MGP sequence can be downloaded for FASTA
        @note: seqdetail-seq-1
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('"MGP_AKRJ_G0020754"')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        time.sleep(3)
        #find the GO button beside FASTA download and click it
        driver.find_element(By.XPATH, "//input[@value='Go']").click()
        #asserts that the correct sequence data is returned from FASTA
        assert "MGP_AKRJ_G0020754 13:94228187-94249372" in self.driver.page_source 
        wait.forAjax(driver)
   
    def test_mgp_ncbi_blast(self):
        """
        @status: Tests that an MGP sequence can be sent to NCBI Blast
        @note: seqdetail-seq-2 *** this test does not work because NCBI will not let Webdriver access it's page!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('"MGP_AKRJ_G0020754"')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        time.sleep(2)
        #find the sequence list and select the "forward to NCBI Blast" option
        self.driver.find_element(By.NAME, 'seqPullDownForm')
        Select(driver.find_element(By.NAME, 'seqPullDown')).select_by_visible_text('forward to NCBI BLAST')
        time.sleep(2)
        #find the GO button beside FASTA download and click it
        driver.find_element(By.XPATH, "//input[@value='Go']").click()
        time.sleep(2)
        #asserts that the correct blast page is returned by NCBI
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(2)
        #Identify the page title
        #page_header = self.driver.find_element(By.CLASS_NAME, 'pageTitle')      
        #asserts that the Page header is correct
        #self.assertEqual('Standard Nucleotide BLAST', page_header.text)         
        wait.forAjax(driver)

    def test_mgi_gm_fasta(self):
        """
        @status: Tests that an MGI gene model sequence can be downloaded for FASTA
        @note: seqdetail-seq-3
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('"MGI_C57BL6J_98660"')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        time.sleep(3)
        #find the GO button beside FASTA download and click it
        driver.find_element(By.XPATH, "//input[@value='Go']").click()
        #asserts that the correct sequence data is returned from FASTA
        assert "MGI_C57BL6J_98660 Y:2662471-2663658" in self.driver.page_source 
        wait.forAjax(driver)

    def test_mgi_gm_ncbi_blast(self):
        """
        @status: Tests that an MGI gene model sequence can be sent to NCBI Blast
        @note: seqdetail-seq-4 *** this test does not work because NCBI will not let Webdriver access it's page!!!
        """
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys('"MGI_C57BL6J_98660"')
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #finds the sequence link and clicks it
        driver.find_element(By.LINK_TEXT, 'Sequence').click()
        time.sleep(2)
        #find the sequence list and select the "forward to NCBI Blast" option
        self.driver.find_element(By.NAME, 'seqPullDownForm')
        Select(driver.find_element(By.NAME, 'seqPullDown')).select_by_visible_text('forward to NCBI BLAST')
        time.sleep(2)
        #find the GO button beside FASTA download and click it
        driver.find_element(By.XPATH, "//input[@value='Go']").click()
        time.sleep(2)
        #asserts that the correct blast page is returned by NCBI
        #switch focus to the new tab for strain detail page
        driver.switch_to_window(self.driver.window_handles[-1])
        time.sleep(2)
        #Identify the page title
        #page_header = self.driver.find_element(By.CLASS_NAME, 'pageTitle')      
        #asserts that the Page header is correct
        #self.assertEqual('Standard Nucleotide BLAST', page_header.text)         
        wait.forAjax(driver)
        
    def tearDown(self):
        self.driver.quit()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSequenceDetail))
    return suite

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.TestSequenceDetail']
    unittest.main()   