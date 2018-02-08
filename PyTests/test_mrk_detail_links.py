'''
Created on Dec 12, 2016
This test verifies all public links found on the wiki page mgiwiki/mediawiki/index.php/sw:WI_Pages_by_Software_Product.
It does not test what is found for data on each page.
@author: jeffc
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
        self.driver.find_element(By.LINK_TEXT, 'Pax*')
        assert "No results found" not in self.driver.page_source
        assert "pax*" in self.driver.page_source
        
    def test_snorna_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'snoRNA')
        assert "No results found" not in self.driver.page_source
        assert "snoRNA gene" in self.driver.page_source
       
    def test_jnumber_links(self):
        self.driver.find_element(By.LINK_TEXT, 'J:69860')
        assert "No results found" not in self.driver.page_source
        assert "J:69860" in self.driver.page_source

    def test_bmp3_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Bmp3')
        assert "No results found" not in self.driver.page_source
        assert "Bmp3" in self.driver.page_source
        
    def test_batch_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Empty')
        assert "No results found" not in self.driver.page_source
        
    def test_microarray_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Trp53')
        assert "No results found" not in self.driver.page_source

    def test_intexplorer_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Bmp4')
        assert "No results found" not in self.driver.page_source

    def test_mappingsummrker_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Sry')
        assert "No results found" not in self.driver.page_source

    def test_mappingsumref_links(self):
        self.driver.find_element(By.LINK_TEXT, 'J:2945')
        assert "No results found" not in self.driver.page_source

    def test_mapdetailcross_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Cross')
        assert "No results found" not in self.driver.page_source

    def test_mapdetailri_links(self):
        self.driver.find_element(By.LINK_TEXT, 'RI')
        assert "No results found" not in self.driver.page_source

    def test_mapdetailtext_links(self):
        self.driver.find_element(By.LINK_TEXT, 'TEXT')
        assert "No results found" not in self.driver.page_source

    def test_mapdetailtextgenetic_links(self):
        self.driver.find_element(By.LINK_TEXT, 'TEXT-Genetic Cross')
        assert "No results found" not in self.driver.page_source
        
#GO                
    def test_goannotmrk_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Pax6')
        assert "No results found" not in self.driver.page_source

    def test_goannotref_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'J:114843')
        assert "No results found" not in self.driver.page_source

    def test_goannotsum1_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'motility')
        assert "No results found" not in self.driver.page_source

    def test_goannotsum2_links(self):
        self.driver.find_element(By.LINK_TEXT, 'digestion')
        assert "No results found" not in self.driver.page_source

    def test_markergograph_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Graph for Kit')
        assert "No results found" not in self.driver.page_source

    def test_gobrowser_link(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Gene Ontology Browser')
        assert "No results found" not in self.driver.page_source

    def test_gotermdetail_links(self):
        self.driver.find_element(By.LINK_TEXT, 'gastric motility')
        assert "No results found" not in self.driver.page_source

#Phenotypes Alleles & Disease Models
    def test_alleleqf_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Allele Query')
        assert "No results found" not in self.driver.page_source 

    def test_allelesum_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Albino')
        assert "No results found" not in self.driver.page_source
    
    def test_allelesummrk_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Atp7a')
        assert "No results found" not in self.driver.page_source

    def test_alleleannotdisease_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'annotated to diseases')
        assert "No results found" not in self.driver.page_source

    def test_allelesumref_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'J:24766')
        assert "No results found" not in self.driver.page_source

    def test_alleledetail_links(self):
        self.driver.find_element(By.LINK_TEXT, 'agouti yellow')
        assert "No results found" not in self.driver.page_source

    def test_phenoimagedetail1_links(self):
        self.driver.find_element(By.LINK_TEXT, 'image for agouti yellow')
        assert "No results found" not in self.driver.page_source

    def test_videoexample_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'CvDC')
        assert "No results found" not in self.driver.page_source

    def test_phenoimagemrk1_links(self):
        self.driver.find_element(By.LINK_TEXT, 'a')
        assert "No results found" not in self.driver.page_source
            
    def test_phenoimagemrk2_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Dnaic1')
        assert "No results found" not in self.driver.page_source
        
    def test_phenoimagedetail2_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Pheno Image agouti yellow')
        assert "No results found" not in self.driver.page_source

    def test_phenoimageallele_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Pheno Image Dnaic1 allele (CvDC example)')
        assert "No results found" not in self.driver.page_source
        
    def test_phenodetailgeno1_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'pop-up for ht2')
        assert "No results found" not in self.driver.page_source

    def test_phenodetailgeno2_links(self):
        self.driver.find_element(By.LINK_TEXT, 'pop-up for Pax6-Sey-Neu')
        assert "No results found" not in self.driver.page_source

    def test_mutation_links(self):
        self.driver.find_element(By.LINK_TEXT, 'for Del(2Hoxd11-Hoxd13)29Ddu')
        assert "No results found" not in self.driver.page_source

    def test_diseasebrowser_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Browse for P')
        assert "No results found" not in self.driver.page_source
 
    def test_diseasedetail1_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Diabetes mellitus')
        assert "No results found" not in self.driver.page_source

    def test_diseasedetail2_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Pancreatic Cancer')
        assert "No results found" not in self.driver.page_source

    def test_allmodels_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'All models')
        assert "No results found" not in self.driver.page_source

    def test_mpannotterm_links(self):
        self.driver.find_element(By.LINK_TEXT, 'MP:0002098')
        assert "No results found" not in self.driver.page_source

    def test_mpannottermmrk_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'hormone level')
        assert "No results found" not in self.driver.page_source

    def test_mpbrowser_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Mammalian Phenotype Browser')
        assert "No results found" not in self.driver.page_source

    def test_mptermdetail_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Absent coat pigmentation')
        assert "No results found" not in self.driver.page_source

    def test_hpbrowser_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Human Phenotype Ontology Browser')
        assert "No results found" not in self.driver.page_source

    def test_hpotermdetail_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Gowers sign')
        assert "No results found" not in self.driver.page_source
        
#Human Mouse Disease Connection (Disease Portal)
    def test_diseaseqf_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Disease Connection')
        assert "No results found" not in self.driver.page_source

    def test_gridtab_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'hearing loss')
        assert "No results found" not in self.driver.page_source

    def test_grid1_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Cdh23')
        assert "No results found" not in self.driver.page_source

    def test_grid2_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Atp2b2')
        assert "No results found" not in self.driver.page_source

    def test_genocluster1_links(self):
        self.driver.find_element(By.LINK_TEXT, 'one genotype')
        assert "No results found" not in self.driver.page_source

    def test_genocluster2_links(self):
        self.driver.find_element(By.LINK_TEXT, 'multiple genotypes')
        assert "No results found" not in self.driver.page_source

    def test_genestab_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'gene tab')
        assert "No results found" not in self.driver.page_source

    def test_diseasetab_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'disease tab')
        assert "No results found" not in self.driver.page_source
        
#References
    def test_refqf_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Ref QF')
        assert "No results found" not in self.driver.page_source

    def test_refsum_links(self):
        self.driver.find_element(By.LINK_TEXT, '2008')
        assert "No results found" not in self.driver.page_source

    def test_refsummrk_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Tyr')
        assert "No results found" not in self.driver.page_source

    def test_refsumallele_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Myf5')
        assert "No results found" not in self.driver.page_source

    def test_refsum1_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Acan')
        assert "No results found" not in self.driver.page_source

    def test_refsum2_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Acondroplasia')
        assert "No results found" not in self.driver.page_source

    def test_refdetail1ref_links(self):
        self.driver.find_element(By.LINK_TEXT, 'J:181372')
        assert "No results found" not in self.driver.page_source
        
#Recombinase
    #def test_creqf_links(self):
    #    self.driver.find_element(By.LINK_TEXT, 'Minihome')
    #    assert "No results found" not in self.driver.page_source

    def test_cresummary_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Muscle')
        assert "No results found" not in self.driver.page_source

    def test_cresummary1_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Calb2')
        assert "No results found" not in self.driver.page_source
        
    def test_crespecificity_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Foxg1')
        assert "No results found" not in self.driver.page_source

    def test_crespecificitynotdetected_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Not detected')
        assert "No results found" not in self.driver.page_source
        
#Gene Expression
    def test_gxdqf_links(self):
        self.driver.find_element(By.LINK_TEXT, 'GXD Query Form')
        assert "No results found" not in self.driver.page_source

    def test_gxdsummrk_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Expression for Kit')
        assert "No results found" not in self.driver.page_source

    def test_gxdsumref_links(self):
        self.driver.find_element(By.LINK_TEXT, 'for J:61153')
        assert "No results found" not in self.driver.page_source

    def test_gxdsumprobe_links(self):
        self.driver.find_element(By.LINK_TEXT, 'cdh6')
        assert "No results found" not in self.driver.page_source
 
    def test_gxdsumemap_links(self):
        self.driver.find_element(By.LINK_TEXT, 'common atrial chamber')
        assert "No results found" not in self.driver.page_source
 
    def test_gxddetailinsitu_links(self):
        self.driver.find_element(By.LINK_TEXT, 'RNA in situ')
        assert "No results found" not in self.driver.page_source

    def test_gxddetailblot_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Northern Blot')
        assert "No results found" not in self.driver.page_source

    def test_gxdimagedetail_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Image for Lep')
        assert "No results found" not in self.driver.page_source

    def test_gxdlitsummary_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Lit Sum for Brca1')
        assert "No results found" not in self.driver.page_source

    def test_gxdlitsumage_links(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'RNA/10.5')
        assert "No results found" not in self.driver.page_source

    def test_gxdlitdetail_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Bard1/J:91257')
        assert "No results found" not in self.driver.page_source

    def test_gxdlitsummrker_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Trp53')
        assert "No results found" not in self.driver.page_source

    def test_gxdlitsumref_links(self):
        self.driver.find_element(By.LINK_TEXT, 'J:148991')
        assert "No results found" not in self.driver.page_source

    def test_gxdtissuemrker_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Shh')
        assert "No results found" not in self.driver.page_source

    def test_gxdemapa_links(self):
        self.driver.find_element(By.LINK_TEXT, 'mouse')
        assert "No results found" not in self.driver.page_source

    def test_gxdantibodydetail_links(self):
        self.driver.find_element(By.LINK_TEXT, 'MGI:2137372')
        assert "No results found" not in self.driver.page_source

    def test_prbsummrker_links(self):
        self.driver.find_element(By.LINK_TEXT, 'probes Oxt')
        assert "No results found" not in self.driver.page_source

    def test_prbsumref_links(self):
        self.driver.find_element(By.LINK_TEXT, 'J:2945')
        assert "No results found" not in self.driver.page_source

    def test_prbdetail_links(self):
        self.driver.find_element(By.LINK_TEXT, 'MGI:901759')
        assert "No results found" not in self.driver.page_source

    def test_cdnasummrker_links(self):
        self.driver.find_element(By.LINK_TEXT, 'cDNA Oxt')
        assert "No results found" not in self.driver.page_source

    def test_amabrowserresults_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Adult Mouse Anatomy Browser')
        assert "No results found" not in self.driver.page_source

    def test_amatermdetail_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Forebrain')
        assert "No results found" not in self.driver.page_source
        
#Homology
    def test_verthomology_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Homology Class 36030')
        assert "No results found" not in self.driver.page_source

    def test_gograph_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Graph for 36030')
        assert "No results found" not in self.driver.page_source

    def test_pirsf_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Paired box Protein Superfamily')
        assert "No results found" not in self.driver.page_source
        
#Sequences
    def test_seqsum_links(self):
        self.driver.find_element(By.LINK_TEXT, 'T')
        assert "No results found" not in self.driver.page_source

    def test_seqsumref_links(self):
        self.driver.find_element(By.LINK_TEXT, 'J:90438')
        assert "No results found" not in self.driver.page_source

    def test_seqsummrkerprovider_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Grid2/Refseq')
        assert "No results found" not in self.driver.page_source

    def test_seqsummrkerprovider2_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Grid2/Uniprot')
        assert "No results found" not in self.driver.page_source

    def test_seqdetailuniprot_links(self):
        self.driver.find_element(By.LINK_TEXT, 'UniProt sequence')
        assert "No results found" not in self.driver.page_source

    def test_seqdetailrefseq_links(self):
        self.driver.find_element(By.LINK_TEXT, 'RefSeq sequence')
        assert "No results found" not in self.driver.page_source
        
#SNPs & Polymorphisms
    def test_snpqf_links(self):
        self.driver.find_element(By.LINK_TEXT, 'SNP Query Form')
        assert "No results found" not in self.driver.page_source

    def test_snpdetail_links(self):
        self.driver.find_element(By.LINK_TEXT, 'rs51119329')
        assert "No results found" not in self.driver.page_source

    def test_snpsummary_links(self):
        self.driver.find_element(By.LINK_TEXT, 'query by Fmr1')
        assert "No results found" not in self.driver.page_source

    def test_snpsummarymarker_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Fmr1')
        assert "No results found" not in self.driver.page_source

    def test_polymorphsummrker_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Summary for Trp53')
        assert "No results found" not in self.driver.page_source

    def test_polymorphdetail_links(self):
        self.driver.find_element(By.LINK_TEXT, 'RFLP Summary for Trp53')
        assert "No results found" not in self.driver.page_source
        
#Miscellaneous    
    def test_accreport1_links(self):
        self.driver.find_element(By.LINK_TEXT, 'ID=36030')
        assert "No results found" not in self.driver.page_source

    def test_accreport2_links(self):
        self.driver.find_element(By.LINK_TEXT, 'ID=Ren1')
        assert "No results found" not in self.driver.page_source

    def test_glossaryindex_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Glossary Index')
        assert "No results found" not in self.driver.page_source

    def test_glossaryterm_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Boolean')
        assert "No results found" not in self.driver.page_source

#Python WI
    def test_knockoutsum_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Knockout Summary')
        assert "No results found" not in self.driver.page_source

    def test_lexicondetail_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Lexicon Detail for Gpr55')
        assert "No results found" not in self.driver.page_source

    def test_deltagendetail_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Deltagen Detail for Scn11a')
        assert "No results found" not in self.driver.page_source

    def test_deltagenmbdetail_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Deltagen Molecular Biology Detail for Scn11a')
        assert "No results found" not in self.driver.page_source

    def test_deltagenprotocols_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Deltagen Protocols')
        assert "No results found" not in self.driver.page_source

    def test_aboutdeltagen_links(self):
        self.driver.find_element(By.LINK_TEXT, 'About the Deltagen Download')
        assert "No results found" not in self.driver.page_source

    def test_Festing_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Festing Menu Page')
        assert "No results found" not in self.driver.page_source
        
#Quick Search
    def test_quicksearch_links(self):  # returns all buckets
        self.driver.find_element(By.LINK_TEXT, 'Search for curly whiskers')
        assert "No results found" not in self.driver.page_source

    def test_quicksearch100mrk_links(self):  # returns the first 100 results for the marker/allele bucket
        self.driver.find_element(By.LINK_TEXT, 'first 100 results for curly whiskers')
        assert "No results found" not in self.driver.page_source

    def test_quicksearch100voc_links(self):  # returns the first 100 results for the vocabulary bucket
        self.driver.find_element(By.LINK_TEXT, 'first 100 results for tail')
        assert "No results found" not in self.driver.page_source

    def test_quicksearchallmatches_links(self):  # all matches for a marker/allele
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Eny2')
        assert "No results found" not in self.driver.page_source
        
#MGI home
    def test_mgistats_links(self):
        self.driver.find_element(By.LINK_TEXT, 'MGI Stats page')
        assert "No results found" not in self.driver.page_source

    def test_inputwelcomepage_links(self):  # Displays the Your Input Welcome form for Pax6
        self.driver.find_element(By.LINK_TEXT, 'Your Input Welcome for Pax6')
        assert "No results found" not in self.driver.page_source

    def test_allsearchtoolpage_links(self):
        self.driver.find_element(By.LINK_TEXT, 'All Search Tools')
        assert "No results found" not in self.driver.page_source

    def test_moreresourcespage_links(self):
        self.driver.find_element(By.LINK_TEXT, 'More Resources')
        assert "No results found" not in self.driver.page_source

    def test_analysistoolspage_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Analysis Tools')
        assert "No results found" not in self.driver.page_source

    def test_softwaredevelopertoolspage_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Software Developer Tools')
        assert "No results found" not in self.driver.page_source

    def test_submitdatapage_links(self):
        self.driver.find_element(By.LINK_TEXT, 'Submit Data')
        assert "No results found" not in self.driver.page_source
        
#SeqFetch
    def test_fasta_links(self):  # tests a FASTA sequence gets returned
        self.driver.find_element(By.LINK_TEXT, 'OTTMUST00000035645')
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