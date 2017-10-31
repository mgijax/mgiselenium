'''
Created on Nov 22, 2016
These tests start out using the Marker form
@author: jeffc
'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,os.path
from util import wait, iterate
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import TEST_PWI_URL

class TestLitIndexByMrk(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() 

    def test_disease_annotations(self):
        """
        @status: Tests that the disease annotations section is correct, this section now has both OMIM and DO annotations. Does not capture  the term NOT setting.
        @bug data has changed so the results are now no longer the same, needs verification of data and then test changes!!!
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/#markerForm')
        
        nomenbox = driver.find_element_by_id('nomen')
        # put your marker symbol in the box
        nomenbox.send_keys("pax6")
        nomenbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the marker link and clicks it
        driver.find_element_by_link_text("Pax6").click()
        time.sleep(3)
        driver.find_element_by_link_text("Alleles").click()
        time.sleep(5)
        driver.find_element_by_partial_link_text("Sey-Dey").click()
        time.sleep(5)
        #Locates the summary table and finds the table headings
        driver.find_element_by_css_selector('div.genotypeDetail:nth-child(3)')
        driver.find_element_by_css_selector('dl.detailPageListData:nth-child(1)')
        driver.find_elements_by_tag_name('dd.detailPageListData')
        data = driver.find_elements_by_tag_name('a')
        #print iterate.getTextAsList(data)#prints out almost all data found on this page, hopefully someday  I can figure out how to capture just the disease annotations section.
        time.sleep(5)
        term1 = data[59]
        id1 = data[60]
        ref1 = data[61]
        term2 = data[62]
        id2 = data[63]
        ref2 = data[64]
        term3 = data[65]
        id3 = data[66]
        ref3 = data[67]
        term4 = data[68]
        id4 = data[69]
        ref4 = data[70]
        term5 = data[71]
        id5 = data[72]
        ref5 = data[73]
        term6 = data[74]
        id6 = data[75]
        ref6 = data[76]
        term7 = data[77]
        id7 = data[78]
        ref7 = data[79]
        term8 = data[80]
        id8 = data[81]
        ref8 = data[82]
        #asserts that all the disease annotations are correct, but does not capture if a term is a NOT!
        self.assertEqual(term1.text, "Aniridia 1; AN1")
        self.assertEqual(id1.text, "OMIM:106210")
        self.assertEqual(ref1.text, "J:10820")
        self.assertEqual(term2.text, "Wilms Tumor, Aniridia, Genitourinary Anomalies, and Mental Retardation Syndrome; WAGR")
        self.assertEqual(id2.text, "OMIM:194072")
        self.assertEqual(ref2.text, "J:10820")
        self.assertEqual(term3.text, "Peters Anomaly")
        self.assertEqual(id3.text, "OMIM:604229")
        self.assertEqual(ref3.text, "J:10820")
        self.assertEqual(term4.text, "ptosis")
        self.assertEqual(id4.text, "DOID:0060260")
        self.assertEqual(ref4.text, "J:116600")  
        self.assertEqual(term5.text, "Peters anomaly")
        self.assertEqual(id5.text, "DOID:0060673")
        self.assertEqual(ref5.text, "J:10820") 
        self.assertEqual(term6.text, "aniridia")
        self.assertEqual(id6.text, "DOID:12271")
        self.assertEqual(ref6.text, "J:10820") 
        self.assertEqual(term7.text, "WAGR syndrome")
        self.assertEqual(id7.text, "DOID:14515")
        self.assertEqual(ref7.text, "J:10820") 
        self.assertEqual(term8.text, "uveal disease")
        self.assertEqual(id8.text, "DOID:3480")
        self.assertEqual(ref8.text, "J:116600")       
        #print searchTextItems
        #verifies all the table headings are correct and in order
        #self.assertEqual(searchTextItems, ['*','Reference','Priority','Conditional'])
        print "Current working dir : %s" % os.getcwd()
        
    def test_page_sort(self):
        """
        @status: Tests that the default page sort is correct
        sort is by no particular order?
        """
        driver = self.driver
        #opens the PWI marker form
        driver.get(TEST_PWI_URL + '/#markerForm')
        
        nomenbox = driver.find_element_by_id('nomen')
        # put your marker symbol in the box
        nomenbox.send_keys("gata1")
        nomenbox.send_keys(Keys.RETURN)
        time.sleep(3)
        #finds the marker link and clicks it
        driver.find_element_by_link_text("Gata1").click()
        wait.forAjax(driver)
        driver.find_element_by_link_text("Lit Index").click()
        wait.forAjax(driver)
        #finds the coded column and then the first 10 items
        refindextable = driver.find_element_by_id("indexRefsTable")
        coded = refindextable.find_elements_by_css_selector('td:nth-child(1)')
        code1 = coded[0]
        code2 = coded[1]
        code3 = coded[2]
        code4 = coded[3]
        code5 = coded[4]
        code6 = coded[5]
        code7 = coded[6]
        code8 = coded[7]
        code9 = coded[8]
        code10 = coded[9]
        #asserts the first 10 coded labels are correct and in correct order
        self.assertEqual(code1.text, "*")
        self.assertEqual(code2.text, "")
        self.assertEqual(code3.text, "")
        self.assertEqual(code4.text, "")
        self.assertEqual(code5.text, "")
        self.assertEqual(code6.text, "")
        self.assertEqual(code7.text, "")
        self.assertEqual(code8.text, "*")
        self.assertEqual(code9.text, "")
        self.assertEqual(code10.text, "")
        #finds the priority column and then the first 10 items
        refindextable = driver.find_element_by_id("indexRefsTable")
        priority = refindextable.find_elements_by_css_selector('td:nth-child(3)')
        pri1 = priority[0]
        pri2 = priority[1]
        pri3 = priority[2]
        pri4 = priority[3]
        pri5 = priority[4]
        pri6 = priority[5]
        pri7 = priority[6]
        pri8 = priority[7]
        pri9 = priority[8]
        pri10 = priority[9]
        #asserts the first 10 priority labels are correct and in correct order
        self.assertEqual(pri1.text, "High")
        self.assertEqual(pri2.text, "Low")
        self.assertEqual(pri3.text, "High")
        self.assertEqual(pri4.text, "High")
        self.assertEqual(pri5.text, "High")
        self.assertEqual(pri6.text, "Medium")
        self.assertEqual(pri7.text, "Medium")
        self.assertEqual(pri8.text, "Low")
        self.assertEqual(pri9.text, "Medium")
        self.assertEqual(pri10.text, "High")
        
        #finds the conditional column and then the first 10 items
        refindextable = driver.find_element_by_id("indexRefsTable")
        cond = refindextable.find_elements_by_css_selector('td:nth-child(4)')
        con1 = cond[0]
        con2 = cond[1]
        con3 = cond[2]
        con4 = cond[3]
        con5 = cond[4]
        con6 = cond[5]
        con7 = cond[6]
        con8 = cond[7]
        con9 = cond[8]
        con10 = cond[9]
        #asserts the first 10 conditional labels are correct and in correct order
        self.assertEqual(con1.text, "Not Specified")
        self.assertEqual(con2.text, "Not Specified")
        self.assertEqual(con3.text, "Conditional")
        self.assertEqual(con4.text, "Not Applicable")
        self.assertEqual(con5.text, "Conditional")
        self.assertEqual(con6.text, "Not Specified")
        self.assertEqual(con7.text, "Not Specified")
        self.assertEqual(con8.text, "Not Specified")
        self.assertEqual(con9.text, "Not Applicable")
        self.assertEqual(con10.text, "Not Applicable")
        

    def tearDown(self):
        self.driver.close()
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLitIndexByMrk))
    return suite

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSpecSumByRef']
    unittest.main()