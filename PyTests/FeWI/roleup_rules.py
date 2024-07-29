"""
Created on Apr 15, 2024
This set of tests verifies to the best of the test's ability to verify rollup rules are working correctly
@author: jeffc
Rule 1 Verify that rollup rule 1 One Marker Genotype. Naturally simple genotypes are included in the roll-up, so we associate these genotypes with their corresponding markers
        Have only one marker
        Have no "inserted expressed sequence" attribute (CREAM)
        Have no "mutation involves" relationships (CREAM)
        Are not conditional genotypes
Rule 1.2 Verify that For the remaining conditional and complex genotypes perform the following steps to remove non-causative alleles before further roll-up is done. If at the end of these steps there are no remaining markers, that genotype is eliminated from the pre-computed set of annotations (Elim #1), otherwise continue on.
        If the genotype is conditional, then remove any recombinase alleles as long as they don't have any "inserted expressed sequence" attribute. (CREAM)
        remove reporter transgene alleles (when it is transgenic & only attribute = Reporter)
        remove wild-type alleles
        remove transgenic alleles that have an attribute of "Transactivator" and do NOT have the attribute "inserted expressed sequence". Other attributes may be present. (TR 11860; 5.22)

Rule 1.3 Verify Tests that Next, for the remaining genotypes we need to collect 3 sets of markers from the alleles that have not been removed
        (M) a set of markers related to the genotype's alleles via the traditional marker-allele path
        (EC) a set of markers with "expresses component" relationships with the genotype's alleles (either mouse or orthologous components)
        (I) a set of markers with "mutation involves" relationships with the genotype's alleles
Rule 2 Verify that Transgene expresses Abc & Abc is mutated.
        If the genotype still has 2 markers in (M) and the following is also true
            The genotype has no markers in (I), i.e. no mutation involves data
            The 2 markers in (M) are a Transgene marker and a non-Transgene marker
            There is exactly 1 marker in (EC), and it is the non-Transgene marker, and it is a mouse component
            The Transgene marker expresses that non-Transgene marker.
        Roll-up this genotype to both markers in (M) -- transgene and non-transgene markers.
Rule 3 Verify that Mutation Involves.
        If the genotype has exactly 1 marker in (M) and that marker is of feature type: heritable phenotypic marker, complex/cluster/region, or any descendent of cytogenetic marker and has at least one mutation involves relationship and does NOT have the attribute “inserted expressed sequence”, then roll-up this genotype to the marker in (M). (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Transgene and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the Transgene marker (M) and non-transgene marker (I) (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Docking Site, and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the mutation involves marker (I) and NOT to the Docking Site marker (CREAM)
Rule 4 Verify that Transgene.
        If the marker in (M) is a transgene; roll-up the genotype to that marker.
Rule 5 Verify that Transgene Expresses One Component.
        If the marker in (M) is a transgene AND there is exactly one marker for the genotype in (EC) and it is a
        mouse component, then also roll-up the genotype to the EC marker.
Rule 6 Verify that Docking site Expresses One Component
        If the marker in (M) is a docking site AND there is exactly one marker for the genotype in (EC) and it is a
        mouse component, then roll-up the genotype to the EC marker.
            Current docking sites are: Col1a1, Gt(ROSA)26Sor, Hprt
Rule 7 Verify that Single with no Expresses Component.
        If the marker in (M) is neither a transgene nor a docking site AND the alleles do NOT have any “inserted expressed
        sequence attribute”,, then roll-up the genotype to the marker in (M). (CREAM)
Rule 8 Verify that Self-expressing single
        If the marker in (M) is neither a transgene nor a docking site and there is exactly 1 marker in (EC) and it is a
        mouse component, AND it is the same marker in (M), then roll-up the genotype to the marker in (M).
Rule 9 Verify that Docking site Expresses No Components
        If the marker in (M) is a docking site other than Gt(ROSA)26Sor AND the alleles do NOT have any “inserted expressed
        sequence attribute”, then roll-up the genotype to the docking site marker. (CREAM)
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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate,wait
from util.table import Table

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../..', )
)

# Tests
tracemalloc.start()


class TestRollupRules(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        #self.driver.get(config.TEST_URL + "/marker.shtml")
        self.driver.implicitly_wait(10)

    def test_rollup_rule1_do(self):
        """
        @status: Tests rollup rule 1 One Marker Genotype. Naturally simple genotypes are included in the roll-up, so we associate these genotypes with their corresponding markers
        Have only one marker
        Have no "inserted expressed sequence" attribute (CREAM)
        Have no "mutation involves" relationships (CREAM)
        Are not conditional genotypes
        @note: rollup-rule-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("App")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'App').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseRibbon'))):
            print('Human Diseases ribbon is loaded')
        # find the Human Diseases 'More' toggle and click it
        self.driver.find_element(By.ID, 'hdToggle').click()
        time.sleep(2)
        # find the Human Disease table
        disease_table = self.driver.find_element(By.ID, "humanDiseaseTable")
        table = Table(disease_table)
        # Iterate and print the results for column Mutant Allele(s)
        strn = table.get_column_cells('Human Disease')
        dlist = iterate.getTextAsList(strn)
        print(dlist)
        # verify the Mutant Allele(s) of each row
        self.assertEqual(dlist[1], "Alzheimer's disease\nIDs")
        self.assertEqual(dlist[2], "Alzheimer's disease 1\nIDs")
        # find the View Models link and click it
        driver.find_element(By.ID, 'showDOID_10652').click()
        # find the popup Model table and click the first View link in the Phenotypes column
        self.driver.find_element(By.LINK_TEXT, "View").click()
        # switch focus to the new tab for strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'titleBarMainTitle'))):
            print('Page title is loaded')
        # verify the disease listed in the Mouse Models of Human Disease table is correct
        disease_table = Table(self.driver.find_element(By.CLASS_NAME, "results"))
        cell = disease_table.get_cell(1, 0)
        print(cell.text)
        # Asserts that the right Human disease is displayed
        self.assertEqual(cell.text, "Alzheimer's disease")

    def test_rollup_rule1_mp(self):
        """
        @status: Tests rollup rule 1 One Marker Genotype. Naturally simple genotypes are included in the roll-up, so we associate these genotypes with their corresponding markers
        Have only one marker
        Have no "inserted expressed sequence" attribute (CREAM)
        Have no "mutation involves" relationships (CREAM)
        Are not conditional genotypes
        @note: rollup-rule-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("App")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'App').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('The Summary Ribbon is displayed')
        # find the Phenotype slim grid and click the Cellular box
        mpsgrid = self.driver.find_element(By.ID, 'mpSlimgrid4Div')
        driver.execute_script("arguments[0].click();", mpsgrid)
        time.sleep(2)
        # switch focus to the new tab for Phenotype annotations related to cellular
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert all 7 results for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/div[2]/table[2]"))
        cell1 = mp_table.get_cell(2, 1)
        print(cell1.text)
        cell2 = mp_table.get_cell(3, 1)
        print(cell2.text)
        cell3 = mp_table.get_cell(4, 1)
        print(cell3.text)
        cell4 = mp_table.get_cell(5, 1)
        print(cell4.text)
        cell5 = mp_table.get_cell(6, 1)
        print(cell5.text)
        cell6 = mp_table.get_cell(7, 1)
        print(cell6.text)
        cell7 = mp_table.get_cell(8, 1)
        print(cell7.text)
        # verify the Mouse Phenotypes for each row
        self.assertEqual(cell1.text, "Apptm1.1Cep/Apptm1.1Cep")
        self.assertEqual(cell2.text, "Apptm1Cep/Apptm1Cep")
        self.assertEqual(cell3.text, "Apptm1.1Cep/App+")
        self.assertEqual(cell4.text, "Apptm1Cep/App+")
        self.assertEqual(cell5.text, "Tg(APP-App*R609D*K612E)7Vln/0")
        self.assertEqual(cell6.text, "Tg(Thy1-App*R609D*K612E)2Vln/0")
        self.assertEqual(cell7.text, "Tg(Thy1-App*R609D*K612E)4Vln/0")

    def test_rollup_rule1_hmdc(self):
        """
        @status: Tests rollup rule 1 One Marker Genotype. Naturally simple genotypes are included in the roll-up, so we associate these genotypes with their corresponding markers
        Have only one marker
        Have no "inserted expressed sequence" attribute (CREAM)
        Have no "mutation involves" relationships (CREAM)
        Are not conditional genotypes
        @note: rollup-rule-1
        """
        driver = self.driver
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "App")  # identifies the input field and a marker symbol
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        time.sleep(2)
        #click on the Cellular field for App
        self.driver.find_element(By.CSS_SELECTOR, "tr.ngc:nth-child(3) > td:nth-child(5) > div:nth-child(1) > div:nth-child(1)").click()
        # switch focus to the popup for Mouse cellular abnormalities for APP/App
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert row 4 results for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/p/table"))
        cell4 = mp_table.get_cell(5, 1)
        print(cell4.text)
        # verify the Mouse Phenotypes for row 4, then click it
        self.assertEqual(cell4.text, "Apptm1Cep/App+")
        cell4.click()
        # switch focus to the new tab for Phenotype associated with App<tm1Cep>/App<+>
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        geno = self.driver.find_element(By.CLASS_NAME, 'genoID')
        # assert the Genotype ID is correct
        self.assertEqual(geno.text, 'MGI:2652361')
        # locate the Mouse Models of Human Disease table
        mm_table = self.driver.find_element(By.CLASS_NAME, 'results')
        table = Table(mm_table)
        # Find the first table column for row 1
        mm1 = table.get_cell(1, 0)
        print(mm1.text)
        # Find the second table column for row 1
        doid1 = table.get_cell(1, 1)
        print(doid1.text)
        # Assert the Disease and DOID are correct
        self.assertEqual(mm1.text, "Alzheimer's disease")
        self.assertEqual(doid1.text, 'DOID:10652')


    def test_rollup_rule1_2_do(self):
        """
        @status: Tests that For the remaining conditional and complex genotypes perform the following steps to remove non-causative alleles before further roll-up is done. If at the end of these steps there are no remaining markers, that genotype is eliminated from the pre-computed set of annotations (Elim #1), otherwise continue on.
        If the genotype is conditional, then remove any recombinase alleles as long as they don't have any "inserted expressed sequence" attribute. (CREAM)
        remove reporter transgene alleles (when it is transgenic & only attribute = Reporter)
        remove wild-type alleles
        remove transgenic alleles that have an attribute of "Transactivator" and do NOT have the attribute "inserted expressed sequence". Other attributes may be present. (TR 11860; 5.22)
        @note: rollup-rule1.2
        """


    def test_rollup_rule1_3_do(self):
        """
        @status: Tests that Next, for the remaining genotypes we need to collect 3 sets of markers from the alleles that have not been removed
        (M) a set of markers related to the genotype's alleles via the traditional marker-allele path
        (EC) a set of markers with "expresses component" relationships with the genotype's alleles (either mouse or orthologous components)
        (I) a set of markers with "mutation involves" relationships with the genotype's alleles
        @note: rollup-rule1.3
        """


    def test_rollup_rule2_do(self):
        """
        @status: Tests that Transgene expresses Abc & Abc is mutated.
        If the genotype still has 2 markers in (M) and the following is also true
            The genotype has no markers in (I), i.e. no mutation involves data
            The 2 markers in (M) are a Transgene marker and a non-Transgene marker
            There is exactly 1 marker in (EC), and it is the non-Transgene marker, and it is a mouse component
            The Transgene marker expresses that non-Transgene marker.
        Roll-up this genotype to both markers in (M) -- transgene and non-transgene markers.
        @note: rollup-rule2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Jup")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Jup').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseRibbon'))):
            print('Human Diseases ribbon is loaded')
        # find the Human Diseases 'More' toggle and click it
        self.driver.find_element(By.ID, 'hdToggle').click()
        time.sleep(2)
        # find the Human Disease table
        disease_table = self.driver.find_element(By.ID, "humanDiseaseTable")
        table = Table(disease_table)
        # Iterate and print the results for column Human Disease
        strn = table.get_column_cells('Human Disease')
        dlist = iterate.getTextAsList(strn)
        print(dlist)
        # verify the Mutant Allele(s) of each row
        self.assertEqual(dlist[1], "arrhythmogenic right ventricular dysplasia 12\nIDs")
        self.assertEqual(dlist[2], "epidermolytic hyperkeratosis\nIDs")
        # find the View Models link and click it
        driver.find_element(By.ID, 'showDOID_0110083').click()
        # find the popup Model table and click the first View link in the Phenotypes column
        self.driver.find_element(By.LINK_TEXT, "View").click()
        # switch focus to the new tab for strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'titleBarMainTitle'))):
            print('Page title is loaded')
        # verify the disease listed in the Mouse Models of Human Disease table is correct
        disease_table = Table(self.driver.find_element(By.CLASS_NAME, "results"))
        cell = disease_table.get_cell(1, 0)
        print(cell.text)
        # Asserts that the right Human disease is displayed
        self.assertEqual(cell.text, 'arrhythmogenic right ventricular dysplasia 12')

    def test_rollup_rule2_mp(self):
        """
        !!!!!this test is not ready yet!!!!!
        @status: Tests that Transgene expresses Abc & Abc is mutated.
        If the genotype still has 2 markers in (M) and the following is also true
            The genotype has no markers in (I), i.e. no mutation involves data
            The 2 markers in (M) are a Transgene marker and a non-Transgene marker
            There is exactly 1 marker in (EC), and it is the non-Transgene marker, and it is a mouse component
            The Transgene marker expresses that non-Transgene marker.
        Roll-up this genotype to both markers in (M) -- transgene and non-transgene markers.
        @note: rollup-rule2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Jup")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Jup').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('The Summary Ribbon is displayed')
        # find the Phenotype slim grid and click the Cardiovascular system box
        mpsgrid = self.driver.find_element(By.ID, 'mpSlimgrid3Div')
        driver.execute_script("arguments[0].click();", mpsgrid)
        time.sleep(2)
        # switch focus to the new tab for Phenotype annotations related to cellular
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert row 4 results for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/div[2]/table[3]"))
        cell4 = mp_table.get_cell(5, 1)
        print(cell4.text)
        # verify the Mouse Phenotypes for row 4
        self.assertEqual(cell4.text, "Juptm1Ruiz/Jup+\nTg(Myh6-Jup*)1Ajm/0")

    def test_rollup_rule2_hmdc(self):
        """
        @status: Tests that Transgene expresses Abc & Abc is mutated.
        If the genotype still has 2 markers in (M) and the following is also true
            The genotype has no markers in (I), i.e. no mutation involves data
            The 2 markers in (M) are a Transgene marker and a non-Transgene marker
            There is exactly 1 marker in (EC), and it is the non-Transgene marker, and it is a mouse component
            The Transgene marker expresses that non-Transgene marker.
        Roll-up this genotype to both markers in (M) -- transgene and non-transgene markers.
        @note: rollup-rule2
        """
        driver = self.driver
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Jup")  # identifies the input field and a marker symbol
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        time.sleep(2)
        # Find the cardiovascular system box for Jup and click it.
        self.driver.find_element(By.CSS_SELECTOR, "tr.ngc:nth-child(3) > td:nth-child(5) > div:nth-child(1) > div:nth-child(1)").click()
        # switch focus to the popup for Human and Mouse cardiovascular system abnormalities for JUP/Jup
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert all row 4 results for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/p/table"))
        cell4 = mp_table.get_cell(5, 1)
        print(cell4.text)
        # verify the Mouse Phenotypes for row 4, then click it
        self.assertEqual(cell4.text, "Juptm1Ruiz/Jup+\nTg(Myh6-Jup*)1Ajm/0")
        cell4.click()
        # switch focus to the new tab for Phenotypes associated with Juptm1Ruiz/Jup+ Tg(Myh6-Jup*)1Ajm/0
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        geno = self.driver.find_element(By.CLASS_NAME, 'genoID')
        # assert the Genotype ID is correct
        self.assertEqual(geno.text, 'MGI:5660499')
        # locate the Mouse Models of Human Disease table
        mm_table = self.driver.find_element(By.CLASS_NAME, 'results')
        table = Table(mm_table)
        # Find the first table column for row 1
        mm1 = table.get_cell(1, 0)
        print(mm1.text)
        # Find the second table column for row 1
        doid1 = table.get_cell(1, 1)
        print(doid1.text)
        # Assert the Disease and DOID are correct
        self.assertEqual(mm1.text, "arrhythmogenic right ventricular dysplasia 12")
        self.assertEqual(doid1.text, 'DOID:0110083')

    def test_rollup_rule3_1_do(self):
        """
        @status: Tests that Mutation Involves.
        If the genotype has exactly 1 marker in (M) and that marker is of feature type: heritable phenotypic marker, complex/cluster/region, or any descendent of cytogenetic marker and has at least one mutation involves relationship and does NOT have the attribute “inserted expressed sequence”, then roll-up this genotype to the marker in (M). (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Transgene and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the Transgene marker (M) and non-transgene marker (I) (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Docking Site, and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the mutation involves marker (I) and NOT to the Docking Site marker (CREAM)
        @note: rollup-rule3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Del(5Letm1-D5Mit81)3Jcs")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Del(5Letm1-D5Mit81)3Jcs').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseRibbon'))):
            print('Human Diseases ribbon is loaded')
        # find the Human Diseases 'More' toggle and click it
        self.driver.find_element(By.ID, 'hdToggle').click()
        time.sleep(2)
        # find the Human Disease table
        disease_table = self.driver.find_element(By.ID, "humanDiseaseTable")
        table = Table(disease_table)
        # Iterate and print the results for column Human Disease
        strn = table.get_column_cells('Human Disease')
        dlist = iterate.getTextAsList(strn)
        print(dlist)
        # verify the Human Diseases of each row
        self.assertEqual(dlist[1], "Wolf-Hirschhorn syndrome\nIDs")
        # find the View Models link and click it
        driver.find_element(By.ID, 'showDOID_0050460').click()
        # find the popup Model table and click the first View link in the Phenotypes column
        self.driver.find_element(By.LINK_TEXT, "View").click()
        # switch focus to the new tab for strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'titleBarMainTitle'))):
            print('Page title is loaded')
        # verify the disease listed in the Mouse Models of Human Disease table is correct
        disease_table = Table(self.driver.find_element(By.CLASS_NAME, "results"))
        cell = disease_table.get_cell(1, 0)
        print(cell.text)
        # Asserts that the right Human disease is displayed
        self.assertEqual(cell.text, 'Wolf-Hirschhorn syndrome')

    def test_rollup_rule3_1_mp(self):
        """
        @status: Tests that Mutation Involves.
        If the genotype has exactly 1 marker in (M) and that marker is of feature type: heritable phenotypic marker, complex/cluster/region, or any descendent of cytogenetic marker and has at least one mutation involves relationship and does NOT have the attribute “inserted expressed sequence”, then roll-up this genotype to the marker in (M). (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Transgene and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the Transgene marker (M) and non-transgene marker (I) (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Docking Site, and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the mutation involves marker (I) and NOT to the Docking Site marker (CREAM)
        @note: rollup-rule3.1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Del(5Letm1-D5Mit81)3Jcs")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Del(5Letm1-D5Mit81)3Jcs').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('The Summary Ribbon is displayed')
        # find the Phenotype slim grid and click the Craniofacial box
        self.driver.find_element(By.ID, 'mpSlimgrid5Div').click()
        time.sleep(2)
        # switch focus to the new tab for Phenotype annotations related to craniofacial
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert the result for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/div[2]/table[2]"))
        cell1 = mp_table.get_cell(2, 1)
        print(cell1.text)
        # verify the Mouse Phenotypes for each row
        self.assertEqual(cell1.text, "Del(5Letm1-D5Mit81)3Jcs/+")


    def test_rollup_rule3_1_hmdc(self):
        """
        @status: Tests that Mutation Involves.
        If the genotype has exactly 1 marker in (M) and that marker is of feature type: heritable phenotypic marker, complex/cluster/region, or any descendent of cytogenetic marker and has at least one mutation involves relationship and does NOT have the attribute “inserted expressed sequence”, then roll-up this genotype to the marker in (M). (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Transgene and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the Transgene marker (M) and non-transgene marker (I) (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Docking Site, and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the mutation involves marker (I) and NOT to the Docking Site marker (CREAM)
        @note: rollup-rule3
        """
        driver = self.driver
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Del(5Letm1-D5Mit81)3Jcs")  # identifies the input field and a marker symbol
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        time.sleep(2)
        # Find the craniofacial box for Del(5Letm1-D5Mit81)3Jcs and click it.
        self.driver.find_element(By.CSS_SELECTOR, "td.middle:nth-child(4) > div:nth-child(1) > div:nth-child(1)").click()
        # switch focus to the popup for Mouse craniofacial abnormalities for Del(5Letm1-D5Mit81)3Jcs
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert row 1 result for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/p/table"))
        cell1 = mp_table.get_cell(2, 1)
        print(cell1.text)
        # verify the Mouse Phenotypes for row 1, then click it
        self.assertEqual(cell1.text, "Del(5Letm1-D5Mit81)3Jcs/+")
        cell1.click()
        # switch focus to the new tab for Phenotypes associated with Del(5Letm1-D5Mit81)3Jcs/+
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        geno = self.driver.find_element(By.CLASS_NAME, 'genoID')
        # assert the Genotype ID is correct for Del(5Letm1-D5Mit81)3Jcs/+
        self.assertEqual(geno.text, 'MGI:3798297')
        # locate the Mouse Models of Human Disease table
        mm_table = self.driver.find_element(By.CLASS_NAME, 'results')
        table = Table(mm_table)
        # Find the first table column for row 1
        mm1 = table.get_cell(1, 0)
        print(mm1.text)
        # Find the second table column for row 1
        doid1 = table.get_cell(1, 1)
        print(doid1.text)
        # Assert the Disease and DOID are correct
        self.assertEqual(mm1.text, "Wolf-Hirschhorn syndrome")
        self.assertEqual(doid1.text, 'DOID:0050460')

    def test_rollup_rule3_2_do(self):
        """
        !!!!This test is not complete because currently(5/1/2024) there is no example.!!!!!!!
        @status: Tests that Mutation Involves.
        If the genotype has exactly 1 marker in (M) and that marker is of feature type: heritable phenotypic marker, complex/cluster/region, or any descendent of cytogenetic marker and has at least one mutation involves relationship and does NOT have the attribute “inserted expressed sequence”, then roll-up this genotype to the marker in (M). (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Transgene and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the Transgene marker (M) and non-transgene marker (I) (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Docking Site, and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the mutation involves marker (I) and NOT to the Docking Site marker (CREAM)
        @note: rollup-rule3
        """
        #driver = self.driver
        #driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        #self.driver.find_element(By.NAME, 'nomen').send_keys("Tg(CAG-CHRM3*,-mCitrine)1Ute")
        #self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        #self.driver.find_element(By.LINK_TEXT, 'Tg(CAG-CHRM3*,-mCitrine)1Ute').click()
        #if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'originHeader'))):
            #print('Transgene origin ribbon is loaded')
        # find the Human Diseases 'More' toggle and click it
        #self.driver.find_element(By.ID, 'hdToggle').click()
        #time.sleep(2)
        # find the Human Disease table
        #disease_table = self.driver.find_element(By.ID, "humanDiseaseTable")
        #table = Table(disease_table)
        # Iterate and print the results for column Human Disease
        #strn = table.get_column_cells('Human Disease')
        #dlist = iterate.getTextAsList(strn)
        #print(dlist)
        # verify the Human Diseases of each row
        #self.assertEqual(dlist[1], "Wolf-Hirschhorn syndrome\nIDs")
        # find the View Models link and click it
        #driver.find_element(By.ID, 'showDOID_0050460').click()
        # find the popup Model table and click the first View link in the Phenotypes column
        #self.driver.find_element(By.LINK_TEXT, "View").click()
        # switch focus to the new tab for strain detail page
        #self.driver.switch_to.window(self.driver.window_handles[-1])
        #wait.forNewWindow(self.driver, 2)
        #if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'titleBarMainTitle'))):
            #print('Page title is loaded')
        # verify the disease listed in the Mouse Models of Human Disease table is correct
        #disease_table = Table(self.driver.find_element(By.CLASS_NAME, "results"))
        #cell = disease_table.get_cell(1, 0)
        #print(cell.text)
        # Asserts that the right Human disease is displayed
        #self.assertEqual(cell.text, 'Wolf-Hirschhorn syndrome')

    def test_rollup_rule3_2_hmdc(self):
        """
        @status: Tests that Mutation Involves.
        If the genotype has exactly 1 marker in (M) and that marker is of feature type: heritable phenotypic marker, complex/cluster/region, or any descendent of cytogenetic marker and has at least one mutation involves relationship and does NOT have the attribute “inserted expressed sequence”, then roll-up this genotype to the marker in (M). (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Transgene and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the Transgene marker (M) and non-transgene marker (I) (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Docking Site, and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the mutation involves marker (I) and NOT to the Docking Site marker (CREAM)
        @note: rollup-rule3
        """

    def test_rollup_rule3_3_do(self):
        """
        @status: Tests that Mutation Involves.
        If the genotype has exactly 1 marker in (M) and that marker is of feature type: heritable phenotypic marker, complex/cluster/region, or any descendent of cytogenetic marker and has at least one mutation involves relationship and does NOT have the attribute “inserted expressed sequence”, then roll-up this genotype to the marker in (M). (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Transgene and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the Transgene marker (M) and non-transgene marker (I) (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Docking Site, and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the mutation involves marker (I) and NOT to the Docking Site marker (CREAM)
        @note: rollup-rule3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Tafazzin")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Tafazzin').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseRibbon'))):
            print('Human Diseases ribbon is loaded')
        # find the Human Diseases 'More' toggle and click it
        self.driver.find_element(By.ID, 'hdToggle').click()
        time.sleep(2)
        # find the Human Disease table
        disease_table = self.driver.find_element(By.ID, "humanDiseaseTable")
        table = Table(disease_table)
        # Iterate and print the results for column Human Disease
        strn = table.get_column_cells('Human Disease')
        dlist = iterate.getTextAsList(strn)
        print(dlist)
        # verify the Human Diseases of each row
        self.assertEqual(dlist[1], "Barth syndrome\nIDs")
        # find the View Models link and click it
        driver.find_element(By.ID, 'showDOID_0050476').click()
        # find the popup Model table and click the first View link in the Phenotypes column
        self.driver.find_element(By.LINK_TEXT, "View").click()
        # switch focus to the new tab for strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'titleBarMainTitle'))):
            print('Page title is loaded')
        # verify the disease listed in the Mouse Models of Human Disease table is correct
        disease_table = Table(self.driver.find_element(By.CLASS_NAME, "results"))
        cell = disease_table.get_cell(1, 0)
        print(cell.text)
        # Asserts that the right Human disease is displayed
        self.assertEqual(cell.text, 'Barth syndrome')


    def test_rollup_rule3_3_mp(self):
        """
        @status: Tests that Mutation Involves.
        If the genotype has exactly 1 marker in (M) and that marker is of feature type: heritable phenotypic marker, complex/cluster/region, or any descendent of cytogenetic marker and has at least one mutation involves relationship and does NOT have the attribute “inserted expressed sequence”, then roll-up this genotype to the marker in (M). (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Transgene and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the Transgene marker (M) and non-transgene marker (I) (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Docking Site, and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the mutation involves marker (I) and NOT to the Docking Site marker (CREAM)
        @note: rollup-rule3.3
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Tafazzin")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Tafazzin').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('The Summary Ribbon is displayed')
        # find the Phenotype slim grid and click the Muscle box
        mpsgrid = self.driver.find_element(By.ID, 'mpSlimgrid18Div')
        driver.execute_script("arguments[0].click();", mpsgrid)
        time.sleep(2)
        # switch focus to the new tab for Phenotype annotations related to Muscle
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert the row 2 result for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/div[2]/table[2]"))
        cell1 = mp_table.get_cell(3, 1)
        print(cell1.text)
        # verify the Mouse Phenotypes for this row
        self.assertEqual(cell1.text, "Gt(ROSA)26Sortm37(H1/tetO-RNAi:Tafazzin)Arte/?")

    def test_rollup_rule3_3_hmdc(self):
        """
        @status: Tests that Mutation Involves.
        If the genotype has exactly 1 marker in (M) and that marker is of feature type: heritable phenotypic marker, complex/cluster/region, or any descendent of cytogenetic marker and has at least one mutation involves relationship and does NOT have the attribute “inserted expressed sequence”, then roll-up this genotype to the marker in (M). (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Transgene and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the Transgene marker (M) and non-transgene marker (I) (CREAM)
        If the genotype has exactly 1 marker in (M) and that marker is a Docking Site, and has exactly 1 mutation involves relationship marker (I) and does NOT have the attribute “inserted expressed sequence”, then roll this genotype up to the mutation involves marker (I) and NOT to the Docking Site marker (CREAM)
        @note: rollup-rule3
        """
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Tafazzin")  # identifies the input field and a marker symbol
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        time.sleep(2)
        # Find the muscle box for Tafazzin and click it.
        self.driver.find_element(By.CSS_SELECTOR, "td.middle:nth-child(9) > div:nth-child(1) > div:nth-child(1)").click()
        # switch focus to the popup for Human and Mouse muscle abnormalities for TAFAZZIN/Tafazzin
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert row 2 result for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/p/table"))
        cell1 = mp_table.get_cell(3, 1)
        print(cell1.text)
        # verify the Mouse Phenotypes for row 1, then click it
        self.assertEqual(cell1.text, "Gt(ROSA)26Sortm37(H1/tetO-RNAi:Tafazzin)Arte/?")
        cell1.click()
        # switch focus to the new tab for Phenotypes associated with Gt(ROSA)26Sortm37(H1/tetO-RNAi:Tafazzin)Arte/?
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        geno = self.driver.find_element(By.CLASS_NAME, 'genoID')
        # assert the Genotype ID is correct for Gt(ROSA)26Sortm37(H1/tetO-RNAi:Tafazzin)Arte/?
        self.assertEqual(geno.text, 'MGI:5288490')
        # locate the Mouse Models of Human Disease table
        mm_table = self.driver.find_element(By.CLASS_NAME, 'results')
        table = Table(mm_table)
        # Find the first table column for row 1
        mm1 = table.get_cell(1, 0)
        print(mm1.text)
        # Find the second table column for row 1
        doid1 = table.get_cell(1, 1)
        print(doid1.text)
        # Assert the Disease and DOID are correct
        self.assertEqual(mm1.text, "Barth syndrome")
        self.assertEqual(doid1.text, 'DOID:0050476')

    def test_rollup_rule4_do(self):
        """
        @status: Tests Transgene.
        If the marker in (M) is a transgene; roll-up the genotype to that marker.
        @note: rollup-rule-4
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Tg(APPSwFlLon,PSEN1*M146L*L286V)6799Vas")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Tg(APPSwFlLon,PSEN1*M146L*L286V)6799Vas').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseModelsHeader'))):
            print('Disease Models ribbon is loaded')
        # find the Human Diseases table
        disease_table = self.driver.find_element(By.ID, "diseasetable_id")
        table = Table(disease_table)
        # Iterate and print the results for column Human Disease
        strn = table.get_column_cells('Human Diseases')
        dlist = iterate.getTextAsList(strn)
        print(dlist)
        # verify the Human Diseases of each row
        self.assertEqual(dlist[1], "Alzheimer's disease\nIDs")

    def test_rollup_rule4_mp(self):
        """
        @status: Tests Transgene.
        If the marker in (M) is a transgene; roll-up the genotype to that marker.
        @note: rollup-rule-4
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Tg(APPSwFlLon,PSEN1*M146L*L286V)6799Vas")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Tg(APPSwFlLon,PSEN1*M146L*L286V)6799Vas').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryHeader'))):
            print('The Summary Ribbon is displayed')
        # find the Phenotype table and click the tg14 box for mortality/aging
        tg14 = self.driver.find_element(By.CSS_SELECTOR, '#mortality_aging_id_row > td:nth-child(16) > a:nth-child(1)')
        driver.execute_script("arguments[0].click();", tg14)
        time.sleep(2)
        # switch focus to the new tab for Phenotypes Associated with this Genotype
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        pheno = self.driver.find_element(By.CSS_SELECTOR, '.MP0002083')
        print(pheno.text)
        # verify the correct phenotype is displayed
        self.assertEqual(pheno.text, "premature death")

    def test_rollup_rule4_hmdc(self):
        """
        @status: Tests Transgene.
        If the marker in (M) is a transgene; roll-up the genotype to that marker.
        @note: rollup-rule-4
        """

    def test_rollup_rule5_do(self):
        """
        @status: Tests Transgene Expresses One Component.
        If the marker in (M) is a transgene AND there is exactly one marker for the genotype in (EC) and it is a
        mouse component, then also roll-up the genotype to the EC marker.
        @note: rollup-rule-5
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Tg(Pnkd*A7V*A9V,-DsRed)704Ljp")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Tg(Pnkd*A7V*A9V,-DsRed)704Ljp').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseModelsHeader'))):
            print('Disease Models ribbon is loaded')
        # find the Human Diseases table
        disease_table = self.driver.find_element(By.ID, "diseasetable_id")
        table = Table(disease_table)
        # Iterate and print the results for column Human Disease
        strn = table.get_column_cells('Human Diseases')
        dlist = iterate.getTextAsList(strn)
        print(dlist)
        # verify the Human Diseases of each row
        self.assertEqual(dlist[1], "paroxysmal nonkinesigenic dyskinesia 1\nIDs")

    def test_rollup_rule5_mp(self):
        """
        @status: Tests Transgene Expresses One Component.
        If the marker in (M) is a transgene AND there is exactly one marker for the genotype in (EC) and it is a
        mouse component, then also roll-up the genotype to the EC marker.
        @note: rollup-rule-5
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pnkd")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pnkd').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('The Summary Ribbon is displayed')
        # find the Phenotype slim grid and click the homeostasis/metabolism box
        mpsgrid = self.driver.find_element(By.ID, 'mpSlimgrid12Div')
        driver.execute_script("arguments[0].click();", mpsgrid)
        time.sleep(2)
        # switch focus to the new tab for Phenotype annotations related to cellular
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert all 3 results for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/div[2]/table[2]"))
        cell1 = mp_table.get_cell(2, 1)
        print(cell1.text)
        cell2 = mp_table.get_cell(3, 1)
        print(cell2.text)
        cell3 = mp_table.get_cell(4, 1)
        print(cell3.text)
        # verify the Mouse Phenotypes for row 4
        self.assertEqual(cell1.text, "Pnkdtm1Ljp/Pnkdtm1Ljp")
        self.assertEqual(cell2.text, "Tg(Pnkd*A7V*A9V,-DsRed)671Ljp/0")
        self.assertEqual(cell3.text, "Tg(Pnkd*A7V*A9V,-DsRed)704Ljp/0")

    def test_rollup_rule5_hmdc(self):
        """
        @status: Tests Transgene Expresses One Component.
        If the marker in (M) is a transgene AND there is exactly one marker for the genotype in (EC) and it is a
        mouse component, then also roll-up the genotype to the EC marker.
        @note: rollup-rule-5
        """
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Pnkd")  # identifies the input field and a marker symbol
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        time.sleep(2)
        # Find the homeostasis/metabolism box for Tg(Pnkd*A7V*A9V,-DsRed)704Ljp and click it.
        self.driver.find_element(By.CSS_SELECTOR, "tr.ngc:nth-child(5) > td:nth-child(4) > div:nth-child(1) > div:nth-child(1)").click()
        # switch focus to the popup for Mouse homeostasis/metabolism abnormalities for Tg(Pnkd*A7V*A9V,-DsRed)704Ljp
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert row 1 result for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/p/table"))
        cell = mp_table.get_cell(2, 1)
        print(cell.text)
        # verify the Mouse Phenotypes for row 1, then click it
        self.assertEqual(cell.text, "Tg(Pnkd*A7V*A9V,-DsRed)704Ljp/0")
        cell.click()
        # switch focus to the new tab for Phenotypes associated with Mouse homeostasis/metabolism abnormalities
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        geno = self.driver.find_element(By.CLASS_NAME, 'genoID')
        # assert the Genotype ID is correct for Tg(Pnkd*A7V*A9V,-DsRed)704Ljp/0
        self.assertEqual(geno.text, 'MGI:5469979')
        # locate the Mouse Models of Human Disease table
        mm_table = self.driver.find_element(By.CLASS_NAME, 'results')
        table = Table(mm_table)
        # Find the first table column for row 1
        mm1 = table.get_cell(1, 0)
        print(mm1.text)
        # Find the second table column for row 1
        doid1 = table.get_cell(1, 1)
        print(doid1.text)
        # Assert the Disease and DOID are correct
        self.assertEqual(mm1.text, "paroxysmal nonkinesigenic dyskinesia 1")
        self.assertEqual(doid1.text, 'DOID:0090049')

    def test_rollup_rule6_do(self):
        """
        @status: Tests Docking site Expresses One Component
        If the marker in (M) is a docking site AND there is exactly one marker for the genotype in (EC) and it is a
        mouse component, then roll-up the genotype to the EC marker.
            Current docking sites are: Col1a1, Gt(ROSA)26Sor, Hprt
        @note: rollup-rule-6
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Smo")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Smo').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseRibbon'))):
            print('Human Diseases ribbon is loaded')
        # find the Human Diseases 'More' toggle and click it
        self.driver.find_element(By.ID, 'hdToggle').click()
        time.sleep(2)
        # find the Human Disease table
        disease_table = self.driver.find_element(By.ID, "humanDiseaseTable")
        table = Table(disease_table)
        # Iterate and print the results for column Human Disease
        strn = table.get_column_cells('Human Disease')
        dlist = iterate.getTextAsList(strn)
        print(dlist)
        # verify the Human Diseases of each row
        self.assertEqual(dlist[1], "medulloblastoma\nIDs")
        # find the View Models link and click it
        driver.find_element(By.ID, 'showDOID_0050902').click()
        # find the popup Model table and click the first View link in the Phenotypes column
        self.driver.find_element(By.LINK_TEXT, "View").click()
        # switch focus to the new tab for strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'titleBarMainTitle'))):
            print('Page title is loaded')
        # verify the disease listed in the Mouse Models of Human Disease table is correct
        disease_table = Table(self.driver.find_element(By.CLASS_NAME, "results"))
        cell = disease_table.get_cell(1, 0)
        print(cell.text)
        # Asserts that the right Human disease is displayed
        self.assertEqual(cell.text, 'medulloblastoma')

    def test_rollup_rule6_mp(self):
        """
        @status: Tests Docking site Expresses One Component
        If the marker in (M) is a docking site AND there is exactly one marker for the genotype in (EC) and it is a
        mouse component, then roll-up the genotype to the EC marker.
            Current docking sites are: Col1a1, Gt(ROSA)26Sor, Hprt
        @note: rollup-rule-6
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Smo")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Smo').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('The Summary Ribbon is displayed')
        # find the Phenotype slim grid and click the nervous system box
        mpsgrid = self.driver.find_element(By.ID, 'mpSlimgrid19Div')
        driver.execute_script("arguments[0].click();", mpsgrid)
        time.sleep(2)
        # switch focus to the new tab for Phenotype annotations related to cellular
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert the 12th result for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/div[2]/table[3]"))
        cell = mp_table.get_cell(13, 1)
        print(cell.text)
        # verify the Mouse Phenotypes for row 12
        self.assertEqual(cell.text, "Gt(ROSA)26Sortm1(Smo/EYFP)Amc/Gt(ROSA)26Sortm1(Smo/EYFP)Amc\nTg(Atoh1-cre/Esr1*)14Fsh/0  (conditional)")

    def test_rollup_rule6_hmdc(self):
        """
        @status: Tests Docking site Expresses One Component
        If the marker in (M) is a docking site AND there is exactly one marker for the genotype in (EC) and it is a
        mouse component, then roll-up the genotype to the EC marker.
            Current docking sites are: Col1a1, Gt(ROSA)26Sor, Hprt
        @note: rollup-rule-6
        """
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Smo")  # identifies the input field and a marker symbol
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        time.sleep(2)
        # Find the nervous system box for Smo and click it.
        self.driver.find_element(By.CSS_SELECTOR, "tr.ngc:nth-child(3) > td:nth-child(21) > div:nth-child(1) > div:nth-child(1)").click()
        # switch focus to the popup for Human and Mouse nervous system abnormalities for SMO/Smo
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert row 11 result for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/p/table"))
        cell = mp_table.get_cell(13, 1)
        print(cell.text)
        # verify the Mouse Phenotypes for row 11, then click it
        self.assertEqual(cell.text, "Gt(ROSA)26Sortm1(Smo/EYFP)Amc/Gt(ROSA)26Sortm1(Smo/EYFP)Amc\nTg(Atoh1-cre/Esr1*)14Fsh/0  (conditional)")
        cell.click()
        # switch focus to the new tab for Phenotypes associated with Gt(ROSA)26Sortm1(Smo/EYFP)Amc/Gt(ROSA)26Sortm1(Smo/EYFP)Amc Tg(Atoh1-cre/Esr1*)14Fsh/0
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        geno = self.driver.find_element(By.CLASS_NAME, 'genoID')
        # assert the Genotype ID is correct for Gt(ROSA)26Sortm1(Smo/EYFP)Amc/Gt(ROSA)26Sortm1(Smo/EYFP)Amc Tg(Atoh1-cre/Esr1*)14Fsh/0
        self.assertEqual(geno.text, 'MGI:3810322')
        # locate the Mouse Models of Human Disease table
        mm_table = self.driver.find_element(By.CLASS_NAME, 'results')
        table = Table(mm_table)
        # Find the first table column for row 1
        mm1 = table.get_cell(1, 0)
        print(mm1.text)
        # Find the second table column for row 1
        doid1 = table.get_cell(1, 1)
        print(doid1.text)
        # Assert the Disease and DOID are correct
        self.assertEqual(mm1.text, "medulloblastoma")
        self.assertEqual(doid1.text, 'DOID:0050902')

    def test_rollup_rule7_do(self):
        """
        @status: Tests Single with no Expresses Component.
        If the marker in (M) is neither a transgene nor a docking site AND the alleles do NOT have any “inserted expressed
        sequence attribute”,, then roll-up the genotype to the marker in (M). (CREAM)
        @note: rollup-rule-7
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Btbd9")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Btbd9').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseRibbon'))):
            print('Human Diseases ribbon is loaded')
        # find the Human Diseases 'More' toggle and click it
        self.driver.find_element(By.ID, 'hdToggle').click()
        time.sleep(2)
        # find the Human Disease table
        disease_table = self.driver.find_element(By.ID, "humanDiseaseTable")
        table = Table(disease_table)
        # Iterate and print the results for column Human Disease
        strn = table.get_column_cells('Human Disease')
        dlist = iterate.getTextAsList(strn)
        print(dlist)
        # verify the Human Diseases of each row
        self.assertEqual(dlist[1], "restless legs syndrome\nIDs")
        # find the View Models link and click it
        driver.find_element(By.ID, 'showDOID_0050425').click()
        # find the popup Model table and click the first View link in the Phenotypes column
        self.driver.find_element(By.LINK_TEXT, "View").click()
        # switch focus to the new tab for strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'titleBarMainTitle'))):
            print('Page title is loaded')
        # verify the disease listed in the Mouse Models of Human Disease table is correct
        disease_table = Table(self.driver.find_element(By.CLASS_NAME, "results"))
        cell = disease_table.get_cell(1, 0)
        print(cell.text)
        # Asserts that the right Human disease is displayed
        self.assertEqual(cell.text, 'restless legs syndrome')

    def test_rollup_rule7_mp(self):
        """
        @status: Tests Single with no Expresses Component.
        If the marker in (M) is neither a transgene nor a docking site AND the alleles do NOT have any “inserted expressed
        sequence attribute”,, then roll-up the genotype to the marker in (M). (CREAM)
        @note: rollup-rule-7
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Btbd9")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Btbd9').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('The Summary Ribbon is displayed')
        # find the Phenotype slim grid and click the nervous system box
        mpsgrid = self.driver.find_element(By.ID, 'mpSlimgrid19Div')
        driver.execute_script("arguments[0].click();", mpsgrid)
        time.sleep(2)
        # switch focus to the new tab for Phenotype annotations related to nervous system
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert the 3rd result for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/div[2]/table[2]"))
        cell = mp_table.get_cell(4, 1)
        print(cell.text)
        # verify the Mouse Phenotypes for row 3
        self.assertEqual(cell.text, "Btbd9tm1c(EUCOMM)Wtsi/Btbd9tm1c(EUCOMM)Wtsi\nEmx1tm1(cre)Yql/Emx1+  (conditional)")

    def test_rollup_rule7_hmdc(self):
        """
        @status: Tests Single with no Expresses Component.
        If the marker in (M) is neither a transgene nor a docking site AND the alleles do NOT have any “inserted expressed
        sequence attribute”,, then roll-up the genotype to the marker in (M). (CREAM)
        @note: rollup-rule-7
        """
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Btbd9")  # identifies the input field and a marker symbol
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        time.sleep(2)
        # Find the nervous system box for Btbd9 and click it.
        self.driver.find_element(By.CSS_SELECTOR, "td.middle:nth-child(6) > div:nth-child(1) > div:nth-child(1)").click()
        # switch focus to the popup for Human and Mouse nervous system abnormalities for BTBD9/Btbd9
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert row 3 result for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/p/table"))
        cell = mp_table.get_cell(4, 1)
        print(cell.text)
        # verify the Mouse Phenotypes for row 3, then click it
        self.assertEqual(cell.text, "Btbd9tm1c(EUCOMM)Wtsi/Btbd9tm1c(EUCOMM)Wtsi\nEmx1tm1(cre)Yql/Emx1+  (conditional)")
        cell.click()
        # switch focus to the new tab for Phenotypes associated with Btbd9tm1c(EUCOMM)Wtsi/Btbd9tm1c(EUCOMM)Wtsi Emx1tm1(cre)Yql/Emx1+
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        geno = self.driver.find_element(By.CLASS_NAME, 'genoID')
        # assert the Genotype ID is correct for Gt(ROSA)26Sortm1(Smo/EYFP)Amc/Gt(ROSA)26Sortm1(Smo/EYFP)Amc Tg(Atoh1-cre/Esr1*)14Fsh/0
        self.assertEqual(geno.text, 'MGI:6488233')
        # locate the Mouse Models of Human Disease table
        mm_table = self.driver.find_element(By.CLASS_NAME, 'results')
        table = Table(mm_table)
        # Find the first table column for row 1
        mm1 = table.get_cell(1, 0)
        print(mm1.text)
        # Find the second table column for row 1
        doid1 = table.get_cell(1, 1)
        print(doid1.text)
        # Assert the Disease and DOID are correct
        self.assertEqual(mm1.text, "restless legs syndrome")
        self.assertEqual(doid1.text, 'DOID:0050425')

    def test_rollup_rule8_do(self):
        """
        @status: Tests Self-expressing single
        If the marker in (M) is neither a transgene nor a docking site and there is exactly 1 marker in (EC) and it is a
        mouse component, AND it is the same marker in (M), then roll-up the genotype to the marker in (M).
        @note: rollup-rule-8  ***as of 04/2024 no example with a DO annotation***
        """


    def test_rollup_rule8_mp(self):
        """
        @status: Tests Self-expressing single
        If the marker in (M) is neither a transgene nor a docking site and there is exactly 1 marker in (EC) and it is a
        mouse component, AND it is the same marker in (M), then roll-up the genotype to the marker in (M).
        @note: rollup-rule-8
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Erbb2")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Erbb2').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('The Summary Ribbon is displayed')
        # find the Phenotype slim grid and click the mortality/aging system box
        mpsgrid = self.driver.find_element(By.ID, 'mpSlimgrid17Div')
        driver.execute_script("arguments[0].click();", mpsgrid)
        time.sleep(2)
        # switch focus to the new tab for Phenotype annotations related to nervous system
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert the 8th result for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/div[2]/table[2]"))
        cell = mp_table.get_cell(9, 1)
        print(cell.text)
        # verify the Mouse Phenotypes for row 8
        self.assertEqual(cell.text, "Erbb2tm8(Erbb2)Mul/Erbb2tm8(Erbb2)Mul")

    def test_rollup_rule8_hmdc(self):
        """
        @status: Tests Self-expressing single
        If the marker in (M) is neither a transgene nor a docking site and there is exactly 1 marker in (EC) and it is a
        mouse component, AND it is the same marker in (M), then roll-up the genotype to the marker in (M).
        @note: rollup-rule-8  ***as of 04/2024 no example with a DO annotation***
        """
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Erbb2")  # identifies the input field and a marker symbol
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        time.sleep(2)
        # Find the mortality/aging box for Erbb2 and click it.
        self.driver.find_element(By.CSS_SELECTOR, "tr.ngc:nth-child(3) > td:nth-child(13) > div:nth-child(1) > div:nth-child(1)").click()
        # switch focus to the popup for Mouse mortality/aging abnormalities for ERBB2/Erbb2
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert row 8 result for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/p/table"))
        cell = mp_table.get_cell(7, 1)
        print(cell.text)
        # verify the Mouse Phenotypes for row 9, then click it
        self.assertEqual(cell.text, "Erbb2tm8.1(Erbb2)Mul/Erbb2tm8.1(Erbb2)Mul")
        cell.click()
        # switch focus to the new tab for Phenotypes associated with Erbb2tm8.1(Erbb2)Mul/Erbb2tm8.1(Erbb2)Mul
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        geno = self.driver.find_element(By.CLASS_NAME, 'genoID')
        # assert the Genotype ID is correct for Gt(ROSA)26Sortm1(Smo/EYFP)Amc/Gt(ROSA)26Sortm1(Smo/EYFP)Amc Tg(Atoh1-cre/Esr1*)14Fsh/0
        self.assertEqual(geno.text, 'MGI:3805580')

    def test_rollup_rule9_do(self):
        """
        @status: Tests Docking site Expresses No Components
        If the marker in (M) is a docking site other than Gt(ROSA)26Sor AND the alleles do NOT have any “inserted expressed
        sequence attribute”, then roll-up the genotype to the docking site marker. (CREAM)
        @note: rollup-rule-9
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Col1a1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Col1a1').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'diseaseRibbon'))):
            print('Human Diseases ribbon is loaded')
        # find the Human Diseases 'More' toggle and click it
        self.driver.find_element(By.ID, 'hdToggle').click()
        time.sleep(2)
        # find the Human Disease table
        disease_table = self.driver.find_element(By.ID, "humanDiseaseTable")
        table = Table(disease_table)
        # Iterate and print the results for column Human Disease
        strn = table.get_column_cells('Human Disease')
        dlist = iterate.getTextAsList(strn)
        time.sleep(2)
        print(dlist)
        # verify the Human Diseases of each row
        self.assertEqual(dlist[1], "osteogenesis imperfecta\nIDs")
        # find the View Models link for osteogenesis imperfecta type 2 and click it
        driver.find_element(By.ID, 'showDOID_0110341').click()
        # find the popup Model table and click the first View link in the Phenotypes column
        self.driver.find_element(By.LINK_TEXT, "View").click()
        # switch focus to the new tab for strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'titleBarMainTitle'))):
            print('Page title is loaded')
        # verify the disease listed in the Mouse Models of Human Disease table is correct
        disease_table = Table(self.driver.find_element(By.CLASS_NAME, "results"))
        cell = disease_table.get_cell(1, 0)
        print(cell.text)
        # Asserts that the right Human disease is displayed
        self.assertEqual(cell.text, 'osteogenesis imperfecta type 2')

    def test_rollup_rule9_mp(self):
        """
        @status: Tests Docking site Expresses No Components
        If the marker in (M) is a docking site other than Gt(ROSA)26Sor AND the alleles do NOT have any “inserted expressed
        sequence attribute”, then roll-up the genotype to the docking site marker. (CREAM)
        @note: rollup-rule-9
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/marker/")
        # find the Gene/Marker Symbol/Name field and enter the marker symbol
        self.driver.find_element(By.NAME, 'nomen').send_keys("Col1a1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Col1a1').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('The Summary Ribbon is displayed')
        # find the Phenotype slim grid and click the nervous system box
        mpsgrid =self.driver.find_element(By.ID, 'mpSlimgrid19Div')
        driver.execute_script("arguments[0].click();", mpsgrid)
        time.sleep(2)
        # switch focus to the new tab for Phenotype annotations related to nervous system
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert the 2nd result for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/div[2]/table[3]"))
        cell = mp_table.get_cell(3,1)
        print(cell.text)
        # verify the Mouse Phenotypes for row 2
        self.assertEqual(cell.text, "Col1a1Aga2/Col1a1+")

    def test_rollup_rule9_hmdc(self):
        """
        @status: Tests Docking site Expresses No Components
        If the marker in (M) is a docking site other than Gt(ROSA)26Sor AND the alleles do NOT have any “inserted expressed
        sequence attribute”, then roll-up the genotype to the docking site marker. (CREAM)
        @note: rollup-rule-9
        """
        self.driver.get(config.TEST_URL + "/humanDisease.shtml")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Col1a1")  # identifies the input field and a marker symbol
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Grid tab and click on it
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        time.sleep(2)
        # Find the nervous system box for Col1a1 and click it.
        self.driver.find_element(By.CSS_SELECTOR, "tr.ngc:nth-child(3) > td:nth-child(22) > div:nth-child(1) > div:nth-child(1)").click()
        # switch focus to the popup for Human and Mouse nervous system abnormalities for COL1A1/Col1a1
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find the Mouse Phenotypes table and assert row 2 result for the Mouse Phenotype column
        mp_table = Table(self.driver.find_element(By.XPATH, "/html/body/p/table"))
        cell = mp_table.get_cell(3, 1)
        print(cell.text)
        # verify the Mouse Phenotypes for row 3, then click it
        self.assertEqual(cell.text, "Col1a1Aga2/Col1a1+")
        cell.click()
        # switch focus to the new tab for Phenotypes associated with Col1a1Aga2/Col1a1+
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        geno = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div[1]/font')
        # assert the Genotype ID is correct for Col1a1Aga2/Col1a1+
        self.assertEqual(geno.text, 'MGI:3769907')
        # locate the Mouse Models of Human Disease table
        mm_table = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[4]/div[2]/table')
        table = Table(mm_table)
        # Find the first table column for row 1
        mm1 = table.get_cell(1, 0)
        print(mm1.text)
        # Find the second table column for row 1
        doid1 = table.get_cell(1, 1)
        print(doid1.text)
        # Assert the Disease and DOID are correct
        self.assertEqual(mm1.text, "osteogenesis imperfecta type 2")
        self.assertEqual(doid1.text, 'DOID:0110341')

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRefByStrain))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))