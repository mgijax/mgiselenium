'''
Created on Jan 19, 2016

@author: jeffc
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MarkerDetailLinks(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox() 
        self.driver.get("http://mgiwiki.jax.org/mediawiki/index.php/sw:WI_Pages_by_Software_Product#Python_WI-postgres")

    def test_mrk_detail_links(self):
        self.driver.find_element_by_link_text("Pax*")
        assert "No results found" not in self.driver.page_source
        
    def test_snorna_links(self):
        self.driver.find_element_by_partial_link_text("snoRNA")
        assert "No results found" not in self.driver.page_source
       
    def test_jnumber_links(self):
        self.driver.find_element_by_link_text("J:69860")
        assert "No results found" not in self.driver.page_source

    def test_bmp3_links(self):
        self.driver.find_element_by_link_text("Bmp3")
        assert "No results found" not in self.driver.page_source
        
    def test_batch_links(self):
        self.driver.find_element_by_partial_link_text("Empty")
        assert "No results found" not in self.driver.page_source
        
    def test_microarray_links(self):
        self.driver.find_element_by_link_text("Trp53")
        assert "No results found" not in self.driver.page_source

    def test_intexplorer_links(self):
        self.driver.find_element_by_partial_link_text("Bmp4")
        assert "No results found" not in self.driver.page_source
        
    def test_goannotmrk_links(self):
        self.driver.find_element_by_partial_link_text("Pax6")
        assert "No results found" not in self.driver.page_source

    def test_goannotref_links(self):
        self.driver.find_element_by_partial_link_text("J:114843")
        assert "No results found" not in self.driver.page_source

    def test_goannotsum1_links(self):
        self.driver.find_element_by_partial_link_text("motility")
        assert "No results found" not in self.driver.page_source

    def test_goannotsum2_links(self):
        self.driver.find_element_by_link_text("digestion")
        assert "No results found" not in self.driver.page_source

    def test_alleleqf_links(self):
        self.driver.find_element_by_partial_link_text("Allele Query")
        assert "No results found" not in self.driver.page_source 

    def test_allelesum_links(self):
        self.driver.find_element_by_partial_link_text("Albino")
        assert "No results found" not in self.driver.page_source
    
    def test_allelesummrk_links(self):
        self.driver.find_element_by_partial_link_text("Atp7a")
        assert "No results found" not in self.driver.page_source

    def test_alleleannotdisease_links(self):
        self.driver.find_element_by_partial_link_text("annotated to diseases")
        assert "No results found" not in self.driver.page_source

    def test_allelesumref_links(self):
        self.driver.find_element_by_partial_link_text("J:24766")
        assert "No results found" not in self.driver.page_source

    def test_alleledetail_links(self):
        self.driver.find_element_by_link_text("agouti yellow")
        assert "No results found" not in self.driver.page_source

    def test_phenoimagedetail1_links(self):
        self.driver.find_element_by_link_text("image for agouti yellow")
        assert "No results found" not in self.driver.page_source

    def test_videoexample_links(self):
        self.driver.find_element_by_partial_link_text("CvDC")
        assert "No results found" not in self.driver.page_source

    def test_phenoimagemrk1_links(self):
        self.driver.find_element_by_link_text("a")
        assert "No results found" not in self.driver.page_source
            
    def test_phenoimagemrk2_links(self):
        self.driver.find_element_by_partial_link_text("Dnaic1")
        assert "No results found" not in self.driver.page_source

    def test_phenodetailgeno1_links(self):
        self.driver.find_element_by_partial_link_text("pop-up for ht2")
        assert "No results found" not in self.driver.page_source

    def test_phenodetailgeno2_links(self):
        self.driver.find_element_by_link_text("pop-up for Pax6-Sey-Neu")
        assert "No results found" not in self.driver.page_source

    def test_mutation_links(self):
        self.driver.find_element_by_link_text("for Del(2Hoxd11-Hoxd13)29Ddu")
        assert "No results found" not in self.driver.page_source

    def test_diseasebrowser_links(self):
        self.driver.find_element_by_partial_link_text("Browse for P")
        assert "No results found" not in self.driver.page_source
 
    def test_diseasedetail1_links(self):
        self.driver.find_element_by_partial_link_text("Diabetes mellitus")
        assert "No results found" not in self.driver.page_source

    def test_diseasedetail2_links(self):
        self.driver.find_element_by_link_text("Pancreatic Cancer")
        assert "No results found" not in self.driver.page_source

    def test_allmodels_links(self):
        self.driver.find_element_by_partial_link_text("All models")
        assert "No results found" not in self.driver.page_source

    def test_mpannotterm_links(self):
        self.driver.find_element_by_link_text("MP:0002098")
        assert "No results found" not in self.driver.page_source

    def test_mpannottermmrk_links(self):
        self.driver.find_element_by_partial_link_text("hormone level")
        assert "No results found" not in self.driver.page_source

    def test_diseaseqf_links(self):
        self.driver.find_element_by_link_text("Disease Connection")
        assert "No results found" not in self.driver.page_source

    def test_gridtab_links(self):
        self.driver.find_element_by_partial_link_text("hearing loss")
        assert "No results found" not in self.driver.page_source

    def test_grid1_links(self):
        self.driver.find_element_by_partial_link_text("Cdh23")
        assert "No results found" not in self.driver.page_source

    def test_grid2_links(self):
        self.driver.find_element_by_partial_link_text("Atp2b2")
        assert "No results found" not in self.driver.page_source

    def test_genocluster1_links(self):
        self.driver.find_element_by_link_text("one genotype")
        assert "No results found" not in self.driver.page_source

    def test_genocluster2_links(self):
        self.driver.find_element_by_link_text("multiple genotypes")
        assert "No results found" not in self.driver.page_source

    def test_genestab_links(self):
        self.driver.find_element_by_partial_link_text("gene tab")
        assert "No results found" not in self.driver.page_source

    def test_diseasetab_links(self):
        self.driver.find_element_by_partial_link_text("disease tab")
        assert "No results found" not in self.driver.page_source

    def test_refqf_links(self):
        self.driver.find_element_by_link_text("Ref QF")
        assert "No results found" not in self.driver.page_source

    def test_refsum_links(self):
        self.driver.find_element_by_link_text("2008")
        assert "No results found" not in self.driver.page_source

    def test_refsummrk_links(self):
        self.driver.find_element_by_link_text("Tyr")
        assert "No results found" not in self.driver.page_source

    def test_refsumallele_links(self):
        self.driver.find_element_by_partial_link_text("Myf5")
        assert "No results found" not in self.driver.page_source

    def test_refsum1_links(self):
        self.driver.find_element_by_link_text("Acan")
        assert "No results found" not in self.driver.page_source

    def test_refsum2_links(self):
        self.driver.find_element_by_link_text("Acondroplasia")
        assert "No results found" not in self.driver.page_source

    def test_refdetail1ref_links(self):
        self.driver.find_element_by_link_text("J:181372")
        assert "No results found" not in self.driver.page_source

    def test_gxdqf_links(self):
        self.driver.find_element_by_link_text("GXD Query Form")
        assert "No results found" not in self.driver.page_source

    def test_gxdsummrk_links(self):
        self.driver.find_element_by_link_text("Expression for Lit")
        assert "No results found" not in self.driver.page_source

    def test_gxdsumref_links(self):
        self.driver.find_element_by_link_text("J:61153")
        assert "No results found" not in self.driver.page_source

    def test_gxdsumprobe_links(self):
        self.driver.find_element_by_link_text("cdh6")
        assert "No results found" not in self.driver.page_source
 
    def test_gxdsumemap_links(self):
        self.driver.find_element_by_link_text("common atrial chamber")
        assert "No results found" not in self.driver.page_source
 
    def test_gxddetailinsitu_links(self):
        self.driver.find_element_by_link_text("RNA in situ")
        assert "No results found" not in self.driver.page_source

    def test_gxddetailblot_links(self):
        self.driver.find_element_by_link_text("Northern Blot")
        assert "No results found" not in self.driver.page_source
                                                                                                                                                  
                                                   
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()