'''
Created on Feb 15, 2016

@author: jeffc
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://scrumdog.informatics.jax.org/pwi/edit/emapBrowser")
        self.driver.implicitly_wait(1)

    def testDefaultDetail(self):
        searchbox = self.driver.find_element_by_id("termSearch")
        searchbox.send_keys("%cort%")
        searchbox.send_keys(Keys.RETURN)
        
        term_result = self.driver.find_element_by_id("termResultList")
        items = term_result.find_elements_by_tag_name("li")
        searchTextItems = self.getSearchTextAsList(items)
        self.assertEqual(searchTextItems[0], "adrenal cortex TS22-28")
        
        term_det = self.driver.find_element_by_id("termDetailContent")
        item = term_det.find_elements_by_tag_name("dd")
        searchTermItems = self.getTermDetailTextAsList(item)
        self.assertEqual(searchTermItems[0], "adrenal cortex")
        self.assertEqual(searchTermItems[1], "Theiler Stages 22-28")
        self.assertEqual(searchTermItems[2], "EMAPA:18427")
        self.assertEqual(searchTermItems[3], "adrenal gland cortex")
        self.assertEqual(searchTermItems[4], "part-of adrenal gland")

    def getSearchTextAsList(self, liItems):
        """
        Take all found li tags in liItems
            and return a list of all the text values
            for each li tag (search result section)
        """
        searchTextItems = []
        for item in liItems:
            text = item.text
            searchTextItems.append(item.text)
            
        print "li text = %s" % searchTextItems
        return searchTextItems
    
    def getTermDetailTextAsList(self, ddItem):            
        """
        Take all found dd tags in ddItem 
            and return a list of all the text values 
            for each dd tag (term detail section)
        """
        searchTermItems = []
        for item in ddItem:
            text = item.text
            searchTermItems.append(item.text)
            
        print "dd text = %s" % searchTermItems
        return searchTermItems


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()