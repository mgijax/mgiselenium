"""
Created on Apr 25, 2019
This set of tests is for the Cell Ontology autocomplete list of the Cell Ontology query form
@author: jeffc
Verify the auto complete list is displaying the correct cell ontology structures associated to the text you entered
Verify
"""
import unittest
import time
import tracemalloc
import config
import sys, os.path

from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from lib import *
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)

# Tests
tracemalloc.start()


class TestGxdCellOntologyAutocomplete(unittest.TestCase):

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
        self.driver.get(config.TEST_URL + "/vocab/cell_ontology/")
        self.driver.implicitly_wait(10)

    def test_index_structureAC_headers(self):
        """
        @status this test verifies the auto complete list is displaying the correct cell ontology structures associated to the text you entered.
        @see GXD-RNASeq-search-1
        """
        print("BEGIN test_structureAC_headers")
        self.driver.find_element(By.ID, 'searchTerm').send_keys(
            'cell')  # identifies the cell ontology field and enters text
        # wait.forAngular(self.driver)
        # time.sleep(2)
        # identify the autocomplete dropdown list
        auto_list = self.driver.find_element(By.ID, "eac-container-searchTerm")
        items = auto_list.find_elements(By.TAG_NAME, "li")
        for item in items:
            text = item.text
            print(text)
        self.assertEqual(items[0].text, "cell", "Term 0 is not visible!")
        self.assertEqual(items[1].text, "cell in vitro", "Term 1 is not visible!")
        self.assertEqual(items[2].text, "cell of Claudius [synonym]", "Term 2 is not visible!")
        self.assertEqual(items[3].text, "cell of Hensen [synonym]", "Term 3 is not visible!")
        self.assertEqual(items[4].text, "cell of Rouget [synonym]", "Term 4 is not visible!")
        self.assertEqual(items[5].text, "cell of epidermis [synonym]", "Term 5 is not visible!")
        self.assertEqual(items[6].text, "cell of skeletal muscle", "Term 6 is not visible!")
        self.assertEqual(items[7].text, "cell of surface ectoderm [synonym]", "Term 7 is not visible!")
        self.assertEqual(items[8].text, "5-HT secreting cell [synonym]", "Term 8 is not visible!")
        self.assertEqual(items[9].text, "5-Hydroxytryptamine secreting cell [synonym]", "Term 9 is not visible!")
        self.assertEqual(items[10].text, "A Horizontal Cell [synonym]", "Term 10 is not visible!")
        self.assertEqual(items[11].text, "A2 amacrine cell", "Term 11 is not visible!")
        self.assertEqual(items[12].text, "A2-like amacrine cell", "Term 12 is not visible!")
        self.assertEqual(items[13].text, "A7 cell (Mus musculus) [synonym]", "Term 13 is not visible!")
        self.assertEqual(items[14].text, "AB cell [synonym]", "Term 14 is not visible!")
        self.assertEqual(items[15].text, "AB broad diffuse-1 amacrine cell", "Term 15 is not visible!")

    def tearDown(self):
        self.driver.close()
        tracemalloc.stop()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGxdCellOntologyAutocomplete))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\\WebdriverTests'))