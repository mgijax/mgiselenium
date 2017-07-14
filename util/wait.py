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



def forAngular(driver, seconds=20):

    def _angularCheck(driver):
        script = """var callback = arguments[arguments.length - 1];
            var el = document.querySelector('body');
            if (!window.angular) {
                callback(false);
            }
            if (angular.getTestability) {
                angular.getTestability(el).whenStable(function(){callback(true)});
            } else {
                if (!angular.element(el).injector()) {
                    callback(false);
                }
                var browser = angular.element(el).injector().get('$browser');
                browser.notifyWhenNoOutstandingRequests(function(){callback(true)});
            };"""
        
        try:
            return driver.execute_async_script(script)
        except:
            return False
        
    # Define driver and timeout,
    # then use the condition like so:
    WebDriverWait(driver, 20).until(_angularCheck)



def forAjax(driver, seconds=10):
    """
    Wait for all AJAX calls to complete.
    """
    
    
    def _ajaxCheck(driver):
        openConnections = driver.execute_script("return window.openHTTPs")
        
        # check if we need to apply patch
        if openConnections == None:
                # apply javascript patch and try once more
                _applyAjaxPatch(driver)
                openConnections = driver.execute_script("return window.openHTTPs")
        
                # return false if patch didn't work this time
                if openConnections == None:
                        return False
        
        return openConnections == 0
        
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
    
    
### helper functions ###
def _applyAjaxPatch(driver):
        """
        Apply a javascript patch to detect open ajax requests
        """
        
        # override XHR prototype to log when requests open/close
        #   so we can inspect window.openHTTPs counter
        patchScript = """
        (function() {
          var oldOpen = XMLHttpRequest.prototype.open;
          window.openHTTPs = 0;
          XMLHttpRequest.prototype.open = function(method, url, async, user, pass) {
            window.openHTTPs += 1;
            this.addEventListener('readystatechange', function() {
              if(this.readyState == 4) {
                window.openHTTPs -= 1;
              }
            }, false);
            oldOpen.call(this, method, url, async, user, pass);
          } 
        })();
        """
        
        driver.execute_script(patchScript)
    