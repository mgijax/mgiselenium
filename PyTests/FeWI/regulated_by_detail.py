"""
Created on Feb 24, 2025
@author: jeffc
Verify opens the Regulates by  table and verifies it is sorted correctly by distance from the marker
"""
import os.path
import sys
import tracemalloc
import unittest
import config

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from util.table import Table

# from genericpath import exists
# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)
chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability("browserVersion", "latest")
chrome_options.set_capability("platformName", "win10")
# Test
tracemalloc.start()


class TestTssDetail(unittest.TestCase):

    def setUp(self):
        browser = getattr(config, "BROWSER", "chrome").lower()
        if browser == "chrome":
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "firefox":
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == "edge":
            self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        self.driver.set_window_size(1500, 1000)
        self.driver.get(config.TEST_URL + "/marker/")
        self.driver.implicitly_wait(10)

    def test_regulates_by_table(self):
        """
        @status this test opens the regulates by table and verifies it is sorted correctly by distance from the marker.
        @note
        @note regby-sum-?
        """
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Cd8a")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Cd8a').click()
        # Click the link for the regulatory regions popup table
        self.driver.find_element(By.ID, 'showRegulatingMarkers').click()
        tss_table = self.driver.find_element(By.ID, 'regulatingMarkersTable')
        table = Table(tss_table)
        # Capture each row of the TSS table(only the first 5 rows)
        cells1 = table.get_row(1)
        cells2 = table.get_row(2)
        cells3 = table.get_row(3)
        cells4 = table.get_row(4)
        print(cells1.text)
        # Verify the TSS table locations are correct and in the correct order.
        self.assertEqual(cells1.text, 'Rr7, regulatory region 7 locus control region Chr6, Syntenic J:164573')
        self.assertEqual(cells2.text, 'Rr98, regulatory region 98 enhancer Chr6, Syntenic J:113136')
        self.assertEqual(cells3.text, 'Rr99, regulatory region 99 enhancer Chr6, Syntenic J:50624')
        self.assertEqual(cells4.text, 'Rr100, regulatory region 100 enhancer Chr6, Syntenic J:113136')

    def test_regulates_by_display(self):
        """
        @status this test displays a marker detail page and verifies the Regulates data displays between transcription sites and candidate for QTL.
        @note
        @note regby-sum-?
        """
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Ets1")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Ets1').click()
        # find the second section of the Summary section
        hds = self.driver.find_element(By.CLASS_NAME, 'summarySec2').find_elements(By.CLASS_NAME, 'label')
        print(hds[3].text)
        print(hds[4].text)
        print(hds[5].text)
        self.assertEqual(hds[3].text, 'Transcription Start Sites')
        self.assertEqual(hds[4].text, 'Regulated by')
        self.assertEqual(hds[5].text, 'Candidate for QTL')

    def test_regulates_by_display_1_region(self):
        """
        @status this test displays a marker detail page and verifies the Regulated by field when only 1 region.
        @note
        @note regby-sum-?
        """
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Bmp4")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Bmp4').click()
        # find the second section of the Summary section
        reg = self.driver.find_element(By.CSS_SELECTOR, 'section.summarySec2:nth-child(2) > ul:nth-child(1) > li:nth-child(5)')
        print(reg.text)
        self.assertEqual(reg.text, 'Regulated by\nRr16 (1 regulatory region)')

    def test_regulates_by_display_2plus_regions(self):
        """
        @status this test displays a marker detail page and verifies the Regulated by field when 2 or more regions.
        @note
        @note regby-sum-?
        """
        self.driver.find_element(By.NAME, 'nomen').clear()
        self.driver.find_element(By.NAME, 'nomen').send_keys("Hoxb4")
        self.driver.find_element(By.CLASS_NAME, 'buttonLabel').click()
        self.driver.find_element(By.LINK_TEXT, 'Hoxb4').click()
        # find the second section of the Summary section
        reg = self.driver.find_element(By.CSS_SELECTOR, 'section.summarySec2:nth-child(2) > ul:nth-child(1) > li:nth-child(6)')
        print(reg.text)
        self.assertEqual(reg.text, 'Regulated by\nRr6, Rr5, Rr577 ... (4 regulatory regions)')


    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTssDetail))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\\WebdriverTests'))