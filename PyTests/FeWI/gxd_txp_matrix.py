'''
Created on Jan 24, 2018
@author: jeffc
@attention: Beginning  tests for Tissue X Phenotype Matrix
'''

import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import iterate
import config

class TestGXDTissuePhenotypeMatrix(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()

    def test_mp_emapa_single_system(self):
        """
        @status: Tests that an MP to EMAPA  maps to a single anatomy system
        @note: GXD-TxP-5
        @attention: the time sleeps need to be replaced by expected conditions code
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/marker')
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('Foxe1')
        self.driver.find_element(By.NAME, 'submit').click()
        time.sleep(1)
        #find the marker link and click it
        driver.find_element(By.LINK_TEXT, 'Foxe1').click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        time.sleep(2)
        #click the Gene Expression + Phenotype link
        driver.find_element(By.LINK_TEXT, 'Gene Expression + Phenotype').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #find the Anatomical Terms column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('mouse', searchTextItems)
        self.assertIn('body region', searchTextItems)
        self.assertIn('conceptus', searchTextItems)
        self.assertIn('embryo', searchTextItems)
        self.assertIn('germ layer', searchTextItems)
        self.assertIn('organ', searchTextItems)
        self.assertIn('organ system', searchTextItems)
        self.assertIn('tissue', searchTextItems)
        #find the Phenotypes Terms column
        termslist = driver.find_element(By.ID, 'colGroupInner')
        items = termslist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('Foxe1<tm1Rdl>/Foxe1<tm1Rdl>', searchTextItems)
        #find the phenotype grid box for endocrine system for Foxe1<tm1Rdl>/Foxe1<tm1Rdl>
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row9.col1 > rect.phenoBlue1')
        rightclass = item.get_attribute('class')
        #rightclass finds the class name of the gridbox
        #now we assert the class name of the gridbox matches the class name of phenoBlue1
        self.assertEqual(rightclass, 'phenoBlue1')
        
    def test_mp_emapa_multi_geno(self):
        """
        @status: Tests the display when an MP term is annotated to multiple genotypes using different J numbers, each counted as 1 annotation
        @note: GXD-Txp-7
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/marker')
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('Pax4')
        self.driver.find_element(By.NAME, 'submit').click()
        time.sleep(2)
        #find the marker link and click it
        driver.find_element(By.LINK_TEXT, 'Pax4').click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        time.sleep(2)
        #click the Gene Expression + Phenotype link
        driver.find_element(By.LINK_TEXT, 'Gene Expression + Phenotype').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        #find the Anatomical Terms column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('mouse', searchTextItems)
        self.assertIn('hemolymphoid system', searchTextItems)
        self.assertIn('hematopoietic system', searchTextItems)
        #find the Phenotypes Terms column
        termslist = driver.find_element(By.ID, 'colGroupInner')
        items = termslist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('Pax4<tm1b(EUCOMM)Hmgu>/Pax4<+>', searchTextItems)
        #find the phenotype grid box for hemolymphoid system for Pax4<tm1b(EUCOMM)Hmgu>/Pax4<+>
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row13.col3 > rect.phenoBlue2')
        rightclass = item.get_attribute('class')
        #rightclass finds the class name of the gridbox
        #now we assert the class name of the gridbox matches the class name of blue2
        self.assertEqual(rightclass, 'phenoBlue2')
        #find the phenotype grid box for hematopoietic system for Pax4<tm1b(EUCOMM)Hmgu>/Pax4<+>
        boxlist1 = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist1.find_element(By.CSS_SELECTOR, 'g.cell.row12.col3 > rect.phenoBlue2')
        rightclass1 = item.get_attribute('class')
        #rightclass1 finds the class name of the gridbox
        #now we assert the class name of the gridbox matches the class name of phenoBlue1
        self.assertEqual(rightclass1, 'phenoBlue2')        
                
    def test_mp_emapa_child(self):
        """
        @status: Tests the display when an MP annotation maps to a child of mouse but has no GXD annotation
        @note: GXD-TxP-8
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/marker')
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('Avp')
        self.driver.find_element(By.NAME, 'submit').click()
        time.sleep(2)
        #find the marker link and click it
        driver.find_element(By.LINK_TEXT, 'Avp').click()
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        time.sleep(2)
        #click the Gene Expression + Phenotype link
        self.driver.find_element(By.LINK_TEXT, 'Gene Expression + Phenotype').click()
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        #find the Anatomical Terms column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('mouse', searchTextItems)
        self.assertIn('body fluid or substance', searchTextItems)
        #find the Phenotypes Terms column
        termslist = driver.find_element(By.ID, 'colGroupInner')
        items = termslist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('Avp<tm1Hari>/Avp<+>', searchTextItems)
        #find the phenotype grid box for body fluid or substance for Avp<tm1Hari>/Avp<+>
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row1.col2 > rect.phenoBlue1')
        rightclass = item.get_attribute('class')
        #rightclass finds the class name of the gridbox
        #now we assert the class name of the gridbox matches the class name of phenoBlue1
        self.assertEqual(rightclass, 'phenoBlue1')
        
    def test_mp_emapa_jnum_diff(self):
        """
        @status: Tests the display when MP term annotated to multiple genotypes with the same J number, each occurance counted as 1 annotation
        @note: GXD-TxP-11
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/marker')
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('Bmp15')
        self.driver.find_element(By.NAME, 'submit').click()
        time.sleep(2)
        #find the marker link and click it
        driver.find_element(By.LINK_TEXT, 'Bmp15').click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        time.sleep(2)
        #click the Gene Expression + Phenotype link
        driver.find_element(By.LINK_TEXT, 'Gene Expression + Phenotype').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #find the Anatomical Terms column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('mouse', searchTextItems)
        self.assertIn('conceptus', searchTextItems)
        #find the Phenotypes Terms column
        termslist = driver.find_element(By.ID, 'colGroupInner')
        items = termslist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('Bmp15<tm1Zuk>/Bmp15<tm1Zuk>', searchTextItems)
        #find the phenotype grid box for conceptus for Bmp15<tm1Zuk>/Bmp15<tm1Zuk>
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row2.col1 > rect.phenoBlue2')
        rightclass = item.get_attribute('class')
        #rightclass finds the class name of the gridbox
        #now we assert the class name of the gridbox matches the class name of phenoBlue2
        self.assertEqual(rightclass, 'phenoBlue2')
        
    
    def test_multi_mp_same_emapa(self):
        """
        @status: Tests the display for multiple MP annotations using different rollup to same EMAPA term with same genocluster. each occurance counted as 1 annotation
        @note: GXD-TxP-12
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/marker')
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('Foxe1')
        self.driver.find_element(By.NAME, 'submit').click()
        time.sleep(2)
        #find the marker link and click it
        driver.find_element(By.LINK_TEXT, 'Foxe1').click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        time.sleep(2)
        #click the Gene Expression + Phenotype link
        driver.find_element(By.LINK_TEXT, 'Gene Expression + Phenotype').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #find the Anatomical Terms column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('mouse', searchTextItems)
        self.assertIn('integumental system', searchTextItems)
        #find the Phenotypes Terms column
        termslist = driver.find_element(By.ID, 'colGroupInner')
        items = termslist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('Foxe1<tm1Rdl>/Foxe1<tm1Rdl>', searchTextItems)
        #find the phenotype grid box for integumental system system for Foxe1<tm1Rdl>/Foxe1<tm1Rdl>
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row15.col1 > rect.phenoBlue3')
        rightclass = item.get_attribute('class')
        #rightclass finds the class name of the gridbox
        #now we assert the class name of the gridbox matches the class name of phenoBlue3
        self.assertEqual(rightclass, 'phenoBlue3')
            
    def test_norm_mp_only(self):
        """
        @status: Tests the display when a normal MP annotation is the only annotation for a row/cell(7 cells), it also verifies that normals have an N in their cells
        @note: GXD-TxP-16
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/marker')
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('Bmp15')
        self.driver.find_element(By.NAME, 'submit').click()
        time.sleep(2)
        #find the marker link and click it
        driver.find_element(By.LINK_TEXT, 'Bmp15').click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        time.sleep(2)
        #click the Gene Expression + Phenotype link
        driver.find_element(By.LINK_TEXT, 'Gene Expression + Phenotype').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #find the Anatomical Terms column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('mouse', searchTextItems)
        self.assertIn('conceptus', searchTextItems)
        self.assertIn('embryo', searchTextItems)
        self.assertIn('organ system', searchTextItems)
        self.assertIn('reproductive system', searchTextItems)
        self.assertIn('genitourinary system', searchTextItems)
        self.assertIn('visceral organ system', searchTextItems)
        #find the Phenotypes Terms column
        termslist = driver.find_element(By.ID, 'colGroupInner')
        items = termslist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('Bmp15<tm1Zuk>/Y', searchTextItems)
        #find the phenotype grid box for conceptus for Bmp15<tm1Zuk>/Y
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col2 > rect.phenoBlue1')
        rightclass = item.get_attribute('class')
        celltext = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col2 > text')#locates the text in the box to verify it has an N
        item1 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row2.col2 > rect.phenoBlue1')
        rightclass1 = item1.get_attribute('class')
        celltext1 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row2.col2 > text')#locates the text in the box to verify it has an N
        item2 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row4.col2 > rect.phenoBlue1')
        rightclass2 = item2.get_attribute('class')
        celltext2 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row4.col2 > text')#locates the text in the box to verify it has an N
        item3 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row7.col2 > rect.phenoBlue1')
        rightclass3 = item3.get_attribute('class')
        celltext3 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row7.col2 > text')#locates the text in the box to verify it has an N
        item4 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row12.col2 > rect.phenoBlue1')
        rightclass4 = item4.get_attribute('class')
        celltext4 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row12.col2 > text')#locates the text in the box to verify it has an N
        item5 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row20.col2 > rect.phenoBlue1')
        rightclass5 = item5.get_attribute('class')
        celltext5 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row20.col2 > text')#locates the text in the box to verify it has an N
        item6 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row24.col2 > rect.phenoBlue1')
        rightclass6 = item6.get_attribute('class')
        celltext6 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row24.col2 > text')#locates the text in the box to verify it has an N
        #rightclass finds the class name of the gridbox for the 7 anatomical terms pheno box for the allele
        #now we assert the class name of the gridbox matches the class name of phenoBlue1
        self.assertEqual(rightclass, 'phenoBlue1')
        self.assertEqual(celltext.text, 'N')
        self.assertEqual(rightclass1, 'phenoBlue1')
        self.assertEqual(celltext1.text, 'N')
        self.assertEqual(rightclass2, 'phenoBlue1')
        self.assertEqual(celltext2.text, 'N')
        self.assertEqual(rightclass3, 'phenoBlue1')
        self.assertEqual(celltext3.text, 'N')
        self.assertEqual(rightclass4, 'phenoBlue1')
        self.assertEqual(celltext4.text, 'N')
        self.assertEqual(rightclass5, 'phenoBlue1')
        self.assertEqual(celltext5.text, 'N')
        self.assertEqual(rightclass6, 'phenoBlue1')
        self.assertEqual(celltext6.text, 'N')
        
              
    def test_norm_mp_other_mp(self):
        """
        @status: Tests the display when you have a normal MP annotation and another annotation that roll up to a higher level term, but no N gets displayed
        @note: GXD-TxP-17 currently this test is broken, ask connie  why this allele is now gone.
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/marker')
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('Pax7')
        self.driver.find_element(By.NAME, 'submit').click()
        time.sleep(2)
        #find the marker link and click it
        driver.find_element(By.LINK_TEXT, 'Pax7').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        time.sleep(2)
        #click the Gene Expression + Phenotype link
        driver.find_element(By.LINK_TEXT, 'Gene Expression + Phenotype').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #find the Anatomical Terms column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('musculoskeletal system', searchTextItems)
        self.assertIn('musculature', searchTextItems)
        #find the Phenotypes Terms column
        termslist = driver.find_element(By.ID, 'colGroupInner')
        items = termslist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('Pax7<tm1Pgr>/Pax7<tm1Pgr>', searchTextItems)
        #find the phenotype grid box for musculoskeletal system for Pax7<tm1.1(HBEGF,-EYFP)Mal/Pax7<+>
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row20.col3> rect.phenoBlue2')
        rightclass = item.get_attribute('class')
        #rightclass finds the class name of the gridbox
        #now we assert the class name of the gridbox matches the class name of phenoBlue2
        self.assertEqual(rightclass, 'phenoBlue2')
        
    def test_bkgrnd_sense_mp(self):
        """
        @status: Tests the display when an MP annotation is the only annotation for a row/cell that shows background sensitivity
        @note: GXD-TxP-18
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/marker')
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('Kras')
        self.driver.find_element(By.NAME, 'submit').click()
        time.sleep(2)
        #find the marker link and click it
        driver.find_element(By.LINK_TEXT, 'Kras').click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        time.sleep(2)
        #click the Gene Expression + Phenotype link
        driver.find_element(By.LINK_TEXT, 'Gene Expression + Phenotype').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        #find the Anatomical Terms column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('mouse', searchTextItems)
        self.assertIn('integumental system', searchTextItems)
        #find the Phenotypes Terms column
        termslist = driver.find_element(By.ID, 'colGroupInner')
        items = termslist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('Kras<tm2Tyj>/Kras<+>', searchTextItems)
        #find the phenotype grid box for integumental system for Kras<tm2Tyj>/Kras<+>
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row19.col7 > rect.phenoBlue2')
        rightclass = item.get_attribute('class')
        celltext = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row19.col7 > text')#locates the text in the box to verify it has a !
        #rightclass finds the class name of the gridbox for the anatomical terms pheno box for the allele
        #now we assert the class name of the gridbox matches the class name of phenoBlue2
        self.assertEqual(rightclass, 'phenoBlue2')
        self.assertEqual(celltext.text, '!')
        
    def test_bkgrnd_sense_and_normal(self):
        """
        @status: Tests the display when a normal MP annotation with background sensitivity, is the only annotation for a row/cell(7 cells)
        @note: GXD-TxP-21
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/marker')
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('Sry')
        self.driver.find_element(By.NAME, 'submit').click()
        time.sleep(2)
        #find the marker link and click it
        driver.find_element(By.LINK_TEXT, 'Sry').click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        time.sleep(2)
        #click the Gene Expression + Phenotype link
        driver.find_element(By.LINK_TEXT, 'Gene Expression + Phenotype').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        #find the Anatomical Terms column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        #verifies that these 7 anatomy terms are displayed
        self.assertIn('mouse', searchTextItems)
        self.assertIn('conceptus', searchTextItems)
        self.assertIn('embryo', searchTextItems)
        self.assertIn('organ system', searchTextItems)
        self.assertIn('reproductive system', searchTextItems)
        self.assertIn('genitourinary system', searchTextItems)
        self.assertIn('visceral organ system', searchTextItems)
        #find the Phenotypes Terms column
        termslist = driver.find_element(By.ID, 'colGroupInner')
        items = termslist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        #verifies the allele pair you want to use is listed in the header
        self.assertIn('X/Sry<AKR/J>Sry<RIII>', searchTextItems)
        #find the phenotype grid boxs for mouse, conceptus, embryo, organ system, reproductive system, genitourinary system and visceral organ system  for X/Sry<AKR/J>Sry<RIII>
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col1 > rect.phenoBlue1')
        rightclass = item.get_attribute('class')
        celltext = boxlist.find_elements(By.CSS_SELECTOR, 'g.cell.row0.col1 > text')#locates the text in the box to verify it has an N!
        searchTextItems0 = iterate.getTextAsList(celltext)
        print(searchTextItems0)
        #verifies both an N and a ! is displayed in the mouse/phenotype box
        self.assertEqual(['N', '!'], searchTextItems0)
        self.assertEqual('phenoBlue1', rightclass)
        item1 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col1 > rect.phenoBlue1')
        rightclass1 = item1.get_attribute('class')
        celltext1 = boxlist.find_elements(By.CSS_SELECTOR, 'g.cell.row0.col1 > text')#locates the text in the box to verify it has an N!
        searchTextItems1 = iterate.getTextAsList(celltext1)
        print(searchTextItems1)
        #verifies both an N and a ! is displayed in the conceptus/phenotype box
        self.assertEqual(['N', '!'], searchTextItems1)
        self.assertEqual('phenoBlue1', rightclass1)
        item2 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row2.col1 > rect.phenoBlue1')
        rightclass2 = item2.get_attribute('class')
        celltext2 = boxlist.find_elements(By.CSS_SELECTOR, 'g.cell.row2.col1 > text')#locates the text in the box to verify it has an N!
        searchTextItems2 = iterate.getTextAsList(celltext2)
        print(searchTextItems2)
        #verifies both an N and a ! is displayed in the embryo/phenotype box
        self.assertEqual(['N', '!'], searchTextItems2)
        self.assertEqual('phenoBlue1', rightclass2)
        item3 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row3.col1 > rect.phenoBlue1')
        rightclass3 = item3.get_attribute('class')
        celltext3 = boxlist.find_elements(By.CSS_SELECTOR, 'g.cell.row3.col1 > text')#locates the text in the box to verify it has an N!
        searchTextItems3 = iterate.getTextAsList(celltext3)
        print(searchTextItems3)
        #verifies both an N and a ! is displayed in the organ system/genitourimary system box
        self.assertEqual(['N', '!'], searchTextItems3)
        self.assertEqual('phenoBlue1', rightclass3)
        item4 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row11.col1 > rect.phenoBlue1')
        rightclass4 = item4.get_attribute('class')
        celltext4 = boxlist.find_elements(By.CSS_SELECTOR, 'g.cell.row11.col1 > text')#locates the text in the box to verify it has an N!
        searchTextItems4 = iterate.getTextAsList(celltext4)
        print(searchTextItems4)
        #verifies both an N and a ! is displayed in the reproductive system/phenotype box
        self.assertEqual(['N', '!'], searchTextItems4)
        self.assertEqual('phenoBlue1', rightclass4)
        item5 = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row20.col1 > rect.phenoBlue1')
        rightclass5 = item5.get_attribute('class')
        celltext5 = boxlist.find_elements(By.CSS_SELECTOR, 'g.cell.row20.col1 > text')#locates the text in the box to verify it has an N!
        searchTextItems5 = iterate.getTextAsList(celltext5)
        print(searchTextItems5)
        self.assertEqual(['N', '!'], searchTextItems5)
        self.assertEqual('phenoBlue1', rightclass5)
        
    def test_high_cell_color(self):
        """
        @status: Tests the display when you have more than 100 MP annotations
        @note: GXD-TxP-26
        """
        driver = self.driver
        driver.get(config.TEST_URL + '/marker')
        self.driver.find_element(By.ID, 'searchToolTextArea').clear()
        self.driver.find_element(By.ID, 'searchToolTextArea').send_keys('Lepr')
        self.driver.find_element(By.NAME, 'submit').click()
        time.sleep(2)
        #find the marker link and click it
        driver.find_element(By.LINK_TEXT, 'Lepr').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        time.sleep(2)
        #click the Gene Expression + Phenotype link
        driver.find_element(By.LINK_TEXT, "Gene Expression + Phenotype").click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #find the Anatomical Terms column
        termslist = driver.find_element(By.ID, "rowGroupInner")
        items = termslist.find_elements(By.TAG_NAME, 'text')
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('mouse', searchTextItems)
        #find the Phenotypes Terms column
        termslist = driver.find_element(By.ID, 'colGroupInner')
        items = termslist.find_elements(By.TAG_NAME, "text")
        searchTextItems = iterate.getTextAsList(items)
        print(searchTextItems)
        self.assertIn('Lepr<db>/Lepr<db>', searchTextItems)
        #find the phenotype grid box for mouse for Lepr<db>/Lepr<db>
        boxlist = driver.find_element(By.ID, 'matrixGroupInner').find_element(By.CLASS_NAME, 'matrixCell')
        item = boxlist.find_element(By.CSS_SELECTOR, 'g.cell.row0.col17 > rect.phenoBlue2')
        rightclass = item.get_attribute('class')
        #rightclass finds the class name of the gridbox
        #now we assert the class name of the gridbox matches the class name of phenoBlue2
        self.assertEqual(rightclass, 'phenoBlue2')
                
    def tearDown(self):
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGXDTissuePhenotypeMatrix))
    return suite
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))