'''
Created on Nov 3, 2017 -- used HMDC_tests.py as the template

@author: jlewis  
'''
import unittest
from .gxdindex_add_delete_test import TestAdd
from .gxdindex_clear_test import TestClear
from .gxdindex_modify_test import TestModify
from .gxdindex_notes_picklist_test import TestNotes
from .gxdindex_search_test import TestSearch
from .gxdindex_shortcuts_test import TestShort

import os
import HtmlTestRunner
# from EI import gxdindex_add_delete_test, gxdindex_clear_test, gxdindex_modify_test, gxdindex_notes_picklist_test, gxdindex_search_test, gxdindex_shortcuts_test


def main():
    gxdindex_add_delete_test = unittest.TestLoader().loadTestsFromTestCase(TestAdd)
    gxdindex_clear_test = unittest.TestLoader().loadTestsFromTestCase(TestClear)
    gxdindex_modify_test = unittest.TestLoader().loadTestsFromTestCase(TestModify)
    gxdindex_notes_picklist_test = unittest.TestLoader().loadTestsFromTestCase(TestNotes)
    gxdindex_search_test = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    gxdindex_shortcuts_test = unittest.TestLoader().loadTestsFromTestCase(TestShort)

#Put them in an Array
    gxdindex_tests = unittest.TestSuite([gxdindex_add_delete_test, gxdindex_clear_test, gxdindex_modify_test, gxdindex_notes_picklist_test, gxdindex_search_test, gxdindex_shortcuts_test])
#file
    dir = os.getcwd()
    outfile = open(r"C:\WebdriverTests\GXDINDEXtestreport.html", "w")
    runner = HtmlTestRunner.HTMLTestRunner(stream = outfile,title = 'Test Report',description = 'GXDINDEX Test Report')
    runner.run(gxdindex_tests)

if __name__=="__main__":
    main()