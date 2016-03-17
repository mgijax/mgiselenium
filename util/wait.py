"""
Functions for dealing with "waiting" in selenium

    These define different ways to explicitly wait for some behavior
    or browser state
    before continuing execution.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def forAjax(driver, seconds=10):
    """
    Wait for all AJAX calls to complete.
    
    NOTE: only checks status of jQuery AJAX requests
    """
    
    def _ajaxCheck(driver):
        return driver.execute_script("return jQuery.active==0")
    
    WebDriverWait(driver, seconds).until(_ajaxCheck)
    
    
def forNewWindow(driver, timeout=10):
    """
    Wait for browser to open new window
        resulting from a link click
        
    stops waiting after timeout seconds
    
    NOTE: new window content must have a body tag
    NOTE: Uses pre-defined implicit_wait setting for selenium
        when waiting for content to load on new window
    """
    
    while timeout > 0:
        
        if len(driver.window_handles) < 2:
            continue
        else:
            break
        
        # wait for 1 second
        time.sleep(1)
        timeout -= 1
    
    # exit if there is no new window to navigate to
    if len(driver.window_handles) < 2:
        return
    
    # switch window
    driver.switch_to_window(driver.window_handles[-1])
    
    # use remaining timeout to wait for content to load in new window
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    
    