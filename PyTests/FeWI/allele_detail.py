'''
Created on May 23, 2016

@author: jeffc
This suite of tests are for allele detail pages
'''
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
from util import wait, iterate
from genericpath import exists
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)
import config
from config import PWI_URL

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(config.FEWI_URL + "/allele/")
        self.driver.implicitly_wait(10)

    def test_ribbon_locations(self):
        '''
        @status This test verifies the ribbons are being displayed in the correct order on the page.
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Pkd1")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text("tm2Jzh").click()
        assert "Pkd1<sup>tm2Jzh</sup>" in self.driver.page_source
        assert 'id="nomenclatureHeader"' in self.driver.page_source
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
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Slc6a3")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text("tm1(cre)Xz").click()
        assert "Slc6a3<sup>tm1(cre)Xz</sup>" in self.driver.page_source
        assert 'id="nomenclatureHeader"' in self.driver.page_source
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
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Pax3")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text("tm1(cre)Joe").click()
        assert "Pax3<sup>tm1(cre)Joe</sup>" in self.driver.page_source
        assert 'id="nomenclatureHeader"' in self.driver.page_source
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
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Arrdc3")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('Gt(CSE151)Byg').click()
        mutationDownArrow = self.driver.find_element_by_id('downArrowMutationDescription')
        mutationRightArrow = self.driver.find_element_by_id('rightArrowMutationDescription')
        
        self.assertTrue(mutationDownArrow.is_displayed())
        self.assertFalse( mutationRightArrow.is_displayed())
        
        mutationDownArrow.click()
        
        mutationDownArrow = self.driver.find_element_by_id('downArrowMutationDescription')
        mutationRightArrow = self.driver.find_element_by_id('rightArrowMutationDescription')
        
        self.assertFalse( mutationDownArrow.is_displayed())
        self.assertTrue( mutationRightArrow.is_displayed())
        
        sequenceDownArrow = self.driver.find_element_by_id('downArrowSeqTag')
        sequenceRightArrow = self.driver.find_element_by_id('rightArrowSeqTag')
         
        self.assertFalse( sequenceDownArrow.is_displayed())
        self.assertTrue( sequenceRightArrow.is_displayed())
        
        sequenceRightArrow.click()
        
        sequenceDownArrow = self.driver.find_element_by_id('downArrowSeqTag')
        sequenceRightArrow = self.driver.find_element_by_id('rightArrowSeqTag')
        
        self.assertTrue( sequenceDownArrow.is_displayed())
        self.assertFalse( sequenceRightArrow.is_displayed())

        genomeDownArrow = self.driver.find_element_by_id('downArrowGenome')
        genomeRightArrow = self.driver.find_element_by_id('rightArrowGenome')
         
        self.assertFalse( genomeDownArrow.is_displayed())
        self.assertTrue( genomeRightArrow.is_displayed())
        
        genomeRightArrow.click()
        
        genomeDownArrow = self.driver.find_element_by_id('downArrowGenome')
        genomeRightArrow = self.driver.find_element_by_id('rightArrowGenome')
        
        self.assertTrue( genomeDownArrow.is_displayed())
        self.assertFalse( genomeRightArrow.is_displayed())
        
    def test_no_turnstile(self):
        '''
        @status this test verifies In the Mutation Description section, confirm that no turnstile icon exists because the notes are less than 100 characters.
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Kit")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('Ssm').click()
        #mutationDownArrow = self.driver.find_element_by_id('downArrowMutationDescription').
        #mutationRightArrow = self.driver.find_element_by_id('rightArrowMutationDescription')
        
        assert 'id= "downArrowMutationDescription"' not in self.driver.page_source
        assert 'id= "rightArrowMutationDescription"' not in self.driver.page_source
        
    def test_turnstile_largenote(self):
        '''
        @status this test verifies In the Mutation Description section, confirm the turnstile is open for Mutation Notes(large note) and displays the complete information
        (no text is cut off).
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Car12")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('4563.1Dla').click()
        mutationDownArrow = self.driver.find_element_by_id('downArrowMutationDescription')
        mutationRightArrow = self.driver.find_element_by_id('rightArrowMutationDescription')
        
        self.assertTrue(mutationDownArrow.is_displayed())
        self.assertFalse( mutationRightArrow.is_displayed())
        
        mutationDownArrow.click()
        
        mutationDownArrow = self.driver.find_element_by_id('downArrowMutationDescription')
        mutationRightArrow = self.driver.find_element_by_id('rightArrowMutationDescription')
        
        self.assertFalse( mutationDownArrow.is_displayed())
        self.assertTrue( mutationRightArrow.is_displayed())
    
    def test_allele_subtype(self):
        '''
        @status this test verifies  Allele subtypes appear in Mutation Description ribbon on Allele Detail Pages
         as a comma separated list following the allele type. 
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Kdr")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('tm1Jrt').click()
        alleleType = self.driver.find_element_by_id('alleleTypeDisplay')
        
        self.assertEqual(alleleType.text, "Targeted (Null/knockout, Reporter)")
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Olig2")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('Htak').click()
        alleleType = self.driver.find_element_by_id('alleleTypeDisplay')
        
        self.assertEqual(alleleType.text, "Targeted (Inducible, Recombinase)")
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Tg(BCL2)1Tsk")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('Tg(BCL2)1Tsk').click()
        alleleType = self.driver.find_element_by_id('alleleTypeDisplay')
        
        self.assertEqual(alleleType.text, "Transgenic (Inserted expressed sequence)")
        
    def test_allele_nosubtype(self):
        '''
        @status this test verifies Allele Subtypes do not appear when the allele is not assigned to a subtype.
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Lith20")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('SM/J').click()
        alleleType = self.driver.find_element_by_id('alleleTypeDisplay')
        
        self.assertEqual(alleleType.text, "QTL")
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Tg(Id1*-lacZ)1C10Oxb")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('Tg(Id1*-lacZ)1C10Oxb').click()
        alleleType = self.driver.find_element_by_id('alleleTypeDisplay')
        
        self.assertEqual(alleleType.text, "Transgenic")
        
    def test_allele_molecular_image(self):
        '''
        @status this test verifies Allele Detail page displays molecular image in the molecular description ribbon.
        
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Tgm3")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('tm1Sjo').click()
        
        image = self.driver.find_element_by_id('mutationDescriptionTable').find_element_by_css_selector('a img')
        self.assertTrue(image.is_displayed(), 'the image is not displaying')
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Dock2")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('Hsd').click()
        
        image = self.driver.find_element_by_id('mutationDescriptionTable').find_element_by_css_selector('a img')
        self.assertTrue(image.is_displayed(), 'the image is not displaying')
        
        
    def test_mutagenetix_link(self):
        '''
        @status this test verifies these Alleles have the Mutagentix link in the Mutation Description ribbon(under Mutation Details) and the link works.
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Blnk")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('m1Btlr').click()
        mutagenetixlink = self.driver.find_element_by_link_text('incidental mutations')
        actualurl = self.driver.find_element_by_link_text('incidental mutations').get_attribute("href")
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, 'ftp://devftp.informatics.jax.org/pub/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Irf7")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('m1Btlr').click()
        mutagenetixlink = self.driver.find_element_by_link_text('incidental mutations')
        actualurl = self.driver.find_element_by_link_text('incidental mutations').get_attribute("href")
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, 'ftp://devftp.informatics.jax.org/pub/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.FEWI_URL + "/allele/")
            
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Col4a4")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('m1Btlr').click()
        mutagenetixlink = self.driver.find_element_by_link_text('incidental mutations')
        actualurl = self.driver.find_element_by_link_text('incidental mutations').get_attribute("href")
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, 'ftp://devftp.informatics.jax.org/pub/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Nfkbid")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('m1Btlr').click()
        mutagenetixlink = self.driver.find_element_by_link_text('incidental mutations')
        actualurl = self.driver.find_element_by_link_text('incidental mutations').get_attribute("href")
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, 'ftp://devftp.informatics.jax.org/pub/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Unc93b1")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('3d').click()
        mutagenetixlink = self.driver.find_element_by_link_text('incidental mutations')
        actualurl = self.driver.find_element_by_link_text('incidental mutations').get_attribute("href")
        
        self.assertEqual(mutagenetixlink.text, "incidental mutations")
        self.assertEqual(actualurl, 'ftp://devftp.informatics.jax.org/pub/datasets/incidental_muts/Mutagenetix.xlsx')
        self.driver.get(config.FEWI_URL + "/allele/")
    
    def test_allele_molecular_image_caption(self):
        '''
        @status this test verifies Allele Detail page displays thumbnail caption to the left of the molecular image in the molecular description ribbon.
        @bug: This page needs the table to have an ID before a test can really be written
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Stk11")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('tm1.1Jish').click()
        
        caption = self.driver.find_element_by_id('mutationDescriptionTable').find_element_by_css_selector('span.small')
        self.assertTrue(caption.is_displayed(), 'the caption is not displaying')
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Supv3l1")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('tm2.1Jkl').click()
        
        caption = self.driver.find_element_by_id('mutationDescriptionTable').find_element_by_css_selector('span')
        self.assertTrue(caption.is_displayed(), 'the caption is not displaying')
        self.driver.get(config.FEWI_URL + "/allele/")
        
        #6.The correct image/caption is displayed to the left of the molecular image in the molecular description ribbon when more than one thumbnail exists for an allele.
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Dock2")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('Hsd').click()
        
        caption = self.driver.find_element_by_id('mutationDescriptionTable').find_element_by_css_selector('span')
        self.assertEquals(caption.text, 'Schematic showing the duplication and location of the premature stop codon in the Dock2<mu> allele found in Irf5<tm1Ttg>/Irf5<tm1Ttg> mice')
        
        
    def test_afp_link(self):
        '''
        @status this test verifies these Alleles have the Australian Phenome Facility link in the Mutation Description ribbon(under Mutation Details) and the link works.
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Adamts20")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('hip').click()
        afplink = self.driver.find_element_by_link_text('incidental mutations')
        actualurl = self.driver.find_element_by_link_text('incidental mutations').get_attribute("href")
        
        self.assertEqual(afplink.text, "incidental mutations")
        self.assertEqual(actualurl, 'ftp://devftp.informatics.jax.org/pub/datasets/incidental_muts/APF.xlsx')
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Nphp3")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('pol').click()
        afplink = self.driver.find_element_by_link_text('incidental mutations')
        actualurl = self.driver.find_element_by_link_text('incidental mutations').get_attribute("href")
        
        self.assertEqual(afplink.text, "incidental mutations")
        self.assertEqual(actualurl, 'ftp://devftp.informatics.jax.org/pub/datasets/incidental_muts/APF.xlsx')
    
    def test_collection_value(self):
        '''
        @status this test verifies these Alleles have the correct project collection in the Mutation origin ribbon.
        
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("0610037L13Rik")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('tm1(KOMP)Vlcg').click()
        collection = self.driver.find_element_by_id('mutationOriginTable').find_elements_by_css_selector('td.padded')
        collitem = collection[5]
        self.assertEqual(collitem.text, "KOMP-Regeneron")
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Acan")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('b2b183Clo').click()
        collection = self.driver.find_element_by_id('mutationOriginTable').find_elements_by_css_selector('td.padded')
        collitem = collection[2]
        self.assertEqual(collitem.text, "B2B/CvDC")
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Adamts20")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('hip').click()
        collection = self.driver.find_element_by_id('mutationOriginTable').find_elements_by_css_selector('td.padded')
        collitem = collection[2]
        self.assertEqual(collitem.text, "APF ENU Mutagenesis")
        self.driver.get(config.FEWI_URL + "/allele/")
        
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Dbx1")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('tm1.1(cre)Mull').click()
        collection = self.driver.find_element_by_id('mutationOriginTable').find_elements_by_css_selector('td.padded')
        collitem = collection[4]
        self.assertEqual(collitem.text, "Neuroscience Blueprint cre")
        self.driver.get(config.FEWI_URL + "/allele/")
        
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Tg(Ucn3-cre)KF31Gsat")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('Tg(Ucn3-cre)KF31Gsat').click()
        collection = self.driver.find_element_by_id('mutationOriginTable').find_elements_by_css_selector('td.padded')
        collitem = collection[2]
        self.assertEqual(collitem.text, "GENSAT")
        self.driver.get(config.FEWI_URL + "/allele/")
        
        #Collection does not appear when the allele is not assigned to a collection. 
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Pax6")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('2Neu').click()
        assert "Project Collection" not in self.driver.page_source
        
    def test_pheno_disease_table(self):
        '''
        @status this test verifies these Alleles have the correct Disease models and sorted alphabetically.
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Trp53")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('tm1Tyj').click()
        actualurl = self.driver.find_element_by_link_text('Breast Cancer').get_attribute("href")
        
        self.assertEqual(actualurl, 'http://firien.informatics.jax.org/disease/114480')
        self.driver.get(config.FEWI_URL + "/allele/")
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Trp53")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('tm1Tyj').click()
        diseasesort = self.driver.find_element_by_id("diseasetable_id")
        items = diseasesort.find_elements_by_css_selector("a.MP")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        
        self.assertEqual(["Breast Cancer", "114480", "Li-Fraumeni Syndrome 1; LFS1", "151623", "Medulloblastoma; MDB", "155255", "Myxoid Liposarcoma", "613488", "Neurofibromatosis, Type I; NF1", "162200", "Pancreatic Cancer", "260350", "Peutz-Jeghers Syndrome; PJS", "175200"], searchTreeItems)
    
    def test_pheno_show_hide(self):
        '''
        @status this test verifies these Alleles with phenotypes ribbon show/hide affected systems properly.
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Tg(ACTFLPe)9205Dym")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('Tg(ACTFLPe)9205Dym').click()
        self.driver.find_element_by_link_text('show').click()
        phenotypesort = self.driver.find_element_by_id("phenotable_id")
        items = phenotypesort.find_elements_by_css_selector(".phenoSummarySystemRow td:first-child, .phenoSummaryTermRow td:first-child")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        
        self.assertEqual(["behavior/neurological", "tremors", "impaired balance", "impaired coordination", "abnormal gait", "short stride length", "cardiovascular system", "cardiovascular system phenotype", "hearing/vestibular/ear", "abnormal ear physiology", "mortality/aging", "perinatal lethality", "nervous system", "abnormal synaptic vesicle recycling", "abnormal excitatory postsynaptic currents"], searchTreeItems)
        self.driver.get(config.FEWI_URL + "/allele/")    
        
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Tg(ACTFLPe)9205Dym")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text('Tg(ACTFLPe)9205Dym').click()
        #self.driver.find_element_by_link_text('show').click()
        phenotypesort = self.driver.find_element_by_id("phenotable_id")
        items = phenotypesort.find_elements_by_css_selector(".phenoSummarySystemRow div:first-child")
        
        # add all li text to a list for "assertIn" test
        searchTreeItems = iterate.getTextAsList(items)
        self.assertEqual(["behavior/neurological", "cardiovascular system", "hearing/vestibular/ear", "mortality/aging", "nervous system"], searchTreeItems)
    
    def test_geno_popup_data(self):
        '''
        @status this test verifies the data found in a genotype popup page.
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("lepr")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_link_text("Leprdb").click()
        main_window = self.driver.window_handles[0]
        self.driver.find_element_by_link_text('hm1').click()
        
        wait.forNewWindow(self.driver)
        page_title = self.driver.find_element_by_class_name('titleBarMainTitle')
        self.assertEqual(page_title.text, "Phenotypes Associated with This Genotype")
        mgi_id = self.driver.find_element_by_class_name('genoID')
        self.assertEqual(mgi_id.text, 'MGI:4429457')
        geno_type_id = self.driver.find_element_by_css_selector('.hmGeno.genotypeType')
        self.assertEqual(geno_type_id.text, 'hm1')
        allelesystems = self.driver.find_elements_by_class_name("mpSystemRow")
        allelesystems = iterate.getTextAsList(allelesystems)
        print allelesystems
        self.assertEqual(allelesystems, ['homeostasis/metabolism', 'behavior/neurological', 'renal/urinary system'])
  
        '''
        *** many more tests from AlleleDetailPhenoSummary2.html needed
        '''
    def test_allele_img_suppression(self):
        '''
        @status this test verifies that Molecular images are not included on allele detail pages. Verifies only 3 rows of data returned for this allele.
        '''
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Ecscr")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_link_text("Ecscrtm1Iked").click()
        image_link = self.driver.find_element_by_partial_link_text('3 phenotype image(s)')
        image_link.click()
        row_count = len(self.driver.find_elements_by_xpath("//table[@class='borderedTable']/tbody/tr"))
        #NOTE: 2 rows are  used for the header, so actual data rows would be 3
        self.assertEqual(5, row_count)
        self.driver.get(config.FEWI_URL + "/allele/")
        '''
        @todo Table needs an id to finish this test
        self.driver.find_element_by_name("nomen").clear()
        self.driver.find_element_by_name("nomen").send_keys("Stk11")
        self.driver.find_element_by_class_name("buttonLabel").click()
        self.driver.find_element_by_partial_link_text("tm1Jish").click()
        image_link = self.driver.find_element_by_id('???').find_element_by_tag_name('img')
        image_link.click()
        row_count = len(self.driver.find_elements_by_xpath("//table[@class='borderedTable']/tbody/tr"))
        #NOTE: 2 rows are  used for the header, so actual data rows would be 3
        self.assertEqual("5", row_count)
        '''
        
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
