"""
Base class for all EMAPA tests
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)

from configparser import SafeConfigParser
from util import iterate, wait
import time



class EmapaBaseClass(object):
    """
    define base methods for all EMAPA unit tests
    """
    
    def init(self):
        parser = SafeConfigParser()
        parser.read("..\..\..\config\config.ini")
        base_url = parser.get('testpwi', 'url')
        print('>>>', base_url)
        # constants
        BROWSER_URL = base_url + "/edit/emapaBrowser"
        self.driver = webdriver.Chrome()
        self.driver.get(BROWSER_URL)
        self.driver.implicitly_wait(10)
    
    def closeAllWindows(self):
        """
        close all open windows for the current driver
        """
        for window_handle in self.driver.window_handles:
            self.driver.switch_to.window(window_handle)
            self.driver.close()
            
            
    def performSearch(self, 
                      term="", 
                      stage=""):
        """
        Submit the EMAPA search form
           with the supplied parameters
        """
        
        termSearch = self.driver.find_element(By.ID, "termSearch")
        termSearch.clear()
        termSearch.send_keys(term)
        
        stageSearch = self.driver.find_element(By.ID, "stageSearch")
        stageSearch.clear()
        stageSearch.send_keys(stage)
        
        stageSearch.send_keys(Keys.RETURN)
        
        # wait for all AJAX behavior to complete
        wait.forAngular(self.driver)
        