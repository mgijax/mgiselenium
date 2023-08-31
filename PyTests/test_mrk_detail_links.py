'''
Created on Dec 12, 2016
This test verifies all public links found on the wiki page mgiwiki/mediawiki/index.php/sw:WI_Pages_by_Software_Product.
It does not test what is found for data on each page.
@author: jeffc
Verifies the follwing:
search for Pax*
Search for snoRNA
Search for J:69860
Search for Bmp3
Search for Empty string
Search for Trp53 (microarray link)
Search for Bmp4 (intexplorer link)
Search for Sry (mapping summary marker link)
Search for J:2945 (mapping summary reference link)
Search for Cross (mapping detail cross link)
Search for RI (mapping detail RI link)
Search for TEXT (mapping detail TEXT link)
Search for TEXT-Genetic Cross (mapping detail TEXT genetic cross)
Search for Pax6 (GO annotation marker link)
Search for J:114843 (GO annotation reference link)
Search for motility (GO annotation summary link 1)
Search for digestion (GO annotation summary link 2)
Search for Graph for Kit (GO graph link)
Search for Gene Ontology Browser (GO browser link)
Search for gastric motility (GO term detail link)
Search for Allele Query (allele query form link)
Search for Albino (allele summary link)
Search for Atp7a (allele summary marker link)
Search for annotated to diseases (allele annotation disease link)
Search for J:24766 (allele summary reference link)
Search for agouti yellow (allele detail link)
Search for image for agouti yellow (allele phenotype image detail link)
Search for CvDC (video example link)
Search for a (phenotype image marker link)
Search for Dnaic1 (a second phenotype image marker link)
Search for Pheno Image agouti yellow (phenotypic image detail link)
Search for Pheno Image Dnaic1 allele (CvDC example) (allele phenotype image detail link)
Search for pop-up for ht2 (phenotype allele genotype link)
Search for pop-up for Pax6-Sey-Neu (second phenotype allele genotype link)
Search for for Del(2Hoxd11-Hoxd13)29Ddu (mutation link)
Search for Browse for P (disease browser link)
Search for Diabetes mellitus (disease detail link)
Search for Pancreatic Cancer (second disease detail link)
Search for All models (all models link)
Search for MP:0002098 (MP annotation term link)
Search for hormone level (MP annotation marker term link)
Search for Mammalian Phenotype Browser (MP browser link)
Search for Absent coat pigmentation (MP annotation term link)
Search for Human Phenotype Ontology Browser (HP browser link)
Search for Gowers sign (HP term detail link)
Search for Disease Connection (disease query form link)
Search for hearing loss (Grid tab link)
Search for Cdh23 (Grid link)
Search for Atp2b2 (second Grid link)
Search for one genotype (genocluster link)
Search for multiple genotypes (second genocluster link)
Search for gene tab (gene tab link)
Search for disease tab (disease tab link)
Search for Ref QF (Reference query form link)
Search for 2008 (Reference summary link)
Search for Tyr (Reference summary marker link)
Search for Myf5 (Reference summary allele link)
Search for Acan (Reference summary link)
Search for Acondroplasia (second Reference summary link)
Search for J:181372 (Reference detail link)
Search for Muscle (CRE summary link)
Search for Calb2 (second CRE summary link)
Search for Foxg1 (CRE specificity link)
Search for Not detected (CRE specificity not detected link)
Search for GXD Query Form (GXD query form link)
Search for Expression for Kit (GXD summary marker link)
Search for for J:61153 (GXD summary reference link)
Search for cdh6 (GXD summary probe link)
Search for common atrial chamber (GXD summary map link)
Search for RNA in situ (GXD detail insitu link)
Search for Northern Blot (GXD detail blot link)
Search for Image for Lep (GXD image detail link)
Search for Lit Sum for Brca1 (GXD Lit Summary link)
Search for RNA/10.5 (GXD Lit summary link)
Search for Bard1/J:91257 (GXD Lit detail link)
Search for Trp53 (GXD Lit Summary by marker link)
Search for J:148991 (GXD Lit summary by reference link)
Search for Shh (GXD tissue by marker link)
Search for mouse (GXD emapa link)
Search for MGI:2137372 (GXD antibody detail link)
Search for probes Oxt (probe summary by marker link)
Search for J:2945 (probe summary by reference link)
Search for MGI:901759 (probe detail link)
Search for cDNA Oxt (cDNA summary by marker link)
Search for Adult Mouse Anatomy Browser (adult mouse anatomy browser link)
Search for Forebrain (adult mouse term detail link)
Search for Homology Class 36030 (homology link)
Search for Graph for 36030 (GO graph link)
Search for Paired box Protein Superfamily (PIRSF link)
Search for T (sequence summary link)
Search for J:90438 (sequence summary by reference link)
Search for Grid2/Refseq (sequence summary by marker provider link)
Search for Grid2/Uniprot (sequence summary by marker provider link)
Search for UniProt sequence (sequence detail uniprot link)
Search for RefSeq sequence (sequence detail refseq link)
Search for SNP Query Form (SNP query form link)
Search for rs51119329 (SNP detail link)
Search for query by Fmr1 (SNP summary link)
Search for Fmr1 (SNP summary by marker link)
Search for Summary for Trp53 (polymorphism by marker link)
Search for RFLP Summary for Trp53 (polymorphism detail link)
Search for ID=36030 (ACC report link)
Search for ID=Ren1 (ACC report link)
Search for Glossary Index (Glossary index link)
Search for Boolean (Glossary term link)
Search for Knockout Summary (Knockout summary link)
Search for Lexicon Detail for Gpr55 (Lexicon detail link)
Search for Deltagen Detail for Scn11a (Deltagen detail link)
Search for Deltagen Molecular Biology Detail for Scn11a (Deltgen MB detail link)
Search for Deltagen Protocols (Deltagen protocol detail link)
Search for About the Deltagen Download (About Deltagen link)
Search for Festing Menu Page (Festing link)
Search for Search for curly whiskers (Quick Search link)
Search for first 100 results for curly whiskers (Quick search first 100 for marker link)
Search for first 100 results for tail (Quick search first 100 for vocabulary link)
Search for Eny2 (Quick search all matches link)
Search for MGI Stats page (MGI stats link)
Search for Your Input Welcome for Pax6 (Your input welcome link)
Search for All Search Tools (All search tool link)
Search for More Resources (More resources link)
Search for Analysis Tools (Analysis tools link)
Search for Software Developer Tools (Software developer tools link)
Search for Submit Data (Submit Data link)
Search for OTTMUST00000035645 (FASTA link)
'''
import unittest
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config

#Tests
tracemalloc.start()
class TestMarkerDetailLinks(unittest.TestCase):

#Genes, Genome Features & Maps
    def setUp(self):
        self.driver = webdriver.Firefox() 
        #self.driver = webdriver.Chrome() 
        #self.driver.get(config.WIKI_URL + "sw:WI_Pages_by_Software_Product")
        self.driver.get(config.WIKI_URL + "sw:WI_Pages_by_Software_Product_test")

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
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMarkerDetailLinks))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
        