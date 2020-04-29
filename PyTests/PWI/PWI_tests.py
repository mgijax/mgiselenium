'''
Created on Apr 28, 2020

@author: jeffc
'''

import HtmlTestRunner
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from pwi_do_allele_detail import TestPwiDoAlleleDetail
from pwi_gxd_antibody_summary import TestPwiGxdAntibodySummaryPage
from pwi_gxd_assay_summary import TestPwiGxdAssaySummaryPage
from pwi_gxd_image_pane_summary import TestPwiGxdImagePanePage
from pwi_gxd_lit_index_by_mrk import TestPwiGxdLitIndexByMrk
from pwi_gxd_spec_summary_by_ref import TestPwiGxdSpecSumByRef
from pwi_mrk_detail import TestPwiMrkDetail

print('Begin PWI testing')
pwi_do_allele_test = TestLoader().loadTestsFromTestCase(TestPwiDoAlleleDetail)
pwi_gxd_antibody_test = TestLoader().loadTestsFromTestCase(TestPwiGxdAntibodySummaryPage)
pwi_gxd_assay_test = TestLoader().loadTestsFromTestCase(TestPwiGxdAssaySummaryPage)
pwi_gxd_image_test = TestLoader().loadTestsFromTestCase(TestPwiGxdImagePanePage)
pwi_gxd_litindex_mrk_test = TestLoader().loadTestsFromTestCase(TestPwiGxdLitIndexByMrk)
pwi_gxd_spec_byref_test = TestLoader().loadTestsFromTestCase(TestPwiGxdSpecSumByRef)
pwi_mrk_test = TestLoader().loadTestsFromTestCase(TestPwiMrkDetail)
#Put them in an Array
pwi_test_suite = TestSuite([pwi_do_allele_test, pwi_gxd_antibody_test, pwi_gxd_assay_test, pwi_gxd_image_test, pwi_gxd_litindex_mrk_test, pwi_gxd_spec_byref_test, pwi_mrk_test])
print('End PWI testing')
#file
runner = HTMLTestRunner(output='C://WebdriverTests/pwi_test_suite')
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyPWIReport", add_timestamp=False).run(pwi_test_suite)
runner.run(pwi_test_suite)

if __name__=="__main__":
    main()