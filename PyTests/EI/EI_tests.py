'''
Created on Apr 28, 2020

@author: jeffc
'''
import unittest
import HtmlTestRunner
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
#from Allele.allele_search_tests import TestEIAlleleSearch
from DOAnnot.do_annot_search_tests import TestEIDoannotSearch
from EmapA.emapaclipboardtest import TestEiEmapaClipboard
from EmapA.emapadetailtest import TestEiEmapaDetail
from EmapA.emapasearchtest import TestEiEmapaSearch
from EmapA.emapatreeviewtest import TestEiEmapaTreeView
from Genotype.genotype_search_tests import TestEiGenotypeSearch
from GxdIndex.gxdindex_clear_test import TestEiGxdIndexClear
from GxdIndex.gxdindex_notes_picklist_test import TestEiGxdIndexNotesPicklist
from GxdIndex.gxdindex_search_test import TestEiGxdIndexSearch
from GxdIndex.gxdindex_shortcuts_test import TestEiGxdIndexShortcuts
from Image.image_creative_commons_tests import TestEiImageCCSearch
from Image.image_pane_tests import TestEiImagePaneSearch
from Image.image_search_test import TestEiImageSearch
from LitTriage.littriage_detail_test import TestEiLitTriageDetail
from LitTriage.littriage_search_test import TestEiLitTriageSearch
from LitTriage.littriage_summary_test import TestEiLitTriageSummarySearch
from Marker.marker_search_history_test import TestEiMrkSearchHistory 
from Marker.marker_search_test import TestEiMrkSearchHistory 
from MPAnnot.mp_annot_search_tests import TestEiMpannotSearch
from Variant.variant_search_test import TestEiVariantSearch
from Logintest import TestLogintest
print('Begin EI testing')
#ei_allele_search_test = TestLoader().loadTestsFromTestCase(TestEIAlleleSearch)
ei_doannot_search_test = TestLoader().loadTestsFromTestCase(TestEIDoannotSearch)
ei_emapa_clipboard_test = TestLoader().loadTestsFromTestCase(TestEiEmapaClipboard)
ei_emapa_detail_test = TestLoader().loadTestsFromTestCase(TestEiEmapaDetail)
ei_emapa_search_test = TestLoader().loadTestsFromTestCase(TestEiEmapaSearch)
ei_emapa_treeeview_test = TestLoader().loadTestsFromTestCase(TestEiEmapaTreeView)
ei_genotype_search_test = TestLoader().loadTestsFromTestCase(TestEiGenotypeSearch)
ei_gxdindex_clear_test = TestLoader().loadTestsFromTestCase(TestEiGxdIndexClear)
ei_gxdindex_picklist_test = TestLoader().loadTestsFromTestCase(TestEiGxdIndexNotesPicklist)
ei_gxdindex_search_test = TestLoader().loadTestsFromTestCase(TestEiGxdIndexSearch)
ei_gxdindex_shortcuts_test = TestLoader().loadTestsFromTestCase(TestEiGxdIndexShortcuts)
ei_image_cc_test = TestLoader().loadTestsFromTestCase(TestEiImageCCSearch)
ei_image_pane_test = TestLoader().loadTestsFromTestCase(TestEiImagePaneSearch)
ei_image_search_test = TestLoader().loadTestsFromTestCase(TestEiImageSearch)
ei_littriage_detail_test = TestLoader().loadTestsFromTestCase(TestEiLitTriageDetail)
ei_littriage_search_test = TestLoader().loadTestsFromTestCase(TestEiLitTriageSearch)
ei_littriage_summary_test = TestLoader().loadTestsFromTestCase(TestEiLitTriageSummarySearch)
ei_marker_search_history_test = TestLoader().loadTestsFromTestCase(TestEiMrkSearchHistory)
ei_marker_search_test = TestLoader().loadTestsFromTestCase(TestEiMrkSearchHistory)
ei_mp_annot_search_test = TestLoader().loadTestsFromTestCase(TestEiMpannotSearch)
ei_variant_search_test = TestLoader().loadTestsFromTestCase(TestEiVariantSearch)
ei_login_test = TestLoader().loadTestsFromTestCase(TestLogintest)
#Put them in an Array
ei_test_suite = TestSuite([ei_doannot_search_test, ei_emapa_clipboard_test, ei_emapa_detail_test, ei_emapa_search_test, ei_emapa_treeeview_test, ei_genotype_search_test, ei_gxdindex_clear_test, ei_gxdindex_picklist_test, ei_gxdindex_search_test, ei_gxdindex_shortcuts_test, ei_image_cc_test, ei_image_pane_test, ei_image_search_test, ei_littriage_detail_test, ei_littriage_search_test, ei_littriage_summary_test, ei_marker_search_history_test, ei_marker_search_test, ei_mp_annot_search_test, ei_variant_search_test, ei_login_test])
print('End EI testing')
#file
runner = HTMLTestRunner(output='C://WebdriverTests/ei_test_suite')
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyEIReport", add_timestamp=False).run(ei_test_suite)
#runner.run(ei_test_suite)

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
#reports generated Users/jeffc/git/mgiselenium/PyTests/EI/reports  