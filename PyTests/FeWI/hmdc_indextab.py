"""
Created on Nov 17, 2016
This test should check the column headers for correct display and order. It currently verifies the returned genes
in correct order and the returned diseases and their order,
Updated: July 2017 (jlewis) - updates to make tests more tolerant to changes in annotations.  e.g. removing counts
@author: jeffc
Verify the headings on the Gene Homologs x Phenotypes/Diseases tab( or Index tab) are correct and in the correct order.
Verify that human/mouse; human only; mouse only disease associations exist as expected by checking the Title of the pop-up
Verify the correct genes are returned for this query, both human and mouse.  This includes 3 transgenes that are
    returned due to Expressed Component
Verify the correct genes are returned for this query, The symbol used has several unusual characters
Verify that the expected annotations are present under the phenotype systems.This includes a system with both mouse
     and human; a system with only human; and a system with only mouse.  The check is made using the Title of the phenotype pop-up
"""
import os.path
import sys
import tracemalloc
import unittest
import config

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate, wait

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)

# Tests
tracemalloc.start()


class TestHmdcIndex(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/diseasePortal")
        self.driver.implicitly_wait(10)

    def test_index_tab_headers(self):
        """
        @status this test verifies the headings on the Gene Homologs x Phenotypes/Diseases tab( or Index tab) are correct and
                in the correct order.
        @see: HMDC-grid-# (tab heading, gene column headings)
        """
        print("BEGIN test_index_tab_headers")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Gata1")  # indentifies the input field and enters gata1
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        self.assertIn("Gene Homologs x Phenotypes/Diseases", grid_tab.text)
        grid_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'tr.ngc:nth-child(4) > td:nth-child(2) > div:nth-child(1) > a:nth-child(1)'))):
            print('HMDC grid data loaded')
        human_header = self.driver.find_element(By.CLASS_NAME, 'hgHeader')
        self.assertEqual(human_header.text, 'Human Gene', 'The human gene header is missing')
        mouse_header = self.driver.find_element(By.CLASS_NAME, 'mgHeader')
        self.assertEqual(mouse_header.text, 'Mouse Gene', 'The mouse gene header is missing')

    def test_index_tab_diseases(self):
        """
        @status This test verifies that human/mouse; human only; mouse only disease associations exist as expected by checking the Title of the pop-up
        @see: HMDC-grid-2 (Return row with both mouse/human annoations); HMDC-popup-17 (1 row per genocluster in disease pop-up);
        """
        print("BEGIN test_index_tab_diseases")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Gucy2c")  # identifies the input field and enters gata1
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        grid_tab.click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'td.middle:nth-child(2) > div:nth-child(1) > a:nth-child(1)'))):
            print('HMDC grid data loaded')
        # captures all the table data blocks of phenotypes and diseases on the first row of data
        phenodiseasecells = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.center.cell.middle")
        parentwindowid = self.driver.current_window_handle

        # click on disease cell with human and mouse annotations; verify pop-up title
        phenodiseasecells[12].click()  # clicks the first phenotype data cell to open up the genotype popup page
        wait.forNewWindow(self.driver, 5)
        self.driver.switch_to.window(self.driver.window_handles[1])  # switches focus to the genotype popup page
        matching_text = "Human Genes and Mouse Models for autosomal genetic disease and GUCY2C/Gucy2c"
        # asserts the heading text is correct in page source
        print(self.driver.title)
        self.assertIn(matching_text, self.driver.title, 'matching mouse/human text not displayed')
        self.driver.close()
        self.driver.switch_to.window(parentwindowid)

        # click on disease cell with only human annotations; verify pop-up title
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print('disease cell with only human: ' + grid_tab.text)
        grid_tab.click()
        phenodiseasecells[
            13].click()  # clicks the first phenotype data cell to open up the craniofacial phenotype popup page
        wait.forNewWindow(self.driver, 5)
        self.driver.switch_to.window(self.driver.window_handles[1])  # switches focus to the Phenotype popup page
        matching_text = "Human Genes for gastrointestinal system disease and GUCY2C/Gucy2c"
        # asserts the heading text is correct in page source
        print('header text is: ' + self.driver.title)
        self.assertIn(matching_text, self.driver.title, 'matching human only text not displayed')
        self.driver.close()
        self.driver.switch_to.window(parentwindowid)

        # click on disease cell with only mouse annotations; verify pop-up title
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print('disease cell with only mouse: ' + grid_tab.text)
        grid_tab.click()
        phenodiseasecells[
            11].click()  # clicks the first phenotype data cell to open up the craniofacial phenotype popup page
        wait.forNewWindow(self.driver, 5)
        self.driver.switch_to.window(self.driver.window_handles[1])  # switches focus to the Phenotype popup page
        matching_text = "Mouse Models for acquired metabolic disease and GUCY2C/Gucy2c"
        # asserts the heading text is correct in page source
        print('header text is: ' + self.driver.title)
        self.assertIn(matching_text, self.driver.title, 'matching mouse only text not displayed')

        # Identify the table
        mouse_geno_table = self.driver.find_element(By.CLASS_NAME, "popupTable")
        data = mouse_geno_table.find_element(By.TAG_NAME, "td")
        print(data.text)
        # find all the TR tags in the table and iterate through them
        cells = mouse_geno_table.find_elements(By.TAG_NAME, "tr")
        print(iterate.getTextAsList(cells))

        # move mouse genotype data
        mousegenotyperows = iterate.getTextAsList(cells)
        # asserts that one of the genoclusters with annotations to this Phenotype System is returned.
        self.assertIn('Gucy2ctm1Gar/Gucy2ctm1Gar', mousegenotyperows)
        print("Gucy2c<tm1Gar> genocluster found in disease pop-up")

    def test_index_tab_genes(self):
        """
        @status this test verifies the correct genes are returned for this query, both human and mouse.  This includes 3 transgenes
                that are returned due to Expressed Component.  In these cases the transgene has 1 expresses component = mouse gene Gata1.
        @see: HMDC-grid-2 (return row with both human and mouse genes);
              HMDC-GQ-1, 3, 9 (query that matches mouse symbol, human symbol, expressed component that passes roll-up)
              HMDC-grid-27 (return row with transgene w/ expresses component and rolled up genoclusters)
              Sue states that the 2 Transgenes will no longer return because the rollup rule change does not display complex genotypes now 12/29/2023
        """
        print("BEGIN test_index_tab_genes")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Gata1")  # identifies the input field and enters gata1
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        grid_tab.click()
        hgenes = self.driver.find_element(By.CSS_SELECTOR, "td.ngc.left.middle.cell.first")
        print(hgenes.text)
        self.assertEqual(hgenes.text, 'GATA1')  # returned due to gene nomenclature match
        mgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.last")

        searchtermitems = iterate.getTextAsList(mgenes)
        self.assertIn("Gata1", searchtermitems)  # returned due to gene nomenclature match
        # self.assertIn("Tg(Gata1)#Mym", searchTermItems) #returned due to Expressed Component w/ rolled up genocluster
        # self.assertIn("Tg(Gata1*V205G)1Mym", searchTermItems) #returned due to Expressed Component w/ rolled up genocluster
        self.assertIn("Tg(HBB-Gata1)G4Phi",
                      searchtermitems)  # returned due to Expressed Component w/ rolled up genocluster
        print(searchtermitems)

    def test_index_tab_genes_Unique_symbol(self):
        """
        @status this test verifies the correct genes are returned for this query, The symbol used has several unusual characters.
        @see: HMDC-GQ-2 (symbols with special characters);
              HMDC-grid-6 (Return row with no human gene)
        """
        print("BEGIN test_index_tab_genes_Unique_symbol")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Tg(IGH@*)SALed")  # identifies the input field and enters gata1
        # wait.forAngular(self.driver)
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Genes tab and verify the tab's text
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        grid_tab.click()
        if WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'li.uib-tab:nth-child(1) > a:nth-child(1)'))):
            print('HMDC grid data loaded')
        mgenes = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.left.middle.cell.last")
        searchtermitems = iterate.getTextAsList(mgenes)
        self.assertEqual(searchtermitems[0], "Tg(IGH@*)SALed")
        print(searchtermitems)

    def test_genotype_popup(self):
        """
        @status This test verifies that the expected annotations are present under the phenotype systems.
                This includes a system with both mouse and human; a system with only human; and a system with
                only mouse.  The check is made using the Title of the phenotype pop-up.
        @see: HMDC-grid-2; HMDC-popup-1 (display pop-up page by clicking cell); HMDC-popup-11 (return row for mouse genocluster)
        """
        print("BEGIN test_genotype_popup")
        my_select = self.driver.find_element(By.XPATH,
                                             "//select[starts-with(@id, 'field_0_')]")  # identifies the select field and picks the gene symbols option
        for option in my_select.find_elements(By.TAG_NAME, "option"):
            if option.text == 'Gene Symbol(s) or ID(s)':
                option.click()
                break

        self.driver.find_element(By.NAME, "formly_3_input_input_0").send_keys(
            "Gata1")  # identifies the input field and enters Gata1
        self.driver.find_element(By.ID, "searchButton").click()
        wait.forAngular(self.driver)
        # identify the Grid tab and print out tab text
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)
        grid_tab.click()
        # captures all the table data blocks of phenotypes on the first row of data
        phenocells = self.driver.find_elements(By.CSS_SELECTOR, "td.ngc.center.cell.middle")
        parentwindowid = self.driver.current_window_handle

        # Grid pop-up for a Phenotype System with both Human and Mouse annotations
        phenocells[0].click()  # clicks the first phenotype data cell to open up the genotype popup page
        self.driver.switch_to.window(self.driver.window_handles[1])  # switches focus to the genotype popup page
        wait.forNewWindow(self.driver, 5)
        matching_text = "Human and Mouse cardiovascular system abnormalities for GATA1/Gata1"
        print(matching_text)
        # asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.title, 'matching mouse/human text not displayed')
        self.driver.close()
        self.driver.switch_to.window(parentwindowid)
        # Grid pop-up for a Phenotype System with only Human annotations
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)

        grid_tab.click()
        phenocells[2].click()  # clicks the first phenotype data cell to open up the craniofacial phenotype popup page
        self.driver.switch_to.window(self.driver.window_handles[1])  # switches focus to the Phenotype popup page
        wait.forNewWindow(self.driver, 5)
        matching_text = "Human craniofacial abnormalities for GATA1/Gata1"
        # asserts the heading text is correct in page source
        print(self.driver.title)
        self.assertIn(matching_text, self.driver.title, 'matching human only text not displayed')
        self.driver.close()
        self.driver.switch_to.window(parentwindowid)

        # Grid popup for a Phenotype System with only Mouse annotations
        grid_tab = self.driver.find_element(By.CSS_SELECTOR,
                                            "ul.nav.nav-tabs > li.uib-tab.nav-item.ng-scope.ng-isolate-scope:nth-child(1) > a.nav-link.ng-binding")
        print(grid_tab.text)

        grid_tab.click()
        phenocells[10].click()  # clicks the phenotype data cell to open up the Phenotype popup page
        self.driver.switch_to.window(self.driver.window_handles[1])  # switches focus to the genotype popup page
        wait.forNewWindow(self.driver, 5)
        matching_text = "Mouse liver/biliary system abnormalities for GATA1/Gata1"
        # asserts the heading text is correct in page source
        self.assertIn(matching_text, self.driver.title, 'matching mouse only text not displayed')

        # Identify the table
        mouse_geno_table = self.driver.find_element(By.CSS_SELECTOR, "p > table.popupTable ")
        data = mouse_geno_table.find_element(By.TAG_NAME, "td")
        print(data.text)
        # find all the TR tags in the table and iterate through them
        cells = mouse_geno_table.find_elements(By.TAG_NAME, "tr")
        print(iterate.getTextAsList(cells))

        # move mouse genotype data
        mousegenotyperows = iterate.getTextAsList(cells)
        # asserts that one of the genoclusters with annotations to this Phenotype System is returned.
        self.assertIn('Gata1tm2Sho/Gata1tm2Sho', mousegenotyperows)
        print("Gata1<tm2Sho> genocluster found in phenotype pop-up")

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHmdcIndex))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
