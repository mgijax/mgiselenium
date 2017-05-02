'''
Created on Dec 12, 2016
This test verifies all public links found on the wiki page mgiwiki/mediawiki/index.php/sw:WI_Pages_by_Software_Product.
It does not test what is found for data on each page.
@author: jeffc
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config

class TestMarkerDetailLinks(unittest.TestCase):

#Genes, Genome Features & Maps
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get(config.WIKI_URL + "sw:WI_Pages_by_Software_Product")

    def test_mrk_detail_links(self):
        self.driver.find_element_by_link_text("Pax*")
        assert "No results found" not in self.driver.page_source
        assert "pax*" in self.driver.page_source
        
    def test_snorna_links(self):
        self.driver.find_element_by_partial_link_text("snoRNA")
        assert "No results found" not in self.driver.page_source
        assert "snoRNA gene" in self.driver.page_source
       
    def test_jnumber_links(self):
        self.driver.find_element_by_link_text("J:69860")
        assert "No results found" not in self.driver.page_source
        assert "J:69860" in self.driver.page_source

    def test_bmp3_links(self):
        self.driver.find_element_by_link_text("Bmp3")
        assert "No results found" not in self.driver.page_source
        assert "Bmp3" in self.driver.page_source
        
    def test_batch_links(self):
        self.driver.find_element_by_partial_link_text("Empty")
        assert "No results found" not in self.driver.page_source
        
    def test_microarray_links(self):
        self.driver.find_element_by_link_text("Trp53")
        assert "No results found" not in self.driver.page_source

    def test_intexplorer_links(self):
        self.driver.find_element_by_partial_link_text("Bmp4")
        assert "No results found" not in self.driver.page_source

    def test_mappingsummrker_links(self):
        self.driver.find_element_by_link_text("Sry")
        assert "No results found" not in self.driver.page_source

    def test_mappingsumref_links(self):
        self.driver.find_element_by_link_text("J:2945")
        assert "No results found" not in self.driver.page_source

    def test_mapdetailcross_links(self):
        self.driver.find_element_by_link_text("Cross")
        assert "No results found" not in self.driver.page_source

    def test_mapdetailri_links(self):
        self.driver.find_element_by_link_text("RI")
        assert "No results found" not in self.driver.page_source

    def test_mapdetailtext_links(self):
        self.driver.find_element_by_link_text("TEXT")
        assert "No results found" not in self.driver.page_source

    def test_mapdetailtextgenetic_links(self):
        self.driver.find_element_by_link_text("TEXT-Genetic Cross")
        assert "No results found" not in self.driver.page_source
        
#GO                
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

    def test_markergograph_links(self):
        self.driver.find_element_by_link_text("Graph for Kit")
        assert "No results found" not in self.driver.page_source

    def test_gobrowser_link(self):
        self.driver.find_element_by_partial_link_text("Gene Ontology Browser")
        assert "No results found" not in self.driver.page_source

    def test_gotermdetail_links(self):
        self.driver.find_element_by_link_text("gastric motility")
        assert "No results found" not in self.driver.page_source

#Phenotypes Alleles & Disease Models
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
        
    def test_phenoimagedetail2_links(self):
        self.driver.find_element_by_link_text("Pheno Image for agouti yellow")
        assert "No results found" not in self.driver.page_source

    def test_phenoimageallele_links(self):
        self.driver.find_element_by_partial_link_text("Pheno Image DNaic 1 allele (CvDC example)")
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

    def test_mpbrowser_links(self):
        self.driver.find_element_by_link_text("Mammalian Phenotype Browser")
        assert "No results found" not in self.driver.page_source

    def test_mptermdetail_links(self):
        self.driver.find_element_by_link_text("Absent coat pigmentation")
        assert "No results found" not in self.driver.page_source

    def test_hpbrowser_links(self):
        self.driver.find_element_by_link_text("Human Phenotype Ontology Browser")
        assert "No results found" not in self.driver.page_source

    def test_hpotermdetail_links(self):
        self.driver.find_element_by_link_text("Gowers sign")
        assert "No results found" not in self.driver.page_source
        
#Human Mouse Disease Connection (Disease Portal)
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
        
#References
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
        
#Recombinase
    def test_creqf_links(self):
        self.driver.find_element_by_link_text("Minihome")
        assert "No results found" not in self.driver.page_source

    def test_cresummary_links(self):
        self.driver.find_element_by_link_text("Muscle")
        assert "No results found" not in self.driver.page_source

    def test_cresummary1_links(self):
        self.driver.find_element_by_link_text("Calb2")
        assert "No results found" not in self.driver.page_source
        
    def test_crespecificity_links(self):
        self.driver.find_element_by_partial_link_text("Foxg1")
        assert "No results found" not in self.driver.page_source

    def test_crespecificitynotdetected_links(self):
        self.driver.find_element_by_partial_link_text("Not detected")
        assert "No results found" not in self.driver.page_source
        
#Gene Expression
    def test_gxdqf_links(self):
        self.driver.find_element_by_link_text("GXD Query Form")
        assert "No results found" not in self.driver.page_source

    def test_gxdsummrk_links(self):
        self.driver.find_element_by_link_text("Expression for Kit")
        assert "No results found" not in self.driver.page_source

    def test_gxdsumref_links(self):
        self.driver.find_element_by_link_text("for J:61153")
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

    def test_gxdimagedetail_links(self):
        self.driver.find_element_by_link_text("Image for Lep")
        assert "No results found" not in self.driver.page_source

    def test_gxdlitsummary_links(self):
        self.driver.find_element_by_partial_link_text("Lit Sum for Brca1")
        assert "No results found" not in self.driver.page_source

    def test_gxdlitsumage_links(self):
        self.driver.find_element_by_partial_link_text("RNA/10.5")
        assert "No results found" not in self.driver.page_source

    def test_gxdlitdetail_links(self):
        self.driver.find_element_by_link_text("Bard1/J:91257")
        assert "No results found" not in self.driver.page_source

    def test_gxdlitsummrker_links(self):
        self.driver.find_element_by_link_text("Trp53")
        assert "No results found" not in self.driver.page_source

    def test_gxdlitsumref_links(self):
        self.driver.find_element_by_link_text("J:148991")
        assert "No results found" not in self.driver.page_source

    def test_gxdtissuemrker_links(self):
        self.driver.find_element_by_link_text("Shh")
        assert "No results found" not in self.driver.page_source

    def test_gxdemapa_links(self):
        self.driver.find_element_by_link_text("mouse")
        assert "No results found" not in self.driver.page_source

    def test_gxdantibodydetail_links(self):
        self.driver.find_element_by_link_text("MGI:2137372")
        assert "No results found" not in self.driver.page_source

    def test_prbsummrker_links(self):
        self.driver.find_element_by_link_text("probes Oxt")
        assert "No results found" not in self.driver.page_source

    def test_prbsumref_links(self):
        self.driver.find_element_by_link_text("J:2945")
        assert "No results found" not in self.driver.page_source

    def test_prbdetail_links(self):
        self.driver.find_element_by_link_text("MGI:901759")
        assert "No results found" not in self.driver.page_source

    def test_cdnasummrker_links(self):
        self.driver.find_element_by_link_text("cDNA Oxt")
        assert "No results found" not in self.driver.page_source

    def test_amabrowserresults_links(self):
        self.driver.find_element_by_link_text("Adult Mouse Anatomy Browser")
        assert "No results found" not in self.driver.page_source

    def test_amatermdetail_links(self):
        self.driver.find_element_by_link_text("Forebrain")
        assert "No results found" not in self.driver.page_source
        
#Homology
    def test_verthomology_links(self):
        self.driver.find_element_by_link_text("Homology Class 36030")
        assert "No results found" not in self.driver.page_source

    def test_gograph_links(self):
        self.driver.find_element_by_link_text("Graph for 36030")
        assert "No results found" not in self.driver.page_source

    def test_pirsf_links(self):
        self.driver.find_element_by_link_text("Paired box Protein Superfamily")
        assert "No results found" not in self.driver.page_source
        
#Sequences
    def test_seqsum_links(self):
        self.driver.find_element_by_link_text("T")
        assert "No results found" not in self.driver.page_source

    def test_seqsumref_links(self):
        self.driver.find_element_by_link_text("J:90438")
        assert "No results found" not in self.driver.page_source

    def test_seqsummrkerprovider_links(self):
        self.driver.find_element_by_link_text("Grid2/Refseq")
        assert "No results found" not in self.driver.page_source

    def test_seqsummrkerprovider2_links(self):
        self.driver.find_element_by_link_text("Grid2/Uniprot")
        assert "No results found" not in self.driver.page_source

    def test_seqdetailuniprot_links(self):
        self.driver.find_element_by_link_text("UniProt sequence")
        assert "No results found" not in self.driver.page_source

    def test_seqdetailrefseq_links(self):
        self.driver.find_element_by_link_text("RefSeq sequence")
        assert "No results found" not in self.driver.page_source
        
#SNPs & Polymorphisms
    def test_snpqf_links(self):
        self.driver.find_element_by_link_text("SNP Query Form")
        assert "No results found" not in self.driver.page_source

    def test_snpdetail_links(self):
        self.driver.find_element_by_link_text("rs51119329")
        assert "No results found" not in self.driver.page_source

    def test_snpsummary_links(self):
        self.driver.find_element_by_link_text("Query by Fmr1")
        assert "No results found" not in self.driver.page_source

    def test_snpsummarymarker_links(self):
        self.driver.find_element_by_link_text("Fmr1")
        assert "No results found" not in self.driver.page_source

    def test_polymorphsummrker_links(self):
        self.driver.find_element_by_link_text("Summary for Trp53")
        assert "No results found" not in self.driver.page_source

    def test_polymorphdetail_links(self):
        self.driver.find_element_by_link_text("RFLP Summary for Trp53")
        assert "No results found" not in self.driver.page_source
        
#Miscellaneous    
    def test_accreport1_links(self):
        self.driver.find_element_by_link_text("ID=36030")
        assert "No results found" not in self.driver.page_source

    def test_accreport2_links(self):
        self.driver.find_element_by_link_text("ID=Ren1")
        assert "No results found" not in self.driver.page_source

    def test_glossaryindex_links(self):
        self.driver.find_element_by_link_text("Glossary Index")
        assert "No results found" not in self.driver.page_source

    def test_glossaryterm_links(self):
        self.driver.find_element_by_link_text("Boolean")
        assert "No results found" not in self.driver.page_source

#Python WI
    def test_knockoutsum_links(self):
        self.driver.find_element_by_link_text("Knockout Summary")
        assert "No results found" not in self.driver.page_source

    def test_lexicondetail_links(self):
        self.driver.find_element_by_link_text("Lexicon Detail for Gpr55")
        assert "No results found" not in self.driver.page_source

    def test_deltagendetail_links(self):
        self.driver.find_element_by_link_text("Deltagen Detail for Scn11a")
        assert "No results found" not in self.driver.page_source

    def test_deltagenmbdetail_links(self):
        self.driver.find_element_by_link_text("Deltagen Molecular Biology Detail for Scn11a")
        assert "No results found" not in self.driver.page_source

    def test_deltagenprotocols_links(self):
        self.driver.find_element_by_link_text("Deltagen Protocols")
        assert "No results found" not in self.driver.page_source

    def test_aboutdeltagen_links(self):
        self.driver.find_element_by_link_text("About the Deltagen Download")
        assert "No results found" not in self.driver.page_source

    def test_Festing_links(self):
        self.driver.find_element_by_link_text("Festing Menu Page")
        assert "No results found" not in self.driver.page_source
        
#Quick Search
    def test_quicksearch_links(self):  # returns all buckets
        self.driver.find_element_by_link_text("Search for curly whiskers")
        assert "No results found" not in self.driver.page_source

    def test_quicksearch100mrk_links(self):  # returns the first 100 results for the marker/allele bucket
        self.driver.find_element_by_link_text("first 100 results for curly whiskers")
        assert "No results found" not in self.driver.page_source

    def test_quicksearch100voc_links(self):  # returns the first 100 results for the vocabulary bucket
        self.driver.find_element_by_link_text("first 100 results for tail")
        assert "No results found" not in self.driver.page_source

    def test_quicksearchallmatches_links(self):  # all matches for a marker/allele
        self.driver.find_element_by_partial_link_text("Eny2")
        assert "No results found" not in self.driver.page_source
        
#MGI home
    def test_mgistats_links(self):
        self.driver.find_element_by_link_text("MGI Stats page")
        assert "No results found" not in self.driver.page_source

    def test_inputwelcomepage_links(self):  # Displays the Your Input Welcome form for Pax6
        self.driver.find_element_by_link_text("Your Input Welcome for Pax6")
        assert "No results found" not in self.driver.page_source

    def test_allsearchtoolpage_links(self):
        self.driver.find_element_by_link_text("All Search Tools")
        assert "No results found" not in self.driver.page_source

    def test_moreresourcespage_links(self):
        self.driver.find_element_by_link_text("More Resources")
        assert "No results found" not in self.driver.page_source

    def test_analysistoolspage_links(self):
        self.driver.find_element_by_link_text("Analysis Tools")
        assert "No results found" not in self.driver.page_source

    def test_softwaredevelopertoolspage_links(self):
        self.driver.find_element_by_link_text("Software Developer Tools")
        assert "No results found" not in self.driver.page_source

    def test_submitdatapage_links(self):
        self.driver.find_element_by_link_text("Submit Data")
        assert "No results found" not in self.driver.page_source
        
#SeqFetch
    def test_fasta_links(self):  # tests a FASTA sequence gets returned
        self.driver.find_element_by_link_text("OTTMUST00000035645")
        assert "No results found" not in self.driver.page_source


    def tearDown(self):
        self.driver.close()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMarkerDetailLinks))
    return suite



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()