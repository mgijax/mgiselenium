'''
Created on Feb 2, 2018
These tests check the finctionality of the the GXD Differental query form
@author: jeffc
'''
import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys,os.path
from selenium.webdriver.common.action_chains import ActionChains
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import iterate, wait
import config

class TestGxdDifferentialQF(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()

    def test_diff_wt_results(self):
        """
        @status: Tests that wild type results(broad definition) are excluded in results.(assays which are not associated with any allele pairs,
        or In Situ reporter(knock-in) assays associated with a single allele pair which is heterozygous wild type for the assayed gene)
        @note: GXD-Diff-2
        @attention: the time sleeps need to be replaced by expected conditions code
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/differential')
        #self.driver.find_element(By.ID, 'difStructure3').clear()
        pickitem = self.driver.find_element(By.ID, 'difStructure3').send_keys('bladder')
        actions = ActionChains(driver)
        actions.move_to_element(pickitem)
        actions.click(pickitem)
        time.sleep(2)
        #self.driver.find_element(By.ID, 'difStructure4').clear()
        pickitem2 = self.driver.find_element(By.ID, 'difStructure4').send_keys('adventitia of bladder')
        actions = ActionChains(driver)
        actions.move_to_element(pickitem2)
        actions.click(pickitem2)
        time.sleep(5)
        self.driver.find_element(By.ID, 'submit4').click()
        time.sleep(40)
        self.driver.find_element(By.ID, 'genegridtab')
        #find the Genes column
        self.driver.find_element(By.ID, 'colGroup')
        genelist = driver.find_element(By.ID, 'colGroupInner')
        items = genelist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        #print searchTextItems
        #self.assertIn('Adgrb2', searchTextItems)
        self.assertIn('Agtr2', searchTextItems)
        self.assertIn('Cldn2', searchTextItems)
        #find the tissue grid box for bladder for marker Agtr2
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col88 > rect.blue1')
        rightclass = item.get_attribute('class')
        #rightclass finds the class name of the gridbox
        #now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue1')
        #find the Anatomical Systems column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        #print searchTextItems
        #Now assert that these 2 systems are returned in the first column of the grid
        self.assertIn('bladder', searchTextItems)
        self.assertIn('adventitia of bladder', searchTextItems)

    def test_diff_systems(self):
        """
        @status: Tests that query for detected in "A", Not detected in "B", where "A" and "B" are in different anatomical systems
        @note: GXD-Diff-3(partial test)
        @attention: the time sleeps need to be replaced by expected conditions code
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/differential')
        #self.driver.find_element(By.ID, 'difStructure3').clear()
        pickitem = self.driver.find_element(By.ID, 'difStructure3').send_keys('pulmonary valve')
        actions = ActionChains(driver)
        actions.move_to_element(pickitem)
        actions.click(pickitem)
        time.sleep(2)
        #self.driver.find_element(By.ID, 'difStructure4').clear()
        pickitem2 = self.driver.find_element(By.ID, 'difStructure4').send_keys('aortic valve')
        actions = ActionChains(driver)
        actions.move_to_element(pickitem2)
        actions.click(pickitem2)
        time.sleep(5)
        self.driver.find_element(By.ID, 'submit4').click()
        time.sleep(10)
        self.driver.find_element(By.ID, 'genegridtab')
        #find the Genes column
        self.driver.find_element(By.ID, 'colGroup')
        genelist = driver.find_element(By.ID, 'colGroupInner')
        items = genelist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        #print searchTextItems
        self.assertIn('Bmp2', searchTextItems)
        self.assertIn('Casp3', searchTextItems)
        self.assertIn('Col11a1', searchTextItems)
        self.assertIn('Crip2', searchTextItems)
        self.assertIn('Evc', searchTextItems)
        self.assertIn('Evc2', searchTextItems)
        self.assertIn('Foxc2', searchTextItems)
        self.assertIn('Hand1', searchTextItems)
        self.assertIn('Hapln1', searchTextItems)
        self.assertIn('Itga6', searchTextItems)
        self.assertIn('Mki67', searchTextItems)
        self.assertIn('Notch2', searchTextItems)
        self.assertIn('Vcan', searchTextItems)
        #find the tissue grid box for bladder for marker Agtr2
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col12 > rect.blue1')
        rightclass = item.get_attribute('class')
        #rightclass finds the class name of the gridbox
        #now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue1')
        #find the Anatomical Systems column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        #print searchTextItems
        #Now assert that only this system is returned in the grid
        self.assertIn('pulmonary valve', searchTextItems)

    def test_diff_parent(self):
        """
        @status: Tests that query for detected in "A", Not detected in "B", where "A" is a parent of "B" in the same anatomical system
        @note: GXD-Diff-4(partial test)
        @attention: the time sleeps need to be replaced by expected conditions code
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/differential')
        #self.driver.find_element(By.ID, 'difStructure3').clear()
        pickitem = self.driver.find_element(By.ID, 'difStructure3').send_keys('pulmonary valve')
        actions = ActionChains(driver)
        actions.move_to_element(pickitem)
        actions.click(pickitem)
        time.sleep(2)
        #self.driver.find_element(By.ID, 'difStructure4').clear()
        pickitem2 = self.driver.find_element(By.ID, 'difStructure4').send_keys('pulmonary valve leaflet')
        actions = ActionChains(driver)
        actions.move_to_element(pickitem2)
        actions.click(pickitem2)
        time.sleep(5)
        self.driver.find_element(By.ID, 'submit4').click()
        time.sleep(10)
        self.driver.find_element(By.ID, 'genegridtab')
        #find the Genes column
        self.driver.find_element(By.ID, 'colGroup')
        genelist = driver.find_element(By.ID, 'colGroupInner')
        items = genelist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        #print searchTextItems
        #self.assertIn('Adgrb2', searchTextItems)
        self.assertIn('Acta2', searchTextItems)
        self.assertIn('Casp3', searchTextItems)
        self.assertIn('Col11a1', searchTextItems)
        self.assertIn('Crip2', searchTextItems)
        self.assertIn('Evc', searchTextItems)
        self.assertIn('Evc2', searchTextItems)
        self.assertIn('Foxc2', searchTextItems)
        self.assertIn('Gnb4', searchTextItems)
        self.assertIn('Hand1', searchTextItems)
        self.assertIn('Itga6', searchTextItems)
        self.assertIn('Itgb1', searchTextItems)
        self.assertIn('Mki67', searchTextItems)
        self.assertIn('Mxra8', searchTextItems)
        self.assertIn('Npas3', searchTextItems)
        self.assertIn('Postn', searchTextItems)
        self.assertIn('Tnmd', searchTextItems)
        
        #find the tissue grid box for bladder for marker Agtr2
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col12 > rect.blue1')
        rightclass = item.get_attribute('class')
        #rightclass finds the class name of the gridbox
        #now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue1')
        #find the Anatomical Systems column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        #print searchTextItems
        #Now assert that only this system is returned in the grid
        self.assertIn('pulmonary valve', searchTextItems)
        
    def test_diff_exp_notexp(self):
        """
        @status: Tests that query for detected in "A", Not detected in "B", where a gene has both "expressed" and "not expressed" results for "A"
        and has no results and/or "not expressed" results for "B" should return the gene.
        @note: GXD-Diff-6
        @attention: the time sleeps need to be replaced by expected conditions code. This test has a long sleep because something is slow!
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/gxd/differential')
        #self.driver.find_element(By.ID, 'difStructure3').clear()
        pickitem = self.driver.find_element(By.ID, 'difStructure3').send_keys('liver')
        actions = ActionChains(driver)
        actions.move_to_element(pickitem)
        actions.click(pickitem)
        time.sleep(2)
        #self.driver.find_element(By.ID, 'difStructure4').clear()
        pickitem2 = self.driver.find_element(By.ID, 'difStructure4').send_keys('spleen')
        actions = ActionChains(driver)
        actions.move_to_element(pickitem2)
        actions.click(pickitem2)
        time.sleep(2)
        self.driver.find_element(By.ID, 'submit4').click()
        time.sleep(28)
        self.driver.find_element(By.ID, 'genegridtab')
        #find the Genes column
        self.driver.find_element(By.ID, 'colGroup')
        genelist = driver.find_element(By.ID, 'colGroupInner')
        items = genelist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        #print searchTextItems
        self.assertIn('A2m', searchTextItems)
        self.assertIn('Aard', searchTextItems)
        self.assertIn('Abca3', searchTextItems)
        #self.assertIn('Bckdk', searchTextItems)
        #self.assertIn('Pkm', searchTextItems)
        #find the tissue grid box for liver for marker A2m
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col19 > rect')
        rightclass = item.get_attribute('class')
        #rightclass finds the class name of the gridbox
        #now we assert the class name of the gridbox matches the class name of blue1
        self.assertEqual(rightclass, 'blue1')
        #find the Anatomical Systems column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        #print searchTextItems
        #Now assert that both systems are returned in the grid
        self.assertIn('liver', searchTextItems) 
        self.assertIn('spleen', searchTextItems)               
                
    def tearDown(self):
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxdDifferentialQF))
    return suite
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
    