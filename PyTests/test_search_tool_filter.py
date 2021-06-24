'''
Created on Sep 14, 2016
This test is for searches using the quick search feature of the WI
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        time.sleep(2)
        #find the Molecular Function filter button and click it
        self.driver.find_element_by_id('functionFilter').click()
        time.sleep(2)
        #select the filter option 'carbohydrate derivative binding'
        self.driver.find_elements_by_name('functionFilter')[3].click()
        #click the filter button
        self.driver.find_element_by_id('yui-gen0-button').click()
        time.sleep(10)
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Symbol column of the table
        all_cells = table.get_column_cells('Symbol')
        #print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Gnas') 
        self.assertEqual(all_cells[2].text, 'Gsk3a') 
        self.assertEqual(all_cells[3].text, 'Gsk3b') 
        self.assertEqual(all_cells[4].text, 'Pik3ca') 

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        time.sleep(2)
        #find the Biological Process filter button and click it
        self.driver.find_element_by_id('processFilter').click()
        time.sleep(4)
        #select the filter option 'lipid metabolic process'
        self.driver.find_elements_by_name('processFilter')[8].click()
        #click the filter button
        self.driver.find_element_by_id('yui-gen0-button').click()
        time.sleep(10)
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Symbol column of the table
        all_cells = table.get_column_cells('Symbol')
        #print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Brca1') 
        self.assertEqual(all_cells[2].text, 'Mecp2')
        self.assertEqual(all_cells[3].text, 'Pik3ca')

    def test_cellular_component_filter(self):
        """
        @status: Tests that using an GO ID and the cellular component filter it brings back the proper information
        """
        print ("BEGIN test_cellular_component_filter")
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your EntrezGene(NCBI) ID in the quick search box
        searchbox.send_keys("GO:0071514")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        time.sleep(2)
        #find the cellular component filter button and click it
        self.driver.find_element_by_id('componentFilter').click()
        time.sleep(4)
        #select the filter option 'golgi apparatus'
        self.driver.find_elements_by_name('componentFilter')[0].click()
        #click the filter button
        self.driver.find_element_by_id('yui-gen0-button').click()
        time.sleep(10)
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Symbol column of the table
        all_cells = table.get_column_cells('Symbol')
        #print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Gnas') 
        self.assertEqual(all_cells[2].text, 'Pcgf5')

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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        time.sleep(2)
        #find the phenotype filter button and click it
        self.driver.find_element_by_id('phenotypeFilter').click()
        time.sleep(2)
        #select the filter option 'respiratory system phenotype'
        self.driver.find_elements_by_name('phenotypeFilter')[23].click()
        #click the filter button
        self.driver.find_element_by_id('yui-gen0-button').click()
        time.sleep(2)
        self.driver.find_element_by_id('ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Symbol column of the table of Genome Feature tab
        all_cells = table.get_column_cells('Symbol')
        #print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Gata1') 
        #Find the allele tab and click it
        self.driver.find_element_by_id('ui-id-2').click()
        time.sleep(5)
        results_table = self.driver.find_element(By.ID, 'b5Table')
        table = Table(results_table)
        #Iterate the data to find the Symbol column of the table of Alleles tab
        all_cells = table.get_column_cells('Symbol')
        print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Gata1tm6Sho')
        self.assertEqual(all_cells[2].text, 'Tg(Gata1-Cbfb)1Tok')
        self.assertEqual(all_cells[3].text, 'Tg(Gata1-Epor)AMym') 
        #Find the Other Results by ID tab and click it
        self.driver.find_element_by_id('ui-id-5').click()
        time.sleep(5)
        results_table = self.driver.find_element(By.ID, 'b3Table')
        table = Table(results_table)
        #Iterate the data to find the Type column of the table of Other results by ID tab
        all_cells = table.get_column_cells('Type')
        #print(all_cells[1].text)
        #asserts that the type data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Homolog')

    def test_disease_filter(self):
        """
        @status: Tests that using a term and the disease filter it brings back the proper information
        """
        print ("BEGIN test_disease_filter")
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your EntrezGene(NCBI) ID in the quick search box
        searchbox.send_keys("blood island")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the phenotype filter button and click it
        self.driver.find_element_by_id('diseaseFilter').click()
        time.sleep(2)
        #select the filter option 'thoracic disease'
        self.driver.find_elements_by_name('diseaseFilter')[34].click()
        #click the filter button
        self.driver.find_element_by_id('yui-gen0-button').click()
        time.sleep(4)
        self.driver.find_element_by_id('ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Symbol column of the table of Genome Feature tab
        all_cells = table.get_column_cells('Symbol')
        #print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Runx3') 
        #Find the allele tab and click it
        self.driver.find_element_by_id('ui-id-2').click()
        time.sleep(5)
        results_table = self.driver.find_element(By.ID, 'b5Table')
        table = Table(results_table)
        #Iterate the data to find the Symbol column of the table of Alleles tab
        all_cells = table.get_column_cells('Symbol')
        print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Ptentm1Hwu')
        self.assertEqual(all_cells[2].text, 'Trp53tm1Tyj')
        self.assertEqual(all_cells[3].text, 'Cav1tm1Mls') 
        #Find the Other Results by ID tab and click it
        self.driver.find_element_by_id('ui-id-3').click()
        time.sleep(5)
        results_table = self.driver.find_element(By.ID, 'b2Table')
        table = Table(results_table)
        #Iterate the data to find the Type column of the table of Other results by ID tab
        all_cells = table.get_column_cells('Term')
        #print(all_cells[1].text)
        #asserts that the type data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Disease: breast angiosarcoma')

    def test_feature_type_filter(self):
        """
        @status: Tests that using a term and the feature type filter it brings back the proper information
        """
        print ("BEGIN test_feature_type_filter")
        driver = self.driver
        driver.get(config.TEST_URL)
        searchbox = driver.find_element(By.ID, 'searchToolTextArea')
        # put your EntrezGene(NCBI) ID in the quick search box
        searchbox.send_keys("blood island")
        searchbox.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-id-1')))#waits until the results are displayed on the page
        #find the feature type filter button and click it
        self.driver.find_element_by_id('featureTypeFilter').click()
        time.sleep(2)
        #select the filter option 'pseudogene'
        self.driver.find_elements_by_name('featureTypeFilter')[22].click()
        #click the filter button
        self.driver.find_element_by_id('yui-gen0-button').click()
        time.sleep(4)
        self.driver.find_element_by_id('ui-id-1').click()
        results_table = self.driver.find_element(By.ID, 'b1Table')
        table = Table(results_table)
        #Iterate the first row of data to find the Symbol column of the table of Genome Feature tab
        all_cells = table.get_column_cells('Type')
        #print(all_cells[1].text)
        #asserts that the Type data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'pseudogene') 
        self.assertEqual(all_cells[2].text, 'pseudogene')
        self.assertEqual(all_cells[3].text, 'pseudogene')
        self.assertEqual(all_cells[4].text, 'pseudogene')
        #Find the allele tab and click it
        self.driver.find_element_by_id('ui-id-2').click()
        time.sleep(5)
        results_table = self.driver.find_element(By.ID, 'b5Table')
        table = Table(results_table)
        #Iterate the data to find the Symbol column of the table of Alleles tab
        all_cells = table.get_column_cells('Symbol')
        print(all_cells[1].text)
        #asserts that the Symbol data is correct for the filter used
        self.assertEqual(all_cells[1].text, 'Speer6-ps1Tg(Alb-cre)21Mgn')
        self.assertEqual(all_cells[2].text, '2610005L07RikGt(ROSA)73Sor')

           
    def tearDown(self):
        self.driver.quit()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSearchTool))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))