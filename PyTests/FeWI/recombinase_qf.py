'''
Created on Apr 5, 2022
Tests features(especially search features) of the Recombinase (CRE) query form
@author: jeffc
'''
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys,os.path
from genericpath import exists
from selenium.webdriver.support.wait import WebDriverWait
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from util import wait, iterate
from util.table import Table
import config
from config import TEST_URL
import time

class TestCreSpecificity(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL + "/home/recombinase")
        self.driver.implicitly_wait(10)

    def test_1structure_detected(self):
        '''
        @status This test verifies that searching by a single structure detected return the correct results.
        @note: Recomb-test-1
        '''
        #find the Anatomical Structure field and enter text
        self.driver.find_element(By.NAME, 'structure_1').send_keys('definitive endoderm')
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'titleBarMainTitle'), 'Recombinase Alleles - Tissue Summary'))
        #find all the results in the Driver column so they can be verified
        driver1 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(1) > div:nth-child(1)')
        print(driver1.text)
        driver2 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec1 > td:nth-child(1) > div:nth-child(1)')
        print(driver2.text)
        driver3 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec2 > td:nth-child(1) > div:nth-child(1)')
        print(driver3.text)
        driver4 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec3 > td:nth-child(1) > div:nth-child(1)')
        print(driver4.text)
        
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('Foxa2', driver1.text, 'driver1 is not correct' )
        self.assertEqual('Krt19', driver2.text, 'driver2 is not correct')
        self.assertEqual('Lhx1', driver3.text, 'driver1 is not correct' )
        self.assertEqual('Sox17', driver4.text, 'driver2 is not correct')

    def test_2structure_detected(self):
        '''
        @status This test verifies that searching by a two structures detected return the correct results.
        @note: Recomb-test-2
        '''
        #find the Anatomical Structure field and enter text
        self.driver.find_element(By.NAME, 'structure_1').send_keys('ductus deferens')
        time.sleep(2)
        #find and click the Add structure button
        self.driver.find_element(By.CLASS_NAME, 'addButton').click()
        #find the new structure field and add a second structure
        self.driver.find_element(By.NAME, 'structure_2').send_keys('pons')
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'titleBarMainTitle'), 'Recombinase Alleles - Tissue Summary'))
        #find all the results in the Driver column so they can be verified
        driver1 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(1) > div:nth-child(1)')
        print(driver1.text)
        
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('EIIA', driver1.text, 'driver1 is not correct' )
     
    def test_2structure_detected_nowhere(self):
        '''
        @status This test verifies that searching by 2 structures detected and no where else return the correct results.
        @note: Recomb-test-3
        '''
        #find the Anatomical Structure field and enter text
        self.driver.find_element(By.NAME, 'structure_1').send_keys('brain stem')
        time.sleep(2)
        #find and click the Add structure button
        self.driver.find_element(By.CLASS_NAME, 'addButton').click()
        #find the new structure field and add a second structure, had  to use elem because autocomplete was not closing and causing nowhereEle box to be clicked.
        elem = self.driver.find_element(By.NAME, 'structure_2')
        elem.send_keys('pons')
        time.sleep(2)
        elem.send_keys(Keys.TAB)
        #click the No where else toggle
        self.driver.find_element(By.NAME, 'nowhereElse').click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'titleBarMainTitle'), 'Recombinase Alleles - Tissue Summary'))
        #find all the results in the Driver column so they can be verified
        driver1 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(1) > div:nth-child(1)')
        print(driver1.text)
        
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('Calca', driver1.text, 'driver1 is not correct' )
        
    def test_1structure_detected_1notdetected(self):
        '''
        @status This test verifies that searching by 2 structures, 1 detected and 1 not detected return the correct results.
        @note: Recomb-test-4
        '''
        #find the Anatomical Structure field and enter text
        self.driver.find_element(By.NAME, 'structure_1').send_keys('ductus deferens')
        time.sleep(2)
        #find and click the Add structure button
        self.driver.find_element(By.CLASS_NAME, 'addButton').click()
        #find the new structure field and add a second structure
        self.driver.find_element(By.NAME, 'structure_2').send_keys('pons')
        time.sleep(2)
        #set the not detected option for the structure pons
        self.driver.find_element(By.XPATH, "//input[@name='detected_2' and @value='false']").click()
        self.driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'titleBarMainTitle'), 'Recombinase Alleles - Tissue Summary'))
        #find all the results in the Driver column so they can be verified
        driver1 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(1) > div:nth-child(1)')
        print(driver1.text)
        driver2 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec1 > td:nth-child(1) > div:nth-child(1)')
        print(driver2.text)
        driver3 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec2 > td:nth-child(1) > div:nth-child(1)')
        print(driver3.text)
        driver4 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec3 > td:nth-child(1) > div:nth-child(1)')
        print(driver4.text)
        driver5 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec4 > td:nth-child(1) > div:nth-child(1)')
        print(driver5.text)
        driver6 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec5 > td:nth-child(1) > div:nth-child(1)')
        print(driver6.text)
        driver7 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec6 > td:nth-child(1) > div:nth-child(1)')
        print(driver7.text)
        
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('Ckm', driver1.text, 'driver1 is not correct' )
        self.assertEqual('Ltf', driver2.text, 'driver2 is not correct')
        self.assertEqual('MMTV', driver3.text, 'driver3 is not correct' )
        self.assertEqual('Myh11', driver4.text, 'driver4 is not correct')                
        self.assertEqual('Pax2', driver5.text, 'driver5 is not correct')
        self.assertEqual('Pbsn', driver6.text, 'driver6 is not correct' )
        self.assertEqual('Prlr', driver7.text, 'driver7 is not correct')
        
    def test_1structure_detected_1notdetecteddriver(self):
        '''
        @status This test verifies that searching by 2 structures, 1 detected and 1 not detected and driven by Ltf return the correct results.
        @note: Recomb-test-5
        '''
        #find the Anatomical Structure field and enter text
        self.driver.find_element(By.NAME, 'structure_1').send_keys('ductus deferens')
        time.sleep(2)
        #find and click the Add structure button
        self.driver.find_element(By.CLASS_NAME, 'addButton').click()
        #find the new structure field and add a second structure
        self.driver.find_element(By.NAME, 'structure_2').send_keys('pons')
        time.sleep(2)
        #set the not detected option for the structure pons
        self.driver.find_element(By.XPATH, "//input[@name='detected_2' and @value='false']").click()
        self.driver.find_element(By.ID, 'creDriverAC').send_keys('Ltf')
        self.driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'titleBarMainTitle'), 'Recombinase Alleles - Tissue Summary'))
        #find all the results in the Driver column so they can be verified
        driver1 = self.driver.find_element(By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(1) > div:nth-child(1)')
        print(driver1.text)
        
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('Ltf', driver1.text, 'driver1 is not correct' )
                
    def test_Matrix_sort(self):
        '''
        @status This test verifies that the sorting order for alleles is correct on Gene Expression + Recombinase Activity Comparison Matrix. 
        Order should be:
        1. GXD expression column first
        2. Alleles with mouse drivers next, then human, then rat, then others, Not specified last
        3. Within each group, targeted before Endonuclease-mediated then transgenic
        4. Within each of these, smart alpha on allele symbol
        @note: Recomb-drvr-2
        '''
        #find the Recombinase driven by field and enter text
        self.driver.find_element(By.ID, 'creDriverAC').send_keys('Nes')
        self.driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        time.sleep(2)
        #find the matric view icon and click it
        self.driver.find_element(By.CSS_SELECTOR, '#yui-rec1 > td:nth-child(2) > div:nth-child(1) > a:nth-child(1)').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        #find the gene expression column and grab the text
        geneexp = self.driver.find_element(By.CSS_SELECTOR, '#colGroupInner > g:nth-child(3) > g:nth-child(1) > text:nth-child(2)')
        print(geneexp.text)
        all1 = self.driver.find_element(By.CSS_SELECTOR, 'g.col1:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all1.text)
        all2 = self.driver.find_element(By.CSS_SELECTOR, 'g.col2:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all2.text)
        all3 = self.driver.find_element(By.CSS_SELECTOR, 'g.col3:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all3.text)
        all4 = self.driver.find_element(By.CSS_SELECTOR, 'g.col4:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all4.text)
        all5 = self.driver.find_element(By.CSS_SELECTOR, 'g.col5:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all5.text)
        all6 = self.driver.find_element(By.CSS_SELECTOR, 'g.col6:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all6.text)
        all7 = self.driver.find_element(By.CSS_SELECTOR, 'g.col7:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all7.text)
        all8 = self.driver.find_element(By.CSS_SELECTOR, 'g.col8:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all8.text)
        all9 = self.driver.find_element(By.CSS_SELECTOR, 'g.col9:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all9.text)
        all10 = self.driver.find_element(By.CSS_SELECTOR, 'g.col10:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all10.text)
        all11 = self.driver.find_element(By.CSS_SELECTOR, 'g.col11:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all11.text)
        all12 = self.driver.find_element(By.CSS_SELECTOR, 'g.col12:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all12.text)
        all13 = self.driver.find_element(By.CSS_SELECTOR, 'g.col13:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all13.text)
        all14 = self.driver.find_element(By.CSS_SELECTOR, 'g.col14:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all14.text)
        all15 = self.driver.find_element(By.CSS_SELECTOR, 'g.col15:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all15.text)
        all16 = self.driver.find_element(By.CSS_SELECTOR, 'g.col16:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all16.text)
        all17 = self.driver.find_element(By.CSS_SELECTOR, 'g.col17:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all17.text)
        all18 = self.driver.find_element(By.CSS_SELECTOR, 'g.col18:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all18.text)
        all19 = self.driver.find_element(By.CSS_SELECTOR, 'g.col19:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all19.text)
        all20 = self.driver.find_element(By.CSS_SELECTOR, 'g.col20:nth-child(1) > text:nth-child(2) > a:nth-child(1)')
        print(all20.text)
        # verifies the returned terms are the correct terms and sort order for this search
        self.assertEqual('Nes - gene expression', geneexp.text, 'gene expression allele is not correct')        
        self.assertEqual('Nes<em1(flpo)Awar>', all1.text, 'first allele is not correct')        
        self.assertEqual('Tg(NES-cre)#Ajde', all2.text, 'second allele is not correct' )
        self.assertEqual('Tg(Nes-cre)1Atp', all3.text, 'third allele is not correct' )
        self.assertEqual('Tg(Nes-cre)1Kln', all4.text, 'forth allele is not correct' )
        self.assertEqual('Tg(Nes-cre)1Sasa', all5.text, 'fifth allele is not correct' )
        self.assertEqual('Tg(Nes-cre/ERT2)1Adra', all6.text, 'sixth allele is not correct')        
        self.assertEqual('Tg(Nes-cre/ERT2)1Kag', all7.text, 'seventh allele is not correct' )
        self.assertEqual('Tg(Nes-cre/ERT2)4Kag', all8.text, 'eighth allele is not correct' )
        self.assertEqual('Tg(Nes-cre/ERT2)5-1Kag', all9.text, 'ninth allele is not correct' )
        self.assertEqual('Tg(Nes-cre/ERT2)73Lfp', all10.text, 'tenth allele is not correct' )
        self.assertEqual('Tg(Nes-cre/ERT2)KEisc', all11.text, 'eleventh allele is not correct')        
        self.assertEqual('Tg(Nes-cre/Esr1*)4Ynj', all12.text, 'twelfth allele is not correct' )
        self.assertEqual('Tg(Nes-cre)1Kag', all13.text, 'thirteenth allele is not correct' )
        self.assertEqual('Tg(Nes-cre)1Nogu', all14.text, 'fourteenth allele is not correct' )
        self.assertEqual('Tg(Nes-cre)1Wme', all15.text, 'fifteenth allele is not correct' )
        self.assertEqual('Tg(Nes-cre)1Wmz', all16.text, 'sixteenth allele is not correct')        
        self.assertEqual('Tg(Nes-cre/ERT2)1Fsh', all17.text, 'seventeenth allele is not correct' )
        self.assertEqual('Tg(Nes-phiC31*)1Imayo', all18.text, 'eighteenth allele is not correct' )
        self.assertEqual('Tg(Nes-phiC31*/ERT2)2Imayo', all19.text, 'nineteenth allele is not correct' )
        self.assertEqual('Tg(Nes-phiC31*/ERT2)4Imayo', all20.text, 'twentieth allele is not correct' )

    def test_Matrix_species(self):
        '''
        @status This test verifies that the alleles popup displays correct species data on Gene Expression + Recombinase Activity Comparison Matrix. 
        Order should be:
        1. GXD expression column first
        2. Alleles with mouse drivers next, then human, then rat, then others, Not specified last
        3. species should be displayed in popup text
        @note: Recomb-drvr-3
        '''
        #find the Recombinase driven by field and enter text
        self.driver.find_element(By.ID, 'creDriverAC').send_keys('Krt5, KRT5')
        self.driver.find_element(By.CLASS_NAME, 'goButton').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1]) 
        time.sleep(2)
        #find the matric view icon in the 5th row and click it
        self.driver.find_element(By.CSS_SELECTOR, '#yui-rec4 > td:nth-child(2) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)').click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        #capture and print on hover text for first allele
        toolTip = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.col1:nth-child(1) > text:nth-child(2) > a:nth-child(1)")))
        hov = ActionChains(self.driver).move_to_element(toolTip)
        txt = hov.perform()
        tooltip = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.col1:nth-child(1) > text:nth-child(2) > title:nth-child(2)"))).get_attribute("innerHTML")
        print(tooltip)
        #capture and print on hover text for second allele
        toolTip2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.col2:nth-child(1) > text:nth-child(2) > a:nth-child(1)")))
        hov = ActionChains(self.driver).move_to_element(toolTip2)
        txt = hov.perform()
        tooltip2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.col2:nth-child(1) > text:nth-child(2) > title:nth-child(2)"))).get_attribute("innerHTML")
        print(tooltip2)
        #capture and print on hover text for third allele
        toolTip3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.col3:nth-child(1) > text:nth-child(2) > a:nth-child(1)")))
        hov = ActionChains(self.driver).move_to_element(toolTip3)
        txt = hov.perform()
        tooltip3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.col3:nth-child(1) > text:nth-child(2) > title:nth-child(2)"))).get_attribute("innerHTML")
        print(tooltip3)
        #capture and print on hover text for fourth allele
        toolTip4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.col4:nth-child(1) > text:nth-child(2) > a:nth-child(1)")))
        hov = ActionChains(self.driver).move_to_element(toolTip4)
        txt = hov.perform()
        tooltip4 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.col4:nth-child(1) > text:nth-child(2) > title:nth-child(2)"))).get_attribute("innerHTML")
        print(tooltip4)
        #capture and print on hover text for fifth allele
        toolTip5 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.col5:nth-child(1) > text:nth-child(2) > a:nth-child(1)")))
        hov = ActionChains(self.driver).move_to_element(toolTip5)
        txt = hov.perform()
        tooltip5 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.col5:nth-child(1) > text:nth-child(2) > title:nth-child(2)"))).get_attribute("innerHTML")
        print(tooltip5)
        #capture and print on hover text for sixth allele
        toolTip6 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.col6:nth-child(1) > text:nth-child(2) > a:nth-child(1)")))
        hov = ActionChains(self.driver).move_to_element(toolTip6)
        txt = hov.perform()
        tooltip6 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.col6:nth-child(1) > text:nth-child(2) > title:nth-child(2)"))).get_attribute("innerHTML")
        print(tooltip6)
        #capture and print on hover text for seventh allele
        toolTip7 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.col7:nth-child(1) > text:nth-child(2) > a:nth-child(1)")))
        hov = ActionChains(self.driver).move_to_element(toolTip7)
        txt = hov.perform()
        tooltip7 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "g.col7:nth-child(1) > text:nth-child(2) > title:nth-child(2)"))).get_attribute("innerHTML")
        print(tooltip7)
        self.assertEqual('Tg(KRT5-cre/ERT2)1Blh\nhuman driver species', tooltip, 'the tooltip species is wrong')
        self.assertEqual('Tg(KRT5-cre/PGR)1Der\nhuman driver species', tooltip2, 'the tooltip2 species is wrong')
        self.assertEqual('Tg(KRT5-cre)5132Jlj\ncattle driver species', tooltip3, 'the tooltip2 species is wrong')
        self.assertEqual('Tg(KRT5-cre/ERT2)2Ipc\ncattle driver species', tooltip4, 'the tooltip species is wrong')
        self.assertEqual('Tg(KRT5-cre/ERT)ICmch\ncattle driver species', tooltip5, 'the tooltip2 species is wrong')
        self.assertEqual('Tg(KRT5-cre/ERT)SCmch\ncattle driver species', tooltip6, 'the tooltip2 species is wrong')
        self.assertEqual('Tg(Krt1-5-cre/ERT)1Ipc\nnot specified driver species', tooltip7, 'the tooltip2 species is wrong')
        
    def tearDown(self):
        self.driver.quit()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCreSpecificity))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))   