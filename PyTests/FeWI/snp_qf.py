'''
Created on Sep 7, 2018
This set of tests verifies the SNP query form
@author: jeffc
'''

import unittest
import time
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from util.table import Table
import sys,os.path
from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
import config
from config import TEST_URL

#Test
tracemalloc.start()
class TestSnpQF(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        #options = Options()
        #options.binary_location = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
        #self.driver = webdriver.Firefox(executable_path=r'C:\webdriver\bin\geckodriver.exe')

        #self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/snp")
        self.driver.implicitly_wait(10)

    def test_search_1_ref_strain_nocompare(self):
        """
        @status: Tests that you can search for snps using a single reference strain
        @note: snp-qf-gene-3
        Attention: this test will change once SNP's updated to 39 from 38!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        genesearchbox = driver.find_element(By.ID, 'nomen')
        # Enter your Gene symbol
        genesearchbox.send_keys("shh")
        time.sleep(2)
        #find the Yes button for comparing to one or more Reference strains and click it
        self.driver.find_element(By.XPATH, ".//input[@name='referenceMode' and @value='yes']").click()
        #find the Reference box for strain A/J and click it
        elem = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/J']"));
        driver.execute_script("arguments[0].click();", elem)
        #find the search button and click it
        driver.find_element(By.ID, 'geneSearch').click()
        #locates the SNP summary table and verify the rs IDs returned are correct
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        cells = snp_table.get_column_cells("SNP ID\n(GRCm38)")
        #cells = snp_table.get_column_cells("SNP ID\n(GRCm39)")
        print(iterate.getTextAsList(cells))     
        rsReturned = iterate.getTextAsList(cells)        
        #asserts that the following rs IDs are returned
        #self.assertEqual(['SNP ID\n(GRCm39)', 'rs36693755\nMGI SNP Detail', 'rs45992472\nMGI SNP Detail', 'rs47056606\nMGI SNP Detail', 'rs49586871\nMGI SNP Detail', 'rs108005419\nMGI SNP Detail', 'rs50091221\nMGI SNP Detail', 'rs47608361\nMGI SNP Detail', 'rs47802569\nMGI SNP Detail', 'rs38838986\nMGI SNP Detail', 'rs108810980\nMGI SNP Detail', 'rs36834363\nMGI SNP Detail', 'rs45730245\nMGI SNP Detail', 'rs49987272\nMGI SNP Detail', 'rs50481652\nMGI SNP Detail', 'rs36908712\nMGI SNP Detail', 'rs36250889\nMGI SNP Detail', 'rs107627921\nMGI SNP Detail', 'rs107868583\nMGI SNP Detail', 'rs37209710\nMGI SNP Detail', 'rs37559562\nMGI SNP Detail', 'rs39411786\nMGI SNP Detail', 'rs37808220\nMGI SNP Detail', 'rs45982583\nMGI SNP Detail', 'rs49721050\nMGI SNP Detail', 'rs45852704\nMGI SNP Detail', 'SNP ID\n(GRCm39)', 'rs46309889\nMGI SNP Detail', 'rs50848922\nMGI SNP Detail', 'rs36475093\nMGI SNP Detail', 'rs37617865\nMGI SNP Detail', 'rs37733367\nMGI SNP Detail', 'rs38671463\nMGI SNP Detail', 'rs38006235\nMGI SNP Detail', 'rs49277784\nMGI SNP Detail', 'rs50713983\nMGI SNP Detail', 'rs37770794\nMGI SNP Detail', 'rs36409597\nMGI SNP Detail', 'rs37594020\nMGI SNP Detail', 'rs48569389\nMGI SNP Detail', 'rs47471416\nMGI SNP Detail', 'rs50885594\nMGI SNP Detail', 'rs50068245\nMGI SNP Detail', 'rs50235477\nMGI SNP Detail', 'rs49604342\nMGI SNP Detail', 'rs50048728\nMGI SNP Detail', 'rs50725935\nMGI SNP Detail', 'rs37236717\nMGI SNP Detail', 'rs36256614\nMGI SNP Detail', 'rs50494556\nMGI SNP Detail', 'rs46110206\nMGI SNP Detail', 'rs37008263\nMGI SNP Detail', 'SNP ID\n(GRCm39)', 'rs38679453\nMGI SNP Detail', 'rs37621066\nMGI SNP Detail', 'rs51232661\nMGI SNP Detail', 'rs48161934\nMGI SNP Detail', 'rs107770016\nMGI SNP Detail', 'rs46957181\nMGI SNP Detail', 'rs107969822\nMGI SNP Detail', 'rs46851740\nMGI SNP Detail', 'rs46016689\nMGI SNP Detail', 'rs47024843\nMGI SNP Detail', 'rs48979048\nMGI SNP Detail', 'rs33094456\nMGI SNP Detail', 'rs33484219\nMGI SNP Detail', 'rs33681888\nMGI SNP Detail', 'rs29779268\nMGI SNP Detail', 'rs33264300\nMGI SNP Detail', 'rs50911636\nMGI SNP Detail', 'rs51872819\nMGI SNP Detail', 'rs45901879\nMGI SNP Detail', 'rs46857918\nMGI SNP Detail', 'rs50411707\nMGI SNP Detail', 'rs45865431\nMGI SNP Detail', 'rs33674412\nMGI SNP Detail', 'rs108198781\nMGI SNP Detail', 'rs108778547\nMGI SNP Detail', 'SNP ID\n(GRCm39)', 'rs29729942\nMGI SNP Detail', 'rs33485416\nMGI SNP Detail', 'rs33068028\nMGI SNP Detail', 'rs29682823\nMGI SNP Detail', 'rs33133952\nMGI SNP Detail', 'rs33181672\nMGI SNP Detail', 'rs48089243\nMGI SNP Detail', 'rs33541793\nMGI SNP Detail', 'rs33746193\nMGI SNP Detail', 'rs33214222\nMGI SNP Detail', 'rs33285952\nMGI SNP Detail', 'rs33560337\nMGI SNP Detail', 'rs33259009\nMGI SNP Detail', 'rs29727180\nMGI SNP Detail', 'rs33735948\nMGI SNP Detail', 'rs33682898\nMGI SNP Detail', 'rs51528487\nMGI SNP Detail', 'rs29676307\nMGI SNP Detail', 'rs33455132\nMGI SNP Detail', 'rs29562835\nMGI SNP Detail', 'rs33112153\nMGI SNP Detail', 'rs29530423\nMGI SNP Detail', 'rs29733217\nMGI SNP Detail', 'rs46215891\nMGI SNP Detail', 'rs33079729\nMGI SNP Detail'], rsReturned) # this is all the data returned from the SNP ID column

        self.assertEqual(['SNP ID\n(GRCm38)', 'rs33674412\nMGI SNP Detail', 'rs108198781\nMGI SNP Detail', 'rs108778547\nMGI SNP Detail', 'rs29729942\nMGI SNP Detail', 'rs33485416\nMGI SNP Detail', 'rs33068028\nMGI SNP Detail', 'rs29682823\nMGI SNP Detail', 'rs33133952\nMGI SNP Detail', 'rs33181672\nMGI SNP Detail', 'rs48089243\nMGI SNP Detail', 'rs33541793\nMGI SNP Detail', 'rs33746193\nMGI SNP Detail', 'rs33214222\nMGI SNP Detail', 'rs33285952\nMGI SNP Detail', 'rs33560337\nMGI SNP Detail', 'rs33259009\nMGI SNP Detail', 'rs29727180\nMGI SNP Detail', 'rs33735948\nMGI SNP Detail', 'rs33682898\nMGI SNP Detail', 'rs51528487\nMGI SNP Detail', 'rs29676307\nMGI SNP Detail', 'rs33455132\nMGI SNP Detail', 'rs29562835\nMGI SNP Detail', 'rs33112153\nMGI SNP Detail', 'rs29530423\nMGI SNP Detail', 'SNP ID\n(GRCm38)', 'rs29733217\nMGI SNP Detail'], rsReturned)  # this is all the data returned from the SNP ID column

    def test_search_1_ref_strain_different(self):
        """
        @status: Tests that you can search for snps using a single reference strain and the option Different from the reference strain
        @note: snp-qf-gene-3 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        genesearchbox = driver.find_element(By.ID, 'nomen')
        # Enter your Gene symbol
        genesearchbox.send_keys("shh")
        time.sleep(2)
        #find the Yes button for comparing to one or more Reference strains and click it
        self.driver.find_element(By.XPATH, ".//input[@name='referenceMode' and @value='yes']").click()
        #find the Reference box for strain A/J and click it
        elem = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/J']"))
        driver.execute_script("arguments[0].click();", elem)
        #find the search button and click it
        driver.find_element(By.ID, 'geneSearch').click()
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'alleleAgreementFilter'))):
            print('Allele Agreement loaded')
        driver.find_element(By.ID, 'alleleAgreementFilter').click()
        #find the allele agreement filter for "All reference strains agree and all comparison strains differ with reference" and select it
        alleleFil = self.driver.find_element(By.XPATH, (".//input[@name='alleleAgreementFilter' and @value='All reference strains agree and all comparison strains differ from reference']"));
        driver.execute_script("arguments[0].click();", alleleFil)
        #find and click the Filter button
        driver.find_element(By.ID, 'yui-gen0-button').click()
        #locates the SNP summary table and verify the rs IDs returned are correct
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        cells = snp_table.get_column_cells("SNP ID\n(GRCm38)")
        #cells = snp_table.get_column_cells("SNP ID\n(GRCm39)")
        print(iterate.getTextAsList(cells))     
        rsReturned = iterate.getTextAsList(cells)        
        #asserts that the following rs IDs are returned
        #self.assertEqual(['SNP ID\n(GRCm39)', 'rs108198781\nMGI SNP Detail'], rsReturned) # this is all the data returned from the SNP ID column
        self.assertEqual(['SNP ID\n(GRCm38)', 'rs108198781\nMGI SNP Detail'], rsReturned) # this is all the data returned from the SNP ID column

    def test_search_1_ref_strain_same(self):
        """
        @status: Tests that you can search for snps using a single reference strain and the Allele Agreement filter All reference strains agree and all comparison strains agree with reference 
        @note: snp-qf-gene-3 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        genesearchbox = driver.find_element(By.ID, 'nomen')
        # Enter your Gene symbol
        genesearchbox.send_keys("shh")
        time.sleep(2)
        #find the Yes button for comparing to one or more Reference strains and click it
        self.driver.find_element(By.XPATH, ".//input[@name='referenceMode' and @value='yes']").click()
        #find the Reference box for strain A/J and click it
        elem = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/J']"));
        driver.execute_script("arguments[0].click();", elem)
        #find the search button and click it
        driver.find_element(By.ID, 'geneSearch').click()
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'alleleAgreementFilter'))):
            print('Allele Agreement loaded')
        #find the allele agreement filter for "All reference strains agree and all comparison strains agree with reference" and select it
        driver.find_element(By.ID, 'alleleAgreementFilter').click()
        alleleFil = driver.find_element(By.XPATH, (".//input[@name='alleleAgreementFilter' and @value='All reference strains agree and all comparison strains agree with reference']"));
        driver.execute_script("arguments[0].click();", alleleFil)
        #find and click the Filter button
        driver.find_element(By.ID, 'yui-gen0-button').click()
        #locates the SNP summary table and verify the rs IDs returned are correct
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        #cells = snp_table.get_column_cells("SNP ID\n(GRCm39)")
        cells = snp_table.get_column_cells("SNP ID\n(GRCm38)")
        print(iterate.getTextAsList(cells))     
        rsReturned = iterate.getTextAsList(cells)        
        #asserts that the following rs IDs are returned
        
        #self.assertEqual(['SNP ID\n(GRCm39)', 'rs51528487\nMGI SNP Detail'], rsReturned) # this is all the data returned from the SNP ID column
        self.assertEqual(['SNP ID\n(GRCm38)', 'rs51528487\nMGI SNP Detail'], rsReturned) # this is all the data returned from the SNP ID column

    def test_search_multi_ref_strain(self):
        """
        @status: Tests that you can search for snps using multiple reference strains and selective comparison strains
        this example is actually biologically significant.  All of the Reference strains in this example show what is 
        called the AH+ phenotype (for Ahr), while all of the comparison strains show the AH- phenotype (for Ahr).
        The SNPs returned are all candidates for the genetic variation that defines the AH+ vs. AH- phenotype.
        @note: snp-qf-gene-4 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        genesearchbox = driver.find_element(By.ID, 'nomen')
        # Enter your Gene symbol
        genesearchbox.send_keys("Ahr")
        time.sleep(2)
        #find the Yes button for comparing to one or more Reference strains and click it
        self.driver.find_element(By.XPATH, ".//input[@name='referenceMode' and @value='yes']").click()        
        #find the comparison strains button for "Clear All" and click it
        driver.find_element(By.ID, 'deselectButton').click()
        #find the Comparison box for strain 129S1/SvImJ and click it
        comelem = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='129S1/SvImJ']"));
        driver.execute_script("arguments[0].click();", comelem)
        #find the Comparison box for strain AKR/J and click it
        comelem1 = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='AKR/J']"));
        driver.execute_script("arguments[0].click();", comelem1)
        #find the Comparison box for strain DBA/2J and click it
        comelem2 = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='DBA/2J']"));
        driver.execute_script("arguments[0].click();", comelem2)
        #find the Comparison box for strain NZB/B1NJ and click it
        comelem3 = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='NZB/BlNJ']"));
        driver.execute_script("arguments[0].click();", comelem3)
        #find the Comparison box for strain NZW/LacJ and click it
        comelem4 = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='NZW/LacJ']"));
        driver.execute_script("arguments[0].click();", comelem4)
              
        #find the Reference box for strain A/Hej and click it
        refelem = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/HeJ']"));
        driver.execute_script("arguments[0].click();", refelem)
        #find the Reference box for strain A/J and click it
        refelem1 = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/J']"));
        driver.execute_script("arguments[0].click();", refelem1)
        #find the Reference box for strain B10.D2-Hc<0> H2<d> H2-T18<c>/oSnJ and click it
        refelem2 = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='B10.D2-Hc<0> H2<d> H2-T18<c>/oSnJ']"));
        driver.execute_script("arguments[0].click();", refelem2)
        #find the Reference box for strain BALB/cJ and click it
        refelem3 = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='BALB/cJ']"));
        driver.execute_script("arguments[0].click();", refelem3)
        #find the Reference box for strain C3H/HeJ and click it
        refelem4 = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='C3H/HeJ']"));
        driver.execute_script("arguments[0].click();", refelem4)
        #find the Reference box for strain C57BL/6J and click it
        refelem5 = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='C57BL/6J']"));
        driver.execute_script("arguments[0].click();", refelem5)
        
        #find the search button and click it
        driver.find_element(By.ID, 'geneSearch').click()
        time.sleep(2)
        driver.find_element(By.ID, 'alleleAgreementFilter').click()
        #find the Allele Agreement filter, select it and choose the option "All reference strains agree and all comparison strains differ from reference".
        alleleFil = driver.find_element(By.XPATH, (".//input[@name='alleleAgreementFilter' and @value='All reference strains agree and all comparison strains differ from reference']"));
        driver.execute_script("arguments[0].click();", alleleFil)
        driver.find_element(By.ID, 'yui-gen0-button').click()
        #locates the SNP summary table and verify the rs IDs returned are correct, strains returned are correct
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        #cells = snp_table.get_column_cells("SNP ID\n(GRCm39)")
        cells = snp_table.get_column_cells("SNP ID\n(GRCm38)")
        print(iterate.getTextAsList(cells))     
        rsReturned = iterate.getTextAsList(cells)        
        #asserts that the following rs IDs are returned
        #self.assertEqual(['SNP ID\n(GRCm39)', 'rs3021544\nMGI SNP Detail', 'rs3021927\nMGI SNP Detail', 'rs3021928\nMGI SNP Detail', 'rs3021931\nMGI SNP Detail', 'rs3021868\nMGI SNP Detail'], rsReturned) # this is all the data returned from the SNP ID column currently 5 IDs as of 9/1218
        self.assertEqual(['SNP ID\n(GRCm38)', 'rs3021544\nMGI SNP Detail', 'rs3021927\nMGI SNP Detail', 'rs3021928\nMGI SNP Detail', 'rs3021931\nMGI SNP Detail', 'rs3021868\nMGI SNP Detail'], rsReturned) # this is all the data returned from the SNP ID column currently 5 IDs as of 9/1218

        cells1 = snp_table.get_header_cells()
        print(iterate.getTextAsList(cells1))  
        #print cells1[14].text   
        self.assertEqual(cells1[5].text, 'A/HeJ', 'The first ref strain is not A/HeJ')
        self.assertEqual(cells1[6].text, 'A/J', 'The second ref strain is not A/J')
        self.assertEqual(cells1[7].text, 'B10.D2-Hc<0> H2<d> H2-T18<c>/oSnJ', 'The third ref strain is not B10.D2-Hc<0> H2<d> H2-T18<c>/oSnJ')
        self.assertEqual(cells1[8].text, 'BALB/cJ', 'The fourth ref strain is not BALB/cJ')
        self.assertEqual(cells1[9].text, 'C3H/HeJ', 'The fifth ref strain is not C3H/HeJ')
        self.assertEqual(cells1[10].text, 'C57BL/6J', 'The sixth ref strain is not C57BL/6J')
        self.assertEqual(cells1[11].text, '129S1/SvImJ', 'The first comparison strain is not 129S1/SvImJ')
        self.assertEqual(cells1[12].text, 'AKR/J', 'The second comparison strain is not AKR/J')
        self.assertEqual(cells1[13].text, 'DBA/2J', 'The third comparison strain is not DBA/2J')
        self.assertEqual(cells1[14].text, 'NZB/BlNJ', 'The fourth comparison strain is not NZB/B1NJ')
        self.assertEqual(cells1[15].text, 'NZW/LacJ', 'The fifth comparison strain is not NZW/LacJ')
           
        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSnpQF))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))