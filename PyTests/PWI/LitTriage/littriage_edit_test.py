'''
Created on Sep 7, 2017
These tests are to confirm results you get back using various edit requirements
@author: jeffc
@attention: Do not use these tests against a production system! Since you are editing it will cause  data to be changed
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import HtmlTestRunner
import sys, os.path
from selenium.webdriver.support.wait import WebDriverWait

# adjust the path to find config
sys.path.append(
    os.path.join(os.path.dirname(__file__), '../../..', )
)
import config
from util import iterate, wait
from util.form import ModuleForm
from util.table import Table


# Tests

class TestEiLitTriageEdit(unittest.TestCase):
    """
    @status Test Literature Triage editing features
    """

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.form = ModuleForm(self.driver)
        self.form.get_module(config.TEST_PWI_URL + "/edit/triageFull")
        username = self.driver.find_element(By.NAME, 'user')  # finds the user login box
        username.send_keys(config.PWI_LOGIN)  # enters the username
        passwd = self.driver.find_element(By.NAME, 'password')  # finds the password box
        passwd.send_keys(config.PWI_PASSWORD)  # enters a valid password
        submit = self.driver.find_element(By.NAME, "submit")  # Find the Login button
        submit.click()  # click the login button

    def tearDown(self):
        self.driver.close()

    def testRefStatusEdit(self):
        """
        @Status tests that changing a "not routed" reference to "chosen" assigns it a J number
        @attention: This test works but once you have changed it to chosen the J number will always be present
        @see LitTri-edit-1,2 (1) consider getting rid of this test, currently broken 11/18/2021
        """
        # enter text into the authors filed,click the alleles Not Routed box then search
        self.driver.find_element(By.ID, 'authors').send_keys('Baran%')
        self.driver.find_element(By.ID, 'status_AP_Not_Routed').click()
        self.driver.find_element(By.ID, 'searchButton').click()
        # time.sleep(5)
        # wait until the Pubmed ID of the first row is visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#resultsTable > tbody > tr > td:nth-child(4) > div > a")))
        # finds the results table and then the first pubmed ID field(text)
        table_element = self.driver.find_element(By.ID, "resultsTable")
        link_element = table_element.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(4) > div > a')
        txt = link_element.get_attribute('innerHTML')
        # finds the AP column and confirm it is Not Routed
        not_route = table_element.find_element(By.CSS_SELECTOR, 'tbody > tr > td:nth-child(8)')
        # print not_route.text
        # assert the first row AP column is 'Not Routed'
        self.assertTrue(not_route.text, "Not Routed")
        # select the chosen status for AP
        table_element1 = self.driver.find_element(By.ID, 'editTabWorkFlowStatus')
        chosen = table_element1.find_element(By.CSS_SELECTOR, 'tbody>tr:nth-child(1)>td:nth-child(4)>input').click()
        # click the Modify button
        self.driver.find_element(By.ID, 'modifyEditTabButton').click()
        # Verifies Chosen status is selected for AP now in the table
        chosen1 = self.driver.find_element(By.NAME, '90')
        self.assertTrue(chosen1.is_selected())
        print(chosen1.text)
        # select the not routed status for AP tp put the data back to normal
        table_element1 = self.driver.find_element(By.ID, 'editTabWorkFlowStatus')
        norouted = table_element1.find_element(By.CSS_SELECTOR, 'tbody>tr:nth-child(1)>td:nth-child(2)>input').click()

    def testReftypeEdit(self):
        """
        @Status tests the modifying of a Reference Type by using the pulldown list
        @see LitTri-edit-4 (9), LitTri-edit-32 (47)
        """
        # driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:15839')
        form.click_search()
        # finds the Reference Type field and return it's text value
        ref_type = self.driver.find_element(By.ID, "editTabRefType").get_attribute('value')
        print(ref_type)
        self.assertEqual(ref_type, '31576686')  # 31576686 = MGI Curation Record
        # finds the Reference type field and modify its value
        select = Select(self.driver.find_element(By.ID, "editTabRefType"))
        select.select_by_visible_text('Unreviewed Article')
        # presses the Tab key
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
        # click the Modify button
        self.driver.find_element(By.ID, 'modifyEditTabButton').click()
        # finds the Reference Type field and return it's text value
        ref_type = self.driver.find_element(By.ID, "editTabRefType").get_attribute('value')
        self.assertEqual(ref_type, '31576689')  # 31576689 = Unreviewed Article
        # finds the Reference type field and modify its value
        select = Select(self.driver.find_element(By.ID, "editTabRefType"))
        select.select_by_visible_text('MGI Curation Record')
        # click the Modify button to set the Reference Type back to MGI Curation Record.
        self.driver.find_element(By.ID, 'modifyEditTabButton').click()

    def testDiscardEdit(self):
        """
        @Status tests the setting of the MGI Discard flag
        @see LitTri-edit-21 (27)
        """
        form = self.form
        time.sleep(5)
        form.enter_value('accids', 'J:32887')
        form.click_search()
        discard = self.driver.find_element(By.XPATH,
                                           "/html/body/main/div/div/form/div/div[2]/div/div/div[2]/div/input[2]")
        self.assertFalse(discard.is_selected())
        # finds the MGI Discard box and checks it
        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div/div/form/div/div[2]/div/div/div[2]/div/input[2]").click()
        # find the MGI Discard box and check it's selected
        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div/div/form/div/div[2]/div/div/div[2]/div/input[2]").is_selected()
        # click the Modify button
        self.driver.find_element(By.ID, 'modifyEditTabButton').click()
        # find the MGI Discard box and check it's selected
        self.driver.find_element(By.XPATH,
                                 "/html/body/main/div/div/form/div/div[2]/div/div/div[2]/div/input[2]").is_selected()

    def testAddTagEdit(self):
        """
        @Status tests that you can add a tag using the autocomplete option
        @see LitTri-edit-22, 23
        """
        # driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:22341')
        form.click_search()

        # finds the tag field
        self.driver.find_element(By.ID, "tags").send_keys("MGI:CorrectionAdded")
        # find and click the Associate button
        self.driver.find_element(By.ID, "saveTagButton").click()
        wait.forAngular(self.driver)
        # finds the Tag list and verifies the required tag is listed.
        table_element = self.driver.find_element(By.ID, "editTabTags")
        table = Table(table_element)
        # finds the selected tags column and verified it contains the added tag
        sel_tags = table.get_column_cells(1)
        used_tags = iterate.getTextAsList(sel_tags)
        print(used_tags)
        # asserts that the following J numbers are returned
        self.assertIn('MGI:CorrectionAdded', used_tags)

    def testSupplementalEdit(self):
        """
        @Status tests that you can change the Supplemental field option
        @see LitTri-edit-22, 23
        """
        # driver = self.driver
        form = self.form
        form.enter_value('accids', 'J:269580')
        form.click_search()

        # finds the supplemental field and selects the option Supplement attached
        Select(self.driver.find_element(By.ID, "editTabSuppData")).select_by_value('34026997')
        wait.forAngular(self.driver)
        # find and click the Modify button
        self.driver.find_element(By.ID, "modifyEditTabButton").click()
        wait.forAngular(self.driver)
        # finds the Supplemental and verifies the correct option is selected.
        supp = self.driver.find_element(By.ID, "editTabSuppData").get_attribute('value')
        print(supp)
        # asserts that the following J numbers are returned
        self.assertEqual(supp, '34026997', 'The wrong supplemental is displayed!')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEiLitTriageEdit))
    return suite


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\WebdriverTests'))