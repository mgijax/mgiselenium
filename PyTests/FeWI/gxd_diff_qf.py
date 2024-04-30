"""
Created on Feb 2, 2018
These tests check the functionality of the the GXD Differental query form
these tests need  to be worked on!!! none of them work right now5/20/2021
@author: jeffc
Verify that wild type results(broad definition) are excluded in results
Verify query for detected in "A", Not detected in "B", where "A" and "B" are in different anatomical systems
Verify query for detected in "A", Not detected in "B", where "A" is a parent of "B" in the same anatomical system
Verify query for detected in "A", Not detected in "B", where a gene has both "expressed" and "not expressed" results
       for "A" and has no results and/or "not expressed" results for "B" should return the gene
"""
import os.path
import sys
import time
import tracemalloc
import unittest
import config

from util import iterate
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../..', )
)

# Tests
tracemalloc.start()


class TestGxdDifferentialQF(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)

    def test_diff_wt_results(self):
        """
        @status: Tests that wild type results(broad definition) are excluded in results.(assays which are not associated with any allele pairs,
        or In Situ reporter(knock-in) assays associated with a single allele pair which is heterozygous wild type for the assayed gene)
        @note: GXD-Diff-2 !!this test is no longer working
        @attention: this test is taking so long to return results it fails, might work again  when switched to lucene indexing OR find an example with less results!!!.
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/differential')
        # self.driver.find_element(By.ID, 'difStructure3').clear()
        pickitem = self.driver.find_element(By.ID, 'difStructure3')
        pickitem.send_keys('bla')
        time.sleep(2)
        pickitem.send_keys(Keys.TAB)
        actions = ActionChains(self.driver)
        actions.move_to_element(pickitem)
        actions.perform()
        time.sleep(2)
        # self.driver.find_element(By.ID, 'difStructure4').clear()
        pickitem2 = self.driver.find_element(By.ID, 'difStructure4')
        pickitem2.send_keys('adv')
        time.sleep(2)
        pickitem2.send_keys(Keys.TAB)
        actions = ActionChains(driver)
        actions.move_to_element(pickitem2)
        actions.perform()
        time.sleep(3)
        self.driver.find_element(By.ID, 'submit4').click()
        # time.sleep(40)
        # if WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, 'genegriddata'))):
        # print('page loaded')
        # wait.forAngular(driver, 85)
        time.sleep(25)
        self.driver.find_element(By.ID, 'genegridtab')
        # find the Genes column
        self.driver.find_element(By.ID, 'colGroup')
        genelist = driver.find_element(By.ID, 'colGroupInner')
        items = genelist.find_elements(By.TAG_NAME, "text")
        searchtextitems = iterate.getTextAsList(items)
        # print(searchtextitems)
        self.assertIn('Adgrb2', searchtextitems)
        self.assertIn('Agtr2', searchtextitems)
        # self.assertIn('Cldn2', searchtextitems)
        # find the tissue grid box for bladder for marker Agtr2
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col107 > rect.blue1')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue1')
        # find the Anatomical Systems column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        # Now assert that these 2 systems are returned in the first column of the grid
        self.assertIn('bladder', searchtextitems)
        self.assertIn('adventitia of bladder', searchtextitems)

    def test_diff_systems(self):
        """
        @status: Tests that query for detected in "A", Not detected in "B", where "A" and "B" are in different anatomical systems
        @note: GXD-Diff-3(partial test) !!this test  no longer works because of move to issue!
        @attention: the time sleeps need to be replaced by expected conditions code!!needs to be fixed broken!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/differential')
        self.driver.find_element(By.ID, 'difStructure3').clear()
        anatstructure = driver.find_element(By.ID, 'difStructure3')
        # Enter your anatomical structure in the box
        anatstructure.send_keys("pul")
        time.sleep(1)
        # select the option pulmonary valve TS21-28
        driver.find_element(By.CSS_SELECTOR,
                            '#difStructureContainer3 > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(5)').click()
        anatstructure.send_keys(Keys.TAB)
        anatstructure2 = driver.find_element(By.ID, 'difStructure4')
        # Enter your anatomical structure in the box
        anatstructure2.send_keys("aorti")
        time.sleep(1)
        # select the option aortic valve TS21-28
        driver.find_element(By.CSS_SELECTOR,
                            '#difStructureContainer4 > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(3)').click()
        anatstructure2.send_keys(Keys.TAB)
        time.sleep(1)
        self.driver.find_element(By.ID, 'submit4').click()
        if WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'g.cell:nth-child(12) > rect:nth-child(1)'))):
            print('Tissue x Gene matrix data loaded')
        self.driver.find_element(By.ID, 'genegridtab')
        # find the Genes column
        self.driver.find_element(By.ID, 'colGroup')
        genelist = driver.find_element(By.ID, 'colGroupInner')
        items = genelist.find_elements(By.TAG_NAME, "text")
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        self.assertIn('Bmp2', searchtextitems)
        self.assertIn('Col11a1', searchtextitems)
        self.assertIn('Crip2', searchtextitems)
        self.assertIn('Evc', searchtextitems)
        self.assertIn('Evc2', searchtextitems)
        self.assertIn('Foxc2', searchtextitems)
        self.assertIn('Hand1', searchtextitems)
        self.assertIn('Hapln1', searchtextitems)
        self.assertIn('Itga6', searchtextitems)
        self.assertIn('Matr3', searchtextitems)
        self.assertIn('Mki67', searchtextitems)
        self.assertIn('Notch2', searchtextitems)
        # find the tissue grid box for bladder for marker Matr3
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col9 > rect.blue1')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue1')
        # find the Anatomical Systems column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        # Now assert that only this system is returned in the grid
        self.assertIn('pulmonary valve', searchtextitems)

    def test_same_parent(self):
        """
        @status: Tests that query for detected in "A", Not detected in "B", where "A" is a parent of "B" in the same anatomical system
        @note: GXD-Diff-4(partial test)
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/differential')
        anat = driver.find_element(By.ID, 'difStructure3')
        # Enter your anatomical structure in the box
        anat1.send_keys("pul")
        time.sleep(1)
        # select the fifth option Pulmonary valve TS21-28
        anat1 = self.driver.find_element(By.CSS_SELECTOR,
                                         '#difStructureContainer3 > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(5)').click()
        anat1.send_keys(Keys.TAB)
        print(anat1)
        anat2 = driver.find_element(By.ID, 'difStructure4')
        # Enter your anatomical structure in the box
        anat2.send_keys("pulmo")
        time.sleep(1)
        # select the seventh option Pulmonary valve leaflet TS23-26
        anatstructure2 = driver.find_element(By.CSS_SELECTOR,
                                             '#difStructureContainer4 > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(7)').click()
        anat2.send_keys(Keys.TAB)
        print(anatstructure2)
        time.sleep(1)
        self.driver.find_element(By.ID, 'submit4').click()
        if WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'g.cell:nth-child(30) > rect:nth-child(1)'))):
            print('Tissue x Gene matrix data loaded')
        self.driver.find_element(By.ID, 'genegridtab')
        # find the Genes column
        self.driver.find_element(By.ID, 'colGroup')
        genelist = driver.find_element(By.ID, 'colGroupInner')
        items = genelist.find_elements(By.TAG_NAME, "text")
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        # self.assertIn('Adgrb2', searchTextItems)
        self.assertIn('Acta2', searchtextitems)
        self.assertIn('Casp3', searchtextitems)
        self.assertIn('Col11a1', searchtextitems)
        self.assertIn('Crip2', searchtextitems)
        self.assertIn('Evc', searchtextitems)
        self.assertIn('Evc2', searchtextitems)
        self.assertIn('Foxc2', searchtextitems)
        self.assertIn('Gnb4', searchtextitems)
        self.assertIn('Hand1', searchtextitems)
        self.assertIn('Itga6', searchtextitems)
        self.assertIn('Itgb1', searchtextitems)
        self.assertIn('Mki67', searchtextitems)
        self.assertIn('Mxra8', searchtextitems)
        self.assertIn('Npas3', searchtextitems)
        self.assertIn('Postn', searchtextitems)
        self.assertIn('Tnmd', searchtextitems)

        # find the tissue grid box for bladder for marker Agtr2
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col12 > rect.blue1')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue1')
        # find the Anatomical Systems column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        # Now assert that only this system is returned in the grid
        self.assertIn('pulmonary valve', searchtextitems)

    def test_diff_exp_notexp(self):
        """
        @status: Tests that query for detected in "A", Not detected in "B", where a gene has both "expressed" and "not expressed" results for "A"
        and has no results and/or "not expressed" results for "B" should return the gene.
        @note: GXD-Diff-6
        @attention:  This test needs to be fixed once we go to lucene indexing OR find an example with less results!!
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/differential')
        anatstructure = driver.find_element(By.ID, 'difStructure3')
        # Enter your anatomical structure in the box
        anatstructure.send_keys("liv")
        time.sleep(2)
        selectstructure = driver.find_element(By.CSS_SELECTOR,
                                              '#difStructureContainer3 > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1)').click()
        print(selectstructure)
        time.sleep(2)
        anatstructure2 = driver.find_element(By.ID, 'difStructure4')
        # Enter your anatomical structure in the box
        anatstructure2.send_keys("spl")
        time.sleep(2)
        selectstructure2 = driver.find_element(By.CSS_SELECTOR,
                                               '#difStructureContainer4 > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(3)').click()
        print(selectstructure2)
        time.sleep(2)
        self.driver.find_element(By.ID, 'submit4').click()
        if WebDriverWait(self.driver, 16).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'g.cell:nth-child(2953) > rect:nth-child(1)'))):
            print('Tissue x Gene matrix data loaded')
        self.driver.find_element(By.ID, 'genegridtab')
        time.sleep(5)
        # find the Genes column
        self.driver.find_element(By.ID, 'colGroup')
        genelist = driver.find_element(By.ID, 'colGroupInner')
        items = genelist.find_elements(By.TAG_NAME, "text")
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        self.assertIn('A2m', searchtextitems)
        self.assertIn('Aard', searchtextitems)
        self.assertIn('Abca1', searchtextitems)
        # self.assertIn('Bckdk', searchTextItems)
        # self.assertIn('Pkm', searchTextItems)
        # find the tissue grid box for liver for marker A2m
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col19 > rect')
        rightclass = item.get_attribute('class')
        # rightclass finds the class name of the gridbox
        # now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue1')
        # find the Anatomical Systems column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchtextitems = iterate.getTextAsList(items)
        # print searchTextItems
        # Now assert that both systems are returned in the grid
        self.assertIn('liver', searchtextitems)
        self.assertIn('spleen', searchtextitems)

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxdDifferentialQF))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
