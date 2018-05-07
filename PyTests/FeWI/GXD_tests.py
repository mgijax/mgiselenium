'''
Created on Apr 23, 2018

@author: jeffc
'''

import unittest
from gxd_diff_qf import TestGXDDifferentialQF
from gxd_image_summary import TestGXDImageSummary
from gxd_qf import TestGXDQF
from gxd_txp_matrix import TestGXDTissuePhenotypeMatrix
from gxd_txs_matrix import TestGXDTissueStageMatrix
import os
import HTMLTestRunner
from FeWI import gxd_diff_qf, gxd_image_summary, gxd_qf, gxd_txp_matrix, gxd_txs_matrix

#from fewi import TestGXDDifferentialQF, TestGXDImageSummary, TestGXDQF, TestGXDTissuePhenotypeMatrix, TestGXDTissueStageMatrix
def main():
    gxd_diff_qf_test = unittest.TestLoader().loadTestsFromTestCase(TestGXDDifferentialQF)
    gxd_image_summary_test = unittest.TestLoader().loadTestsFromTestCase(TestGXDImageSummary)
    gxd_qf_test = unittest.TestLoader().loadTestsFromTestCase(TestGXDQF)
    gxd_txp_matrix_test = unittest.TestLoader().loadTestsFromTestCase(TestGXDTissuePhenotypeMatrix)
    gxd_txs_matrix_test = unittest.TestLoader().loadTestsFromTestCase(TestGXDTissueStageMatrix)

#Put them in an Array
    gxd_tests = unittest.TestSuite([gxd_diff_qf_test, gxd_image_summary_test, gxd_qf_test, gxd_txp_matrix_test, gxd_txs_matrix_test])
#file
    dir = os.getcwd()
    outfile = open(r"C:\WebdriverTests\Fewigxdreport.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream = outfile,title = 'Test Report',description = 'Fewi GXD Test Report')
    runner.run(gxd_tests)

if __name__=="__main__":
    main()