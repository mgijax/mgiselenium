"""
Created on Feb 7, 2017
These tests are for verifying information found on the Models tab of the Disease Ontology Browser
@author: jeffc
Verify term line header section
Verify results that have NOT models
Verify multiple results for various result combinations
Verify results for same genes with multiple subtypes
Verify results that has only NOT models
Verify genetic background strain link
"""
import os.path
import sys
import time
import tracemalloc
import unittest

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import config
from util import iterate
from util.table import Table

# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)


# Tests
tracemalloc.start()
class TestDoBrowserModelTab(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL)
        self.driver.implicitly_wait(10)
        
    def test_dobrowser_header(self):
        """
        @status this test verifies the term line in the header section on the DO browser page is correct.
        """
        print("BEGIN test_dobrowser_header")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:1324")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'lung cancer').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        header = self.driver.find_element(By.ID, 'diseaseNameID')#identifies the header section of the DO Browser page
        print(header.text)
        
        self.assertEqual(header.text, "lung cancer (DOID:1324)")
        syn = self.driver.find_element(By.ID, 'diseaseSynonym')#identifies the synonym line in the header section of the DO Browser page
        print(syn.text)
        
        self.assertEqual(syn.text, "lung neoplasm")
        alt_id = self.driver.find_element(By.ID, 'diseaseSecondaryIDs')#identifies the alternate IDs line of the header section of the DO Browser page
        print(alt_id.text)
        
        self.assertEqual(alt_id.text, "OMIM:211980, OMIM:608935, OMIM:612571, OMIM:612593, OMIM:614210, DOID:13075, DOID:1322, DOID:9881, ICD10CM:C34.1, ICD10CM:C34.2, ICD10CM:C34.3, ICD9CM:162.3, ICD9CM:162.4, ICD9CM:162.5, ICD9CM:162.8, UMLS_CUI:C0024624, UMLS_CUI:C0153491, UMLS_CUI:C0153492, UMLS_CUI:C0153493")
        # locates and verifies the definition
        definition = self.driver.find_element(By.ID, 'diseaseDefinition')#identifies the Definition line of the header section of the DO Browser page
        print(definition.text)
        
        self.assertEqual(definition.text, "A respiratory system cancer that is located_in the lung.")
        
    def test_dobrowser_modeltab_mh_m_not(self):
        """
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse/human(6), just mouse(1), and 3 NOT models
        """
        print("BEGIN test_dobrowser_modeltab_mh_m_not")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:0050646")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'distal arthrogryposis').click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(By.ID, 'modelsTabButton').click()#identifies the Models tab and clicks it.
        model_table = self.driver.find_element(By.ID, "modelTabTable")
        table = Table(model_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of disease model data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        row4 = cells[5]
        row5 = cells[6]
        row6 = cells[7]
        row7 = cells[8]
        row8 = cells[9]
        row9 = cells[10]

        self.assertEqual(row1.text, '         distal arthrogryposis b2b2966Clo/b2b2966Clo C57BL/6J-b2b2966Clo J:175213 View')
        self.assertEqual(row2.text, 'distal arthrogryposis Ecel1em1Hiki/Ecel1em1Hiki\nTg(Hlxb9-GFP)1Tmj/0 involves: C57BL/6 * CBA J:262090 View')
        self.assertEqual(row3.text, 'distal arthrogryposis Ecel1tm1Hiki/Ecel1tm1Hiki\nTg(Hlxb9-GFP)1Tmj/0 involves: 129S1/Sv * 129X1/SvJ * C57BL/6 * CBA J:262090 View')
        self.assertEqual(row4.text, 'distal arthrogryposis Fbn2fp-4J/Fbn2fp-4J BALB/cByJ-Fbn2fp-4J/GrsrJ J:222308 View')
        self.assertEqual(row5.text, 'distal arthrogryposis Fbn2mz/Fbn2mz involves: BALB/cAnNCrl * C3H/HeH J:157998 View')
        self.assertEqual(row6.text, 'distal arthrogryposis Fbn2tm1Rmz/Fbn2tm1Rmz either: (involves: 129/Sv) or (involves: 129/Sv * C57BL/6J) J:70592 View')
        self.assertEqual(row7.text, 'distal arthrogryposis Fbn2tm1Rmz/Fbn2tm1Rmz involves: 129S/SvEv J:166786 View')
        self.assertEqual(row8.text, 'distal arthrogryposis Tnni2tm1Sgao/Tnni2+ involves: 129 * ICR J:228857 View')
        self.assertEqual(row9.text, 'distal arthrogryposis Tnni2tm1Sgao/Tnni2tm1Sgao involves: 129 * ICR J:228857 View')

        notmodel_table = self.driver.find_element(By.ID, 'modelTabNotTable')
        table = Table(notmodel_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of NOT models data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        
        self.assertEqual(row1.text, 'NOT Models         distal arthrogryposis Fbn2fp-2J/Fbn2fp-2J involves: C57BL/6J * C.B10-H2b/LiMcdJ J:68881 View')
        self.assertEqual(row2.text, 'distal arthrogryposis Fbn2fp/Fbn2fp C3Fe(B6)-Fbn2fp/J J:68881 View')
        self.assertEqual(row3.text, 'distal arthrogryposis sy/sy B6C3Fe-a/a J:68881 View')
                
    def test_dobrowser_modelstab_trans_not(self):
        """
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to Transgenes and other mutations model(1) and 1 NOT model
        @note: this test no longer has a Transgene result, need to find a new example !!!!!!
        """
        print("BEGIN test_dobrowser_modeltab_trans_not")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:14748")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'Sotos syndrome').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(By.ID, 'modelsTabButton').click()#identifies the Models tab and clicks it.
        
        model_table = self.driver.find_element(By.ID, 'modelTabTable')
        table = Table(model_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of disease model data
        row1 = cells[2]
        row2 = cells[3]
        print(row1)
        self.assertEqual(row1.text, '         Sotos syndrome 2 Nfixtm1.1Rmg/Nfix+ involves: 129S4/SvJae * C57BL/6J J:295051 View')
        self.assertEqual(row2.text, '         Sotos syndrome Del(13Simc1-B4galt7)2Dja/+ involves: 129P2/OlaHsd * 129S7/SvEvBrd * C57BL/6J J:190741 View')
        
        notmodel_table = self.driver.find_element(By.ID, 'modelTabNotTable')
        table = Table(notmodel_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of NOT models data
        row1 = cells[2]
        self.assertEqual(row1.text, 'NOT Models         Sotos syndrome Nsd1tm1.1Pcn/Nsd1tm1.1Pcn involves: 129/Sv * C57BL/6 J:83923 View')
                
    def test_dobrowser_modelstab_mh_nots(self):
        """
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse/human(8) and NOTs(4)
        """
        print("BEGIN test_dobrowser_modeltab_mh_nots")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:11949")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'Creutzfeldt-Jakob disease').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'termTabButton'))):
            print('page loaded')
        self.driver.find_element(By.ID, 'modelsTabButton').click()#identifies the Models tab and clicks it.
        model_table = self.driver.find_element(By.ID, 'modelTabTable')
        table = Table(model_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of disease model data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        row4 = cells[5]
        row5 = cells[6]
        row6 = cells[7]
        row7 = cells[8]
        row8 = cells[9]
        
        self.assertEqual(row1.text, '         Creutzfeldt-Jakob disease Prnptm1(PRNP)Tkit/Prnptm1(PRNP)Tkit Not Specified J:86603 View')
        self.assertEqual(row2.text, 'Creutzfeldt-Jakob disease Prnptm1Cwe/Prnptm1Cwe\nTg(Prnp*)#Rgab/0 involves: 129S7/SvEvBrd * C57BL/6 * FVB/N J:183170 View')
        self.assertEqual(row3.text, 'Creutzfeldt-Jakob disease Prnptm1Cwe/Prnptm1Cwe\nTg(Prnp*D177N*M128V)A21Rchi/0 involves: 129S7/SvEvBrd * C57BL/6 * CBA J:142098 View')
        self.assertEqual(row4.text, 'Creutzfeldt-Jakob disease Prnptm1Cwe/Prnptm1Cwe\nTg(Prnp*D177N*M128V)A21Rchi/Tg(Prnp*D177N*M128V)A21Rchi involves: 129S7/SvEvBrd * C57BL/6 * CBA J:142098 View')
        self.assertEqual(row5.text, 'Creutzfeldt-Jakob disease Prnptm3Lnq/Prnptm3Lnq involves: 129P2/OlaHsd * C57BL/6N J:200974 View')        
        self.assertEqual(row6.text, 'Creutzfeldt-Jakob disease Tg(Prnp*)#Rgab/0 involves: C57BL/6 * FVB/N J:183170 View')
        self.assertEqual(row7.text, 'Creutzfeldt-Jakob disease Tg(Prnp*D177N*M128V)A21Rchi/0 involves: C57BL/6 * CBA J:142098 View')
        self.assertEqual(row8.text, 'Creutzfeldt-Jakob disease Tg(Prnp*D177N*M128V)A21Rchi/Tg(Prnp*D177N*M128V)A21Rchi involves: C57BL/6 * CBA J:142098 View')
        
        notmodel_table = self.driver.find_element(By.ID, 'modelTabNotTable')
        table = Table(notmodel_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of NOT models data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        row4 = cells[5]
        self.assertEqual(row1.text, 'NOT Models         Creutzfeldt-Jakob disease Prnptm1Cwe/Prnptm1Cwe involves: 129S7/SvEvBrd * C57BL/6 J:472 View')
        self.assertEqual(row2.text, 'Creutzfeldt-Jakob disease Prnptm1Edin/Prnptm1Edin 129P2/OlaHsd-Prnptm1Edin/EdinH J:58820 View')
        self.assertEqual(row3.text, 'Creutzfeldt-Jakob disease Prnptm1Miy/Prnptm1Miy involves: 129S4/SvJae * C57BL/6 J:69186 View')
        self.assertEqual(row4.text, 'Creutzfeldt-Jakob disease Prnptm1Rcm/Prnptm1Rcm 129P2/OlaHsd-Prnptm1Rcm J:45908 View')
        
        
                
    def test_dobrowser_modelstab_mh_m_h_nots(self):
        """
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse/human, mouse and human. Also has NOTS
        @bug currently not displaying human associations
        """
        print("BEGIN test_dobrowser_modeltab_mh_m_h_nots")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:5572")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'Beckwith-Wiedemann syndrome').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'termTabButton'))):
            print('page loaded')
        self.driver.find_element(By.ID, 'modelsTabButton').click()#identifies the Models tab and clicks it.
        
        model_table = self.driver.find_element(By.ID, 'modelTabTable')
        table = Table(model_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of disease model data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        
        self.assertEqual(row1.text, '         Beckwith-Wiedemann syndrome Cdkn1ctm1Sje/Cdkn1ctm1Sje involves: 129S7/SvEvBrd * C57BL/6 J:40203 View')
        self.assertEqual(row2.text, 'Beckwith-Wiedemann syndrome Tg(YACW408A5)1952Ricc/0 involves: 129/Sv * SD7 J:96366 View')        
        self.assertEqual(row3.text, '         Beckwith-Wiedemann syndrome Sptbn1tm1Mish/Sptbn1+ involves: 129S6/SvEvTac J:166879 View')
        
        notmodel_table = self.driver.find_element(By.ID, 'modelTabNotTable')
        table = Table(notmodel_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of NOT models data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        self.assertEqual(row1.text, 'NOT Models         Beckwith-Wiedemann syndrome Cdkn1ctm1Bbd/Cdkn1ctm1Bbd involves: 129S1/Sv * 129X1/SvJ * C57BL/6 J:40142 View')
        self.assertEqual(row2.text, 'Beckwith-Wiedemann syndrome Cdkn1ctm1Kat/Cdkn1ctm1Kat involves: 129P2/OlaHsd * C57BL/6 J:61190 View')
        self.assertEqual(row3.text, 'Beckwith-Wiedemann syndrome Kcnq1tm1Apf/Kcnq1tm1Apf involves: 129P2/OlaHsd * C57BL/6 J:66428 View')
                
    def test_dobrowser_modelstab_mh_h_not(self):
        """
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse/human, human and 4 NOT
        """
        print("BEGIN test_dobrowser_modeltab_mh_h_not")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:0050771")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'pheochromocytoma').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'termTabButton'))):
            print('page loaded')
        self.driver.find_element(By.ID, 'modelsTabButton').click()#identifies the Models tab and clicks it.
        
        model_table = self.driver.find_element(By.ID, 'modelTabTable')
        table = Table(model_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of disease model data
        row1 = cells[2]
        row2 = cells[3]
        
        self.assertEqual(row1.text, '         pheochromocytoma Rettm2.1Cos/Rettm2.1Cos involves: 129S1/Sv * C57BL/6J * FVB/N J:60659 View')
        self.assertEqual(row2.text, '         pheochromocytoma Ptentm1Mro/Ptentm1Mro\nSdhbtm1.1Ics/Sdhb+\nTg(KLK3-cre)D4Trp/0 involves: 129S2/SvPas * FVB J:236514 View')
        
        notmodel_table = self.driver.find_element(By.ID, 'modelTabNotTable')
        table = Table(notmodel_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays rows of NOT models data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        row4 = cells[5]
        row5 = cells[6]
        
        self.assertEqual(row1.text, 'NOT Models         paraganglioma Sdhctm1c(EUCOMM)Wtsi/Sdhctm1c(EUCOMM)Wtsi\nGt(ROSA)26Sortm1.1(rtTA,tetO-cre)Bkmn/Gt(ROSA)26Sor+ involves: 129S1/Sv * 129X1/SvJ * C57BL/6N J:284745 View')
        self.assertEqual(row2.text, 'paraganglioma Sdhdtm1Jlob/Sdhd+ involves: 129X1/SvJ J:95252 View')
        self.assertEqual(row3.text, 'paraganglioma Sdhdtm1Jlob/Sdhdtm1Jlob involves: 129X1/SvJ J:95252 View')
        self.assertEqual(row4.text, 'paraganglioma Sdhdtm1Jpb/Sdhd+ either: 129P2/OlaHsd-Sdhdtm1Jpb or (involves: 129P2/OlaHsd * C57BL/6J) J:155380 View')
        self.assertEqual(row5.text, 'pheochromocytoma Rettm1Cos/Rettm2.1Cos involves: 129S/SvEv * 129S1/Sv * C57BL/6J * FVB/N * MF1 J:60659 View')
                
    def test_dobrowser_modelstab_m_trans_complex_not(self):
        """
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse, transgenes, and complex, also has 1 NOT
        """
        print("BEGIN test_dobrowser_modeltab_m_trans_complex_not")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:7148")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'rheumatoid arthritis').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'termTabButton'))):
            print('page loaded')
        self.driver.find_element(By.ID, 'modelsTabButton').click()#identifies the Models tab and clicks it.
        
        model_table = self.driver.find_element(By.ID, 'modelTabTable')
        table = Table(model_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of disease model data
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
        self.assertEqual(row1.text, '         rheumatoid arthritis TnfBpsm1/Tnf+ involves: C57BL/6 J:226052 View')
        self.assertEqual(row2.text, 'rheumatoid arthritis TnfBpsm1/TnfBpsm1 involves: C57BL/6 J:226052 View')
        self.assertEqual(row3.text, 'rheumatoid arthritis Tnftm1Gkl/Tnftm2Gkl involves: 129S/SvEv * C57BL/6 J:54056 View')
        self.assertEqual(row4.text, 'rheumatoid arthritis Tnftm2Gkl/Tnf+ involves: 129S/SvEv * C57BL/6 J:54056 View')
        self.assertEqual(row5.text, 'rheumatoid arthritis Tnftm2Gkl/Tnf+ involves: 129S/SvEv * C57BL/6J J:264147 View')
        self.assertEqual(row6.text, 'rheumatoid arthritis Tnftm2Gkl/Tnftm2Gkl involves: 129S/SvEv * C57BL/6 J:54056 View')
        self.assertEqual(row7.text, '         rheumatoid arthritis Dnase2atm1Osa/Dnase2atm1Osa\nIfnar1tm1Agt/Ifnar1tm1Agt involves: 129S1/Sv * 129S2/SvPas * 129X1/SvJ * C57BL/6 J:114982, J:238323 View')
        self.assertEqual(row8.text, 'rheumatoid arthritis Dnase2atm1Osa/Dnase2atm2Osa\nTg(Mx1-cre)1Cgn/0 involves: 129S1/Sv * 129S2/SvPas * 129X1/SvJ * C57BL/6 * CBA J:114982 View')
        self.assertEqual(row9.text, 'rheumatoid arthritis Il6sttm1Thir/Il6sttm1Thir involves: 129 * C57BL/6 J:133059 View')
        self.assertEqual(row10.text, 'rheumatoid arthritis Mmp14tm1Hbh/Mmp14tm1Hbh involves: 129P2/OlaHsd * Black Swiss J:57969 View')
        self.assertEqual(row11.text, 'rheumatoid arthritis Zap70m1Saka/Zap70m1Saka involves: BALB/c J:86607 View')
        self.assertEqual(row12.text, 'rheumatoid arthritis Zfp36tm1Pjb/Zfp36tm1Pjb B6.Cg-Zfp36tm1Pjb J:214114 View')
        self.assertEqual(row13.text, 'Transgenes and\nOther Mutations        rheumatoid arthritis H2b/H2g7\nTg(TcraR28,TcrbR28)KRNDim/0 involves: C57BL/6 * NOD * SJL J:36815 View')
        self.assertEqual(row14.text, 'rheumatoid arthritis Tg(CAG-SYVN1)1Tn/? D1.Cg-Tg(CAG-SYVN1)1Tn J:86009 View')
        self.assertEqual(row15.text, 'rheumatoid arthritis Tg(FCGR2A)11Mkz/Tg(FCGR2A)11Mkz involves: C57BL/6 * SJL J:136516 View')
        self.assertEqual(row16.text, 'rheumatoid arthritis Tg(HLA-DRA*0101,HLA-DRB1*0101)1Dmz/Tg(HLA-DRA*0101,HLA-DRB1*0101)1Dmz involves: C57BL/6 * C57BL/10Sn * SJL/J J:108635 View')
        self.assertEqual(row17.text, 'rheumatoid arthritis Tg(TcraR28,TcrbR28)KRNDim/0 involves: C57BL/6 * NOD * SJL J:36815 View')
        self.assertEqual(row18.text, 'rheumatoid arthritis Tg(TNF)197Gkl/0 involves: C57BL/6 * CBA J:92576 View')
        self.assertEqual(row19.text, 'rheumatoid arthritis Tg(TNF)3647Gkl/0 involves: C57BL/6 * CBA J:190204 View')
        self.assertEqual(row20.text, 'Additional\nComplex\nModels        rheumatoid arthritis H2q/?\nNcf1m1J/Ncf1m1J B6.Cg-Ncf1m1J H2q J:92437 View')
        
        notmodel_table = self.driver.find_element(By.ID, 'modelTabNotTable')
        table = Table(notmodel_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of NOT models data
        row1 = cells[2]
        self.assertEqual(row1.text, 'NOT Models         rheumatoid arthritis Ighmtm1Cgn/Ighmtm1Cgn\nTg(TcraR28,TcrbR28)KRNDim/0 involves: 129S2/SvPas * C57BL/6 * NOD * SJL J:36815 View')
                
        
    def test_dobrowser_modelstab_m_h_trans(self):
        """
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse, human and transgene, can be better used as a Genes Tab test.
        """
        print("BEGIN test_dobrowser_modeltab_m_h_trans")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:633")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'myositis').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'termTabButton'))):
            print('page loaded')
        self.driver.find_element(By.ID, 'modelsTabButton').click()#identifies the Models tab and clicks it.        
        model_table = self.driver.find_element(By.ID, 'modelTabTable')
        table = Table(model_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of gene data
        row1 = cells[2]
        row2 = cells[3]
        row3 = cells[4]
        row4 = cells[5]
        row5 = cells[6]
        
        self.assertEqual(row1.text, 'Transgenes and\nOther Mutations        dermatomyositis Tg(Krt14-Angptl2)1Yo/0 C.Cg-Tg(Krt14-Angptl2)1Yo J:181261 View')
        self.assertEqual(row2.text, 'inclusion body myositis Tg(Ckm-APPSw)A2Lfa/0 involves: C57BL/6 * SJL J:76338 View')
        self.assertEqual(row3.text, 'inclusion body myositis Tg(Ckm-APPSw)A6Lfa/0 involves: C57BL/6 * SJL J:76338 View')
        self.assertEqual(row4.text, 'myositis Tg(CKMM-tTA)A3Rhvh/0\nTg(tetO-H2-K1)#Papl/0 B6.Cg-Tg(CKMM-tTA)A3Rhvh Tg(tetO-H2-K1)#Papl J:205907 View')
        self.assertEqual(row5.text, 'Additional\nComplex\nModels        inclusion body myositis Gnetm1Sngi/Gnetm1Sngi\nTg(ACTB-GNE*D176V)9Sngi/0 involves: C57BL/6 J:117854 View')
        
    def test_dobrowser_modelstab_h(self):
        """
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to just human
        """
        print("BEGIN test_dobrowser_modeltab_h")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:3132")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'porphyria cutanea tarda').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'termTabButton'))):
            print('page loaded')
        self.driver.find_element(By.ID, 'modelsTabButton').click()#identifies the Models tab and clicks it.
        model_table = self.driver.find_element(By.ID, 'modelTabTable')
        table = Table(model_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of disease model data
        row1 = cells[2]
        self.assertEqual(row1.text, '         porphyria cutanea tarda Hfetm2Nca/Hfetm2Nca\nUrodtm1Kush/Urod+ involves: C57BL/6J J:66704 View')

    def test_dobrowser_modelstab_same_gene_mult_subtypes(self):
        """
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to mouse/human and mouse. Genes COL1A1 and COL1A2 are attached multiple times
        """
        print("BEGIN test_dobrowser_modeltab_same_gene_mult_subtypes")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:12347")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'osteogenesis imperfecta').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'termTabButton'))):
            print('page loaded')
        self.driver.find_element(By.ID, 'modelsTabButton').click()#identifies the Models tab and clicks it.
        
        model_table = self.driver.find_element(By.ID, 'modelTabTable')
        table = Table(model_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of disease model data
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
        self.assertEqual(row1.text, '         osteogenesis imperfecta Col1a1m1Btlr/Col1a1m1Btlr C57BL/6J-Col1a1m1Btlr J:253622 View')
        self.assertEqual(row2.text, 'osteogenesis imperfecta Col1a2oim/Col1a2+ B6C3Fe a/a-Col1a2oim/J J:38013 View')
        self.assertEqual(row3.text, 'osteogenesis imperfecta Col1a2tm1.1Mcbr/Col1a2+ (A/J x B6.129-Col1a2tm1.1Mcbr)F1 J:178743 View')
        self.assertEqual(row4.text, 'osteogenesis imperfecta Col1a2tm1.1Mcbr/Col1a2+ (BALB/cByJ x B6.129-Col1a2tm1.1Mcbr)F1 J:178743 View')
        self.assertEqual(row5.text, 'osteogenesis imperfecta Col1a2tm1.1Mcbr/Col1a2+ (C3H/HeJ x B6.129-Col1a2tm1.1Mcbr)F1 J:178743 View')
        self.assertEqual(row6.text, 'osteogenesis imperfecta Col1a2tm1.1Mcbr/Col1a2+ (FVB/NJ x B6.129-Col1a2tm1.1Mcbr)F1 J:178743 View')
        self.assertEqual(row7.text, 'osteogenesis imperfecta type 1 Col1a1Mov13/Col1a1+ involves: C57BL/6 J:107045 View')
        self.assertEqual(row8.text, 'osteogenesis imperfecta type 2 Col1a1Aga2/Col1a1+ involves: C3HeB/FeJ * C57BL/6J J:129569 View')
        self.assertEqual(row9.text, 'osteogenesis imperfecta type 2 Col1a1tm1Jcm/Col1a1+ either: (involves: 129X1/SvJ * C3H/HeJ) or (involves: 129X1/SvJ * CD-1) J:59168 View')
        self.assertEqual(row10.text, 'osteogenesis imperfecta type 3 Col1a1Aga2/Col1a1+ C3HeB/FeJ-Col1a1Aga2 J:185988 View')
        self.assertEqual(row11.text, 'osteogenesis imperfecta type 3 Col1a2oim/Col1a2oim B6C3Fe a/a-Col1a2oim/J J:38013 View')
        self.assertEqual(row12.text, 'osteogenesis imperfecta type 3 Col1a2oim/Col1a2oim involves: C3H/HeJ * C57BL/6JLe J:4348 View')
        self.assertEqual(row13.text, 'osteogenesis imperfecta type 4 Col1a1M1Jrt/Col1a1+ involves: C3H/HeJ * C57BL/6J * FVB/NJ J:216423 View')
        self.assertEqual(row14.text, 'osteogenesis imperfecta type 4 Col1a1M1Jrt/Col1a1+ involves: C57BL/6 * FVB/N J:228439 View')
        self.assertEqual(row15.text, 'osteogenesis imperfecta type 4 Col1a1tm1.1Jcm/Col1a1+ either: (involves: 129X1/SvJ * C3H/HeJ) or (involves: 129X1/SvJ * CD-1) J:59168 View')
        self.assertEqual(row16.text, 'osteogenesis imperfecta type 6 Serpinf1tm1Craw/Serpinf1tm1Craw Not Specified J:230409 View')
        self.assertEqual(row17.text, 'osteogenesis imperfecta type 7 Crtaptm1Brle/Crtaptm1Brle involves: 129S7/SvEvBrd J:116096 View')
        self.assertEqual(row18.text, 'osteogenesis imperfecta type 8 P3h1tm1Dgen/P3h1tm1Dgen involves: C57BL/6 J:163884 View')
        self.assertEqual(row19.text, 'osteogenesis imperfecta type 9 PpibGt(RST139)Byg/PpibGt(RST139)Byg involves: 129P2/OlaHsd * C57BL/6 J:226318 View')
        self.assertEqual(row20.text, 'osteogenesis imperfecta type 9 Ppibtm1.1Rjb/Ppibtm1.1Rjb Not Specified J:161748 View')
        self.assertEqual(row21.text, 'osteogenesis imperfecta type 10 Serpinh1tm2Kzn/Serpinh1tm2Kzn\nTg(Col2a1-cre)1Bhr/0 involves: 129S6/SvEvTac * C57BL/6 * C57BL/6J * SJL J:197791 View')
        self.assertEqual(row22.text, '         osteogenesis imperfecta Smad4tm2.1Cxd/Smad4tm2.1Cxd\nTg(Sp7-tTA,tetO-EGFP/cre)1Amc/0 involves: 129S6/SvEvTac * C57BL/6J * CD-1 J:211171 View')
        self.assertEqual(row23.text, 'osteogenesis imperfecta Smpd3fro/Smpd3fro Not Specified J:100158 View')
        self.assertEqual(row24.text, 'osteogenesis imperfecta type 2 Smpd3fro/Smpd3fro Not Specified J:3906 View')
        self.assertEqual(row25.text, 'osteogenesis imperfecta type 3 Smpd3fro/Smpd3fro Not Specified J:3906 View')
        self.assertEqual(row26.text, 'osteogenesis imperfecta type 5 SucoGt(KST050)Byg/SucoGt(KST050)Byg involves: 129P2/OlaHsd * C57BL/6 * CD-1 J:159823 View')
        self.assertEqual(row27.text, '         osteogenesis imperfecta type 5 Tg(Col1a1-Ifitm5*)1Brle/0 involves: FVB/N J:233366 View')
        self.assertEqual(row28.text, 'Transgenes and\nOther Mutations        osteogenesis imperfecta type 1 Tg(COL1A1)73Prc/0 involves: FVB/N J:146429 View')
        self.assertEqual(row29.text, 'Additional\nComplex\nModels        osteogenesis imperfecta Bmp1tm1.1Dgr/Bmp1tm1.1Dgr\nTll1tm2.1Dgr/Tll1tm2.1Dgr\nNdor1Tg(UBC-cre/ERT2)1Ejb/0 involves: 129S/SvEv * 129S6/SvEvTac * C57BL/6 * SJL J:210366 View')

    def test_dobrowser_modelstab_not_only(self):
        """
        @status this test verifies the correct genes, models and source are returned. This test example displays a disease that returns
        results for associations to only a NOT
        """
        print("BEGIN test_dobrowser_modeltab_not_only")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:10126")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, 'keratoconus').click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'termTabButton'))):
            print('page loaded')
        self.driver.find_element(By.ID, 'modelsTabButton').click()#identifies the Models tab and clicks it.
        
        notmodel_table = self.driver.find_element(By.ID, 'modelTabNotTable')
        table = Table(notmodel_table)
        cells = table.get_rows()
        print(iterate.getTextAsList(cells))
        # displays each row of NOT models data
        row1 = cells[2]
        row2 = cells[3]
        self.assertEqual(row1.text, 'NOT Models         keratoconus Vsx1tm1Mci/Vsx1tm1Mci either: (involves: 129S1/Sv * 129S1/SvImJ * 129X1/SvJ) or (involves: 129S1/Sv * 129X1/SvJ * Black Swiss) J:88182 View')
        self.assertEqual(row2.text, 'keratoconus Vsx1tm2Mci/Vsx1tm2Mci either: (involves: 129S1/Sv * 129S1/SvImJ * 129X1/SvJ) or (involves: 129S1/Sv * 129X1/SvJ * Black Swiss) J:88182 View')

    def test_dobrowser_modelstab_strain_link(self):
        """
        @status this test verifies that strains listed in the Genetic Background column link to their strain detail page
        @note do-results-model-1
        """
        print("BEGIN test_dobrowser_modeltab_strain_link")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:14330")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(2)
        # find the Vocabulary Term tab and click it
        self.driver.find_element(By.ID, 'vLink').click()
        self.driver.find_element(By.LINK_TEXT, "Parkinson's disease").click()
        # switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'termTabButton'))):
            print('page loaded')
        self.driver.find_element(By.ID, 'modelsTabButton').click()#identifies the Models tab and clicks it.
        # Find the link in the Genetic Background column C57BL/6J-Tg(SNCA)ARyot and click it
        strainlink = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'C57BL/6J-Tg')
        self.driver.execute_script("arguments[0].click();", strainlink)
        # switch focus to the new tab for strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # Asserts that the strain page is for the correct strain
        assert "C57BL/6J-Tg(SNCA)ARyot" in self.driver.page_source  
        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(TestDoBrowserModelTab))
        return suite
        
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
