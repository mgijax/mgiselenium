'''
Created on Jan 28, 2016
This test verifies searching within the EmapA module, Both a term search and a stage search
Add'l 4 tests added August 2016; jlewis
all tests verified to work 6/9/2023
@author: jeffc
'''
import unittest
import tracemalloc
import time
import config
import sys, os.path
# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table

# Tests
tracemalloc.start()
class TestEiEmapaSearch(unittest.TestCase):
    """
    @status Test EMAPA browser search using terms, stages, synonymns
    """

    def setUp(self):
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(1500, 1000)
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/emapaBrowser")
        # logging in for all tests
        username = self.driver.find_element(By.NAME, 'user')  # finds the user login box
        username.send_keys(config.PWI_LOGIN)  # enters the username
        passwd = self.driver.find_element(By.NAME, 'password')  # finds the password box
        passwd.send_keys(config.PWI_PASSWORD)  # enters a valid password
        submit = self.driver.find_element(By.NAME, "submit")  # Find the Login button
        submit.click()  # click the login button
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()
        tracemalloc.stop()

    def testBasicSearch(self):
        """
        tests that a basic term search works
        """
        driver = self.driver
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term brain
        self.driver.find_element(By.ID, "termSearch").send_keys('brain')
        wait.forAngular(self.driver)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'stageList')))  # waits until the PWI stagelist field is displayed on the page
        term_result = self.driver.find_element(By.ID, "termResultList")
        items = term_result.find_elements(By.TAG_NAME, "li")

        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)

        self.assertIn('brain TS17-28', searchTextItems)

    def testSynonymSearch(self):
        """
        tests that a synonym term search works
        """
        driver = self.driver
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term myocardium
        self.driver.find_element(By.ID, "termSearch").send_keys('myocardium')
        wait.forAngular(self.driver)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'stageList')))  # waits until the PWI stagelist field is displayed on the page
        term_result = self.driver.find_element(By.ID, "emapTermArea")
        items = term_result.find_elements(By.TAG_NAME, "li")

        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)

        self.assertIn('cardiac muscle tissue TS12-28 (myocardium)', searchTextItems)

    def testWildcardSearch(self):
        """
        tests that a wildcard term search works
        """
        driver = self.driver
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term %tectum
        self.driver.find_element(By.ID, "termSearch").send_keys('%tectum')
        wait.forAngular(self.driver)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'stageList')))  # waits until the PWI stagelist field is displayed on the page
        term_result = self.driver.find_element(By.ID, "termResultList")
        items = term_result.find_elements(By.TAG_NAME, "li")

        # add all li text to a list for "assertIn" test
        searchTextTerms = self.getOnlyTermNames(items)

        self.assertIn('pretectum', searchTextTerms)
        self.assertIn('tectum', searchTextTerms)

    def testStageSearch(self):
        """
        tests that a stage search works
        """
        driver = self.driver
        wait.forAngular(self.driver)
        # find the "Stage Search" box and enter the stage "10"
        self.driver.find_element(By.ID, "stageSearch").send_keys('10')
        wait.forAngular(self.driver)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'stageList')))  # waits until the PWI stagelist field is displayed on the page
        term_result = self.driver.find_element(By.ID, "emapTermArea")
        items = term_result.find_elements(By.TAG_NAME, "li")

        # add all li text to a list for "assertIn" test
        searchTextTerms = self.getOnlyTermNames(items)

        # verify term that exists at 10 or beyond
        self.assertIn('allantois', searchTextTerms)

        # verify term that only exists at 10
        self.assertIn('amniotic fold ectoderm', searchTextTerms)

    def testMultipleStageSearch(self):
        """
        tests that a multiple stages search works.
        """
        driver = self.driver
        wait.forAngular(self.driver)
        # find the "Stage Search" box and enter the stages "10,11,12"
        self.driver.find_element(By.ID, "stageSearch").send_keys('10,11,12')
        wait.forAngular(self.driver)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'stageList')))  # waits until the PWI stagelist field is displayed on the page
        term_result = self.driver.find_element(By.ID, "emapTermArea")
        items = term_result.find_elements(By.TAG_NAME, "li")

        # add all li text to a list for "assertIn" test
        searchTextTerms = self.getOnlyTermNames(items)

        # verify term that exists at one, but not all the three stages
        self.assertIn('1st branchial arch', searchTextTerms)

        # verify term that exists at all stages entered
        self.assertIn('amniotic cavity', searchTextTerms)

    def testTermShortcut(self):
        """
        tests that the shortcut ALT + c clears the term and stage fields
        """
        driver = self.driver
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term brain
        self.driver.find_element(By.ID, "termSearch").send_keys('brain')
        # find the "Stage Search" box and enter the stages "20,21,22"
        self.driver.find_element(By.ID, "stageSearch").send_keys('20,21,22')
        wait.forAngular(self.driver)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'stageList')))  # waits until the PWI stagelist field is displayed on the page
        term_result = self.driver.find_element(By.ID, "termResultList")
        items = term_result.find_elements(By.TAG_NAME, "li")

        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)

        self.assertIn('brain TS17-28', searchTextItems)
        searchbox = self.driver.find_element(By.ID, "termSearch")
        searchbox.text
        self.assertIn("brain", searchbox.get_attribute("value"))
        searchbox.send_keys(Keys.ALT + "c")
        self.assertIn("", searchbox.get_attribute("value"))

    def testComboTermStageSearch(self):
        """
        tests that a combined search of term and stage works; also includes wild cards; jlewis
        """
        driver = self.driver
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term %renal artery%
        self.driver.find_element(By.ID, "termSearch").send_keys('%renal artery%')
        # find the "Stage Search" box and enter the stage "27"
        self.driver.find_element(By.ID, "stageSearch").send_keys('27')
        wait.forAngular(self.driver)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'stageList')))  # waits until the PWI stagelist field is displayed on the page
        term_result = self.driver.find_element(By.ID, "termResultList")
        items = term_result.find_elements(By.TAG_NAME, "li")

        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)

        self.assertIn('endothelium of renal artery TS21-28', searchTextItems)

    def testSpecialCharSearch(self):
        """
        tests that a term with a special character works; jlewis
        """
        driver = self.driver
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term rathke's pouch
        self.driver.find_element(By.ID, "termSearch").send_keys("rathke's pouch")
        wait.forAngular(self.driver)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'stageList')))  # waits until the PWI stagelist field is displayed on the page
        term_result = self.driver.find_element(By.ID, "emapTermArea")
        items = term_result.find_elements(By.TAG_NAME, "li")

        # add all li text to a list for "assertIn" test
        searchTextItems = iterate.getTextAsList(items)

        self.assertIn("Rathke's pouch TS14-19", searchTextItems)

    def testMultipleTermSearch(self):
        """
        tests that a search with multiple terms works; semi-colon is the delimiter; jlewis
        """
        driver = self.driver
        wait.forAngular(self.driver)
        # find the "Term Search" box and enter the term "liver; brain; heart"
        self.driver.find_element(By.ID, "termSearch").send_keys("liver; brain; heart")
        wait.forAngular(self.driver)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'stageList')))  # waits until the PWI stagelist field is displayed on the page
        term_result = self.driver.find_element(By.ID, "termResultList")
        items = term_result.find_elements(By.TAG_NAME, "li")

        # add all li text to a list for "assertIn" test
        searchTextTerms = self.getOnlyTermNames(items)

        self.assertIn('brain', searchTextTerms)
        self.assertIn('heart', searchTextTerms)
        self.assertIn('liver', searchTextTerms)

    def testStageRangeSearch(self):
        """
        tests that a search for a range of stages works; jlewis
        """
        driver = self.driver
        wait.forAngular(self.driver)
        # find the "Stage Search" box and enter the stages "1-3"
        self.driver.find_element(By.ID, "stageSearch").send_keys("1-3")
        wait.forAngular(self.driver)
        # find the Search button and click it
        self.driver.find_element(By.CSS_SELECTOR, '#termSearchForm > input:nth-child(1)').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'stageList')))  # waits until the PWI stagelist field is displayed on the page
        term_result = self.driver.find_element(By.ID, "emapTermArea")
        items = term_result.find_elements(By.TAG_NAME, "li")

        # add all li text to a list for "assertIn" test
        searchTextTerms = self.getOnlyTermNames(items)

        # verify term that exists only at stage 1
        self.assertIn('first polar body', searchTextTerms)

        # verify term that only exists at stage 2
        self.assertIn('2-cell stage conceptus', searchTextTerms)

        # verify term that only exists at stage 3
        self.assertIn('8-cell stage embryo', searchTextTerms)

    def getOnlyTermNames(self, elements):
        """
        Returns text strings from each element,
            but only includes the term name, not the TS range or synonyms
        """

        terms = []
        for element in elements:
            # term is the first section before TS range
            term = element.text.split(" TS")[0]
            terms.append(term)

        return terms


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiEmapaSearch))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='C:\WebdriverTests'))