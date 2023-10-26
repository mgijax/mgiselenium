'''
Created on May 23, 2016
@author: jeffc
This suite of tests are for allele detail pages
verify ribbon lacations
verify turnstile functions in mutation ribbon
verify allele subtypes in mutation ribbon
verify molecular image displays
verify mutagentix link(on public)
verify thumbnail image caption for molecular images
verify AFP link
verify correct project collection listed
verify mutation strain link
verify phenotype table strain link
verify disease models in phenotype table
verify show/hide of phenotype ribbon
verify data of genotype popup
verify molecular images not included on allele detail
verify display of DOIDs
verify certain rollup rules
verify alleles related to human, rat, zebrafish, fruitfly and yeast
verify recombinase activity section
verify Alliance link, IMPC link, MMHCdb link
'''
import unittest
import tracemalloc
import config
import time
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../..',)
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.remote import webelement
from genericpath import exists
from util import wait, iterate
from util.table import Table
from config import TEST_URL

#Tests
tracemalloc.start()
class TestAlleleDetail(unittest.TestCase):


    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/allele/")
        #self.driver.get('http://scrumdogdev.informatics.jax.org/allele')
        self.driver.implicitly_wait(10)

    def test_ribbon_locations(self):
        '''
        @status This test verifies the ribbons are being displayed in the correct order on the page.
        '''
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Pkd1')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm2Jzh').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'nomenTable')))#waits until the nomenclature table(summary ribbon) is displayed on the page
        assert "Pkd1<sup>tm2Jzh</sup>" in self.driver.page_source
        #print self.driver.page_source
        assert 'id="summaryHeader"' in self.driver.page_source
        assert 'id="originHeader"' in self.driver.page_source
        assert 'id="descriptionHeader"' in self.driver.page_source
        assert 'id="phenotypesHeader"' in self.driver.page_source
        assert 'id="diseaseModelsHeader"' in self.driver.page_source
        assert 'id="expressionHeader"' in self.driver.page_source
        assert 'id="imsrHeader"' in self.driver.page_source
        assert 'id="referencesHeader"' in self.driver.page_source
        
    def test_ribbon_locations2(self):
        '''
        @status This test verifies the ribbons are being displayed in the correct order on the page.
        This allele had recombinase and phenotype ribbons
        '''
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Slc6a3')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1(cre)Xz').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'nomenTable')))#waits until the nomenclature table(summary ribbon) is displayed on the page
        assert "Slc6a3<sup>tm1(cre)Xz</sup>" in self.driver.page_source
        assert 'id="summaryHeader"' in self.driver.page_source
        assert 'id="originHeader"' in self.driver.page_source
        assert 'id="descriptionHeader"' in self.driver.page_source
        assert 'id="recombinaseHeader"' in self.driver.page_source
        assert 'id="phenotypesHeader"' in self.driver.page_source
        assert 'id="diseaseModelsHeader"' in self.driver.page_source
        assert 'id="expressionHeader"' in self.driver.page_source
        assert 'id="imsrHeader"' in self.driver.page_source
        assert 'id="referencesHeader"' in self.driver.page_source
        
    def test_ribbon_locations3(self):
        '''
        @status This test verifies the ribbons are being displayed in the correct order on the page.
        This allele had no disease models so the Expression ribbon should follow the phenotype ribbon
        '''
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Pax3')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1(cre)Joe').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'nomenTable')))#waits until the nomenclature table(summary ribbon) is displayed on the page
        assert "Pax3<sup>tm1(cre)Joe</sup>" in self.driver.page_source
        assert 'id="summaryHeader"' in self.driver.page_source
        assert 'id="originHeader"' in self.driver.page_source
        assert 'id="descriptionHeader"' in self.driver.page_source
        assert 'id="recombinaseHeader"' in self.driver.page_source
        assert 'id="phenotypesHeader"' in self.driver.page_source
        assert 'id="expressionHeader"' in self.driver.page_source
        assert 'id="imsrHeader"' in self.driver.page_source
        assert 'id="referencesHeader"' in self.driver.page_source
        
    def test_turnstile_behavior(self):
        '''
        @status this test verifies In the Mutation Description section, confirm there are turnstile icons for Mutation Notes, 
        Sequence Tags, and Genome Context Verify clicking the turnstile icon for Mutation Notes, Sequence tags, and Genome context displays the complete information.
        @bug clicking the turnstiles was not working, traced to firefox, works fine using Chrome
        '''
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Arrdc3')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Gt(CSE151)Byg').click()
        mutationDownArrow = self.driver.find_element(By.ID, 'downArrowMutationDescription')
        mutationRightArrow = self.driver.find_element(By.ID, 'rightArrowMutationDescription')
        self.assertTrue(mutationDownArrow.is_displayed())
        self.assertFalse( mutationRightArrow.is_displayed())
        mutationDownArrow.click()
        mutationDownArrow = self.driver.find_element(By.ID, 'downArrowMutationDescription')
        mutationRightArrow = self.driver.find_element(By.ID, 'rightArrowMutationDescription')
        self.assertFalse( mutationDownArrow.is_displayed())
        self.assertTrue( mutationRightArrow.is_displayed())
        sequenceDownArrow = self.driver.find_element(By.ID, 'downArrowSeqTag')
        sequenceRightArrow = self.driver.find_element(By.ID, 'rightArrowSeqTag')
        self.assertFalse( sequenceDownArrow.is_displayed())
        self.assertTrue( sequenceRightArrow.is_displayed())
        sequenceRightArrow.click()
        sequenceDownArrow = self.driver.find_element(By.ID, 'downArrowSeqTag')
        sequenceRightArrow = self.driver.find_element(By.ID, 'rightArrowSeqTag')
        self.assertTrue( sequenceDownArrow.is_displayed())
        self.assertFalse( sequenceRightArrow.is_displayed())
        genomeDownArrow = self.driver.find_element(By.ID, 'downArrowGenome')
        genomeRightArrow = self.driver.find_element(By.ID, 'rightArrowGenome')
        self.assertFalse( genomeDownArrow.is_displayed())
        self.assertTrue( genomeRightArrow.is_displayed())
        genomeRightArrow.click()
        genomeDownArrow = self.driver.find_element(By.ID, 'downArrowGenome')
        genomeRightArrow = self.driver.find_element(By.ID, 'rightArrowGenome')
        self.assertTrue( genomeDownArrow.is_displayed())
        self.assertFalse( genomeRightArrow.is_displayed())
        
    def test_no_turnstile(self):
        '''
        @status this test verifies In the Mutation Description section, confirm that no turnstile icon exists
        because the notes are less than 100 characters.
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Kit')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Ssm').click()
        #mutationDownArrow = self.driver.find_element(By.ID, 'downArrowMutationDescription').
        #mutationRightArrow = self.driver.find_element(By.ID, 'rightArrowMutationDescription')
        
        assert 'id= "downArrowMutationDescription"' not in self.driver.page_source
        assert 'id= "rightArrowMutationDescription"' not in self.driver.page_source
        
    def test_turnstile_largenote(self):
        '''
        @status this test verifies In the Mutation Description section, confirm the turnstile is open for Mutation Notes(large note) and displays the complete information
        (no text is cut off).
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Car12')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '4563.1Dla').click()
        mutationDownArrow = self.driver.find_element(By.ID, 'downArrowMutationDescription')
        mutationRightArrow = self.driver.find_element(By.ID, 'rightArrowMutationDescription')
        
        self.assertTrue(mutationDownArrow.is_displayed())
        self.assertFalse( mutationRightArrow.is_displayed())
        mutationDownArrow.click()
        mutationDownArrow = self.driver.find_element(By.ID, 'downArrowMutationDescription')
        mutationRightArrow = self.driver.find_element(By.ID, 'rightArrowMutationDescription')
        
        self.assertFalse( mutationDownArrow.is_displayed())
        self.assertTrue( mutationRightArrow.is_displayed())
    
    def test_allele_subtype(self):
        '''
        @status this test verifies  Allele subtypes appear in Mutation Description ribbon on Allele Detail Pages
         as a comma separated list following the allele type. 
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Kdr')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1Jrt').click()
        alleleType = self.driver.find_element(By.ID, 'alleleTypeDisplay')
        
        self.assertEqual(alleleType.text, "Targeted (Null/knockout, Reporter)")
        self.driver.get(config.TEST_URL + "/allele/")
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Olig2')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Htak').click()
        alleleType = self.driver.find_element(By.ID, 'alleleTypeDisplay')
        
        self.assertEqual(alleleType.text, "Targeted (Inducible, Recombinase)")
        self.driver.get(config.TEST_URL + "/allele/")
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Tg(BCL2)1Tsk')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Tg(BCL2)1Tsk').click()
        alleleType = self.driver.find_element(By.ID, 'alleleTypeDisplay')
        
        self.assertEqual(alleleType.text, "Transgenic (Inserted expressed sequence)")
        
    def test_allele_nosubtype(self):
        '''
        @status this test verifies Allele Subtypes do not appear when the allele is not assigned to a subtype.
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Lith20')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'SM/J').click()
        alleleType = self.driver.find_element(By.ID, 'alleleTypeDisplay')
        
        self.assertEqual(alleleType.text, "QTL")
        self.driver.get(config.TEST_URL + "/allele/")
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Tg(Id1*-lacZ)1C10Oxb')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Tg(Id1*-lacZ)1C10Oxb').click()
        alleleType = self.driver.find_element(By.ID, 'alleleTypeDisplay')
        
        self.assertEqual(alleleType.text, "Transgenic")
        
    def test_allele_molecular_image(self):
        '''
        @status this test verifies Allele Detail page displays molecular image in the molecular description ribbon.
        
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Tgm3')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1Sjo').click()
        
        image = self.driver.find_element(By.ID, 'mutationDescriptionTable').find_element(By.CSS_SELECTOR, 'a img')
        self.assertTrue(image.is_displayed(), 'the image is not displaying')
        self.driver.get(config.TEST_URL + "/allele/")
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Dock2')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'm1Hsd').click()
        
        image = self.driver.find_element(By.ID, 'mutationDescriptionTable').find_element(By.CSS_SELECTOR, 'a img')
        self.assertTrue(image.is_displayed(), 'the image is not displaying')
        
        
    def test_mutagenetix_link(self):
        '''
        @status this test verifies these Alleles have the Mutagentix link in the Mutation Description ribbon(under Mutation Details) and the link works.
        @bug Mutagenetix file missing(only available on public), so link is not there, once file is there this test will work
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Blnk')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'm1Btlr').click()
        mutagenetixlink = self.driver.find_element(By.LINK_TEXT, 'incidental mutations')
        actualurl = self.driver.find_element(By.LINK_TEXT, 'incidental mutations').get_attribute('href')
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, config.TEST_URL + '/downloads/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.TEST_URL + "/allele/")
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Irf7')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'm1Btlr').click()
        mutagenetixlink = self.driver.find_element(By.LINK_TEXT, 'incidental mutations')
        actualurl = self.driver.find_element(By.LINK_TEXT, 'incidental mutations').get_attribute('href')
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, config.TEST_URL + '/downloads/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.TEST_URL + "/allele/")
            
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Col4a4')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'm1Btlr').click()
        mutagenetixlink = self.driver.find_element(By.LINK_TEXT, 'incidental mutations')
        actualurl = self.driver.find_element(By.LINK_TEXT, 'incidental mutations').get_attribute('href')
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, config.TEST_URL + '/downloads/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.TEST_URL + "/allele/")
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Nfkbid')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'm1Btlr').click()
        mutagenetixlink = self.driver.find_element(By.LINK_TEXT, 'incidental mutations')
        actualurl = self.driver.find_element(By.LINK_TEXT, 'incidental mutations').get_attribute('href')
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, config.TEST_URL + '/downloads/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.TEST_URL + "/allele/")
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Unc93b1')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '3d').click()
        mutagenetixlink = self.driver.find_element(By.LINK_TEXT, 'incidental mutations')
        actualurl = self.driver.find_element(By.LINK_TEXT, 'incidental mutations').get_attribute('href')
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, config.TEST_URL + '/downloads/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.TEST_URL + "/allele/")
    
    def test_allele_molecular_image_caption(self):
        '''
        @status this test verifies Allele Detail page displays thumbnail caption to the left of the molecular image in the molecular description ribbon.
        @bug: This page needs the table to have an ID before a test can really be written
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Stk11')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1.1Jish').click()
        
        caption = self.driver.find_element(By.ID, 'mutationDescriptionTable').find_element(By.CSS_SELECTOR, 'span.small')
        self.assertTrue(caption.is_displayed(), 'the caption is not displaying')
        self.driver.get(config.TEST_URL + "/allele/")
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Supv3l1')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm2.1Jkl').click()
        
        caption = self.driver.find_element(By.ID, 'mutationDescriptionTable').find_element(By.CSS_SELECTOR, 'span')
        self.assertTrue(caption.is_displayed(), 'the caption is not displaying')
        self.driver.get(config.TEST_URL + "/allele/")
        
        #6.The correct image/caption is displayed to the left of the molecular image in the molecular description ribbon when more than one thumbnail exists for an allele.
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Dock2')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'm1Hsd').click()
        
        caption = self.driver.find_element(By.ID, 'mutationDescriptionTable').find_element(By.CSS_SELECTOR, 'span.small')
        self.assertEqual(caption.text, 'Schematic showing the duplication and location of the premature stop codon in the Dock2m1Hsd allele')
        
        
    def test_afp_link(self):
        '''
        @status this test verifies these Alleles have the Australian Phenome Facility link in the Mutation Description ribbon(under Mutation Details) and the link works.
        @bug Mutagenetix file missing(only available on public), so link is not there, once file is there this test will work
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Adamts20')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'hip').click()
        afplink = self.driver.find_element(By.LINK_TEXT, 'incidental mutations')
        actualurl = self.driver.find_element(By.LINK_TEXT, 'incidental mutations').get_attribute('href')
        
        self.assertEqual(afplink.text, "incidental mutations")
        self.assertEqual(actualurl, config.TEST_URL + '/downloads/datasets/incidental_muts/APF.xlsx')        
        self.driver.get(config.TEST_URL + "/allele/")        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Nphp3')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        #time.sleep(4)
        self.driver.find_elements(By.PARTIAL_LINK_TEXT, 'pol')[1].click()
        #time.sleep(4)
        afplink = self.driver.find_element(By.LINK_TEXT, 'incidental mutations')
        actualurl = self.driver.find_element(By.LINK_TEXT, 'incidental mutations').get_attribute('href')
        
        self.assertEqual(afplink.text, "incidental mutations")
        self.assertEqual(actualurl, config.TEST_URL + '/downloads/datasets/incidental_muts/APF.xlsx')
    
    def test_collection_value(self):
        '''
        @status this test verifies these Alleles have the correct project collection in the Mutation origin ribbon.
        
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('0610037L13Rik')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1(KOMP)Vlcg').click()
        collection = self.driver.find_element(By.ID, 'mutationOriginTable').find_elements(By.CSS_SELECTOR, 'td.padded')
        collitem = collection[5]
        self.assertEqual(collitem.text, "KOMP-Regeneron")
        self.driver.get(config.TEST_URL + "/allele/")
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Acan')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'b2b183Clo').click()
        collection = self.driver.find_element(By.ID, 'mutationOriginTable').find_elements(By.CSS_SELECTOR, 'td.padded')
        collitem = collection[2]
        self.assertEqual(collitem.text, "B2B/CvDC")
        self.driver.get(config.TEST_URL + "/allele/")
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Adamts20')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'hip').click()
        collection = self.driver.find_element(By.ID, 'mutationOriginTable').find_elements(By.CSS_SELECTOR, 'td.padded')
        collitem = collection[2]
        self.assertEqual(collitem.text, "APF ENU Mutagenesis")
        self.driver.get(config.TEST_URL + "/allele/")
        
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Dbx1')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1.1(cre)Mull').click()
        collection = self.driver.find_element(By.ID, 'mutationOriginTable').find_elements(By.CSS_SELECTOR, 'td.padded')
        collitem = collection[4]
        self.assertEqual(collitem.text, "Neuroscience Blueprint cre")
        self.driver.get(config.TEST_URL + "/allele/")
        
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Tg(Ucn3-cre)KF31Gsat')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Tg(Ucn3-cre)KF31Gsat').click()
        collection = self.driver.find_element(By.ID, 'mutationOriginTable').find_elements(By.CSS_SELECTOR, 'td.padded')
        collitem = collection[2]
        self.assertEqual(collitem.text, "GENSAT")
        self.driver.get(config.TEST_URL + "/allele/")
        
        #Collection does not appear when the allele is not assigned to a collection. 
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Pax6')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '2Neu').click()
        assert "Project Collection" not in self.driver.page_source
      
    def test_mutation_strain_link(self):
        '''
        @status this test verifies the strain link in the Mutation origin ribbon.
        @note: alldetail-mutation-1
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('shh')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Dsh').click()
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.LINK_TEXT, '(101 x C3H)F1')))
        self.driver.find_element(By.LINK_TEXT, '(101 x C3H)F1').click()
        #switch focus to the new tab for strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        ptitle = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        #Assert the page title is for the correct strain name
        self.assertEqual(ptitle.text, "(101 x C3H)F1")

    def test_pheno_table_strain_link(self):
        '''
        @status this test verifies the strain link in the phenotype table Genetic Background column opens in a new tab.
        @note: alldetail-pheno-1
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Shh')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Dz').click()
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(3) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)')))
        #find the first link for C57BL/6J-Rr29<Dz> in the Genetic Background column of the Phenotype table and click it.
        self.driver.find_element(By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(3) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)').click()
        #switch focus to the new tab for Strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        print(page_title.text)
        #Asserts that the strain page is for the correct strain
        self.assertEqual(page_title.text, 'C57BL/6J-Rr29Dz', 'Page title is not correct!')
        ptitle = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        #Assert the page title is for the correct strain name
        self.assertEqual(ptitle.text, "C57BL/6J-Rr29Dz")

    def test_view_table_strain_link(self):
        '''
        @status this test verifies the strain links in the allgenoviews table Genetic Background columns opens in a new tab(both summary & Genotype ribbons.
        @note: alldetail-pheno-2
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Shh')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Dz').click()
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.LINK_TEXT, 'View')))
        #locate the View link found at the bottom of the Phenotypes ribbon and click it
        self.driver.find_element(By.LINK_TEXT, 'View').click()
        #switch focus to the new tab for Phenotypes associated with this allele page        
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #find the first link for C57BL/6J-Shh<Dz> in the Genetic Background column of the Summary ribbon and click it.
        self.driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[3]/a').click()
        #switch focus to the new tab for Strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        ptitle = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        #Assert the page title is for the correct strain name
        self.assertEqual(ptitle.text, "C57BL/6J-Rr29Dz", 'Page title is not correct!')
        #switch focus back to the tab for Phenotypes associated with this allele page
        self.driver.switch_to.window(self.driver.window_handles[+1])
        #find the first link for C57BL/6J-Shh<Dz> in the Genetic Background section of the Genotype ribbon and click it.
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div[2]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/a').click()
        #switch focus to the new tab for Strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        ptitle = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        #Assert the page title is for the correct strain name
        self.assertEqual(ptitle.text, "C57BL/6J-Rr29Dz", 'Page title is not correct!')   
               
    def test_pheno_disease_table(self):
        '''
        @status this test verifies these Alleles have the correct Disease models and sorted alphabetically.
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Trp53')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1Tyj').click()

        actualurl = self.driver.find_element(By.LINK_TEXT, 'breast cancer').get_attribute('href')
        
        self.assertEqual(actualurl, 'https://mgitest.jax.org/disease/DOID:1612')
        self.driver.get(config.TEST_URL + "/allele/")
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Trp53')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1Tyj').click()
        diseasesort = self.driver.find_element(By.ID, 'diseasetable_id')
        items = diseasesort.find_elements(By.CSS_SELECTOR, 'a.MP')
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        
        self.assertIn("breast cancer", searchTreeItems)
        self.assertIn("diffuse large B-cell lymphoma", searchTreeItems)
        self.assertIn("glioblastoma", searchTreeItems)
        self.assertIn("Li-Fraumeni syndrome", searchTreeItems)
        self.assertIn("lymphoma", searchTreeItems)
        self.assertIn("malignant astrocytoma", searchTreeItems)
        self.assertIn("medulloblastoma", searchTreeItems)
        self.assertIn("myxoid liposarcoma", searchTreeItems)
        self.assertIn("neurofibromatosis", searchTreeItems)
        self.assertIn("pancreatic carcinoma", searchTreeItems)
        self.assertIn("Peutz-Jeghers syndrome", searchTreeItems)

    
    def test_pheno_show_hide(self):
        '''
        @status this test verifies these Alleles with phenotypes ribbon show/hide affected systems properly.
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Tg(ACTFLPe)9205Dym')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Tg(ACTFLPe)9205Dym').click()
        self.driver.find_element(By.ID, 'showPhenoButton').click()
        phenotypesort = self.driver.find_element(By.ID, 'phenotable_id')
        items = phenotypesort.find_elements(By.CSS_SELECTOR, '.phenoSummarySystemRow td:first-child, .phenoSummaryTermRow td:first-child')
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        print(searchTreeItems)
        self.assertEqual(['behavior/neurological', '', '', '', '', '', 'cardiovascular system',  '', 'hearing/vestibular/ear', '', 'mortality/aging', '', 'nervous system', '', ''], searchTreeItems)
        self.driver.get(config.TEST_URL + "/allele/")    
        
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Tg(ACTFLPe)9205Dym')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Tg(ACTFLPe)9205Dym').click()
        #self.driver.find_element(By.LINK_TEXT, 'show').click()
        phenotypesort = self.driver.find_element(By.ID, 'phenotable_id')
        items = phenotypesort.find_elements(By.CSS_SELECTOR, '.phenoSummarySystemRow div:first-child')
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["behavior/neurological", "cardiovascular system", "hearing/vestibular/ear", "mortality/aging", "nervous system"], searchTreeItems)
    
    def test_geno_popup_data(self):
        '''
        @status this test verifies the data found in a genotype popup page.
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('lepr')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Leprdb').click()
        wait.forAjax(self.driver, 2)
        self.driver.find_element(By.CSS_SELECTOR, '#yui-rec0 > td:nth-child(1) > div:nth-child(1) > a:nth-child(1) > span:nth-child(1)').click()
        # switch focus to the new tab for Phenotypes Associated with this Genotype page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        self.assertEqual(page_title.text, "Phenotypes Associated with This Genotype")
        mgi_id = self.driver.find_element(By.CLASS_NAME, 'genoID')
        self.assertEqual(mgi_id.text, 'MGI:4429457')
        geno_type_id = self.driver.find_element(By.CSS_SELECTOR, '.hmGeno.genotypeType')
        self.assertEqual(geno_type_id.text, 'hm1')
        allelesystems = self.driver.find_elements(By.CLASS_NAME, 'mpSystemRow')
        allelesystems = iterate.getTextAsList(allelesystems)
        print(allelesystems)
        self.assertEqual(allelesystems, ['homeostasis/metabolism', 'behavior/neurological', 'renal/urinary system'])
  
        '''
        *** many more tests from AlleleDetailPhenoSummary2.html needed
        '''
    def test_allele_img_suppression(self):
        '''
        @status this test verifies that Molecular images are not included on allele detail pages. Verifies only 3 rows of data returned for this allele.
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Ecscr')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ecscrtm1Iked').click()
        image_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, '3 phenotype image(s)')
        image_link.click()
        row_count = len(self.driver.find_elements(By.XPATH, "//table[@class='borderedTable']/tbody/tr"))
        #NOTE: 2 rows are  used for the header, so actual data rows would be 3
        self.assertEqual(5, row_count)
        self.driver.get(config.TEST_URL + "/allele/")
        '''
        @todo Table needs an id to finish this test
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Stk11')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1Jish').click()
        image_link = self.driver.find_element(By.ID, '???').find_element(By.TAG_NAME, 'img')
        image_link.click()
        row_count = len(self.driver.find_elements(By.XPATH, "//table[@class='borderedTable']/tbody/tr"))
        #NOTE: 2 rows are  used for the header, so actual data rows would be 3
        self.assertEqual("5", row_count)
        '''
        
    def test_disease_doids(self):
        '''
        @status this test verifies In the Disease models section, that after each disease in the disease table is it's corresponding DO ID.
        @bug once DOIDs added need to retest
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys('Gata1')
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm2Sho').click()
        disease_table = self.driver.find_element(By.ID, 'diseasetable_id')
        table = Table(disease_table)
        #Iterate and print the search results headers
        header_cells = table.get_header_cells()
        print(iterate.getTextAsList(header_cells))
        
        # print row 1
        cells = table.get_column_cells("Human Diseases")
        disease_cells = iterate.getTextAsList(cells)
        print(disease_cells)
        self.assertEqual(disease_cells[1], 'myelofibrosis\nIDs')
        
    def test_allele_detail_exp_sec_both_links_simple_geno(self):
        '''
        @status this test verifies in the expression section that both the assay results & anatomical structures links
        exist when Allele w/ MP terms annotated to simple genotypes that roll-up.
        @note: test #1
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ccnd3<tm1Pisc>")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1Pisc').click()
        #verifies that the assays results link exists/is displayed
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'assay results').is_displayed()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'anatomical structures').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'titleBarMainTitleGxd'), 'Mouse Developmental Anatomy Browser'))
        #Captures the anatomy search results
        searchList = self.driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchList)
        print([x.text for x in searchList])
        
        # The term 'thymus' should be returned in the anatomy search results
        self.assertIn('thymus TS24-28', terms, 'the term thymus is not listed!')
        
    def test_allele_detail_exp_sec_both_links_cond_geno(self):
        '''
        @status this test verifies in the expression section that both the assay results & anatomical structures links exist when Allele w/ MP terms annotated to conditional genotypes that roll-up when a recombinase allele is factored out.
        @note: Test #2
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Tardbp<tm1.1Ckjs>")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1.1Ckjs').click()
        #verifies that the assays results link exists/is displayed
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'assay results').is_displayed()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'anatomical structures').click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'titleBarMainTitleGxd'), 'Mouse Developmental Anatomy Browser'))
        searchList = self.driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchList)
        print([x.text for x in searchList])
        
        # There should be 5 structures returned in the anatomy search results
        self.assertIn('mouse TS1-28\nmuscle organ TS28\nmuscle tissue TS12-28\nspinal cord ventral horn TS20-28\nventral grey horn TS21-26\nvertebral column TS27-28', terms, 'the 5 terms are not listed!')        
        
    def test_allele_detail_exp_sec_struct_link_only_norm(self):
        '''
        @status this test verifies in the expression section that just the anatomical structures links exist when Allele w/ a mapping that only has Normal annotations; don't include that tissue
        @note: Test #6
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Adam17<tm1.1Wesh>")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1.1Wesh').click()
        #verifies that the assays results link does not exist/is not displayed
        bodyText = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertFalse('assay results' in bodyText)  
        #verifies that the anatomical structures link does exist and clicks it
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'anatomical structures').click()
        searchList = self.driver.find_elements(By.ID, 'searchResults')
        terms = iterate.getTextAsList(searchList)
        print([x.text for x in searchList])
        
        # There should be 5 structures returned in the anatomy search results
        self.assertIn('cardiac muscle tissue TS12-28\nheart TS11-28\nlung epithelium TS15-28\nlung mesenchyme TS15-26\nlung vascular element TS15-28', terms, 'the 5 terms are not listed!')        

    def test_allele_detail_no_exp_section(self):
        '''
        @status this test verifies no expression section when Allele w/ expressed gene that does not match the gene of the allele
        @note: Test #7
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ak7<tg(tetO-Hmox1)67Sami>")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '67Sami').click()
        #verifies that the assays results and anatomical structures links do not exist/are not displayed
        bodyText = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertFalse('assay results' in bodyText) 
        self.assertFalse('anatomical structures' in bodyText)  

    def test_allele_detail_no_exp_section_norm_noRollUp(self):
        '''
        @status this test verifies no expression section when Allele with MP terms that are 1) Normal; and 2) annotated to genotypes that don't roll-up
        @note: Test #19
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Tg(MMTV-rtTA)1Lach")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '1Lach').click()
        #verifies that the assays results and anatomical structures links do not exist/are not displayed
        bodyText = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertFalse('assay results' in bodyText) 
        self.assertFalse('anatomical structures' in bodyText)  

    def test_allele_detail_exp_sec_assays_link_only(self):
        '''
        @status this test verifies in the expression section that just the assay results link exists when Allele w/ expression results but no tissues (simple genotype's MP terms don't have mappings and other genotypes don't roll up)
        @note: Test #21
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Trim27<Gt(XP0484)Wtsi>")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Wtsi').click()
        #verifies that the assays results link does exist/is displayed
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'assay results').click()
        allele_name = self.driver.find_element(By.CLASS_NAME, 'summaryHeaderData1').find_element(By.TAG_NAME, "span")
        # Just want to assert the correct Allele is returned
        self.assertEqual(allele_name.text, 'gene trap XP0484, Wellcome Trust Sanger Institute')
        #verifies that the anatomical structures link does not exist
        bodyText = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertFalse('anatomical structures' in bodyText)  

    def test_allele_detail_Relates_to_human(self):
        '''
        @status this test verifies in the mutation section that now if expressed in a Human gene, it is represented.
        @note: CRM-58
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Apoe<tm2.1(APOE_i3)Hol>")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Hol').click()
        #find the first right arrow in the Mutation Description section and click it
        expressesRightArrow = self.driver.find_element(By.ID, 'rightArrowExpressesComponent')
        expressesRightArrow.click()
        expresses_table = self.driver.find_element(By.CLASS_NAME, 'detail')
        table = Table(expresses_table)
        #iterate and print the table headers
        header_cells = table.get_header_cells()
        print (iterate.getTextAsList(header_cells))
        # find the text in the Organism column and print it
        org_cell = table.get_cell(1, 0)
        print (org_cell.text)
        #verify the organism is Human
        self.assertEquals(org_cell.text, 'human')

    def test_allele_detail_Relates_to_Rat(self):
        '''
        @status this test verifies in the mutation section that now if expressed in a Rat gene, it is represented.
        @note: CRM-58
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Gt(ROSA)26Sor<tm1(Wnk1)Clhu>")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Clhu').click()
        #find the first right arrow in the Mutation Description section and click it
        expressesRightArrow = self.driver.find_element(By.ID, 'rightArrowExpressesComponent')
        expressesRightArrow.click()
        expresses_table = self.driver.find_element(By.CLASS_NAME, 'detail')
        table = Table(expresses_table)
        #iterate and print the table headers
        header_cells = table.get_header_cells()
        print (iterate.getTextAsList(header_cells))
        # find the text in the Organism column and print it
        org_cell = table.get_cell(1, 0)
        print (org_cell.text)
        #verify the organism is Human
        self.assertEqual(org_cell.text, 'rat')

    def test_allele_detail_Relates_to_Zebrafish(self):
        '''
        @status this test verifies in the mutation section that now if expressed in a Zebrafish gene, it is represented.
        @note: CRM-58
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Tg(MMTV-Catnb)3Pac")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '3Pac').click()
        #find the first right arrow in the Mutation Description section and click it
        expressesRightArrow = self.driver.find_element(By.ID, 'rightArrowExpressesComponent')
        expressesRightArrow.click()
        expresses_table = self.driver.find_element(By.CLASS_NAME, 'detail')
        table = Table(expresses_table)
        #iterate and print the table headers
        header_cells = table.get_header_cells()
        print (iterate.getTextAsList(header_cells))
        # find the text in the Organism column and print it
        org_cell = table.get_cell(1, 0)
        print (org_cell.text)
        #verify the organism is Human
        self.assertEqual(org_cell.text, 'zebrafish')

    def test_allele_detail_Relates_to_Fruitfly(self):
        '''
        @status this test verifies in the mutation section that now if expressed in a Fruitfly gene, it is represented.
        @note: CRM-58
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Tg(CAG-H3.3A/EGFP)1Dean")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '1Dean').click()
        #find the first right arrow in the Mutation Description section and click it
        expressesRightArrow = self.driver.find_element(By.ID, 'rightArrowExpressesComponent')
        expressesRightArrow.click()
        expresses_table = self.driver.find_element(By.CLASS_NAME, 'detail')
        table = Table(expresses_table)
        #iterate and print the table headers
        header_cells = table.get_header_cells()
        print (iterate.getTextAsList(header_cells))
        # find the text in the Organism column and print it
        org_cell = table.get_cell(1, 0)
        print (org_cell.text)
        #verify the organism is Fruit Fly
        self.assertEqual(org_cell.text, 'Drosophila melanogaster')

    def test_allele_detail_Relates_to_Yeast(self):
        '''
        @status this test verifies in the mutation section that now if expressed in a Yeast gene, it is represented.
        @note: CRM-58
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Tg(CMV-GAL4)1Wrk")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '1Wrk').click()
        #find the first right arrow in the Mutation Description section and click it
        expressesRightArrow = self.driver.find_element(By.ID, 'rightArrowExpressesComponent')
        expressesRightArrow.click()
        expresses_table = self.driver.find_element(By.CLASS_NAME, 'detail')
        table = Table(expresses_table)
        #iterate and print the table headers
        header_cells = table.get_header_cells()
        print (iterate.getTextAsList(header_cells))
        # find the text in the Organism column and print it
        org_cell = table.get_cell(1, 0)
        print (org_cell.text)
        #verify the organism is Human
        self.assertEqual(org_cell.text, 'yeast')

    def test_allele_detail_Recomb_structure(self):
        '''
        @status this test verifies in the Recombinase activity section that default main structures are correct.
        @note: CRM-58, alldetail-recombact-4
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("gfi1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Gan').click()
        #find the toggle arrow in the Recombinase activity section and click it to open up the grid.
        gridArrow = self.driver.find_element(By.ID, 'recomRibbonTeaser')
        gridArrow.click()
        #find and print the E table headers
        header_cell1 = self.driver.find_element(By.CSS_SELECTOR, '.pgg-table > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(2) > div:nth-child(1)')
        print (header_cell1.text)
        header_cell2 = self.driver.find_element(By.CSS_SELECTOR, '.pgg-table > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(3) > div:nth-child(1)')
        print (header_cell2.text)
        header_cell3 = self.driver.find_element(By.CSS_SELECTOR, '.pgg-table > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(4) > div:nth-child(1)')
        print (header_cell3.text)
        header_cell4 = self.driver.find_element(By.CSS_SELECTOR, '.pgg-table > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(5) > div:nth-child(1)')
        print (header_cell4.text)
        header_cell5 = self.driver.find_element(By.CSS_SELECTOR, '.pgg-table > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(6) > div:nth-child(1)')
        print (header_cell5.text)
        header_cell6 = self.driver.find_element(By.CSS_SELECTOR, '.pgg-table > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(7) > div:nth-child(1)')
        print (header_cell6.text)
        header_cell7 = self.driver.find_element(By.CSS_SELECTOR, '.pgg-table > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(8) > div:nth-child(1)')
        print (header_cell5.text)
        header_cell8 = self.driver.find_element(By.CSS_SELECTOR, '.pgg-table > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(9) > div:nth-child(1)')
        print (header_cell6.text)
        #verify the main E table headers are correct
        self.assertEqual(header_cell1.text, 'Embryonic (E0-8.9)')
        self.assertEqual(header_cell2.text, 'Embryonic (E9-13.9)')
        self.assertEqual(header_cell3.text, 'Embryonic (E14-21)')
        self.assertEqual(header_cell4.text, 'Newborn (P0-3.9)')
        self.assertEqual(header_cell5.text, 'Pre-weaning (P4-21.9)')
        self.assertEqual(header_cell6.text, 'Post-weaning (P22-42.9)')
        self.assertEqual(header_cell7.text, 'Adult (P>43)')
        self.assertEqual(header_cell8.text, 'Postnatal (age unspecified)')
        # find the text in the Systems column(main headers only)
        activity1 = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(1) > td:nth-child(1) > span:nth-child(1)')
        print (activity1.text)
        activity2 = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(9) > td:nth-child(1) > span:nth-child(1)')
        activity3 = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(11) > td:nth-child(1) > span:nth-child(1)')
        activity4 = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(26) > td:nth-child(1) > span:nth-child(1)')
        activity5 = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(28) > td:nth-child(1) > span:nth-child(1)')
        activity6 = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(30) > td:nth-child(1) > span:nth-child(1)')
        activity7 = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(32) > td:nth-child(1) > span:nth-child(1)')
        activity8 = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(36) > td:nth-child(1) > span:nth-child(1)')
        activity9 = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(39) > td:nth-child(1) > span:nth-child(1)')
        activity10 = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(41) > td:nth-child(1) > span:nth-child(1)')
        activity11 = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(53) > td:nth-child(1) > span:nth-child(1)')
        #verify the main header activity structures
        self.assertEqual(activity1.text, 'alimentary system')
        self.assertEqual(activity2.text, 'cardiovascular system')
        self.assertEqual(activity3.text, 'head')
        self.assertEqual(activity4.text, 'hemolymphoid system')
        self.assertEqual(activity5.text, 'integumental system')
        self.assertEqual(activity6.text, 'liver & biliary system')
        self.assertEqual(activity7.text, 'nervous system')
        self.assertEqual(activity8.text, 'renal & urinary system')
        self.assertEqual(activity9.text, 'respiratory system')
        self.assertEqual(activity10.text, 'sensory organs')
        self.assertEqual(activity11.text, 'skeletal system')
        
    def test_allele_detail_Recomb_structure_popup(self):
        '''
        @status this test verifies in the Recombinase activity section that when you click on a blue box it displays a popup.
        @note: CRM-116, alldetail-recombact-5
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("gfi1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Gan').click()
        #find the toggle arrow in the Recombinase activity section and click it to open up the grid.
        gridArrow = self.driver.find_element(By.ID, 'recomRibbonTeaser')
        gridArrow.click()
        #locate the light blue field for nervous system E14-19.5
        c_color = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(32) > td:nth-child(4)').get_attribute('class')
        #assert the field has the correct class name of pgg-cell b1
        self.assertEqual(c_color, 'pgg-cell b1')
        #locate the blank field with yellow corner for nervous system P0-21
        c_color = self.driver.find_element(By.CSS_SELECTOR, 'td.gold-corner').get_attribute('class')
        #assert the field has the correct class name of pgg-cell gold-corner
        self.assertEqual(c_color, 'pgg-cell gold-corner')
        # find the blue box for alimentary system E14-21 and click it
        self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(1) > td:nth-child(4)').click()
        #find the heading text and print it
        header = self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[5]/td[2]/div/table/tbody/tr[1]/td[2]/div[2]/div/div/div[2]/div[2]/div/span")
        print(header.text)
        #find the number of Yes results and print it
        data_yes = self.driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[5]/td[2]/div/table/tbody/tr[1]/td[2]/div[2]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]')
        print(data_yes.text)        
        #verify the heading text is correct
        self.assertEqual(header.text, 'alimentary system (Embryonic (E14-21))')
        #verify the number of Yes results are correct
        self.assertEqual(data_yes.text, '8')

    def test_allele_detail_Recomb_structure_popup2(self):
        '''
        @status this test verifies in the Recombinase activity section that when you click on a blue box with yellow corner it displays a popup.
        @note: CRM-116, alldetail-recombact-6
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Tg(ACTA1-cre)79Jme")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '79Jme').click()
        #find the toggle arrow in the Recombinase activity section and click it to open up the grid.
        gridArrow = self.driver.find_element(By.ID, 'recomRibbonTeaser')
        gridArrow.click()
        #locate the blank field for adipose system E9.0-13.9
        c_color = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(1) > td:nth-child(3)').get_attribute('class')
        #assert the field has the correct class name of pgg-cell empty-circle
        self.assertEqual(c_color, 'pgg-cell empty-circle')
        #locate the circle field for adipose system E14-21
        c_color = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(1) > td:nth-child(4)').get_attribute('class')
        #assert the field has the correct class name of pgg-cell empty-circle
        self.assertEqual(c_color, 'pgg-cell empty-circle')
        #locate the light red field for adipose system P4-21.9
        c_color = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(1) > td:nth-child(6)').get_attribute('class')
        #assert the field has the correct class name of pgg-cell r1
        self.assertEqual(c_color, 'pgg-cell r1')
        #locate the blue with yellow corner field for alimentary system P4-21.9
        c_color = self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(4) > td:nth-child(6)').get_attribute('class')
        #assert the field has the correct class name of pgg-cell b2g
        self.assertEqual(c_color, 'pgg-cell b2g')
        # find the blue box with yellow corner for alimentary system P4-21.9 and click it
        self.driver.find_element(By.CSS_SELECTOR, 'tr.pgg-row:nth-child(4) > td:nth-child(6)').click()
        #find the heading text and print it
        header = self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[5]/td[2]/div/table/tbody/tr[1]/td[2]/div[2]/div/div/div[2]/div[2]/div/span")
        print(header.text)
        #find the number of Yes results and print it
        data_yes = self.driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[5]/td[2]/div/table/tbody/tr[1]/td[2]/div[2]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]')
        print(data_yes.text)
        #find the number of No/Ambiguous results and print it
        data_noamb = self.driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[5]/td[2]/div/table/tbody/tr[1]/td[2]/div[2]/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]')
        print(data_noamb.text)        
        #verify the heading text is correct
        self.assertEqual(header.text, 'alimentary system (Pre-weaning (P4-21.9))')
        #verify the number of Yes results are correct
        self.assertEqual(data_yes.text, '6')
        #verify the number of No/Ambiguous results are correct
        self.assertEqual(data_noamb.text, '3')

    def test_allele_detail_Alliance_link(self):
        '''
        @status this test verifies in the Summary section that an Alliance link to their allele page exists.
        @note: CRM-210,
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Aak1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1b(EUCOMM)Hmgu').click()
        #find the Alliance link in the Summary section and click it
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1b(EUCOMM)Hmgu').click()
        allele_var = self.driver.find_element(By.CSS_SELECTOR, '.d-none > h1:nth-child(1) > span:nth-child(1)')
        #assert the correct allele is returned
        self.assertEqual(allele_var.text, 'Aak1tm1b(EUCOMM)Hmgu')

    def test_allele_detail_impc_link(self):
        '''
        @status this test verifies in the Summary section that an IMPC link to their allele page exists.
        @note: CRM-211,
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Aak1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1b(EUCOMM)Hmgu').click()
        #time.sleep(2)
        #find the IMPC link in the Summary section and click it
        self.driver.find_element(By.CSS_SELECTOR, '#nomenTable > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2) > a:nth-child(1)').click()
        #time.sleep(2)
        gene = self.driver.find_element(By.CSS_SELECTOR, '.h1 > b:nth-child(1)')
        #assert the correct gene is returned
        self.assertEqual(gene.text, 'Gene: Aak1')

    def test_allele_detail_MMHCdb_link(self):
        '''
        @status this test verifies in the Tumor section that an MMHCdb link to their allele page exists.
        @note: CRM-212,
        '''
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pten")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'tm1.1Gle').click()
        #find the MMHCdb link in the Tumor section and click it
        self.driver.find_element(By.CSS_SELECTOR, '#tumorTable > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)').click()
        allele = self.driver.find_element(By.CSS_SELECTOR, 'li.term-selected:nth-child(1) > span:nth-child(1)')
        #assert the correct gene is returned
        self.assertEqual(allele.text, 'Ptentm1.1Gle')
        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAlleleDetail))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
        