'''
Created on Apr 24, 2018
This set of tests verifies the Strains query form does correct searching by Name, wildcard and ID
@author: jeffc
'''
import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from util.table import Table
import sys,os.path
from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
import config
#from config import TEST_URL

class TestStrainQF(unittest.TestCase):


    def setUp(self):
    
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/home/strain")
        self.driver.implicitly_wait(10)

    def test_search_strain_name(self):
        """
        @status: Tests that you can search for a strain by its name
        @note: Strain-qf-name-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/home/strain")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("CD")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        
        strainNamesReturned = iterate.getTextAsList(cells)
        
        #asserts that the following strains are returned
        self.assertIn('CD', strainNamesReturned) # Strain/Stock Name
  
    def test_search_strain_syn_name(self):
        """
        @status: Tests that you can search for a strain by its synonym name
        @note: Strain-qf-name-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("APPSWE")
        strainsearchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('129S6.Cg-Tg(APPSWE)2576Kha/Tac', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("Synonyms")
        print(iterate.getTextAsList(cells1))
        strainSynReturned = iterate.getTextAsList(cells1)
        #asserts that the synonym strains are returned
        self.assertIn('129S6.Cg-Tg(APPSWE)2576Kha N20+?\nAPPSWE', strainSynReturned) # synonym strain name
       
    def test_search_strain_wild_front(self):
        """
        @status: Tests that you can search for a strain by using a wildcard in front of text
        @note: Strain-qf-name-3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("*129")
        strainsearchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('129S6(B6)-Pgk2tm1Dao/Mmnc', strainNamesReturned) # Strain/Stock Name
        self.assertIn('C57BL/6J x 129', strainNamesReturned) # Strain/Stock Name
        self.assertIn('B6;129S5-Elovl6Gt(OST222498)Lex/Orl', strainNamesReturned) # Strain/Stock Name
        self.assertIn('C.129', strainNamesReturned) # Strain/Stock Name
       
    def test_search_strain_wild_front_back(self):
        """
        @status: Tests that you can search for a strain by using a wildcard at the front and end of text
        @note: Strain-qf-name-5
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("*Crygs*")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('B6.129-Crygstm1Gwis', strainNamesReturned) # Strain/Stock Name
        self.assertIn('B6N(Cg)-Crygstm1b(KOMP)Wtsi/2J', strainNamesReturned) # Strain/Stock Name
        self.assertIn('C3H.Cg-CrygsOpj/H', strainNamesReturned) # Strain/Stock Name
        self.assertIn('C57BL/6N-Crygstm1a(KOMP)Wtsi/2J', strainNamesReturned) # Strain/Stock Name
        
    def test_search_strain_mgi_id(self):
        """
        @status: Tests that you can search for a strain by using an MGI ID
        @note: Strain-qf-id-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:2159854")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('101/H', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:2159854', idReturned) # ID is correct                    
        
    def test_search_strain_alt_mgi_id(self):
        """
        @status: Tests that you can search for a strain by using an alternate MGI ID
        @note: Strain-qf-id-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:2164529")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('SJL/J', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:2159739\nJAX:000686\nMPD:17', idReturned) # ID is correct                    
                
    def test_search_strain_jax_id(self):
        """
        @status: Tests that you can search for a strain by using a JAX ID
        @note: Strain-qf-id-3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("000651")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('BALB/cJ', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:2159737\nJAX:000651\nMPD:5', idReturned) # ID is correct        

    def test_search_strain_MMRCC_id(self):
        """
        @status: Tests that you can search for a strain by using an MMRCC ID
        @note: Strain-qf-id-4
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("mmrrc:029868")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('129-Myh7tm1Unc/Mmnc', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:4452117\nMMRRC:029868', idReturned) # ID is correct        

    def test_search_strain_APB_id(self):
        """
        @status: Tests that you can search for a strain by using an APB ID
        @note: Strain-qf-id-5
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("APB:629")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('B6;129S4-Elf5tm1Mapr/Apb', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:6332119\nAPB:629', idReturned) # ID is correct   

    def test_search_strain_ARC_id(self):
        """
        @status: Tests that you can search for a strain by using an ARC ID
        @note: Strain-qf-id-6
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("ARC:B6")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('C57BL/6JArc', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:5425110\nARC:B6\nMPD:784', idReturned) # ID is correct   
    '''test_search_strain_BCBC_id not possible until data exists'''
        
    def test_search_strain_CARD_id(self):
        """
        @status: Tests that you can search for a strain by using an CARD ID
        @note: Strain-qf-id-8 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("242")
        strainsearchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('129-Atp6v0ctm1Hka', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:3054560\nCARD:242', idReturned) # ID is correct 
    '''test_search_strain_CHROMUS_id not possible until data exists'''        

    def test_search_strain_CMMR_id(self):
        """
        @status: Tests that you can search for a strain by using an CMMR ID
        @note: Strain-qf-id-10 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("0076")        
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('129-Alpltm1(cre)Nagy', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:4358196\nCMMR:0076', idReturned) # ID is correct 
    '''test_search_strain_CRL_id not possible until data exists'''                

    def test_search_strain_EMMA_id(self):
        """
        @status: Tests that you can search for a strain by using an EMMA ID
        @note: Strain-qf-id-12 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("EM:05001")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('129-Acaa1btm1Vnf/Orl', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:5490030\nEM:05001', idReturned) # ID is correct 

    def test_search_strain_EMS_id(self):
        """
        @status: Tests that you can search for a strain by using an EMS ID
        @note: Strain-qf-id-13 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("PacEMS1D")
        strainsearchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('B6.Cg-Tg(NR2E1)11Ems/Ems', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:3616881\npacEMS1D', idReturned) # ID is correct 
    '''test_search_strain_EUMMCR_id not possible until data exists'''        

    def test_search_strain_Harwell_id(self):
        """
        @status: Tests that you can search for a strain by using an Harwell ID
        @note: Strain-qf-id-15 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("FESA:03299")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('101/H-Tbob/H', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:4821385\nFESA:03299', idReturned) # ID is correct 

    def test_search_strain_JPGA_id(self):
        """
        @status: Tests that you can search for a strain by using an JPGA ID
        @note: Strain-qf-id-16 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("11473")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('C57BL/6J-GckHlb62/J', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:3621725\nJAX:004611\nJPGA:11473', idReturned) # ID is correct 
    '''test_search_strain_genOway_id not possible until data exists'''
    '''test_search_strain_KOMP_id not possible until data exists'''                

    def test_search_strain_NCIMR_id(self):
        """
        @status: Tests that you can search for a strain by using an NCIMR ID
        @note: Strain-qf-id-19 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("01XH9")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('129(Cg)-Mdm2tm1.2Mep', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:3618491\nNCIMR:01XH9', idReturned) # ID is correct 

    def test_search_strain_MPD_id(self):
        """
        @status: Tests that you can search for a strain by using an MPD ID
        @note: Strain-qf-id-20 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("53")
        strainsearchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('129S6/SvEvTac', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:3044417\nTAC:129sve\nMPD:53', idReturned) # ID is correct 
    '''test_search_strain_MTG_id not possible until data exists'''        

    def test_search_strain_MUGEN_id(self):
        """
        @status: Tests that you can search for a strain by using an CMMR ID
        @note: Strain-qf-id-22 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("M193046")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('B6;129-Adgre1tm1(cre)Kpf', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:4358385\nM193046', idReturned) # ID is correct 

    def test_search_strain_NIG_id(self):
        """
        @status: Tests that you can search for a strain by using an NIG ID
        @note: Strain-qf-id-23 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("NIG:229")
        strainsearchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('AVZ/Ms', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:3610724\nNIG:229', idReturned) # ID is correct 

    def test_search_strain_NMICE_id(self):
        """
        @status: Tests that you can search for a strain by using an NMICE ID
        @note: Strain-qf-id-24 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("MGI:1861634")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('C57BL/6J-Clockm1Jt/Nwu', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:3622461\nMGI:1861634', idReturned) # ID is correct 

    def test_search_strain_OBS_id(self):
        """
        @status: Tests that you can search for a strain by using an OBS ID
        @note: Strain-qf-id-25 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("OBS:27")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('B6.129P2-Hrh1tm1Wtn/Obs', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:5577152\nOBS:27', idReturned) # ID is correct 

    def test_search_strain_ORNL_id(self):
        """
        @status: Tests that you can search for a strain by using an ORNL ID
        @note: Strain-qf-id-26 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("47BS")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('47BS/Rl', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:5293354\nORNL:47BS', idReturned) # ID is correct 
        
    def test_search_strain_RIKEN_BRC_id(self):
        """
        @status: Tests that you can search for a strain by using an RIKEN BRC ID
        @note: Strain-qf-id-27 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("RBRC00222")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('SL/KhStmRbrc', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:2160561\nRBRC00222\nMPD:981', idReturned) # ID is correct 
    '''test_search_strain_SMOC_id not possible until data exists'''                 

    def test_search_strain_TAC_id(self):
        """
        @status: Tests that you can search for a strain by using an TAC ID
        @note: Strain-qf-id-29  NOTE: besides ID 1334 you can use ID TAC:rag2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("1334")
        strainsearchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('129S/SvEv-Rag2tm1Fwa/Tac', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:4838311\nTAC:1334\nTAC:rag2', idReturned) # ID is correct 
    '''test_search_strain_UNC_id not possible until data exists'''        
        
    def test_search_strain_RMRC_NLAC_id(self):
        """
        @status: Tests that you can search for a strain by using an RMRC-NLAC ID
        @note: Strain-qf-id-31 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        # Enter your strain name
        strainsearchbox.send_keys("RMRC11005")
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and verify the strain name is correct
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainNamesReturned = iterate.getTextAsList(cells)
        #asserts that the following strains are returned
        self.assertIn('C57BL/6JNarl', strainNamesReturned) # Strain/Stock Name
        cells1 = strain_table.get_column_cells("IDs")
        print(iterate.getTextAsList(cells1))
        idReturned = iterate.getTextAsList(cells1)
        #asserts that the correct ID is  returned
        self.assertIn('MGI:5699857\nRMRC11005', idReturned) # ID is correct 
    '''test_search_strain_WTSI_id not possible until data exists'''         

    def test_search_strain_attrib_coisogenic(self):
        '''
        @status: Tests that you can search for a strains using the strain attribute of conplastic
        @note: Strain-qf-attrib-1 
        '''
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        #find the conplastic option in the list and select it
        Select (driver.find_element(By.NAME, 'attributes')).select_by_visible_text('conplastic')
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and find the data in the Attributes column
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Attributes")
        print(iterate.getTextAsList(cells))
        attributesReturned = iterate.getTextAsList(cells)
        #asserts the following attributes are returned
        self.assertIn('conplastic', attributesReturned) # assert attribute is listed
        
    def test_search_strain_attrib_multi_default(self):
        '''
        @status: Tests that you can search for a strains using the strain attribute of conplastic and mutant strain with default of Any
        @note: Strain-qf-attrib-2 
        '''
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        #find the conplastic and inbred strain option in the list and select them
        select_box = Select (driver.find_element(By.NAME, 'attributes'))
        select_box.select_by_visible_text('conplastic')
        select_box.select_by_visible_text('inbred strain')
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and find the data in the Attributes column
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Attributes")
        print(iterate.getTextAsList(cells))
        attributesReturned = iterate.getTextAsList(cells)
        #asserts the following attributes are returned
        self.assertIn('conplastic', attributesReturned) # contains this attribute
        self.assertIn('inbred strain', attributesReturned) # contains this attribute

    def test_search_strain_and_attrib(self):
        '''
        @status: Tests that you can search for a strains and strain attributes
        @note: Strain-qf-attrib-3 
        '''
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        strainsearchbox = driver.find_element(By.ID, 'strainNameAC')
        #Enter your strain name
        strainsearchbox.send_keys("B6*")
        #find the conplastic and closed colony options in the list and select them
        select_box = Select (driver.find_element(By.NAME, 'attributes'))
        select_box.select_by_visible_text('conplastic')
        select_box.select_by_visible_text('closed colony')
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and find the data in the Attributes column
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Attributes")
        print(iterate.getTextAsList(cells))
        attributesReturned = iterate.getTextAsList(cells)
        time.sleep(2)
        #asserts the following attributes are returned
        self.assertIn('conplastic\ntargeted mutation', attributesReturned) # contains this attribute
        self.assertIn('closed colony\nmutant stock', attributesReturned) # contains this attribute
        #get data from the Strain/Stock Name column
        cells1 = strain_table.get_column_cells("Strain/Stock Name")
        print(iterate.getTextAsList(cells))
        strainsReturned = iterate.getTextAsList(cells1)
        time.sleep(2)
        #asserts the following strains are returned
        self.assertIn('B6.Cg-mt-Co1m1Jiha', strainsReturned) # contains this attribute
        self.assertIn('B6;129X1-Decr1tm1Jkh/Oulu[cc]', strainsReturned) # contains this attribute

    def test_search_two_attrib_all(self):
        '''
        @status: Tests that you can search for 2 strain attributes using all(AND) option
        @note: Strain-qf-attrib-4 
        '''
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        #find the 2 attribute options in the list and select them
        select_box = Select (driver.find_element(By.NAME, 'attributes'))
        select_box.select_by_visible_text('coisogenic')
        select_box.select_by_visible_text('revertant')
        #find the Match selected attributes list and select the "all" option
        #self.driver.find_element(By.NAME, 'seqPullDownForm')
        Select(driver.find_element(By.NAME, 'attributeOperator')).select_by_visible_text('all')
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and find the data in the Attributes column
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Attributes")
        print(iterate.getTextAsList(cells))
        attributesReturned = iterate.getTextAsList(cells)
        time.sleep(2)
        #asserts the following attributes are returned
        self.assertIn('coisogenic\nmutant strain\nrevertant\ntargeted mutation', attributesReturned) # contains this attribute
        self.assertIn('coisogenic\nmutant strain\nrevertant\ntargeted mutation', attributesReturned) # contains this attribute
        
    def test_search_two_attrib_any(self):
        '''
        @status: Tests that you can search for 2 strain attributes using any(OR) option
        @note: Strain-qf-attrib-5 
        '''
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        #find the 2 attribute options in the list and select them
        select_box = Select (driver.find_element(By.NAME, 'attributes'))
        select_box.select_by_visible_text('F3 hybrid')
        select_box.select_by_visible_text('revertant')
        #find the Match selected attributes list and select the "all" option
        #self.driver.find_element(By.NAME, 'seqPullDownForm')
        Select(driver.find_element(By.NAME, 'attributeOperator')).select_by_visible_text('any')
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and find the data in the Attributes column
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Attributes")
        print(iterate.getTextAsList(cells))
        attributesReturned = iterate.getTextAsList(cells)
        time.sleep(2)
        #asserts the following attributes are returned
        self.assertIn('F3 hybrid\nmutant stock', attributesReturned) # contains this attribute
        self.assertIn('F3 hybrid', attributesReturned) # contains this attribute
        self.assertIn('coisogenic\nmutant strain\nrevertant\ntargeted mutation', attributesReturned) # contains this attribute

    def test_search_multi_attrib_all(self):
        '''
        @status: Tests that you can search for multiple strain attributes using all(AND) option
        @note: Strain-qf-attrib-6 
        '''
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        #find the 3 attribute options in the list and select them
        select_box = Select (driver.find_element(By.NAME, 'attributes'))
        select_box.select_by_visible_text('coisogenic')
        select_box.select_by_visible_text('revertant')
        select_box.select_by_visible_text('targeted mutation')
        #find the Match selected attributes list and select the "all" option
        #self.driver.find_element(By.NAME, 'seqPullDownForm')
        Select(driver.find_element(By.NAME, 'attributeOperator')).select_by_visible_text('all')
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and find the data in the Attributes column
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Attributes")
        print(iterate.getTextAsList(cells))
        attributesReturned = iterate.getTextAsList(cells)
        time.sleep(2)
        #asserts the following attributes are returned
        self.assertIn('coisogenic\nmutant strain\nrevertant\ntargeted mutation', attributesReturned) # contains this attribute
        self.assertIn('coisogenic\nmutant strain\nrevertant\ntargeted mutation', attributesReturned) # contains this attribute

    def test_search_multi_attrib_any(self):
        '''
        @status: Tests that you can search for multiple strain attributes using any(OR) option
        @note: Strain-qf-attrib-7 
        '''
        driver = self.driver
        driver.get(config.TEST_URL + "/strains_SNPs.shtml")
        #find the 3 attribute options in the list and select them
        select_box = Select (driver.find_element(By.NAME, 'attributes'))
        select_box.select_by_visible_text('F3 hybrid')
        select_box.select_by_visible_text('revertant')
        select_box.select_by_visible_text('trisomy')
        #find the Match selected attributes list and select the "all" option
        #self.driver.find_element(By.NAME, 'seqPullDownForm')
        Select(driver.find_element(By.NAME, 'attributeOperator')).select_by_visible_text('any')
        time.sleep(2)
        #find the search button and click it
        driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        #locates the strain table and find the data in the Attributes column
        strain_table = Table(self.driver.find_element(By.ID, "strainSummaryTable"))
        cells = strain_table.get_column_cells("Attributes")
        print(iterate.getTextAsList(cells))
        attributesReturned = iterate.getTextAsList(cells)
        time.sleep(2)
        #asserts the following attributes are returned
        self.assertIn('F3 hybrid\nmutant stock', attributesReturned) # contains this attribute
        self.assertIn('F3 hybrid', attributesReturned) # contains this attribute
        self.assertIn('chromosome aberration\nmutant strain\ntrisomy', attributesReturned) # contains this attribute
        
    def tearDown(self):
        #self.driver.close()
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestStrainQF))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))