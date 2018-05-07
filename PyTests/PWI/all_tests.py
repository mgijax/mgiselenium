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

# import all sub test suites
import gxd_antibody_summary
import gxd_assay_summary
import gxd_image_pane_summary
import gxd_lit_index_by_mrk
import gxd_spec_summary_by_ref

# add the test suites
def master_suite():
        suites = []
        suites.append(gxd_antibody_summary.suite())
        suites.append(gxd_assay_summary.suite())
        suites.append(gxd_image_pane_summary.suite())
        suites.append(gxd_lit_index_by_mrk.suite())
        suites.append(gxd_spec_summary_by_ref.suite())
        
        master_suite = unittest.TestSuite(suites)
        return master_suite

if __name__ == '__main__':
        test_suite = master_suite()
        runner = unittest.TextTestRunner()
        
        ret = not runner.run(test_suite).wasSuccessful()
        sys.exit(ret)
