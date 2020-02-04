'''
Created on Mar 24, 2017
These tests are for verifying the functionality and data for the Mouse model popup found off the Genes tab results
@author: jeffc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

class TestDoBrowserModelsPopup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL)
        self.driver.implicitly_wait(10)
        
    def test_dobrowser_modelspopup_tableheaders(self):
        '''
        @status this test verifies the header section on the DO browser mouse models popup page is correct, this is for the 
        headings Human Disease Modeled and Associated Mouse Gene.
        '''
        print ("BEGIN test_dobrowser_modelspopup_tableheaders")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:1324")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, 'lung cancer').click()
        
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, 'geneTabTable')
        table = Table(gene_table)
        #cells = table.get_rows()
        cell = table.get_cell(6, 3)
        #Identify the data found in the Mouse Models column for the fifth row(for marker Robo1)
        print cell.text
        cell.find_element(By.LINK_TEXT, '1 model').click()
        
        self.driver.switch_to_window(self.driver.window_handles[-1])
        header = self.driver.find_element(By.ID, 'diseaseBrowserModelsPopup')
        model_heading = header.find_element(By.ID, 'diseaseDisplay')
        print model_heading.text
        
        #assert that the Human Disease Modeled heading above the table is correct
        self.assertEquals(model_heading.text, "lung cancer")
        
        assoc_gene_heading = header.find_element(By.ID, 'markerDisplay')
        print assoc_gene_heading.text
        
        #assert that the Associated Mouse Gene heading above the table is correct
        self.assertEquals(assoc_gene_heading.text, "Robo1")
        
    def test_dobrowser_modelspopup_tableheaders2(self):
        '''
        @status this test verifies the header section on the DO browser mouse models popup page is correct, this is for the 
        headings Human Disease Modeled and Associated Mouse Gene. This second test is to verify when the disease name has changed
        '''
        print ("BEGIN test_dobrowser_modelspopup_tableheaders2")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:1324")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, 'lung cancer').click()
        
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, 'geneTabTable')
        table = Table(gene_table)
        #cells = table.get_rows()
        cell = table.get_cell(8, 3)
        #Identify the data found in the Mouse Models column for the second row(for marker Fgfp)
        print cell.text
        cell.find_element(By.LINK_TEXT, '1 model').click()
        
        self.driver.switch_to_window(self.driver.window_handles[-1])
        header = self.driver.find_element(By.ID, 'diseaseBrowserModelsPopup')
        model_heading = header.find_element(By.ID, 'diseaseDisplay')
        print model_heading.text
        
        #assert that the Human Disease Modeled heading above the table is correct
        self.assertEquals(model_heading.text, "pleuropulmonary blastoma")
        
        assoc_gene_heading = header.find_element(By.ID, 'markerDisplay')
        print assoc_gene_heading.text
        
        #assert that the Associated Mouse Gene heading above the table is correct
        self.assertEquals(assoc_gene_heading.text, "Fgf9")        
        
    def test_dobrowser_modelspopup_onlynots(self):
        '''
        @status this test verifies the display of disease model popup when only NOTs are returned.
        '''
        print ("BEGIN test_dobrowser_modelspopup_onlynots")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:0050581")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, 'brachydactyly').click()
        
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, 'geneTabTable')
        table = Table(gene_table)
        cell = table.get_cell(10, 3)
        #Identify the data found in the Mouse Models column for the ninth row(for marker ROR2)
        print cell.text
        cell.find_element(By.LINK_TEXT, '1 "NOT" model').click()
        
        self.driver.switch_to_window(self.driver.window_handles[-1])
        model_table = self.driver.find_element(By.ID, 'diseaseBrowserNotModelPopupTable')
        table1 = Table(model_table)
        #print table1
        row1 = table1.get_row(1)
        #assert the data in the table's first row is correct
        self.assertEquals(row1.text, 'Ror2tm1Anec/Ror2+ B6.129S1-Ror2tm1Anec J:134490 View', 'Wrong data displayed for row 1!')
        print row1.text
        
    def test_dobrowser_modelspopup_onlyhuman(self):
        '''
        @status this test verifies the display of disease model popup when only human data is returned.
        '''
        print ("BEGIN test_dobrowser_modelspopup_onlyhuman")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:10652")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, "Alzheimer's disease").click()
        
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, 'geneTabTable')
        table = Table(gene_table)
        #cells = table.get_rows()
        cell = table.get_cell(21, 3)
        #Identify the data found in the Mouse Models column for the twenth row(for marker PSEN2)
        print cell.text
        cell.find_element(By.LINK_TEXT, '1 model').click()
        
        self.driver.switch_to_window(self.driver.window_handles[-1])
        model_table = self.driver.find_element(By.ID, 'diseaseBrowserModelPopupTable')
        table1 = Table(model_table)
        #print table1
        row1 = table1.get_row(1)
        #assert the table data for row 1 is correct
        self.assertEquals(row1.text, 'Psen1tm1Jzt/Psen1tm1Jzt\nPsen2tm1Ber/Psen2tm1Ber\nTg(Camk2a-cre)T29-1Stl/0 involves: C57BL/6 * CBA J:90685 View', 'Wrong data displayed for row 1!')
        print row1.text
        
    def test_dobrowser_modelspopup_mouse_nots(self):
        '''
        @status this test verifies the display of disease model popup when you have mouse and NOTs returned.
        '''
        print ("BEGIN test_dobrowser_modelspopup_mouse_nots")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:9744")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, 'type 1 diabetes mellitus').click()
        
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, 'geneTabTable')
        table = Table(gene_table)
        cell = table.get_cell(11, 3)
        #Identify the data found in the Mouse Models column for the tenth row(for marker Ighm)
        print cell.text
        cell.find_element(By.LINK_TEXT, '5 models').click()
        
        self.driver.switch_to_window(self.driver.window_handles[-1])
        model_table = self.driver.find_element(By.ID, 'diseaseBrowserModelPopupTable')
        table1 = Table(model_table)
        #print table1
        #asserts that each row of data in the table is correct
        row1 = table1.get_row(1)
        self.assertEquals(row1.text, 'Ighmtm1Cgn/Ighmtm1Cgn\nTg(Igh-VB1-8/Igh-6m)1Mjsk/? NODCaj.Cg-Ighmtm1Cgn Tg(Igh-VB1-8/Igh-6m)1Mjsk/FswJ J:93190 View', 'Wrong data displayed for row 2!')
        row2 = table1.get_row(2)
        self.assertEquals(row2.text, 'Tg(Igh-6/Igh-V281)3Jwt/0 NOD.B6-Tg(Igh-6/Igh-V281)3Jwt J:91865 View', 'Wrong data displayed for row 1!')
        row3 = table1.get_row(3)
        self.assertEquals(row3.text, 'Tg(Igh-6/Igh-V125)2Jwt/0\nTg(Igk-C/Igk-V125)1Jwt/0 NOD.B6-Tg(Igh-6/Igh-V125)2Jwt Tg(Igk-C/Igk-V125)1Jwt J:91865 View', 'Wrong data displayed for row 3!')
        row4 = table1.get_row(4)
        self.assertEquals(row4.text, 'Ighmtm1Cgn/Ighm+\nTg(Igh-6/Igh-V281)3Jwt/0 NOD.Cg-Ighmtm1Cgn Tg(Igh-6/Igh-V281)3Jwt J:91865 View', 'Wrong data displayed for row 4!')
        row5 = table1.get_row(5)
        self.assertEquals(row5.text, 'Ighmtm1Cgn/Ighm+ NOD.129S2-Ighmtm1Cgn J:37287 View', 'Wrong data displayed for row 5!')
        
        
        notmodel_table = self.driver.find_element(By.ID, 'diseaseBrowserNotModelPopupTable')
        table2 = Table(notmodel_table)
        #print table2
        #asserts that each row of data for NOTs is correct
        row1 = table2.get_row(1)
        self.assertEquals(row1.text, 'Ighmtm1Cgn/Ighmtm1Cgn NOD.129S2-Ighmtm1Cgn J:37287 View', 'Wrong data displayed for row 1!')
        row2 = table2.get_row(2)
        #print row2.text
        self.assertEquals(row2.text, 'Ighmtm1Cgn/Ighmtm1Cgn NOD.129S2-Ighmtm1Cgn/DvsJ J:80859 View', 'Wrong data displayed for row 2!')
        row3 = table2.get_row(3)
        self.assertEquals(row3.text, 'Ighmtm1Cgn/Ighmtm1Cgn\nTg(IghelMD4)4Ccg/Tg(IghelMD4)4Ccg NOD.Cg-Ighmtm1Cgn Tg(IghelMD4)4Ccg/DvsJ J:80859 View', 'Wrong data displayed for row 3!')
        
    def test_dobrowser_modelspopup_strain_links(self):
        '''
        @status this test verifies that strains in the Genetic Background column link to their strain detail page
        @note do-results-gene-1
        '''
        print ("BEGIN test_dobrowser_modelspopup_strain_links")
        searchbox = self.driver.find_element(By.ID, 'searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:14330")
        searchbox.send_keys(Keys.RETURN)
        
        self.driver.find_element(By.LINK_TEXT, "Parkinson's disease").click()
        
        self.driver.find_element(By.ID, 'genesTabButton').click()#identifies the Genes tab and clicks it.
        
        gene_table = self.driver.find_element(By.ID, 'geneTabTable')
        table = Table(gene_table)
        #cells = table.get_rows()
        cell = table.get_cell(3, 3)
        #Identify the data found in the Mouse Models column for the first row(for marker Snca)
        print cell.text
        cell.find_element(By.LINK_TEXT, '23 models').click()
        #switch focus to the popup page
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #Find the link in the Genetic Background column C57BL/6J-Tg(SNCA)ARyot and click it
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'C57BL/6J-Tg').click()
        time.sleep(2)
        #switch focus to the new tab for strain detail page
        self.driver.switch_to_window(self.driver.window_handles[-1])
        #Asserts that the strain page is for the correct strain
        assert "C57BL/6J-Tg(SNCA)ARyot" in self.driver.page_source  


            
        def tearDown(self):
            self.driver.close()
        
        def suite():
            suite = unittest.TestSuite()
            suite.addTest(unittest.makeSuite(TestDoBrowserModelsPopup))
            return suite
        
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.TestDoBrowserModelsPopup']
    HTMLTestRunner.main() 