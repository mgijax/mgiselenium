"""
Functions for dealing with "waiting" in selenium

    These define different ways to explicitly wait for some behavior
    or browser state
    before continuing execution.
"""

from selenium.webdriver.support.ui import WebDriverWait


def forAjax(driver, seconds=10):
    """
    Wait for all AJAX calls to complete.
    
    NOTE: only checks status of jQuery AJAX requests
    """
    
    def _ajaxCheck(driver):
        return driver.execute_script("return jQuery.active==0")
    
    WebDriverWait(driver, seconds).until(_ajaxCheck)
    