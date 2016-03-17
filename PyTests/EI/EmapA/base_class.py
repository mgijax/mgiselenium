"""
Base class for all EMAPA tests
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys,os.path
# adjust the path to find config
sys.path.append(
  os.path.join(os.path.dirname(__file__), '../../..',)
)
import config
from util import iterate, wait

# constants
BROWSER_URL = config.PWI_URL + "/edit/emapaBrowser"

class EmapaBaseClass(object):
    """
    define base methods for all EMAPA unit tests
    """
    
    def init(self):
        self.driver = webdriver.Firefox()
        self.driver.get(BROWSER_URL)
        self.driver.implicitly_wait(10)
    
    def closeAllWindows(self):
        """
        close all open windows for the current driver
        """
        for window_handle in self.driver.window_handles:
            self.driver.switch_to_window(window_handle)
            self.driver.close()
            
            
    def performSearch(self, 
                      term="", 
                      stage=""):
        """
        Submit the EMAPA search form
           with the supplied parameters
        """
        
        termSearch = self.driver.find_element_by_id("termSearch")
        termSearch.send_keys(term)
            
        stageSearch = self.driver.find_element_by_id("stageSearch")
        stageSearch.send_keys(stage)
        
        stageSearch.send_keys(Keys.RETURN)
        
        # wait for all AJAX behavior to complete
        wait.forAjax(self.driver)
        