"""
Created on Oct 20, 2016
@author: jeffc
This suite of tests are for marker detail pages
Verify the ribbons are being displayed in the correct order on the page
Verify that the APF link for incidential mutations goes to the correct website location
Verify the link for Transcription exits(and is correctly worded) in the summary ribbon and clicking it displays the popup table
    @note the sites should be displayed by coordinate order
Verify this test opens the Tss table and verifies the table results are sorted by location coordinates
    @note the sites should be displayed by coordinate order on marker detail but by Distance from Gene 6'-end in Tss table
Verify clicking a Tss site ID takes you to it's detail page
Verify the strain table headings in the Genome Context & Strain Distribution ribbon are correctly ordered/displayed
Verify the strain table(no strain ribbon) is not present in the Strain Comparison ribbon when strains have no annotation
Verify the Strain Comparison ribbon when the turnstile is closed shows strain annotations and SNPs within 2kb(if available)
Verify the Strain Comparison ribbon does not display when no Annotation Data or SNP Data exists
Verify the Multiple Genome Viewer(MGV) link exists only when B6 coordinates exist
Verify that the Gene Model IDs in the strains table link to their MGI gene model sequence, found in the Strain Comparison ribbon. (only verifying 1 link of 18)
Verify that when a canonical gene doesn't have a B6 strain gene then the strain table for C57BL/6J says "no annotation"
Verify that the sequence map coordinates do not match the strains table C57BL/6J coordinates when the gene model is not MGI
Verify that the sequence map coordinates match the strains table C57BL/6J coordinates when the gene model is MGI
Verify that you can download a single FASTA sequence from the Strain table using the download checkbox
Verify that you can download multiple FASTA sequences from the Strain table using the download checkboxs
Verify that you can download a B6 strain gene FASTA sequence from the Strain table using the download checkbox
Verify that you can download all FASTA sequences from the Strain table using the 'Check All' button
Verify that a strain-specific marker is correctly identified in the Strain Comparison ribbon
Verify that only the SNPs within 2kb, PCR,and RFLP links exists in the Strain Comparison ribbon when no strain available
Verify that only polymorphism data exists in the Strain Comparison ribbon when no strain or coordinates available
Verify that when you click the Select DO/CC Founders button in the Strain Comparison ribbon the correct strains get selected in the strains table
Verify that when a gene has multiple gene model IDs to the same strain the strain table displays them correctly
Verify In the Human Diseases section, confirm there are turnstile icons for showing more data
    and clicking the turnstile icon displays the complete Human Diseases table
Verify that the disease table in the Human Diseases ribbon now displays the DOID beside
    each disease instead of the OMIM ID
Verify In the Human Diseases section, from the Mouse Model popup strains in Genetic background link to their strain
    detail page
Verify when you click the Phenotype summary link(for genetic backgrounds) from the Mutations, Alleles, and Phenotypes ribbon
    to open the MP ontology annotations page you find strains in the genetic background column link to their strain detail page
Verify when you click the Phenotype summary link(for multigenic genotypes) from the Mutations, Alleles, and Phenotypes ribbon
    to open the MP ontology annotations page you find strains in the genetic background column link to their strain detail page
Verify when you click one of the blue cells in the phenoslim grid from the Mutations, Alleles, and Phenotypes ribbon
    to open the Phenotype annotations related to page, then click a Mouse Genotype to find strains in the genetic background column
    link to their strain detail page(for Summary ribbon and for Genotype ribbon
Verify the existence of a QTL interaction link in the summary section below the Feature Type. Clicking the link displays a popup table
Verify the existence of a Candidate Genes link in the summary section below the Feature Type(on QTL detail). Clicking the link displays a popup table
Verify the existence of a Candidate for QTL link in the summary section below the Feature Type(on Marker detail). Clicking the link displays a popup table
Verify the Glygen link in the Protein Information section.
"""
import os.path
import sys
import time
import tracemalloc
import unittest
import config

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from genericpath import exists
from util import iterate, wait
from util.table import Table

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)

# Test
tracemalloc.start()


class TestMarkerDetail(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/marker/")
        self.driver.implicitly_wait(10)

    def test_ribbon_locations(self):
        """
        @status This test verifies the ribbons are being displayed in the correct order on the page.
        tested 4/9/2021
        """
        self.driver.find_element(By.NAME, 'nomen').send_keys("Gata1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Gata1').click()
        time.sleep(2)
        summaryribbon = self.driver.find_element(By.CSS_SELECTOR, '#summaryRibbon > div:nth-child(1)')
        print(summaryribbon.text)
        self.assertEqual(summaryribbon.text, 'Summary', "Summary ribbon is missing")
        locationribbon = self.driver.find_element(By.CSS_SELECTOR, '#locationRibbon > div:nth-child(1)')
        print(locationribbon.text)
        self.assertEqual(locationribbon.text, "Location &\nMaps", "Location & Maps ribbon is missing")
        strainribbon = self.driver.find_element(By.CSS_SELECTOR, '#strainRibbon > div:nth-child(1)')
        print(strainribbon.text)
        self.assertEqual(strainribbon.text, "Strain\nComparison", "Strain Comparison ribbon is missing")
        homologyribbon = self.driver.find_element(By.CSS_SELECTOR, '#homologyRibbon > div:nth-child(1)')
        print(homologyribbon.text)
        self.assertEqual(homologyribbon.text, 'Homology', "Homology ribbon is missing")
        diseaseribbon = self.driver.find_element(By.CSS_SELECTOR, '#diseaseRibbon > div:nth-child(1)')
        self.assertEqual(diseaseribbon.text, "Human Diseases", "Human Diseases ribbon is missing")
        phenoribbon = self.driver.find_element(By.CSS_SELECTOR, '#phenotypeRibbon > div:nth-child(1)')
        print(phenoribbon.text)
        self.assertEqual(phenoribbon.text, "Mutations,\nAlleles, and\nPhenotypes", "Phenotype ribbon is missing")
        goribbon = self.driver.find_element(By.CSS_SELECTOR, '#goRibbon > div:nth-child(1)')
        print(goribbon.text)
        self.assertEqual(goribbon.text, "Gene Ontology\n(GO)\nClassifications", "GO ribbon is missing")
        gxdribbon = self.driver.find_element(By.CSS_SELECTOR, '#expressionRibbon > div:nth-child(1)')
        print(gxdribbon.text)
        self.assertEqual(gxdribbon.text, "Expression", "Expression ribbon is missing")
        sequenceribbon = self.driver.find_element(By.CSS_SELECTOR, '#sequenceRibbon > div:nth-child(1)')
        print(sequenceribbon.text)
        self.assertEqual(sequenceribbon.text, "Sequences &\nGene Models", "Sequence ribbon is missing")
        proteinribbon = self.driver.find_element(By.CSS_SELECTOR, '#proteinInfoRibbon > div:nth-child(1)')
        print(proteinribbon.text)
        self.assertEqual(proteinribbon.text, "Protein\nInformation", "Protein Information ribbon is missing")
        molecularribbon = self.driver.find_element(By.CSS_SELECTOR, '#molecularReagentsRibbon > div:nth-child(1)')
        print(molecularribbon.text)
        self.assertEqual(molecularribbon.text, 'Molecular\nReagents', "Molecular Reagents ribbon is missing")
        otheraccribbon = self.driver.find_element(By.CSS_SELECTOR, '#otherMgiIdsRibbon > div:nth-child(1)')
        print(otheraccribbon.text)
        self.assertEqual(otheraccribbon.text, 'Other\nAccession IDs', "Other Accession IDs ribbon is missing")
        referencesribbon = self.driver.find_element(By.CSS_SELECTOR, '#referenceRibbon > div:nth-child(1)')
        print(referencesribbon.text)
        self.assertEqual(referencesribbon.text, 'References', "References ribbon is missing")

    def test_apf_link(self):
        """
        @status this test verifies that the APF link for incidential mutations goes to the correct website location.
        @note test works as of 3/29/18
        """
        self.driver.find_element(By.NAME, 'nomen').send_keys("Alad")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Alad').click()
        apflnk = self.driver.find_element(By.LINK_TEXT, 'APF')
        href = apflnk.find_element(By.XPATH, "//a").get_attribute('href')

        self.assertTrue(href, "https://databases.apf.edu.au/mutations/snpRow/list?mgiAccessionid=MGI:96853")

    def test_tss_display(self):
        """
        @status this test verifies the link for Transcription exits(and is correctly worded) in the summary ribbon and clicking it displays the popup table
        @note the sites should be displayed by coordinate order
        @note mrkdetail-sum-1, 2
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Vwa3b")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Vwa3b').click()
        # Find the Transcription link in the summary ribbon section, verify the link text and click it
        tss_link = self.driver.find_element(By.ID, 'showTss')
        print(tss_link.text)
        self.assertEqual(tss_link.text, '9 TSS', 'The tss link text is not correct!')
        tss_link.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'tssDiv_h')))  # waits until the TSS table popup is displayed on the page
        # find the Tss table popup and verify the table heading
        tss_head = self.driver.find_element(By.ID, 'tssDiv_h')
        print(tss_head.text)
        self.assertEqual(tss_head.text, 'TSS for Vwa3b:', 'The TSS table heading is not correct!')

    def test_tss_table_display_sort(self):
        """
        @status this test opens the Tss table and verifies the table results are sorted by location coordinates
        @note the sites should be displayed by coordinate order on marker detail but by Distance from Gene 6'-end in Tss table
        @note mrkdetail-sum-3
        """
        self.driver.find_element(By.NAME, 'nomen').send_keys("Sgk3")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Sgk3').click()
        # Find the All TSS link and click it
        self.driver.find_element(By.ID, 'showTss').click()
        tss_table = self.driver.find_element(By.ID, 'tssTable')
        table = Table(tss_table)
        # Iterate the table Location column
        cells = table.get_column_cells('Location')
        loc_cells = iterate.getTextAsList(cells)
        # Verify the TSS table locations are correct and in the correct order.
        self.assertEqual(loc_cells[1], 'Chr1:9868020-9868034 (+)')
        self.assertEqual(loc_cells[2], 'Chr1:9868037-9868048 (+)')
        self.assertEqual(loc_cells[3], 'Chr1:9868211-9868265 (+)')
        self.assertEqual(loc_cells[4], 'Chr1:9868348-9868441 (+)')
        self.assertEqual(loc_cells[5], 'Chr1:9869397-9869445 (+)')
        self.assertEqual(loc_cells[6], 'Chr1:9877231-9877239 (+)')
        self.assertEqual(loc_cells[7], 'Chr1:9906273-9906277 (+)')
        # Iterate the table Distance from Gene 5' -end column
        cells = table.get_column_cells("Distance from Gene 5'-end")
        loc_cells = iterate.getTextAsList(cells)
        # Verify the TSS table Distance are correct and in the correct order.
        self.assertEqual(loc_cells[1], '-305 bp')
        self.assertEqual(loc_cells[2], '-289 bp')
        self.assertEqual(loc_cells[3], '-94 bp')
        self.assertEqual(loc_cells[4], '63 bp')
        self.assertEqual(loc_cells[5], '1,089 bp')
        self.assertEqual(loc_cells[6], '8,903 bp')
        self.assertEqual(loc_cells[7], '37,943 bp')

    def test_tss_detail_link(self):
        """
        @status this test verifies clicking a Tss site ID takes you to it's detail page
        @note mrkdetail-sum-4
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Carf")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Carf').click()
        # Find the TSS link and click it
        self.driver.find_element(By.ID, 'showTss').click()
        # locates the TSS table and verify the tss ID is correct
        tss_table = Table(self.driver.find_element(By.ID, "tssTable"))
        cell = tss_table.get_cell(1, 0)
        print(cell.text)
        self.assertEqual(cell.text, 'Tssr6917', 'The TSSR ID is not correct!')
        # find and click the Tssr ID
        self.driver.find_element(By.LINK_TEXT, 'Tssr6917').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'titleBarMainTitle')))  # waits until the page title is displayed on the page
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        # Assert that the page title is for Tssr6917
        self.assertEqual(page_title.text, 'Tssr6917')

    def test_strain_table_headings(self):
        """
        @status this test verifies the strain table headings in the Genome Context & Strain Distribution ribbon are correctly ordered/displayed.
        @note mrkdetail-strain-1
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ren1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ren1').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'summaryRibbon')))  # waits until the summary ribbon is displayed on the page
        # clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR,
                                                                     'div.toggleImage.hdExpand').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'table_strainMarkers')))  # waits until the strain marker table is displayed on the page
        strain_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strain_table)
        # Iterate and print the table headers
        cells = table.get_header_cells()
        header_cells = iterate.getTextAsList(cells)
        # Verify the strain table headers are correct.
        self.assertEqual(header_cells[0], 'Strain')
        self.assertEqual(header_cells[1], 'Gene Model ID')
        self.assertEqual(header_cells[2], 'Feature Type')
        self.assertEqual(header_cells[3], 'Coordinates')
        self.assertEqual(header_cells[4], 'Select Strains')

    def test_strain_no_annot(self):
        """
        @status this test verifies the strain table(no strain ribbon) is not present in the Strain Comparison ribbon when strains have no annotation.
        @note mrkdetail-strain-2
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Arp")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Arp').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'summaryRibbon')))  # waits until the summary ribbon is displayed on the page

        # asserts that the strains ribbon is not displayed on the page
        assert "table_strainRibbon" not in self.driver.page_source

    def test_strain_turnstile_closed(self):
        """
        @status this test verifies the Strain Comparison ribbon when the turnstile is closed shows strain annotations and SNPs within 2kb(if available).
        @note mrkdetail-strain-3
        """
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ren1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ren1').click()
        # locate the number of strain annotations
        strain_annot = self.driver.find_element(By.ID, 'annotatedStrainMarkerCount')
        # verify the strain annotations number is correct
        self.assertEqual(strain_annot.text, '16')
        # verify the SNP URL
        snp_s = self.driver.find_element(By.ID, 'snpLink')
        self.assertEquals(snp_s.text, '295')

    def test_strain_turnstile_nostrain_snp_data(self):
        """
        @status this test verifies the Strain Comparison ribbon does not display when no Annotation Data or SNP Data exists.
        @note mrkdetail-strain-4
        """
        self.driver.find_element(By.NAME, 'nomen').send_keys("Arp")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Arp').click()
        # verify the strain annotations number is not displayed
        assert "annotatedStrainMarkerCount" not in self.driver.page_source
        # Assert the SNPs within 2kb link is not displayed
        assert "snpLink" not in self.driver.page_source

    def test_mgv_link_not_exists(self):
        """
        @status this test verifies the Multiple Genome Viewer(MGV) link exists only when B6 coordinates exist.
        @note mrkdetail-strain-5
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ren2")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ren2').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'summaryRibbon')))  # waits until the summary ribbon is displayed on the page
        # verify the there is no strain table in the Strain Comparison ribbon
        assert "id='table_strainMarkers'" not in self.driver.page_source

    """def test_mgv_link_10kb_flank(self):\n'
     '                \n'
     '        @status this test verifies the Multiple Genome Viewer(MGV) has 10kb flanking on each end of the sequence link URL.\n'
     '        @note mrkdetail-strain-6 *this is no longer a requirement?\n'
     '              \n'
     '        driver = self.driver \n'
     '        self.driver.find_element(By.NAME, \'nomen\').clear()\n'
     '        self.driver.find_element(By.NAME, \'nomen\').send_keys("Ren1")\n'
     '        self.driver.find_element(By.CLASS_NAME, \'buttonLabel\').click()\n'
     '        self.driver.find_element(By.LINK_TEXT, \'Ren1\').click()\n'
     '        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, \'summaryRibbon\')))#waits until the summary ribbon is displayed on the page\n'
     '        #clicks the More toggle(turnstile) to display the strain distribution data\n'
     '        self.driver.find_element(By.ID, \'strainRibbon\').find_element(By.CSS_SELECTOR, \'div.toggleImage.hdExpand\').click()\n'
     '        #find the "Get FASTA" option in the pulldown list located above the strain table and select it\n'
     '        Select (self.driver.find_element(By.NAME, \'strainOp\')).select_by_visible_text(\'Get FASTA\')\n'
     '        time.sleep(2)\n'
     '        #find and click the \'Go\' button\n'
     '        self.driver.find_elements(By.CLASS_NAME, \'sgButton\')[0].click()\n'
     '        #time.sleep(2)\n'
     '        #switch focus to the new tab for the FASTA results\n'
     '        self.driver.switch_to.window(self.driver.window_handles[-1])\n'
     '        #time.sleep(2)\n'
     '        #verify the correct sequence is being returned\n'
     '        assert \'MGI_C57BL6J_95661 X:7959260-7978071\' in self.driver.page_source     \n'
     '        \n'
     '        #time.sleep(2)\n'
     '        #locates all MGV link on the page\n'
     '        mgv_link = self.driver.find_element(By.LINK_TEXT, \'Multiple Genome Viewer (MGV)\')    \n'
     '        print(mgv_link.get_attribute(\'href\'))\n'
     '        #verify the MGV link href is correct(the 10KB flanking added is in the url)\n'
     '        self.assertEqual(mgv_link.get_attribute(\'href\'), \'http://proto.informatics.jax.org/prototypes/mgv/#ref=C57BL/6J&genomes=C57BL/6J+129S1/SvImJ+A/J+AKR/J+BALB/cJ+C3H/HeJ+C57BL/6NJ+CAROLI/EIJ+CAST/EiJ+CBA/J+DBA/2J+FVB/NJ+LP/J+NOD/ShiLtJ+NZO/HlLtJ+PAHARI/EIJ+PWK/PhJ+SPRET/EiJ+WSB/EiJ&chr=1&start=133300674&end=133410320&highlight=MGI:97898\', \'The MGV link href flanking is incorrect!\')\n')
"""
    def test_strain_table_genemodelid_links(self):
        """
        @status this test verifies that the Gene Model IDs in the strains table link to their MGI gene model sequence, found in the Strain Comparison ribbon. (only verifying 1 link of 18)
        @bug: broken, can't find row data.
        @note mrkdetail-strain-9
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Gata1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Gata1').click()
        # Store the ID of the original window
        original_window = self.driver.current_window_handle
        # Check we don't have other windows open already
        assert len(self.driver.window_handles) == 1
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'summaryRibbon')))  # waits until the summary ribbon is displayed on the page
        # clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR,
                                                                     ' div.toggleImage.hdExpand').click()
        # find the link for C57BL/6J gene model id
        self.driver.find_element(By.LINK_TEXT, 'MGI_C57BL6J_95661').click()
        # switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        structure_table = self.driver.find_element(By.CLASS_NAME, 'detailStructureTable')
        table = Table(structure_table)
        # Iterate the second row of the disease table
        all_cells = table.get_row('ID/Version')
        print(all_cells.text)
        # verify the ID/Version row of data
        self.assertEqual(all_cells.text,
                         'ID/Version\nMGI_C57BL6J_95661 Multiple Genome Viewer (MGV) Version: MGI_C57BL6J_95661.GRCm39')
        # switch focus back to the Gene Detail page
        driver.switch_to.window(original_window)
        # find the link for 129S1/SvImJ gene model id
        self.driver.find_element(By.LINK_TEXT, 'MGP_129S1SvImJ_G0035536').click()
        # switch focus to the new tab for sequence detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        structure_table = self.driver.find_element(By.CLASS_NAME, 'detailStructureTable')
        table = Table(structure_table)
        # Iterate the second row of the disease table
        all_cells = table.get_row('ID/Version')
        print(all_cells.text)
        # verify the ID/Version row of data
        self.assertEqual(all_cells.text,
                         'ID/Version\nMGP_129S1SvImJ_G0035536 (Ensembl) Multiple Genome Viewer (MGV) Version: MGP_129S1SvImJ_G0035536.Ensembl Release 92')

    def test_strain_table_vs_seqmap_noB6(self):
        """
        @status this test verifies that when a canonical gene doesn't have a B6 strain gene then the strain table for C57BL/6J says "no annotation"
        @note mrkdetail-strain-10
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("n-R5s85")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'n-R5s85').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'summaryRibbon')))  # waits until the summary ribbon is displayed on the page
        # locate the Sequence Map coordinates
        seq_map = self.driver.find_element(By.XPATH,
                                           '//*[@id="templateBodyInsert"]/div[2]/div[2]/div[2]/section[1]/ul/li[1]/div[2]')
        print(seq_map.text)
        # verify the coordinates data for the sequence map
        self.assertEqual(seq_map.text, 'Genome coordinates not available from the current reference assembly.',
                         'sequence map coordinates have changed!')
        # clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR,
                                                                     'div.toggleImage.hdExpand').click()
        # find the Gene Model ID column of the strains table
        strains_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strains_table)
        # Iterate the second row of the disease table
        all_cells = table.get_column_cells('Gene Model ID')
        print(all_cells[1].text)
        # verify the ID/Version row of data
        self.assertEqual(all_cells[1].text, 'no annotation')

    def test_strain_table_vs_seqmap_nomatch(self):
        """
        @status this test verifies that the sequence map coordinates do not match the strains table C57BL/6J coordinates when the gene model is not MGI
        @note mrkdetail-strain-11 *this test will go away when we stop using the reference B6 models
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pax6').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'summaryRibbon')))  # waits until the summary ribbon is displayed on the page
        # locate the Sequence Map coordinates
        seq_map = self.driver.find_element(By.XPATH,
                                           '//*[@id="templateBodyInsert"]/div[2]/div[2]/div[2]/section[1]/ul/li[1]/div[2]')
        print(seq_map.text)
        # verify the coordinates data for the sequence map
        self.assertEqual(seq_map.text, 'Chr2:105499245-105527709 bp, + strand\nFrom Ensembl annotation of GRCm39',
                         'sequence map coordinates have changed!')
        # clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR,
                                                                     'div.toggleImage.hdExpand').click()
        # find the coordinates column of the strains table
        strains_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strains_table)
        # Iterate the second row of the disease table
        all_cells = table.get_column_cells('Coordinates')
        print(all_cells[1].text)
        # verify the ID/Version row of data
        self.assertEqual(all_cells[1].text, 'Chr2:105499241-105528755 (+)')

    def test_strain_table_vs_seqmap_match(self):
        """
        @status this test verifies that the sequence map coordinates match the strains table C57BL/6J coordinates when the gene model is MGI
        @note mrkdetail-strain-11A
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Igh-8")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Igh-8').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'summaryRibbon')))  # waits until the summary ribbon is displayed on the page
        # locate the Sequence Map coordinates
        seq_map = self.driver.find_element(By.XPATH, '//*[@id="locationRibbon"]/div[2]/section[1]/ul/li[1]/div[2]')
        print(seq_map.text)
        # verify the coordinates data for the sequence map
        self.assertEqual(seq_map.text, 'Chr12:113329416-113330847 bp\nFrom MGI annotation of GRCm39',
                         'sequence map coordinates have changed!')
        # clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR,
                                                                     'div.toggleImage.hdExpand').click()
        # find the coordinates column of the strains table
        strains_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strains_table)
        # Iterate the second row of the disease table
        all_cells = table.get_column_cells('Coordinates')
        print(all_cells[1].text)
        # verify the ID/Version row of data
        self.assertEqual(all_cells[1].text, 'Chr12:113329416-113330847 (.)')

    def test_strain_table_single_fasta(self):
        """
        @status this test verifies that you can download a single FASTA sequence from the Strain table using the download checkbox
        @note mrkdetail-strain-14
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ppnr")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ppnr').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'summaryRibbon')))  # waits until the summary ribbon is displayed on the page
        # clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'scToggle').click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'table_strainMarkers'))):
            print('Strain table is loaded')
        # find and select the the Select Strain box for the strain A/J
        self.driver.find_elements(By.CLASS_NAME, 'sgCheckbox')[2].click()
        # find the "Get FASTA" option in the pulldown list located above the strain table and select it
        Select(self.driver.find_element(By.NAME, 'strainOp')).select_by_visible_text('Get FASTA')
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'strainOp'))):
            print('selected  strain operation box loaded')
        # find and click the 'Go' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[0].click()
        # switch focus to the new tab for the FASTA results
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # verify the correct sequence is being returned
        assert 'MGP_AJ_G0036915 19:53381666-53386571' in self.driver.page_source

    def test_strain_table_multiple_fasta(self):
        """
        @status this test verifies that you can download multiple FASTA sequences from the Strain table using the download checkboxs
        @note mrkdetail-strain-15
        """
        driver = self.driver
        self.driver.set_window_size(1024, 768)
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pax6').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'summaryRibbon')))  # waits until the summary ribbon is displayed on the page
        # clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'scToggle').click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'table_strainMarkers'))):
            print('Strain table is loaded')
        # find and select the the Download boxes for the strains A/J, C3H/HeJ, and CBA/J
        self.driver.find_elements(By.CLASS_NAME, 'sgCheckbox')[2].click()
        self.driver.find_elements(By.CLASS_NAME, 'sgCheckbox')[5].click()
        self.driver.find_elements(By.CLASS_NAME, 'sgCheckbox')[9].click()
        # find the "Get FASTA" option in the pulldown list located above the strain table and select it
        Select(self.driver.find_element(By.NAME, 'strainOp')).select_by_visible_text('Get FASTA')
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'strainOp'))):
            print('selected  strain operation box loaded')
        # find and click the 'Go' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[0].click()
        time.sleep(2)
        # switch focus to the new tab for the FASTA results
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 5)
        # verify the correct sequences are being returned
        assert 'MGP_AJ_G0026191 2:103346997-103376112' in self.driver.page_source
        assert 'MGP_C3HHeJ_G0025950 2:106465683-106497601' in self.driver.page_source
        assert 'MGP_CBAJ_G0025928 2:115224186-115254439' in self.driver.page_source

    def test_strain_table_B6_fasta(self):
        """
        @status this test verifies that you can download a B6 strain gene FASTA sequence from the Strain table using the download checkbox
        @note mrkdetail-strain-16
        """
        driver = self.driver
        self.driver.set_window_size(1200, 900)
        self.driver.find_element(By.NAME, 'nomen').send_keys("Gata1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Gata1').click()
        # waits until the summary ribbon is displayed on the page
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('Summary ribbon is loaded')
        # clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'scToggle').click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'table_strainMarkers'))):
            print('Strain table is loaded')
        # find and select the Download box for the strain C57BL/6J
        self.driver.find_elements(By.CLASS_NAME, 'sgCheckbox')[0].click()
        # find the "Get FASTA" option in the pulldown list located above the strain table and select it
        Select(self.driver.find_element(By.NAME, 'strainOp')).select_by_visible_text('Get FASTA')
        if WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'strainOp'))):
            print('selected  strain operation box loaded')
        # find and click the 'Go' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[0].click()
        time.sleep(2)
        # switch focus to the new tab for the FASTA results
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # verify the correct sequence is being returned
        assert 'MGI_C57BL6J_95661 X:7825499-7844310' in self.driver.page_source

    def test_strain_table_all_fasta(self):
        """
        @status this test verifies that you can download all FASTA sequences from the Strain table using the 'Check All' button
        @note mrkdetail-strain-12, 17
        """
        driver = self.driver
        self.driver.set_window_size(1200, 900)
        self.driver.find_element(By.NAME, 'nomen').send_keys("Zim3")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Zim3').click()
        # waits until the summary ribbon is displayed on the page
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('Summary ribbon is loaded')
        # clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'scToggle').click()
        if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'table_strainMarkers'))):
            print('Strain table is loaded')
        # find and click the 'Select All' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[1].click()
        # find the "Get FASTA" option in the pulldown list located above the strain table and select it
        Select(self.driver.find_element(By.NAME, 'strainOp')).select_by_visible_text('Get FASTA')
        # find and click the 'Go' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[0].click()
        time.sleep(2)
        # switch focus to the new tab for the FASTA results
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # verify the correct sequences are being returned
        assert 'MGI_C57BL6J_2151058 7:6958684-6980419' in self.driver.page_source
        assert 'MGP_129S1SvImJ_G0004408 7:4064690-4089229' in self.driver.page_source
        assert 'MGP_AJ_G0004385 7:3946706-3968051' in self.driver.page_source
        assert 'MGP_AKRJ_G0004367 7:4199441-4224713' in self.driver.page_source
        assert 'MGP_BALBcJ_G0004371 7:4050119-4074786' in self.driver.page_source
        assert 'MGP_C3HHeJ_G0004320 7:4032181-4053614' in self.driver.page_source
        assert 'MGP_C57BL6NJ_G0004520 7:4282414-4306205' in self.driver.page_source
        assert 'MGP_CASTEiJ_G0004280 7:3933580-3955838' in self.driver.page_source
        assert 'MGP_CBAJ_G0004314 7:4422337-4449131' in self.driver.page_source
        assert 'MGP_DBA2J_G0004329 7:3984146-4005522' in self.driver.page_source
        assert 'MGP_FVBNJ_G0004347 7:3958576-3980320' in self.driver.page_source
        assert 'MGP_LPJ_G0004409 7:4189174-4214764' in self.driver.page_source
        assert 'MGP_NZOHlLtJ_G0004519 7:3984097-4008151' in self.driver.page_source
        assert 'MGP_PWKPhJ_G0004233 7:4142731-4165139' in self.driver.page_source
        assert 'MGP_SPRETEiJ_G0004175 7:3565285-3587263' in self.driver.page_source
        assert 'MGP_WSBEiJ_G0004319 7:4155212-4179026' in self.driver.page_source

    def test_strain_specific_marker(self):
        """
        @status this test verifies that a strain-specific marker is correctly identified in the Strain Comparison ribbon
        @note mrkdetail-strain-18
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Mx2")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Mx2').click()
        # waits until the summary ribbon is displayed on the page
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('Summary ribbon is loaded')
        # locate the Strain-specific icon and text in the strain comparison ribbon
        specific = self.driver.find_element(By.LINK_TEXT, 'Strain-Specific Marker')
        print(specific.text)
        # verify the Strain-specific icon and text is displayed in the strain comparison ribbon
        self.assertEqual(specific.text, 'Strain-Specific Marker',
                         'the Strain-specific icon and text is not displaying!')

    def test_strain_only_coord(self):
        """
        @status this test verifies that only the SNPs within 2kb, PCR,and RFLP links exists in the Strain Comparison ribbon when no strain available
        @note mrkdetail-strain-19
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ifna")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ifna').click()
        # waits until the summary ribbon is displayed on the page
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('Summary ribbon is loaded')
        # locate the strain comparison ribbon
        strain_ribbon = self.driver.find_element(By.ID, 'strainRibbon')
        print(strain_ribbon.text)
        # verify the Strain-specific icon and text is displayed in the strain comparison ribbon
        self.assertEqual(strain_ribbon.text, 'Strain\nComparison\nmore\nSNPs within 2kb\n52 from dbSNP Build 142',
                         'the Strain Comparison ribbon display has changed!')

    def test_strain_only_poly(self):
        """
        @status this test verifies that only polymorphism data exists in the Strain Comparison ribbon when no strain or coordinates available
        @note mrkdetail-strain-20
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Act2")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Act2').click()
        # waits until the summary ribbon is displayed on the page
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('Summary ribbon is loaded')
        # locate the strain comparison ribbon
        strain_ribbon = self.driver.find_element(By.ID, 'strainRibbon')
        print(strain_ribbon.text)
        time.sleep(2)  # sleep added to give time for toggle to go from more to less
        # verify the Strain-specific icon and text is displayed in the strain comparison ribbon
        self.assertEqual(strain_ribbon.text, 'Strain\nComparison\nless\nRFLP\n1',
                         'the Strain Comparison ribbon display has changed!')

    def test_strain_table_founders_select(self):
        """
        @status this test verifies that when you click the Select DO/CC Founders button in the Strain Comparison ribbon the correct strains get selected in the strains table
        @note mrkdetail-strain-21
        """
        driver = self.driver
        self.driver.set_window_size(1200, 900)
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pax6")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pax6').click()
        # waits until the summary ribbon is displayed on the page
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('Summary ribbon is loaded')
        # clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR,
                                                                     'div.toggleImage.hdExpand').click()
        # find and click the 'Select DO/CC Founders' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[2].click()
        # verify which Select Strains are checked and which ones are not
        sel1 = self.driver.find_elements(By.NAME, 'seqs')[0].get_attribute('checked')
        sel2 = self.driver.find_elements(By.NAME, 'seqs')[1].get_attribute('checked')
        sel3 = self.driver.find_elements(By.NAME, 'seqs')[2].get_attribute('checked')
        sel4 = self.driver.find_elements(By.NAME, 'seqs')[3].get_attribute('checked')
        sel5 = self.driver.find_elements(By.NAME, 'seqs')[4].get_attribute('checked')
        sel6 = self.driver.find_elements(By.NAME, 'seqs')[5].get_attribute('checked')
        sel7 = self.driver.find_elements(By.NAME, 'seqs')[6].get_attribute('checked')
        sel8 = self.driver.find_elements(By.NAME, 'seqs')[7].get_attribute('checked')
        sel9 = self.driver.find_elements(By.NAME, 'seqs')[8].get_attribute('checked')
        sel10 = self.driver.find_elements(By.NAME, 'seqs')[9].get_attribute('checked')
        sel11 = self.driver.find_elements(By.NAME, 'seqs')[10].get_attribute('checked')
        sel12 = self.driver.find_elements(By.NAME, 'seqs')[11].get_attribute('checked')
        sel13 = self.driver.find_elements(By.NAME, 'seqs')[12].get_attribute('checked')
        sel14 = self.driver.find_elements(By.NAME, 'seqs')[13].get_attribute('checked')
        sel15 = self.driver.find_elements(By.NAME, 'seqs')[14].get_attribute('checked')
        sel16 = self.driver.find_elements(By.NAME, 'seqs')[15].get_attribute('checked')
        sel17 = self.driver.find_elements(By.NAME, 'seqs')[16].get_attribute('checked')
        sel18 = self.driver.find_elements(By.NAME, 'seqs')[17].get_attribute('checked')
        self.assertTrue(sel1, 'sel1 is not selected')
        self.assertTrue(sel2, 'sel2 is not selected')
        self.assertTrue(sel3, 'sel3 is not selected')
        self.assertFalse(sel4, 'sel4 is not selected')
        self.assertFalse(sel5, 'sel5 is not selected')
        self.assertFalse(sel6, 'sel6 is not selected')
        self.assertFalse(sel7, 'sel7 is not selected')
        self.assertFalse(sel8, 'sel8 is not selected')
        self.assertTrue(sel9, 'sel9 is not selected')
        self.assertFalse(sel10, 'sel10 is not selected')
        self.assertFalse(sel11, 'sel11 is not selected')
        self.assertFalse(sel12, 'sel12 is not selected')
        self.assertFalse(sel13, 'sel13 is not selected')
        self.assertTrue(sel14, 'sel14 is not selected')
        self.assertTrue(sel15, 'sel15 is not selected')
        self.assertTrue(sel16, 'sel16 is not selected')
        self.assertFalse(sel17, 'sel17 is not selected')
        self.assertTrue(sel18, 'sel18 is not selected')

    """def test_strain_table_send_sanger(self):
               
        @status this test verifies that you can send Strain table data to Sanger using the pulldown option and it returns the correct data
        @note mrkdetail-strain-22
        @attention this test is not valid right now because there is no option for 'send to Sanger SNP Query  (+/- 2kb)' in he pulldown list
         
        driver = self.driver 
        self.driver.set_window_size(1200, 900)     
        self.driver.find_element(By.NAME, 'nomen').send_keys("Zim3")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Zim3').click()
        # waits until the summary ribbon is displayed on the page
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('Summary ribbon is loaded')
        #clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR, 'div.toggleImage.hdExpand').click()
        #time.sleep(2)
        #find and click the 'Select All' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[1].click()
        time.sleep(2)
        #find the "Send to Sanger SNP Query" option in the pulldown list located above the strain table and select it
        Select (self.driver.find_element(By.NAME, 'strainOp')).select_by_visible_text('Send to Sanger SNP Query (+/- 2kb)')
        time.sleep(2)
        #find and click the 'Go' button
        self.driver.find_elements(By.CLASS_NAME, 'sgButton')[0].click()
        #time.sleep(2)
        #switch focus to the new tab for the Sanger results
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #time.sleep(2)
        #locates the SNPs table and verify the table headers have all the correct strains
        strain_table = Table(self.driver.find_element(By.XPATH, '//*[@id="t_snps_0"]/div[1]/table'))
        cells = strain_table.get_header_cells()
        print(iterate.getTextAsList(cells))
        #time.sleep(5)
        #verify the correct strains are being returned in the header of the table
        print(cells[5].text)
        self.assertEqual(cells[5].text, '129S1/SvImJ', '129S1/SvImJ is not a header')
        self.assertEqual(cells[6].text, 'AKR/J', 'AKR/J is not a header')
        self.assertEqual(cells[7].text, 'A/J', 'A/J is not a header')
        self.assertEqual(cells[8].text, 'BALB/cJ', 'BALB/cJ is not a header')
        self.assertEqual(cells[9].text, 'C3H/HeJ', 'C3H/HeJ is not a header')
        self.assertEqual(cells[10].text, 'C57BL/6NJ', 'C57BL/6NJ is not a header')
        self.assertEqual(cells[11].text, 'CAST/EiJ', 'CAST/EiJ is not a header')
        self.assertEqual(cells[12].text, 'CBA/J', 'CBA/J is not a header')
        self.assertEqual(cells[13].text, 'DBA/2J', 'DBA/2J is not a header')
        self.assertEqual(cells[14].text, 'FVB/NJ', 'FVB/NJ is not a header')
        self.assertEqual(cells[15].text, 'LP/J', 'LP/J is not a header')
        self.assertEqual(cells[16].text, 'NOD/ShiLtJ', 'NOD/ShiLtJ is not a header')
        self.assertEqual(cells[17].text, 'NZO/HlLtJ', 'NZO/HlLtJ is not a header')
        self.assertEqual(cells[18].text, 'PWK/PhJ', 'PWK/PhJ is not a header')
        self.assertEqual(cells[19].text, 'SPRET/EiJ', 'SPRET/EiJ is not a header')
        self.assertEqual(cells[20].text, 'WSB/EiJ', 'WSB/EiJ is not a header')      
"""

    def test_strain_table_multi_models(self):
        """
        @status this test verifies that when a gene has multiple gene model IDs to the same strain the strain table displays them correctly
        @note mrkdetail-strain-22
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Rprl1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Rprl1').click()
        # waits until the summary ribbon is displayed on the page
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('Summary ribbon is loaded')
        # clicks the More toggle(turnstile) to display the strain table
        self.driver.find_element(By.ID, 'strainRibbon').find_element(By.CSS_SELECTOR,
                                                                     'div.toggleImage.hdExpand').click()
        # find the Gene Model ID column of the strains table
        strains_table = self.driver.find_element(By.ID, 'table_strainMarkers')
        table = Table(strains_table)
        # Iterate the first column of the disease table
        strain_cells = table.get_column_cells('Strain')
        print(strain_cells[1].text)
        # verify the rows of data for the Strain column
        self.assertEqual(strain_cells[1].text, 'C57BL/6J')
        self.assertEqual(strain_cells[2].text, '129S1/SvImJ')
        self.assertEqual(strain_cells[3].text, 'A/J')
        self.assertEqual(strain_cells[4].text, 'A/J')
        self.assertEqual(strain_cells[5].text, 'AKR/J')
        self.assertEqual(strain_cells[6].text, 'AKR/J')
        self.assertEqual(strain_cells[7].text, 'BALB/cJ')
        self.assertEqual(strain_cells[8].text, 'BALB/cJ')
        self.assertEqual(strain_cells[9].text, 'C3H/HeJ')
        # Iterate the second column of the disease table
        model_cells = table.get_column_cells('Gene Model ID')
        print(model_cells[1].text)
        # verify the Gene Model ID column of data
        self.assertEqual(model_cells[1].text, 'MGI_C57BL6J_105105')
        self.assertEqual(model_cells[2].text, 'MGP_129S1SvImJ_G0005544')
        self.assertEqual(model_cells[3].text, 'MGP_AJ_G0006976')
        self.assertEqual(model_cells[4].text, 'MGP_AJ_G0036786')
        self.assertEqual(model_cells[5].text, 'MGP_AKRJ_G0036736')
        self.assertEqual(model_cells[6].text, 'MGP_AKRJ_G0007264')
        self.assertEqual(model_cells[7].text, 'MGP_BALBcJ_G0036776')
        self.assertEqual(model_cells[8].text, 'MGP_BALBcJ_G0006952')
        self.assertEqual(model_cells[9].text, 'no annotation')

    def test_turnstile_behavior(self):
        """
        @status this test verifies In the Human Diseases section, confirm there are turnstile icons for showing more data
        and clicking the turnstile icon displays the complete Human Diseases table.
        @note mrkdetail-hdisease-1
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Shh")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Shh').click()
        # waits until the summary ribbon is displayed on the page
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('Summary ribbon is loaded')
        # clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, '#diseaseRibbon > div:nth-child(2) > div:nth-child(1)').click()
        diseasetable = self.driver.find_element(By.ID, 'humanDiseaseTable')
        self.assertTrue(diseasetable.is_displayed())

    def test_disease_tbl_doids(self):
        """
        @status this test verifies that the disease table in the Human Diseases ribbon now displays the DOID beside
         each disease instead of the OMIM ID
         @bug need to ask Olin why would only certain diseases get captured from the table?
         @note mrkdetail-hdisease-2
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ins2")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ins2').click()
        # waits until the summary ribbon is displayed on the page
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('Summary ribbon is loaded')
        # clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, '#diseaseRibbon > div:nth-child(2) > div:nth-child(1)').click()
        # find each of the Human Diseases listed for the first 6 items
        disease1 = self.driver.find_element(By.CSS_SELECTOR,
                                            '#humanDiseaseTable > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(5) > div:nth-child(1) > a:nth-child(1)')
        disease2 = self.driver.find_element(By.CSS_SELECTOR,
                                            '#humanDiseaseTable > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
        disease3 = self.driver.find_element(By.CSS_SELECTOR,
                                            '#humanDiseaseTable > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
        disease4 = self.driver.find_element(By.CSS_SELECTOR,
                                            '#humanDiseaseTable > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(5) > div:nth-child(1) > a:nth-child(1)')
        disease5 = self.driver.find_element(By.CSS_SELECTOR,
                                            '#humanDiseaseTable > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
        disease6 = self.driver.find_element(By.CSS_SELECTOR,
                                            '#humanDiseaseTable > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(5) > div:nth-child(1) > a:nth-child(1)')
        print(disease1.text)
        print(disease2.text)
        print(disease3.text)
        print(disease4.text)
        print(disease5.text)
        print(disease6.text)
        # print row 1
        # assert the first 6 disease names are correct
        self.assertEqual(disease1.text, 'permanent neonatal diabetes mellitus')
        self.assertEqual(disease2.text, 'type 1 diabetes mellitus')
        self.assertEqual(disease3.text, 'type 2 diabetes mellitus')
        self.assertEqual(disease4.text, 'maturity-onset diabetes of the young')
        self.assertEqual(disease5.text, 'neonatal diabetes')
        self.assertEqual(disease6.text, 'diabetes mellitus')

    def test_mouse_model_strain_links(self):
        """
        @status this test verifies In the Human Diseases section, from the Mouse Model popup strains in Genetic background link to their strain
        detail page.
        @note mrkdetail-hdisease-3
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pde6b")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pde6b').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('Summary ribbon is loaded')
        # clicks the More toggle(turnstile) to display the human disease table
        self.driver.find_element(By.CSS_SELECTOR, '#diseaseRibbon > div:nth-child(2) > div:nth-child(1)').click()
        # find and click the View link for mouse model of retinitis pigmentosa 40
        self.driver.find_element(By.ID, 'showDOID_0110375').click()
        # Find the link in the Genetic Background column for Pde6B<rd1>/Pde6b<rd1> and click it
        self.driver.find_element(By.LINK_TEXT, 'C3H/HeJ').click()
        time.sleep(2)
        # switch focus to the new tab for strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # Asserts that the strain page is for the correct strain
        assert "C3H/HeJ" in self.driver.page_source

    def test_mpontology_annot_strain_links(self):
        """
        @status this test verifies when you click the Phenotype summary link(for genetic backgrounds) from the Mutations, Alleles, and Phenotypes ribbon
        to open the MP ontology annotations page you find strains in the genetic background column link to their strain detail page.
        @note mrkdetail-allele-5
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pde6b")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pde6b').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('Summary ribbon is loaded')
        self.driver.find_element(By.ID, 'phenoAnnotationLink').click()
        # Find the link in the Genetic Background column C57BL/6J-Pde6b<rd1-2J>/J and click it
        self.driver.find_element(By.LINK_TEXT, 'C57BL/6J-Pde6brd1-2J/J').click()
        # switch focus to the new tab for strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        print(page_title.text)
        # Asserts that the strain page is for the correct strain
        self.assertEqual(page_title.text, 'C57BL/6J-Pde6brd1-2J/J', 'Page title is not correct!')

    def test_mpontology_annot_strain_links2(self):
        """
        @status this test verifies when you click the Phenotype summary link(for multigenic genotypes) from the Mutations, Alleles, and Phenotypes ribbon
        to open the MP ontology annotations page you find strains in the genetic background column link to their strain detail page.
        @note mrkdetail-allele-6
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').send_keys("Pde6b")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Pde6b').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('Summary ribbon is loaded')
        self.driver.find_element(By.ID, 'phenoMultigenicLink').click()
        # Find the link in the Genetic Background column C57BL/6J-Pde6b<rd1-2J> Pde6a<nmf363>and click it
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'C57BL/6J-Pde6brd1-2J').click()
        time.sleep(2)
        # switch focus to the new tab for strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        print(page_title.text)
        # Asserts that the strain page is for the correct strain
        self.assertEqual(page_title.text, 'C57BL/6J-Pde6brd1-2J Pde6anmf363', 'Page title is not correct!')

    def test_mpontology_annot_strain_links3(self):
        """
        @status this test verifies when you click one of the blue cells in the phenoslim grid from the Mutations, Alleles, and Phenotypes ribbon
        to open the Phenotype annotations related to page, then click a Mouse Genotype to find strains in the genetic background column link to their strain detail page(for Summary ribbon and for Genotype ribbon.
        @note mrkdetail-allele-7 !!!broken - 3/25/2024!!
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Sry")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Sry').click()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'summaryRibbon'))):
            print('Summary ribbon is loaded')
        # locates the phenogrid and click on the cell for reproductive System
        self.driver.find_element(By.ID, 'mpSlimgrid22Div').click()
        pheno_table = Table(self.driver.find_element(By.ID, "mpSlimgridTable"))
        pheno_table.get_cell(2, 21).click()
        # switch focus to the new tab for Phenotype annotations related to reproductive System
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # find and click the Mouse Genotype for X/Sry<AKR/J>
        self.driver.find_element(By.CSS_SELECTOR, "fm19084a").click()
        # switch focus to the new tab for Phenotypes associated with X/Sry<AKR/J>
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 2)
        # Locate the Genetic Background column and click the link found there(Summary ribbon)
        self.driver.find_element(By.LINK_TEXT, 'AKR/J').click()
        # switch focus to the new tab for strain detail page
        self.driver.switch_to.window(self.driver.window_handles[-1])
        wait.forNewWindow(self.driver, 5)
        page_title = self.driver.find_element(By.CLASS_NAME, 'titleBarMainTitle')
        print(page_title.text)
        # Asserts that the strain page is for the correct strain detail
        self.assertEqual(page_title.text, 'AKR/J', 'Page title is not correct!')

    def test_qtl_detail_interactions(self):
        """
        @status this test verifies the existence of a QTL interaction link in the summary section below the Feature Type. Clicking the link displays a popup table.
        @bug: can't get to page because other page tab closes....
        @note mrkdetail-qtl-interaction-1
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Lmr14")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Lmr14').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'summaryRibbon')))  # waits until the summary ribbon is displayed on the page
        # find the QTL Interaction link and click it
        self.driver.find_element(By.ID, 'showInteractingQTL').click()
        # find the Interaction table
        inter_table = self.driver.find_element(By.ID, 'interactingQTLTbl')
        print(inter_table.text)
        # Asserts that the Interaction table is returning the correct data
        self.assertEqual(inter_table.text,
                         'QTL Genetic Location* Genome Location (GRCm39) Interaction Type Reference\nLmr5 Chr10, 73.57 cM Chr10:116220635-122179828 enhancement J:108764\nLmr12 Chr16, 30.45 cM Chr16:45792813-45792952 synthetic J:108764\nLmr13 Chr18, 23.86 cM Chr18:45109380-45109518 synthetic J:108764\nLmr25 Chr10, syntenic Chr10:125575094-125575232 enhancement J:82717',
                         'Page title is not correct!')

    def test_qtl_detail_candidate(self):
        """
        @status this test verifies the existence of a Candidate Genes link in the summary section below the Feature Type(on QTL detail). Clicking the link displays a popup table.
        @note mrkdetail-qtl-candidate-gene-1
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Skts2")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Skts2').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'summaryRibbon')))  # waits until the summary ribbon is displayed on the page
        # find the Candidate Genes link and click it
        self.driver.find_element(By.ID, 'showCandidates').click()
        # find the Candidates table
        candidate_table = self.driver.find_element(By.ID, 'candidatesTbl')
        print(candidate_table.text)
        # find the first gene listed and assert it's correct
        gene1 = self.driver.find_element(By.CSS_SELECTOR,
                                         '#candidatesTbl > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > a:nth-child(1)')
        self.assertEqual(gene1.text, 'Hras')
        # find the second gene listed and assert it's correct
        gene2 = self.driver.find_element(By.CSS_SELECTOR,
                                         '#candidatesTbl > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > a:nth-child(1)')
        self.assertEqual(gene2.text, 'Tyr')

    def test_qtl_detail_candidate1(self):
        """
        @status this test verifies the existence of a Candidate for QTL link in the summary section below the Feature Type(on Marker detail). Clicking the link displays a popup table.
        @note mrkdetail-qtl-candidate-gene-1
        """
        driver = self.driver
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Hras")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Hras').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, 'summaryRibbon')))  # waits until the summary ribbon is displayed on the page
        # find the Candidate for QTL link and click it
        self.driver.find_element(By.ID, 'showCandidateFor').click()
        # find the Candidates table
        candidatefor_table = self.driver.find_element(By.ID, 'candidateForTbl')
        print(candidatefor_table.text)
        # Asserts that the Interaction table is returning the correct data
        self.assertEqual(candidatefor_table.text,
                         'QTL Genetic Location* Genome Location (GRCm39) Reference QTL Note\nSkts2 Chr7, 73.19 cM Chr7:129922733-129922943 J:85134 Several skin tumor susceptibility QTLs (Skts1-Skts13) were previously identified in a population of (NIH/Ola x M. spretus)F1 x NIH/Ola backcross animals. In this study the association of allele-specific mutations at the Skts intervals was examined in skin carcinoma samples. Several loci displayed allelic loss or duplication in skin carcinomas. 90 % of papillomas and carcinomas contain a mutation at codon 61 of the Hras1 gene (72 cM). In 23 out of 26 mouse tumors the Hras1 mutation occurred in the NIH/Ola-inherited allele. Hras1 maps near skin tumor susceptibility QTL Skts2 (64 cM on mouse Chromosome 7). A nearby marker, D7Mit12 (66 cM) also shows allelic imbalance involving the NIH/Ola allele. On mouse Chromosome 6, preferential gain of the M. spretus allele or loss of the NIH/Ola allele was observed at D6Mit9 (36.5 cM) near Skts11 in 21 out of 21 carcinomas, and preferential gain of the M. spretus allele was observed at D6Mit15 (74 cM) near Skts12 in 14 out of 16 carcinomas. On mouse Chromosome 9, preferential loss of the M. spretus allele or gain of the NIH/Ola allele was observed at D9Mit9 (48 cM) near Skts6 in 16 out of 23 carcinomas. On mouse Chromosome 16, preferential loss of the M. spretus allele or gain of the NIH/Ola allele was observed at D16Mit2 (14.1 cM) near Skts9 in 10 out of 29 carcinomas.',
                         'Page data is not correct!')

    def test_glygen_link(self):
        """
        @status this test verifies that the glygen link for proteins goes to the correct website location.
        @note test works as of 3/01/24
        """
        self.driver.find_element(By.NAME, 'nomen').send_keys("Cds2")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Cds2').click()
        glygenlnk = self.driver.find_element(By.LINK_TEXT, 'Q99L43')
        href = glygenlnk.find_element(By.XPATH, "//a").get_attribute('href')

        self.assertTrue(href, "https://glygen.org/protein/Q99L43/#Glycosylation")

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestMarkerDetail))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
