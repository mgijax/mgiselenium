'''
Created on Nov 23, 2016
This is just an example of how to run a suite of tests from one python file.
@author: jeffc
'''
import unittest
import tracemalloc
import os
from jd_HTMLTestRunner import HTMLTestRunner
from .test_search_tool import TestSearchTool
from .test_snp_build_numbers import TestSnpBuild
from .test_private_data import TestPrivateData


tracemalloc.start()
def main():
    searchtool_test = unittest.TestLoader().loadTestsFromTestCase(TestSearchTool)
    snpbuild_test = unittest.TestLoader().loadTestsFromTestCase(TestSnpBuild)
    private_data_test = unittest.TestLoader().loadTestsFromTestCase(TestPrivateData)
#Put them in an Array
    pwi_tests = unittest.TestSuite([searchtool_test, snpbuild_test, private_data_test])
#file
    dir = os.getcwd()
    outfile = open(dir + "PWItestreport.html", "w")
    runner = HTMLTestRunner(stream = outfile,title = 'Test Report',description = 'PWI Test Report')
    runner.run(pwi_tests)

if __name__=="__main__":
    main()