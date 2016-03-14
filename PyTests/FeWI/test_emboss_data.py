'''
Created on Feb 22, 2016

@author: jeffc
A work in progress, bringing back data but now need to figure how to apply it.
'''
import csv, unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ddt import ddt, data, unpack
from pkgutil import get_data
#from csv import reader
from config.config import PUBLIC_URL
@ddt
class TestFile(unittest.TestCase):


    def get_data(self, file_name):
        #get_data("embossdata.txt")
        #create an empty list to store rows
        rows = []
        #open the text file
        data_file = open(file_name, "rb")
        reader = csv.reader(data_file)
        next(reader, None)
        for row in reader:
            rows.append(row)
        return rows
        #print rows
    
        
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(PUBLIC_URL)
        self.driver.implicitly_wait(10)
        
    @data(get_data("mgiselenium/data/", "../../data/embossdata.txt"))
    @unpack
    def test_search(self, search_value):
        self.search_field = self.driver.find_element_by_id("searchToolTextArea")
        self.search_field.clear()
        self.search_field.send_keys("search_value")
        self.search_field.send_keys(Keys.RETURN)
     
        
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()