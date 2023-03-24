'''
Created on Oct 3, 2019
These are tests that check the searching options of the MP Annotations module
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
import HtmlTestRunner
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

class TestEiMpannotSearch(unittest.TestCase):
    """
    @status Test MP Annotations searching, etc
    """

    def setUp(self):
        self.driver = webdriver.Firefox() 
        #self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/mpannot")
    
    def tearDown(self):
        self.driver.close()

    def testMPMgiIdSearch(self):
        """
        @Status tests that a basic MP MGI ID genotype search works
        @see pwi-mp-search-1
        """
        driver = self.driver
        #finds the MGI ID field and enters an MGI genotype ID, tabs out of the field
        driver.find_element(By.ID, "genotypeAccId").send_keys('MGI:5445717')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        an_table = self.driver.find_element(By.ID, 'annotTable')
        table = Table(an_table)
        #Iterate and print the table results
        header_cells = table.get_header_cells()
        headings = iterate.getTextAsList(header_cells)
        print(headings)
        #assert the headers are correct
        self.assertEqual(headings, ['', '', '', 'MP Term', 'Vocabulary Term', 'Qualifier', 'J#', 'Citation', 'Evidence', 'Sex', 'Modified', 'Date', 'Created', 'Date'])
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'termID-1')))
        #find the search results table first row of data
        term0 = driver.find_element(By.ID, 'termID-0').get_property('value')
        print(term0)
        voc_term = driver.find_element(By.CLASS_NAME, 'term')
        print(voc_term.text)
        qualfy = driver.find_element(By.ID, 'qualifierAbbreviation-0').get_property('value')
        #value should be 'string:2181423' that equals (none)
        print(qualfy)
        j_num = driver.find_element(By.ID, 'jnumID-0').get_property('value')
        print(j_num)
        cite = driver.find_element(By.CLASS_NAME, 'short_citation')
        print(cite.text)
        evid = driver.find_element(By.ID, 'evidenceAbbreviation-0').get_property('value')#value should be "string:52280" which is EXP
        print(evid)
        sex_abbrev = driver.find_element(By.ID, 'sexAbbreviation-0').get_property('value')#value should be "string:NA"
        print(sex_abbrev)
        mod_by = driver.find_element(By.ID, 'modifiedBy-0').get_property('value')
        print(mod_by)
        mod_date = driver.find_element(By.ID, 'modifiedDate-0').get_property('value')
        print(mod_date)
        create_by = driver.find_element(By.ID, 'createdBy-0').get_property('value')
        print(create_by)
        create_date = driver.find_element(By.ID, 'createdDate-0').get_property('value')
        print(create_date)
        #we are asserting the first row of data is correct
        self.assertEqual(term0, 'MP:0001927')
        self.assertEqual(voc_term.text, 'abnormal estrous cycle')
        self.assertEqual(qualfy, 'string:2181423')
        self.assertEqual(j_num, 'J:189146')
        self.assertEqual(cite.text, 'Burnicka-Turek O, Endocrinology 2012 Oct;153(10):4655-65')
        self.assertEqual(evid, 'string:52280')
        self.assertEqual(sex_abbrev, 'string:F')
        self.assertEqual(mod_by, 'smb')
        self.assertEqual(mod_date, '2020-05-12')
        self.assertEqual(create_by, 'mnk')
        self.assertEqual(create_date, '2012-12-13')

    def testMPGenotypeSearch(self):
        """
        @Status tests that a basic Genotype search works
        @see pwi-mp-search-2
        """
        driver = self.driver
        #finds the Genotype field and enters a genotype(can also use wildcard of %, tabs out of the field then clicks the Search button
        driver.find_element(By.ID, "genotypeDisplay").send_keys('129S/SvEv-Bey%')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'termID-8')))
        #find the search results table first row of data
        term0 = driver.find_element(By.ID, 'termID-0').get_property('value')
        print(term0)
        voc_term = driver.find_element(By.CLASS_NAME, 'term')
        print(voc_term.text)
        qualfy = driver.find_element(By.ID, 'qualifierAbbreviation-0').get_property('value')#value should be 'string:2181423' that equals (none)
        print(qualfy)
        j_num = driver.find_element(By.ID, 'jnumID-0').get_property('value')
        print(j_num)
        cite = driver.find_element(By.CLASS_NAME, 'short_citation')
        print(cite.text)
        evid = driver.find_element(By.ID, 'evidenceAbbreviation-0').get_property('value')#value should be "string:52280" which is EXP
        print(evid)
        sex_abbrev = driver.find_element(By.ID, 'sexAbbreviation-0').get_property('value')#value should be "string:NA"
        print(sex_abbrev)
        mod_by = driver.find_element(By.ID, 'modifiedBy-0').get_property('value')
        print(mod_by)
        mod_date = driver.find_element(By.ID, 'modifiedDate-0').get_property('value')
        print(mod_date)
        create_by = driver.find_element(By.ID, 'createdBy-0').get_property('value')
        print(create_by)
        create_date = driver.find_element(By.ID, 'createdDate-0').get_property('value')
        print(create_date)
        #we are asserting the first row of data is correct
        self.assertEqual(term0, 'MP:0003743')
        self.assertEqual(voc_term.text, 'abnormal facial morphology')
        self.assertEqual(qualfy, 'string:2181423')
        self.assertEqual(j_num, 'J:47965')
        self.assertEqual(cite.text, 'Carlton MB, Dev Dyn 1998 Jun;212(2):242-9')
        self.assertEqual(evid, 'string:52280')
        self.assertEqual(sex_abbrev, 'string:NA')
        self.assertEqual(mod_by, 'anna')
        self.assertEqual(mod_date, '2017-11-16')
        self.assertEqual(create_by, 'anna')
        self.assertEqual(create_date, '2017-11-16')
        
    def testMPTermIdSearch(self):
        """
        @Status tests that a basic MP Term ID genotype search works
        @see pwi-mp-search-3, 4
        """
        driver = self.driver
        #finds the Term ID field and enters an MP ID then Tabs out of the field
        driver.find_element(By.ID, "termID-0").send_keys('MP:0010768')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'termID-3')))
        #find the search results table first row of data
        term0 = driver.find_element(By.ID, 'termID-0').get_property('value')
        print(term0)
        voc_term = driver.find_element(By.CLASS_NAME, 'term')
        print(voc_term.text)
        qualfy = driver.find_element(By.ID, 'qualifierAbbreviation-0').get_property('value')#value should be 'string:2181423' that equals (none)
        print(qualfy)
        j_num = driver.find_element(By.ID, 'jnumID-0').get_property('value')
        print(j_num)
        cite = driver.find_element(By.CLASS_NAME, 'short_citation')
        print(cite.text)
        evid = driver.find_element(By.ID, 'evidenceAbbreviation-0').get_property('value')#value should be "string:107" which is TAS
        print(evid)
        sex_abbrev = driver.find_element(By.ID, 'sexAbbreviation-0').get_property('value')#value should be "string:M"
        print(sex_abbrev)
        mod_by = driver.find_element(By.ID, 'modifiedBy-0').get_property('value')
        print(mod_by)
        mod_date = driver.find_element(By.ID, 'modifiedDate-0').get_property('value')
        print(mod_date)
        create_by = driver.find_element(By.ID, 'createdBy-0').get_property('value')
        print(create_by)
        create_date = driver.find_element(By.ID, 'createdDate-0').get_property('value')
        print(create_date)
        #we are asserting the first row of data is correct
        self.assertEqual(term0, 'MP:0001447')
        self.assertEqual(voc_term.text, 'abnormal nest building behavior')
        self.assertEqual(qualfy, 'string:2181423')
        self.assertEqual(j_num, 'J:135825')
        self.assertEqual(cite.text, 'Samaco RC, Hum Mol Genet 2008 Jun 15;17(12):1718-27')
        self.assertEqual(evid, 'string:107')
        self.assertEqual(sex_abbrev, 'string:M')
        self.assertEqual(mod_by, 'rbabiuk')
        self.assertEqual(mod_date, '2008-11-21')
        self.assertEqual(create_by, 'rbabiuk')
        self.assertEqual(create_date, '2008-11-21')
        #now lets find the Term ID for the 9th row and verify it is MP:0010768
        term8 = driver.find_element(By.ID, 'termID-8').get_property('value')
        print(term8)
        self.assertEqual(term8, 'MP:0010768')

    def testMPQualSearch(self):
        """
        @Status tests that a basic MP Qualifier search works
        @see pwi-mp-search-6
        """
        driver = self.driver
        time.sleep(2)
        #find and click the Clear button
        driver.find_element(By.ID, "clearButton").click()
        time.sleep(2)
        #finds the Qualifier field and select 'norm', find the Evidence field and select 'ND' then click Search.
        qual_box = Select(driver.find_element(By.ID, "qualifierAbbreviation-0"))
        qual_box.select_by_value('string:2181424')#value is Norm                          
        time.sleep(2)
        evid_box = Select(driver.find_element(By.ID, "evidenceAbbreviation-0"))
        evid_box.select_by_value('string:108')#value is ND
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'termID-3')))
        #find the search results table third row of data
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        #Iterate and print the search results
        cell2 = table.get_row_cells(2)
        result1 = iterate.getTextAsList(cell2)
        print(result1)
        term0 = driver.find_element(By.ID, 'termID-0').get_property('value')
        print(term0)
        voc_term = driver.find_elements(By.CLASS_NAME, 'term')[0]
        print(voc_term.text)
        qualfy = driver.find_elements(By.ID, 'qualifierAbbreviation-0')[0].get_property('value')#value should be 'string:2181423' that equals (none)
        print(qualfy)
        j_num = driver.find_element(By.ID, 'jnumID-0').get_property('value')
        print(j_num)
        cite = driver.find_elements(By.CLASS_NAME, 'short_citation')[0]
        print(cite.text)
        evid = driver.find_elements(By.ID, 'evidenceAbbreviation-0')[0].get_property('value')#value should be "string:108" which is ND
        print(evid)
        sex_abbrev = driver.find_elements(By.ID, 'sexAbbreviation-0')[0].get_property('value')#value should be "string:NA"
        print(sex_abbrev)
        mod_by = driver.find_elements(By.ID, 'modifiedBy-0')[0].get_property('value')
        print(mod_by)
        mod_date = driver.find_elements(By.ID, 'modifiedDate-0')[0].get_property('value')
        print(mod_date)
        create_by = driver.find_elements(By.ID, 'createdBy-0')[0].get_property('value')
        print(create_by)
        create_date = driver.find_elements(By.ID, 'createdDate-0')[0].get_property('value')
        print(create_date)
        #we are asserting the third row of data is correct
        self.assertEqual(term0, 'MP:0003012')
        self.assertEqual(voc_term.text, 'no phenotypic analysis')
        self.assertEqual(qualfy, 'string:2181424')
        self.assertEqual(j_num, 'J:133638')
        self.assertEqual(cite.text, 'Hitz C, Nucleic Acids Res 2007;35(12):e90')
        self.assertEqual(evid, 'string:108')
        self.assertEqual(sex_abbrev, 'string:NA')
        self.assertEqual(mod_by, 'tmeehan')
        self.assertEqual(mod_date, '2008-05-27')
        self.assertEqual(create_by, 'tmeehan')
        self.assertEqual(create_date, '2008-05-27')

    def testMPJnumSearch(self):
        """
        @Status tests that a basic MP J number search works
        @see pwi-mp-search-7, 8
        """
        driver = self.driver
        #finds the J number field and enters a J number then Tabs out of the field
        driver.find_element(By.ID, "jnumID-0").send_keys('J:29022')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'termID-3')))
        #find the search results table seventh row of data
        term0 = driver.find_element(By.ID, 'termID-6').get_property('value')
        print(term0)
        voc_term = driver.find_elements(By.CLASS_NAME, 'term')[6]
        print(voc_term.text)
        qualfy = driver.find_element(By.ID, 'qualifierAbbreviation-6').get_property('value')#value should be 'string:2181423' that equals (none)
        print(qualfy)
        j_num = driver.find_element(By.ID, 'jnumID-6').get_property('value')
        print(j_num)
        cite = driver.find_elements(By.CLASS_NAME, 'short_citation')[6]
        print(cite.text)
        evid = driver.find_element(By.ID, 'evidenceAbbreviation-6').get_property('value')#value should be "string:52280" which is EXP
        print(evid)
        sex_abbrev = driver.find_element(By.ID, 'sexAbbreviation-6').get_property('value')#value should be "string:NA"
        print(sex_abbrev)
        mod_by = driver.find_element(By.ID, 'modifiedBy-6').get_property('value')
        print(mod_by)
        mod_date = driver.find_element(By.ID, 'modifiedDate-6').get_property('value')
        print(mod_date)
        create_by = driver.find_element(By.ID, 'createdBy-6').get_property('value')
        print(create_by)
        create_date = driver.find_element(By.ID, 'createdDate-6').get_property('value')
        print(create_date)
        #we are asserting the seventh row of data is correct
        self.assertEqual(term0, 'MP:0000705')
        self.assertEqual(voc_term.text, 'athymia')
        self.assertEqual(qualfy, 'string:2181423')
        self.assertEqual(j_num, 'J:29022')
        self.assertEqual(cite.text, 'Ignatjeva L, Mouse Genome 1993;91(2):314')
        self.assertEqual(evid, 'string:52280')
        self.assertEqual(sex_abbrev, 'string:NA')
        self.assertEqual(mod_by, 'hdene')
        self.assertEqual(mod_date, '2007-09-27')
        self.assertEqual(create_by, 'hdene')
        self.assertEqual(create_date, '2007-09-27')

    def testMPEvidenceSearch(self):
        """
        @Status tests that a basic MP Evidence Code search works
        @see pwi-mp-search-10
        """
        driver = self.driver
        #finds the Evidence Code field and select and evidence code then Tabs out of the field
        driver.find_element(By.ID, "evidenceAbbreviation-0").send_keys('NAS')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'termID-3')))
        #find the search results table thirteenth row of data
        term0 = driver.find_element(By.ID, 'termID-12').get_property('value')
        print(term0)
        voc_term = driver.find_elements(By.CLASS_NAME, 'term')[12]
        print(voc_term.text)
        qualfy = driver.find_element(By.ID, 'qualifierAbbreviation-12').get_property('value')#value should be 'string:2181423' that equals (none)
        print(qualfy)
        j_num = driver.find_element(By.ID, 'jnumID-12').get_property('value')
        print(j_num)
        cite = driver.find_elements(By.CLASS_NAME, 'short_citation')[12]
        print(cite.text)
        evid = driver.find_element(By.ID, 'evidenceAbbreviation-12').get_property('value')#value should be "string:6126026" which is NAS
        print(evid)
        sex_abbrev = driver.find_element(By.ID, 'sexAbbreviation-12').get_property('value')#value should be "string:NA"
        print(sex_abbrev)
        mod_by = driver.find_element(By.ID, 'modifiedBy-12').get_property('value')
        print(mod_by)
        mod_date = driver.find_element(By.ID, 'modifiedDate-12').get_property('value')
        print(mod_date)
        create_by = driver.find_element(By.ID, 'createdBy-12').get_property('value')
        print(create_by)
        create_date = driver.find_element(By.ID, 'createdDate-12').get_property('value')
        print(create_date)
        #we are asserting the thirteenth row of data is correct
        self.assertEqual(term0, 'MP:0011099')
        self.assertEqual(voc_term.text, 'lethality throughout fetal growth and development, complete penetrance')
        self.assertEqual(qualfy, 'string:2181423')
        self.assertEqual(j_num, 'J:163428')
        self.assertEqual(cite.text, 'Yu L, J Exp Med 2010 Jun 7;207(6):1183-95')
        self.assertEqual(evid, 'string:6126026')
        self.assertEqual(sex_abbrev, 'string:NA')
        self.assertEqual(mod_by, 'rbabiuk')
        self.assertEqual(mod_date, '2011-05-04')
        self.assertEqual(create_by, 'smb')
        self.assertEqual(create_date, '2010-09-15')

    def testMPSexSearch(self):
        """
        @Status tests that a basic MP Sex search works
        @see pwi-mp-search-11
        """
        driver = self.driver
        #finds the Sex field and select a sex code then clicks the Search button
        driver.find_element(By.ID, "sexAbbreviation-0").send_keys('M')
        time.sleep(2)
        actions = ActionChains(driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID, 'searchButton').click()
        #waits until the element is located or 10 seconds
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'termID-3')))
        #find the search results table first row of data
        term0 = driver.find_element(By.ID, 'termID-0').get_property('value')
        print(term0)
        voc_term = driver.find_element(By.CLASS_NAME, 'term')
        print(voc_term.text)
        qualfy = driver.find_element(By.ID, 'qualifierAbbreviation-0').get_property('value')#value should be 'string:2181424' that equals (norm)
        print(qualfy)
        j_num = driver.find_element(By.ID, 'jnumID-0').get_property('value')
        print(j_num)
        cite = driver.find_elements(By.CLASS_NAME, 'short_citation')[0]
        print(cite.text)
        evid = driver.find_element(By.ID, 'evidenceAbbreviation-0').get_property('value')#value should be "string:52280" which is EXP
        print(evid)
        sex_abbrev = driver.find_element(By.ID, 'sexAbbreviation-0').get_property('value')#value should be "string:M"
        print(sex_abbrev)
        mod_by = driver.find_element(By.ID, 'modifiedBy-0').get_property('value')
        print(mod_by)
        mod_date = driver.find_element(By.ID, 'modifiedDate-0').get_property('value')
        print(mod_date)
        create_by = driver.find_element(By.ID, 'createdBy-0').get_property('value')
        print(create_by)
        create_date = driver.find_element(By.ID, 'createdDate-0').get_property('value')
        print(create_date)
        #we are asserting the thirteenth row of data is correct
        self.assertEqual(term0, 'MP:0003631')
        self.assertEqual(voc_term.text, 'nervous system phenotype')
        self.assertEqual(qualfy, 'string:2181424')
        self.assertEqual(j_num, 'J:13773')
        self.assertEqual(cite.text, 'Taylor BA, Mouse News Lett 1978;59():25')
        self.assertEqual(evid, 'string:52280')
        self.assertEqual(sex_abbrev, 'string:M')
        self.assertEqual(mod_by, 'csmith')
        self.assertEqual(mod_date, '2005-03-11')
        self.assertEqual(create_by, 'csmith')
        self.assertEqual(create_date, '2005-03-11')



    def testMpannotCreateBySearch(self):
        """
        @Status tests that an MP annotation search using the Created By field returns correct data
        @see pwi-mp-date-search-1 
        """
        driver = self.driver
        #find the Modified By field and enter the user name
        driver.find_element(By.ID, "createdBy-0").send_keys("honda")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
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
        #Assert the correct genotype has been returned in the results table
        self.assertEqual(cell0.text, '129P2/OlaHsd-Jmjd6<Gt(RRJ099)Byg> Jmjd6<Gt(RRJ099)Byg>,Jmjd6<Gt(RRJ099)Byg>')
        self.assertEqual(cell1.text, '129S1.Cg-Mgrn1<md-nc> Mgrn1<md-nc>,Mgrn1<md-nc>')
        self.assertEqual(cell2.text, '129S1/SvImJ-Ubr3<tm1Ytkw> Ubr3<tm1Ytkw>,Ubr3<tm1Ytkw>')
        self.assertEqual(cell3.text, '129S4.129P2-Fn1<tm4Hyn> Fn1<tm4Hyn>,Fn1<tm4Hyn>')
        self.assertEqual(cell4.text, '129S6(B6)-Srebf1<tm1Mbr> Srebf1<tm1Mbr>,Srebf1<tm1Mbr>')
        self.assertEqual(cell5.text, '129S6.Cg-Htr2a<tm1Grch> Htr2a<tm2Grch> Emx1<tm1(cre)Ito> Emx1<tm1(cre)Ito>,Emx1<+>,Htr2a<tm1Grch>,Htr2a<tm2Grch>')
        #Assert the correct Creation Name is returned in the Created By field
        createuser = driver.find_element(By.ID, 'createdBy-0').get_attribute('value')
        self.assertEqual(createuser, 'honda')    

    def testMpannotModBySearch(self):
        """
        @Status tests that an image search using the Modified By field returns correct data
        @see pwi-mp-date-search-2 
        """
        driver = self.driver
        #find the Modified By field and enter the user name
        driver.find_element(By.ID, "modifiedBy-0").send_keys("rbabiuk")
        #find the Search button and click it
        driver.find_element(By.ID, 'searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
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
        self.assertEqual(cell2.text, '(B6.129-Crebbp<tm2Pkb> x 129-Crebbp<tm2Pkb>)F1 Crebbp<tm2Pkb>,Crebbp<tm2Pkb>')
        self.assertEqual(cell3.text, '(C3H/HeH x 101/H)F1 Fnld')
        self.assertEqual(cell4.text, '(C57BL/6 x DBA/2)F1 H2<b>,H2<d>')
        self.assertEqual(cell5.text, '(C57BL/6 x FVB/N)F1 Tg(APP)6209Kha')
        #Assert the correct Modified By Name is returned in the Modified By field
        moduser = driver.find_element(By.ID, 'modifiedBy-0').get_attribute('value')
        self.assertEqual(moduser, 'rbabiuk')        

    def testMpannotCreateDateSearch(self):
        """
        @Status tests that a basic Creation Date search works
        @see pwi-mp-date-search-3 
        """
        driver = self.driver
        #finds the Creation Date field, enters a Date
        driver.find_element(By.ID, "createdDate-0").send_keys("2009-09-03")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
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
        self.assertEqual(cell0.text, 'A/J Nrg3<ska>,Nrg3<ska>')
        self.assertEqual(cell1.text, 'B6.Cg-Tg(GFAP-tTA)67Pop Tg(tetO-Ifng)184Pop Tg(GFAP-tTA)67Pop,Tg(tetO-Ifng)184Pop')
        self.assertEqual(cell2.text, 'C3HeB/FeJ-Atp2b2<Obv> Atp2b2<Obv>,Atp2b2<+>')
        self.assertEqual(cell3.text, 'C3HeB/FeJ-Atp2b2<Obv> Atp2b2<Obv>,Atp2b2<Obv>')
        self.assertEqual(cell4.text, 'C57BL/6-Klrk1<tm1.1Bpol> Klrk1<tm1.1Bpol>,Klrk1<tm1.1Bpol>')
        self.assertEqual(cell5.text, 'involves: 129S/SvEv * C57BL/6 * DBA/2 Stat1<tm1Rds>,Stat1<tm1Rds>,Tg(GFAP-tTA)67Pop,Tg(tetO-Ifng)184Pop')
        #Assert the correct Creation Name is returned in the Creation Date field
        createdate = driver.find_element(By.ID, 'createdDate-0').get_attribute('value')
        self.assertEqual(createdate, '2009-09-03')        
             
    def testMpannotModifyDateSearch(self):
        """
        @Status tests that a basic Modification Date search works
        @see pwi-mp-date-search-4 
        """
        driver = self.driver
        #finds the Modification Date field, enters a Date
        driver.find_element(By.ID, "modifiedDate-0").send_keys("2013-02-08")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        cell2 = table.get_row(2)
        print(cell0.text)
        print(cell1.text)
        print(cell2.text)
        #Assert the correct genotypes have been returned in the results table
        self.assertEqual(cell0.text, 'involves: 129P2/OlaHsd * C57BL/6J Cbs<tm1Unc>,Cbs<tm1Unc>,Tg(CBS)11181Eri')
        self.assertEqual(cell1.text, 'involves: 129S1/Sv * 129X1/SvJ Mthfr<tm1Rzn>,Mthfr<tm1Rzn>')
        self.assertEqual(cell2.text, 'involves: FVB/N Tg(GFAP-tTA)6Hyms,Tg(tetO-HMOX1)6Hyms')
        #Assert the correct Creation Name is returned in the Creation Date field
        modifydate = driver.find_element(By.ID, 'modifiedDate-0').get_attribute('value')
        self.assertEqual(modifydate, '2013-02-08')            
       
    def testMpannotModifyDateLessSearch(self):
        """
        @Status tests that a basic Modification Date by less than works
        @see pwi-mp-date-search-7 
        """
        driver = self.driver
        #finds the Modification Date field, enters a Date with less than symbol
        driver.find_element(By.ID, "modifiedDate-0").send_keys('<2005-09-16')
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct genotypes have been returned in the results table
        self.assertEqual(cell0.text, '(129/Sv x BALB/c)F1 Slc11a1<r>,Slc11a1<s>')
        self.assertEqual(cell1.text, '(129P2/Ola x BALB/c)F1 Cbx2<tm1Cim>,Cbx2<tm1Cim>')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element(By.ID, 'modifiedDate-0').get_attribute('value')
        self.assertEqual(modifydate, '2003-11-26')        

    def testMpannotModifyDateLessEqualSearch(self):
        """
        @Status tests that a basic Modification Date by less than equals works
        @see pwi-mp-date-search-8 
        """
        driver = self.driver
        #finds the Modification Date field, enters a Date with less than symbol
        driver.find_element(By.ID, "modifiedDate-0").send_keys('<=2003-04-16')
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct gentypes have been returned in the results table
        self.assertEqual(cell0.text, '(BALB/c x 129)F1 Tz,Tz<+>')
        self.assertEqual(cell1.text, '129S/SvEv-Nodal<TgR(MPSVNeo)413.dRob> Nodal<TgR(MPSVNeo)413.dRob>,Nodal<TgR(MPSVNeo)413.dRob>')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element(By.ID, 'modifiedDate-0').get_attribute('value')
        self.assertEqual(modifydate, '2003-04-16')        
      
    def testMpannotModifyDateRangeSearch(self):
        """
        @Status tests that a basic Modification Date by range search works
        @see pwi-mp-date-search-9 
        """
        driver = self.driver
        #finds the Modification Date field, enters a range of Dates
        driver.find_element(By.ID, "modifiedDate-0").send_keys("2019-05-08..2019-05-09")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct genotypes have been returned in the results table
        self.assertEqual(cell0.text, 'B6.Cg-Atg16l1<tm1Kuv> Tg(Vil1-cre)997Gum Atg16l1<tm1Kuv>,Atg16l1<tm1Kuv>,Tg(Vil1-cre)997Gum')
        self.assertEqual(cell1.text, 'B6.Cg-Atg16l1<tm1Kuv> Xbp1<tm2Glm> Tg(Vil1-cre)997Gum Atg16l1<tm1Kuv>,Atg16l1<tm1Kuv>,Tg(Vil1-cre)997Gum,Xbp1<tm2Glm>,Xbp1<tm2Glm>')
        #Assert the correct Modification Date is returned in the Modification Date field
        modifydate = driver.find_element(By.ID, 'modifiedDate-0').get_attribute('value')
        self.assertEqual(modifydate, '2019-05-08')  
       
    def testMpannotCreateDateLessSearch(self):
        """
        @Status tests that a basic Creation Date by less than works
        @see pwi-mp-date-search-12 
        """
        driver = self.driver
        #finds the Creation Date field, enters a Date with less than symbol
        driver.find_element(By.ID, "createdDate-0").send_keys('<2005-09-13')
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct genotypes have been returned in the results table
        self.assertEqual(cell0.text, '(129/Sv x BALB/c)F1 Slc11a1<r>,Slc11a1<s>')
        self.assertEqual(cell1.text, '(129/Sv x C57BL/6J)F1 Slc11a1<s>,Slc11a1<r>')
        #Assert the correct Creation Date is returned in the Modification Date field
        modifydate = driver.find_element(By.ID, 'createdDate-0').get_attribute('value')
        self.assertEqual(modifydate, '2003-11-26')        

    def testMpannotCreateDateLessEqualSearch(self):
        """
        @Status tests that a basic Creation Date by less than equals works
        @see pwi-mp-date-search-13 
        """
        driver = self.driver
        #finds the Creation Date field, enters a Date with less than symbol
        driver.find_element(By.ID, "createdDate-0").send_keys('<=2002-03-28')
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct genotypes have been returned in the results table
        self.assertEqual(cell0.text, '129P2/OlaHsd-Prnp<tm1Edin>/EdinH Prnp<tm1Edin>,Prnp<tm1Edin>')
        self.assertEqual(cell1.text, '129P2/OlaHsd-Prnp<tm1Rcm> Prnp<tm1Rcm>,Prnp<tm1Rcm>')
        #Assert the correct Creation Date is returned in the Creation Date field
        createdate = driver.find_element(By.ID, 'createdDate-0').get_attribute('value')
        self.assertEqual(createdate, '2002-03-20')        
      
    def testMpannotCreateDateRangeSearch(self):
        """
        @Status tests that a basic Creation Date by range search works
        @see pwi-mp-date-search-14 
        """
        driver = self.driver
        #finds the Creation Date field, enters a range of Dates
        driver.find_element(By.ID, "createdDate-0").send_keys("2002-03-28..2002-03-29")
        #finds the Search button and clicks it
        driver.find_element(By.ID, 'searchButton').click()
        #wait until the Results list is displayed on the page    
        wait.forAngular(self.driver)
        #find the search results table
        results_table = self.driver.find_element(By.ID, "resultsTable")
        table = Table(results_table)
        # get and print the first 2 rows
        cell0 = table.get_row(0)
        cell1 = table.get_row(1)
        print(cell0.text)
        print(cell1.text)
        #Assert the correct genotypes have been returned in the results table
        self.assertEqual(cell0.text, 'B6.129S4-Mdfi<tm1Krt> Mdfi<tm1Krt>,Mdfi<tm1Krt>')
        self.assertEqual(cell1.text, 'B6EiC3Sn a/A-Egfr<wa2> Wnt3a<vt>/J Egfr<wa2>,Egfr<wa2>')
        #Assert the correct Creation Date is returned in the Creation Date field
        createdate = driver.find_element(By.ID, 'createdDate-0').get_attribute('value')
        self.assertEqual(createdate, '2002-03-28')                  

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiMpannotSearch))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
    