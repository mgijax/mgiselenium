"""
Created on Apr 25, 2019
This set of tests is for searching of the RNA Seq and Microarray Experiments query form
@author: jeffc
Verify the searching by anatomical structure on the rna seq query form works
Verify the searching by theiler stage on the rna seq query form works
Verify the searching by age on the rna seq query form works
Verify the searching by mutant using a marker symbol on the rna seq query form works
Verify the searching by mutant using a marker synonym on the rna seq query form works
Verify the searching by mutant using an MGI marker ID on the rna seq query form works
Verify the searching by strain on the rna seq query form works
Verify the searching by strain using a wildcard on the rna seq query form works
Verify the searching by sex on the rna seq query form works
Verify the searching by method on the rna seq query form works
Verify the searching by text on the rna seq query form works
Verify the searching by text using a wildcard on the rna seq query form works
Verify the searching by arrayexpress ID on the rna seq query form works
Verify the searching by GEO ID on the rna seq query form works
"""
import os.path
import sys
import time
import tracemalloc
import unittest
import config
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
# from lib import *
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate
from util.table import Table

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)

# Tests
tracemalloc.start()


class TestGxdRnaSeqSearching(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/gxd/htexp_index")
        self.driver.implicitly_wait(10)

    def test_rnaseq_structure_search(self):
        """
        @status this test verifies the searching by anatomical structure on the rna seq query form works.
        @see GXD-RNASeq-search-1
        """
        print("BEGIN test_rnaseq_structure_search")
        self.driver.find_element(By.ID, 'structureAC').send_keys(
            'lung lobe')  # identifies the anatomical structure field and enters text
        # find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        # identify the titles of the results returned
        result_set = self.driver.find_element(By.ID, "injectedResults").find_elements(By.CLASS_NAME, 'title')
        print(result_set[0].text)
        self.assertEqual(result_set[0].text,
                         "Evolutionary dynamics of gene and isoform regulation in mammalian tissues")
        self.assertEqual(result_set[1].text, "Strand-specific RNA-seq of nine mouse tissues")

    def test_rnaseq_theiler_search(self):
        """
        @status this test verifies the searching by theiler stage on the rna seq query form works.
        @see GXD-RNASeq-search-2
        """
        print("BEGIN test_rnaseq_theiler_search")
        self.driver.find_element(By.ID, 'stagesTab').click()  # Clicks the "Use Thieler Stages" tab
        Select(self.driver.find_element(By.ID, 'theilerStage')).deselect_by_value('0')  # deselect the default option
        Select(self.driver.find_element(By.ID, 'theilerStage')).select_by_value(
            '5')  # finds the theiler stage list and select the TS 5 option
        # find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        # identify the titles of the results returned
        result_set = self.driver.find_element(By.ID, "injectedResults").find_elements(By.CLASS_NAME, 'title')
        print(result_set[0].text)
        self.assertEqual(result_set[0].text,
                         "Transcription profiling by high throughput sequencing of Oct4 null and wild type mouse embryos at three embryonic stages")
        self.assertEqual(result_set[1].text, "Transcriptome of mouse preimplantation development [Rlim KO]")

    def test_rnaseq_age_search(self):
        """
        @status this test verifies the searching by age on the rna seq query form works.
        @see GXD-RNASeq-search-3
        """
        print("BEGIN test_rnaseq_age_search")
        Select(self.driver.find_element(By.ID, 'age')).deselect_by_value('ANY')  # deselect the default option
        Select(self.driver.find_element(By.ID, 'age')).select_by_value(
            '1.5')  # finds the age list and select the E1.5 option
        # find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        # identify the titles of the results returned
        result_set = self.driver.find_element(By.ID, "injectedResults").find_elements(By.CLASS_NAME, 'title')
        print(result_set[0].text)
        self.assertEqual(result_set[0].text, "Transcription profiling of mouse preimplantation development")
        self.assertEqual(result_set[1].text, "Transcriptome of mouse preimplantation development [Xist KO]")

    def test_rnaseq_mutant_search(self):
        """
        @status this test verifies the searching by mutant using a marker symbol on the rna seq query form works.
        @see GXD-RNASeq-search-4
        """
        print("BEGIN test_rnaseq_mutant_search")
        self.driver.find_element(By.ID, 'mutatedIn').send_keys(
            'MF1')  # finds the mutant field and enters the gene symbol
        # find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        viewl = self.driver.find_elements(By.LINK_TEXT, 'View')[2]  # clicks the first View link of the third sample result
        self.driver.execute_script("arguments[0].click();", viewl)
        # switch focus to the new tab for Sample Experiments page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # find the sample table
        sample_table = self.driver.find_element(By.ID, "sampleTable")
        table = Table(sample_table)
        # Iterate and print the results for column Mutant Allele(s)
        strn = table.get_column_cells('Mutant Allele(s)')
        slist = iterate.getTextAsList(strn)
        print(slist)
        # verify the Mutant Allele(s) of each row
        self.assertEqual(slist[1], "Foxc1tm1Blh/Foxc1tm1Blh")
        self.assertEqual(slist[2], "Foxc1tm1Blh/Foxc1tm1Blh")
        self.assertEqual(slist[3], "Foxc1tm1Blh/Foxc1tm1Blh")
        self.assertEqual(slist[4], "Foxc1tm1Blh/Foxc1tm1Blh")
        self.assertEqual(slist[5], "Foxc1tm1Blh/Foxc1tm1Blh")
        self.assertEqual(slist[6], "Foxc1tm1Blh/Foxc1tm1Blh")
        self.assertEqual(slist[7], "")
        self.assertEqual(slist[8], "")
        self.assertEqual(slist[9], "")
        self.assertEqual(slist[10], "")
        self.assertEqual(slist[11], "")
        self.assertEqual(slist[12], "")

    def test_rnaseq_mutant_search1(self):
        """
        @status this test verifies the searching by mutant using a marker synonym on the rna seq query form works.
        @see GXD-RNASeq-search-4
        """
        print("BEGIN test_rnaseq_mutant_search1")
        self.driver.find_element(By.ID, 'mutatedIn').send_keys('Tcf1')  # finds the mutant field and enters the Synonym
        # find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        self.driver.find_elements(By.LINK_TEXT, 'View')[
            1].click()  # clicks the second View link of the first sample result
        # switch focus to the new tab for Sample Experiments page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # find the sample table
        sample_table = self.driver.find_element(By.ID, "sampleTable")
        table = Table(sample_table)
        # Iterate and print the results for column Mutant Allele(s)
        strn = table.get_column_cells('Mutant Allele(s)')
        slist = iterate.getTextAsList(strn)
        print(slist)
        # verify the genetic backgrounds of each row
        self.assertEqual(slist[1], "Hnf1atm1.1Ylee/Hnf1atm1.1Ylee")
        self.assertEqual(slist[2], "Hnf1atm1.1Ylee/Hnf1atm1.1Ylee")
        self.assertEqual(slist[3], "Hnf1atm1.1Ylee/Hnf1atm1.1Ylee")
        self.assertEqual(slist[4], "")
        self.assertEqual(slist[5], "")
        self.assertEqual(slist[6], "")

    def test_rnaseq_mutant_search2(self):
        """
        @status this test verifies the searching by mutant using an MGI marker ID on the rna seq query form works.
        @see GXD-RNASeq-search-4
        """
        print("BEGIN test_rnaseq_mutant_search2")
        self.driver.find_element(By.ID, 'mutatedIn').send_keys(
            'MGI:95661')  # finds the mutant field and enters the MGI ID
        # find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        self.driver.find_elements(By.LINK_TEXT, 'View')[
            0].click()  # clicks the first View link of the first sample result
        # switch focus to the new tab for Sample Experiments page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # find the sample table
        sample_table = self.driver.find_element(By.ID, "sampleTable")
        table = Table(sample_table)
        # Iterate and print the results for column Mutant Allele(s)
        strn = table.get_column_cells('Mutant Allele(s)')
        slist = iterate.getTextAsList(strn)
        print(slist)
        # verify the genetic backgrounds of each row
        self.assertEqual(slist[1], "Gata1tm7Sho/Gata1tm7Sho")
        self.assertEqual(slist[2], "Gata1tm7Sho/Y")
        self.assertEqual(slist[3], "Gata1tm7Sho/Gata1tm7Sho")
        self.assertEqual(slist[4], "Gata1tm7Sho/Y")
        self.assertEqual(slist[5], "")
        self.assertEqual(slist[6], "")
        self.assertEqual(slist[7], "")
        self.assertEqual(slist[8], "")

    def test_rnaseq_strain_search(self):
        """
        @status this test verifies the searching by strain on the rna seq query form works.
        @see GXD-RNASeq-search-5
        """
        print("BEGIN test_rnaseq_strain_search")
        self.driver.find_element(By.ID, 'strainNameAC').send_keys(
            'C57BL/6JRj')  # finds the strains field and enters the text
        # find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        self.driver.find_elements(By.LINK_TEXT, 'View')[
            0].click()  # clicks the first View link of the first sample result
        # switch focus to the new tab for Sample Experiments page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # find the sample table
        sample_table = self.driver.find_element(By.ID, "sampleTable")
        table = Table(sample_table)
        # Iterate and print the results for column Genetic Background
        strn = table.get_column_cells('Genetic Background')
        slist = iterate.getTextAsList(strn)
        print(slist)
        # verify the genetic backgrounds of each row(only checks the first 8 results)
        self.assertEqual(slist[1], "C57BL/6JRj")
        self.assertEqual(slist[2], "C57BL/6JRj")
        self.assertEqual(slist[3], "C57BL/6JRj")
        self.assertEqual(slist[4], "C57BL/6JRj")
        self.assertEqual(slist[5], "C57BL/6JRj")
        self.assertEqual(slist[6], "C57BL/6JRj")
        self.assertEqual(slist[7], "C57BL/6JRj")
        self.assertEqual(slist[8], "C57BL/6JRj")

    def test_rnaseq_strain_wild_search(self):
        """
        @status this test verifies the searching by strain using a wildcard on the rna seq query form works.
        @see GXD-RNASeq-search-6
        """
        print("BEGIN test_rnaseq_strain_wild_search")
        self.driver.find_element(By.ID, 'strainNameAC').send_keys(
            'C57BL/6JR*')  # finds the strains field and enters the text
        # find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        time.sleep(2)
        self.driver.find_elements(By.LINK_TEXT, 'View')[
            0].click()  # clicks the first View link of the first sample result
        # switch focus to the new tab for Sample Experiments page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # find the sample table
        sample_table = self.driver.find_element(By.ID, "sampleTable")
        table = Table(sample_table)
        # Iterate and print the results for column Genetic Background
        strn = table.get_column_cells('Genetic Background')
        slist = iterate.getTextAsList(strn)
        print(slist)
        # verify the genetic backgrounds of each row
        self.assertEqual(slist[1], "C57BL/6JRcc")
        self.assertEqual(slist[2], "C57BL/6JRcc")
        self.assertEqual(slist[3], "C57BL/6JRcc")
        self.assertEqual(slist[4], "C57BL/6JRcc")
        self.assertEqual(slist[5], "C57BL/6JRcc")
        self.assertEqual(slist[6], "C57BL/6JRcc")
        self.assertEqual(slist[7], "B6JRccHsd.Cg-Ppt1tm1Aj Cln5tm1Pltn")
        self.assertEqual(slist[8], "B6JRccHsd.Cg-Ppt1tm1Aj Cln5tm1Pltn")
        self.assertEqual(slist[9], "B6JRccHsd.Cg-Ppt1tm1Aj Cln5tm1Pltn")
        self.assertEqual(slist[10], "B6JRccHsd.Cg-Ppt1tm1Aj Cln5tm1Pltn")
        self.assertEqual(slist[11], "B6JRccHsd.Cg-Ppt1tm1Aj Cln5tm1Pltn")
        self.assertEqual(slist[12], "B6JRccHsd.Cg-Ppt1tm1Aj Cln5tm1Pltn")

    def test_rnaseq_sex_search(self):
        """
        @status this test verifies the searching by sex on the rna seq query form works.
        @see GXD-RNASeq-search-7
        """
        print("BEGIN test_rnaseq_sex_search")
        self.driver.find_element(By.ID, 'sex2').click()  # finds the sex radio button Pooled and clicks it
        # find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        # time.sleep(2)
        self.driver.find_elements(By.LINK_TEXT, 'View')[
            1].click()  # clicks the second View link of the first sample result
        # time.sleep(2)
        # switch focus to the new tab for Sample Experiments page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # find the sample table
        sample_table = self.driver.find_element(By.ID, "sampleTable")
        table = Table(sample_table)
        # Iterate and print the results for column Sex
        strn = table.get_column_cells('Sex')
        slist = iterate.getTextAsList(strn)
        print(slist)
        # verify the genetic backgrounds of each row
        self.assertEqual(slist[1], "Pooled")
        self.assertEqual(slist[2], "Pooled")
        self.assertEqual(slist[3], "Pooled")
        self.assertEqual(slist[4], "Pooled")
        self.assertEqual(slist[5], "Pooled")
        self.assertEqual(slist[6], "Pooled")

    def test_rnaseq_method_search(self):
        """
        @status this test verifies the searching by method on the rna seq query form works.
        @see GXD-RNASeq-search-8
        """
        print("BEGIN test_rnaseq_method_search")
        self.driver.find_element(By.ID, 'method1').click()  # finds the method RNA-Seq and clicks it
        # find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        # find all the Method data for the first 8 results
        meth0 = self.driver.find_element(By.ID, 'methodData0')
        meth1 = self.driver.find_element(By.ID, 'methodData1')
        meth2 = self.driver.find_element(By.ID, 'methodData2')
        meth3 = self.driver.find_element(By.ID, 'methodData3')
        meth4 = self.driver.find_element(By.ID, 'methodData4')
        meth5 = self.driver.find_element(By.ID, 'methodData5')
        meth6 = self.driver.find_element(By.ID, 'methodData6')
        meth7 = self.driver.find_element(By.ID, 'methodData7')
        print(meth0.text)
        # Assert the Method is RNA-Seq for the first 8 results, all results should be RNA-Seq but we only check the first 8
        self.assertEqual(meth0.text, "RNA-Seq")
        self.assertEqual(meth1.text, "RNA-Seq")
        self.assertEqual(meth2.text, "RNA-Seq")
        self.assertEqual(meth3.text, "RNA-Seq")
        self.assertEqual(meth4.text, "RNA-Seq")
        self.assertEqual(meth5.text, "RNA-Seq")
        self.assertEqual(meth6.text, "RNA-Seq")
        self.assertEqual(meth7.text, "RNA-Seq")  # there are another 600+ results and they should all be method RNA-Seq

    def test_rnaseq_text_search(self):
        """
        @status this test verifies the searching by text on the rna seq query form works.
        @see GXD-RNASeq-search-9
        """
        print("BEGIN test_rnaseq_text_search")
        self.driver.find_element(By.ID, 'text').send_keys('SCARKO')  # finds the Text field and enters the text
        # find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        # find the Description field
        desc1 = self.driver.find_element(By.ID, 'description0')
        desc2 = self.driver.find_element(By.ID, 'description1')
        desc3 = self.driver.find_element(By.ID, 'description2')
        print(desc1.text)
        # assert the word SCARKO can be found it the description section of results
        self.assertTrue("SCARKO" in desc1.text)
        self.assertTrue("SCARKO" in desc2.text)
        self.assertTrue("SCARKO" in desc3.text)

    def test_rnaseq_text_wild_search(self):
        """
        @status this test verifies the searching by text using a wildcard on the rna seq query form works.
        @see GXD-RNASeq-search-10
        """
        print("BEGIN test_rnaseq_text_wild_search")
        self.driver.find_element(By.ID, 'text').send_keys(
            'spectrophotometr*')  # finds the Text field and enters the text
        # find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        # identify the description sections of the results returned
        desc1 = self.driver.find_element(By.ID, 'description0')
        desc2 = self.driver.find_element(By.ID, 'description1')
        desc3 = self.driver.find_element(By.ID, 'description2')
        desc4 = self.driver.find_element(By.ID, 'description3')
        print(desc1.text)
        # assert the word spectrophotometry or Spectrophotometry can be found it the description section of results
        self.assertTrue("spectrophotometry" in desc1.text)
        self.assertTrue("Spectrophotometry" in desc2.text)
        self.assertTrue("spectrophotometry" in desc3.text)
        self.assertTrue("spectrophotometry" in desc4.text)

    def test_rnaseq_array_id_search(self):
        """
        @status this test verifies the searching by arrayexpress ID on the rna seq query form works.
        @see GXD-RNASeq-search-11
        """
        print("BEGIN test_rnaseq_array_id_search")
        self.driver.find_element(By.ID, 'arrayExpressID').send_keys(
            'E-GEOD-45719')  # finds the ArrayExprees or GEO ID field and enters an ID
        # find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        # identify the View experiment at field of the results returned
        arrayid = self.driver.find_element(By.ID, 'viewData0')
        print(arrayid.text)
        self.assertEqual(arrayid.text, "ArrayExpress: E-GEOD-45719\nGEO: GSE45719")

    def test_rnaseq_geo_id_search(self):
        """
        @status this test verifies the searching by GEO ID on the rna seq query form works.
        @see GXD-RNASeq-search-12
        """
        print("BEGIN test_rnaseq_geo_id_search")
        self.driver.find_element(By.ID, 'arrayExpressID').send_keys(
            'GSE41637')  # finds the ArrayExprees or GEO ID field and enters an ID
        # find the Search button and click it
        self.driver.find_element(By.ID, 'submit1').click()
        # identify the View experiment at field of the results returned
        geoid = self.driver.find_element(By.ID, 'viewData0')
        print(geoid.text)
        self.assertEqual(geoid.text, "ArrayExpress: E-GEOD-41637\nGEO: GSE41637")

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxdRnaSeqSearching))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
