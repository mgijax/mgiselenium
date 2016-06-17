'''
Created on Feb 22, 2016

@author: jeffc
A work in progress, bringing back data and verifies some, problem is some results have no ID in results, like nib files so need to
figure out how to handle these.
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from ddt import ddt, data, unpack
from pkgutil import get_data
#from csv import reader

import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)

from config import PUBLIC_URL

### constants ###
SEQUENCE_URL = PUBLIC_URL + "/sequence/"


class TestFile(unittest.TestCase):


    def get_data(self, fileName):
        """
    	opens single column file at fileName
    	returns all lines as a list
    	"""
        f = open(fileName, 'r')
        lines = []
        for line in f.readlines():
            line = line.strip()
            lines.append(line)
        
        return lines
        
    
        
    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.get(PUBLIC_URL)
        self.driver.implicitly_wait(10)
        
    def test_search(self):
    
        embossIds = self.get_data(os.path.join('../../data','embossdata.txt'))
        print embossIds
    
        for embossId in embossIds:
    
            self.driver.get(SEQUENCE_URL + embossId)
    
            goButton = self.driver.find_element_by_css_selector("form[name=\"seqPullDownForm\"] input")
            goButton.click()
    
            self.assertIn(embossId, self.driver.page_source)
    
    
        
    def tearDown(self):
        self.driver.close()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFile))
    return suite


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
