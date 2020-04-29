'''
Created on Jan 27, 2017

@author: jeffc
'''
import HtmlTestRunner
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from hmdc_autocomplete_list import TestHmdcAutocomplete
from hmdc_diseasetab import TestHmdcDiseaseTab
from hmdc_genetab import TestHmdcGeneTab
from hmdc_indextab import TestHmdcIndex
from hmdc_search_gene import TestHmdcGenesSearch
from hmdc_search_geneid import TestHmdcSearchGeneid
from hmdc_search_id import TestHmdcSearchID
from hmdc_search_term import TestHmdcSearchTerm

print('Begin HMDC testing')
hmdc_autocomplete_test = TestLoader().loadTestsFromTestCase(TestHmdcAutocomplete)
hmdc_diseasetab_test = TestLoader().loadTestsFromTestCase(TestHmdcDiseaseTab)
hmdc_genetab_test = TestLoader().loadTestsFromTestCase(TestHmdcGeneTab)
hmdc_indextab_test = TestLoader().loadTestsFromTestCase(TestHmdcIndex)
hmdc_genesearch_test = TestLoader().loadTestsFromTestCase(TestHmdcGenesSearch)
hmdc_geneidsearch_test = TestLoader().loadTestsFromTestCase(TestHmdcSearchGeneid)
hmdc_idsearch_test = TestLoader().loadTestsFromTestCase(TestHmdcSearchID)
hmdc_termsearch_test = TestLoader().loadTestsFromTestCase(TestHmdcSearchTerm)
#Put them in an Array
hmdc_suite = TestSuite([hmdc_autocomplete_test, hmdc_diseasetab_test, hmdc_genetab_test, hmdc_indextab_test, hmdc_genesearch_test, hmdc_geneidsearch_test, hmdc_idsearch_test, hmdc_termsearch_test])
print('End HMDC testing')
#file
runner = HTMLTestRunner(output='C://WebdriverTests/hmdc_suite')
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyHMDCReport", add_timestamp=False).run(hmdc_suite)
runner.run(hmdc_suite)

if __name__=="__main__":
    main()