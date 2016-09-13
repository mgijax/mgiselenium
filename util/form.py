"""
Helper for working with html forms
"""
from selenium.webdriver.common.keys import Keys
from util import wait

class ModuleForm(object):
    """
    Form page to represent a PWI module
    """
    
    def __init__(self, driver):
        self.driver = driver
        
        self.previous_element = None
        
        
    def get_module(self, url):
        self.driver.get(url)
        wait.forAngular(self.driver)
        
    
    def enter_value(self, id, value):
        """
        Sets value of input box
        """
        input = self.driver.find_element_by_id(id)
        
        input.send_keys(value)
        
        self.previous_element = input
        
        return input
    
    
    def press_enter(self):
        """
        press enter key on previous_element
        """
        current_element = self._get_current_element()
        current_element.send_keys(Keys.RETURN)
        wait.forAngular(self.driver)
        
        
    def press_tab(self):
        """
        press enter key on previous_element
        """
        current_element = self._get_current_element()
        current_element.send_keys(Keys.TAB)
        wait.forAngular(self.driver)
        
    
    def enter_shortcut(self, keys):
        """
        send keys to previous_element
        """
        current_element = self._get_current_element()
        current_element.send_keys(keys)
        wait.forAngular(self.driver)
    
    
    def _get_current_element(self):
        if self.previous_element:
            return self.previous_element
        return self.driver.find_element_by_tag_name("body")
    
    
    def get_value(self, id):
        """
        Retrieve the value of an input element
        """
        input = self.driver.find_element_by_id(id)
        
        return input.get_attribute("value")
    
    
    def get_selected_text(self, id):
        """
        Retrieve the text of the <select> element option
            that is currectly checked
        """
        option = self.driver.find_element_by_id(id) \
            .find_element_by_css_selector('#%s option:checked' % id)
        
        return option.text
    
    def get_error_message(self):
        """
        get the displayed error message
        """
        error_element = self.driver.find_element_by_id("errorMessage")
        return error_element.text
        
        
        
    # Standard EI buttons
    def click_search(self):  
        self.driver.find_element_by_id('searchButton').click()
        wait.forAngular(self.driver)
        
    def click_clear(self):  
        self.driver.find_element_by_id('clearButton').click()
        wait.forAngular(self.driver)
        
    def click_add(self):  
        self.driver.find_element_by_id('addButton').click()
        wait.forAngular(self.driver)
        
    def click_modify(self):  
        self.driver.find_element_by_id('modifyButton').click()
        wait.forAngular(self.driver)
        
    def click_delete(self):  
        self.driver.find_element_by_id('deleteButton').click()
        wait.forAngular(self.driver)
        
        
        
        
        