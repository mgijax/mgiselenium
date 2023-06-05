'''
Created on Jan 27, 2017

@author: jeffc
'''
import unittest
from unittest import TestLoader, TestSuite
from HTMLTestRunner import HTMLTestRunner
from hmdc_autocomplete_list import TestHmdcAutocomplete
from hmdc_diseasetab import TestHmdcDiseaseTab
from hmdc_genetab import TestHmdcGeneTab
from hmdc_indextab import TestHmdcIndex
from hmdc_search_gene import TestHmdcGenesSearch
from hmdc_search_geneid import TestHmdcSearchGeneid
from hmdc_search_id import TestHmdcSearchID
from hmdc_search_term import TestHmdcSearchTerm

print('Begin HMDC testing')
test1 = TestLoader().loadTestsFromTestCase(TestHmdcAutocomplete)
test2 = TestLoader().loadTestsFromTestCase(TestHmdcDiseaseTab)
test3 = TestLoader().loadTestsFromTestCase(TestHmdcGeneTab)
test4 = TestLoader().loadTestsFromTestCase(TestHmdcIndex)
test5 = TestLoader().loadTestsFromTestCase(TestHmdcGenesSearch)
test6 = TestLoader().loadTestsFromTestCase(TestHmdcSearchGeneid)
test7 = TestLoader().loadTestsFromTestCase(TestHmdcSearchID)
test8 = TestLoader().loadTestsFromTestCase(TestHmdcSearchTerm)
suite = unittest.TestSuite([test1, test2, test3, test4, test5, test6, test7, test8])
runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='fewi HDMC Test report', report_name='fewihdmcreport',
                          open_in_browser=True, description="HTMLTestReport")
runner.run(suite)

if __name__=="__main__":
    unittest.main(testRunner=HTMLTestRunner())

