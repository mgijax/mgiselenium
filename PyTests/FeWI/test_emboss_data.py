'''
Created on Feb 22, 2016

@author: jeffc
This test verifies EMBOSS data is being returned from the EMBOSS server.
@attention: need to update data between file and  wiki page. Need to find how to close file once data is inputted.
'''
import unittest
import tracemalloc
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from ddt import ddt, data, unpack
from pkgutil import get_data
#from csv import reader
import time
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../config',)
)

from config import PUBLIC_URL

### constants ###
SEQUENCE_URL = PUBLIC_URL + "/sequence/"

#Tests
tracemalloc.start()
class TestEmbossData(unittest.TestCase):


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
        #self.driver = webdriver.Chrome('C:/Users/testuser/Downloads/chromedriver')
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get(PUBLIC_URL)
        self.driver.implicitly_wait(10)
        
    def test_search(self):
    
        embossIds = self.get_data(
                os.path.join(os.path.dirname(__file__), 
                '..', '..', 'data','embossdata.txt')
        )
        print(embossIds)
    
        for embossId in embossIds:
            chrLine = None
            parts = embossId.split(',')
            if len(parts) > 1:
                embossId = parts[0]
                chrLine = parts[1]
    
            self.driver.get(SEQUENCE_URL + embossId)
            time.sleep(2)
            goButton = self.driver.find_element(By.CSS_SELECTOR, "form[name=\"seqPullDownForm\"] input")
            goButton.click()
            time.sleep(2)
            if chrLine:
                self.assertIn(chrLine, self.driver.page_source)
            else:
                try:
                    self.assertNotIn("An error occurred", self.driver.page_source)
                except:
                    print(embossId + ' ID has an error.')
                    pass
                self.assertIn(embossId, self.driver.page_source)
                
    
    
        
    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEmbossData))
    return suite

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))
