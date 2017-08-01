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
import HTMLTestRunner
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table
# Tests
class TestDoBrowserGeneTab(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL)
        self.driver.implicitly_wait(10)
        
    def test_dobrowser_header(self):
        '''
        @status this test verifies the term line in the header section on the DO browser page is correct.
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:1324")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_link_text('lung cancer').click()
        wait.forAjax(self.driver)
        header = self.driver.find_element_by_id('diseaseNameID')#identifies the header section of the DO Browser page
        print header.text
        time.sleep(1)
        self.assertEqual(header.text, "lung cancer (DOID:1324)")
        syn = self.driver.find_element_by_id('diseaseSynonym')#identifies the synonym line in the header section of the DO Browser page
        print syn.text
        time.sleep(1)
        self.assertEqual(syn.text, "lung neoplasm")
        alt_id = self.driver.find_element_by_id('diseaseSecondaryIDs')#identifies the alternate IDs line of the header section of the DO Browser page
        print alt_id.text
        time.sleep(1)
        self.assertEqual(alt_id.text, "OMIM:211980, OMIM:608935, OMIM:612571, OMIM:612593, OMIM:614210, DOID:13075, DOID:1322, DOID:9881, ICD10CM:C34.1, ICD10CM:C34.2, ICD10CM:C34.3, ICD9CM:162.3, ICD9CM:162.4, ICD9CM:162.5, ICD9CM:162.8, UMLS_CUI:C0024624, UMLS_CUI:C0153491, UMLS_CUI:C0153492, UMLS_CUI:C0153493")
        #locates and verifies the definition
        definition = self.driver.find_element_by_id('diseaseDefinition')#identifies the Definition line of the header section of the DO Browser page
        print definition.text
        time.sleep(1)
        self.assertEqual(definition.text, "A respiratory system cancer that is located_in the lung.")
        
    def test_dobrowser_genestab_modelstab_text(self):
        '''
        @status this test verifies the genes tab has the correct number of genes by verifying the tab's text and the models tab has the correct number
        of models by verifying the tab's text
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:11198")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_link_text('DiGeorge syndrome').click()
        gene_tab = self.driver.find_element_by_link_text('Genes (21)')#identifies the Genes tab.
        print gene_tab.text
        self.assertEqual(gene_tab.text, "Genes (21)", "The Genes Tab number is not correct")
        model_tab = self.driver.find_element_by_link_text('Models (44)')#identifies the Genes tab.
        print model_tab.text
        self.assertEqual(model_tab.text, "Models (44)", "The Models Tab number is not correct")#time.sleep(2)   
        
    def test_dobrowser_genestab_m_hmht(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse/human(TBX1), just mouse, and just human(DGCR) plus  Transgenes
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:11198")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_link_text('DiGeorge syndrome').click()
        self.driver.find_element_by_id('genesTabButton').click()#identifies the Genes tab and clicks it.
        time.sleep(2)
        gene_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(gene_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
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
    
        self.assertEqual(row1.text, '       DiGeorge syndrome TBX1* Tbx1* 21 models HomoloGene and HGNC')
        self.assertEqual(row2.text, '       DiGeorge syndrome ALDH1A2 Aldh1a2* 1 model HomoloGene and HGNC')
        self.assertEqual(row3.text, 'DiGeorge syndrome b2b954Clo* 1 model')
        self.assertEqual(row4.text, 'DiGeorge syndrome b2b1941Clo* 1 model')
        self.assertEqual(row5.text, 'DiGeorge syndrome b2b2696Clo* 1 model')
        self.assertEqual(row6.text, 'DiGeorge syndrome CHRD Chrd* 1 model HomoloGene and HGNC')
        self.assertEqual(row7.text, 'DiGeorge syndrome CRKL Crkl* 1 model HomoloGene and HGNC')
        self.assertEqual(row8.text, 'DiGeorge syndrome DICER1 Dicer1* 1 model HomoloGene and HGNC')
        self.assertEqual(row9.text, 'DiGeorge syndrome DOCK1 Dock1* 1 model HomoloGene and HGNC')
        self.assertEqual(row10.text, 'DiGeorge syndrome FGF8 Fgf8* 1 model HomoloGene and HGNC')
        self.assertEqual(row11.text, 'DiGeorge syndrome FOXN1 Foxn1* 1 model HomoloGene and HGNC')
        self.assertEqual(row12.text, 'DiGeorge syndrome HOXA3 Hoxa3* 1 model HomoloGene and HGNC')
        self.assertEqual(row13.text, 'DiGeorge syndrome KAT6A Kat6a* 2 models HomoloGene and HGNC')
        self.assertEqual(row14.text, 'DiGeorge syndrome NDST1 Ndst1* 1 model HomoloGene and HGNC')
        self.assertEqual(row15.text, 'DiGeorge syndrome PLXND1 Plxnd1* 2 models HomoloGene and HGNC')
        self.assertEqual(row16.text, 'DiGeorge syndrome pta* 1 model')
        self.assertEqual(row17.text, 'DiGeorge syndrome TGFBR2 Tgfbr2* 1 model HomoloGene and HGNC')
        self.assertEqual(row18.text, 'DiGeorge syndrome VEGFA Vegfa* 2 models HomoloGene and HGNC')
        self.assertEqual(row19.text, 'DiGeorge syndrome ZNF366 Zfp366* 1 model HomoloGene and HGNC')
        self.assertEqual(row20.text, '       DiGeorge syndrome DGCR*   HGNC')
        time.sleep(2)
        transgene_table = self.driver.find_element_by_id("transgeneTable")
        table = Table(transgene_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
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
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:5572")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_link_text('Beckwith-Wiedemann syndrome').click()
        self.driver.find_element_by_id('genesTabButton').click()#identifies the Genes tab and clicks it.
        time.sleep(2)
        gene_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(gene_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        row4 = cells[5]
        row5 = cells[6]
        row6 = cells[7]
        row7 = cells[8]
        row8 = cells[9]
        self.assertEqual(row1.text, '       Beckwith-Wiedemann syndrome CDKN1C* Cdkn1c* 2 models HGNC')
        self.assertEqual(row2.text, '       Beckwith-Wiedemann syndrome SPTBN1 Sptbn1* 1 model HomoloGene and HGNC')
        self.assertEqual(row3.text, '       Beckwith-Wiedemann syndrome H19*   HGNC')
        self.assertEqual(row4.text, 'Beckwith-Wiedemann syndrome H19-ICR*  ')
        self.assertEqual(row5.text, 'Beckwith-Wiedemann syndrome IGF2* Igf2   HomoloGene and HGNC')
        self.assertEqual(row6.text, 'Beckwith-Wiedemann syndrome KCNQ1* Kcnq1 1 model HomoloGene and HGNC')
        self.assertEqual(row7.text, 'Beckwith-Wiedemann syndrome KCNQ1OT1* Kcnq1ot1   HGNC')
        self.assertEqual(row8.text, 'Beckwith-Wiedemann syndrome NSD1* Nsd1   HomoloGene and HGNC')
        time.sleep(2)
        transgene_table = self.driver.find_element_by_id("transgeneTable")
        table = Table(transgene_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
        #displays each row of transgene data
        row1 = cells[2]
        self.assertEqual(row1.text, '  Beckwith-Wiedemann syndrome Tg(YACW408A5)1952Ricc 1 model')
        
    def test_dobrowser_genestab_m_hm(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse/human(GALC) and just mouse(Psap)
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:10587")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_link_text('Krabbe disease').click()
        self.driver.find_element_by_id('genesTabButton').click()#identifies the Genes tab and clicks it.
        time.sleep(2)
        gene_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(gene_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        row1 = cells[2]
        row2 = cells[3]
        self.assertEqual(row1.text, '       Krabbe disease GALC* Galc* 2 models HomoloGene and HGNC')
        self.assertEqual(row2.text, '       Krabbe disease PSAP Psap* 1 model HomoloGene and HGNC')
        
    def test_dobrowser_genestab_m(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to just mouse(Tfam)
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:12934")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_link_text('Kearns-Sayre syndrome').click()
        self.driver.find_element_by_id('genesTabButton').click()#identifies the Genes tab and clicks it.
        time.sleep(2)
        gene_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(gene_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        row1 = cells[2]
        self.assertEqual(row1.text, '       Kearns-Sayre syndrome TFAM Tfam* 2 models HomoloGene and HGNC')

    def test_dobrowser_genestab_ht(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to just human(IL6) Plus Transgene
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:8632")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_link_text("Kaposi's sarcoma").click()
        self.driver.find_element_by_id('genesTabButton').click()#identifies the Genes tab and clicks it.
        time.sleep(2)
        gene_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(gene_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        row1 = cells[2]
        self.assertEqual(row1.text, "       Kaposi's sarcoma IL6* Il6   HomoloGene and HGNC")
        time.sleep(2)
        transgene_table = self.driver.find_element_by_id("transgeneTable")
        table = Table(transgene_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
        #displays each row of transgene data
        row1 = cells[2]
        self.assertEqual(row1.text, "  Kaposi's sarcoma Tg(Acta2-RAC1*G12V)33Pjgc 2 models")
        
    def test_dobrowser_genestab_h(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to just human
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:0050807")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_link_text("Kahrizi syndrome").click()

        self.driver.find_element_by_id('genesTabButton').click()#identifies the Genes tab and clicks it.
        time.sleep(2)
        gene_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(gene_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        row1 = cells[2]
        self.assertEqual(row1.text, '       Kahrizi syndrome SRD5A3* Srd5a3   HomoloGene and HGNC')

    def test_dobrowser_genestab_m_h(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to just mouse/human(UBR1)
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:14694")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_link_text("Johanson-Blizzard syndrome").click()
        self.driver.find_element_by_id('genesTabButton').click()#identifies the Genes tab and clicks it.
        time.sleep(2)
        gene_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(gene_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        row1 = cells[2]
        self.assertEqual(row1.text, '       Johanson-Blizzard syndrome UBR1* Ubr1* 1 model HomoloGene and HGNC')
        
    def test_dobrowser_genestab_m_hh(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse/human(HAMP, HFE, HFE2, SLC40A1, TFR2) and just human(Bmp2)
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:2352")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_link_text('hemochromatosis').click()
        self.driver.find_element_by_id('genesTabButton').click()#identifies the Genes tab and clicks it.
        time.sleep(2)
        gene_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(gene_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
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
        self.assertEqual(row1.text, '       hemochromatosis type 1 HFE* Hfe* 13 models HomoloGene and HGNC')
        self.assertEqual(row2.text, 'hemochromatosis type 2A HFE2* Hfe2* 2 models HomoloGene and HGNC')
        self.assertEqual(row3.text, 'hemochromatosis type 2B HAMP* Hamp* 1 model HGNC')
        self.assertEqual(row4.text, 'hemochromatosis type 3 TFR2* Tfr2* 2 models HomoloGene and HGNC')
        self.assertEqual(row5.text, 'hemochromatosis type 4 SLC40A1* Slc40a1* 3 models HomoloGene and HGNC')
        self.assertEqual(row6.text, '       hemochromatosis B2M B2m* 1 model HomoloGene and HGNC')
        self.assertEqual(row7.text, 'hemochromatosis HMOX1 Hmox1* 1 model HomoloGene and HGNC')
        self.assertEqual(row8.text, '       hemochromatosis type 1 BMP2* Bmp2   HomoloGene and HGNC')
        self.assertEqual(row9.text, 'hemochromatosis type 5 FTH1* Fth1   HomoloGene and HGNC')
        
    def test_dobrowser_genestab_mult_homolog(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse and human but has multiple Mouse Homologs
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:633")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_link_text('myositis').click()
        self.driver.find_element_by_id('genesTabButton').click()#identifies the Genes tab and clicks it.
        time.sleep(2)
        gene_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(gene_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
        #displays each row of gene data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        self.assertEqual(row1.text, '       myositis HLA-A H2-K1*, Gm8909, Gm10499, H2-Bl, H2-D1, H2-Q1, H2-Q2, H2-Q4, H2-Q6, H2-Q7, H2-Q10 1 model HomoloGene and HGNC')
        self.assertEqual(row2.text, '       inclusion body myositis GNE* Gne 1 model HomoloGene and HGNC')
        self.assertEqual(row3.text, 'inclusion body myositis MYH2* Myh2   HomoloGene and HGNC')
        transgene_table = self.driver.find_element_by_id("transgeneTable")
        table = Table(transgene_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
        #displays each row of transgene data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        self.assertEqual(row1.text, '  inclusion body myositis Tg(Ckm-APPSw)A2Lfa 1 model')
        self.assertEqual(row2.text, '  inclusion body myositis Tg(Ckm-APPSw)A6Lfa 1 model')
        self.assertEqual(row3.text, '  myositis Tg(tetO-H2-K1)#Papl 1 model')

    def test_dobrowser_genestab_same_gene_mult_subtypes(self):
        '''
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse/human, mouse, and human. Genes COL1A1 and COL1A2 are attached multiple times
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:12347")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.find_element_by_link_text("osteogenesis imperfecta").click()
        self.driver.find_element_by_id('genesTabButton').click()#identifies the Models tab and clicks it.
        time.sleep(2)
        model_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(model_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
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
        
        self.assertEqual(row1.text, '       osteogenesis imperfecta type 1 COL1A1* Col1a1* 2 models HomoloGene and HGNC')
        self.assertEqual(row2.text, 'osteogenesis imperfecta type 10 SERPINH1* Serpinh1* 1 model HomoloGene and HGNC')
        self.assertEqual(row3.text, 'osteogenesis imperfecta type 2 COL1A1* Col1a1* 2 models HomoloGene and HGNC')
        self.assertEqual(row4.text, 'osteogenesis imperfecta type 3 COL1A1* Col1a1* 1 model HomoloGene and HGNC')
        self.assertEqual(row5.text, 'osteogenesis imperfecta type 3 COL1A2* Col1a2* 2 models HomoloGene and HGNC')
        self.assertEqual(row6.text, 'osteogenesis imperfecta type 4 COL1A1* Col1a1* 3 models HomoloGene and HGNC')
        self.assertEqual(row7.text, 'osteogenesis imperfecta type 6 SERPINF1* Serpinf1* 1 model HomoloGene and HGNC')
        self.assertEqual(row8.text, 'osteogenesis imperfecta type 7 CRTAP* Crtap* 1 model HomoloGene and HGNC')
        self.assertEqual(row9.text, 'osteogenesis imperfecta type 8 P3H1* P3h1* 1 model HomoloGene and HGNC')
        self.assertEqual(row10.text, 'osteogenesis imperfecta type 9 PPIB* Ppib* 2 models HomoloGene and HGNC')
        self.assertEqual(row11.text, '       osteogenesis imperfecta SMAD4 Smad4* 1 model HomoloGene and HGNC')
        self.assertEqual(row12.text, 'osteogenesis imperfecta COL1A2 Col1a2* 5 models HomoloGene and HGNC')
        self.assertEqual(row13.text, 'osteogenesis imperfecta type 2 SMPD3 Smpd3* 1 model HomoloGene and HGNC')
        self.assertEqual(row14.text, 'osteogenesis imperfecta type 3 SMPD3 Smpd3* 1 model HomoloGene and HGNC')
        self.assertEqual(row15.text, 'osteogenesis imperfecta type 5 SUCO Suco* 1 model HomoloGene and HGNC')
        self.assertEqual(row16.text, '       Cole-Carpenter syndrome P4HB* P4hb   HomoloGene and HGNC')
        self.assertEqual(row17.text, 'Cole-Carpenter syndrome SEC24D* Sec24d   HomoloGene and HGNC')
        self.assertEqual(row18.text, 'osteogenesis imperfecta type 11 FKBP10* Fkbp10   HomoloGene and HGNC')
        self.assertEqual(row19.text, 'osteogenesis imperfecta type 12 SP7* Sp7   HomoloGene and HGNC')
        self.assertEqual(row20.text, 'osteogenesis imperfecta type 13 BMP1* Bmp1   HomoloGene and HGNC')
        self.assertEqual(row21.text, 'osteogenesis imperfecta type 14 TMEM38B* Tmem38b   HomoloGene and HGNC')
        self.assertEqual(row22.text, 'osteogenesis imperfecta type 15 WNT1* Wnt1   HomoloGene and HGNC')
        self.assertEqual(row23.text, 'osteogenesis imperfecta type 17 SPARC* Sparc   HomoloGene and HGNC')
        self.assertEqual(row24.text, 'osteogenesis imperfecta type 2 COL1A2* Col1a2   HomoloGene and HGNC')
        self.assertEqual(row25.text, 'osteogenesis imperfecta type 4 COL1A2* Col1a2   HomoloGene and HGNC')
        self.assertEqual(row26.text, 'osteogenesis imperfecta type 5 IFITM5* Ifitm5   HomoloGene and HGNC')
        transgene_table = self.driver.find_element_by_id("transgeneTable")
        table = Table(transgene_table)
        cells = table.get_rows()
        print iterate.getTextAsList(cells)
        #displays each row of transgene data
        row1 = cells[2]
        self.assertEqual(row1.text, '  osteogenesis imperfecta type 1 Tg(COL1A1)73Prc 1 model')

            
        def tearDown(self):
            self.driver.close()
        '''
        def suite():
            suite = unittest.TestSuite()
            suite.addTest(unittest.makeSuite(TestAdd))
            return suite
        '''
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    HTMLTestRunner.main() 
