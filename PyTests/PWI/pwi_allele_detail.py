'''
Created on Nov 22, 2016
These tests start out using the Marker form THE MARKER FORM IS NOW GONE reevaluate these tests!
@author: jeffc
'''

import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import sys,os.path
from util import wait, iterate
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import TEST_PWI_URL

class TestPwiAlleleDetail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome() 

    def test_disease_annotations(self):
        """
        @status: Tests that the disease annotations section is correct, this section now has both OMIM and DO annotations.
        @note rewritten on 4/8/2022
        """
        driver = self.driver
        #opens the PWI
        driver.get(TEST_PWI_URL)
        time.sleep(5)
        #find the Acc ID(s) / Gene Symbol box and enter text
        accbox = driver.find_element(By.NAME, 'ids')
        # put your marker symbol in the box
        accbox.send_keys("MGI:97490")
        accbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Public Pax6 Page')))#waits until the Public Pax6 Page link is displayed on the page
        driver.find_element(By.LINK_TEXT, "Alleles").click()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Sey-Dey')))#waits until the allele link for Pax6<Sey-Dey> is displayed on the page
        driver.find_element(By.PARTIAL_LINK_TEXT, "Sey-Dey").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Public Allele Detail Page')))#waits until the link 'Public Allele Detail Page' is displayed on the page
        #Locates the summary table and finds the table headings
        #driver.find_element(By.CSS_SELECTOR, 'div.genotypeDetail:nth-child(3)')
        #driver.find_element(By.CSS_SELECTOR, 'dl.detailPageListData:nth-child(1)')
        #driver.find_elements(By.TAG_NAME, 'dd.detailPageListData')
        #data = driver.find_elements(By.TAG_NAME, 'a')
        #print (iterate.getTextAsList(data))#prints out almost all data found on this page, hopefully someday  I can figure out how to capture just the disease annotations section.
        time.sleep(5)
        element = driver.find_elements(By.CSS_SELECTOR, 'dl.detailPageListData:nth-child(13) > dd:nth-child(4) > a:nth-child(1)')
        # iterate through list and get text
        for i in element:
            print("Classes:"+ i.text)
        time.sleep(2)        
        #asserts that all the disease annotations data is correct for MGI:2175204 Pax6Sey-Dey/Pax6+
        self.assertIn(i.text, "Term\naniridia\nDO ID\nDOID:12271\nReference\nJ:10820\nTerm\nWAGR syndrome (NOT)\nDO ID\nDOID:14515\nReference\nJ:10820")

    def test_AlleleDet_multi_synonymns(self):
        """
        @status: Tests that the PWI Allele detail page displays multiple synonyms correctly.
        @note written on 4/8/2022 CRM-249
        """
        driver = self.driver
        #opens the PWI
        driver.get(TEST_PWI_URL)
        time.sleep(5)
        #find the Acc ID(s) / Gene Symbol box and enter text
        accbox = driver.find_element(By.NAME, 'ids')
        # put your allele ID in the box
        accbox.send_keys("MGI:3530323")
        accbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Public Allele Detail Page')))#waits until the Public Pax6 Allele Detail link is displayed on the page
        #find the data in the Synonym(s) field
        syn = driver.find_element(By.CSS_SELECTOR, "dd.ng-binding:nth-child(14)")
        print(syn.text)  
        #asserts that all the synonym(s) data is correct
        self.assertIn(syn.text, "KitGsfsow3, KitSow3, phenotype like Sl or W 3, SOW3")        

    def test_AlleleDet_multi_cell_lines(self):
        """
        @status: Tests that the PWI Allele detail page displays multiple cell lines correctly.
        @note written on 4/8/2022 CRM-249
        """
        driver = self.driver
        #opens the PWI
        driver.get(TEST_PWI_URL)
        time.sleep(5)
        #find the Acc ID(s) / Gene Symbol box and enter text
        accbox = driver.find_element(By.NAME, 'ids')
        # put your allele ID in the box
        accbox.send_keys("MGI:3796212")
        accbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Public Allele Detail Page')))#waits until the Public Pax6 Allele Detail link is displayed on the page
        #find the data in the Mutant Cell Line field
        mcl = driver.find_element(By.CSS_SELECTOR, "dl.detailPageListData:nth-child(5) > dd:nth-child(2)")
        print(mcl.text)  
        #asserts that all the mutant cell line data is correct
        self.assertIn(mcl.text, "10013C-A4, 10013C-B11, 10013C-E10, 10013C-E5, 10013D-B12, 10013D-H7")        

    def test_AlleleDet_driver_induc_note(self):
        """
        @status: Tests that the PWI Allele detail page displays a gene driver with Inducible note correctly.
        @note written on 4/8/2022 CRM-249
        """
        driver = self.driver
        #opens the PWI
        driver.get(TEST_PWI_URL)
        time.sleep(5)
        #find the Acc ID(s) / Gene Symbol box and enter text
        accbox = driver.find_element(By.NAME, 'ids')
        # put your allele ID in the box
        accbox.send_keys("MGI:6724081")
        accbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Public Allele Detail Page')))#waits until the Public Pax6 Allele Detail link is displayed on the page
        #find the data in the Driver Gene field
        dvrgene = driver.find_element(By.CSS_SELECTOR, "dl.detailPageListData:nth-child(3) > dd:nth-child(20)")
        print(dvrgene.text)  
        #asserts that all the driver gene data is correct
        self.assertIn(dvrgene.text, "Axin2 ")        
        #find the data in the Inducible Note field
        indnote = driver.find_element(By.CSS_SELECTOR, "dl.detailPageListData:nth-child(3) > dd:nth-child(22)")
        print(indnote.text)  
        #asserts that the Inducible Note data is correct
        self.assertIn(indnote.text, "tamoxifen ")        

    def test_AlleleDet_gen_note_mrkclip(self):
        """
        @status: Tests that the PWI Allele detail page displays a general note and marker clip correctly.
        @note written on 4/8/2022 CRM-249
        """
        driver = self.driver
        #opens the PWI
        driver.get(TEST_PWI_URL)
        time.sleep(5)
        #find the Acc ID(s) / Gene Symbol box and enter text
        accbox = driver.find_element(By.NAME, 'ids')
        # put your allele ID in the box
        accbox.send_keys("MGI:7257816")
        accbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Public Allele Detail Page')))#waits until the Public Pax6 Allele Detail link is displayed on the page
        #find the data in the general note field
        gennote = driver.find_element(By.CSS_SELECTOR, "dl.detailPageListData:nth-child(9) > dd:nth-child(6)")
        print(gennote.text)  
        #asserts that all the general note data is correct
        self.assertIn(gennote.text, "The version of this allele that does not contain the neomycin selection cassette, Opn4tm1.1(cre)Saha, has been analyzed. ")        
        #find the data in the marker detail clip field
        mrkclip = driver.find_element(By.CSS_SELECTOR, "dl.detailPageListData:nth-child(9) > dd:nth-child(8)")
        print(mrkclip.text)  
        #asserts that the Marker Detail Clip data is correct
        self.assertIn(mrkclip.text, "Homozygous inactivation of this gene results in absent intrinsic inner retinal photosensitivity, abnormal pupillary reflex, and abnormal circadian rhythms. ")    

    def test_AlleleDet_colony_note(self):
        """
        @status: Tests that the PWI Allele detail page displays a IKMC Colony Name Note correctly.
        @note written on 4/8/2022 CRM-249
        """
        driver = self.driver
        #opens the PWI
        driver.get(TEST_PWI_URL)
        time.sleep(5)
        #find the Acc ID(s) / Gene Symbol box and enter text
        accbox = driver.find_element(By.NAME, 'ids')
        # put your allele ID in the box
        accbox.send_keys("MGI:7257808")
        accbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Public Allele Detail Page')))#waits until the Public Pax6 Allele Detail link is displayed on the page
        #find the data in the IKMC Colony Name Note field
        colonynote = driver.find_element(By.CSS_SELECTOR, "dl.detailPageListData:nth-child(9) > dd:nth-child(4)")
        print(colonynote.text)  
        #asserts that the IKMC Colony Name Note data is correct
        self.assertIn(colonynote.text, "ABFH ")  

    def test_AlleleDet_high_lvl_pheno(self):
        """
        @status: Tests that the PWI Allele detail page displays the high level phenotype terms correctly sorted.
        @note written on 4/8/2022 CRM-250. this test will be redone once a better example of sort is done.
        """
        driver = self.driver
        #opens the PWI
        driver.get(TEST_PWI_URL)
        time.sleep(5)
        #find the Acc ID(s) / Gene Symbol box and enter text
        accbox = driver.find_element(By.NAME, 'ids')
        # put your allele ID in the box
        accbox.send_keys("MGI:5567084")
        accbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Public Allele Detail Page')))#waits until the Public Pax6 Allele Detail link is displayed on the page
        time.sleep(4)
        #find the high level phenotype terms for the third genotype
        high_lvl_term1 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(7) > div:nth-child(3) > span:nth-child(1)")
        high_lvl_term2 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(7) > div:nth-child(4) > span:nth-child(1)")
        high_lvl_term3 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(7) > div:nth-child(5) > span:nth-child(1)")
        print(high_lvl_term1.text)
        print(high_lvl_term2.text)
        print(high_lvl_term3.text)  
        #asserts that the terms are correct and in the correct order
        self.assertIn(high_lvl_term1.text, "vision/eye phenotype")  
        self.assertIn(high_lvl_term2.text, "cellular phenotype")
        self.assertIn(high_lvl_term3.text, "nervous system phenotype")

    def test_AlleleDet_all_lvls_pheno(self):
        """
        @status: Tests that the PWI Allele detail page displays all levels of  phenotype terms correctly sorted.
        @note written on 6/29/2022 CRM-282. 
        """
        driver = self.driver
        #opens the PWI
        driver.get(TEST_PWI_URL)
        time.sleep(5)
        #find the Acc ID(s) / Gene Symbol box and enter text
        accbox = driver.find_element(By.NAME, 'ids')
        # put your allele ID in the box
        accbox.send_keys("MGI:1861932")
        accbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.genotypeDetail:nth-child(1024) > dl:nth-child(1) > dd:nth-child(6)')))#waits until the last phenotype annotation MGI ID is displayed on the page
        time.sleep(4)
        #find the high level phenotype terms for the forth genotype(MGI:3852467 (key 46893))
        high_lvl_term1 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(82) > div:nth-child(3) > span:nth-child(1)")
        high_lvl_term2 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(82) > div:nth-child(4) > span:nth-child(1)")
        high_lvl_term3 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(82) > div:nth-child(5) > span:nth-child(1)")
        print(high_lvl_term1.text)
        print(high_lvl_term2.text)
        print(high_lvl_term3.text)  
        #asserts that the terms are correct and in the correct order
        self.assertIn(high_lvl_term1.text, "embryo phenotype")  
        self.assertIn(high_lvl_term2.text, "nervous system phenotype")
        self.assertIn(high_lvl_term3.text, "cardiovascular system phenotype")
        time.sleep(4)
        #find the phenotype terms MGI IDs for the first 20 0r 21 annotations to verify sort order
        pheno_id1 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(2) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id2 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(9) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id3 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(16) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id4 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(82) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id5 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(87) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id6 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(88) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id7 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(92) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id8 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(99) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id9 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(100) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id10 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(101) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id11 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(102) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id12 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(103) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id13 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(104) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id14 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(105) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id15 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(108) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id16 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(110) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id17 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(111) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id18 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(112) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id19 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(113) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id20 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(115) > dl:nth-child(1) > dd:nth-child(6)")
        pheno_id21 = driver.find_element(By.CSS_SELECTOR, "div.genotypeDetail:nth-child(116) > dl:nth-child(1) > dd:nth-child(6)")
        print(pheno_id1.text)
        print(pheno_id2.text)
        print(pheno_id3.text) 
        print(pheno_id4.text)
        print(pheno_id5.text)
        print(pheno_id6.text)
        print(pheno_id7.text)
        print(pheno_id8.text)
        print(pheno_id9.text)
        print(pheno_id10.text)
        print(pheno_id11.text)
        print(pheno_id12.text)
        print(pheno_id13.text)
        print(pheno_id14.text)
        print(pheno_id15.text)
        print(pheno_id16.text)
        print(pheno_id17.text)
        print(pheno_id18.text)
        print(pheno_id19.text)
        print(pheno_id20.text)
        print(pheno_id21.text) 
        #asserts that the phenotype term IDs are correct and in the correct order
        self.assertIn(pheno_id1.text, "MGI:2176735 (key 9052)")  
        self.assertIn(pheno_id2.text, "MGI:3803606 (key 39416)")
        self.assertIn(pheno_id3.text, "MGI:5085301 (key 57010)")
        self.assertIn(pheno_id4.text, "MGI:3852467 (key 46893)")  
        self.assertIn(pheno_id5.text, "MGI:5702903 (key 75711)")
        self.assertIn(pheno_id6.text, "MGI:4839957 (key 53677)")
        self.assertIn(pheno_id7.text, "MGI:3531461 (key 20218)")  
        self.assertIn(pheno_id8.text, "MGI:3807487 (key 40126)")
        self.assertIn(pheno_id9.text, "MGI:5563244 (key 69739)") 
        self.assertIn(pheno_id10.text, "MGI:5563247 (key 69742)")         
        self.assertIn(pheno_id11.text, "MGI:3836424 (key 43990)")
        self.assertIn(pheno_id12.text, "MGI:3767613 (key 35569)")
        self.assertIn(pheno_id13.text, "MGI:3767612 (key 35568)")  
        self.assertIn(pheno_id14.text, "MGI:4940095 (key 54878)")
        self.assertIn(pheno_id15.text, "MGI:3716982 (key 32733)")
        self.assertIn(pheno_id16.text, "MGI:5563246 (key 69741)")  
        self.assertIn(pheno_id17.text, "MGI:5447168 (key 63214)")
        self.assertIn(pheno_id18.text, "MGI:5447167 (key 63213)")
        self.assertIn(pheno_id19.text, "MGI:5304570 (key 59128)")  
        self.assertIn(pheno_id20.text, "MGI:5285375 (key 57539)")
        self.assertIn(pheno_id21.text, "MGI:5308956 (key 59703)")
        
        
    def tearDown(self):
        self.driver.close()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPwiAlleleDetail))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))    
        