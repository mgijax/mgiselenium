'''
Created on Jun 8, 2018

@author: jeffc
'''

import unittest
from .strain_qf import TestStrainQF
from .strain_detail import TestStrainDetail
from .strain_summary import TestStrainSummary
from .ref_by_strain import TestRefByStrain
from .reference_summary_bystrain import TestReferenceSummaryStrain
import os
import HtmlTestRunner
from FeWI import strain_qf, strain_detail, strain_summary, ref_by_strain, reference_summary_bystrain

def main():
    strain_qf_test = unittest.TestLoader().loadTestsFromTestCase(TestStrainQF)
    strain_detail_test = unittest.TestLoader().loadTestsFromTestCase(TestStrainDetail)
    strain_summary_test = unittest.TestLoader().loadTestsFromTestCase(TestStrainSummary)
    ref_by_strain_test = unittest.TestLoader().loadTestsFromTestCase(TestRefByStrain)
    refeference_summary_bystrain_test = unittest.TestLoader().loadTestsFromTestCase(TestReferenceSummaryStrain)

#Put them in an Array
    strain_tests = unittest.TestSuite([strain_qf_test, strain_detail_test, strain_summary_test, ref_by_strain_test, refeference_summary_bystrain_test])
#file
    result_dir = os.getcwd()
    outfile = open(result_dir + "C:\WebdriverTests\Straintestreport.html", "w")
    runner = HtmlTestRunner.HTMLTestRunner(stream = outfile,title = 'Test Report',description = 'Strains Test Report')
    runner.run(strain_tests)

if __name__=="__main__":
    main()