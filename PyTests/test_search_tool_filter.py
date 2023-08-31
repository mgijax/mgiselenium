'''
Created on Sep 14, 2016
This test is for searches using the quick search feature of the WI
@author: jeffc
Tests the molecular function filter, biological process filter, cellular component filter, phenotype filter,
disease filter, feature type filter
'''

import unittest
import time
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from util import wait, iterate
from util.table import Table
#from config.config import TEST_URL
# adjust the path to find config
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)

import config
#from config import TEST_URL

#Tests
tracemalloc.start()
class TestSearchTool(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        #self.driver.get("http://www.informatics.jax.org")
        #self.driver.get("http://bluebob.informatics.jax.org")
        self.driver.get(config.TEST_URL) 
        #print (config)
       

    def test_molecular_function_filter(self):
        """
        @status: Tests that using a GO ID and the molecular function filter it brings back the proper information
        """
        print ("BEGIN test_molecular_function_filter")
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your EntrezGene(NCBI) ID in the quick search box
        searchbox.send_keys("GO:0071514")
        searchbox.send_keys(Keys.RETURN)
        #waits until the results are displayed on the page and molecular function filter displayed
        if WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.ID, 'functionFilterF'))):
            print('page loaded')
        #find the Molecular Function filter button and click it
        self.driver.find_element(By.ID, 'functionFilterF').click()
        #select the filter option 'carbohydrate derivative binding'
        self.driver.find_elements(By.NAME, 'functionFilterF')[0].click()
        #click the filter button
        self.driver.find_element(By.ID, 'yui-gen0-button').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Symbol column of the table
        all_cells = table.get_column_cells('Symbol')
        print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Gnas') 
        self.assertEqual(all_cells[2].text, 'Ddx4')
        self.assertEqual(all_cells[3].text, 'Mov10l1')
        self.assertEqual(all_cells[4].text, 'Pik3ca')
        self.assertEqual(all_cells[5].text, 'Tdrd9')
        self.assertEqual(all_cells[6].text, 'Tdrd12')

    def test_biological_process_filter(self):
        """
        @status: Tests that using an GO ID and the biological process filter it brings back the proper information
        """
        print ("BEGIN test_biological_process_filter")
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your EntrezGene(NCBI) ID in the quick search box
        searchbox.send_keys("GO:0071514")
        searchbox.send_keys(Keys.RETURN)
        if WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'processFilterF'))):
            print('page loaded')
        #find the Biological Process filter button and click it
        self.driver.find_element(By.ID, 'processFilterF').click()
        #select the filter option 'lipid metabolic process'
        self.driver.find_elements(By.NAME, 'processFilterF')[6].click()
        #click the filter button
        self.driver.find_element(By.ID, 'yui-gen0-button').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Symbol column of the table
        all_cells = table.get_column_cells('Symbol')
        print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Pik3ca')
        self.assertEqual(all_cells[2].text, 'Pld6')

    def test_cellular_component_filter(self):
        """
        @status: Tests that using an GO ID and the cellular component filter it brings back the proper information
        """
        print ("BEGIN test_cellular_component_filter")
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your GO ID in the quick search box
        searchbox.send_keys("GO:0071514")
        searchbox.send_keys(Keys.RETURN)
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'componentFilterF'))):
            print('page loaded')
        #find the cellular component filter button and click it
        self.driver.find_element(By.ID, 'componentFilterF').click()
        #select the filter option 'golgi apparatus'
        self.driver.find_elements(By.NAME, 'componentFilterF')[6].click()
        #click the filter button
        self.driver.find_element(By.ID, 'yui-gen0-button').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Symbol column of the table
        all_cells = table.get_column_cells('Symbol')
        print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Gnas') 
        self.assertEqual(all_cells[2].text, 'Axin1')
        self.assertEqual(all_cells[3].text, 'Pld6')
        self.assertEqual(all_cells[4].text, 'Pcgf5')

    def test_phenotype_filter(self):
        """
        @status: Tests that using an Gene Name and the phenotype filter it brings back the proper information
        """
        print ("BEGIN test_phenotype_filter")
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your EntrezGene(NCBI) ID in the quick search box
        searchbox.send_keys("Gata1")
        searchbox.send_keys(Keys.RETURN)
        #waits until the results are displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'phenotypeFilterF'))):
            print('page loaded')
        #find the phenotype filter button and click it
        self.driver.find_element(By.ID, 'phenotypeFilterF').click()
        #select the filter option 'respiratory system phenotype'
        self.driver.find_elements(By.NAME, 'phenotypeFilterF')[10].click()
        #click the filter button
        self.driver.find_element(By.ID, 'yui-gen0-button').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'b1Table'))):
            print('results loaded')
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Symbol column of the table of Genome Feature tab
        all_cells = table.get_column_cells('Symbol')
        print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Gata1')
        # waits until the Alleles tab is clickable on the page
        #if WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.ID, 'alleleTab'))):
            #print('allele tab ready')
        #Find the allele tab and click it
        self.driver.find_element(By.ID, 'alleleTab').find_element(By.ID, 'aLink').click()
        if WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.ID, 'phenotypeFilterA'))):
            print('phenotype filter button ready')
        # find the phenotype filter button and click it
        self.driver.find_element(By.ID, 'phenotypeFilterA').click()
        # select the filter option 'respiratory system phenotype'
        self.driver.find_elements(By.NAME, 'phenotypeFilterA')[15].click()
        # click the filter button
        self.driver.find_element(By.ID, 'yui-gen0-button').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'b5Table'))):
            print('results loaded')
        results_table = self.driver.find_element(By.ID, 'b5Table')
        table = Table(results_table)
        #Iterate the data to find the Symbol column of the table of Alleles tab
        all_cells = table.get_column_cells('Symbol')
        print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Tg(Gata1-Cbfb)1Tok')
        self.assertEqual(all_cells[2].text, 'Tg(Gata1-Epor)AMym')
        self.assertEqual(all_cells[3].text, 'Gata1tm6Sho')
        self.assertEqual(all_cells[4].text, 'Tg(Rr438-Runx1)#Mym')

    def test_disease_filter(self):
        """
        @status: Tests that using a term and the disease filter it brings back the proper information
        """
        print ("BEGIN test_disease_filter")
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your disease name in the quick search box
        searchbox.send_keys("blood island")
        searchbox.send_keys(Keys.RETURN)
        # waits until the disease filter is displayed on the page
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'diseaseFilterF'))):
            print('page loaded')
        #find the disease filter button and click it
        self.driver.find_element(By.ID, 'diseaseFilterF').click()
        #select the option thoracic disease
        self.driver.find_elements(By.NAME, 'diseaseFilterF')[23].click()
        #click the filter button
        self.driver.find_element(By.ID, 'yui-gen0-button').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'b1Table'))):
            print('genome results loaded')
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Symbol column of the table of Genome Feature tab
        all_cells = table.get_column_cells('Symbol')
        #print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Kdr')
        self.assertEqual(all_cells[2].text, 'Runx3')
        # Find the allele tab and click it
        self.driver.find_element(By.ID, 'alleleTab').find_element(By.ID, 'aLink').click()
        if WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.ID, 'diseaseFilterA'))):
            print('disease filter button ready')
        # find the disease filter button and click it
        self.driver.find_element(By.ID, 'diseaseFilterA').click()
        # select the filter option 'cardiovascular system disease'
        self.driver.find_elements(By.NAME, 'diseaseFilterA')[1].click()
        # click the filter button
        self.driver.find_element(By.ID, 'yui-gen0-button').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'b5Table'))):
            print('allele results loaded')
        results_table = self.driver.find_element(By.ID, 'b5Table')
        table = Table(results_table)
        #Iterate the data to find the Symbol column of the table of Alleles tab
        all_cells = table.get_column_cells('Symbol')
        print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Engtm1Mle')
        self.assertEqual(all_cells[2].text, 'Bmp4tm1Blh')

    def test_feature_type_filter(self):
        """
        @status: Tests that using a term and the feature type filter it brings back the proper information
        """
        print ("BEGIN test_feature_type_filter")
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your EntrezGene(NCBI) ID in the quick search box
        searchbox.send_keys("Gata1")
        searchbox.send_keys(Keys.RETURN)
        # waits until the Feature Type filter is displayed on the page
        if WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'featureTypeFilterF'))):
            print('page loaded')
        # find the feature type filter button and click it
        self.driver.find_element(By.ID, 'featureTypeFilterF').click()
        # select the option non coding RNA gene
        self.driver.find_elements(By.NAME, 'featureTypeFilterF')[1].click()
        # click the filter button
        self.driver.find_element(By.ID, 'yui-gen0-button').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Symbol column of the table of Genome Feature tab
        all_cells = table.get_column_cells('Type')
        print(all_cells[1].text)
        #asserts that the feature Type data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'unclassified non-coding RNA gene')
        # Find the allele tab and click it
        self.driver.find_element(By.ID, 'alleleTab').find_element(By.ID, 'aLink').click()
        if WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.ID, 'featureTypeFilterA'))):
            print('feature type filter button ready')
        # find the Feature Type filter button and click it
        self.driver.find_element(By.ID, 'featureTypeFilterA').click()
        # select the filter option 'protein coding gene'
        self.driver.find_elements(By.NAME, 'featureTypeFilterA')[1].click()
        # click the filter button
        self.driver.find_element(By.ID, 'yui-gen0-button').click()
        # waits until the results are displayed on the page
        if WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'b5Table'))):
            print('allele results loaded')
        results_table = self.driver.find_element(By.ID, 'b5Table')
        table = Table(results_table)
        #Iterate the data to find the Symbol column of the table of Alleles tab
        all_cells = table.get_column_cells('Symbol')
        print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Gata1tm1.1Itl')
        self.assertEqual(all_cells[2].text, 'Gata1tm1.1Schro')
        self.assertEqual(all_cells[13].text, 'Gata1Plt13')

           
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSearchTool))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))