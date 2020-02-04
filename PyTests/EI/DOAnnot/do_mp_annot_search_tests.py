'''
Created on Nov 26, 2019
Tests the searching of the DO Phenotypes (mpannot) module
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import HTMLTestRunner
import json
import sys,os.path
from test.test_base64 import BaseXYTestCase
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests

class TestDoMpannotSearch(unittest.TestCase):
    """
    @status Test DO Allele Annotations searching, etc
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/doalleleannot")
    
    def tearDown(self):
        self.driver.close()

    def testDoMpMgiIdSearch(self):
        """
        @Status tests that a basic DO MGI ID genotype search works
        @see pwi-domp-search-1 
        """
        driver = self.driver
        #finds the MGI ID field and enters an MGI allele ID, tabs out of the field then clicks the Search button
        driver.find_element_by_id("alleleAccId").send_keys('MGI:1857438')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the Allele field and verify it's text
        alle = driver.find_element_by_id('alleleDisplay').get_property('value')
        print alle
        self.assertEqual(alle, 'Hexb<tm1Rlp>, targeted mutation 1, Richard L Proia')
        an_table = self.driver.find_element_by_id('annotTable')
        table = Table(an_table)
        #Iterate and print the table results
        header_cells = table.get_header_cells()
        headings = iterate.getTextAsList(header_cells)
        print headings
        #assert the headers are correct
        self.assertEqual(headings, ['', 'DO Term', 'Vocabulary Term', 'Qualifier', 'J#', 'Citation', 'Modified', 'Date', 'Created', 'Date'])
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'termID-1')))
        #find the search results table first row of data
        term0 = driver.find_element_by_id('termID-0').get_property('value')
        print term0
        voc_term = driver.find_element_by_class_name('term')
        print voc_term.text
        qualfy = driver.find_element_by_id('qualifierAbbreviation-0').get_property('value')
        #value should be 'string:8068249' that equals Therapy
        print qualfy
        j_num = driver.find_element_by_id('jnumID-0').get_property('value')
        print j_num
        cite = driver.find_element_by_class_name('short_citation')
        print cite.text
        mod_by = driver.find_element_by_id('modifiedBy-0').get_property('value')
        print mod_by
        mod_date = driver.find_element_by_id('modifiedDate-0').get_property('value')
        print mod_date
        create_by = driver.find_element_by_id('createdBy-0').get_property('value')
        print create_by
        create_date = driver.find_element_by_id('createdDate-0').get_property('value')
        print create_date
        #we are asserting the first row of data is correct
        self.assertEqual(term0, 'DOID:3323')
        self.assertEqual(voc_term.text, 'Sandhoff disease')
        self.assertEqual(qualfy, 'string:8068249')
        self.assertEqual(j_num, 'J:184450')
        self.assertEqual(cite.text, 'Keilani S, J Neurosci 2012 Apr 11;32(15):5223-36')
        self.assertEqual(mod_by, 'mnk')
        self.assertEqual(mod_date, '2012-07-27')
        self.assertEqual(create_by, 'mnk')
        self.assertEqual(create_date, '2012-07-27')

    def testDoMpAlleleSearch(self):
        """
        @Status tests that a basic Allele search works
        @see pwi-domp-search-2
        """
        driver = self.driver
        #finds the Allele field and enters an allele(can also use wildcard of %, tabs out of the field then clicks the Search button
        driver.find_element_by_id("alleleDisplay").send_keys('Kmt2a<tm1Clgr>%')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        driver.find_element_by_id('searchButton').click()
        #waits until the element is located or 10 seconds
        #WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, 'termID-1')))
        time.sleep(5)
        #find the search results table first row of data
        term0 = driver.find_element_by_id('termID-0').get_property('value')
        print term0
        voc_term = driver.find_element_by_class_name('term')
        print voc_term.text
        qualfy = driver.find_element_by_id('qualifierAbbreviation-0').get_property('value')#value should be 'string:8068250' that equals (none)
        print qualfy
        j_num = driver.find_element_by_id('jnumID-0').get_property('value')
        print j_num
        cite = driver.find_element_by_class_name('short_citation')
        print cite.text
        mod_by = driver.find_element_by_id('modifiedBy-0').get_property('value')
        print mod_by
        mod_date = driver.find_element_by_id('modifiedDate-0').get_property('value')
        print mod_date
        create_by = driver.find_element_by_id('createdBy-0').get_property('value')
        print create_by
        create_date = driver.find_element_by_id('createdDate-0').get_property('value')
        print create_date
        #we are asserting the first row of data is correct
        self.assertEqual(term0, 'DOID:9119')
        self.assertEqual(voc_term.text, 'acute myeloid leukemia')
        self.assertEqual(qualfy, 'string:8068250')
        self.assertEqual(j_num, 'J:203559')
        self.assertEqual(cite.text, 'Bernot KM, Leukemia 2013 Dec;27(12):2379-82')
        self.assertEqual(mod_by, 'mnk')
        self.assertEqual(mod_date, '2014-01-13')
        self.assertEqual(create_by, 'mnk')
        self.assertEqual(create_date, '2014-01-13')
        
    def testDoMpTermIdSearch(self):
        """
        @Status tests that a basic DO Term ID search works
        @see pwi-domp-search-3, 4
        """
        driver = self.driver
        #finds the DO Term field and enters an DOID then clicks the Search button
        driver.find_element_by_id("termID-0").send_keys('DOID:3323')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element_by_id('searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'termID-3')))
        #find the search results table first row of data
        term0 = driver.find_element_by_id('termID-0').get_property('value')
        print term0
        voc_term = driver.find_element_by_class_name('term')
        print voc_term.text
        qualfy = driver.find_element_by_id('qualifierAbbreviation-0').get_property('value')#value should be 'string:8068250' that equals (none)
        print qualfy
        j_num = driver.find_element_by_id('jnumID-0').get_property('value')
        print j_num
        cite = driver.find_element_by_class_name('short_citation')
        print cite.text
        mod_by = driver.find_element_by_id('modifiedBy-0').get_property('value')
        print mod_by
        mod_date = driver.find_element_by_id('modifiedDate-0').get_property('value')
        print mod_date
        create_by = driver.find_element_by_id('createdBy-0').get_property('value')
        print create_by
        create_date = driver.find_element_by_id('createdDate-0').get_property('value')
        print create_date
        #we are asserting the first row of data is correct
        self.assertEqual(term0, 'DOID:3323')
        self.assertEqual(voc_term.text, 'Sandhoff disease')
        self.assertEqual(qualfy, 'string:8068250')
        self.assertEqual(j_num, 'J:237590')
        self.assertEqual(cite.text, 'Richardson K, Behav Brain Res 2016 Jan 15;297():213-23')
        self.assertEqual(mod_by, 'monikat')
        self.assertEqual(mod_date, '2018-07-17')
        self.assertEqual(create_by, 'monikat')
        self.assertEqual(create_date, '2018-07-17')


    def testDoMpQualSearch(self):
        """
        @Status tests that a basic DOMP Qualifier search works
        @see pwi-domp-search-7
        """
        driver = self.driver
        #finds the Qualifier field and select 'therapy' then clicks the Search button
        driver.find_element_by_id("qualifierAbbreviation-0").send_keys('therapy')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element_by_id('searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'termID-3')))
        #find the search results table fifth row of data
        term0 = driver.find_element_by_id('termID-4').get_property('value')
        print term0
        voc_term = driver.find_elements_by_class_name('term')[4]
        print voc_term.text
        qualfy = driver.find_element_by_id('qualifierAbbreviation-4').get_property('value')#value should be 'string:8068249' that equals therapy
        print qualfy
        j_num = driver.find_element_by_id('jnumID-4').get_property('value')
        print j_num
        cite = driver.find_elements_by_class_name('short_citation')[4]
        print cite.text
        mod_by = driver.find_element_by_id('modifiedBy-4').get_property('value')
        print mod_by
        mod_date = driver.find_element_by_id('modifiedDate-4').get_property('value')
        print mod_date
        create_by = driver.find_element_by_id('createdBy-4').get_property('value')
        print create_by
        create_date = driver.find_element_by_id('createdDate-4').get_property('value')
        print create_date
        #we are asserting the fifth row of data is correct
        self.assertEqual(term0, 'DOID:9352')
        self.assertEqual(voc_term.text, 'type 2 diabetes mellitus')
        self.assertEqual(qualfy, 'string:8068249')
        self.assertEqual(j_num, 'J:222870')
        self.assertEqual(cite.text, 'Liu ZQ, Toxicol Appl Pharmacol 2015 May 15;285(1):61-70')
        self.assertEqual(mod_by, 'monikat')
        self.assertEqual(mod_date, '2015-08-07')
        self.assertEqual(create_by, 'monikat')
        self.assertEqual(create_date, '2015-08-07')

    def testDoMpJnumSearch(self):
        """
        @Status tests that a basic DOMP J number search works
        @see pwi-domp-search-8, 9
        """
        driver = self.driver
        #finds the J number field and enters a J number then clicks the Search button
        driver.find_element_by_id("jnumID-0").send_keys('J:201095')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element_by_id('searchButton').click()
        #waits until the element is located or 10 seconds
        #WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, 'termID-0')))
        time.sleep(5)
        #find the search results table first row of data
        term0 = driver.find_element_by_id('termID-0').get_property('value')
        print term0
        voc_term = driver.find_elements_by_class_name('term')[0]
        print voc_term.text
        qualfy = driver.find_element_by_id('qualifierAbbreviation-0').get_property('value')#value should be 'string:8068249' that equals therapy
        print qualfy
        j_num = driver.find_element_by_id('jnumID-0').get_property('value')
        print j_num
        cite = driver.find_elements_by_class_name('short_citation')[0]
        print cite.text
        mod_by = driver.find_element_by_id('modifiedBy-0').get_property('value')
        print mod_by
        mod_date = driver.find_element_by_id('modifiedDate-0').get_property('value')
        print mod_date
        create_by = driver.find_element_by_id('createdBy-0').get_property('value')
        print create_by
        create_date = driver.find_element_by_id('createdDate-0').get_property('value')
        print create_date
        #we are asserting the seventh row of data is correct
        self.assertEqual(term0, 'DOID:0110927')
        self.assertEqual(voc_term.text, 'nemaline myopathy 3')
        self.assertEqual(qualfy, 'string:8068249')
        self.assertEqual(j_num, 'J:201095')
        self.assertEqual(cite.text, 'Ravenscroft G, Hum Mol Genet 2013 Oct 1;22(19):3987-97')
        self.assertEqual(mod_by, 'monikat')
        self.assertEqual(mod_date, '2016-09-19')
        self.assertEqual(create_by, 'monikat')
        self.assertEqual(create_date, '2016-09-19')

    def testDoMpannotCreatedSearch(self):
        """
        @Status tests that an DOMP annotation search using the Created field returns correct data
        @see pwi-domp-date-search-1 
        """
        driver = self.driver
        #find the Modified By field and enter the user name
        driver.find_element_by_id("createdBy-0").send_keys("smb")
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 6 rows of results
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        cell2 = table.get_row(2)
        cell3 = table.get_row(3)
        cell4 = table.get_row(4)
        cell5 = table.get_row(5)
        print cell0.text
        print cell1.text
        print cell2.text
        print cell3.text
        print cell4.text
        print cell5.text
        #Assert the correct alleles have been returned in the results table(only the first 6 results)
        self.assertEqual(cell0.text, 'A<y>, agouti yellow')
        self.assertEqual(cell1.text, 'Abcc6<tm1Aabb>, targeted mutation 1, Arthur AB Bergen')
        self.assertEqual(cell2.text, 'Acta1<tm1Hrd>, targeted mutation 1, Edna C Hardeman')
        self.assertEqual(cell3.text, 'Actb<tm3.1(Sirt1)Npa>, targeted mutation 3.1, Novartis Pharma AG')
        self.assertEqual(cell4.text, 'Acvrl1<tm2.1Spo>, targeted mutation 2.1, S Paul Oh')
        self.assertEqual(cell5.text, 'Aire<tm1.1Doi>, targeted mutation 1.1, Christophe Benoist and Diane Mathis')
        #Assert the correct Creation Name is returned in the Created By field
        createuser = driver.find_element_by_id('createdBy-0').get_attribute('value')
        self.assertEqual(createuser, 'smb')    

    def testDoMpannotModBySearch(self):
        """
        @Status tests that a search using the Modified field returns correct data
        @see pwi-domp-date-search-2 
        """
        driver = self.driver
        #find the Modified By field and enter the user name
        driver.find_element_by_id("modifiedBy-0").send_keys("wilmil")
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 6 rows of results
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        cell2 = table.get_row(2)
        cell3 = table.get_row(3)
        cell4 = table.get_row(4)
        cell5 = table.get_row(5)
        print cell0.text
        print cell1.text
        print cell2.text
        print cell3.text
        print cell4.text
        print cell5.text
        #Assert the correct alleles have been returned in the results table(first 6 results only)
        self.assertEqual(cell0.text, 'Abcb1a<tm1Bor>, targeted mutation 1, Piet Borst')
        self.assertEqual(cell1.text, 'Afg3l2<tm1.1Alfb>, targeted mutation 1.1, Alfredo Brusco')
        self.assertEqual(cell2.text, 'Agpat2<tm1Garg>, targeted mutation 1, Abhimanyu Garg')
        self.assertEqual(cell3.text, 'Amacr<tm1Jkh>, targeted mutation 1, J Kalervo Hiltunen')
        self.assertEqual(cell4.text, 'Apc<tm1Tno>, targeted mutation 1, Tetsuo Noda')
        self.assertEqual(cell5.text, 'Brd4<M1Rvt>, mutation 1, Rajesh V Thakker')
        #Assert the correct Modified By Name is returned in the Modified field
        moduser = driver.find_element_by_id('modifiedBy-1').get_attribute('value')
        self.assertEqual(moduser, 'wilmil')        

    def testDoMpannotCreateDateSearch(self):
        """
        @Status tests that a basic Creation Date search works
        @see pwi-domp-date-search-3 
        """
        driver = self.driver
        #finds the Creation Date field, enters a Date
        driver.find_element_by_id("createdDate-0").send_keys("2014-09-09")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 4 rows of results
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        cell2 = table.get_row(2)
        cell3 = table.get_row(3)
        print cell0.text
        print cell1.text
        print cell2.text
        print cell3.text
        #Assert the correct alleles have been returned in the results table
        self.assertEqual(cell0.text, 'A<y>, agouti yellow')
        self.assertEqual(cell1.text, 'Fbn1<tm2Rmz>, targeted mutation 2, Francesco Ramirez')
        self.assertEqual(cell2.text, 'Hbb-b1<tm1Unc>, targeted mutation 1, University of North Carolina')
        self.assertEqual(cell3.text, 'Hbb-b2<tm1Unc>, targeted mutation 1, University of North Carolina')
        #Assert the correct Creation Name is returned in the Creation Date field
        createdate = driver.find_element_by_id('createdDate-3').get_attribute('value')
        self.assertEqual(createdate, '2014-09-09')        
             
    def testDoMpannotModifyDateSearch(self):
        """
        @Status tests that a basic Modification Date search works
        @see pwi-domp-date-search-4 
        """
        driver = self.driver
        #finds the Modification Date field, enters a Date
        driver.find_element_by_id("modifiedDate-0").send_keys("2015-08-07")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 5 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        cell2 = table.get_row(2)
        cell3 = table.get_row(3)
        cell4 = table.get_row(4)
        print cell0.text
        print cell1.text
        print cell2.text
        print cell3.text
        print cell4.text
        #Assert the correct alleles have been returned in the results table
        self.assertEqual(cell0.text, 'A<y>, agouti yellow')
        self.assertEqual(cell1.text, 'Gnmt<tm1Ymac>, targeted mutation 1, Yi-Ming Arthur Chen')
        self.assertEqual(cell2.text, 'Pten<tm1Hwu>, targeted mutation 1, Hong Wu')
        self.assertEqual(cell3.text, 'Stk11<tm1Rdp>, targeted mutation 1, Ronald DePinho')
        self.assertEqual(cell4.text, 'Tg(APPSwFlLon,PSEN1*M146L*L286V)6799Vas, transgene insertion 6799, Robert Vassar')
        #Assert the correct Creation Name is returned in the Creation Date field
        modifydate = driver.find_element_by_id('modifiedDate-4').get_attribute('value')
        self.assertEqual(modifydate, '2015-08-07')        

    def testDoMpannotModifyDateLessSearch(self):
        """
        @Status tests that a basic Modification Date by less than works
        @see pwi-domp-date-search-7  
        """
        driver = self.driver
        #finds the Modification Date field, enters a Date with less than symbol
        driver.find_element_by_id("modifiedDate-0").send_keys('<2012-02-02')
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct alleles have been returned in the results table
        self.assertEqual(cell0.text, 'Apoa1<tm1Unc>, targeted mutation 1, University of North Carolina')
        self.assertEqual(cell1.text, 'Cd14<tm1Frm>, targeted mutation 1, Mason W Freeman')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('modifiedDate-0').get_attribute('value')
        self.assertEqual(modifydate, '2012-02-01')        

    def testDoMpannotModifyDateLessEqualSearch(self):
        """
        @Status tests that a basic Modification Date by less than equals works
        @see pwi-domp-date-search-8 
        """
        driver = self.driver
        #finds the Modification Date field, enters a Date with less than symbol
        driver.find_element_by_id("modifiedDate-0").send_keys('<=2012-02-01')
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct gentypes have been returned in the results table
        self.assertEqual(cell0.text, 'Apoa1<tm1Unc>, targeted mutation 1, University of North Carolina')
        self.assertEqual(cell1.text, 'Cd14<tm1Frm>, targeted mutation 1, Mason W Freeman')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('modifiedDate-0').get_attribute('value')
        self.assertEqual(modifydate, '2012-02-01')        
      
    def testDoMpannotModifyDateRangeSearch(self):
        """
        @Status tests that a basic Modification Date by range search works
        @see pwi-domp-date-search-9 
        """
        driver = self.driver
        #finds the Modification Date field, enters a range of Dates
        driver.find_element_by_id("modifiedDate-0").send_keys("2014-08-20..2014-08-21")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct alleles have been returned in the results table
        self.assertEqual(cell0.text, 'Apc<Min>, multiple intestinal neoplasia')
        self.assertEqual(cell1.text, 'Prkn<tm1Ccs>, targeted mutation 1, Christine C Stichel')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('modifiedDate-1').get_attribute('value')
        self.assertEqual(modifydate, '2014-08-21')  
        
    def testDoMpannotCreateDateLessSearch(self):
        """
        @Status tests that a basic Creation Date by less than works
        @see pwi-domp-date-search-12 
        """
        driver = self.driver
        #finds the Creation Date field, enters a Date with less than symbol
        driver.find_element_by_id("createdDate-0").send_keys('<2012-02-02')
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct alleles have been returned in the results table
        self.assertEqual(cell0.text, 'Apoa1<tm1Unc>, targeted mutation 1, University of North Carolina')
        self.assertEqual(cell1.text, 'Cd14<tm1Frm>, targeted mutation 1, Mason W Freeman')
        #Assert the correct Creation Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('createdDate-0').get_attribute('value')
        self.assertEqual(modifydate, '2012-02-01')        

    def testDoMpannotCreateDateLessEqualSearch(self):
        """
        @Status tests that a basic Creation Date by less than equals works
        @see pwi-domp-date-search-13 
        """
        driver = self.driver
        #finds the Creation Date field, enters a Date with less than symbol
        driver.find_element_by_id("createdDate-0").send_keys('<=2012-02-16')
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print cell0.text
        print cell1.text
        #Assert the correct alleles have been returned in the results table
        self.assertEqual(cell0.text, 'Actb<tm3.1(Sirt1)Npa>, targeted mutation 3.1, Novartis Pharma AG')
        self.assertEqual(cell1.text, 'Ambn<tm1Nid>, targeted mutation 1, Yoshihiko Yamada')
        #Assert the correct Creation Date is returned in the Creation Date field
        createdate = driver.find_element_by_id('createdDate-0').get_attribute('value')
        self.assertEqual(createdate, '2012-02-16')        
      
    def testDoMpannotCreateDateRangeSearch(self):
        """
        @Status tests that a basic Creation Date by range search works
        @see pwi-domp-date-search-14  
        """
        driver = self.driver
        #finds the Creation Date field, enters a range of Dates
        driver.find_element_by_id("createdDate-0").send_keys("2012-02-16..2012-02-24")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        cell2 = table.get_row(2)
        print cell0.text
        print cell1.text
        print cell2.text
        #Assert the correct alleles have been returned in the results table
        self.assertEqual(cell0.text, 'Actb<tm3.1(Sirt1)Npa>, targeted mutation 3.1, Novartis Pharma AG')
        self.assertEqual(cell1.text, 'Ambn<tm1Nid>, targeted mutation 1, Yoshihiko Yamada')
        self.assertEqual(cell2.text, 'Tcirg1<oc>, osteosclerotic')
        #Assert the correct Creation Date is returned in the Creation Date field
        createdate = driver.find_element_by_id('createdDate-0').get_attribute('value')
        self.assertEqual(createdate, '2012-02-16')        
         

'''
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestImgSearch))
    return suite
'''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main()
    