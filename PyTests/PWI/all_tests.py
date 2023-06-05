"""
Run all PWI EMAPA test suites
"""
import sys,os.path

# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../../config',)
)
import config

import unittest
from HTMLTestRunner import HTMLTestRunner

# import all sub test suites
from PWI import pwi_gxd_antibody_summary
from PWI import pwi_gxd_assay_summary
from PWI import pwi_gxd_image_pane_summary
from PWI import pwi_mrk_detail
from PWI import pwi_gxd_spec_summary_by_ref

# add the test suites
def master_suite():
        suites = []
        suites.append(pwi_gxd_antibody_summary.suite())
        suites.append(pwi_gxd_assay_summary.suite())
        suites.append(pwi_gxd_image_pane_summary.suite())
        suites.append(pwi_mrk_detail.suite())
        suites.append(pwi_gxd_spec_summary_by_ref.suite())
        
        master_suite = unittest.TestSuite(suites)
        return master_suite

if __name__ == '__main__':
        test_suite = master_suite()
        runner = unittest.TextTestRunner()
        
        ret = not runner.run(test_suite).wasSuccessful()
        sys.exit(ret)
