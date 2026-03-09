"""
Created on Feb 22, 2016

@author: jeffc
This test verifies EMBOSS data is being returned from the EMBOSS server.
@attention: need to update data between file and  wiki page. Need to find how to close file once data is inputted.
"""
import os.path
import sys
import time
import tracemalloc
import unittest

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from ddt import ddt, data, unpack
# from csv import reader
from config import PUBLIC_URL

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../config', )
)

# constants
SEQUENCE_URL = PUBLIC_URL + "/sequence/"

# Tests
tracemalloc.start()

class TestEmbossData(unittest.TestCase):

    def get_data(self, fileName):
        """
    	opens single column file at fileName
    	returns all lines as a list
    	"""
        with open(fileName, 'r') as f:
            return [line.strip() for line in f if line.strip()]

    def setUp(self):
        browser = os.getenv("BROWSER", "chrome").lower()

        if browser == "chrome":
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "firefox":
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == "edge":
            self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        self.driver.set_window_size(1500, 1000)
        self.driver.get(PUBLIC_URL)
        self.driver.implicitly_wait(10)

    def test_search(self):
        emboss_ids = self.get_data(
            os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'embossdata.txt')
        )

        wait = WebDriverWait(self.driver, 10)

        for entry in emboss_ids:
            with self.subTest(entry=entry):
                parts = entry.split(',')
                emboss_id = parts[0]
                chr_line = parts[1] if len(parts) > 1 else None

                self.driver.get(SEQUENCE_URL + emboss_id)

                go_button = wait.until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, 'form[name="seqPullDownForm"] input')
                    )
                )
                go_button.click()

                wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                page = self.driver.page_source

                if chr_line:
                    self.assertIn(chr_line, page)
                else:
                    self.assertIn(emboss_id, page)
                    self.assertNotIn("An error occurred", page)


def tearDown(self):
    self.driver.quit()
    tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEmbossData))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\\WebdriverTests'))
