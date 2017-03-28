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

class TestDoBrowserTermTab(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.TEST_URL)
        self.driver.implicitly_wait(10)
        
    def test_dobrowser_modelspopup_tableheaders(self):
        '''
@status this test verifies the header section on the DO browser mouse models popup page is correct, this is for the 
        headings Human Disease Modeled and Associated Mouse Gene.
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:1324")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('lung cancer').click()
        wait.forAjax(self.driver)
        self.driver.find_element_by_id('genesTabButton').click()#identifies the Genes tab and clicks it.
        time.sleep(2)
        gene_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(gene_table)
        #cells = table.get_rows()
        cell = table.get_cell(3, 6)
        #Identify the data found in the Mouse Models column for the second row(for marker Fgf9)
        print cell.text
        cell.find_element_by_link_text("1 model").click()
        time.sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        header = self.driver.find_element_by_id('diseaseBrowserModelsPopup')
        model_heading = header.find_element_by_id('diseaseDisplay')
        print model_heading.text
        time.sleep(1)
        #assert that the Human Disease Modeled heading above the table is correct
        self.assertEquals(model_heading.text, "lung cancer")
        
        assoc_gene_heading = header.find_element_by_id('markerDisplay')
        print assoc_gene_heading.text
        time.sleep(1)
        #assert that the Associated Mouse Gene heading above the table is correct
        self.assertEquals(assoc_gene_heading.text, "Fgf9")
        
    def test_dobrowser_modelspopup_tableheaders2(self):
        '''
        @status this test verifies the header section on the DO browser mouse models popup page is correct, this is for the 
        headings Human Disease Modeled and Associated Mouse Gene. This second test is to verify when the disease name has changed
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:1324")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('lung cancer').click()
        wait.forAjax(self.driver)
        self.driver.find_element_by_id('genesTabButton').click()#identifies the Genes tab and clicks it.
        time.sleep(2)
        gene_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(gene_table)
        #cells = table.get_rows()
        cell = table.get_cell(7, 3)
        #Identify the data found in the Mouse Models column for the second row(for marker Fgf9)
        print cell.text
        cell.find_element_by_link_text("1 model").click()
        time.sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        header = self.driver.find_element_by_id('diseaseBrowserModelsPopup')
        model_heading = header.find_element_by_id('diseaseDisplay')
        print model_heading.text
        time.sleep(1)
        #assert that the Human Disease Modeled heading above the table is correct
        self.assertEquals(model_heading.text, "pleuropulmonary blastoma")
        
        assoc_gene_heading = header.find_element_by_id('markerDisplay')
        print assoc_gene_heading.text
        time.sleep(1)
        #assert that the Associated Mouse Gene heading above the table is correct
        self.assertEquals(assoc_gene_heading.text, "Fgf9")        
        
    def test_dobrowser_modelspopup_onlynots(self):
        '''
        @status this test verifies the display of disease model popup when only NOTs are returned.
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:0050581")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('brachydactyly').click()
        wait.forAjax(self.driver)
        self.driver.find_element_by_id('genesTabButton').click()#identifies the Genes tab and clicks it.
        time.sleep(2)
        gene_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(gene_table)
        cell = table.get_cell(10, 3)
        #Identify the data found in the Mouse Models column for the ninth row(for marker ROR2)
        print cell.text
        cell.find_element_by_link_text('1 "NOT" model').click()
        time.sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        model_table = self.driver.find_element_by_id('diseaseBrowserNotModelPopupTable')
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
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:10652")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text("Alzheimer's disease").click()
        wait.forAjax(self.driver)
        self.driver.find_element_by_id('genesTabButton').click()#identifies the Genes tab and clicks it.
        time.sleep(2)
        gene_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(gene_table)
        #cells = table.get_rows()
        cell = table.get_cell(20, 3)
        #Identify the data found in the Mouse Models column for the twenth row(for marker SORL1)
        print cell.text
        cell.find_element_by_link_text('1 model').click()
        time.sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        model_table = self.driver.find_element_by_id('diseaseBrowserModelPopupTable')
        table1 = Table(model_table)
        #print table1
        row1 = table1.get_row(1)
        #assert the table data for row 1 is correct
        self.assertEquals(row1.text, 'Sorl1tm1Tew/Sorl1tm1Tew\nTg(APP695)3Dbo/0\nTg(PSEN1dE9)S9Dbo/0 involves: 129 * C3H/HeJ * C57BL/6 J:142501 View', 'Wrong data displayed for row 1!')
        print row1.text
        
    def test_dobrowser_modelspopup_mouse_nots(self):
        '''
        @status this test verifies the display of disease model popup when you have mouse and NOTs returned.
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your DO ID in the quick search box
        searchbox.send_keys("DOID:9744")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text("type 1 diabetes mellitus").click()
        wait.forAjax(self.driver)
        self.driver.find_element_by_id('genesTabButton').click()#identifies the Genes tab and clicks it.
        time.sleep(2)
        gene_table = self.driver.find_element_by_id("geneTabTable")
        table = Table(gene_table)
        cell = table.get_cell(11, 3)
        #Identify the data found in the Mouse Models column for the tenth row(for marker Ighm)
        print cell.text
        cell.find_element_by_link_text('5 models').click()
        time.sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        model_table = self.driver.find_element_by_id('diseaseBrowserModelPopupTable')
        table1 = Table(model_table)
        #print table1
        #asserts that each row of data in the table is correct
        row1 = table1.get_row(1)
        self.assertEquals(row1.text, 'Ighmtm1Cgn/Ighmtm1Cgn\nTg(Igh-VB1-8/Igh-6m)1Mjsk/? NODCaj.Cg-Ighmtm1Cgn Tg(Igh-VB1-8/Igh-6m)1Mjsk/FswJ J:93190 View', 'Wrong data displayed for row 1!')
        row2 = table1.get_row(2)
        print row2.text
        self.assertEquals(row2.text, 'Tg(Igh-6/Igh-V281)3Jwt/0 NOD.B6-Tg(Igh-6/Igh-V281)3Jwt J:91865 View', 'Wrong data displayed for row 2!')
        row3 = table1.get_row(3)
        self.assertEquals(row3.text, 'Tg(Igh-6/Igh-V125)2Jwt/0\nTg(Igk-C/Igk-V125)1Jwt/0 NOD.B6-Tg(Igh-6/Igh-V125)2Jwt Tg(Igk-C/Igk-V125)1Jwt J:91865 View', 'Wrong data displayed for row 3!')
        row4 = table1.get_row(4)
        self.assertEquals(row4.text, 'Ighmtm1Cgn/Ighm+\nTg(Igh-6/Igh-V281)3Jwt/0 NOD.Cg-Ighmtm1Cgn Tg(Igh-6/Igh-V281)3Jwt J:91865 View', 'Wrong data displayed for row 4!')
        row5 = table1.get_row(5)
        self.assertEquals(row5.text, 'Ighmtm1Cgn/Ighm+ NOD.129S2-Ighmtm1Cgn J:37287 View', 'Wrong data displayed for row 5!')
        
        time.sleep(1)
        
        notmodel_table = self.driver.find_element_by_id('diseaseBrowserNotModelPopupTable')
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
        
        
        
        
        
    def test_dobrowser_children(self):
        '''
        @status this test verifies the correct Parent Terms, Siblings, and Children are returned for this query. This test example has children
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:12365")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('malaria').click()
        wait.forAjax(self.driver)
        #locate the Parent Term box
        parent = self.driver.find_elements_by_id("termTabParentWrapper")#identifies all the parents found in the Parents term box
        searchTermItems = iterate.getTextAsList(parent)
        self.assertEqual(searchTermItems[0], "parasitic protozoa infectious disease +")
        print searchTermItems
        #locate the siblings terms box
        siblings = self.driver.find_elements_by_id("termTabTermWrapper")
        searchTermItems = iterate.getTextAsList(siblings)
        self.assertEquals(searchTermItems[0], "malaria +\n\namebiasis\nbabesiosis\nbalantidiasis\ncoccidiosis +\ndientamoebiasis\ngiardiasis\ngranulomatous amebic encephalitis\nleishmaniasis +\nprimary amebic meningoencephalitis\ntheileriasis\ntrichomoniasis\ntrypanosomiasis +")
        print searchTermItems
        #locate the children terms box
        children = self.driver.find_elements_by_id("termTabChildWrapper")
        searchTermItems = iterate.getTextAsList(children)
        self.assertEquals(searchTermItems[0], "blackwater fever\ncerebral malaria\nmixed malaria\nPlasmodium falciparum malaria\nPlasmodium malariae malaria\nPlasmodium ovale malaria\nPlasmodium vivax malaria")
        print searchTermItems

    def test_dobrowser_many_children(self):
        '''
        @status this test verifies the correct Parent Terms, Siblings, and Children are returned for this query. This test example has many children(shows no rollup used)
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:9562")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('primary ciliary dyskinesia').click()
        wait.forAjax(self.driver)
        #locate the Parent Term box
        parent = self.driver.find_elements_by_id("termTabParentWrapper")#identifies all the parents found in the Parents term box
        searchTermItems = iterate.getTextAsList(parent)
        self.assertEqual(searchTermItems[0], "ciliopathy +")
        print searchTermItems
        #locate the siblings terms box
        siblings = self.driver.find_elements_by_id("termTabTermWrapper")
        searchTermItems = iterate.getTextAsList(siblings)
        self.assertEquals(searchTermItems[0], "primary ciliary dyskinesia +\n\nJoubert syndrome +\nMeckel syndrome")
        print searchTermItems
        #locate the children terms box
        children = self.driver.find_elements_by_id("termTabChildWrapper")
        searchTermItems = iterate.getTextAsList(children)
        self.assertEquals(searchTermItems[0], "Kartagener syndrome\nprimary ciliary dyskinesia 1\nprimary ciliary dyskinesia 10\nprimary ciliary dyskinesia 11\nprimary ciliary dyskinesia 12\nprimary ciliary dyskinesia 13\nprimary ciliary dyskinesia 14\nprimary ciliary dyskinesia 15\nprimary ciliary dyskinesia 16\nprimary ciliary dyskinesia 17\nprimary ciliary dyskinesia 18\nprimary ciliary dyskinesia 19\nprimary ciliary dyskinesia 2\nprimary ciliary dyskinesia 20\nprimary ciliary dyskinesia 21\nprimary ciliary dyskinesia 22\nprimary ciliary dyskinesia 23\nprimary ciliary dyskinesia 24\nprimary ciliary dyskinesia 25\nprimary ciliary dyskinesia 26\nprimary ciliary dyskinesia 27\nprimary ciliary dyskinesia 28\nprimary ciliary dyskinesia 29\nprimary ciliary dyskinesia 3\nprimary ciliary dyskinesia 30\nprimary ciliary dyskinesia 32\nprimary ciliary dyskinesia 33\nprimary ciliary dyskinesia 34\nprimary ciliary dyskinesia 35\nprimary ciliary dyskinesia 4\nprimary ciliary dyskinesia 5\nprimary ciliary dyskinesia 6\nprimary ciliary dyskinesia 7\nprimary ciliary dyskinesia 8\nprimary ciliary dyskinesia 9\nStromme syndrome")
        print searchTermItems

    def test_dobrowser_noomim(self):
        '''
        @status this test verifies the correct Parent Terms and Siblings are returned for this query. This test example has no children because it has no OMIM
        and no annotations
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:14332")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('postencephalitic Parkinson disease').click()
        wait.forAjax(self.driver)
        #locate the Parent Term box
        parent = self.driver.find_elements_by_id("termTabParentWrapper")#identifies all the parents found in the Parents term box
        searchTermItems = iterate.getTextAsList(parent)
        self.assertEqual(searchTermItems[0], "secondary Parkinson disease +")
        print searchTermItems
        #locate the siblings terms box
        siblings = self.driver.find_elements_by_id("termTabTermWrapper")
        searchTermItems = iterate.getTextAsList(siblings)
        self.assertEquals(searchTermItems[0], "postencephalitic Parkinson disease")
        print searchTermItems

    def test_dobrowser_child_of_children(self):
        '''
        @status this test verifies the correct Parent Terms, Siblings, and Children are returned for this query. This test example verifies
        that when a child term has children it's followed by a + sign
        '''
        searchbox = self.driver.find_element_by_id('searchToolTextArea')
        # put your Gene ID in the quick search box
        searchbox.send_keys("DOID:680")
        searchbox.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.find_element_by_link_text('tauopathy').click()
        wait.forAjax(self.driver)
        #locate the Parent Term box
        parent = self.driver.find_elements_by_id("termTabParentWrapper")#identifies all the parents found in the Parents term box
        searchTermItems = iterate.getTextAsList(parent)
        self.assertEqual(searchTermItems[0], "neurodegenerative disease +")
        print searchTermItems
        #locate the siblings terms box
        siblings = self.driver.find_elements_by_id("termTabTermWrapper")
        searchTermItems = iterate.getTextAsList(siblings)
        self.assertEquals(searchTermItems[0], "tauopathy +\n\ndemyelinating disease +\neye degenerative disease +\neyelid degenerative disease +\nfamilial encephalopathy with neuroserpin inclusion bodies\nhereditary ataxia +\nHuntington's disease\ninfantile cerebellar-retinal degeneration\nLafora disease\nmotor neuron disease +\nmyoclonic cerebellar dyssynergia\nneuroacanthocytosis +\nneurodegeneration with brain iron accumulation +\nolivopontocerebellar atrophy\nPick's disease\nplexopathy\npontocerebellar hypoplasia +\nprimary cerebellar degeneration\nsecondary Parkinson disease +\nSPOAN syndrome\nsynucleinopathy +")
        print searchTermItems
        #locate the children terms box
        children = self.driver.find_elements_by_id("termTabChildWrapper")
        searchTermItems = iterate.getTextAsList(children)
        self.assertEquals(searchTermItems[0], "Alzheimer's disease +")
        print searchTermItems
            
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