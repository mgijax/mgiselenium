'''
Created on Apr 23, 2018

@author: jeffc
'''
import unittest
from unittest import TestLoader, TestSuite
from HTMLTestRunner import HTMLTestRunner
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
test1 = TestLoader().loadTestsFromTestCase(TestGxdDifferentialQF)
test2 = TestLoader().loadTestsFromTestCase(TestGxdImageSummary)
test3 = TestLoader().loadTestsFromTestCase(TestGxdQF)
test4 = TestLoader().loadTestsFromTestCase(TestGxdResults)
test5 = TestLoader().loadTestsFromTestCase(TestGxdRnaSeqAutocomplete)
test6 = TestLoader().loadTestsFromTestCase(TestGxdRnaSeqSearching)
test7 = TestLoader().loadTestsFromTestCase(TestGxdRnaSeqSamples)
test8 = TestLoader().loadTestsFromTestCase(TestGxdRnaSeqSummary)
test9 = TestLoader().loadTestsFromTestCase(TestGXDTissuePhenotypeMatrix)
test10 = TestLoader().loadTestsFromTestCase(TestGXDTissueStageMatrix)
suite = unittest.TestSuite([test1, test2, test3, test4, test5, test6, test7, test8, test9, test10])
runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='fewi GXD Test report', report_name='fewigxdreport',
                          open_in_browser=True, description="HTMLTestReport")
runner.run(suite)

if __name__=="__main__":
    unittest.main(testRunner=HTMLTestRunner())
