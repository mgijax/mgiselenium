'''
Created on Apr 22, 2016
@author: jeffc
Verify parent data is correctly identified
Verify tree view smart alpha sort order
Verify search by EmapA term associated with multiple phenotypes
Verify search by EmapA term associated to a single phenotype
Verify search by  EmapA term associated to phenotype but NO expression
Verify the phenotype link treeview returns correct results
Verify 1to1 mapping with NO child terms phenotype link
Verify 1to1 mapping with child terms phenotype link
Verify 1to1 mapping with NO phenotype link but an expression link
Verify 1to1 NO mapping for expression or phenotype
Verify 1to1 NO mapping for expression or phenotype but has children
Verify 1toN mapping with parents and 3 phenotype children
Verify 1toN mapping with parents and expression children
Verify NO phenotype mapping, zero expression, NO children
Verify NO phenotype mapping, has expression mapping, NO children
Verify NO phenotype mapping, NO expression mapping, NO children
Verify the phenotype term link results are alphanumeric sorted
'''
import unittest
import time
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.table import Table
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../',)
)
from util import wait, iterate
import config
tracemalloc.start()
class TestEmapaBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome() 

    def test_parent_data(self):
        """
        @status: Tests that the parent terms are correctly identified
        In this case all 3 parent terms should be part-of
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:16042")
        #identifies the table tags that contain parent terms
        parent = driver.find_element(By.ID, 'termPaneDetails').find_elements(By.TAG_NAME, 'td')
        if WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.ID, 'termPaneDetails'))):
          print('Term details loaded')
        # verifies that the returned part terms are correct
        self.assertEqual(parent[4].text, "part-of conceptus\npart-of egg cylinder\npart-of mouse")
        
        
    def test_default_sort_treeview(self):
        """
        @status: Tests that the terms are correctly sorted
        The default sort for the tree view is smart alpha
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:16042")
        time.sleep(2)
        term1 = driver.find_element(By.ID, 'ygtvlabelel2')
        term2 = driver.find_element(By.ID, 'ygtvlabelel3')
        term3 = driver.find_element(By.ID, 'ygtvlabelel4')
        term4 = driver.find_element(By.ID, 'ygtvlabelel5')
        term5 = driver.find_element(By.ID, 'ygtvlabelel15')
        term6 = driver.find_element(By.ID, 'ygtvlabelel16')
        term7 = driver.find_element(By.ID, 'ygtvlabelel17')
        term8 = driver.find_element(By.ID, 'ygtvlabelel18')
        term9 = driver.find_element(By.ID, 'ygtvlabelel19')
        term10 = driver.find_element(By.ID, 'ygtvlabelel20')
        term11 = driver.find_element(By.ID, 'ygtvlabelel21')
        term12 = driver.find_element(By.ID, 'ygtvlabelel22')
        term13 = driver.find_element(By.ID, 'ygtvlabelel6')
        term14 = driver.find_element(By.ID, 'ygtvlabelel7')
        term15 = driver.find_element(By.ID, 'ygtvlabelel8')
        term16 = driver.find_element(By.ID, 'ygtvlabelel9')
        print(term1.text)
        print(term16.text)
        if WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, 'ygtvchildren'))):
            print('Tree view details loaded')
        # extra embryonic component should not be 2nd item in list
        self.assertEqual(term1.text, 'body fluid or substance')
        self.assertEqual(term2.text, 'body region')
        self.assertEqual(term3.text, 'cavity or lining')
        self.assertEqual(term4.text, 'conceptus')
        self.assertEqual(term5.text, 'blastocyst')
        self.assertEqual(term6.text, 'early conceptus')
        self.assertEqual(term7.text, 'embryo')
        self.assertEqual(term8.text, 'extraembryonic component')
        self.assertEqual(term9.text, 'polar body')
        self.assertEqual(term10.text, 'primitive endoderm')
        self.assertEqual(term11.text, 'primordial germ cell')
        self.assertEqual(term12.text, 'zona pellucida')
        self.assertEqual(term13.text, 'early embryo')
        self.assertEqual(term14.text, 'embryo')
        self.assertEqual(term15.text, 'extracellular matrix')
        self.assertEqual(term16.text, 'extraembryonic component')

    def test_pheno_link_multi(self):
        """
        @status: Tests that searching by an Emapa term that is associated with multiple phenotypes return the
        correct results/link
        @note: EMAPA-ID-Search-2
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:16237")
        driver.find_element(By.LINK_TEXT, 'phenotype terms').click()
        searchList = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchList)
        print([x.text for x in searchList])
        if WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('MP Annotation summary loaded')
        # print('Tree view details loaded')
        # These 2 terms should be returned in the phenotype search results(could be other terms as well)
        self.assertIn('absent sinus venosus\nsinus venosus hypoplasia', terms, 'these terms are not listed!')
        
 
    def test_pheno_link_single(self):
        """
        @status: Tests that searching by an Emapa term that is associated with a single phenotype returns the
        correct results/link
        @note: EMAPA-ID-Search-1
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:16076")
        driver.find_element(By.LINK_TEXT, 'phenotype terms').click()
        searchList = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchList)
        print([x.text for x in searchList])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('MP Annotation summary loaded')
        # This term should be returned in the phenotype search results
        self.assertIn('absent amniotic folds', terms, 'this term is not listed!')
        
    def test_pheno_link_noexpression(self):
        """
        @status: Tests that searching by an Emapa term that is associated to a phenotype but has no expression
        annotations
        @note: EMAPA-ID_Search-4
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:16044")
        driver.find_element(By.LINK_TEXT, 'phenotype terms').click()
        searchList = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchList)
        print([x.text for x in searchList])
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'searchResults'))):
            print('MP Annotation summary loaded')
        # These 2 terms should be returned in the phenotype search results
        self.assertIn('abnormal blastocoele morphology\nabsent blastocoele', terms, 'these terms are not listed!')
        
    def test_pheno_link_treeview(self):
        """
        @status: Tests that the phenotype annotations link in the Treeview section when clicked returns correct results.
        @note: maybe not needed?
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:35272")
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'phenotypeAnnotationCount'))):
            print('Tree view details loaded')
        driver.find_element(By.CLASS_NAME, 'phenotypeAnnotationCount').click()#clicks the phenotype annotations link found in the Treeview section
        results_table = self.driver.find_element(By.ID, 'resultsTable')
        table = Table(results_table)
        #gets the 1st,6th,13th,16th rows of the Annotated term column
        term1 = table.get_cell(3, 1)
        term2 = table.get_cell(8, 1)
        term3 = table.get_cell(16, 1)
        term4 = table.get_cell(19, 1)
        print(term1.text)
        print(term2.text)
        print(term3.text)
        print(term4.text)
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'resultsTable'))):
            print('MP Annotation summary loaded')
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('abnormal cerebellum deep nucleus morphology', term1.text, 'Term1 is not returning' )
        self.assertEqual('abnormal cerebellum fastigial nucleus morphology', term2.text, 'Term2 is not returning' )
        self.assertEqual('abnormal cerebellum dentate nucleus morphology', term3.text, 'Term3 is not returning' )
        self.assertEqual('abnormal cerebellum interpositus nucleus morphology', term4.text, 'Term4 is not returning' )

    def test_pheno_link_nochild_treeview(self):
        """
        @status: Tests that when you have a 1to1 mapping with no child terms associated(gxd&pheno),the phenotype
        annotations link in the Treeview section when clicked returns correct results.
        @note: EMAPA-ID-search-7
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:36506")
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'phenotypeAnnotationCount'))):
            print('Tree view details loaded')
        driver.find_element(By.CLASS_NAME, 'phenotypeAnnotationCount').click()#clicks the phenotype annotations link found in the Treeview section
        results_table = self.driver.find_element(By.ID, 'resultsTable')
        table = Table(results_table)
        #gets the 1st and only row of the Annotated term column
        term1 = table.get_cell(3, 1)
        print(term1.text)
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'resultsTable'))):
            print('MP Annotation summary loaded')
        # verifies the returned terms are the correct terms for this search
        self.assertEqual("abnormal Peyer's patch epithelium morphology", term1.text, 'Term1 is not returning' )

    def test_pheno_link_withchildboth_treeview(self):
        """
        @status: Tests that when you have a 1to1 mapping with child terms associated(gxd&pheno),the phenotype
        annotations link in the Treeview section when clicked returns correct results.
        @note: EMAPA-ID-search-8
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:16333")
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'phenotypeAnnotationCount'))):
            print('Tree view details loaded')
        driver.find_element(By.CLASS_NAME, 'phenotypeAnnotationCount').click()#clicks the phenotype annotations link found in the Treeview section
        results_table = self.driver.find_element(By.ID, 'resultsTable')
        table = Table(results_table)
        #gets the 1st,2nd rows of the Annotated term column, only 2 rows exist
        term1 = table.get_cell(3, 1)
        term2 = table.get_cell(4, 1)
        print(term1.text)
        print(term2.text)
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'resultsTable'))):
            print('MP Annotation summary loaded')
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('abnormal bulbus cordis morphology', term1.text, 'Term1 is not returning' )
        self.assertEqual('abnormal bulbus cordis morphology', term2.text, 'Term2 is not returning' )

    def test_no_pheno_link_exp_link(self):
        """
        @status: Tests that when you have a 1to1 mapping with NO Pheno mapping/has GXD mapping,the GXD link has data
        the phenotype annotations link in the Treeview section has zero results.
        @note: EMAPA-ID-search-9 :broken, awaiting a software fix
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:32750")
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        #the phenotype annotations link found in the Treeview section should be zero
        assert '0 phenotype annotations' in driver.page_source

    def test_zero_pheno_link_zero_exp_link(self):
        """
        @status: Tests that when you have a 1to1 NO mapping for expression or pheno, NO child terms, the phenotype
        annotations is zero and expression results links in the Treeview section is normal.
        @note: EMAPA-ID-search-10
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:37850")
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'ygtvchildren'))):
            print('Tree view details loaded')
        # verifies the returned results are zero for this search
        assert '(0 expression results; 0 phenotype annotations)' in driver.page_source 
        

    def test_zero_pheno_link_zero_exp_link_MP_child(self):
        """
        @status: Tests that when you have a 1to1  NO mapping for expression or pheno, has child terms,the phenotype
        annotations is zero and expression results links in the Treeview section is normal.
        @note: EMAPA-ID-search-11 
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:16824")
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        linkE = driver.find_element(By.CLASS_NAME, 'expressionResultCount') #the expression annotations link found in the Treeview section
        print(linkE.text)
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('3', linkE.text, 'The 0 expression results link is wrong' )
        self.assertIn('0 phenotype annotations', driver.page_source, 'The 0 phenotypes annotation link is missing')#confirms that o phenotype annitations text is displayed when no results
        
    def test_pheno_link_withparent3child_treeview(self):
        """
        @status: Tests that when you have a 1toN mapping with parent and 3 child terms associated(pheno)
        has child terms,the phenotype annotations link in the Treeview section when clicked returns correct results.
        @note: EMAPA-ID-search-12
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:28373")
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        driver.find_element(By.CLASS_NAME, 'phenotypeAnnotationCount').click()#clicks the phenotype annotations link found in the Treeview section
        results_table = self.driver.find_element(By.ID, 'resultsTable')
        table = Table(results_table)
        #gets the 1st-8th rows of the Annotated term column, only 8 rows exist
        term1 = table.get_cell(3, 1)
        term2 = table.get_cell(4, 1)
        term3 = table.get_cell(5, 1)
        term4 = table.get_cell(6, 1)
        term5 = table.get_cell(7, 1)
        term6 = table.get_cell(8, 1)
        term7 = table.get_cell(9, 1)
        term8 = table.get_cell(10, 1)
        print(term1.text)
        print(term2.text)
        print(term3.text)
        print(term4.text)
        print(term5.text)
        print(term6.text)
        print(term7.text)
        print(term8.text)
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('abnormal renal artery morphology', term1.text, 'Term1 is not returning' )
        self.assertEqual('abnormal renal artery morphology', term2.text, 'Term2 is not returning' )
        self.assertEqual('abnormal right renal artery morphology', term3.text, 'Term3 is not returning' )
        self.assertEqual('abnormal right renal artery morphology', term4.text, 'Term4 is not returning' )
        self.assertEqual('abnormal right renal artery morphology', term5.text, 'Term5 is not returning' )
        self.assertEqual('abnormal right renal artery morphology', term6.text, 'Term6 is not returning' )
        self.assertEqual('abnormal renal artery morphology', term7.text, 'Term7 is not returning' )
        self.assertEqual('abnormal right renal artery morphology', term8.text, 'Term8 is not returning' )
        
    def test_pheno_link_with_parent_and_child_treeview(self):
        """
        @status: Tests that when you have a 1toN mapping for pheno and expression, child terms for expression,
        the phenotype annotations link in the Treeview section when clicked returns correct results.
        @note: EMAPA-ID-search-13
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:16075")
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        driver.find_element(By.CLASS_NAME, 'phenotypeAnnotationCount').click()#clicks the phenotype annotations link found in the Treeview section
        results_table = self.driver.find_element(By.ID, 'resultsTable')
        table = Table(results_table)
        #gets the 1st, 2nd, 7th, 8th, and 9th rows of the Annotated term column
        term1 = table.get_cell(3, 1)
        term2 = table.get_cell(4, 1)
        term3 = table.get_cell(9, 1)
        term4 = table.get_cell(10, 1)
        term5 = table.get_cell(11, 1)
        print(term1.text)
        print(term2.text)
        print(term3.text)
        print(term4.text)
        print(term5.text)
        # verifies the returned terms are the correct terms for this search
        self.assertEqual('absent embryonic cilia', term1.text, 'Term1 is not returning' )
        self.assertEqual('absent primitive node', term2.text, 'Term2 is not returning' )
        self.assertEqual('abnormal primitive node morphology', term3.text, 'Term3 is not returning' )
        self.assertEqual('abnormal motile primary cilium morphology', term4.text, 'Term4 is not returning' )
        self.assertEqual('decreased embryonic cilium length', term5.text, 'Term5 is not returning' )
        
        
    def test_no_pheno_mapping_zero_exp_link(self):
        """
        @status: Tests that when you have no phenotype mapping but zero Expression mapping, NO child terms,
        the phenotype annotations link in the Treeview section does not display, the expression results link is zero.
        @note: EMAPA-ID-search-14
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:37425")
        wait.forAjax(driver)
        bodyText = driver.find_element(By.TAG_NAME, 'body').text
        # verifies the returned terms are the correct terms for this search
        self.assertTrue('0 expression results', 'The 0 expression results link is wrong' )
        self.assertFalse('phenotype annotations' in bodyText)       

    def test_no_pheno_mapping_has_exp_link(self):
        """
        @status: Tests that when you have no phenotype mapping but Expression mapping, NO child terms,the phenotype
        annotations link in the Treeview section does not display, the expression results link has normal display.
        @note: EMAPA-ID-search-15
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:36473")
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        linkE = driver.find_element(By.CLASS_NAME, 'expressionResultCount') #the expression annotations link found in the Treeview section
        bodyText = driver.find_element(By.TAG_NAME, 'body').text
        print(linkE.text)
        # asserts the expression results link exist and phenotype annotations link does not exist
        self.assertTrue('expression results' in bodyText)
        self.assertFalse('phenotype annotations' in bodyText)       

    def test_no_pheno_mapping_zero_exp_link2(self):
        """
        @status: Tests that when you have no phenotype mapping no Expression mapping, NO child terms,the phenotype
        annotations link in the Treeview section does not display, the expression results link has zero results.
        @note: EMAPA-ID-search-16
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:19101")
        wait.forAjax(driver)
        bodyText = driver.find_element(By.TAG_NAME, 'body').text
        # verifies the returned terms are the correct terms for this search
        self.assertTrue('0 expression results', 'The 0 expression results link is wrong' )
        self.assertFalse('phenotype annotations' in bodyText)        
        
    def test_pheno_link_results_sort(self):
        """
        @status: Tests that when you click the phenotypes term link in the detail section the results returned are
        in alphanumeric sort
        @note: EMAPA-ID-Search-6
        """
        driver = self.driver
        driver.get(config.TEST_URL + "/vocab/gxd/anatomy/EMAPA:16117")
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'expressionResultCount'))):
            print('Tree view details loaded')
        driver.find_element(By.LINK_TEXT, 'phenotype terms').click()
        searchList = driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchList)
        print([x.text for x in searchList])
        print(terms)
        # These terms should be returned in the phenotype search results with the order given
        self.assertIn('abnormal pharyngeal arch morphology\nabsent pharyngeal arches\nectopic pharyngeal arch\nenlarged pharyngeal arch\nfused pharyngeal arches\npharyngeal arch hypoplasia\nsmall pharyngeal arch', terms, 'The sort order is not correct' )
                
        
    def tearDown(self):
        pass
        self.driver.quit()
        tracemalloc.stop()
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEmapaBrowser))
    return suite
        
if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
