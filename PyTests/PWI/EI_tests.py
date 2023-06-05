'''
Created on Apr 28, 2020

@author: jeffc
'''
import unittest
from unittest import TestLoader, TestSuite
from HTMLTestRunner import HTMLTestRunner
#from Allele.Allelesearchtests import TestPwiAlleleSearch
from DOAnnot.do_annot_search_tests import TestEIDoannotSearch
from EmapA.emapa_clipboard_tests import TestPwiEmapaClipboard
from EmapA.emapadetailtest import TestPwiEmapaDetail
from EmapA.emapasearchtest import TestPwiEmapaSearch
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
ei_allele_search_test = TestLoader().loadTestsFromTestCase(TestPwiAlleleSearch)
ei_doannot_search_test = TestLoader().loadTestsFromTestCase(TestEIDoannotSearch)
ei_emapa_clipboard_test = TestLoader().loadTestsFromTestCase(TestPwiEmapaClipboard)
ei_emapa_detail_test = TestLoader().loadTestsFromTestCase(TestPwiEmapaDetail)
ei_emapa_search_test = TestLoader().loadTestsFromTestCase(TestPwiEmapaSearch)
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
def test_suite():
  test1 = unittest.TestLoader().loadTestsFromTestCase(TestPwiEmapaClipboard)
  test2 = unittest.TestLoader().loadTestsFromTestCase(TestPwiEmapaDetail)
  test3 = unittest.TestLoader().loadTestsFromTestCase(TestPwiEmapaSearch)
  suite = unittest.TestSuite([test1, test2, test3])
  runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                          open_in_browser=True, description="HTMLTestReport")
  runner.run(suite)
if __name__=="__main__":
    unittest.main(testRunner=HTMLTestRunner())
#reports generated Users/jeffc/git/mgiselenium/PyTests/EI/reports  
