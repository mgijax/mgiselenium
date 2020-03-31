'''
Created on Jan 27, 2017

@author: jeffc
'''
import unittest
from .hmdc_autocomplete_list import TestHMDCAutocomplete
from .hmdc_diseasetab import TestDiseaseTab
from .hmdc_genetab import TestGeneTab
from .hmdc_indextab import TestHmdcIndex
from .hmdc_search_gene import TestGenesSearch
from .hmdc_search_geneid import TestGeneid
from .hmdc_search_id import TestHmdcSearchID
from .hmdc_search_term import TestSearchTerm
import os
import HtmlTestRunner
from FeWI import hmdc_autocomplete_list, hmdc_diseasetab, hmdc_genetab, hmdc_indextab, hmdc_search_gene, hmdc_search_gene, hmdc_search_geneid, hmdc_search_id, hmdc_search_term


def main():
    hmdc_autocomplete_test = unittest.TestLoader().loadTestsFromTestCase(TestHMDCAutocomplete)
    hmdc_diseasetab_test = unittest.TestLoader().loadTestsFromTestCase(TestDiseaseTab)
    hmdc_genetab_test = unittest.TestLoader().loadTestsFromTestCase(TestGeneTab)
    hmdc_indextab_test = unittest.TestLoader().loadTestsFromTestCase(TestHmdcIndex)
    hmdc_genesearch_test = unittest.TestLoader().loadTestsFromTestCase(TestGenesSearch)
    hmdc_geneidsearch_test = unittest.TestLoader().loadTestsFromTestCase(TestGeneid)
    hmdc_idsearch_test = unittest.TestLoader().loadTestsFromTestCase(TestHmdcSearchID)
    hmdc_termsearch_test = unittest.TestLoader().loadTestsFromTestCase(TestSearchTerm)
#Put them in an Array
    hmdc_tests = unittest.TestSuite([hmdc_autocomplete_test, hmdc_diseasetab_test, hmdc_genetab_test, hmdc_indextab_test, hmdc_genesearch_test, hmdc_geneidsearch_test, hmdc_idsearch_test, hmdc_termsearch_test])
#file
    dir = os.getcwd()
    outfile = open(r"C:\WebdriverTests\HMDCtestreport.html", "w")
    runner = HtmlTestRunner.HTMLTestRunner(stream = outfile,title = 'Test Report',description = 'HMDC Test Report')
    runner.run(hmdc_tests)

if __name__=="__main__":
    main()