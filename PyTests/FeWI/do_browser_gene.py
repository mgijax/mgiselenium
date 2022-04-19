'''
Created on Jan 30, 2017
These tests are to verify the data displayed on the Genes tab of the Do Browser page.
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import HtmlTestRunner
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table
# Tests !!!!these tests should be rewritten using the query form instead of the quick search box!!!
class TestDoBrowserGeneTab(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL)
        self.driver.implicitly_wait(10)
        
    def test_dobrowser_header(self):
        '''
        @status this test verifies the term line in the header section on the DO browser page is correct.
        '''
        print ("BEGIN test_dobrowser_header")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:1324")
        searchbox.send_keys(Keys.RETURN)
        self.driver.find_element(By.LINK_TEXT, 'lung cancer').click()
        #Does a webdriver wait until the disease name is present so we know the page is loaded
        if WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, 'diseaseNameID'))):
            print('page loaded')
        header = self.driver.find_element(By.ID, 'diseaseNameID')#identifies the header section of the DO Browser page
        print(header.text)
        self.assertEqual(header.text, "lung cancer (DOID:1324)")
        syn = self.driver.find_element(By.ID, 'diseaseSynonym')#identifies the synonym line in the header section of the DO Browser page
        print(syn.text)
        self.assertEqual(syn.text, "lung neoplasm")
        alt_id = self.driver.find_element(By.ID, 'diseaseSecondaryIDs')#identifies the alternate IDs line of the header section of the DO Browser page
        print(alt_id.text)
        self.assertEqual(alt_id.text, "OMIM:211980, OMIM:608935, OMIM:612571, OMIM:612593, OMIM:614210, DOID:13075, DOID:1322, DOID:9881, ICD10CM:C34.1, ICD10CM:C34.2, ICD10CM:C34.3, ICD9CM:162.3, ICD9CM:162.4, ICD9CM:162.5, ICD9CM:162.8, UMLS_CUI:C0024624, UMLS_CUI:C0153491, UMLS_CUI:C0153492, UMLS_CUI:C0153493")
        #locates and verifies the definition
        definition = self.driver.find_element(By.ID, 'diseaseDefinition')#identifies the Definition line of the header section of the DO Browser page
        print(definition.text)
        self.assertEqual(definition.text, "A respiratory system cancer that is located_in the lung.")
        
    def test_dobrowser_genestab_modelstab_text(self):
        '''
        @status this test verifies the genes tab has the correct number of genes by verifying the tab's text and the models tab has the correct number
        of models by verifying the tab's text
        '''
        print ("BEGIN test_dobrowser_genestab_modelstab_text")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:11198")
        searchbox.send_keys(Keys.RETURN)
        self.driver.find_element(By.LINK_TEXT, 'DiGeorge syndrome').click()
        gene_tab = self.driver.find_element(By.LINK_TEXT, 'Genes (21)')#identifies the Genes tab.
        print(gene_tab.text)
        self.assertEqual(gene_tab.text, "Genes (21)", "The Genes Tab number is not correct")
        model_tab = self.driver.find_element(By.LINK_TEXT, 'Models (44)')#identifies the Genes tab.
        print(model_tab.text)
        self.assertEqual(model_tab.text, "Models (44)", "The Models Tab number is not correct")#time.sleep(2)   
        
    def test_dobrowser_genestab_m_hmht(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse/human(TBX1), just mouse, and just human(DGCR) plus  Transgenes
        '''
        print ("BEGIN test_dobrowser_genestab_m_hmht")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:11198")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, 'DiGeorge syndrome').click()
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, "geneTabTable")
        table = Table(gene_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of gene data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        row4 = cells[5]
        row5 = cells[6]
        row6 = cells[7]
        row7 = cells[8]
        row8 = cells[9]
        row9 = cells[10]
        row10 = cells[11]
        row11 = cells[12]
        row12 = cells[13]
        row13 = cells[14]
        row14 = cells[15]
        row15 = cells[16]
        row16 = cells[17]
        row17 = cells[18]
        row18 = cells[19]
        row19 = cells[20]
        row20 = cells[21]
    
        self.assertEqual(row1.text, '       DiGeorge syndrome TBX1* Tbx1* 21 models Alliance of Genome Resources')
        self.assertEqual(row2.text, '       DiGeorge syndrome ALDH1A2 Aldh1a2* 1 model Alliance of Genome Resources')
        self.assertEqual(row3.text, 'DiGeorge syndrome b2b954Clo* 1 model')
        self.assertEqual(row4.text, 'DiGeorge syndrome b2b1941Clo* 1 model')
        self.assertEqual(row5.text, 'DiGeorge syndrome b2b2696Clo* 1 model')
        self.assertEqual(row6.text, 'DiGeorge syndrome CHRD Chrd* 1 model Alliance of Genome Resources')
        self.assertEqual(row7.text, 'DiGeorge syndrome CRKL Crkl* 1 model Alliance of Genome Resources')
        self.assertEqual(row8.text, 'DiGeorge syndrome DICER1 Dicer1* 1 model Alliance of Genome Resources')
        self.assertEqual(row9.text, 'DiGeorge syndrome DOCK1 Dock1* 1 model Alliance of Genome Resources')
        self.assertEqual(row10.text, 'DiGeorge syndrome FGF8 Fgf8* 1 model Alliance of Genome Resources')
        self.assertEqual(row11.text, 'DiGeorge syndrome FOXN1 Foxn1* 1 model Alliance of Genome Resources')
        self.assertEqual(row12.text, 'DiGeorge syndrome HOXA3 Hoxa3* 1 model Alliance of Genome Resources')
        self.assertEqual(row13.text, 'DiGeorge syndrome KAT6A Kat6a* 2 models Alliance of Genome Resources')
        self.assertEqual(row14.text, 'DiGeorge syndrome NDST1 Ndst1* 1 model Alliance of Genome Resources')
        self.assertEqual(row15.text, 'DiGeorge syndrome PLXND1 Plxnd1* 2 models Alliance of Genome Resources')
        self.assertEqual(row16.text, 'DiGeorge syndrome pta* 1 model')
        self.assertEqual(row17.text, 'DiGeorge syndrome TGFBR2 Tgfbr2* 1 model Alliance of Genome Resources')
        self.assertEqual(row18.text, 'DiGeorge syndrome VEGFA Vegfa* 2 models Alliance of Genome Resources')
        self.assertEqual(row19.text, 'DiGeorge syndrome ZNF366 Zfp366* 1 model Alliance of Genome Resources')
        self.assertEqual(row20.text, '       DiGeorge syndrome DGCR*  ')
        
        transgene_table = self.driver.find_element(By.ID, "transgeneTable")
        table = Table(transgene_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of transgene data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        
        self.assertEqual(row1.text, '  DiGeorge syndrome Del(16Dgcr2-Hira)1Rak 1 model')
        self.assertEqual(row2.text, '  DiGeorge syndrome Del(16Dgcr2-Hira)3Aam 1 model')
        self.assertEqual(row3.text, '  DiGeorge syndrome Del(16Es2el-Ufd1l)217Bld 1 model')
        
    def test_dobrowser_genestab_m_hmh(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse/human(CDKN1C), just mouse(Sptbn1), and just human(H19, H19-ICR, IGF2, KCNQ1, KCNQ1OT1, NSD1).
        '''
        print ("BEGIN test_dobrowser_genestab_m_hmh")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:5572")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, 'Beckwith-Wiedemann syndrome').click()
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, "geneTabTable")
        table = Table(gene_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of gene data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        row4 = cells[5]
        row5 = cells[6]
        row6 = cells[7]
        self.assertEqual(row1.text, '       Beckwith-Wiedemann syndrome CDKN1C* Cdkn1c* 2 models Alliance of Genome Resources')
        self.assertEqual(row2.text, '       Beckwith-Wiedemann syndrome SPTBN1 Sptbn1* 1 model Alliance of Genome Resources')
        self.assertEqual(row3.text, '       Beckwith-Wiedemann syndrome H19-ICR*  ')
        self.assertEqual(row4.text, 'Beckwith-Wiedemann syndrome IGF2* Igf2   Alliance of Genome Resources')
        self.assertEqual(row5.text, 'Beckwith-Wiedemann syndrome KCNQ1* Kcnq1 1 model Alliance of Genome Resources')
        self.assertEqual(row6.text, 'Beckwith-Wiedemann syndrome KCNQ1OT1* Kcnq1ot1   Alliance of Genome Resources')       
        time.sleep(2)
        transgene_table = self.driver.find_element(By.ID, "transgeneTable")
        table = Table(transgene_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of transgene data
        row1 = cells[2]
        self.assertEqual(row1.text, '  Beckwith-Wiedemann syndrome Tg(YACW408A5)1952Ricc 1 model')
        
    def test_dobrowser_genestab_m_hm(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse/human(GALC) and just mouse(Psap)
        '''
        print ("BEGIN test_dobrowser_genestab_m_hm")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:10587")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, 'Krabbe disease').click()
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, "geneTabTable")
        table = Table(gene_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of gene data
        row1 = cells[2]
        row2 = cells[3]
        self.assertEqual(row1.text, '       Krabbe disease GALC* Galc* 2 models Alliance of Genome Resources')
        self.assertEqual(row2.text, '       Krabbe disease PSAP Psap* 1 model Alliance of Genome Resources')
        
    def test_dobrowser_genestab_m(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to just mouse(Tfam)
        '''
        print ("BEGIN test_dobrowser_genestab_m")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:12934")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, 'Kearns-Sayre syndrome').click()
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, "geneTabTable")
        table = Table(gene_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of gene data
        row1 = cells[2]
        self.assertEqual(row1.text, '       Kearns-Sayre syndrome TFAM Tfam* 2 models Alliance of Genome Resources')

    def test_dobrowser_genestab_ht(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to just human(IL6) Plus Transgene
        '''
        print ("BEGIN test_dobrowser_genestab_ht")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box Use DOID:0050909 if this DOID changes.
        searchbox.send_keys("DOID:0050637")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, "Finnish type amyloidosis").click()
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, 'geneTabTable')
        table = Table(gene_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of gene data
        row1 = cells[2]
        self.assertEqual(row1.text, "       Finnish type amyloidosis GSN* Gsn 2 models Alliance of Genome Resources")
        
        transgene_table = self.driver.find_element(By.ID, 'transgeneTable')
        table = Table(transgene_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of transgene data
        row1 = cells[2]
        self.assertEqual(row1.text, "  Finnish type amyloidosis Tg(Ckm-GSN*D187N)AJewe 2 models")
        
    def test_dobrowser_genestab_h(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to just human
        '''
        print ("BEGIN test_dobrowser_genestab_h")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:0050807")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, "Kahrizi syndrome").click()

        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, 'geneTabTable')
        table = Table(gene_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of gene data
        row1 = cells[2]
        self.assertEqual(row1.text, '       Kahrizi syndrome SRD5A3* Srd5a3   Alliance of Genome Resources')

    def test_dobrowser_genestab_m_h(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to just mouse/human(UBR1)
        '''
        print ("BEGIN test_dobrowser_genestab_m_h")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:14694")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, 'Johanson-Blizzard syndrome').click()
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, 'geneTabTable')
        table = Table(gene_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of gene data
        row1 = cells[2]
        self.assertEqual(row1.text, '       Johanson-Blizzard syndrome UBR1* Ubr1* 1 model Alliance of Genome Resources')
        
    def test_dobrowser_genestab_m_hh(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse/human(HAMP, HFE, HFE2, SLC40A1, TFR2) and just human(Bmp2)
        '''
        print ("BEGIN test_dobrowser_genestab_m_hh")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:2352")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, 'hemochromatosis').click()
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, "geneTabTable")
        table = Table(gene_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of gene data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        row4 = cells[5]
        row5 = cells[6]
        row6 = cells[7]
        row7 = cells[8]
        row8 = cells[9]
        row9 = cells[10]
        self.assertEqual(row1.text, '       hemochromatosis type 1 HFE* Hfe* 13 models Alliance of Genome Resources')
        self.assertEqual(row2.text, 'hemochromatosis type 2A HJV* Hjv* 2 models Alliance of Genome Resources')
        self.assertEqual(row3.text, 'hemochromatosis type 2B HAMP* Hamp*, Hamp2 1 model Alliance of Genome Resources')
        self.assertEqual(row4.text, 'hemochromatosis type 3 TFR2* Tfr2* 2 models Alliance of Genome Resources')
        self.assertEqual(row5.text, 'hemochromatosis type 4 SLC40A1* Slc40a1* 3 models Alliance of Genome Resources')
        self.assertEqual(row6.text, '       hemochromatosis B2M B2m* 1 model Alliance of Genome Resources')
        self.assertEqual(row7.text, 'hemochromatosis HMOX1 Hmox1* 1 model Alliance of Genome Resources')
        self.assertEqual(row8.text, '       hemochromatosis type 1 BMP2* Bmp2   Alliance of Genome Resources')
        self.assertEqual(row9.text, 'hemochromatosis type 5 FTH1* Fth1   Alliance of Genome Resources')
        
    def test_dobrowser_genestab_mult_homolog(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse and human but has multiple Mouse Homologs
        '''
        print ("BEGIN test_dobrowser_genestab_multi_homolog")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:633")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, 'myositis').click()
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, 'geneTabTable')
        table = Table(gene_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of gene data
        row1 = cells[2]
        row2 = cells[3]
        self.assertEqual(row1.text, '       dermatomyositis ANGPTL2 Angptl2* 1 model Alliance of Genome Resources')
        self.assertEqual(row2.text, 'myositis HLA-A, HLA-B, HLA-C, HLA-E, HLA-F, HLA-G, HLA-H H2-K1*, Gm7030, Gm8909, Gm11127, H2-D1, H2-M1, H2-M2, H2-M3, H2-M5, H2-M9, H2-M10.1, H2-M10.2, H2-M10.3, H2-M10.4, H2-M10.5, H2-M10.6, H2-Q1, H2-Q2, H2-Q4, H2-Q6, H2-Q7, H2-Q8, H2-Q10, H2-T3, H2-T22, H2-T23 1 model Alliance of Genome Resources')
        transgene_table = self.driver.find_element(By.ID, "transgeneTable")
        table = Table(transgene_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of transgene data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        row4 = cells[5]
        self.assertEqual(row1.text, '  dermatomyositis Tg(Krt14-Angptl2)1Yo 1 model')
        self.assertEqual(row2.text, '  inclusion body myositis Tg(Ckm-APPSw)A2Lfa 1 model')
        self.assertEqual(row3.text, '  inclusion body myositis Tg(Ckm-APPSw)A6Lfa 1 model')
        self.assertEqual(row4.text, '  myositis Tg(tetO-H2-K1)#Papl 1 model')

    def test_dobrowser_genestab_same_gene_mult_subtypes(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse/human, mouse, and human. Genes COL1A1 and COL1A2 are attached multiple times
        '''
        print ("BEGIN test_dobrowser_genestab_same_gene_mult_subtypes")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:12347")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, 'osteogenesis imperfecta').click()
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Models tab and clicks it.
        
        model_table = self.driver.find_element(By.ID, 'geneTabTable')
        table = Table(model_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of disease model data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        row4 = cells[5]
        row5 = cells[6]
        row6 = cells[7]
        row7 = cells[8]
        row8 = cells[9]
        row9 = cells[10]
        row10 = cells[11]
        row11 = cells[12]
        row12 = cells[13]
        row13 = cells[14]
        row14 = cells[15]
        row15 = cells[16]
        row16 = cells[17]
        row17 = cells[18]
        row18 = cells[19]
        row19 = cells[20]
        row20 = cells[21]
        row21 = cells[22]
        row22 = cells[23]
        row23 = cells[24]
        row24 = cells[25]
        row25 = cells[26]
        row26 = cells[27]
        row27 = cells[28]
        row28 = cells[29]
        row29 = cells[30]
        row30 = cells[31]
        row31 = cells[32]
        row32 = cells[33]
        row33 = cells[34]
        self.assertEqual(row1.text, '       osteogenesis imperfecta type 1 COL1A1* Col1a1* 2 models Alliance of Genome Resources')
        self.assertEqual(row2.text, 'osteogenesis imperfecta type 10 SERPINH1* Serpinh1* 1 model Alliance of Genome Resources')
        self.assertEqual(row3.text, 'osteogenesis imperfecta type 2 COL1A1* Col1a1* 2 models Alliance of Genome Resources')
        self.assertEqual(row4.text, 'osteogenesis imperfecta type 3 COL1A2* Col1a2* 2 models Alliance of Genome Resources')
        self.assertEqual(row5.text, 'osteogenesis imperfecta type 3 COL1A1* Col1a1* 1 model Alliance of Genome Resources')
        self.assertEqual(row6.text, 'osteogenesis imperfecta type 4 COL1A1* Col1a1* 3 models Alliance of Genome Resources')
        self.assertEqual(row7.text, 'osteogenesis imperfecta type 6 SERPINF1* Serpinf1* 1 model Alliance of Genome Resources')
        self.assertEqual(row8.text, 'osteogenesis imperfecta type 7 CRTAP* Crtap* 1 model Alliance of Genome Resources')
        self.assertEqual(row9.text, 'osteogenesis imperfecta type 8 P3H1* P3h1* 1 model Alliance of Genome Resources')
        self.assertEqual(row10.text, 'osteogenesis imperfecta type 9 PPIB* Ppib* 2 models Alliance of Genome Resources')
        self.assertEqual(row11.text, '       osteogenesis imperfecta COL1A1 Col1a1* 1 model Alliance of Genome Resources')
        self.assertEqual(row12.text, 'osteogenesis imperfecta COL1A2 Col1a2* 5 models Alliance of Genome Resources')
        self.assertEqual(row13.text, 'osteogenesis imperfecta SMAD4 Smad4* 1 model Alliance of Genome Resources')
        self.assertEqual(row14.text, 'osteogenesis imperfecta SMPD3 Smpd3* 1 model Alliance of Genome Resources')
        self.assertEqual(row15.text, 'osteogenesis imperfecta type 2 SMPD3 Smpd3* 1 model Alliance of Genome Resources')
        self.assertEqual(row16.text, 'osteogenesis imperfecta type 3 SMPD3 Smpd3* 1 model Alliance of Genome Resources')
        self.assertEqual(row17.text, 'osteogenesis imperfecta type 5 SUCO Suco* 1 model Alliance of Genome Resources')
        self.assertEqual(row18.text, '       Cole-Carpenter syndrome P4HB* P4hb   Alliance of Genome Resources')
        self.assertEqual(row19.text, 'Cole-Carpenter syndrome SEC24D* Sec24d   Alliance of Genome Resources')
        self.assertEqual(row20.text, 'osteogenesis imperfecta type 11 FKBP10* Fkbp10   Alliance of Genome Resources')
        self.assertEqual(row21.text, 'osteogenesis imperfecta type 12 SP7* Sp7   Alliance of Genome Resources')
        self.assertEqual(row22.text, 'osteogenesis imperfecta type 13 BMP1* Bmp1   Alliance of Genome Resources')
        self.assertEqual(row23.text, 'osteogenesis imperfecta type 14 TMEM38B* Tmem38b   Alliance of Genome Resources')
        self.assertEqual(row24.text, 'osteogenesis imperfecta type 15 WNT1* Wnt1   Alliance of Genome Resources')
        self.assertEqual(row25.text, 'osteogenesis imperfecta type 16 CREB3L1* Creb3l1   Alliance of Genome Resources')
        self.assertEqual(row26.text, 'osteogenesis imperfecta type 17 SPARC* Sparc   Alliance of Genome Resources')
        self.assertEqual(row27.text, 'osteogenesis imperfecta type 18 TENT5A* Tent5a   Alliance of Genome Resources')
        self.assertEqual(row28.text, 'osteogenesis imperfecta type 19 MBTPS2* Mbtps2   Alliance of Genome Resources')
        self.assertEqual(row29.text, 'osteogenesis imperfecta type 2 COL1A2* Col1a2   Alliance of Genome Resources')
        self.assertEqual(row30.text, 'osteogenesis imperfecta type 20 MESD* Mesd   Alliance of Genome Resources')
        self.assertEqual(row31.text, 'osteogenesis imperfecta type 21 KDELR2* Kdelr2   Alliance of Genome Resources')
        self.assertEqual(row32.text, 'osteogenesis imperfecta type 4 COL1A2* Col1a2   Alliance of Genome Resources')
        self.assertEqual(row33.text, 'osteogenesis imperfecta type 5 IFITM5* Ifitm5 1 "NOT" model Alliance of Genome Resources')
        transgene_table = self.driver.find_element(By.ID, "transgeneTable")
        table = Table(transgene_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        #displays each row of transgene data
        row1 = cells[2]
        row2 = cells[3]
        self.assertEqual(row1.text, '  osteogenesis imperfecta type 1 Tg(COL1A1)73Prc 1 model')
        self.assertEqual(row2.text, '  osteogenesis imperfecta type 5 Tg(Col1a1-Ifitm5*)1Brle 1 model')
            
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDoBrowserGeneTab))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests')) 
