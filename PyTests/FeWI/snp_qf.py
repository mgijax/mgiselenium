"""
Created on Sep 7, 2018
This set of tests verifies the SNP query form
@author: jeffc
Verify that you can search for snps using a single reference strain
Verify that you can search for snps using a single reference strain and the option Different from the reference strain
Verify that you can search for snps using a single reference strain and the Allele Agreement filter All reference strains
    agree and all comparison strains agree with reference
Verify that you can search for snps using multiple reference strains and selective comparison strains
    this example is actually biologically significant.  All of the Reference strains in this example show what is
    called the AH+ phenotype (for Ahr), while all of the comparison strains show the AH- phenotype (for Ahr).
    The SNPs returned are all candidates for the genetic variation that defines the AH+ vs. AH- phenotype.
Verify search for snps using a region search of Chromosome and genome coordinates.
Verify search for snps using a region search by Marker Range.
Verify search for snps using a region search with results that take some time to display the heatmap.
Verify search for snps using a region search by Marker Range and then filter by Function Class.
Verify search for snps using a region search of Chromosome and genome coordinates and compare to a reference strain,
    Uses the Select DO/CC Founders option.
Verify search for snps using a region search of Chromosome and genome coordinates
    and compare to a reference strain, Uses the Select DO/CC Founders option and selects the Allele Agreement
    All reference strains agree and all comparison strains differ from reference
Verify search for snps using a region search of Chromosome and genome coordinates
    and compare to a reference strain, Uses the Select DO/CC Founders option and selects the Allele Agreement
    All reference strains agree and all comparison strains agree with reference
Verify
"""

import os.path
import sys
import time
import tracemalloc
import unittest
import config

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from util import iterate
from util.table import Table

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../..', )
)

# Test
tracemalloc.start()


class TestSnpQF(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        # self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/snp")
        self.driver.implicitly_wait(10)

    def test_search_1_ref_strain_nocompare(self):
        """
        @status: Tests that you can search for snps using a single reference strain
        @note: snp-qf-gene-3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        genesearchbox = driver.find_element(By.ID, 'nomen')
        # Enter your Gene symbol
        genesearchbox.send_keys("shh")
        time.sleep(2)
        # find the Yes button for comparing to one or more Reference strains and click it
        self.driver.find_element(By.XPATH, ".//input[@name='referenceMode' and @value='yes']").click()
        # find the Reference box for strain A/J and click it
        elem = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/J']"))
        driver.execute_script("arguments[0].click();", elem)
        # find the search button and click it
        driver.find_element(By.ID, 'geneSearch').click()
        # locates the SNP summary table and verify the rs IDs returned are correct
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        # cells = snp_table.get_column_cells("SNP ID\n(GRCm38)")
        cells = snp_table.get_column_cells("SNP ID\n(GRCm39)")
        print(iterate.getTextAsList(cells))
        rsreturned = iterate.getTextAsList(cells)
        # asserts that the following rs IDs are returned
        self.assertEqual(['SNP ID\n(GRCm39)', 'rs242800284\nMGI SNP Detail', 'rs578523809\nMGI SNP Detail', 'rs582188582\nMGI SNP Detail', 'rs212457488\nMGI SNP Detail', 'rs226445658\nMGI SNP Detail', 'rs33674412\nMGI SNP Detail', 'rs585655143\nMGI SNP Detail', 'rs108198781\nMGI SNP Detail', 'rs108778547\nMGI SNP Detail', 'rs261004727\nMGI SNP Detail', 'rs218362427\nMGI SNP Detail', 'rs47111361\nMGI SNP Detail', 'rs249730915\nMGI SNP Detail', 'rs46947101\nMGI SNP Detail', 'rs239706155\nMGI SNP Detail', 'rs261929355\nMGI SNP Detail', 'rs224835265\nMGI SNP Detail', 'rs247694355\nMGI SNP Detail', 'rs51773329\nMGI SNP Detail', 'rs45811526\nMGI SNP Detail', 'rs236309150\nMGI SNP Detail', 'rs253623880\nMGI SNP Detail', 'rs226413509\nMGI SNP Detail', 'rs579981447\nMGI SNP Detail', 'rs51494338\nMGI SNP Detail', 'SNP ID\n(GRCm39)', 'rs217616493\nMGI SNP Detail', 'rs231885837\nMGI SNP Detail', 'rs260499155\nMGI SNP Detail', 'rs218267274\nMGI SNP Detail', 'rs29729942\nMGI SNP Detail', 'rs33485416\nMGI SNP Detail', 'rs214491230\nMGI SNP Detail', 'rs231875716\nMGI SNP Detail', 'rs257041982\nMGI SNP Detail', 'rs225232488\nMGI SNP Detail', 'rs245058791\nMGI SNP Detail', 'rs264149809\nMGI SNP Detail', 'rs221790820\nMGI SNP Detail', 'rs236474324\nMGI SNP Detail', 'rs253582848\nMGI SNP Detail', 'rs33068028\nMGI SNP Detail', 'rs245621764\nMGI SNP Detail', 'rs263816277\nMGI SNP Detail', 'rs232641833\nMGI SNP Detail', 'rs254923948\nMGI SNP Detail', 'rs260861789\nMGI SNP Detail', 'rs29682823\nMGI SNP Detail', 'rs243668594\nMGI SNP Detail', 'rs214599967\nMGI SNP Detail', 'rs231824630\nMGI SNP Detail', 'SNP ID\n(GRCm39)', 'rs258411027\nMGI SNP Detail', 'rs583636057\nMGI SNP Detail', 'rs586160681\nMGI SNP Detail', 'rs216598691\nMGI SNP Detail', 'rs239951257\nMGI SNP Detail', 'rs260764549\nMGI SNP Detail', 'rs221886881\nMGI SNP Detail', 'rs230621041\nMGI SNP Detail', 'rs247947812\nMGI SNP Detail', 'rs219903994\nMGI SNP Detail', 'rs242744376\nMGI SNP Detail', 'rs33133952\nMGI SNP Detail', 'rs580354696\nMGI SNP Detail', 'rs224523062\nMGI SNP Detail', 'rs251897484\nMGI SNP Detail', 'rs260958293\nMGI SNP Detail', 'rs225222961\nMGI SNP Detail', 'rs33181672\nMGI SNP Detail', 'rs258504798\nMGI SNP Detail', 'rs230433332\nMGI SNP Detail', 'rs253202906\nMGI SNP Detail', 'rs216278752\nMGI SNP Detail', 'rs237823120\nMGI SNP Detail', 'rs247388744\nMGI SNP Detail', 'rs216681365\nMGI SNP Detail', 'SNP ID\n(GRCm39)', 'rs230589357\nMGI SNP Detail', 'rs248104048\nMGI SNP Detail', 'rs219829424\nMGI SNP Detail', 'rs237785982\nMGI SNP Detail', 'rs259064435\nMGI SNP Detail', 'rs223739221\nMGI SNP Detail', 'rs248077077\nMGI SNP Detail', 'rs254813293\nMGI SNP Detail', 'rs219238652\nMGI SNP Detail', 'rs237467004\nMGI SNP Detail', 'rs258608523\nMGI SNP Detail', 'rs230149305\nMGI SNP Detail', 'rs249385308\nMGI SNP Detail', 'rs263280273\nMGI SNP Detail', 'rs235042173\nMGI SNP Detail', 'rs246801108\nMGI SNP Detail', 'rs216646629\nMGI SNP Detail', 'rs242156134\nMGI SNP Detail', 'rs215008935\nMGI SNP Detail', 'rs48089243\nMGI SNP Detail', 'rs263212619\nMGI SNP Detail', 'rs215460178\nMGI SNP Detail', 'rs236061108\nMGI SNP Detail', 'rs254046834\nMGI SNP Detail', 'rs219163717\nMGI SNP Detail'],
                         rsreturned)  # this is all the data returned from the SNP ID column

    """def test_search_1_ref_strain_different(self):
        
        @status: Tests that you can search for snps using a single reference strain and the option Different from the reference strain
        @note: snp-qf-gene-3 I believe this test is no longer valid
        
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        genesearchbox = driver.find_element(By.ID, 'nomen')
        # Enter your Gene symbol
        genesearchbox.send_keys("shh")
        time.sleep(4)
        # find the Yes button for comparing to one or more Reference strains and click it
        self.driver.find_element(By.XPATH, ".//input[@name='referenceMode' and @value='yes']").click()
        # declares the entire tab as an entire form
        form2 = driver.find_element(By.ID, 'form2')
        # find the Reference box for strain A/J and click it
        form2.find_element(By.XPATH, '//*[@id="form2"]/table/tbody/tr[2]/td[2]/div/div[2]/div[1]/div[11]').click()
        #elem = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/J']"))
        #driver.execute_script("arguments[0].click();", elem)
        # find the search button and click it
        driver.find_element(By.ID, 'geneSearch').click()
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'alleleAgreementFilter'))):
            print('Allele Agreement loaded')
        aa = driver.find_element(By.ID, 'alleleAgreementFilter')
        driver.execute_script("arguments[0].click();", aa)
        # find the allele agreement filter for "All reference strains agree and all comparison strains differ with reference" and select it
        allelefil = self.driver.find_element(By.XPATH, (
            ".//input[@name='alleleAgreementFilter' and @value='All reference strains agree and all comparison strains differ from reference']"))
        driver.execute_script("arguments[0].click();", allelefil)
        # find and click the Filter button
        fltr = driver.find_element(By.ID, 'yui-gen0-button')
        driver.execute_script("arguments[0].click();", fltr)
        # locates the SNP summary table and verify the rs IDs returned are correct
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        cells = snp_table.get_column_cells("SNP ID\n(GRCm39)")
        print(iterate.getTextAsList(cells))
        rsreturned = iterate.getTextAsList(cells)
        # asserts that the following rs IDs are returned
        self.assertEqual(['SNP ID\n(GRCm39)', 'rs108198781\nMGI SNP Detail'],
                         rsreturned)  # this is all the data returned from the SNP ID column
     """

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
        time.sleep(4)
        # find the Yes button for comparing to one or more Reference strains and click it
        self.driver.find_element(By.XPATH, ".//input[@name='referenceMode' and @value='yes']").click()
        # find the Reference box for strain A/J and click it
        elem = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/J']"))
        driver.execute_script("arguments[0].click();", elem)
        # find the search button and click it
        driver.find_element(By.ID, 'geneSearch').click()
        if WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.ID, 'alleleAgreementFilter'))):
            print('Allele Agreement loaded')
        time.sleep(4)
        # find the allele agreement filter for "All reference strains agree and all comparison strains agree with reference" and select it
        driver.find_element(By.ID, 'alleleAgreementFilter').click()
        allelefil = driver.find_element(By.XPATH, (
            ".//input[@name='alleleAgreementFilter' and @value='All reference strains agree and all comparison strains agree with reference']"))
        driver.execute_script("arguments[0].click();", allelefil)
        # find and click the Filter button
        driver.find_element(By.ID, 'yui-gen0-button').click()
        # locates the SNP summary table and verify the rs IDs returned are correct
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        cells = snp_table.get_column_cells("SNP ID\n(GRCm39)")
        print(iterate.getTextAsList(cells))
        rsreturned = iterate.getTextAsList(cells)
        # asserts that the following rs IDs are returned

        self.assertEqual(['SNP ID\n(GRCm39)', 'rs583636057\nMGI SNP Detail', 'rs586160681\nMGI SNP Detail', 'rs579070145\nMGI SNP Detail', 'rs581574102\nMGI SNP Detail', 'rs581890197\nMGI SNP Detail', 'rs51528487\nMGI SNP Detail'],
                         rsreturned)  # this is all the data returned from the SNP ID column

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
        # find the Yes button for comparing to one or more Reference strains and click it
        self.driver.find_element(By.XPATH, ".//input[@name='referenceMode' and @value='yes']").click()
        # find the comparison strains button for "Clear All" and click it
        driver.find_element(By.ID, 'deselectButton').click()
        # find the Comparison box for strain 129S1/SvImJ and click it
        comelem = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='129S1/SvImJ']"))
        driver.execute_script("arguments[0].click();", comelem)
        # find the Comparison box for strain AKR/J and click it
        comelem1 = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='AKR/J']"))
        driver.execute_script("arguments[0].click();", comelem1)
        # find the Comparison box for strain DBA/2J and click it
        comelem2 = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='DBA/2J']"))
        driver.execute_script("arguments[0].click();", comelem2)
        # find the Comparison box for strain NZB/B1NJ and click it
        comelem3 = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='NZB/BlNJ']"))
        driver.execute_script("arguments[0].click();", comelem3)
        # find the Comparison box for strain NZW/LacJ and click it
        comelem4 = driver.find_element(By.XPATH, (".//input[@name='selectedStrains' and @value='NZW/LacJ']"))
        driver.execute_script("arguments[0].click();", comelem4)

        # find the Reference box for strain A/Hej and click it
        refelem = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/HeJ']"))
        driver.execute_script("arguments[0].click();", refelem)
        # find the Reference box for strain A/J and click it
        refelem1 = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='A/J']"))
        driver.execute_script("arguments[0].click();", refelem1)
        # find the Reference box for strain B10.D2-Hc<0> H2<d> H2-T18<c>/oSnJ and click it
        refelem2 = driver.find_element(By.XPATH, (
            ".//input[@name='referenceStrains' and @value='B10.D2-Hc<0> H2<d> H2-T18<c>/oSnJ']"))
        driver.execute_script("arguments[0].click();", refelem2)
        # find the Reference box for strain BALB/cJ and click it
        refelem3 = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='BALB/cJ']"))
        driver.execute_script("arguments[0].click();", refelem3)
        # find the Reference box for strain C3H/HeJ and click it
        refelem4 = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='C3H/HeJ']"))
        driver.execute_script("arguments[0].click();", refelem4)
        # find the Reference box for strain C57BL/6J and click it
        refelem5 = driver.find_element(By.XPATH, (".//input[@name='referenceStrains' and @value='C57BL/6J']"))
        driver.execute_script("arguments[0].click();", refelem5)

        # find the search button and click it
        driver.find_element(By.ID, 'geneSearch').click()
        time.sleep(2)
        driver.find_element(By.ID, 'alleleAgreementFilter').click()
        # find the Allele Agreement filter, select it and choose the option "All reference strains agree and all comparison strains differ from reference".
        allelefil = driver.find_element(By.XPATH, (
            ".//input[@name='alleleAgreementFilter' and @value='All reference strains agree and all comparison strains differ from reference']"))
        driver.execute_script("arguments[0].click();", allelefil)
        driver.find_element(By.ID, 'yui-gen0-button').click()
        # locates the SNP summary table and verify the rs IDs returned are correct, strains returned are correct
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        cells = snp_table.get_column_cells("SNP ID\n(GRCm39)")
        # cells = snp_table.get_column_cells("SNP ID\n(GRCm38)")
        print(iterate.getTextAsList(cells))
        rsreturned = iterate.getTextAsList(cells)
        # asserts that the following rs IDs are returned
        self.assertEqual(
            ['SNP ID\n(GRCm39)', 'rs3021544\nMGI SNP Detail', 'rs3021927\nMGI SNP Detail', 'rs3021928\nMGI SNP Detail',
             'rs3021931\nMGI SNP Detail', 'rs3021868\nMGI SNP Detail'],
            rsreturned)  # this is all the data returned from the SNP ID column currently 5 IDs as of 9/1218
        # self.assertEqual(['SNP ID\n(GRCm38)', 'rs3021544\nMGI SNP Detail', 'rs3021927\nMGI SNP Detail', 'rs3021928\nMGI SNP Detail', 'rs3021931\nMGI SNP Detail', 'rs3021868\nMGI SNP Detail'], rsReturned) # this is all the data returned from the SNP ID column currently 5 IDs as of 9/1218

        cells1 = snp_table.get_header_cells()
        print(iterate.getTextAsList(cells1))
        # print cells1[14].text
        self.assertEqual(cells1[5].text, 'A/HeJ', 'The first ref strain is not A/HeJ')
        self.assertEqual(cells1[6].text, 'A/J', 'The second ref strain is not A/J')
        self.assertEqual(cells1[7].text, 'B10.D2-Hc<0> H2<d> H2-T18<c>/oSnJ',
                         'The third ref strain is not B10.D2-Hc<0> H2<d> H2-T18<c>/oSnJ')
        self.assertEqual(cells1[8].text, 'BALB/cJ', 'The fourth ref strain is not BALB/cJ')
        self.assertEqual(cells1[9].text, 'C3H/HeJ', 'The fifth ref strain is not C3H/HeJ')
        self.assertEqual(cells1[10].text, 'C57BL/6J', 'The sixth ref strain is not C57BL/6J')
        self.assertEqual(cells1[11].text, '129S1/SvImJ', 'The first comparison strain is not 129S1/SvImJ')
        self.assertEqual(cells1[12].text, 'AKR/J', 'The second comparison strain is not AKR/J')
        self.assertEqual(cells1[13].text, 'DBA/2J', 'The third comparison strain is not DBA/2J')
        self.assertEqual(cells1[14].text, 'NZB/BlNJ', 'The fourth comparison strain is not NZB/B1NJ')
        self.assertEqual(cells1[15].text, 'NZW/LacJ', 'The fifth comparison strain is not NZW/LacJ')

    def test_search_by_region_chr_coord(self):
        """
        @status: Tests that you can search for snps using a region search of Chromosome and genome coordinates.
        @note: snp-qf-gene-?
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        # find the Region tab and click it
        driver.find_element(By.ID, 'ui-id-2').click()
        # select the chromosome
        Select(driver.find_element(By.ID, 'chromosomeDropList')).select_by_value('10')
        # Enter your genome coordinates
        gc = driver.find_element(By.NAME, 'coordinate')
        gc.send_keys("125.618-125.622")
        gc.send_keys(Keys.RETURN)
        Select(driver.find_element(By.ID, 'coordinateUnitDropList')).select_by_value('Mbp')
        # declares the entire tab as an entire form
        form2 = driver.find_element(By.ID, 'form2')
        # find the comparison strains button for "Clear All" and click it
        form2.find_element(By.ID, 'deselectButton').click()
        # locate the cookies popup close button and click it
        driver.find_element(By.CSS_SELECTOR, 'a.ccb-button:nth-child(1)').click()
        # find the Comparison box for strain A/J and click it
        form2.find_element(By.XPATH, '//*[@id="form2"]/table/tbody/tr[2]/td[2]/div/div[2]/div[1]/div[13]').click()
        # locate the cookies popup close button and click it
        driver.find_element(By.CSS_SELECTOR, 'a.ccb-button:nth-child(1)').click()
        # find the Comparison box for strain AKR/J and click it
        form2.find_element(By.XPATH, '//*[@id="form2"]/table/tbody/tr[2]/td[2]/div/div[2]/div[1]/div[15]').click()
        # find the search button and click it
        form2.find_element(By.XPATH, '//*[@id="locationSearch"]').click()
        # Locate the heat map info line and verify the text
        hminfo = driver.find_element(By.XPATH, '//*[@id="heatmapInfoRow"]/td/div/div[1]')
        print(hminfo.text)
        self.assertEqual(hminfo.text, 'Chr10 from 125,618,000 bp to 125,622,000 bp', 'The heatmap text is not correct')
        # locates the SNP summary table
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        # Locate the table header cells and verify the strains are correct
        time.sleep(5)
        cells1 = snp_table.get_header_cells()
        print(iterate.getTextAsList(cells1))
        print(cells1[5].text)
        print(cells1[6].text)
        self.assertEqual(cells1[5].text, 'A/J', 'The first strain is not correct')
        self.assertEqual(cells1[6].text, 'AKR/J', 'The second strain is not correct')

    def test_search_by_region_mrk_range(self):
        """
        @status: Tests that you can search for snps using a region search by Marker Range.
        @note: snp-qf-gene-? !!broken currently not returning the second strain data!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        # find the Region tab and click it
        driver.find_element(By.CSS_SELECTOR, '#ui-id-2').click()
        # enter the start marker
        strtmrkrange = driver.find_element(By.NAME, 'startMarker')
        strtmrkrange.send_keys('D19Mit32')
        # Enter the stop marker
        stopmrkrange = driver.find_element(By.NAME, 'endMarker')
        stopmrkrange.send_keys("Tbx10")
        stopmrkrange.send_keys(Keys.TAB)
        # declares the entire tab as an entire form
        form2 = driver.find_element(By.ID, 'form2')
        # find the comparison strains button for "Clear All" and click it
        form2.find_element(By.ID, 'deselectButton').click()
        # locate the cookies popup close button and click it
        driver.find_element(By.CSS_SELECTOR, '.ccb-tag > svg:nth-child(2)').click()
        # find the Comparison box for strain A/J and click it
        form2.find_element(By.XPATH, '//*[@id="form2"]/table/tbody/tr[2]/td[2]/div/div[2]/div[1]/div[13]').click()
        # find the Comparison box for strain AKR/J and click it
        form2.find_element(By.XPATH, '//*[@id="form2"]/table/tbody/tr[2]/td[2]/div/div[2]/div[1]/div[15]').click()
        # find the search button and click it
        form2.find_element(By.ID, 'locationSearch').click()
        time.sleep(2)
        # Locate the heat map info line and verify the text
        hminfo = driver.find_element(By.XPATH, '//*[@id="heatmapInfoRow"]/td/div/div[1]')
        self.assertEqual(hminfo.text, 'Chr19 from 3,328,551 bp to 4,049,512 bp', 'The heatmap text is not correct')
        # locates the SNP summary table
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        # Locate the table header cells and verify the strains are correct
        cells1 = snp_table.get_header_cells()
        print(iterate.getTextAsList(cells1))
        print(cells1[5].text)
        print(cells1[6].text)
        self.assertEqual(cells1[5].text, 'A/J', 'The first strain is not correct')
        self.assertEqual(cells1[6].text, 'AKR/J', 'The second strain is not correct')

    def test_search_by_region_slow_heatmap(self):
        """
        @status: Tests that you can search for snps using a region search with results that take some
        time to display the heatmap.
        @note: snp-qf-gene-?
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        # find the Region tab and click it
        driver.find_element(By.CSS_SELECTOR, '#ui-id-2').click()
        # select the chromosome
        Select(driver.find_element(By.ID, 'chromosomeDropList')).select_by_value('5')
        # Enter your genome coordinates
        gc = driver.find_element(By.NAME, 'coordinate')
        gc.send_keys("1-125618205")
        gc.send_keys(Keys.RETURN)
        # declares the entire tab as an entire form
        form2 = driver.find_element(By.ID, 'form2')
        # find the search button and click it
        form2.find_element(By.ID, 'locationSearch').click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'heatmapColorRow')))
        # Locate the heat map info line and verify the text
        hminfo = driver.find_element(By.XPATH, '//*[@id="heatmapInfoRow"]/td/div/div[1]')
        self.assertEqual(hminfo.text, 'Chr5 from 1,000,000 bp to 125,618,205,000,000 bp',
                         'The heatmap text is not correct')
        # locates the SNP summary table
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        # Locate the table header cells and verify the strains are correct
        cells1 = snp_table.get_header_cells()
        print(iterate.getTextAsList(cells1))
        print(cells1[5].text)
        print(cells1[6].text)
        self.assertEqual(cells1[7].text, '129S5/SvEvBrd', 'The first strain is not correct')
        self.assertEqual(cells1[8].text, '129S6/SvEvTac', 'The second strain is not correct')

    def test_search_by_region_filter_by_function_class(self):
        """
        @status: Tests that you can search for snps using a region search by Marker Range and
        then filter  by function class.
        @note: snp-qf-gene-?
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        # find the Region tab and click it
        driver.find_element(By.CSS_SELECTOR, '#ui-id-2').click()
        # enter the start marker
        strtmrkrange = driver.find_element(By.NAME, 'startMarker')
        strtmrkrange.send_keys('D19Mit32')
        # Enter the stop marker
        stopmrkrange = driver.find_element(By.NAME, 'endMarker')
        stopmrkrange.send_keys("Tbx10")
        stopmrkrange.send_keys(Keys.TAB)
        # declares the entire tab as an entire form
        form2 = driver.find_element(By.ID, 'form2')
        # find the search button and click it
        form2.find_element(By.ID, 'locationSearch').click()
        time.sleep(2)
        # Locate the page info line and verify the text
        pginfo = driver.find_element(By.ID, 'yui-pg0-0-page-report')
        print(pginfo.text)
        self.assertEqual(pginfo.text, 'Showing SNP(s) 1 - 100 of 14640', 'The page info text is not correct')
        # locates the SNP summary table
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        # Locate the table header cells and verify the strains are correct
        cells1 = snp_table.get_header_cells()
        print(iterate.getTextAsList(cells1))
        print(cells1[5].text)
        print(cells1[6].text)
        self.assertEqual(cells1[5].text, '129P2/OlaHsd', 'The first strain is not correct')
        self.assertEqual(cells1[6].text, '129S1/SvImJ', 'The second strain is not correct')
        driver.find_element(By.ID, 'functionClassFilter').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#command > label:nth-child(1) > input:nth-child(1)').click()
        time.sleep(1)
        driver.find_element(By.ID, 'yui-gen0-button').click()
        time.sleep(1)
        # Locate the page info line and verify the text
        pginfo = driver.find_element(By.ID, 'yui-pg0-0-page-report')
        print(pginfo.text)
        self.assertEqual(pginfo.text, 'Showing SNP(s) 1 - 100 of 12241', 'The page info text is not correct')

    def test_search_by_region_compare(self):
        """
        @status: Tests that you can search for snps using a region search of Chromosome and genome coordinates
        and compare to a reference strain, Uses the Select DO/CC Founders option.
        @note: snp-qf-gene-?
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        # find the Region tab and click it
        driver.find_element(By.ID, 'ui-id-2').click()
        # select the chromosome
        Select(driver.find_element(By.ID, 'chromosomeDropList')).select_by_value('1')
        # Enter your genome coordinates
        gc = driver.find_element(By.NAME, 'coordinate')
        gc.send_keys("125.618-125.622")
        gc.send_keys(Keys.RETURN)
        Select(driver.find_element(By.ID, 'coordinateUnitDropList')).select_by_value('Mbp')
        # declares the entire tab as an entire form
        form2 = driver.find_element(By.ID, 'form2')
        # Find the Select DO/CC Founders button and click it
        form2.find_element(By.ID, 'doccSelectButton').click()
        # find the Compare to one or more Reference strains and click it(Yes)
        form2.find_element(By.XPATH, '//*[@id="form2"]/table/tbody/tr[2]/td[2]/div/div[1]/div/label[2]').click()
        # find the reference strain for A/J and click it
        aj = form2.find_element(By.CSS_SELECTOR, '#form2 > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(13) > label:nth-child(1) > span:nth-child(2)')
        driver.execute_script("arguments[0].click();", aj)
        # find the search button and click it
        form2.find_element(By.ID, 'locationSearch').click()
        time.sleep(2)
        # Locate the heat map info line and verify the text
        hminfo = driver.find_element(By.XPATH, '//*[@id="heatmapInfoRow"]/td/div/div[1]')
        self.assertEqual(hminfo.text, 'Chr1 from 125,618,000 bp to 125,622,000 bp', 'The heatmap text is not correct')
        print(hminfo.text)
        # locates the SNP summary table
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        # Locate the table header cells and verify the strains are correct
        cells1 = snp_table.get_header_cells()
        # print(iterate.getTextAsList(cells1))
        print(cells1[5].text)
        print(cells1[6].text)
        self.assertEqual(cells1[5].text, 'A/J', 'The first strain is not correct')
        self.assertEqual(cells1[6].text, '129S1/SvImJ', 'The second strain is not correct')
        self.assertEqual(cells1[7].text, 'C57BL/6J', 'The third strain is not correct')
        self.assertEqual(cells1[8].text, 'CAST/EiJ', 'The fourth strain is not correct')
        self.assertEqual(cells1[9].text, 'NOD/ShiLtJ', 'The fifth strain is not correct')
        self.assertEqual(cells1[10].text, 'NZO/HlLtJ', 'The sixth strain is not correct')
        self.assertEqual(cells1[11].text, 'PWK/PhJ', 'The seventh strain is not correct')
        self.assertEqual(cells1[12].text, 'WSB/EiJ', 'The eight strain is not correct')

    def test_search_by_region_alleleagree1(self):
        """
        @status: Tests that you can search for snps using a region search of Chromosome and genome coordinates
        and compare to a reference strain, Uses the Select DO/CC Founders option and selects the Allele Agreement
        All reference strains agree and all comparison strains differ from reference
        @note: snp-qf-gene-?
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        # find the Region tab and click it
        driver.find_element(By.ID, 'ui-id-2').click()
        # select the chromosome
        Select(driver.find_element(By.ID, 'chromosomeDropList')).select_by_value('1')
        # Enter your genome coordinates
        gc = driver.find_element(By.NAME, 'coordinate')
        gc.send_keys("125.618-125.622")
        gc.send_keys(Keys.RETURN)
        Select(driver.find_element(By.ID, 'coordinateUnitDropList')).select_by_value('Mbp')
        # declares the entire tab as an entire form
        form2 = driver.find_element(By.ID, 'form2')
        # Find the Select DO/CC Founders button and click it
        form2.find_element(By.ID, 'doccSelectButton').click()
        # find the Compare to one or more Reference strains and click it(Yes)
        form2.find_element(By.XPATH, '//*[@id="form2"]/table/tbody/tr[2]/td[2]/div/div[1]/div/label[2]').click()
        # find the reference strain for A/J and click it
        aj = form2.find_element(By.CSS_SELECTOR, '#form2 > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(13) > label:nth-child(1) > span:nth-child(2)')
        driver.execute_script("arguments[0].click();", aj)
        # find the search button and click it
        form2.find_element(By.ID, 'locationSearch').click()
        time.sleep(2)
        # Locate the heat map info line and verify the text
        hminfo = driver.find_element(By.XPATH, '//*[@id="heatmapInfoRow"]/td/div/div[1]')
        self.assertEqual(hminfo.text, 'Chr1 from 125,618,000 bp to 125,622,000 bp', 'The heatmap text is not correct')
        # locates the SNP summary table
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        # Locate the table header cells and verify the strains are correct
        cells1 = snp_table.get_header_cells()
        # print(iterate.getTextAsList(cells1))
        print(cells1[5].text)
        print(cells1[6].text)
        self.assertEqual(cells1[5].text, 'A/J', 'The first strain is not correct')
        self.assertEqual(cells1[6].text, '129S1/SvImJ', 'The second strain is not correct')
        self.assertEqual(cells1[7].text, 'C57BL/6J', 'The third strain is not correct')
        self.assertEqual(cells1[8].text, 'CAST/EiJ', 'The fourth strain is not correct')
        self.assertEqual(cells1[9].text, 'NOD/ShiLtJ', 'The fifth strain is not correct')
        self.assertEqual(cells1[10].text, 'NZO/HlLtJ', 'The sixth strain is not correct')
        self.assertEqual(cells1[11].text, 'PWK/PhJ', 'The seventh strain is not correct')
        self.assertEqual(cells1[12].text, 'WSB/EiJ', 'The eight strain is not correct')
        driver.find_element(By.ID, 'alleleAgreementFilter').click()
        driver.find_element(By.CSS_SELECTOR, '#command > label:nth-child(1) > input:nth-child(1)').click()
        driver.find_element(By.ID, 'yui-gen0-button').click()
        # locates the SNP summary table
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        # Locate the table header cells and verify the strains are correct
        cells1 = snp_table.get_header_cells()
        print(cells1[5].text)
        print(cells1[6].text)
        self.assertEqual(cells1[5].text, 'A/J', 'The first strain is not correct')
        self.assertEqual(cells1[6].text, 'C57BL/6J', 'The second strain is not correct')

    def test_search_by_region_alleleagree2(self):
        """
        @status: Tests that you can search for snps using a region search of Chromosome and genome coordinates
        and compare to a reference strain, Uses the Select DO/CC Founders option and selects the Allele Agreement
        All reference strains agree and all comparison strains agree with reference
        @note: snp-qf-gene-?
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/snp")
        # find the Region tab and click it
        driver.find_element(By.ID, 'ui-id-2').click()
        # select the chromosome
        Select(driver.find_element(By.ID, 'chromosomeDropList')).select_by_value('1')
        # Enter your genome coordinates
        gc = driver.find_element(By.NAME, 'coordinate')
        gc.send_keys("125.618-125.622")
        gc.send_keys(Keys.RETURN)
        Select(driver.find_element(By.ID, 'coordinateUnitDropList')).select_by_value('Mbp')
        # declares the entire tab as an entire form
        form2 = driver.find_element(By.ID, 'form2')
        # Find the Select DO/CC Founders button and click it
        form2.find_element(By.ID, 'doccSelectButton').click()
        # find the Compare to one or more Reference strains and click it(Yes)
        form2.find_element(By.XPATH, '//*[@id="form2"]/table/tbody/tr[2]/td[2]/div/div[1]/div/label[2]').click()
        # find the reference strain for A/J and click it
        aj = form2.find_element(By.CSS_SELECTOR, '#form2 > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(13) > label:nth-child(1) > span:nth-child(2)')
        driver.execute_script("arguments[0].click();", aj)
        time.sleep(2)
        # Locate the heat map info line and verify the text
        hminfo = driver.find_element(By.XPATH, '//*[@id="heatmapInfoRow"]/td/div/div[1]')
        self.assertEqual(hminfo.text, 'Chr1 from 125,618,000 bp to 125,622,000 bp', 'The heatmap text is not correct')
        # locates the SNP summary table
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        # Locate the table header cells and verify the strains are correct
        cells1 = snp_table.get_header_cells()
        print(iterate.getTextAsList(cells1))
        print(cells1[5].text)
        print(cells1[6].text)
        self.assertEqual(cells1[5].text, 'A/J', 'The first strain is not correct')
        self.assertEqual(cells1[6].text, '129S1/SvImJ', 'The second strain is not correct')
        self.assertEqual(cells1[7].text, 'C57BL/6J', 'The third strain is not correct')
        self.assertEqual(cells1[8].text, 'CAST/EiJ', 'The fourth strain is not correct')
        self.assertEqual(cells1[9].text, 'NOD/ShiLtJ', 'The fifth strain is not correct')
        self.assertEqual(cells1[10].text, 'NZO/HlLtJ', 'The sixth strain is not correct')
        self.assertEqual(cells1[11].text, 'PWK/PhJ', 'The seventh strain is not correct')
        self.assertEqual(cells1[12].text, 'WSB/EiJ', 'The eight strain is not correct')
        driver.find_element(By.ID, 'alleleAgreementFilter').click()
        driver.find_element(By.CSS_SELECTOR, '#command > label:nth-child(3) > input:nth-child(1)').click()
        driver.find_element(By.ID, 'yui-gen0-button').click()
        time.sleep(2)
        # locates the SNP summary table
        snp_table = Table(self.driver.find_element(By.ID, "snpSummaryTable"))
        # Locate the table header cells and verify the strains are correct
        cells1 = snp_table.get_header_cells()
        print(cells1[5].text)
        print(cells1[6].text)
        self.assertEqual(cells1[5].text, 'A/J', 'The first strain is not correct')
        self.assertEqual(cells1[6].text, '129S1/SvImJ', 'The second strain is not correct')
        self.assertEqual(cells1[7].text, 'C57BL/6J', 'The third strain is not correct')
        self.assertEqual(cells1[8].text, 'CAST/EiJ', 'The fourth strain is not correct')
        self.assertEqual(cells1[9].text, 'NOD/ShiLtJ', 'The fifth strain is not correct')
        self.assertEqual(cells1[10].text, 'NZO/HlLtJ', 'The sixth strain is not correct')
        self.assertEqual(cells1[11].text, 'PWK/PhJ', 'The seventh strain is not correct')
        self.assertEqual(cells1[12].text, 'WSB/EiJ', 'The eight strain is not correct')

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSnpQF))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
