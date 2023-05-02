'''
Created on Jun 12, 2018

@author: jeffc
'''
# filename: highlight_elements.py
import unittest
import tracemalloc
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

tracemalloc.start()
class HighlightElements(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

# ...
    def highlight(self, element, duration=3):
        driver = self.driver

        # Store original style so it can be reset later
        original_style = element.get_attribute("style")

        # Style element with dashed red border
        driver.execute_script(
            "arguments[0].setAttribute(arguments[1], arguments[2])",
            element,
            "style",
            "border: 2px solid red; border-style: dashed;")

        # Keep element highlighted for a spell and then revert
        if (duration > 0):
            time.sleep(duration)
            driver.execute_script(
                "arguments[0].setAttribute(arguments[1], arguments[2])",
                element,
                "style",
                original_style)
# ...
    def test_example_1(self):
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/large')
        self.highlight(driver.find_element(By.ID, 'sibling-2.3'))

if __name__ == "__main__":
    unittest.main()
