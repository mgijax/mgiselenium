
'''
Created on Mar 7, 2019
Tests the adding and deleting features of the Variant module
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
#from.selenium.webdriver.support.color import Color
import HtmlTestRunner
import json
import sys,os.path
from selenium.webdriver.support.color import Color

# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests

class TestEiVariantAddDelete(unittest.TestCase):
    """
    @status Test Variant search fields
    """

    def setUp(self):
        #self.driver = webdriver.Firefox() 
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        #self.form.get_module("bhmgipwi02lt:5099/pwi/edit/variant/")
        self.form.get_module(config.TEST_PWI_URL + "/edit/variant/")
        username = self.driver.find_element_by_name('user')#finds the user login box
        username.send_keys(config.PWI_LOGIN) #enters the username
        passwd = self.driver.find_element_by_name('password')#finds the password box
        passwd.send_keys(config.PWI_PASSWORD) #enters a valid password
        submit = self.driver.find_element_by_name("submit") #Find the Login button
        submit.click()
    
    def tearDown(self):
        self.driver.close()
        
    def testVarAddSTrans(self):
        """
        @Status tests that you can add a sourced transcript with a RefSeq ID
        @see pwi-var-create-seq-1 
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters the MGI ID for Samd4<m1Btlr>
        driver.find_element_by_id("alleleID").send_keys('MGI:5563413')
        driver.find_element_by_id('searchButton').click()
        #waits until the page is displayed on the page    
        wait.forAngular(self.driver)
    
        #Find the sourced Transcript ID field and enters the ID
        driver.find_element_by_id("srcRnaID").clear()
        driver.find_element_by_id("srcRnaID").send_keys('XM_006519628')
        time.sleep(2)
        #Find the start field for the sourced transcript and enter data
        driver.find_element_by_id("srcRnaStart").clear()
        driver.find_element_by_id("srcRnaStart").send_keys('23456')
        #Find the stop field for the sourced transcript and enter data
        driver.find_element_by_id("srcRnaEnd").clear()
        driver.find_element_by_id("srcRnaEnd").send_keys('23456')
        time.sleep(2)
        #Find the Modify button and click it
        driver.find_element_by_id('updateVariantButton').click() 
        wait.forAngular(self.driver)
        #find the sourced Transcript ID field
        source_tran = self.driver.find_element_by_id("srcRnaID").get_attribute("value")
    
        print(source_tran)
        #assert the correct ID is saved in the Sourced Transcript ID field
        self.assertEqual(source_tran, 'XM_006519628')
        
    def testVarTypesPopup(self):
        """
        @Status tests that the variant SO Types popup has the correct types sorted in the correct order
        @see pwi-var-type-1, 4 / pwi-var-so-1
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters the MGI ID for Samd4<m1Btlr>
        driver.find_element_by_id("alleleID").send_keys('MGI:5563413')
        driver.find_element_by_id('searchButton').click()
        #waits until the page is displayed on the page    
        wait.forAngular(self.driver)    
        #Find the Types Popup link and click it
        driver.find_element_by_link_text("Types Popup").click()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #find the SO Types table
        types_table = self.driver.find_element_by_id("soTable")
        table = Table(types_table)
        #Iterate and print the Types column
        cell1 = table.get_column_cells('Term')
        alltypes = iterate.getTextAsList(cell1)
        print(alltypes)
        wait.forAngular
        #assert the correct SO Types are listed in the correct order
        self.assertEqual(alltypes, ['Term', 'point_mutation', 'deletion', 'insertion', 'MNV', 'inversion', 'translocation', 'inversion_breakpoint', 'translocation_breakpoint', 'duplication', 'sequence_length_variant', 'complex_substitution', 'complex_structural_alteration'])

    def testVarEffectsPopup(self):
        """
        @Status tests that the variant SO Effects popup has the correct effects sorted in the correct order
        @see pwi-var-type-6, 9 /pwi-var-so-4
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters the MGI ID for Samd4<m1Btlr>
        driver.find_element_by_id("alleleID").send_keys('MGI:5563413')
        driver.find_element_by_id('searchButton').click()
        #waits until the page is displayed on the page    
        wait.forAngular(self.driver)    
        #Find the Effects Popup link and click it
        driver.find_element_by_link_text("Effects Popup").click()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #find the SO Effects table
        effects_table = self.driver.find_element_by_id("soTable")
        table = Table(effects_table)
        #Iterate and print the Effect column
        cell1 = table.get_column_cells('Term')
        alleffects = iterate.getTextAsList(cell1)
        print(alleffects)
        wait.forAngular
        #assert the correct SO Effects are listed in the correct order
        self.assertEqual(alleffects, ['Term', 'missense_variant', 'stop_gained', 'stop_lost', 'start_lost', 'splice_acceptor_variant', 'splice_donor_variant', 'splice_region_variant', 'frameshift_variant', 'frameshift_truncation', 'frameshift_elongation', '5_prime_UTR_premature_start_codon_gain_variant', 'chromosome_number_variation', 'coding_sequence_variant', 'coding_transcript_intron_variant', 'coding_transcript_variant', 'conserved_intergenic_variant', 'conserved_intron_variant', 'disruptive_inframe_deletion', 'disruptive_inframe_insertion', 'downstream_gene_variant', 'exon_loss_variant', 'exon_variant', 'feature_truncation', 'gene_variant', 'inframe_deletion', 'inframe_insertion', 'initiator_codon_variant', 'intergenic_variant', 'internal_feature_elongation', 'intragenic_variant', 'intron_variant', 'non_coding_transcript_exon_variant', 'non_coding_transcript_intron_variant', 'non_coding_transcript_variant', 'rare_amino_acid_variant', 'regulatory_region_variant', 'sequence_variant', 'splicing_variant', 'stop_retained_variant', 'structural_variant', 'synonymous_variant', 'transcript_ablation', 'transcript_variant', 'upstream_gene_variant'])        

    def testVarTypesPopupAdd(self):
        """
        @Status tests that the variant SO Types popup can add SO types using Save button
        @see pwi-var-type-2 / pwi-var-so-2,7 
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters the MGI ID for Samd4<m1Btlr>
        driver.find_element_by_id("alleleID").send_keys('MGI:5563413')
        driver.find_element_by_id('searchButton').click()
        #waits until the page is displayed on the page    
        wait.forAngular(self.driver)    
        #Find the Types Popup link and click it
        driver.find_element_by_link_text("Types Popup").click()
        self.driver.switch_to_window(self.driver.window_handles[-1])#switches focus to the popup window
        wait.forAngular(self.driver) 
        #Find and click 4 variant Type terms(check boxes)
        self.driver.find_element_by_xpath('//table[@id="soTable"]//tbody/tr[3]/td[1]/input').click()#This is for SO:0000159
        self.driver.find_element_by_xpath('//table[@id="soTable"]//tbody/tr[4]/td[1]/input').click()#this is for SO:0000667
        self.driver.find_element_by_xpath('//table[@id="soTable"]//tbody/tr[5]/td[1]/input').click()#this is for SO:0002007
        self.driver.find_element_by_xpath('//table[@id="soTable"]//tbody/tr[6]/td[1]/input').click()#This is for SO:1000036
        wait.forAngular(self.driver)
        #Click the "Save Changes and Close button
        driver.find_element_by_id("soSave").click()
        self.driver.switch_to_window(self.driver.window_handles[-1])#switch focus back to the main window
        #Find the Types display box and get all the SO IDs  in it
        soList = self.driver.find_element_by_id('soTypes').get_attribute('value')
        print(soList)
        #Assert the correct SO Types are displayed in the Types box
        self.assertEqual(soList, 'SO:1000008 (point_mutation)\nSO:0000159 (deletion)\nSO:0000667 (insertion)\nSO:0002007 (MNV)\nSO:1000036 (inversion)')
        

    def testVarTypesPopupDiscard(self):
        """
        @Status tests that the variant SO Types popup can discard changes using the Discard button
        @see pwi-var-so-8  
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters the MGI ID for Samd4<m1Btlr>
        driver.find_element_by_id("alleleID").send_keys('MGI:5563413')
        driver.find_element_by_id('searchButton').click()
        #waits until the page is displayed on the page    
        wait.forAngular(self.driver)    
        #Find the Types Popup link and click it
        driver.find_element_by_link_text("Types Popup").click()
        self.driver.switch_to_window(self.driver.window_handles[-1])#switches focus to the popup window
        wait.forAngular(self.driver) 
        #Find and click 4 variant Type terms(check boxes)
        self.driver.find_element_by_xpath('//table[@id="soTable"]//tbody/tr[7]/td[1]/input').click()#This is for SO:0000199
        self.driver.find_element_by_xpath('//table[@id="soTable"]//tbody/tr[8]/td[1]/input').click()#this is for SO:0001022
        self.driver.find_element_by_xpath('//table[@id="soTable"]//tbody/tr[9]/td[1]/input').click()#this is for SO:0001413
        wait.forAngular(self.driver)
        #Click the "Discard Changes and Close" button
        driver.find_element_by_id("soHide").click()
        self.driver.switch_to_window(self.driver.window_handles[-1])#switch focus back to the main window
        #Find the Types display box and get all the SO IDs  in it
        soList = self.driver.find_element_by_id('soTypes').get_attribute('value')
        print(soList)
        #Assert the correct SO Types are displayed in the Types box
        self.assertEqual(soList, 'SO:1000008 (point_mutation)')

    def testVarEffectsPopupAdd(self):
        """
        @Status tests that the variant SO Effects popup can add SO effects using Save button
        @see pwi-var-so-5, 9 / pwi-var-effect-1 
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters the MGI ID for Samd4<m1Btlr>
        driver.find_element_by_id("alleleID").send_keys('MGI:5563413')
        driver.find_element_by_id('searchButton').click()
        #waits until the page is displayed on the page    
        wait.forAngular(self.driver)    
        #Find the Types Popup link and click it
        driver.find_element_by_link_text("Effects Popup").click()
        self.driver.switch_to_window(self.driver.window_handles[-1])#switches focus to the popup window
        wait.forAngular(self.driver) 
        #Find and click 4 variant Type terms(check boxes)
        self.driver.find_element_by_xpath('//table[@id="soTable"]//tbody/tr[3]/td[1]/input').click()#This is for SO:0001587
        self.driver.find_element_by_xpath('//table[@id="soTable"]//tbody/tr[4]/td[1]/input').click()#this is for SO:0002012
        self.driver.find_element_by_xpath('//table[@id="soTable"]//tbody/tr[5]/td[1]/input').click()#this is for SO:0001574
        self.driver.find_element_by_xpath('//table[@id="soTable"]//tbody/tr[6]/td[1]/input').click()#This is for SO:0001575
        wait.forAngular(self.driver)
        #Click the "Save Changes and Close button
        driver.find_element_by_id("soSave").click()
        self.driver.switch_to_window(self.driver.window_handles[-1])#switch focus back to the main window
        #Find the Effects display box and get all the SO IDs  in it
        soList = self.driver.find_element_by_id('soEffects').get_attribute('value')
        print(soList)
        #Assert the correct SO Types are displayed in the Effects box
        self.assertEqual(soList, 'SO:0001583 (missense_variant)\nSO:0001587 (stop_gained)\nSO:0001578 (stop_lost)\nSO:0002012 (start_lost)\nSO:0001574 (splice_acceptor_variant)')

    def testVarEffectPopupDiscard(self):
        """
        @Status tests that the variant SO Effects popup can discard changes using the Discard button
        @see pwi-var-so-10
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters the MGI ID for Samd4<m1Btlr>
        driver.find_element_by_id("alleleID").send_keys('MGI:5563413')
        driver.find_element_by_id('searchButton').click()
        #waits until the page is displayed on the page    
        wait.forAngular(self.driver)    
        #Find the Types Popup link and click it
        driver.find_element_by_link_text("Effects Popup").click()
        self.driver.switch_to_window(self.driver.window_handles[-1])#switches focus to the popup window
        wait.forAngular(self.driver) 
        #Find and click 4 variant Type terms(check boxes)
        self.driver.find_element_by_xpath('//table[@id="soTable"]//tbody/tr[8]/td[1]/input').click()#This is for SO:0001589
        self.driver.find_element_by_xpath('//table[@id="soTable"]//tbody/tr[9]/td[1]/input').click()#this is for SO:0001910
        self.driver.find_element_by_xpath('//table[@id="soTable"]//tbody/tr[10]/td[1]/input').click()#this is for SO:0001909
        wait.forAngular(self.driver)
        #Click the "Discard Changes and Close" button
        driver.find_element_by_id("soHide").click()
        self.driver.switch_to_window(self.driver.window_handles[-1])#switch focus back to the main window
        #Find the Effects display box and get all the SO IDs  in it
        soList = self.driver.find_element_by_id('soEffects').get_attribute('value')
        print(soList)
        #Assert the correct SO Types are displayed in the Effects box
        self.assertEqual(soList, 'SO:0001583 (missense_variant)')

    def testAllVarTable(self):
        """
        @Status tests that the All Variants Table displays the data that is displayed in the form
        @see pwi-var-create-5, 6, 7 BROKE 9/5/2019
        @attention: This variant might have to be totally recreated upon a new data load, or just create it within this test
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters the MGI ID for Samd4<m1Btlr>
        driver.find_element_by_id("alleleID").send_keys('MGI:3851923')
        driver.find_element_by_id('searchButton').click()
        #waits until the page is displayed on the page    
        wait.forAngular(self.driver)   
        #Find the All Variants table
        variants_table = self.driver.find_element_by_id("variantTable")
        table = Table(variants_table)
        #Iterate and print the search results headers
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print(symbols)
        gbuild1 = table.get_cell(2, 0)
        gbuild2 = table.get_cell(3, 0)
        tid1 = table.get_cell(2, 5)
        tid2 = table.get_cell(3, 5)
        pid1 = table.get_cell(2, 10)
        pid2 = table.get_cell(3, 10)
        print(gbuild1.text)
        #Assert the correct genome build is returned for row1
        self.assertEqual(gbuild1.text, 'GRCm38')
        #Assert the correct genome build is returned for row2
        self.assertEqual(gbuild2.text, 'GRCm38')
        #Assert the correct Transcript ID is returned for row1
        self.assertEqual(tid1.text, 'NM_009170')
        #Assert the correct Transcript ID is returned for row2
        self.assertEqual(tid2.text, 'NM_009170')
        #Assert the correct Polypeptide ID is returned for row1
        self.assertEqual(pid1.text, 'NP_033196')
        #Assert the correct Polypeptide ID is returned for row2
        self.assertEqual(pid2.text, 'NP_033196')
        #Assert that the polypeptide ID cell for row1 has a yellow border first by getting it's class
        polyclass = pid1.get_attribute("class")
        print(polyclass)
        #now we need to assert that the polypeptide ID cell has the correct class of isSource
        self.assertEqual(polyclass, 'isSource')
        #Assert that the polypeptide ID cell for row2 has a green border first by getting it's class
        polyclass2 = pid2.get_attribute("class")
        print(polyclass2)
        #now we need to assert that the polypeptide ID cell has the correct class of isCurated
        self.assertEqual(polyclass2, 'isCurated')
        
    def testVarTableTransRefseqLink(self):
        """
        @Status tests that the All Variants Table Transcript IDs link to their appropriate website(RefSeq ID)
        @see pwi-var-create-8
        @attention: This variant might have to be totally recreated upon a new data load, or just create it within this test
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters the MGI ID
        driver.find_element_by_id("alleleID").send_keys('MGI:5563413')
        driver.find_element_by_id('searchButton').click()
        #waits until the page is displayed on the page    
        wait.forAngular(self.driver)   
        #Find the All Variants table
        variants_table = self.driver.find_element_by_id("variantTable")
        table = Table(variants_table)
        #Iterate and print the search results headers
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print(symbols)
        #find the Transcript ID and click it
        self.driver.find_element_by_link_text("XM_006519628").click()
        #switch focus to the newly opened page
        self.driver.switch_to_window(driver.window_handles[-1])
        #Assert the Transcript ID is displayed somewhere on this page.
        assert "XM_006519628" in self.driver.page_source
        #Assert you do not find "No items found" text on the page  
        assert "No items found" not in self.driver.page_source 
             
    def testVarTableTransEnsemblLink(self):
        """
        @Status tests that the All Variants Table Transcript IDs link to their appropriate website(Ensembl ID)
        @see pwi-var-create-8 
        @attention: This variant might have to be totally recreated upon a new data load, or just create it within this test
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters the MGI ID
        driver.find_element_by_id("alleleID").send_keys('MGI:1856473')
        driver.find_element_by_id('searchButton').click()
        #waits until the page is displayed on the page    
        wait.forAngular(self.driver)   
        #Find the All Variants table
        variants_table = self.driver.find_element_by_id("variantTable")
        table = Table(variants_table)
        #Iterate and print the search results headers
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print(symbols)
        #find the Transcript ID for the first row of data and click it
        self.driver.find_element_by_link_text("ENSMUST00000035342").click()
        #switch focus to the newly opened page
        self.driver.switch_to_window(driver.window_handles[-1])
        #Assert the Ensembl ID is displayed somewhere on this page.
        assert "ENSMUST00000035342" in self.driver.page_source   
        #Assert you do not find "No items found" text on the page  
        assert "No items found" not in self.driver.page_source 

    def testVarTableTransGenbankLink(self):
        """
        @Status tests that the All Variants Table Transcript IDs link to their appropriate website(Genbank ID)
        @see pwi-var-create-8 
        @attention: This variant might have to be totally recreated upon a new data load, or just create it within this test
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters the MGI ID
        driver.find_element_by_id("alleleID").send_keys('MGI:6305831')
        driver.find_element_by_id('searchButton').click()
        #waits until the page is displayed on the page    
        wait.forAngular(self.driver)   
        #Find the All Variants table
        variants_table = self.driver.find_element_by_id("variantTable")
        table = Table(variants_table)
        #Iterate and print the search results headers
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print(symbols)
        #find the Transcript ID and click it
        self.driver.find_element_by_link_text("NM_145223").click()
        #switch focus to the newly opened page
        self.driver.switch_to_window(driver.window_handles[-1])
        #Assert the GenBank ID is displayed somewhere on this page.
        assert "NM_145223" in self.driver.page_source   
        #Assert you do not find "No items found" text on the page  
        assert "No items found" not in self.driver.page_source 

    def testVarTablePepSwissprotLink(self):
        """
        @Status tests that the All Variants Table Polypeptide IDs link to their appropriate website(Swiis-Prot ID)
        @see pwi-var-create-8 
        @attention: This variant might have to be totally recreated upon a new data load, or just create it within this test
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters the MGI ID
        driver.find_element_by_id("alleleID").send_keys('MGI:6336157')
        driver.find_element_by_id('searchButton').click()
        #waits until the page is displayed on the page    
        wait.forAngular(self.driver)   
        #Find the All Variants table
        variants_table = self.driver.find_element_by_id("variantTable")
        table = Table(variants_table)
        #Iterate and print the search results headers
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print(symbols)
        #find the Polypeptide ID and click it
        self.driver.find_element_by_link_text("Q8CJG0").click()
        #switch focus to the newly opened page
        self.driver.switch_to_window(driver.window_handles[-1])
        #Assert the Swiss-Prot ID is displayed somewhere on this page.
        assert "Q8CJG0" in self.driver.page_source   
        #Assert you do not find "No items found" text on the page  
        assert "No items found" not in self.driver.page_source 

    def testVarTablePepTremblLink(self):
        """
        @Status tests that the All Variants Table Polypeptide IDs link to their appropriate website(Trembl ID)
        @see pwi-var-create-8 
        @attention: This variant might have to be totally recreated upon a new data load, or just create it within this test
        """
        driver = self.driver
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, "Effects Popup"))
            )
        #finds the allele ID field and enters the MGI ID
        driver.find_element_by_id("alleleID").send_keys('MGI:6306273')
        driver.find_element_by_id('searchButton').click()
        #waits until the page is displayed on the page    
        wait.forAngular(self.driver)   
        #Find the All Variants table
        variants_table = self.driver.find_element_by_id("variantTable")
        table = Table(variants_table)
        #Iterate and print the search results headers
        cells = table.get_rows()
        symbols = iterate.getTextAsList(cells)
        print(symbols)
        #find the Polypeptide ID and click it
        self.driver.find_element_by_link_text("Q6AXE3").click()
        #switch focus to the newly opened page
        self.driver.switch_to_window(driver.window_handles[-1])
        #Assert the Trembl ID is displayed somewhere on this page.
        assert "Q6AXE3" in self.driver.page_source   
        #Assert you do not find "No items found" text on the page  
        assert "No items found" not in self.driver.page_source 
                        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiVariantAddDelete))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))
            