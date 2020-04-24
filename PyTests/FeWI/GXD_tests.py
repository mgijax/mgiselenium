'''
Created on Apr 23, 2018

@author: jeffc
'''

import unittest
from gxd_diff_qf import TestGXDDifferentialQF
from gxd_image_summary import TestGXDImageSummary
from gxd_qf import TestGXDQF
from gxd_results import TestGXDResults
from gxd_rna_seq_qf_autocomplete_list import TestStructureAutocomplete
from gxd_rna_seq_qf_search import TestRnaSeqSearching
from gxd_rna_seq_samples import TestRnaSeqSamples
from gxd_rna_seq_summary import TestRnaSeqSummary
from gxd_txp_matrix import TestGXDTissuePhenotypeMatrix
from gxd_txs_matrix import TestGXDTissueStageMatrix

import os
import HtmlTestRunner
# Get the Present Working Directory since that is the place where the report
# would be stored
 
current_directory = os.getcwd()
from FeWI import gxd_diff_qf, gxd_image_summary, gxd_qf, gxd_results, gxd_rna_seq_qf_autocomplete_list, gxd_rna_seq_qf_search, gxd_rna_seq_samples, gxd_rna_seq_summary, gxd_txp_matrix, gxd_txs_matrix

#from fewi import TestGXDDifferentialQF, TestGXDImageSummary, TestGXDQF, TestGXDTissuePhenotypeMatrix, TestGXDTissueStageMatrix
class HTML_TestRunner_TestSuite(unittest.TestCase):
    def test_Gxd_Search(self):
        print('first test')
        # Create a TestSuite comprising the two test cases
        consolidated_test = unittest.TestSuite()
 
        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGXDDifferentialQF),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGXDImageSummary),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGXDQF),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGXDResults),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestStructureAutocomplete),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestRnaSeqSearching),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestRnaSeqSamples),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestRnaSeqSummary),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGXDTissuePhenotypeMatrix),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGXDTissueStageMatrix)
        ])
 
        #output_file = open(current_directory + "C:\WebdriverTests\Fewigxdreport.html", "w")
        output_file = open("C:\WebdriverTests\Fewigxdreport.html", "w")
 
        html_runner = HtmlTestRunner.HTMLTestRunner(
            stream=output_file,
            report_title='HTML Reporting using PyUnit',
            descriptions='HTML Reporting using PyUnit & HTMLTestRunner'
        )
 
        html_runner.run(consolidated_test)
 
if __name__ == '__main__':
    unittest.main()
    print('print main')
#def main():
    #gxd_diff_qf_test = unittest.TestLoader().loadTestsFromTestCase(TestGXDDifferentialQF)
    #gxd_image_summary_test = unittest.TestLoader().loadTestsFromTestCase(TestGXDImageSummary)
    #gxd_qf_test = unittest.TestLoader().loadTestsFromTestCase(TestGXDQF)
    #gxd_results_test = unittest.TestLoader().loadTestsFromTestCase(TestGXDResults)
    #gxd_rna_seq_qf_autocomplete_test = unittest.TestLoader().loadTestsFromTestCase(TestStructureAutocomplete)
    #gxd_rna_seq_qf_search_test = unittest.TestLoader().loadTestsFromTestCase(TestRnaSeqSearching)
    #gxd_rna_seq_samples_test = unittest.TestLoader().loadTestsFromTestCase(TestRnaSeqSamples)
    #gxd_rna_seq_summary_test = unittest.TestLoader().loadTestsFromTestCase(TestRnaSeqSummary)
    #gxd_txp_matrix_test = unittest.TestLoader().loadTestsFromTestCase(TestGXDTissuePhenotypeMatrix)
    #gxd_txs_matrix_test = unittest.TestLoader().loadTestsFromTestCase(TestGXDTissueStageMatrix)

#Put them in an Array
    #gxd_tests = unittest.TestSuite([gxd_diff_qf_test, gxd_image_summary_test, gxd_qf_test, gxd_results_test, gxd_rna_seq_qf_autocomplete_test, gxd_rna_seq_qf_search_test, gxd_rna_seq_samples_test, gxd_rna_seq_summary_test, gxd_txp_matrix_test, gxd_txs_matrix_test])
#file
    #result_dir = os.getcwd()
    #outfile = open(result_dir + "C:\WebdriverTests\Fewigxdreport.html", "w")
    #runner = HtmlTestRunner.HTMLTestRunner(stream = outfile,title = 'Test Report',description = 'Fewi GXD Test Report')
    #runner.run(gxd_tests)

#if __name__=="__main__":
    #main()