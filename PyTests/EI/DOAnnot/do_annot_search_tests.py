'''
Created on Nov 13, 2019
These are tests that check the searching options of the DO Annotations module
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
#from configparser import SafeConfigParser
import HtmlTestRunner
import json
import config
import sys,os.path
from test.test_base64 import BaseXYTestCase
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests

class TestEIDoannotSearch(unittest.TestCase):
    """
    @status Test DO Annotations searching, etc
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/doannot")
    
    def tearDown(self):
        self.driver.close()

    def testDoMgiIdSearch(self):
        """
        @Status tests that a basic DO MGI ID genotype search works
        @see pwi-do-search-1 
        """
        driver = self.driver
        #finds the MGI ID field and enters an MGI genotype ID, tabs out of the field then clicks the Search button
        driver.find_element_by_id("genotypeAccId").send_keys('MGI:3624942')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element_by_id('searchButton').click()
        time.sleep(2)
        #find the Genotype field and verify it's text
        geno = driver.find_element_by_id('genotypeDisplay').get_property('value')
        print(geno)
        self.assertEqual(geno, '(NZB x BXSB)F1 Yaa')
        an_table = self.driver.find_element_by_id('annotTable')
        table = Table(an_table)
        #Iterate and print the table results
        header_cells = table.get_header_cells()
        headings = iterate.getTextAsList(header_cells)
        print(headings)
        #assert the headers are correct
        self.assertEqual(headings, ['', '', '', 'DO Term', 'Vocabulary Term', 'Qualifier', 'J#', 'Citation', 'Evidence', 'Modified', 'Date', 'Created', 'Date'])
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'termID-1')))
        #find the search results table first row of data
        term0 = driver.find_element_by_id('termID-0').get_property('value')
        print(term0)
        voc_term = driver.find_element_by_class_name('term')
        print(voc_term.text)
        qualfy = driver.find_element_by_id('qualifierAbbreviation-0').get_property('value')
        #value should be 'string:1614158' that equals (none)
        print(qualfy)
        j_num = driver.find_element_by_id('jnumID-0').get_property('value')
        print(j_num)
        cite = driver.find_element_by_class_name('short_citation')
        print(cite.text)
        evid = driver.find_element_by_id('evidenceAbbreviation-0').get_property('value')#value should be "string:847168" which is TAS
        print(evid)
        mod_by = driver.find_element_by_id('modifiedBy-0').get_property('value')
        print(mod_by)
        mod_date = driver.find_element_by_id('modifiedDate-0').get_property('value')
        print(mod_date)
        create_by = driver.find_element_by_id('createdBy-0').get_property('value')
        print(create_by)
        create_date = driver.find_element_by_id('createdDate-0').get_property('value')
        print(create_date)
        #we are asserting the first row of data is correct
        self.assertEqual(term0, 'DOID:9074')
        self.assertEqual(voc_term.text, 'systemic lupus erythematosus')
        self.assertEqual(qualfy, 'string:1614158')
        self.assertEqual(j_num, 'J:6235')
        self.assertEqual(cite.text, 'Murphy ED, Arthritis Rheum 1979 Nov;22(11):1188-94')
        self.assertEqual(evid, 'string:847168')
        self.assertEqual(mod_by, 'smb')
        self.assertEqual(mod_date, '2006-06-21')
        self.assertEqual(create_by, 'smb')
        self.assertEqual(create_date, '2006-06-21')

    def testDoGenotypeSearch(self):
        """
        @Status tests that a basic Genotype search works
        @see pwi-do-search-2
        """
        driver = self.driver
        #finds the Genotype field and enters a genotype(can also use wildcard of %, tabs out of the field then clicks the Search button
        driver.find_element_by_id("genotypeDisplay").send_keys('B6.Cg-Il10<tm1Cgn> Tg(MUC1)%')
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
        print(term0)
        voc_term = driver.find_element_by_class_name('term')
        print(voc_term.text)
        qualfy = driver.find_element_by_id('qualifierAbbreviation-0').get_property('value')#value should be 'string:1614158' that equals (none)
        print(qualfy)
        j_num = driver.find_element_by_id('jnumID-0').get_property('value')
        print(j_num)
        cite = driver.find_element_by_class_name('short_citation')
        print(cite.text)
        evid = driver.find_element_by_id('evidenceAbbreviation-0').get_property('value')#value should be "string:847168" which is TAS
        print(evid)
        mod_by = driver.find_element_by_id('modifiedBy-0').get_property('value')
        print(mod_by)
        mod_date = driver.find_element_by_id('modifiedDate-0').get_property('value')
        print(mod_date)
        create_by = driver.find_element_by_id('createdBy-0').get_property('value')
        print(create_by)
        create_date = driver.find_element_by_id('createdDate-0').get_property('value')
        print(create_date)
        #we are asserting the first row of data is correct
        self.assertEqual(term0, 'DOID:9256')
        self.assertEqual(voc_term.text, 'colorectal cancer')
        self.assertEqual(qualfy, 'string:1614158')
        self.assertEqual(j_num, 'J:149347')
        self.assertEqual(cite.text, 'Beatty PL, J Immunol 2007 Jul 15;179(2):735-9')
        self.assertEqual(evid, 'string:847168')
        self.assertEqual(mod_by, 'monikat')
        self.assertEqual(mod_date, '2012-08-27')
        self.assertEqual(create_by, 'monikat')
        self.assertEqual(create_date, '2012-08-27')
        
    def testDoTermIdSearch(self):
        """
        @Status tests that a basic DO Term ID search works
        @see pwi-do-search-3, 4
        """
        driver = self.driver
        #finds the Term ID field and enters an MP ID then clicks the Search button
        driver.find_element_by_id("termID-0").send_keys('DOID:9256')
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
        print(term0)
        voc_term = driver.find_element_by_class_name('term')
        print(voc_term.text)
        qualfy = driver.find_element_by_id('qualifierAbbreviation-0').get_property('value')#value should be 'string:1614158' that equals (none)
        print(qualfy)
        j_num = driver.find_element_by_id('jnumID-0').get_property('value')
        print(j_num)
        cite = driver.find_element_by_class_name('short_citation')
        print(cite.text)
        evid = driver.find_element_by_id('evidenceAbbreviation-0').get_property('value')#value should be "string:847168" which is TAS
        print(evid)
        mod_by = driver.find_element_by_id('modifiedBy-0').get_property('value')
        print(mod_by)
        mod_date = driver.find_element_by_id('modifiedDate-0').get_property('value')
        print(mod_date)
        create_by = driver.find_element_by_id('createdBy-0').get_property('value')
        print(create_by)
        create_date = driver.find_element_by_id('createdDate-0').get_property('value')
        print(create_date)
        #we are asserting the first row of data is correct
        self.assertEqual(term0, 'DOID:9256')
        self.assertEqual(voc_term.text, 'colorectal cancer')
        self.assertEqual(qualfy, 'string:1614158')
        self.assertEqual(j_num, 'J:158733')
        self.assertEqual(cite.text, 'Nam KT, J Clin Invest 2010 Mar;120(3):840-9')
        self.assertEqual(evid, 'string:847168')
        self.assertEqual(mod_by, 'jx')
        self.assertEqual(mod_date, '2010-04-21')
        self.assertEqual(create_by, 'jx')
        self.assertEqual(create_date, '2010-04-21')


    def testDoQualSearch(self):
        """
        @Status tests that a basic DO Qualifier search works
        @see pwi-do-search-7
        """
        driver = self.driver
        #finds the Qualifier field and select 'NOT' then clicks the Search button
        driver.find_element_by_id("qualifierAbbreviation-0").send_keys('NOT')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element_by_id('searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'termID-3')))
        #find the search results table third row of data
        term0 = driver.find_element_by_id('termID-0').get_property('value')
        print(term0)
        voc_term = driver.find_elements_by_class_name('term')[0]
        print(voc_term.text)
        qualfy = driver.find_element_by_id('qualifierAbbreviation-0').get_property('value')#value should be 'string:1614157' that equals NOT
        print(qualfy)
        j_num = driver.find_element_by_id('jnumID-2').get_property('value')
        print(j_num)
        cite = driver.find_elements_by_class_name('short_citation')[0]
        print(cite.text)
        evid = driver.find_element_by_id('evidenceAbbreviation-0').get_property('value')#value should be "string:847168" which is TAS
        print(evid)
        mod_by = driver.find_element_by_id('modifiedBy-0').get_property('value')
        print(mod_by)
        mod_date = driver.find_element_by_id('modifiedDate-0').get_property('value')
        print(mod_date)
        create_by = driver.find_element_by_id('createdBy-0').get_property('value')
        print(create_by)
        create_date = driver.find_element_by_id('createdDate-0').get_property('value')
        print(create_date)
        #we are asserting the third row of data is correct
        self.assertEqual(term0, 'DOID:11949')
        self.assertEqual(voc_term.text, 'Creutzfeldt-Jakob disease')
        self.assertEqual(qualfy, 'string:1614157')
        self.assertEqual(j_num, 'J:58820')
        self.assertEqual(cite.text, 'Manson JC, EMBO J 1999 Dec 1;18(23):6855-64')
        self.assertEqual(evid, 'string:847168')
        self.assertEqual(mod_by, 'anna')
        self.assertEqual(mod_date, '2005-06-20')
        self.assertEqual(create_by, 'anna')
        self.assertEqual(create_date, '2005-06-20')

    def testDoJnumSearch(self):
        """
        @Status tests that a basic MP J number search works
        @see pwi-do-search-8, 9
        """
        driver = self.driver
        #finds the J number field and enters a J number then clicks the Search button
        driver.find_element_by_id("jnumID-0").send_keys('J:271850')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element_by_id('searchButton').click()
        #waits until the element is located or 10 seconds
        #WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, 'termID-0')))
        time.sleep(5)
        #find the search results table seventh row of data
        term0 = driver.find_element_by_id('termID-0').get_property('value')
        print(term0)
        voc_term = driver.find_elements_by_class_name('term')[0]
        print(voc_term.text)
        qualfy = driver.find_element_by_id('qualifierAbbreviation-0').get_property('value')#value should be 'string:1614158' that equals (none)
        print(qualfy)
        j_num = driver.find_element_by_id('jnumID-0').get_property('value')
        print(j_num)
        cite = driver.find_elements_by_class_name('short_citation')[0]
        print(cite.text)
        evid = driver.find_element_by_id('evidenceAbbreviation-0').get_property('value')#value should be "string:847168" which is TAS
        print(evid)
        mod_by = driver.find_element_by_id('modifiedBy-0').get_property('value')
        print(mod_by)
        mod_date = driver.find_element_by_id('modifiedDate-0').get_property('value')
        print(mod_date)
        create_by = driver.find_element_by_id('createdBy-0').get_property('value')
        print(create_by)
        create_date = driver.find_element_by_id('createdDate-0').get_property('value')
        print(create_date)
        #we are asserting the seventh row of data is correct
        self.assertEqual(term0, 'DOID:0060041')
        self.assertEqual(voc_term.text, 'autism spectrum disorder')
        self.assertEqual(qualfy, 'string:1614158')
        self.assertEqual(j_num, 'J:271850')
        self.assertEqual(cite.text, 'Shibutani M, Int J Mol Sci 2017 Aug 30;18(9):')
        self.assertEqual(evid, 'string:847168')
        self.assertEqual(mod_by, 'monikat')
        self.assertEqual(mod_date, '2019-04-04')
        self.assertEqual(create_by, 'monikat')
        self.assertEqual(create_date, '2019-04-04')

    def testDoEvidenceSearch(self):
        """
        @Status tests that a basic DO Evidence Code search works
        @see pwi-do-search-11
        """
        driver = self.driver
        #finds the Evidence Code field and select and evidence code then clicks the Search button
        driver.find_element_by_id("evidenceAbbreviation-0").send_keys('TAS')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element_by_id('searchButton').click()
        #waits until the element is located or 10 seconds
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'termID-0')))
        time.sleep(10)
        #find the search results table thirteenth row of data
        term0 = driver.find_element_by_id('termID-0').get_property('value')
        print(term0)
        voc_term = driver.find_elements_by_class_name('term')[0]
        print(voc_term.text)
        qualfy = driver.find_element_by_id('qualifierAbbreviation-0').get_property('value')#value should be 'string:1614158' that equals (none)
        print(qualfy)
        j_num = driver.find_element_by_id('jnumID-0').get_property('value')
        print(j_num)
        cite = driver.find_element_by_class_name('short_citation')
        print(cite.text)
        evid = driver.find_element_by_id('evidenceAbbreviation-0').get_property('value')#value should be "string:847168" which is TAS
        print(evid)
        mod_by = driver.find_element_by_id('modifiedBy-0').get_property('value')
        print(mod_by)
        mod_date = driver.find_element_by_id('modifiedDate-0').get_property('value')
        print(mod_date)
        create_by = driver.find_element_by_id('createdBy-0').get_property('value')
        print(create_by)
        create_date = driver.find_element_by_id('createdDate-0').get_property('value')
        print(create_date)
        #we are asserting the thirteenth row of data is correct
        self.assertEqual(term0, 'DOID:1206')
        self.assertEqual(voc_term.text, 'Rett syndrome')
        self.assertEqual(qualfy, 'string:1614158')
        self.assertEqual(j_num, 'J:135825')
        self.assertEqual(cite.text, 'Samaco RC, Hum Mol Genet 2008 Jun 15;17(12):1718-27')
        self.assertEqual(evid, 'string:847168')
        self.assertEqual(mod_by, 'rbabiuk')
        self.assertEqual(mod_date, '2008-11-21')
        self.assertEqual(create_by, 'rbabiuk')
        self.assertEqual(create_date, '2008-11-21')

    def testDoNoteTextSearch(self):
        """
        @Status tests that a basic note text search works
        @see pwi-do-search-12
        """
        driver = self.driver
        #finds the Note field and enter text, then clicks the Search button
        driver.find_element_by_id("noteType-0").send_keys('aneuploidy syndromes')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element_by_id('searchButton').click()
        #waits until the element is located or 10 seconds
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'termID-0')))
        time.sleep(10)
        #find the search results table thirteenth row of data
        term0 = driver.find_element_by_id('termID-0').get_property('value')
        print(term0)
        voc_term = driver.find_elements_by_class_name('term')[0]
        print(voc_term.text)
        qualfy = driver.find_element_by_id('qualifierAbbreviation-0').get_property('value')#value should be 'string:1614158' that equals (none)
        print(qualfy)
        j_num = driver.find_element_by_id('jnumID-0').get_property('value')
        print(j_num)
        cite = driver.find_element_by_class_name('short_citation')
        print(cite.text)
        evid = driver.find_element_by_id('evidenceAbbreviation-0').get_property('value')#value should be "string:847168" which is TAS
        print(evid)
        mod_by = driver.find_element_by_id('modifiedBy-0').get_property('value')
        print(mod_by)
        mod_date = driver.find_element_by_id('modifiedDate-0').get_property('value')
        print(mod_date)
        create_by = driver.find_element_by_id('createdBy-0').get_property('value')
        print(create_by)
        create_date = driver.find_element_by_id('createdDate-0').get_property('value')
        print(create_date)
        note_text = driver.find_element_by_id('noteType-0').get_property('value')
        print(note_text)
        #we are asserting the thirteenth row of data is correct
        self.assertEqual(term0, 'DOID:0080014')
        self.assertEqual(voc_term.text, 'chromosomal disease')
        self.assertEqual(qualfy, 'string:1614158')
        self.assertEqual(j_num, 'J:97039')
        self.assertEqual(cite.text, 'Vacik T, Proc Natl Acad Sci U S A 2005 Mar 22;102(12):4500-5')
        self.assertEqual(evid, 'string:847168')
        self.assertEqual(mod_by, 'monikat')
        self.assertEqual(mod_date, '2019-01-03')
        self.assertEqual(create_by, 'monikat')
        self.assertEqual(create_date, '2019-01-03')


    def testDoannotCreateBySearch(self):
        """
        @Status tests that an DO annotation search using the Created By field returns correct data
        @see pwi-do-date-search-1 
        """
        driver = self.driver
        #find the Modified By field and enter the user name
        driver.find_element_by_id("createdBy-0").send_keys("honda")
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows of results
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        cell2 = table.get_row(2)
        cell3 = table.get_row(3)
        cell4 = table.get_row(4)
        cell5 = table.get_row(5)
        print(cell0.text)
        print(cell1.text)
        print(cell2.text)
        print(cell3.text)
        print(cell4.text)
        print(cell5.text)
        #Assert the correct genotype has been returned in the results table
        self.assertEqual(cell0.text, '129S6/SvEvTac-Maoa<K284stop> Maoa<K284stop>')
        self.assertEqual(cell1.text, '129X1.Cg-Cyp1b1<tm1Gonz> Cyp1b1<tm1Gonz>,Cyp1b1<tm1Gonz>')
        self.assertEqual(cell2.text, 'B6(Cg)-Tyr<c-2J>/J Tyr<c-2J>,Tyr<c-2J>')
        self.assertEqual(cell3.text, 'B6.129P2-Nlgn4x<Gt(XST093)Byg> Nlgn4l<Gt(XST093)Byg>,Nlgn4l<Gt(XST093)Byg>')
        self.assertEqual(cell4.text, 'B6.129P2-Sptbn2<tm1Mjac> Sptbn2<tm1Mjac>,Sptbn2<tm1Mjac>')
        self.assertEqual(cell5.text, 'B6.129S4-Igk<tm1(Igk564)Tik> Igh<tm1(Igh564)Tik> Igh<tm1.1(Igh564)Tik>,Igh<tm1.1(Igh564)Tik>,Igk<tm1(Igk564)Tik>,Igk<tm1(Igk564)Tik>')
        #Assert the correct Creation Name is returned in the Created By field
        createuser = driver.find_element_by_id('createdBy-0').get_attribute('value')
        self.assertEqual(createuser, 'honda')    

    def testDoannotModBySearch(self):
        """
        @Status tests that a search using the Modified By field returns correct data
        @see pwi-do-date-search-2 
        """
        driver = self.driver
        #find the Modified By field and enter the user name
        driver.find_element_by_id("modifiedBy-0").send_keys("rbabiuk")
        #find the Search button and click it
        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows of results
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        cell2 = table.get_row(2)
        cell3 = table.get_row(3)
        cell4 = table.get_row(4)
        cell5 = table.get_row(5)
        print(cell0.text)
        print(cell1.text)
        print(cell2.text)
        print(cell3.text)
        print(cell4.text)
        print(cell5.text)
        #Assert the correct genotypes have been returned in the results table
        self.assertEqual(cell0.text, '(129S6.129P2-Mecp2<tm1Bird> x C57BL/6)F1 Mecp2<tm1Bird>')
        self.assertEqual(cell1.text, '(129S6.129P2-Mecp2<tm1Bird> x FVB/N)F1 Mecp2<tm1Bird>')
        self.assertEqual(cell2.text, '129S6/SvEvTac-Gck<tm2Mgn> Gck<tm2Mgn>,Gck<+>')
        self.assertEqual(cell3.text, '129S6/SvEvTac-Gck<tm2Mgn> Gck<tm2Mgn>,Gck<tm2Mgn>')
        self.assertEqual(cell4.text, 'B6.129-Manba<tm1Khf> Manba<tm1Khf>,Manba<tm1Khf>')
        self.assertEqual(cell5.text, 'B6.129-Tg(APPSw)40Btla Tg(APPSw)40Btla,Tg(APPSw)40Btla')
        #Assert the correct Modified By Name is returned in the Modified By field
        moduser = driver.find_element_by_id('modifiedBy-0').get_attribute('value')
        self.assertEqual(moduser, 'rbabiuk')        

    def testDoannotCreateDateSearch(self):
        """
        @Status tests that a basic Creation Date search works
        @see pwi-do-date-search-3 
        """
        driver = self.driver
        #finds the Creation Date field, enters a Date
        driver.find_element_by_id("createdDate-0").send_keys("2008-11-21")
        #finds the Search button and clicks it
        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element_by_id("resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows of results
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        cell2 = table.get_row(2)
        cell3 = table.get_row(3)
        print(cell0.text)
        print(cell1.text)
        print(cell2.text)
        print(cell3.text)
        #Assert the correct genotypes have been returned in the results table
        self.assertEqual(cell0.text, '(129S6.129P2-Mecp2<tm1Bird> x C57BL/6)F1 Mecp2<tm1Bird>')
        self.assertEqual(cell1.text, '(129S6.129P2-Mecp2<tm1Bird> x FVB/N)F1 Mecp2<tm1Bird>')
        self.assertEqual(cell2.text, 'involves: 129S7/SvEvBrd Arid4a<tm1Alb>,Arid4a<tm1Alb>')
        self.assertEqual(cell3.text, 'involves: 129S7/SvEvBrd Arid4a<tm1Alb>,Arid4a<tm1Alb>,Arid4b<tm1Alb>,Arid4b<+>')
        #Assert the correct Creation Name is returned in the Creation Date field
        createdate = driver.find_element_by_id('createdDate-0').get_attribute('value')
        self.assertEqual(createdate, '2008-11-21')        
             
    def testDoannotModifyDateSearch(self):
        """
        @Status tests that a basic Modification Date search works
        @see pwi-do-date-search-4 
        """
        driver = self.driver
        #finds the Modification Date field, enters a Date
        driver.find_element_by_id("modifiedDate-0").send_keys("2017-06-08")
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
        print(cell0.text)
        print(cell1.text)
        print(cell2.text)
        #Assert the correct genotypes have been returned in the results table
        self.assertEqual(cell0.text, '(C3H/HeJ x B6.129S2-Trp53<tm1Tyj> Nf1<tm1Tyj>/+ +)F1 Nf1<tm1Tyj>,Nf1<+>,Trp53<tm1Tyj>,Trp53<+>')
        self.assertEqual(cell1.text, '(CAST/EiJ x B6.129S2-Trp53<tm1Tyj> Nf1<tm1Tyj>/+ +)F1 Nf1<tm1Tyj>,Nf1<+>,Trp53<tm1Tyj>,Trp53<+>')
        self.assertEqual(cell2.text, '(CBA/J x B6.129S2-Trp53<tm1Tyj> Nf1<tm1Tyj>/+ +)F1 Nf1<tm1Tyj>,Nf1<+>,Trp53<tm1Tyj>,Trp53<+>')
        #Assert the correct Creation Name is returned in the Creation Date field
        modifydate = driver.find_element_by_id('modifiedDate-0').get_attribute('value')
        self.assertEqual(modifydate, '2017-06-08')        

#    def testDoannotModifyDateGreaterSearch(self):
#        """
#        @Status tests that a basic Modification Date by Greater than works
#        @see pwi-do-date-search-5 
#        """
#        driver = self.driver
        #finds the Modification Date field, enters a Date with greater than symbol
#        driver.find_element_by_id("modifiedDate-0").send_keys('>2019-05-06')
        #finds the Search button and clicks it
#        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
#        wait.forAngular(self.driver)
        #find the search results table
#        results_table = self.driver.find_element_by_id("resultsTable")
#        table = Table(results_table)
        # get and print the first 2 rows
#        cell0 = table.get_row(0)
#        cell1 = table.get_row(1)
#        cell2 = table.get_row(2)
#        cell3 = table.get_row(3)
#        cell4 = table.get_row(4)
#        cell5 = table.get_row(5)
#        print cell0.text
#        print cell1.text
#        print cell2.text
#        print cell3.text
#        print cell4.text
#        print cell5.text
        #Assert the correct genotypes have been returned in the results table
#        self.assertEqual(cell0.text, '129P3/J-Ush1c<dfcr-4J>/J Ush1c<dfcr-4J>,Ush1c<dfcr-4J>')
#        self.assertEqual(cell1.text, '129S6.B6(Cg)-Shank3<tm1.2Bux> Shank3<tm1.2Bux>,Shank3<tm1.2Bux>')
#        self.assertEqual(cell2.text, 'B6(Cg)-Npc1<tm1Tacf> Npc1<tm1Tacf>,Npc1<tm1Tacf>')
#        self.assertEqual(cell3.text, 'B6(Cg)-Npc1<tm1Tacf> Npc1<tm2Tacf> Npc1<tm1Tacf>,Npc1<tm2Tacf>')
#        self.assertEqual(cell4.text, 'B6(Cg)-Slc39a8<tm1.2Mrl> Slc39a8<tm1.2Mrl>,Slc39a8<tm1.2Mrl>')
#        self.assertEqual(cell5.text, 'B6(FVB)-2210010C04Rik<tm1.1Satom> 2210010C04Rik<tm1.1Satom>,2210010C04Rik<+>')
        #Assert the correct Modification Date is returned in the Modification Date field
#        modifydate = driver.find_element_by_id('modifiedDate-0').get_attribute('value')
#        self.assertEqual(modifydate, '2019-09-13')    '''    

#    def testDoannotModifyDateGreaterEqualSearch(self):
#        """
#        @Status tests that a basic Modification Date by greater than equals works
#        @see pwi-do-date-search-6 
#        """
#        driver = self.driver
        #finds the Modification Date field, enters a Date with greater than equals symbols
#        driver.find_element_by_id("modifiedDate-0").send_keys('>=2019-05-09')
        #finds the Search button and clicks it
#        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
#        wait.forAngular(self.driver)
        #find the search results table
#        results_table = self.driver.find_element_by_id("resultsTable")
#        table = Table(results_table)
        # get and print the first 2 rows
#        cell0 = table.get_row(0)
#        cell1 = table.get_row(1)
#        cell2 = table.get_row(2)
#        cell3 = table.get_row(3)
#        cell4 = table.get_row(4)
#        cell5 = table.get_row(5)
#        print cell0.text
#        print cell1.text
#        print cell2.text
#        print cell3.text
#        print cell4.text
#        print cell5.text
        #Assert the correct genotypes have been returned in the results table
#        self.assertEqual(cell0.text, '129P3/J-Ush1c<dfcr-4J>/J Ush1c<dfcr-4J>,Ush1c<dfcr-4J>')
#        self.assertEqual(cell1.text, '129S6.B6(Cg)-Shank3<tm1.2Bux> Shank3<tm1.2Bux>,Shank3<tm1.2Bux>')
#        self.assertEqual(cell2.text, 'B6(Cg)-Npc1<tm1Tacf> Npc1<tm1Tacf>,Npc1<tm1Tacf>')
#        self.assertEqual(cell3.text, 'B6(Cg)-Npc1<tm1Tacf> Npc1<tm2Tacf> Npc1<tm1Tacf>,Npc1<tm2Tacf>')
#        self.assertEqual(cell4.text, 'B6(Cg)-Slc39a8<tm1.2Mrl> Slc39a8<tm1.2Mrl>,Slc39a8<tm1.2Mrl>')
#        self.assertEqual(cell5.text, 'B6(FVB)-2210010C04Rik<tm1.1Satom> 2210010C04Rik<tm1.1Satom>,2210010C04Rik<+>')
        #Assert the correct Modification Date is returned in the Modification Date field
#        modifydate = driver.find_element_by_id('modifiedDate-0').get_attribute('value')
#        self.assertEqual(modifydate, '2019-09-13')    

    def testDoannotModifyDateLessSearch(self):
        """
        @Status tests that a basic Modification Date by less than works
        @see pwi-do-date-search-7  
        """
        driver = self.driver
        #finds the Modification Date field, enters a Date with less than symbol
        driver.find_element_by_id("modifiedDate-0").send_keys('<2005-09-16')
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
        print(cell0.text)
        print(cell1.text)
        #Assert the correct genotypes have been returned in the results table
        self.assertEqual(cell0.text, '129-Nphs2<tm1Antc> Nphs2<tm1Antc>,Nphs2<tm1Antc>')
        self.assertEqual(cell1.text, '129P2(C)-Cecr2<Gt(pGT1)1Hemc> Cecr2<Gt(pGT1)1Hemc>,Cecr2<Gt(pGT1)1Hemc>')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('modifiedDate-0').get_attribute('value')
        self.assertEqual(modifydate, '2005-06-27')        

    def testDoannotModifyDateLessEqualSearch(self):
        """
        @Status tests that a basic Modification Date by less than equals works
        @see pwi-do-date-search-8 
        """
        driver = self.driver
        #finds the Modification Date field, enters a Date with less than symbol
        driver.find_element_by_id("modifiedDate-0").send_keys('<=2009-09-14')
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
        print(cell0.text)
        print(cell1.text)
        #Assert the correct gentypes have been returned in the results table
        self.assertEqual(cell0.text, '(129S6.129P2-Mecp2<tm1Bird> x C57BL/6)F1 Mecp2<tm1Bird>')
        self.assertEqual(cell1.text, '(129S6.129P2-Mecp2<tm1Bird> x FVB/N)F1 Mecp2<tm1Bird>')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('modifiedDate-0').get_attribute('value')
        self.assertEqual(modifydate, '2008-11-21')        
      
    def testDoannotModifyDateRangeSearch(self):
        """
        @Status tests that a basic Modification Date by range search works
        @see pwi-do-date-search-9 
        """
        driver = self.driver
        #finds the Modification Date field, enters a range of Dates
        driver.find_element_by_id("modifiedDate-0").send_keys("2019-05-08..2019-05-10")
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
        print(cell0.text)
        print(cell1.text)
        #Assert the correct genotypes have been returned in the results table
        self.assertEqual(cell0.text, 'B6.129S6-Mlxipl<tm1Kuy>/J Mlxipl<tm1Kuy>,Mlxipl<tm1Kuy>')
        self.assertEqual(cell1.text, 'involves: FVB/N Tg(Col1a1-FGF2*,-Sapphire)203Mmh,Tg(Col1a1-FGF2*,-Sapphire)203Mmh')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('modifiedDate-0').get_attribute('value')
        self.assertEqual(modifydate, '2019-05-10')  
              
#    def testDoannotCreateDateGreaterSearch(self):
#        """
#        @Status tests that a basic Creation Date by Greater than works
#        @see pwi-do-date-search-10 
#        """
#        driver = self.driver
        #finds the Created Date field, enters a Date with greater than symbol
#        driver.find_element_by_id("createdDate-0").send_keys('>2019-05-08')
        #finds the Search button and clicks it
#        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
#        wait.forAngular(self.driver)
        #find the search results table
#        results_table = self.driver.find_element_by_id("resultsTable")
#        table = Table(results_table)
        # get and print the first 2 rows
#        cell0 = table.get_row(0)
#        cell1 = table.get_row(1)
#        cell2 = table.get_row(2)
#        cell3 = table.get_row(3)
#        cell4 = table.get_row(4)
#       cell5 = table.get_row(5)
#        print cell0.text
#        print cell1.text
#        print cell2.text
#        print cell3.text
#        print cell4.text
#        print cell5.text
        #Assert the correct genotypes have been returned in the results table
#        self.assertEqual(cell0.text, '129P3/J-Ush1c<dfcr-4J>/J Ush1c<dfcr-4J>,Ush1c<dfcr-4J>')
#        self.assertEqual(cell1.text, '129S6.B6(Cg)-Shank3<tm1.2Bux> Shank3<tm1.2Bux>,Shank3<tm1.2Bux>')
#        self.assertEqual(cell2.text, 'B6(Cg)-Npc1<tm1Tacf> Npc1<tm1Tacf>,Npc1<tm1Tacf>')
#        self.assertEqual(cell3.text, 'B6(Cg)-Npc1<tm1Tacf> Npc1<tm2Tacf> Npc1<tm1Tacf>,Npc1<tm2Tacf>')
#        self.assertEqual(cell4.text, 'B6(Cg)-Slc39a8<tm1.2Mrl> Slc39a8<tm1.2Mrl>,Slc39a8<tm1.2Mrl>')
#        self.assertEqual(cell5.text, 'B6(FVB)-2210010C04Rik<tm1.1Satom> 2210010C04Rik<tm1.1Satom>,2210010C04Rik<+>')
        #Assert the correct Modification Date is returned in the Modification Date field
#        modifydate = driver.find_element_by_id('createdDate-0').get_attribute('value')
#        self.assertEqual(modifydate, '2019-09-13')        

#    def testDoannotCreateDateGreaterEqualSearch(self):
#        """
#        @Status tests that a basic Creation Date by greater than equals works
#        @see pwi-d0-date-search-11 
#        """
#        driver = self.driver
        #finds the Creation Date field, enters a Date with greater than and equals symbols
#        driver.find_element_by_id("createdDate").send_keys('>=2019-05-09')
        #finds the Search button and clicks it
#        driver.find_element_by_id('searchButton').click()
        #wait until the Results list is displayed on the page    
#        wait.forAngular(self.driver)
        #find the search results table
#        results_table = self.driver.find_element_by_id("resultsTable")
#        table = Table(results_table)
        # get and print the first 2 rows
#        cell0 = table.get_row(0)
#        cell1 = table.get_row(1)
#        cell2 = table.get_row(2)
#        cell3 = table.get_row(3)
#        cell4 = table.get_row(4)
#        cell5 = table.get_row(5)
#        print cell0.text
#        print cell1.text
#        print cell2.text
#        print cell3.text
#        print cell4.text
#        print cell5.text
        #Assert the correct genotypes have been returned in the results table
#        self.assertEqual(cell0.text, '129P3/J-Ush1c<dfcr-4J>/J Ush1c<dfcr-4J>,Ush1c<dfcr-4J>')
#        self.assertEqual(cell1.text, '129S6.B6(Cg)-Shank3<tm1.2Bux> Shank3<tm1.2Bux>,Shank3<tm1.2Bux>')
#        self.assertEqual(cell2.text, 'B6(Cg)-Npc1<tm1Tacf> Npc1<tm1Tacf>,Npc1<tm1Tacf>')
#        self.assertEqual(cell3.text, 'B6(Cg)-Npc1<tm1Tacf> Npc1<tm2Tacf> Npc1<tm1Tacf>,Npc1<tm2Tacf>')
#        self.assertEqual(cell4.text, 'B6(Cg)-Slc39a8<tm1.2Mrl> Slc39a8<tm1.2Mrl>,Slc39a8<tm1.2Mrl>')
#        self.assertEqual(cell5.text, 'B6(FVB)-2210010C04Rik<tm1.1Satom> 2210010C04Rik<tm1.1Satom>,2210010C04Rik<+>')
#        #Assert the correct Modification Date is returned in the Modification Date field
#        modifydate = driver.find_element_by_id('createdDate').get_attribute('value')#
#        self.assertEqual(modifydate, '2019-09-13')    
        
    def testDoannotCreateDateLessSearch(self):
        """
        @Status tests that a basic Creation Date by less than works
        @see pwi-do-date-search-12 
        """
        driver = self.driver
        #finds the Creation Date field, enters a Date with less than symbol
        driver.find_element_by_id("createdDate-0").send_keys('<2005-09-13')
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
        print(cell0.text)
        print(cell1.text)
        #Assert the correct genotypes have been returned in the results table
        self.assertEqual(cell0.text, '129-Nphs2<tm1Antc> Nphs2<tm1Antc>,Nphs2<tm1Antc>')
        self.assertEqual(cell1.text, '129P2(C)-Cecr2<Gt(pGT1)1Hemc> Cecr2<Gt(pGT1)1Hemc>,Cecr2<Gt(pGT1)1Hemc>')
        #Assert the correct Creation Date is returned in the Modification Date field
        modifydate = driver.find_element_by_id('createdDate-0').get_attribute('value')
        self.assertEqual(modifydate, '2005-06-27')        

    def testDoannotCreateDateLessEqualSearch(self):
        """
        @Status tests that a basic Creation Date by less than equals works
        @see pwi-do-date-search-13 
        """
        driver = self.driver
        #finds the Creation Date field, enters a Date with less than symbol
        driver.find_element_by_id("createdDate-0").send_keys('<=2005-05-10')
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
        print(cell0.text)
        print(cell1.text)
        #Assert the correct genotypes have been returned in the results table
        self.assertEqual(cell0.text, 'B6.C3-Mfrp<rd6> Mfrp<rd6>,Mfrp<rd6>')
        self.assertEqual(cell1.text, 'B6.Cg-Aire<tm1Mmat> Aire<tm1Mmat>,Aire<tm1Mmat>')
        #Assert the correct Creation Date is returned in the Creation Date field
        createdate = driver.find_element_by_id('createdDate-0').get_attribute('value')
        self.assertEqual(createdate, '2005-05-10')        
      
    def testDoannotCreateDateRangeSearch(self):
        """
        @Status tests that a basic Creation Date by range search works
        @see pwi-do-date-search-14 
        """
        driver = self.driver
        #finds the Creation Date field, enters a range of Dates
        driver.find_element_by_id("createdDate-0").send_keys("2005-05-09..2005-05-11")
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
        print(cell0.text)
        print(cell1.text)
        #Assert the correct genotypes have been returned in the results table
        self.assertEqual(cell0.text, 'B6.C3-Mfrp<rd6> Mfrp<rd6>,Mfrp<rd6>')
        self.assertEqual(cell1.text, 'B6.Cg-Aire<tm1Mmat> Aire<tm1Mmat>,Aire<tm1Mmat>')
        #Assert the correct Creation Date is returned in the Creation Date field
        createdate = driver.find_element_by_id('createdDate-0').get_attribute('value')
        self.assertEqual(createdate, '2005-05-10')        
         
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEIDoannotSearch))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
    