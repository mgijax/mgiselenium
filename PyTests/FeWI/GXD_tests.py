'''
Created on Apr 23, 2018

@author: jeffc
'''
import HtmlTestRunner
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from gxd_diff_qf import TestGxdDifferentialQF
from gxd_image_summary import TestGxdImageSummary
from gxd_qf import TestGxdQF
from gxd_results import TestGxdResults
from gxd_rna_seq_qf_autocomplete_list import TestGxdRnaSeqAutocomplete
from gxd_rna_seq_qf_search import TestGxdRnaSeqSearching
from gxd_rna_seq_samples import TestGxdRnaSeqSamples
from gxd_rna_seq_summary import TestGxdRnaSeqSummary
from gxd_txp_matrix import TestGXDTissuePhenotypeMatrix
from gxd_txs_matrix import TestGXDTissueStageMatrix

print('Begin GXD testing')
gxd_diff_qf_test = TestLoader().loadTestsFromTestCase(TestGxdDifferentialQF)
gxd_image_summary_test = TestLoader().loadTestsFromTestCase(TestGxdImageSummary)
gxd_qf_test = TestLoader().loadTestsFromTestCase(TestGxdQF)
gxd_results_test = TestLoader().loadTestsFromTestCase(TestGxdResults)
gxd_rna_seq_qf_autocomplete_test = TestLoader().loadTestsFromTestCase(TestGxdRnaSeqAutocomplete)
gxd_rna_seq_qf_search_test = TestLoader().loadTestsFromTestCase(TestGxdRnaSeqSearching)
gxd_rna_seq_samples_test = TestLoader().loadTestsFromTestCase(TestGxdRnaSeqSamples)
gxd_rna_seq_summary_test = TestLoader().loadTestsFromTestCase(TestGxdRnaSeqSummary)
gxd_txp_matrix_test = TestLoader().loadTestsFromTestCase(TestGXDTissuePhenotypeMatrix)
gxd_txs_matrix_test = TestLoader().loadTestsFromTestCase(TestGXDTissueStageMatrix)
#Put them in an Array
gxd_suite = TestSuite([gxd_diff_qf_test, gxd_image_summary_test, gxd_qf_test, gxd_results_test, gxd_rna_seq_qf_autocomplete_test, gxd_rna_seq_qf_search_test, gxd_rna_seq_samples_test, gxd_rna_seq_summary_test, gxd_txp_matrix_test, gxd_txs_matrix_test])
print('End GXD testing') 
#file
runner = HTMLTestRunner(output='C://WebdriverTests/gxd_suite')
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyGXDReport", add_timestamp=False).run(gxd_suite)
runner.run(gxd_suite)

if __name__=="__main__":
    main()