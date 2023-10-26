'''
Created on Jun 12, 2018
This utility allows you to highlight an element for a set period of time using the basis setup of
example: self.highlight(driver.find_element(By.ID, 'element_name'))
@author: jeffc
'''
# filename: highlight_elements.py
import unittest
import tracemalloc
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

tracemalloc.start()
class HighlightElements(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

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
